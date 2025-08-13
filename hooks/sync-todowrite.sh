#!/bin/bash

# TodoWrite Documentation Sync Hook - Simple [EEEE.SS.TT] - [SESSION_ID].log Format
# This script is triggered after TodoWrite tool usage to log task progress updates
# Logs to same format as Task hook: [EEEE.SS.TT] - [SESSION_ID].log
# Receives JSON input via stdin containing session and event data

# Read JSON input from stdin
INPUT=$(cat)

# Extract relevant information from JSON
TIMESTAMP=$(date)
SESSION_ID=$(echo "$INPUT" | jq -r '.session_id // "unknown"' 2>/dev/null || echo "unknown")
TOOL_NAME=$(echo "$INPUT" | jq -r '.tool_name // "TodoWrite"' 2>/dev/null || echo "TodoWrite")
TODOS=$(echo "$INPUT" | jq -r '.tool_input.todos' 2>/dev/null || echo "[]")

echo "[HOOK] $TOOL_NAME simple progress logging triggered at $TIMESTAMP for session $SESSION_ID" >&2

# Create logs directory in current project
LOGS_BASE=".claude/logs"
mkdir -p "$LOGS_BASE"

# Extract task IDs from todos (both IDs and content) for task-specific logging
TASK_PATTERN='[0-9]{4}\.[0-9]{2}\.[0-9]{2}'
TASK_IDS=$(echo "$TODOS" | jq -r '.[] | select(.id) | .id' 2>/dev/null)
CONTENT_TASK_IDS=$(echo "$TODOS" | jq -r '.[].content' 2>/dev/null | grep -oE "$TASK_PATTERN")
ALL_TASK_IDS=$(echo "$TASK_IDS $CONTENT_TASK_IDS" | tr ' ' '\n' | grep -E "$TASK_PATTERN" | sort -u | head -10)
LOGGED_TASKS=""

for TASK_ID in $ALL_TASK_IDS; do
    # Log to same [EEEE.SS.TT] - [SESSION_ID].log file as Task hook
    TASK_LOG="$LOGS_BASE/${TASK_ID} - ${SESSION_ID}.log"

    # Get all todos related to this task ID
    TASK_CONTENT=$(echo "$TODOS" | jq -r ".[] | select(.id==\"$TASK_ID\" or (.content | test(\"$TASK_ID\"))) | .content" 2>/dev/null)
    TASK_STATUS=$(echo "$TODOS" | jq -r ".[] | select(.id==\"$TASK_ID\" or (.content | test(\"$TASK_ID\"))) | .status" 2>/dev/null)

    if [ -n "$TASK_CONTENT" ]; then
        echo "[$TIMESTAMP] ORCHESTRATOR -> PROGRESS UPDATE: $TASK_ID ($TASK_STATUS)" >> "$TASK_LOG"
        echo "[$TIMESTAMP] Task: $TASK_CONTENT" >> "$TASK_LOG"
        echo "" >> "$TASK_LOG"

        LOGGED_TASKS="$LOGGED_TASKS $TASK_ID"
        echo "[HOOK] Updated task progress log: ${TASK_ID} - ${SESSION_ID}.log" >&2
    fi
done

# If no task-specific IDs found, create a general progress log
if [ -z "$LOGGED_TASKS" ]; then
    SESSION_LOG="$LOGS_BASE/progress - ${SESSION_ID}.log"
    echo "[$TIMESTAMP] ORCHESTRATOR -> PROGRESS UPDATE: General todos" >> "$SESSION_LOG"
    echo "[$TIMESTAMP] Todo count: $(echo "$TODOS" | jq length 2>/dev/null)" >> "$SESSION_LOG"
    echo "[$TIMESTAMP] Updates: $(echo "$TODOS" | jq -c '.[].content' 2>/dev/null | head -c 200)..." >> "$SESSION_LOG"
    echo "" >> "$SESSION_LOG"

    echo "[HOOK] Created general progress log: progress - ${SESSION_ID}.log" >&2
fi

echo "[HOOK] Simple TodoWrite progress logging completed at $TIMESTAMP" >&2
exit 0
