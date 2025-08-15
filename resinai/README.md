# ResIn.AI Orchestrator CLI - Comprehensive Usage Guide

This document provides complete usage instructions for the ResIn.AI Orchestrator CLI system, a modern Python-based hook automation system built with Typer and Rich for enterprise-grade multi-agent orchestration.

## Overview

The ResIn.AI Orchestrator CLI is a sophisticated hook automation system that replaces traditional bash hooks with a modern Python CLI framework. It provides:

- **Enterprise-grade CLI** built with Typer framework and Rich formatting
- **Hook automation** for orchestrator state management and documentation sync
- **Quality gate validation** for phase transitions
- **Progress tracking** across Epic/Story/Task hierarchy
- **Modern UX** with progress indicators, colors, and auto-completion

## Installation & Setup

### Quick Setup
```bash
# Navigate to resinai directory
cd resinai

# Install dependencies and verify installation
python3 setup.py

# Verify installation
python3 -m resinai status
```

### Manual Installation
```bash
# Install dependencies manually
pip install typer>=0.16.0 rich>=14.0.0

# Test functionality
python3 -m resinai --help
```

## CLI Commands Reference

### Main Commands

#### 1. `update-progress` - Progress Documentation Update
```bash
# Update DEVELOPMENT_PLAN_AND_PROGRESS.md with phase transitions
echo '{"session_id":"123","tool_input":{"todos":[...]}}' | python3 -m resinai update-progress

# With verbose output and dry run
echo '{"session_id":"123","tool_input":{"todos":[...]}}' | python3 -m resinai update-progress --verbose --dry-run
```

**Purpose**: Automatically updates `docs/DEVELOPMENT_PLAN_AND_PROGRESS.md` when TodoWrite changes phase status, providing real-time synchronization of Epic Implementation State.

**Input Format**:
```json
{
  "session_id": "claude-session-123",
  "tool_input": {
    "todos": [
      {
        "id": "0003.02.01",
        "content": "Implement user authentication - PM_BOOTSTRAP",
        "status": "completed",
        "priority": "high"
      },
      {
        "id": "0003.02.02", 
        "content": "Setup database models - FL_PLAN",
        "status": "in_progress",
        "priority": "high"
      }
    ]
  }
}
```

#### 2. `update-progress-documentation` - Hierarchy Documentation Sync
```bash
# Sync progress across Epic/Story/Task files
echo '{"session_id":"123","tool_input":{"todos":[...]}}' | python3 -m resinai update-progress-documentation

# With options
echo '{"session_id":"123","tool_input":{"todos":[...]}}' | python3 -m resinai update-progress-documentation --verbose --dry-run
```

**Purpose**: Maintains bidirectional documentation sync and calculates progress percentages across the Epic/Story/Task hierarchy. Updates Implementation Status sections in all related files.

#### 3. `validate-transition` - Quality Gate Validation
```bash
# Validate phase transitions before agent delegation
echo '{"session_id":"123","tool_input":{"subagent_type":"developer-python"}}' | python3 -m resinai validate-transition

# With force bypass (use with caution)
echo '{"session_id":"123","tool_input":{"subagent_type":"quality-assurance"}}' | python3 -m resinai validate-transition --force
```

**Purpose**: Enforces quality gates and prevents invalid state transitions. Blocks workflow violations and maintains comprehensive audit trail.

**Input Format**:
```json
{
  "session_id": "claude-session-123",
  "tool_input": {
    "subagent_type": "developer-python",
    "description": "Implement authentication system for task 0003.02.01",
    "prompt": "You are implementing user authentication..."
  }
}
```

#### 4. `status` - System Health Check
```bash
# Display system status and available commands
python3 -m resinai status
```

**Purpose**: Shows system information, recent activity, configuration status, and available commands with descriptions.

### CLI Options & Flags

#### Global Options
- `--version`: Show version information with rich formatting
- `--help`: Display help information with examples
- `--install-completion`: Install shell auto-completion

#### Command-Specific Options
- `--verbose`, `-v`: Enable verbose output with detailed logging
- `--dry-run`, `-n`: Show what would be done without executing
- `--force`, `-f`: Force bypass validation checks (validation command only)

## Advanced Usage Patterns

### Hook Integration
The CLI is designed to be called from Claude Code hooks:

```bash
# In .claude/hooks/user-prompt-submit-hook.py
import subprocess
import json

def on_submit(data):
    hook_input = json.dumps({
        "session_id": data.get("session_id"),
        "tool_input": data.get("tool_input", {})
    })
    
    # Call orchestrator CLI
    subprocess.run([
        "python3", "-m", "resinai", "update-progress"
    ], input=hook_input, text=True)
```

### Direct Script Execution (Legacy Support)
```bash
# Run individual command scripts directly
echo '{"session_id":"123","tool_input":{"todos":[]}}' | python3 resinai/commands/progress.py
echo '{"session_id":"123","tool_input":{"todos":[]}}' | python3 resinai/commands/documentation.py
echo '{"tool_input":{"subagent_type":"developer-python"}}' | python3 resinai/commands/validation.py
```

### Python API Usage
```python
# Import orchestrator components for custom integrations
from resinai.utils import HookLogger, JSONHandler, TaskExtractor, ProgressTracker
from resinai.commands.progress import ProgressUpdater
from resinai.commands.documentation import DocumentationSyncer
from resinai.commands.validation import PhaseTransitionValidator

# Use in custom scripts
updater = ProgressUpdater()
result = updater.update_progress(input_data)
```

## Module Structure & Architecture

### Package Organization
```
resinai/
├── __init__.py                 # Package exports and version info
├── __main__.py                # Main CLI application (Typer + Rich)
├── utils.py                   # Core utilities and shared functionality
├── requirements.txt           # Dependencies (Typer + Rich)
├── setup.py                   # Installation and verification script
├── USAGE.md                   # This comprehensive guide
├── commands/                  # Hook command implementations
│   ├── __init__.py           # Command exports
│   ├── progress.py           # Progress update automation
│   ├── documentation.py      # Documentation sync automation  
│   ├── validation.py         # Quality gate validation
│   └── status.py             # Status reporting functionality
└── logger/                   # Logging infrastructure
    ├── __init__.py           # Logger exports
    ├── config.py             # Logging configuration
    ├── logger.py             # Core logging functionality
    └── formatters.py         # Rich and structured formatters
```

### Clean Import Architecture
The package uses modern Python import patterns:

1. **No naming conflicts**: `logger` module avoids conflicts with Python's built-in `logging`
2. **Relative imports**: All internal imports use proper relative syntax
3. **Module execution**: CLI must be run with `python3 -m resinai` pattern
4. **Type hints**: Full type annotation support throughout codebase

## Testing & Verification

### Functionality Testing
```bash
# Test CLI functionality
python3 -m resinai --version
python3 -m resinai status

# Test individual commands with sample data
echo '{"session_id":"test","tool_input":{"todos":[]}}' | python3 -m resinai update-progress
echo '{"session_id":"test","tool_input":{"todos":[]}}' | python3 -m resinai update-progress-documentation
echo '{"session_id":"test","tool_input":{"subagent_type":"developer-python"}}' | python3 -m resinai validate-transition
```

### Legacy Script Testing
```bash
# Test direct script execution (legacy support)
echo '{"session_id":"test","tool_input":{"todos":[]}}' | python3 resinai/commands/progress.py
echo '{"session_id":"test","tool_input":{"todos":[]}}' | python3 resinai/commands/documentation.py
echo '{"session_id":"test","tool_input":{"subagent_type":"test"}}' | python3 resinai/commands/validation.py
```

## Error Handling & Troubleshooting

### Common Issues

#### 1. Import Errors
```bash
# If you get import errors, ensure you're running as module
python3 -m resinai status  # ✅ Correct
python3 resinai/           # ❌ Incorrect
```

#### 2. Missing Dependencies
```bash
# Install required dependencies
pip install typer>=0.16.0 rich>=14.0.0

# Or use setup script
python3 resinai/setup.py
```

#### 3. JSON Input Validation
```bash
# Valid JSON input format
echo '{"session_id":"test","tool_input":{}}' | python3 -m resinai update-progress

# The CLI will handle invalid JSON gracefully and show warnings
echo 'invalid json' | python3 -m resinai update-progress
```

### Logging & Debugging

The orchestrator provides comprehensive logging:

- **Execution logs**: Stored in `.claude/logs/` directory
- **Console output**: Rich formatted progress and status information
- **Error handling**: Graceful degradation with informative error messages
- **Verbose mode**: Use `--verbose` flag for detailed operation information

## Integration Examples

### Claude Code Hook Integration
```python
#!/usr/bin/env python3
"""Claude Code hook integration example."""

import subprocess
import json
import sys

def orchestrator_hook(session_data):
    """Call ResIn.AI orchestrator from Claude Code hook."""
    
    # Prepare input data
    hook_input = json.dumps({
        "session_id": session_data.get("session_id"),
        "tool_input": session_data.get("tool_input", {})
    })
    
    # Call appropriate orchestrator command
    if "todos" in session_data.get("tool_input", {}):
        # TodoWrite hook - update progress
        subprocess.run([
            "python3", "-m", "resinai", "update-progress"
        ], input=hook_input, text=True)
        
        # Also sync documentation
        subprocess.run([
            "python3", "-m", "resinai", "update-progress-documentation"
        ], input=hook_input, text=True)
        
    elif "subagent_type" in session_data.get("tool_input", {}):
        # Task hook - validate transition
        result = subprocess.run([
            "python3", "-m", "resinai", "validate-transition"
        ], input=hook_input, text=True)
        
        # Exit with same code as validator
        sys.exit(result.returncode)

# Hook entry point
if __name__ == "__main__":
    data = json.loads(sys.stdin.read())
    orchestrator_hook(data)
```

### Custom Automation Scripts
```python
#!/usr/bin/env python3
"""Custom orchestrator automation example."""

from resinai.commands.progress import ProgressUpdater
from resinai.commands.documentation import DocumentationSyncer
from resinai.utils import TaskExtractor, JSONHandler

def automate_epic_progress(epic_id: str):
    """Automate progress tracking for entire epic."""
    
    # Mock input data (replace with real data source)
    input_data = {
        "session_id": f"automation-{epic_id}",
        "tool_input": {
            "todos": [
                {
                    "id": f"{epic_id}.01.01",
                    "content": f"Epic {epic_id} task 1",
                    "status": "completed",
                    "priority": "high"
                }
            ]
        }
    }
    
    # Update progress documentation
    progress_updater = ProgressUpdater()
    result1 = progress_updater.update_progress(input_data)
    
    # Sync documentation hierarchy
    doc_syncer = DocumentationSyncer()
    result2 = doc_syncer.sync_documentation(input_data)
    
    print(f"Epic {epic_id} automation: Progress={result1}, Docs={result2}")

if __name__ == "__main__":
    automate_epic_progress("0003")
```

## Summary

The ResIn.AI Orchestrator CLI provides a comprehensive, enterprise-grade solution for multi-agent orchestration hook automation. With its modern Python architecture, rich user interface, and extensive integration capabilities, it serves as the foundation for sophisticated development workflow automation.

Key benefits:
- ✅ **Modern CLI framework** with Typer + Rich
- ✅ **Clean architecture** without import conflicts  
- ✅ **Comprehensive validation** and error handling
- ✅ **Rich documentation** and progress tracking
- ✅ **Flexible integration** options for any workflow
- ✅ **Enterprise reliability** with comprehensive logging and monitoring
