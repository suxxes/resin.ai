#!/usr/bin/env python3
"""
Update Epic Story Task Command

Automatically syncs progress across Epic/Story/Task files when TodoWrite changes task progress.
Moves agent documentation responsibility to hook automation.
Receives JSON input via stdin containing TodoWrite session and event data.

This is a Python conversion of the original update-epic-story-task-progress.sh bash script.
"""

import sys
from pathlib import Path
from typing import Dict, List, Any, Optional, Tuple

from ..utils import (
    HookLogger, JSONHandler, TaskExtractor, FileOperations, ProgressTracker,
    print_stderr, get_timestamp
)


class DocumentationSyncer:
    """Syncs progress across Epic/Story/Task documentation files."""

    def __init__(self, doc_base: str = "docs/DEVELOPMENT_PLAN_AND_PROGRESS"):
        self.doc_base = Path(doc_base)
        self.logger = HookLogger()
        self.timestamp = get_timestamp()

    def sync_documentation(self, input_data: Dict[str, Any]) -> int:
        """Main documentation sync logic."""
        try:
            # Extract session and todo data
            session_id = JSONHandler.safe_extract(input_data, 'session_id', 'unknown')
            todos = JSONHandler.safe_extract(input_data, 'tool_input.todos', [])

            if not isinstance(todos, list):
                todos = []

            print_stderr(f"Documentation sync triggered at {self.timestamp} for session {session_id}")

            # Extract task IDs
            task_ids = TaskExtractor.extract_task_ids(todos)

            # Log execution for each task
            for task_id in task_ids:
                self.logger.log_execution(
                    session_id,
                    "update-epic-story-task.py",
                    "Documentation sync",
                    task_id
                )

            # If no task IDs, log to orchestrator file
            if not task_ids:
                self.logger.log_execution(
                    session_id,
                    "update-epic-story-task.py",
                    "Documentation sync (no tasks)"
                )
                print_stderr("No task IDs found - skipping documentation sync")
                return 0

            # Check if documentation directory exists
            if not self.doc_base.exists():
                print_stderr(f"Warning: Documentation directory {self.doc_base} not found - skipping documentation sync")
                return 0

            synced_files = []

            # Process each task
            for task_id in task_ids:
                task_files = self._sync_task_documentation(task_id, todos, session_id)
                synced_files.extend(task_files)

            # Log completion
            for task_id in task_ids:
                self.logger.log_completion(
                    session_id,
                    "update-epic-story-task.py",
                    "Documentation sync completed",
                    task_id
                )

            if not task_ids:
                self.logger.log_completion(
                    session_id,
                    "update-epic-story-task.py",
                    "Documentation sync completed (no tasks)"
                )

            if synced_files:
                print_stderr(f"Documentation synchronized for files: {' '.join(map(str, synced_files))}")
            else:
                print_stderr("No documentation files found to sync")

            return 0

        except Exception as e:
            print_stderr(f"Error in documentation sync: {e}")
            return 1

    def _sync_task_documentation(
        self,
        task_id: str,
        todos: List[Dict[str, Any]],
        session_id: str
    ) -> List[Path]:
        """Sync documentation for a specific task and its hierarchy."""
        synced_files = []

        # Extract epic and story IDs
        epic_id = task_id[:4]  # EEEE
        story_id = task_id[:7]  # EEEE.SS

        # Get task details from todos
        task_content, task_status = self._get_task_details(task_id, todos)

        if not task_content or not task_status:
            return synced_files

        print_stderr(f"Syncing documentation for task {task_id} ({task_status})")

        # Update task file
        task_file = self._update_task_file(task_id, task_status)
        if task_file:
            synced_files.append(task_file)

        # Update story file
        story_file = self._update_story_file(story_id, task_id, todos)
        if story_file:
            synced_files.append(story_file)

        # Update epic file
        epic_file = self._update_epic_file(epic_id, task_id, todos)
        if epic_file:
            synced_files.append(epic_file)

        return synced_files

    def _get_task_details(
        self,
        task_id: str,
        todos: List[Dict[str, Any]]
    ) -> Tuple[Optional[str], Optional[str]]:
        """Get task content and status from todos."""
        for todo in todos:
            if (todo.get('id') == task_id or
                task_id in todo.get('content', '')):
                return todo.get('content'), todo.get('status')
        return None, None

    def _update_task_file(self, task_id: str, status: str) -> Optional[Path]:
        """Update individual task file with current status."""
        # Find task file (pattern: EEEE.SS.TT - Epic Name - Story Name - Task Name.md)
        task_files = FileOperations.find_files(self.doc_base, f"{task_id} - *.md")

        if not task_files:
            return None

        task_file = task_files[0]  # Take first match
        content = FileOperations.safe_read(task_file)

        if content is None:
            return None

        # Update or add Implementation Status section
        lines = content.split('\n')
        updated_lines = []
        in_status_section = False
        status_section_found = False

        for line in lines:
            if line.strip() == "## Implementation Status":
                status_section_found = True
                in_status_section = True
                updated_lines.append(line)
                updated_lines.append("")
                updated_lines.append(f"**Status**: {status} (Updated: {self.timestamp} via hook automation)")
                updated_lines.append("")
                continue

            if line.startswith("##") and in_status_section and line.strip() != "## Implementation Status":
                in_status_section = False

            if not (in_status_section and line.strip().startswith("**Status**:")):
                updated_lines.append(line)

        # Add status section if it didn't exist
        if not status_section_found:
            updated_lines.extend([
                "",
                "## Implementation Status",
                "",
                f"**Status**: {status} (Updated: {self.timestamp} via hook automation)",
                ""
            ])

        new_content = '\n'.join(updated_lines)
        if FileOperations.safe_write(task_file, new_content, backup=False):
            return task_file

        return None

    def _update_story_file(
        self,
        story_id: str,
        task_id: str,
        todos: List[Dict[str, Any]]
    ) -> Optional[Path]:
        """Update story file with task progress."""
        # Find story file (pattern: EEEE.SS - Epic Name - Story Name.md)
        story_files = FileOperations.find_files(self.doc_base, f"{story_id} - *.md")

        if not story_files:
            return None

        story_file = story_files[0]  # Take first match
        content = FileOperations.safe_read(story_file)

        if content is None:
            return None

        # Get all task IDs for this story
        all_task_ids = TaskExtractor.extract_task_ids(todos)
        progress = ProgressTracker.calculate_task_progress(all_task_ids, todos, story_id)

        # Update or add Task Progress section
        lines = content.split('\n')
        updated_lines = []
        in_progress_section = False
        progress_section_found = False

        for line in lines:
            if line.strip() == "## Task Progress":
                progress_section_found = True
                in_progress_section = True
                updated_lines.append(line)
                updated_lines.append("")
                updated_lines.append(f"**Progress**: {progress['completed']}/{progress['total']} tasks completed ({progress['percentage']}%)")
                updated_lines.append(f"**Last Updated**: {self.timestamp} (via hook automation)")
                updated_lines.append("")
                continue

            if line.startswith("##") and in_progress_section and line.strip() != "## Task Progress":
                in_progress_section = False

            if not (in_progress_section and
                   (line.strip().startswith("**Progress**:") or
                    line.strip().startswith("**Last Updated**:"))):
                updated_lines.append(line)

        # Add progress section if it didn't exist
        if not progress_section_found:
            updated_lines.extend([
                "",
                "## Task Progress",
                "",
                f"**Progress**: {progress['completed']}/{progress['total']} tasks completed ({progress['percentage']}%)",
                f"**Last Updated**: {self.timestamp} (via hook automation)",
                ""
            ])

        new_content = '\n'.join(updated_lines)
        if FileOperations.safe_write(story_file, new_content, backup=False):
            return story_file

        return None

    def _update_epic_file(
        self,
        epic_id: str,
        task_id: str,
        todos: List[Dict[str, Any]]
    ) -> Optional[Path]:
        """Update epic file with story progress."""
        # Find epic file (pattern: EEEE - Epic Name.md)
        epic_files = FileOperations.find_files(self.doc_base, f"{epic_id} - *.md")

        if not epic_files:
            return None

        epic_file = epic_files[0]  # Take first match
        content = FileOperations.safe_read(epic_file)

        if content is None:
            return None

        # Get all task IDs for this epic
        all_task_ids = TaskExtractor.extract_task_ids(todos)
        progress = ProgressTracker.calculate_story_progress(all_task_ids, todos, epic_id)

        # Update or add Story Progress section
        lines = content.split('\n')
        updated_lines = []
        in_progress_section = False
        progress_section_found = False

        for line in lines:
            if line.strip() == "## Story Progress":
                progress_section_found = True
                in_progress_section = True
                updated_lines.append(line)
                updated_lines.append("")
                updated_lines.append(f"**Progress**: {progress['completed']}/{progress['total']} stories completed ({progress['percentage']}%)")
                updated_lines.append(f"**Last Updated**: {self.timestamp} (via hook automation)")
                updated_lines.append("")
                continue

            if line.startswith("##") and in_progress_section and line.strip() != "## Story Progress":
                in_progress_section = False

            if not (in_progress_section and
                   (line.strip().startswith("**Progress**:") or
                    line.strip().startswith("**Last Updated**:"))):
                updated_lines.append(line)

        # Add progress section if it didn't exist
        if not progress_section_found:
            updated_lines.extend([
                "",
                "## Story Progress",
                "",
                f"**Progress**: {progress['completed']}/{progress['total']} stories completed ({progress['percentage']}%)",
                f"**Last Updated**: {self.timestamp} (via hook automation)",
                ""
            ])

        new_content = '\n'.join(updated_lines)
        if FileOperations.safe_write(epic_file, new_content, backup=False):
            return epic_file

        return None
