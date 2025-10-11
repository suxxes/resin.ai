#!/bin/bash

# Documentation Sync Hook
# =======================
# Syncs progress across Epic/Story/Task documentation files
# Supports parallel agent execution with file locking
#
# Input: JSON via stdin with TodoWrite session and event data
# Output: Updates documentation files if they exist

INPUT=$(cat)
TIMESTAMP=$(date)
SESSION_ID=$(echo "$INPUT" | jq -r '.session_id // "unknown"' 2>/dev/null || echo "unknown")
TODOS=$(echo "$INPUT" | jq -r '.tool_input.todos' 2>/dev/null || echo "[]")

echo "[HOOK] Documentation sync triggered" >&2

# Setup logging
LOGS_BASE=".claude/logs"
mkdir -p "$LOGS_BASE"

# File locking for parallel execution
LOCK_FILE="/tmp/doc-sync-${SESSION_ID}.lock"
exec 200>"$LOCK_FILE"
if ! flock -w 5 200; then
    echo "[HOOK] Waiting for lock..." >&2
    flock 200
fi

# Extract task IDs (format: XXXX.YY.ZZ)
TASK_PATTERN='[0-9]{4}\.[0-9]{2}\.[0-9]{2}'
TASK_IDS=$(echo "$TODOS" | jq -r '.[].content' 2>/dev/null | grep -oE "$TASK_PATTERN" | sort -u)

if [ -z "$TASK_IDS" ]; then
    echo "[HOOK] No task IDs found" >&2
    flock -u 200
    exit 0
fi

# Check for documentation directory
DOC_BASE="docs/DEVELOPMENT-PLAN"
if [ ! -d "$DOC_BASE" ]; then
    echo "[HOOK] Documentation directory not found" >&2
    flock -u 200
    exit 0
fi

# Process each task
for TASK_ID in $TASK_IDS; do
    # Get task status from todos
    TASK_STATUS=$(echo "$TODOS" | jq -r ".[] | select(.content | test(\"$TASK_ID\")) | .status" 2>/dev/null | head -1)

    if [ -z "$TASK_STATUS" ]; then
        continue
    fi

    echo "[HOOK] Updating $TASK_ID ($TASK_STATUS)" >&2

    # Find and update task file
    TASK_FILE=$(find "$DOC_BASE" -name "${TASK_ID} - *.md" -type f 2>/dev/null | head -1)
    if [ -n "$TASK_FILE" ]; then
        # Append simple status update
        {
            echo ""
            echo "## Status Update"
            echo "**Status**: $TASK_STATUS"
            echo "**Updated**: $TIMESTAMP"
        } >> "$TASK_FILE"
    fi

    # Log update
    echo "[$TIMESTAMP] Updated documentation for $TASK_ID" >> "${LOGS_BASE}/${TASK_ID} - ${SESSION_ID}.log"
done

# Release lock
flock -u 200

echo "[HOOK] Documentation sync completed" >&2
exit 0
