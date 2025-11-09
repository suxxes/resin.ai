#!/usr/bin/env python3
"""
Ping/Pong MCP Server for Claude Code Session Monitoring

Zero-dependency MCP server that monitors Claude Code sessions via hook-created files,
detects stale sessions using file mtime, and sends continuation prompts to revive them.
Uses only Python standard library - no external dependencies required.

Implements MCP (Model Context Protocol) JSON-RPC 2.0 over stdio.
Tools: list_sessions, configure, send_continuation

Features:
- Hook-based session tracking (ping-pong.sh creates/deletes session files on active events)
- File existence-based activity monitoring (file only exists when active work is happening)
- File mtime-based staleness detection (no polling overhead)
- Auto-discovery of sessions from $CLAUDE_PROJECT_DIR/.sessions/
- Direct tmux pane continuation prompt injection
- Zero external dependencies

Session files: $CLAUDE_PROJECT_DIR/.sessions/{normalized_project}/{session_id}.txt
File contents: tmux pane ID (e.g., "%0")
Activity tracking:
  - File existence indicates active work (created on UserPromptSubmit, PreToolUse, PostToolUse)
  - File mtime used for staleness detection
  - File deleted on SessionEnd or when session becomes idle

Requires Python 3.10+

Updated: 2025-11-08 21:14:42 UTC
"""

import json
import logging
import os
import random
import subprocess
import sys
import threading
import time
from pathlib import Path
from typing import Any, Union

# Type alias for JSON-compatible values (Python 3.10+ compatible)
JsonValue = Union[str, int, float, bool, None, dict[str, "JsonValue"], list["JsonValue"]]

# Setup logging to stderr
# Use INFO level by default (set PING_PONG_DEBUG=1 for DEBUG level)
log_level = logging.DEBUG if os.environ.get('PING_PONG_DEBUG') == '1' else logging.INFO
logging.basicConfig(
    level=log_level,
    format='[%(levelname)s] %(message)s',
    stream=sys.stderr
)
logger = logging.getLogger(__name__)


class SessionMonitor:
    """File-based session monitoring with stale detection via mtime."""

    def __init__(self) -> None:
        self.sessions: dict[str, dict[str, Any]] = {}
        self.config = {
            "ping_interval": 30,  # seconds between monitoring checks
            "stale_timeout": 150,  # seconds of inactivity before stale
            "forget_timeout": 600,  # seconds of inactivity before forgotten (1 hour)
            "continuation_messages": [
                "Please continue working...\n",
                "Continue with the next tasks...\n",
                "Let's keep going...\n",
                "Please proceed...\n",
                "Continue...\n"
            ]
        }
        self.monitoring_enabled = False
        self.monitor_thread: threading.Thread | None = None
        self.tmux_available = False
        self._lock = threading.Lock()
        self.my_pid = os.getpid()

    def start_monitoring(self) -> None:
        """Start background monitoring thread."""
        if self.monitoring_enabled:
            logger.debug("Monitoring already enabled, skipping start")
            return

        logger.debug("Starting session monitoring...")
        logger.debug(f"PID: {self.my_pid}")
        logger.debug(f"Config: ping_interval={self.config['ping_interval']}s, stale_timeout={self.config['stale_timeout']}s")

        self.tmux_available = self._check_tmux_available()
        if not self.tmux_available:
            logger.warning("✗ tmux not available - monitoring disabled")
            return

        logger.debug("✓ tmux is available")

        self.monitoring_enabled = True
        self.monitor_thread = threading.Thread(target=self._monitor_loop, daemon=True)
        self.monitor_thread.start()
        logger.info("✓ Session monitoring started successfully")

    def stop_monitoring(self) -> None:
        """Stop background monitoring thread."""
        self.monitoring_enabled = False
        if self.monitor_thread:
            self.monitor_thread.join(timeout=5)

    def _check_tmux_available(self) -> bool:
        """Check if tmux is installed and available."""
        try:
            result = subprocess.run(
                ['tmux', '-V'],
                capture_output=True,
                text=True,
                timeout=2
            )
            return result.returncode == 0
        except (FileNotFoundError, subprocess.TimeoutExpired):
            return False

    def _session_exists(self, tmux_session_name: str) -> bool:
        """Check if tmux session exists."""
        if not self.tmux_available:
            return False

        try:
            result = subprocess.run(
                ['tmux', 'has-session', '-t', tmux_session_name],
                capture_output=True,
                timeout=2
            )
            return result.returncode == 0
        except (FileNotFoundError, subprocess.TimeoutExpired):
            return False

    def _am_i_leader(self) -> bool:
        """Check if this is the leader monitor (lowest PID among all ping-pong processes)."""
        try:
            logger.debug(f"Leader election starting: my_pid={self.my_pid}")

            # Find all ping-pong.py processes (runs as "python3 -c ... exec(open('ping-pong.py').read())")
            result = subprocess.run(
                ['pgrep', '-f', 'ping-pong.py'],
                capture_output=True,
                text=True,
                timeout=2
            )

            logger.debug(f"pgrep result (pattern='ping-pong.py'): returncode={result.returncode}, stdout='{result.stdout.strip()}'")

            if result.returncode != 0:
                # No other processes found, we're the leader
                logger.debug(f"No ping-pong processes found via pgrep, assuming leader")
                return True

            # Parse PIDs
            pids = []
            for line in result.stdout.strip().split('\n'):
                line = line.strip()
                if line:
                    try:
                        pid = int(line)
                        pids.append(pid)
                        logger.debug(f"Found ping-pong process: PID {pid}")
                    except ValueError as e:
                        logger.warning(f"Failed to parse PID from line '{line}': {e}")
                        continue

            # Always include our own PID in the list (pgrep doesn't return the calling process)
            if self.my_pid not in pids:
                pids.append(self.my_pid)
                logger.debug(f"Added own PID to list: {self.my_pid}")

            if not pids:
                # No valid PIDs found, we're the leader
                logger.debug(f"No valid PIDs found, assuming leader")
                return True

            # We're the leader if we have the lowest PID
            min_pid = min(pids)
            is_leader = self.my_pid == min_pid

            logger.debug(f"Leader election results:")
            logger.debug(f"  - My PID: {self.my_pid} (type: {type(self.my_pid).__name__})")
            logger.debug(f"  - Leader PID: {min_pid} (type: {type(min_pid).__name__})")
            logger.debug(f"  - All PIDs: {sorted(pids)}")
            logger.debug(f"  - Process count: {len(pids)}")
            logger.debug(f"  - Am I leader? {is_leader}")

            if is_leader:
                logger.info(f"✓ LEADER monitor elected (PID {self.my_pid})")
            else:
                logger.info(f"✗ FOLLOWER monitor (PID {self.my_pid}, leader: {min_pid})")

            return is_leader

        except (subprocess.SubprocessError, subprocess.TimeoutExpired, ValueError) as e:
            logger.warning(f"Leader election failed: {e}, assuming leader by default")
            return True  # Assume leader if can't determine

    def _discover_sessions(self) -> dict[str, dict[str, Any]]:
        """Discover all session files by scanning .sessions directories."""
        discovered: dict[str, dict[str, Any]] = {}

        # Use CLAUDE_PLUGIN_ROOT for .sessions storage (system-wide)
        plugin_root = os.environ.get('CLAUDE_PLUGIN_ROOT')

        if plugin_root:
            plugin_dir = Path(plugin_root)
        else:
            plugin_dir = Path('.')

        sessions_root = plugin_dir / '.sessions'

        logger.debug(f"Session discovery: plugin_dir={plugin_dir}, sessions_root={sessions_root}")

        if not sessions_root.exists():
            logger.debug(f"Sessions root does not exist: {sessions_root}")
            return discovered

        # Scan all normalized project directories
        for project_dir_entry in sessions_root.iterdir():
            if not project_dir_entry.is_dir():
                continue

            logger.debug(f"Scanning project directory: {project_dir_entry.name}")

            # Scan for session files (*.txt)
            session_count = 0
            for session_file in project_dir_entry.glob('*.txt'):
                try:
                    # Session ID is the filename (without .txt)
                    session_id = session_file.stem

                    # Read tmux pane from file
                    tmux_pane = session_file.read_text().strip()

                    # Get file modification time
                    mtime = session_file.stat().st_mtime
                    current_time = time.time()
                    idle_seconds = current_time - mtime

                    discovered[session_id] = {
                        'session_id': session_id,
                        'tmux_pane': tmux_pane,
                        'file_path': str(session_file),
                        'last_mtime': mtime,
                        'project_dir': project_dir_entry.name
                    }

                    session_count += 1
                    logger.debug(f"Discovered session: id={session_id}, pane={tmux_pane}, idle={idle_seconds:.1f}s, file={session_file}")

                except (IOError, OSError) as e:
                    logger.warning(f"Failed to read session file {session_file}: {e}")
                    continue

            logger.debug(f"Found {session_count} sessions in {project_dir_entry.name}")

        logger.debug(f"Total sessions discovered: {len(discovered)}")
        return discovered

    def _validate_pane_exists(self, tmux_pane: str) -> bool:
        """Validate that a tmux pane actually exists and is active."""
        if not self.tmux_available or tmux_pane == 'none':
            return False

        try:
            # Use tmux display-message to check if pane exists and get its info
            result = subprocess.run(
                ['tmux', 'display-message', '-t', tmux_pane, '-p', '#{pane_id}:#{pane_pid}:#{pane_current_command}'],
                capture_output=True,
                text=True,
                timeout=2
            )

            if result.returncode != 0:
                logger.debug(f"Pane validation failed: pane {tmux_pane} does not exist (returncode={result.returncode})")
                return False

            # Parse the output
            output = result.stdout.strip()
            if not output:
                logger.debug(f"Pane validation failed: empty response for pane {tmux_pane}")
                return False

            parts = output.split(':')
            if len(parts) >= 3:
                pane_id, pane_pid, pane_command = parts[0], parts[1], parts[2]
                logger.debug(f"Pane {tmux_pane} validated: id={pane_id}, pid={pane_pid}, command={pane_command}")

                # Check if the pane has an active process
                if pane_pid and pane_pid != '0':
                    return True
                else:
                    logger.warning(f"Pane {tmux_pane} has no active process (pid={pane_pid})")
                    return False

            return False

        except (subprocess.TimeoutExpired, subprocess.SubprocessError) as e:
            logger.error(f"Pane validation error for {tmux_pane}: {e}")
            return False

    def _send_continuation_prompt_to_pane(self, tmux_pane: str, message: str) -> bool:
        """Send continuation prompt to specific tmux pane."""
        if not self.tmux_available or tmux_pane == 'none':
            logger.warning(f"Cannot send prompt - tmux unavailable or no pane: {tmux_pane}")
            return False

        # Validate pane exists before sending
        if not self._validate_pane_exists(tmux_pane):
            logger.warning(f"Cannot send prompt - pane {tmux_pane} does not exist or has no active process")
            return False

        try:
            logger.debug(f"Sending continuation prompt to pane {tmux_pane}")
            logger.debug(f"Message: {repr(message)}")

            # Send the message to the tmux pane
            result1 = subprocess.run(
                ['tmux', 'send-keys', '-t', tmux_pane, message],
                capture_output=True,
                timeout=5
            )
            logger.debug(f"send-keys (message) result: returncode={result1.returncode}")

            time.sleep(0.5)

            # Send Enter to execute
            result2 = subprocess.run(
                ['tmux', 'send-keys', '-t', tmux_pane, 'Enter'],
                capture_output=True,
                timeout=5
            )
            logger.debug(f"send-keys (Enter) result: returncode={result2.returncode}")

            logger.info(f"✓ Continuation prompt sent to pane: {tmux_pane}")
            return True

        except (subprocess.TimeoutExpired, Exception) as e:
            logger.error(f"✗ Failed to send prompt to pane {tmux_pane}: {e}")
            import traceback
            traceback.print_exc(file=sys.stderr)
            return False

    def _monitor_loop(self) -> None:
        """Background monitoring loop - discovers sessions from files."""
        loop_iteration = 0
        while self.monitoring_enabled:
            try:
                loop_iteration += 1
                logger.debug(f"========================================")
                logger.debug(f"Monitor loop iteration #{loop_iteration}")
                logger.debug(f"Timestamp: {time.strftime('%Y-%m-%d %H:%M:%S UTC', time.gmtime())}")

                # Discover sessions from files
                logger.debug(f"Starting session discovery...")
                file_sessions = self._discover_sessions()

                # Update in-memory sessions
                with self._lock:
                    old_count = len(self.sessions)
                    self.sessions = file_sessions
                    new_count = len(self.sessions)

                    if new_count != old_count:
                        logger.info(f"Session count changed: {old_count} -> {new_count}")

                # Check for stale sessions
                logger.debug(f"Starting staleness check...")
                self._check_stale_sessions()

                logger.debug(f"Monitor loop iteration #{loop_iteration} complete")
                logger.debug(f"Next check in {self.config['ping_interval']} seconds")

            except Exception as e:
                logger.error(f"Monitor loop error in iteration #{loop_iteration}: {e}")
                import traceback
                traceback.print_exc(file=sys.stderr)

            time.sleep(self.config["ping_interval"])

    def _check_stale_sessions(self) -> None:
        """Check all sessions for staleness using file mtime (leader only)."""
        # Only leader sends continuation prompts
        is_leader = self._am_i_leader()

        if not is_leader:
            logger.debug(f"Skipping staleness check - not leader")
            return

        logger.debug(f"Running staleness check as LEADER")
        current_time = time.time()
        stale_count = 0
        active_count = 0
        forgotten_count = 0

        with self._lock:
            total_sessions = len(self.sessions)
            logger.debug(f"Checking {total_sessions} sessions (stale_timeout={self.config['stale_timeout']}s, forget_timeout={self.config['forget_timeout']}s)")

            for session_id, session_data in list(self.sessions.items()):
                # Check staleness based on file mtime
                last_mtime = session_data.get("last_mtime", current_time)
                time_since_activity = current_time - last_mtime
                is_stale = time_since_activity > self.config["stale_timeout"]
                is_forgotten = time_since_activity > self.config["forget_timeout"]
                tmux_pane = session_data.get("tmux_pane")

                logger.debug(f"Session {session_id}: idle={time_since_activity:.1f}s, stale={is_stale}, forgotten={is_forgotten}, pane={tmux_pane}")

                if is_forgotten:
                    # Session has been idle too long, don't try to revive it
                    forgotten_count += 1
                    logger.info(f"💤 Forgotten session (idle {time_since_activity:.0f}s > {self.config['forget_timeout']}s): {session_id} - skipping continuation")
                elif is_stale:
                    # Session is stale but not forgotten
                    # Since session file exists, it means there's active work happening
                    stale_count += 1
                    logger.warning(f"⚠️  Stale session detected: {session_id} ({time_since_activity:.0f}s idle, threshold={self.config['stale_timeout']}s)")
                    logger.info(f"🔧 Session {session_id} has active work (file exists) - sending continuation")

                    # Send continuation prompt to tmux pane
                    if tmux_pane and tmux_pane != "none":
                        message = random.choice(self.config["continuation_messages"])
                        logger.info(f"Sending continuation to pane {tmux_pane} for session {session_id}")
                        success = self._send_continuation_prompt_to_pane(tmux_pane, message)
                        if success:
                            logger.info(f"✓ Continuation sent successfully to {session_id}")
                        else:
                            logger.error(f"✗ Failed to send continuation to {session_id}")
                    else:
                        logger.warning(f"Cannot send continuation - no valid tmux pane for {session_id}")
                else:
                    active_count += 1

            logger.debug(f"Staleness check complete: {active_count} active, {stale_count} stale, {forgotten_count} forgotten (total: {total_sessions})")

    def register_session(self, session_id: str, tmux_session_name: str | None = None, session_type: str = "claude_code") -> dict[str, Any]:
        """Register a session for monitoring."""
        current_time = time.time()

        # Validate tmux session if provided
        if tmux_session_name and self.tmux_available:
            if not self._session_exists(tmux_session_name):
                return {
                    "success": False,
                    "error": f"tmux session does not exist: {tmux_session_name}"
                }

        with self._lock:
            self.sessions[session_id] = {
                "tmux_session_name": tmux_session_name,
                "type": session_type,
                "last_activity": current_time,
                "last_ping": current_time,
                "missed_pings": 0,
                "status": "active",
                "registered_at": current_time
            }

        logger.info(f"Registered session: {session_id} (type={session_type}, tmux={tmux_session_name})")

        return {
            "success": True,
            "session_id": session_id,
            "tmux_available": self.tmux_available,
            "monitoring_enabled": self.monitoring_enabled
        }

    def heartbeat(self, session_id: str) -> dict[str, Any]:
        """Update session activity timestamp."""
        with self._lock:
            if session_id not in self.sessions:
                return {
                    "success": False,
                    "error": f"Session not registered: {session_id}"
                }

            current_time = time.time()
            self.sessions[session_id]["last_activity"] = current_time
            self.sessions[session_id]["last_ping"] = current_time
            self.sessions[session_id]["status"] = "active"
            self.sessions[session_id]["missed_pings"] = 0

        return {
            "success": True,
            "session_id": session_id,
            "timestamp": current_time
        }

    def mark_stale(self, session_id: str) -> dict[str, Any]:
        """Explicitly mark session as stale and trigger continuation."""
        with self._lock:
            if session_id not in self.sessions:
                return {
                    "success": False,
                    "error": f"Session not registered: {session_id}"
                }

            session_data = self.sessions[session_id]
            session_data["status"] = "stale"

            tmux_session_name = session_data.get("tmux_session_name")
            if not tmux_session_name:
                return {
                    "success": False,
                    "error": "No tmux session associated"
                }

            # Send continuation prompt immediately
            message = random.choice(self.config["continuation_messages"])
            success = self._send_continuation_prompt(tmux_session_name, message)

            if success:
                # Reset activity after sending prompt
                current_time = time.time()
                session_data["last_activity"] = current_time
                session_data["status"] = "active"

        return {
            "success": success,
            "session_id": session_id,
            "action": "continuation_sent" if success else "failed"
        }

    def list_sessions(self) -> dict[str, Any]:
        """List all discovered sessions with mtime info."""
        current_time = time.time()

        # Discover sessions from filesystem in real-time
        file_sessions = self._discover_sessions()

        # Update in-memory cache
        with self._lock:
            self.sessions = file_sessions

            sessions_list = []
            for session_id, session_data in self.sessions.items():
                last_mtime = session_data.get("last_mtime", current_time)
                idle_seconds = current_time - last_mtime
                is_stale = idle_seconds > self.config["stale_timeout"]
                is_forgotten = idle_seconds > self.config["forget_timeout"]

                sessions_list.append({
                    "session_id": session_id,
                    "tmux_pane": session_data.get("tmux_pane"),
                    "project_dir": session_data.get("project_dir"),
                    "idle_seconds": round(idle_seconds, 1),
                    "is_stale": is_stale,
                    "is_forgotten": is_forgotten,
                    "file_path": session_data.get("file_path")
                })

        return {
            "sessions": sessions_list,
            "count": len(sessions_list),
            "monitoring_enabled": self.monitoring_enabled,
            "tmux_available": self.tmux_available,
            "is_leader": self._am_i_leader(),
            "my_pid": self.my_pid
        }

    def configure(self, ping_interval: int | None = None, stale_timeout: int | None = None, forget_timeout: int | None = None, continuation_messages: list[str] | None = None) -> dict[str, Any]:
        """Update monitoring configuration."""
        with self._lock:
            if ping_interval is not None:
                self.config["ping_interval"] = max(5, ping_interval)  # Minimum 5 seconds

            if stale_timeout is not None:
                self.config["stale_timeout"] = max(30, stale_timeout)  # Minimum 30 seconds

            if forget_timeout is not None:
                self.config["forget_timeout"] = max(300, forget_timeout)  # Minimum 5 minutes

            if continuation_messages is not None and len(continuation_messages) > 0:
                self.config["continuation_messages"] = continuation_messages

        return {
            "success": True,
            "config": self.config.copy()
        }


class PingPongMCPServer:
    """MCP server for session monitoring and revival."""

    def __init__(self, name: str, version: str = "1.0.0") -> None:
        self.name = name
        self.version = version
        self.monitor = SessionMonitor()

    def handle_initialize(self, _: dict[str, JsonValue]) -> dict[str, JsonValue]:
        """Handle initialize request."""
        # Start monitoring on initialization
        self.monitor.start_monitoring()

        return {
            "protocolVersion": "2025-06-18",
            "capabilities": {
                "tools": {}
            },
            "serverInfo": {
                "name": self.name,
                "version": self.version
            }
        }

    def handle_noop(self) -> dict[str, JsonValue]:
        """Handle unsupported requests."""
        return {}

    def handle_tools_list(self, _: dict[str, JsonValue]) -> dict[str, JsonValue]:
        """Handle tools/list request - list available tools."""
        return {
            "tools": [
                {
                    "name": "list_sessions",
                    "description": "List all discovered sessions from hook-created files with their current status and idle time based on file mtime.",
                    "inputSchema": {
                        "type": "object",
                        "properties": {}
                    }
                },
                {
                    "name": "configure",
                    "description": "Configure monitoring parameters (ping interval, stale timeout, forget timeout, continuation messages).",
                    "inputSchema": {
                        "type": "object",
                        "properties": {
                            "ping_interval": {
                                "type": "integer",
                                "description": "Seconds between monitoring checks (minimum 5)"
                            },
                            "stale_timeout": {
                                "type": "integer",
                                "description": "Seconds of inactivity before marking stale (minimum 30)"
                            },
                            "forget_timeout": {
                                "type": "integer",
                                "description": "Seconds of inactivity before forgetting session (minimum 300, default 3600)"
                            },
                            "continuation_messages": {
                                "type": "array",
                                "items": {"type": "string"},
                                "description": "List of messages to randomly select from when sending continuation prompts"
                            }
                        }
                    }
                },
                {
                    "name": "send_continuation",
                    "description": "Manually send continuation prompt to a specific tmux pane (for testing/debugging).",
                    "inputSchema": {
                        "type": "object",
                        "properties": {
                            "tmux_pane": {
                                "type": "string",
                                "description": "Tmux pane ID (e.g., '%0')"
                            },
                            "message": {
                                "type": "string",
                                "description": "Custom message to send (optional, uses default if not provided)"
                            }
                        },
                        "required": ["tmux_pane"]
                    }
                }
            ]
        }

    def handle_tools_call(self, params: dict[str, JsonValue]) -> dict[str, JsonValue]:
        """Handle tools/call request - execute tool."""
        name_value = params.get("name", "")

        if not isinstance(name_value, str):
            raise ValueError("Tool name must be a string")

        name: str = name_value
        arguments = params.get("arguments", {})

        if not isinstance(arguments, dict):
            raise ValueError("Tool arguments must be an object")

        # Route to appropriate handler
        result: dict[str, Any]

        if name == "list_sessions":
            result = self.monitor.list_sessions()

        elif name == "configure":
            ping_interval = arguments.get("ping_interval")
            stale_timeout = arguments.get("stale_timeout")
            forget_timeout = arguments.get("forget_timeout")
            continuation_messages = arguments.get("continuation_messages")

            result = self.monitor.configure(
                ping_interval=ping_interval if isinstance(ping_interval, int) else None,
                stale_timeout=stale_timeout if isinstance(stale_timeout, int) else None,
                forget_timeout=forget_timeout if isinstance(forget_timeout, int) else None,
                continuation_messages=continuation_messages if isinstance(continuation_messages, list) else None
            )

        elif name == "send_continuation":
            tmux_pane = arguments.get("tmux_pane", "")
            message = arguments.get("message")

            if not isinstance(tmux_pane, str) or not tmux_pane:
                raise ValueError("tmux_pane must be a non-empty string")

            # Use provided message or random default
            msg = message if isinstance(message, str) else random.choice(self.monitor.config["continuation_messages"])

            success = self.monitor._send_continuation_prompt_to_pane(tmux_pane, msg)

            result = {
                "success": success,
                "tmux_pane": tmux_pane,
                "message_sent": msg if success else None
            }

        else:
            raise ValueError(f"Unknown tool: {name}")

        # Format result as MCP tool response
        return {
            "content": [{
                "type": "text",
                "text": json.dumps(result, indent=2)
            }]
        }

    def handle_request(self, request: dict[str, JsonValue]) -> dict[str, JsonValue]:
        """Handle incoming JSON-RPC request."""
        method_value = request.get("method", "")
        method = method_value if isinstance(method_value, str) else ""

        params_value = request.get("params", {})
        params: dict[str, JsonValue] = params_value if isinstance(params_value, dict) else {}

        # Check if this is a notification (request without id)
        request_id = request.get("id")
        is_notification = request_id is None

        try:
            if method == "initialize":
                result = self.handle_initialize(params)
            elif method == "ping":
                result = self.handle_noop()
            elif method == "notifications/initialized":
                result = self.handle_noop()
            elif method == "notifications/cancelled":
                result = self.handle_noop()
            elif method == "tools/list":
                result = self.handle_tools_list(params)
            elif method == "tools/call":
                result = self.handle_tools_call(params)
            else:
                response: dict[str, JsonValue] = {
                    "jsonrpc": "2.0",
                    "error": {
                        "code": -32601,
                        "message": f"Method not found: {method}"
                    }
                }
                if not is_notification:
                    response["id"] = request_id
                return response

            # Success response - only send response for non-notifications
            if is_notification:
                return {}

            response: dict[str, JsonValue] = {
                "jsonrpc": "2.0",
                "result": result
            }
            if not is_notification:
                response["id"] = request_id

            return response

        except ValueError as e:
            response: dict[str, JsonValue] = {
                "jsonrpc": "2.0",
                "error": {
                    "code": -32602,
                    "message": str(e)
                }
            }
            if not is_notification:
                response["id"] = request_id
            return response
        except Exception as e:
            response: dict[str, JsonValue] = {
                "jsonrpc": "2.0",
                "error": {
                    "code": -32603,
                    "message": f"Internal error: {str(e)}"
                }
            }
            if not is_notification:
                response["id"] = request_id
            return response

    def run(self) -> None:
        """Run the MCP server - read from stdin, write to stdout."""
        # Use line-buffered mode for stdio
        sys.stdin.reconfigure(line_buffering=True)  # type: ignore[attr-defined]
        sys.stdout.reconfigure(line_buffering=True)  # type: ignore[attr-defined]

        logger.debug(f"Ping/Pong MCP server '{self.name}' starting...")

        try:
            for line in sys.stdin:
                line = line.strip()
                if not line:
                    continue

                logger.debug(f"Received: {line[:200]}{'...' if len(line) > 200 else ''}")

                try:
                    request = json.loads(line)
                    response = self.handle_request(request)

                    # Skip empty responses (notifications don't get responses)
                    if not response:
                        logger.debug("No response needed (notification)")
                        continue

                    response_str = json.dumps(response)
                    logger.debug(f"Sending: {response_str[:200]}{'...' if len(response_str) > 200 else ''}")

                    # Write response as JSON line
                    json.dump(response, sys.stdout)
                    sys.stdout.write('\n')
                    sys.stdout.flush()

                except json.JSONDecodeError as e:
                    logger.debug(f"Parse error: {str(e)}")

                    error_response: dict[str, JsonValue] = {
                        "jsonrpc": "2.0",
                        "error": {
                            "code": -32700,
                            "message": f"Parse error: {str(e)}"
                        }
                    }
                    json.dump(error_response, sys.stdout)
                    sys.stdout.write('\n')
                    sys.stdout.flush()

        except KeyboardInterrupt:
            logger.info("Shutdown signal received")
        except Exception as e:
            logger.debug(f"Fatal error: {e}")
            import traceback
            traceback.print_exc(file=sys.stderr)
        finally:
            # Stop monitoring on shutdown
            self.monitor.stop_monitoring()
            logger.debug(f"Ping/Pong MCP server '{self.name}' stopped.")


def main() -> None:
    """Main entry point."""
    server = PingPongMCPServer("resin-ai-orchestrator-ping-pong")
    server.run()


if __name__ == "__main__":
    main()
