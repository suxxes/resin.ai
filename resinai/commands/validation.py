#!/usr/bin/env python3
"""
Validate Phase Transition Command

Validates completion criteria before allowing Task delegation to next phase.
Moves orchestrator quality gate responsibility to hook automation.
Receives JSON input via stdin containing Task tool delegation event data.

This is a Python conversion of the original validate-phase-transition.sh bash script.
"""

import sys
import subprocess
from pathlib import Path
from typing import Dict, Any, Optional, Tuple, List

from ..utils import (
    HookLogger, JSONHandler, TaskExtractor, FileOperations,
    print_stderr, get_timestamp
)


class PhaseTransitionValidator:
    """Validates phase transitions and quality gates."""

    def __init__(self):
        from pathlib import Path
        self.logs_base = Path(".claude/logs")
        self.logs_base.mkdir(parents=True, exist_ok=True)

        self.logger = HookLogger(str(self.logs_base))
        self.timestamp = get_timestamp()

    def validate_transition(self, input_data: Dict[str, Any]) -> int:
        """Main validation logic."""
        try:
            # Extract delegation event data
            session_id = JSONHandler.safe_extract(input_data, 'session_id', 'unknown')
            subagent_type = JSONHandler.safe_extract(input_data, 'tool_input.subagent_type', 'unknown')
            description = JSONHandler.safe_extract(input_data, 'tool_input.description', 'No description')
            prompt = JSONHandler.safe_extract(input_data, 'tool_input.prompt', '')

            print_stderr(f"Quality gate validation triggered at {self.timestamp} for session {session_id}")

            # Extract task context
            task_id = self._extract_task_id(description, prompt, subagent_type)

            # Log execution
            if task_id:
                self.logger.log_execution(
                    session_id,
                    "validate-phase-transition.py",
                    f"Quality gate validation for {subagent_type}",
                    task_id
                )
            else:
                self.logger.log_execution(
                    session_id,
                    "validate-phase-transition.py",
                    f"Quality gate validation for {subagent_type} (no task)"
                )

            if not task_id:
                self.logger.log_completion(session_id, "validate-phase-transition.py", "No task ID - delegation allowed")
                print_stderr("No task ID found - allowing delegation without validation")
                return 0

            # Define phase transition rules
            required_phase, current_phase = self._get_phase_rules(subagent_type)

            if not required_phase or not current_phase:
                self.logger.log_completion(session_id, "validate-phase-transition.py", "Unknown agent type - delegation allowed", task_id)
                print_stderr("Unknown agent type - allowing delegation without validation")
                return 0

            print_stderr(f"Validating transition to {current_phase} (requires {required_phase} completed)")

            # Validate transition
            validation_result = self._validate_previous_phase_completion(
                task_id,
                session_id,
                required_phase,
                current_phase
            )

            if validation_result == 0:
                # Validate specific quality requirements
                self._validate_quality_requirements(current_phase, task_id, session_id)

                # Log successful validation
                self.logger.log_custom(
                    session_id,
                    f"QUALITY_GATE_PASSED: {required_phase} completed - allowing {current_phase} delegation",
                    task_id
                )
                self.logger.log_custom(
                    session_id,
                    f"Transition: {required_phase} → {current_phase} (Agent: {subagent_type})",
                    task_id
                )
                self.logger.log_completion(
                    session_id,
                    "validate-phase-transition.py",
                    "Quality gate PASSED - delegation allowed",
                    task_id
                )

                print_stderr(f"Quality gate validation passed for task {task_id}")
                print_stderr(f"Quality gate validation completed at {self.timestamp}")
                return 0

            else:
                # Validation failed - block delegation
                return validation_result

        except Exception as e:
            print_stderr(f"Error in phase transition validation: {e}")
            return 1

    def _extract_task_id(self, description: str, prompt: str, subagent_type: str) -> Optional[str]:
        """Extract task ID from description, prompt, or subagent type."""
        search_text = f"{description} {prompt} {subagent_type}"
        task_ids = TaskExtractor.extract_from_text(search_text)
        return task_ids[0] if task_ids else None

    def _get_task_log_path(self, task_id: str, session_id: str) -> Path:
        """Get task log file path by finding existing file with session_id using full pattern matching."""
        import re
        
        # First, try to find an existing log file with this session_id using full pattern matching
        if self.logs_base.exists():
            # Pattern: YYYY-MM-DD-HHmm - SESSION_ID.log
            pattern = re.compile(rf'^\d{{4}}-\d{{2}}-\d{{2}}-\d{{4}} - {re.escape(session_id)}\.log$')
            
            existing_files = []
            for log_file in self.logs_base.glob("*.log"):
                if pattern.match(log_file.name):
                    existing_files.append(log_file)
            
            if existing_files:
                # Use the most recent existing file
                existing_files.sort(key=lambda x: x.stat().st_mtime, reverse=True)
                return existing_files[0]
        
        # If no existing file found, create new one with timestamp format
        from datetime import datetime
        timestamp = datetime.now().strftime("%Y-%m-%d-%H%M")
        return self.logs_base / f"{timestamp} - {session_id}.log"

    def _get_phase_rules(self, subagent_type: str) -> Tuple[Optional[str], Optional[str]]:
        """Get required previous phase and current phase for agent type."""
        if subagent_type == "feature-lead":
            return "PM_BOOTSTRAP", "FL_PLAN"
        elif subagent_type.startswith("developer-"):
            return "FL_PLAN", "DEV_IMPLEMENT"
        elif subagent_type == "quality-assurance":
            return "DEV_IMPLEMENT", "QUALITY_ASSURANCE"
        else:
            return None, None

    def _validate_previous_phase_completion(
        self,
        task_id: str,
        session_id: str,
        required_phase: str,
        current_phase: str
    ) -> int:
        """Validate that the previous phase was completed."""
        # Check for task-specific log file
        if not self.logs_base.exists():
            self.logger.log_completion(session_id, "validate-phase-transition.py", "No logs directory - delegation allowed", task_id)
            print_stderr(f"Warning: Logs directory {self.logs_base} not found - allowing delegation without validation")
            return 0

        task_log = self._get_task_log_path(task_id, session_id)

        if not task_log.exists():
            self.logger.log_completion(session_id, "validate-phase-transition.py", "No previous log - first delegation allowed", task_id)
            print_stderr(f"No previous log found for task {task_id} - allowing first delegation")
            return 0

        # Look for previous phase completion in log
        log_content = FileOperations.safe_read(task_log)
        if not log_content:
            return 0

        # Check for orchestrator completion
        if self._check_orchestrator_completion(log_content, required_phase):
            return 0

        # Check for phase completion in any format
        if self._check_phase_completion(log_content, required_phase):
            return 0

        # Check for existing work that bypassed orchestrator
        existing_work_result = self._check_existing_work(task_id, session_id)
        if existing_work_result == 0:
            return 0

        # Quality gate failed
        print_stderr(f"QUALITY GATE FAILED: {required_phase} not completed for task {task_id}")
        print_stderr(f"No existing work found - blocking delegation to {current_phase}")

        # Log the failure
        self.logger.log_custom(
            session_id,
            f"QUALITY_GATE_FAILURE: Blocked delegation - {required_phase} not completed",
            task_id
        )
        self.logger.log_custom(
            session_id,
            f"Required: {required_phase} → Attempted: {current_phase}",
            task_id
        )
        self.logger.log_custom(
            session_id,
            f"No git commits or documentation found for task {task_id}",
            task_id
        )
        self.logger.log_completion(
            session_id,
            "validate-phase-transition.py",
            "Quality gate FAILED - delegation blocked",
            task_id
        )

        return 2  # Exit code 2 to block delegation

    def _check_orchestrator_completion(self, log_content: str, required_phase: str) -> bool:
        """Check for orchestrator completion in log."""
        lines = log_content.split('\n')
        for line in lines:
            if ("ORCHESTRATOR -> PROGRESS UPDATE" in line and
                "completed" in line and
                required_phase.lower() in line.lower()):
                return True
        return False

    def _check_phase_completion(self, log_content: str, required_phase: str) -> bool:
        """Check for phase completion in any format."""
        lines = log_content.split('\n')
        for line in lines:
            if (("completed" in line.lower() or "SUCCESS" in line) and
                required_phase.lower() in line.lower()):
                return True
        return False

    def _check_existing_work(self, task_id: str, session_id: str) -> int:
        """Check for existing work that bypassed orchestrator."""
        print_stderr("No orchestrator completion found - checking for existing work...")

        # Check for git commits related to this task
        git_commits = self._get_git_commits(task_id)

        # Check for task documentation files
        task_file = self._find_task_documentation(task_id)

        if git_commits and task_file:
            print_stderr(f"DISCOVERED EXISTING WORK: Task {task_id} has git commits and documentation")
            print_stderr("Initializing orchestrator state recovery for pre-existing work")

            # Log state recovery
            task_log = self._get_task_log_path(task_id, session_id)
            self.logger.log_custom(session_id, f"STATE_RECOVERY: Discovered existing work for task {task_id}", task_id)
            self.logger.log_custom(session_id, f"Git commits found: {len(git_commits)} commits", task_id)
            self.logger.log_custom(session_id, f"Documentation exists: {task_file}", task_id)
            self.logger.log_custom(session_id, f"ORCHESTRATOR_STATE_INIT: Marking required phase as completed (recovery)", task_id)
            self.logger.log_completion(session_id, "validate-phase-transition.py", "State recovery successful - allowing delegation", task_id)

            print_stderr("State recovery successful - allowing delegation")
            return 0

        return 1  # No existing work found

    def _get_git_commits(self, task_id: str) -> List[str]:
        """Get git commits related to task ID."""
        try:
            # Try grep search first
            result = subprocess.run(
                ['git', 'log', '--oneline', '--grep', task_id],
                capture_output=True, text=True, timeout=10
            )
            if result.returncode == 0 and result.stdout.strip():
                return result.stdout.strip().split('\n')

            # Try general search
            result = subprocess.run(
                ['git', 'log', '--oneline'],
                capture_output=True, text=True, timeout=10
            )
            if result.returncode == 0:
                lines = result.stdout.strip().split('\n')
                matching_lines = [line for line in lines if task_id.lower() in line.lower()]
                return matching_lines

        except (subprocess.TimeoutExpired, subprocess.CalledProcessError, FileNotFoundError):
            pass

        return []

    def _find_task_documentation(self, task_id: str) -> Optional[Path]:
        """Find task documentation file."""
        doc_base = Path("docs/DEVELOPMENT_PLAN_AND_PROGRESS")
        if doc_base.exists():
            task_files = FileOperations.find_files(doc_base, f"*{task_id}*")
            return task_files[0] if task_files else None
        return None

    def _validate_quality_requirements(self, current_phase: str, task_id: str, session_id: str) -> None:
        """Validate specific quality requirements based on target phase."""
        task_log = self._get_task_log_path(task_id, session_id)
        log_content = FileOperations.safe_read(task_log)

        if not log_content:
            return

        if current_phase == "DEV_IMPLEMENT":
            # Validate FL_PLAN completion requirements
            if not self._check_planning_artifacts(log_content):
                print_stderr(f"QUALITY GATE WARNING: No planning artifacts found for task {task_id}")

        elif current_phase == "QUALITY_ASSURANCE":
            # Validate DEV_IMPLEMENT completion requirements
            if not self._check_implementation_artifacts(log_content):
                print_stderr(f"QUALITY GATE WARNING: No implementation artifacts found for task {task_id}")

    def _check_planning_artifacts(self, log_content: str) -> bool:
        """Check for planning artifacts in log content."""
        patterns = [
            "task.*implementation.*checklist",
            "business.*requirements",
            "acceptance.*criteria"
        ]

        for pattern in patterns:
            if pattern.lower() in log_content.lower():
                return True
        return False

    def _check_implementation_artifacts(self, log_content: str) -> bool:
        """Check for implementation artifacts in log content."""
        patterns = [
            "implementation.*complete",
            "unit.*test.*pass",
            "code.*format"
        ]

        for pattern in patterns:
            if pattern.lower() in log_content.lower():
                return True
        return False
