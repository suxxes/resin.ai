#!/bin/bash

# Task Tool Coordination Logging Hook - Simple [EEEE.SS.TT] - [SESSION_ID].log Format
# This script is triggered after Task tool usage to log agent delegation and coordination activities
# Creates simple log files in format: [EEEE.SS.TT] - [SESSION_ID].log
# Receives JSON input via stdin containing session and event data

# Read JSON input from stdin
INPUT=$(cat)

# Extract relevant information from JSON
TIMESTAMP=$(date)
SESSION_ID=$(echo "$INPUT" | jq -r '.session_id // "unknown"' 2>/dev/null || echo "unknown")
TOOL_NAME=$(echo "$INPUT" | jq -r '.tool_name // "Task"' 2>/dev/null || echo "Task")
SUBAGENT_TYPE=$(echo "$INPUT" | jq -r '.tool_input.subagent_type // "unknown"' 2>/dev/null || echo "unknown")
DESCRIPTION=$(echo "$INPUT" | jq -r '.tool_input.description // "No description"' 2>/dev/null || echo "No description")
PROMPT=$(echo "$INPUT" | jq -r '.tool_input.prompt // ""' 2>/dev/null || echo "")

echo "[HOOK] $TOOL_NAME simple coordination logging triggered at $TIMESTAMP for session $SESSION_ID" >&2

# Create logs directory in current project
LOGS_BASE=".claude/logs"
mkdir -p "$LOGS_BASE"

# Extract task context from description or prompt for task-specific logging
TASK_PATTERN='[0-9]{4}\.[0-9]{2}\.[0-9]{2}'
TASK_ID=$(echo "$DESCRIPTION $PROMPT" | grep -oE "$TASK_PATTERN" | head -1)

if [ -n "$TASK_ID" ]; then
    # Create simple [EEEE.SS.TT] - [SESSION_ID].log file
    TASK_LOG="$LOGS_BASE/${TASK_ID} - ${SESSION_ID}.log"
    echo "[$TIMESTAMP] ORCHESTRATOR -> AGENT DELEGATION: $SUBAGENT_TYPE" >> "$TASK_LOG"
    echo "[$TIMESTAMP] Task: $TASK_ID" >> "$TASK_LOG"
    echo "[$TIMESTAMP] Description: $DESCRIPTION" >> "$TASK_LOG"
    echo "[$TIMESTAMP] Agent: $SUBAGENT_TYPE" >> "$TASK_LOG"
    echo "[$TIMESTAMP] Context: $(echo "$PROMPT" | head -c 100)..." >> "$TASK_LOG"
    echo "" >> "$TASK_LOG"

    echo "[HOOK] Created task log: ${TASK_ID} - ${SESSION_ID}.log" >&2
else
    # If no task ID found, create a general session log
    SESSION_LOG="$LOGS_BASE/general - ${SESSION_ID}.log"
    echo "[$TIMESTAMP] ORCHESTRATOR -> AGENT DELEGATION: $SUBAGENT_TYPE" >> "$SESSION_LOG"
    echo "[$TIMESTAMP] Description: $DESCRIPTION" >> "$SESSION_LOG"
    echo "[$TIMESTAMP] Agent: $SUBAGENT_TYPE" >> "$SESSION_LOG"
    echo "[$TIMESTAMP] Context: $(echo "$PROMPT" | head -c 100)..." >> "$SESSION_LOG"
    echo "" >> "$SESSION_LOG"

    echo "[HOOK] Created general session log: general - ${SESSION_ID}.log" >&2
fi

# No legacy compatibility needed - only use simple [EEEE.SS.TT] - [SESSION_ID].log format

echo "[HOOK] Simple Task coordination logging completed at $TIMESTAMP" >&2
exit 0
