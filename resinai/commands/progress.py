#!/usr/bin/env python3
"""
Update Progress Command

Automatically updates docs/DEVELOPMENT_PLAN_AND_PROGRESS.md when TodoWrite changes phase status.
Moves orchestrator state management functionality to hook automation.
Receives JSON input via stdin containing TodoWrite session and event data.

This is a Python conversion of the original update-progress.sh bash script.
"""

import sys
from pathlib import Path
from typing import Dict, List, Any, Optional

from ..utils import (
    HookLogger, JSONHandler, TaskExtractor, FileOperations,
    print_stderr, get_timestamp
)


class ProgressUpdater:
    """Updates DEVELOPMENT_PLAN_AND_PROGRESS.md with phase transitions."""

    def __init__(self, progress_file: str = "docs/DEVELOPMENT_PLAN_AND_PROGRESS.md"):
        self.progress_file = Path(progress_file)
        self.logger = HookLogger()
        self.timestamp = get_timestamp()

    def update_progress(self, input_data: Dict[str, Any]) -> int:
        """Main progress update logic."""
        try:
            # Extract session and todo data
            session_id = JSONHandler.safe_extract(input_data, 'session_id', 'unknown')
            todos = JSONHandler.safe_extract(input_data, 'tool_input.todos', [])

            if not isinstance(todos, list):
                todos = []

            print_stderr(f"State transition tracking triggered at {self.timestamp} for session {session_id}")

            # Extract task context for logging
            task_ids = TaskExtractor.extract_task_ids(todos)
            task_id = task_ids[0] if task_ids else None

            # Log hook execution
            self.logger.log_execution(
                session_id,
                "update-progress.py",
                "State transition tracking",
                task_id
            )

            # Check if progress file exists
            if not self.progress_file.exists():
                print_stderr(f"Warning: {self.progress_file} not found - skipping state transition")
                self.logger.log_completion(session_id, "update-progress.py", "Progress file not found", task_id)
                return 0

            # Extract phase transitions
            phases = TaskExtractor.extract_phases(todos)

            if not any(phases.values()):
                print_stderr("No phase-related todos found - skipping state transition")
                self.logger.log_completion(session_id, "update-progress.py", "No phase transitions", task_id)
                return 0

            # Find current and completed phases
            completed_phase = phases['completed'][-1] if phases['completed'] else None
            current_phase = phases['in_progress'][0] if phases['in_progress'] else None

            # Update the progress file
            success = self._update_epic_implementation_state(
                current_phase,
                completed_phase,
                session_id
            )

            if success:
                print_stderr(f"State transition updated: {completed_phase} → {current_phase}")
                self.logger.log_completion(
                    session_id,
                    "update-progress.py",
                    "State transition completed",
                    task_id
                )
            else:
                print_stderr("Failed to update state transition")
                self.logger.log_completion(
                    session_id,
                    "update-progress.py",
                    "State transition failed",
                    task_id
                )
                return 1

            return 0

        except Exception as e:
            print_stderr(f"Error in progress update: {e}")
            return 1

    def _update_epic_implementation_state(
        self,
        current_phase: Optional[str],
        completed_phase: Optional[str],
        session_id: str
    ) -> bool:
        """Update the Epic Implementation State section in progress file."""
        if not current_phase and not completed_phase:
            return True

        # Read current content
        content = FileOperations.safe_read(self.progress_file)
        if content is None:
            return False

        # Split into lines for processing
        lines = content.split('\n')
        updated_lines = []
        in_state_section = False
        updated = False

        for line in lines:
            if line.strip() == "## Epic Implementation State":
                in_state_section = True
                updated_lines.append(line)
                continue

            if line.startswith("##") and in_state_section and line.strip() != "## Epic Implementation State":
                in_state_section = False

            if in_state_section and line.strip().startswith("- Current Phase:") and current_phase:
                updated_lines.append(f"- Current Phase: {current_phase}")
                updated = True
                continue

            if in_state_section and line.strip().startswith("- Last Updated:"):
                updated_lines.append(f"- Last Updated: {self.timestamp} (via hook automation)")
                continue

            if in_state_section and line.strip().startswith("- Session ID:"):
                updated_lines.append(f"- Session ID: {session_id}")
                continue

            updated_lines.append(line)

        # Write updated content
        new_content = '\n'.join(updated_lines)
        success = FileOperations.safe_write(self.progress_file, new_content, backup=True)

        if updated:
            print_stderr(f"Updated state transition: {completed_phase} → {current_phase}")

        return success
