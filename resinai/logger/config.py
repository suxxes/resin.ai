#!/usr/bin/env python3
"""
Logging Configuration

Centralized configuration for the logging system including levels,
destinations, and formatting options.
"""

import os
from pathlib import Path
from typing import Dict, Any, Optional
from dataclasses import dataclass, field
from enum import Enum


class LogLevel(Enum):
    """Structured log levels."""
    TRACE = "TRACE"
    DEBUG = "DEBUG" 
    INFO = "INFO"
    WARN = "WARN"
    ERROR = "ERROR"
    CRITICAL = "CRITICAL"


class LogOutput(Enum):
    """Log output destinations."""
    CONSOLE = "console"
    FILE = "file"
    SESSION = "session"
    TASK = "task"


@dataclass
class LoggingConfig:
    """Configuration class for orchestrator logging system."""
    
    # Base configuration
    level: LogLevel = LogLevel.INFO
    enabled_outputs: list[LogOutput] = field(default_factory=lambda: [
        LogOutput.CONSOLE, 
        LogOutput.FILE
    ])
    
    # Directory configuration
    logs_base_dir: Path = field(default_factory=lambda: Path(".claude/logs"))
    session_logs_dir: Path = field(default_factory=lambda: Path(".claude/logs/sessions"))
    task_logs_dir: Path = field(default_factory=lambda: Path(".claude/logs/tasks"))
    
    # File configuration
    main_log_file: str = "orchestrator.log"
    max_file_size_mb: int = 10
    backup_count: int = 5
    
    # Format configuration
    include_timestamp: bool = True
    include_level: bool = True
    include_logger_name: bool = True
    include_correlation_id: bool = True
    
    # Console configuration
    console_colors: bool = True
    console_rich_formatting: bool = True
    
    # Performance configuration
    async_logging: bool = False
    buffer_size: int = 1000
    
    def __post_init__(self):
        """Ensure all directories exist after initialization."""
        self.logs_base_dir.mkdir(parents=True, exist_ok=True)
        
        if LogOutput.SESSION in self.enabled_outputs:
            self.session_logs_dir.mkdir(parents=True, exist_ok=True)
            
        if LogOutput.TASK in self.enabled_outputs:
            self.task_logs_dir.mkdir(parents=True, exist_ok=True)
    
    @classmethod
    def from_environment(cls) -> 'LoggingConfig':
        """Create configuration from environment variables."""
        config = cls()
        
        # Override from environment
        if log_level := os.getenv('RESINAI_LOG_LEVEL'):
            try:
                config.level = LogLevel(log_level.upper())
            except ValueError:
                pass  # Keep default
        
        if logs_dir := os.getenv('RESINAI_LOGS_DIR'):
            config.logs_base_dir = Path(logs_dir)
            config.session_logs_dir = Path(logs_dir) / "sessions"
            config.task_logs_dir = Path(logs_dir) / "tasks"
        
        if console_colors := os.getenv('RESINAI_CONSOLE_COLORS'):
            config.console_colors = console_colors.lower() in ('true', '1', 'yes')
        
        return config
    
    def get_session_log_path(self, session_id: str) -> Path:
        """Get log file path for a specific session by finding existing file with session_id in name."""
        # First, try to find an existing log file with this session_id in the name
        if self.session_logs_dir.exists():
            existing_files = list(self.session_logs_dir.glob(f"*{session_id}*.log"))
            if existing_files:
                # Use the most recent existing file
                existing_files.sort(key=lambda x: x.stat().st_mtime, reverse=True)
                return existing_files[0]
        
        # If no existing file found, create new one with timestamp format
        from datetime import datetime
        timestamp = datetime.now().strftime("%Y-%m-%d-%H-%M")
        return self.session_logs_dir / f"{timestamp} - {session_id}.log"
    
    def get_task_log_path(self, task_id: str, session_id: str) -> Path:
        """Get log file path for a specific task by finding existing file with session_id in name."""
        # First, try to find an existing log file with this session_id in the name
        if self.task_logs_dir.exists():
            existing_files = list(self.task_logs_dir.glob(f"*{session_id}*.log"))
            if existing_files:
                # Use the most recent existing file
                existing_files.sort(key=lambda x: x.stat().st_mtime, reverse=True)
                return existing_files[0]
        
        # If no existing file found, create new one with timestamp format
        from datetime import datetime
        timestamp = datetime.now().strftime("%Y-%m-%d-%H-%M")
        return self.task_logs_dir / f"{timestamp} - {session_id}.log"
    
    def get_main_log_path(self) -> Path:
        """Get main log file path."""
        return self.logs_base_dir / self.main_log_file