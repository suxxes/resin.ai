#!/usr/bin/env python3
"""
Ping/Pong MCP Server for Claude Code Session Monitoring

Zero-dependency MCP server that monitors Claude Code sessions via hook-created files,
detects stale sessions using file mtime, and sends continuation prompts to revive them.
Uses only Python standard library - no external dependencies required.

Implements MCP (Model Context Protocol) JSON-RPC 2.0 over stdio.

Features:
- Hook-based session tracking (ping-pong.sh creates/deletes session files on active events)
- File existence-based activity monitoring (file only exists when active work is happening)
- File mtime-based staleness detection (no polling overhead)
- Auto-discovery of sessions from $CLAUDE_PLUGIN_ROOT/.sessions/
- Direct tmux session continuation prompt injection
- Zero external dependencies

Session files: $CLAUDE_PLUGIN_ROOT/.sessions/{normalized_project}/{session_id}.json
File contents: JSON array of todos from TodoWrite
Activity tracking:
  - File existence indicates active work (created on UserPromptSubmit, PreToolUse, PostToolUse)
  - File mtime used for staleness detection
  - File deleted on SessionEnd or when session becomes idle
  - Todos parsed directly from session file (no dependency on ~/.claude/todos)

Requires Python 3.10+

Updated: 2025-11-11 17:59:24 UTC
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
# Use INFO level by default (set RESIN_AI_DEBUG=1 for DEBUG level)
log_level = logging.DEBUG if os.environ.get('RESIN_AI_DEBUG') == '1' else logging.INFO
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
        self._is_leader_cached: bool | None = None
        self._leader_check_time: float = 0.0

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

    def _am_i_leader(self, force_recheck: bool = False) -> bool:
        """Check if this is the leader monitor (lowest PID among all ping-pong processes).

        Results are cached for 60 seconds to reduce overhead. Use force_recheck=True to bypass cache.
        """
        current_time = time.time()
        cache_ttl = 60.0  # Cache leader status for 60 seconds

        # Return cached result if still valid
        if not force_recheck and self._is_leader_cached is not None:
            if current_time - self._leader_check_time < cache_ttl:
                logger.debug(f"Using cached leader status: {self._is_leader_cached} (age: {current_time - self._leader_check_time:.1f}s)")
                return self._is_leader_cached

        try:
            logger.debug(f"Leader election starting: my_pid={self.my_pid}")

            # Find all ping-pong.py processes using ps + grep
            # Pattern matches: python3 -c ... exec(open('ping-pong.py').read())
            # Using ps is more reliable than pgrep across different systems
            result = subprocess.run(
                ['sh', '-c', 'ps -eo pid,command | grep "[e]xec.*ping-pong" | awk \'{print $1}\''],
                capture_output=True,
                text=True,
                timeout=2
            )

            logger.debug(f"ps+grep result: returncode={result.returncode}, stdout='{result.stdout.strip()}'")

            if result.returncode != 0 or not result.stdout.strip():
                # No processes found, we're the leader
                logger.debug(f"No ping-pong processes found, assuming leader")
                is_leader = True
            else:
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

                if not pids:
                    # No valid PIDs found, we're the leader
                    logger.debug(f"No valid PIDs found, assuming leader")
                    is_leader = True
                else:
                    # We're the leader if we have the lowest PID
                    min_pid = min(pids)
                    is_leader = self.my_pid == min_pid

                    logger.debug(f"Leader election results:")
                    logger.debug(f"  - My PID: {self.my_pid}")
                    logger.debug(f"  - Leader PID: {min_pid}")
                    logger.debug(f"  - All PIDs: {sorted(pids)}")
                    logger.debug(f"  - Process count: {len(pids)}")

            # Cache the result
            self._is_leader_cached = is_leader
            self._leader_check_time = current_time

            # Only log on status change or first check
            if is_leader:
                logger.info(f"✓ LEADER monitor elected (PID {self.my_pid})")
            else:
                min_pid = min(pids) if pids else "unknown"
                logger.info(f"✗ FOLLOWER monitor (PID {self.my_pid}, leader: {min_pid})")

            return is_leader

        except (subprocess.SubprocessError, subprocess.TimeoutExpired, ValueError) as e:
            logger.warning(f"Leader election failed: {e}, assuming leader by default")
            # Cache failure result briefly
            self._is_leader_cached = True
            self._leader_check_time = current_time
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

            # Scan for session files (*.json)
            session_count = 0
            for session_file in project_dir_entry.glob('*.json'):
                try:
                    # Session ID is the filename (without .json extension)
                    session_id = session_file.stem

                    # Read todos from JSON file
                    file_content = session_file.read_text().strip()
                    try:
                        todos = json.loads(file_content) if file_content else []
                    except json.JSONDecodeError:
                        logger.warning(f"Failed to parse JSON in {session_file}, treating as empty todos")
                        todos = []

                    # tmux session name matches session_id (we rename it in the hook)
                    tmux_session = session_id

                    # Get file modification time
                    mtime = session_file.stat().st_mtime
                    current_time = time.time()
                    idle_seconds = current_time - mtime

                    # Count active/pending todos
                    active_todos = [t for t in todos if isinstance(t, dict) and t.get('status') in ['in_progress', 'pending']]
                    active_count_local = len(active_todos)

                    discovered[session_id] = {
                        'session_id': session_id,
                        'tmux_session': tmux_session,
                        'file_path': str(session_file),
                        'last_mtime': mtime,
                        'project_dir': project_dir_entry.name,
                        'todos': todos,
                        'active_todo_count': active_count_local
                    }

                    session_count += 1
                    logger.debug(f"Discovered session: id={session_id}, tmux_session={tmux_session}, todos={len(todos)} ({active_count_local} active), idle={idle_seconds:.1f}s, file={session_file}")

                except (IOError, OSError) as e:
                    logger.warning(f"Failed to read session file {session_file}: {e}")
                    continue

            logger.debug(f"Found {session_count} sessions in {project_dir_entry.name}")

        logger.debug(f"Total sessions discovered: {len(discovered)}")
        return discovered

    def _validate_session_exists(self, tmux_session: str) -> bool:
        """Validate that a tmux session actually exists and is active."""
        if not self.tmux_available or tmux_session == 'none':
            return False

        try:
            # Use tmux has-session to check if session exists
            result = subprocess.run(
                ['tmux', 'has-session', '-t', tmux_session],
                capture_output=True,
                timeout=2
            )

            if result.returncode != 0:
                logger.debug(f"Session validation failed: session {tmux_session} does not exist (returncode={result.returncode})")
                return False

            # Get session info to verify it's active
            result = subprocess.run(
                ['tmux', 'display-message', '-t', tmux_session, '-p', '#{session_name}:#{session_windows}:#{session_attached}'],
                capture_output=True,
                text=True,
                timeout=2
            )

            if result.returncode != 0:
                logger.debug(f"Session info failed for {tmux_session}")
                return False

            output = result.stdout.strip()
            if not output:
                logger.debug(f"Session validation failed: empty response for session {tmux_session}")
                return False

            parts = output.split(':')
            if len(parts) >= 3:
                session_name, session_windows, session_attached = parts[0], parts[1], parts[2]
                logger.debug(f"Session {tmux_session} validated: name={session_name}, windows={session_windows}, attached={session_attached}")
                return True

            return False

        except (subprocess.TimeoutExpired, subprocess.SubprocessError) as e:
            logger.error(f"Session validation error for {tmux_session}: {e}")
            return False

    def _send_continuation_prompt_to_session(self, tmux_session: str, message: str) -> bool:
        """Send continuation prompt to specific tmux session."""
        if not self.tmux_available or tmux_session == 'none':
            logger.warning(f"Cannot send prompt - tmux unavailable or no session: {tmux_session}")
            return False

        # Validate session exists before sending
        if not self._validate_session_exists(tmux_session):
            logger.warning(f"Cannot send prompt - session {tmux_session} does not exist")
            return False

        try:
            logger.debug(f"Sending continuation prompt to session {tmux_session}")
            logger.debug(f"Message: {repr(message)}")

            # Send the message to the tmux session
            result1 = subprocess.run(
                ['tmux', 'send-keys', '-t', tmux_session, message],
                capture_output=True,
                timeout=5
            )
            logger.debug(f"send-keys (message) result: returncode={result1.returncode}")

            time.sleep(0.5)

            # Send Enter to execute
            result2 = subprocess.run(
                ['tmux', 'send-keys', '-t', tmux_session, 'Enter'],
                capture_output=True,
                timeout=5
            )
            logger.debug(f"send-keys (Enter) result: returncode={result2.returncode}")

            logger.info(f"✓ Continuation prompt sent to session: {tmux_session}")
            return True

        except (subprocess.TimeoutExpired, Exception) as e:
            logger.error(f"✗ Failed to send prompt to session {tmux_session}: {e}")
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
                tmux_session = session_data.get("tmux_session")
                active_todo_count = session_data.get("active_todo_count", 0)
                todos = session_data.get("todos", [])

                logger.debug(f"Session {session_id}: idle={time_since_activity:.1f}s, stale={is_stale}, forgotten={is_forgotten}, tmux_session={tmux_session}, active_todos={active_todo_count}")

                if is_forgotten:
                    # Session has been idle too long, don't try to revive it
                    forgotten_count += 1
                    logger.info(f"💤 Forgotten session (idle {time_since_activity:.0f}s > {self.config['forget_timeout']}s): {session_id} - skipping continuation")
                elif is_stale:
                    # Session is stale but not forgotten
                    # Only send continuation if there are active/pending todos
                    if active_todo_count > 0:
                        stale_count += 1
                        logger.warning(f"⚠️  Stale session detected: {session_id} ({time_since_activity:.0f}s idle, threshold={self.config['stale_timeout']}s)")
                        logger.info(f"🔧 Session {session_id} has {active_todo_count} active todos - sending continuation")

                        # Send continuation prompt to tmux session
                        if tmux_session and tmux_session != "none":
                            message = random.choice(self.config["continuation_messages"])
                            logger.info(f"Sending continuation to session {tmux_session} for session {session_id}")
                            success = self._send_continuation_prompt_to_session(tmux_session, message)
                            if success:
                                logger.info(f"✓ Continuation sent successfully to {session_id}")
                            else:
                                logger.error(f"✗ Failed to send continuation to {session_id}")
                        else:
                            logger.warning(f"Cannot send continuation - no valid tmux session for {session_id}")
                    else:
                        logger.debug(f"Session {session_id} is stale but has no active todos - skipping continuation")
                        active_count += 1  # Count as active (no intervention needed)
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
            "tools": []
        }

    def handle_tools_call(self, params: dict[str, JsonValue]) -> dict[str, JsonValue]:
        """Handle tools/call request - execute tool."""
        name_value = params.get("name", "")

        if not isinstance(name_value, str):
            raise ValueError("Tool name must be a string")

        name: str = name_value

        raise ValueError(f"Unknown tool: {name}")

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
