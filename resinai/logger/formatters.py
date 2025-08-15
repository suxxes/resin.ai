"""
Formatters for ResIn.AI Orchestrator logging system
"""

import json
import logging
from typing import Dict, Any


class StructuredFormatter(logging.Formatter):
    """JSON structured log formatter."""

    def format(self, record: logging.LogRecord) -> str:
        log_data = {
            'timestamp': self.formatTime(record),
            'level': record.levelname,
            'name': record.name,
            'message': record.getMessage(),
        }

        # Add any extra fields
        if hasattr(record, '__dict__'):
            for key, value in record.__dict__.items():
                if key not in ['name', 'msg', 'args', 'levelname', 'levelno', 'pathname', 'filename', 'module', 'lineno', 'funcName', 'created', 'msecs', 'relativeCreated', 'thread', 'threadName', 'processName', 'process', 'getMessage', 'exc_info', 'exc_text', 'stack_info']:
                    log_data[key] = value

        return json.dumps(log_data)


class ConsoleFormatter(logging.Formatter):
    """Enhanced console formatter with colors."""

    def format(self, record: logging.LogRecord) -> str:
        # Use standard formatting for console output
        return super().format(record)


class FileFormatter(logging.Formatter):
    """File-specific formatter with detailed context."""

    def format(self, record: logging.LogRecord) -> str:
        # Add extra context for file logging
        log_line = super().format(record)
        if hasattr(record, 'session_id'):
            log_line = f"[{record.session_id}] {log_line}"
        return log_line
