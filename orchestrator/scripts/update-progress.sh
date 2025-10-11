#!/bin/bash

# Project-Level Progress Update Hook
# ===================================
# Updates project roadmap file when TodoWrite changes orchestration status
# Only runs for project-level work (when DEVELOPMENT-PLAN.md exists)
#
# Input: JSON via stdin with TodoWrite session and event data
# Output: Updates DEVELOPMENT-PLAN.md if it exists

INPUT=$(cat)
TIMESTAMP=$(date)
SESSION_ID=$(echo "$INPUT" | jq -r '.session_id // "unknown"' 2>/dev/null || echo "unknown")
TODOS=$(echo "$INPUT" | jq -r '.tool_input.todos' 2>/dev/null || echo "[]")

# Check if this is project-level work
PROGRESS_FILE="docs/DEVELOPMENT-PLAN.md"
if [ ! -f "$PROGRESS_FILE" ]; then
    # Not project-level work, exit silently
    exit 0
fi

echo "[HOOK] Project progress update triggered at $TIMESTAMP" >&2

# Setup logging
LOGS_BASE=".claude/logs"
mkdir -p "$LOGS_BASE"

# Extract task ID if present (format: XXXX.YY.ZZ)
TASK_PATTERN='[0-9]{4}\.[0-9]{2}\.[0-9]{2}'
TASK_ID=$(echo "$TODOS" | jq -r '.[].content' 2>/dev/null | grep -oE "$TASK_PATTERN" | head -1)

# Log to appropriate file
LOG_FILE="${LOGS_BASE}/project-${SESSION_ID}.log"
echo "[$TIMESTAMP] Project progress update hook executed" >> "$LOG_FILE"

# Extract current orchestration level from todos
ORCH_PATTERN="(EPIC|STORY|TASK|Planning|Implementation|Validation)"
CURRENT_LEVEL=$(echo "$TODOS" | jq -r '.[] | select(.status=="in_progress") | .content' 2>/dev/null | grep -oE "$ORCH_PATTERN" | head -1)

if [ -n "$CURRENT_LEVEL" ]; then
    # Simple sed replacement for status updates
    sed -i.bak "s/^- Orchestration Level:.*$/- Orchestration Level: $CURRENT_LEVEL/" "$PROGRESS_FILE" 2>/dev/null
    sed -i.bak "s/^- Last Updated:.*$/- Last Updated: $TIMESTAMP/" "$PROGRESS_FILE" 2>/dev/null
    rm -f "${PROGRESS_FILE}.bak"

    echo "[HOOK] Updated project orchestration level: $CURRENT_LEVEL" >&2
fi

echo "[HOOK] Project progress update completed" >&2
exit 0
