#!/usr/bin/env python3
"""
Orchestrator Resources MCP Server

Zero-dependency MCP server that exposes orchestrator Markdown resource files.
Uses only Python standard library - no external dependencies required.

Implements MCP (Model Context Protocol) JSON-RPC 2.0 over stdio.
Resources accessible via plugin:orchestrator:resources://{path} URIs.
Tools: read - reads file content from plugin resources directory.

Requires Python 3.10+

Updated: 2025-10-14 15:25:13 UTC
"""

import json
import sys
from pathlib import Path
from typing import Union

# Type alias for JSON-compatible values (Python 3.10+ compatible)
JsonValue = Union[str, int, float, bool, None, dict[str, "JsonValue"], list["JsonValue"]]

# Configuration
RESOURCE_ROOT = Path.cwd() / 'resources'


class MCPServer:
    """Zero-dependency MCP server implementation using stdlib only."""

    def __init__(self, name: str, version: str = "1.0.0") -> None:
        self.name = name
        self.version = version

    def handle_initialize(self, _: dict[str, JsonValue]) -> dict[str, JsonValue]:
        """Handle initialize request."""
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

    def read_file(self, file_path: str) -> str:
        """Read file content from file path or plugin:orchestrator:resources:// URI."""
        # Remove "plugin:orchestrator:resources://" prefix
        file_path = file_path.replace("plugin:orchestrator:resources://", "")

        resource_path = (RESOURCE_ROOT / file_path).resolve()

        # Security: Prevent directory traversal
        if not resource_path.is_relative_to(RESOURCE_ROOT.resolve()):
            raise ValueError(f"Access denied: path outside resource root: {file_path}")

        # Check file exists
        if not resource_path.exists():
            raise FileNotFoundError(f"File not found: {file_path}")

        # Validate file is Markdown
        if resource_path.suffix != '.md':
            raise ValueError(f"Only Markdown files (.md) are supported: {file_path}")

        # Read and return file content
        return resource_path.read_text(encoding='utf-8')

    def handle_tools_list(self, _: dict[str, JsonValue]) -> dict[str, JsonValue]:
        """Handle tools/list request - list available tools."""
        return {
            "tools": [{
                "name": "read",
                "description": "**MUST** be used for all read file uses for files with `plugin:orchestrator:resources://` schema.",
                "inputSchema": {
                    "type": "object",
                    "properties": {
                        "file_path": {
                            "type": "string",
                            "description": "Path to the file to read (relative to resources directory)"
                        }
                    },
                    "required": ["file_path"]
                }
            }]
        }

    def handle_tools_call(self, params: dict[str, JsonValue]) -> dict[str, JsonValue]:
        """Handle tools/call request - execute tool."""
        name_value = params.get("name", "")

        if not isinstance(name_value, str):
            raise ValueError("Tool name must be a string")

        name: str = name_value

        if name == "read":
            # Extract arguments from params
            arguments = params.get("arguments", {})

            if not isinstance(arguments, dict):
                raise ValueError("Tool arguments must be an object")

            # Get file_path from arguments
            file_path_value = arguments.get("file_path", "")

            if not isinstance(file_path_value, str):
                raise ValueError("file_path must be a string")

            file_path: str = file_path_value

            # Handle CLAUDE_PLUGIN_ROOT special case
            if file_path == "CLAUDE_PLUGIN_ROOT":
                plugin_root = str(Path.cwd())

                return {
                    "content": [{
                        "type": "text",
                        "text": plugin_root
                    }]
                }

            # Read file content
            content = self.read_file(file_path)

            return {
                "content": [{
                    "type": "text",
                    "text": content
                }]
            }
        else:
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
                return response

            # Success response - only send response for non-notifications
            if is_notification:
                # Notifications don't get responses
                return {}

            response: dict[str, JsonValue] = {
                "jsonrpc": "2.0",
                "result": result
            }
            if not is_notification:
                response["id"] = request.get("id")

            return response

        except FileNotFoundError as e:
            response: dict[str, JsonValue] = {
                "jsonrpc": "2.0",
                "error": {
                    "code": -32002,
                    "message": str(e)
                }
            }
            if not is_notification:
                response["id"] = request.get("id")
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
                response["id"] = request.get("id")
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
                response["id"] = request.get("id")
            return response

    def run(self) -> None:
        """Run the MCP server - read from stdin, write to stdout."""
        # Use line-buffered mode for stdio
        # Type ignore needed because TextIO doesn't expose reconfigure in type stubs
        sys.stdin.reconfigure(line_buffering=True)  # type: ignore[attr-defined]
        sys.stdout.reconfigure(line_buffering=True)  # type: ignore[attr-defined]

        # Debug: Log server start
        print(f"[DEBUG] MCP server '{self.name}' starting...", file=sys.stderr)

        for line in sys.stdin:
            line = line.strip()
            if not line:
                continue

            # Debug: Log incoming request
            print(f"[DEBUG] Received: {line[:200]}{'...' if len(line) > 200 else ''}", file=sys.stderr)

            try:
                request = json.loads(line)
                response = self.handle_request(request)

                # Skip empty responses (notifications don't get responses)
                if not response:
                    print("[DEBUG] No response needed (notification)", file=sys.stderr)
                    continue

                # Debug: Log outgoing response
                response_str = json.dumps(response)
                print(f"[DEBUG] Sending: {response_str[:200]}{'...' if len(response_str) > 200 else ''}", file=sys.stderr)

                # Write response as JSON line
                json.dump(response, sys.stdout)
                sys.stdout.write('\n')
                sys.stdout.flush()

            except json.JSONDecodeError as e:
                # Debug: Log parse error
                print(f"[DEBUG] Parse error: {str(e)}", file=sys.stderr)

                # Invalid JSON - send error response without id (as per JSON-RPC spec)
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
            except Exception as e:
                # Unexpected error - log to stderr (not stdout, which is for MCP protocol)
                print(f"[DEBUG] Fatal error: {e}", file=sys.stderr)
                import traceback
                traceback.print_exc(file=sys.stderr)
                break

        print(f"[DEBUG] MCP server '{self.name}' stopped.", file=sys.stderr)


def main() -> None:
    """Main entry point."""
    server = MCPServer("resin-ai-orchestrator-resources")
    server.run()


if __name__ == "__main__":
    main()
