#!/bin/bash

# Quality Gate Validation Hook
# ============================
# Validates agent delegation based on task context
# Logs warnings but never blocks delegations
#
# Input: JSON via stdin with Task tool delegation event data
# Output: Always returns 0 (success) but logs context

INPUT=$(cat)
TIMESTAMP=$(date)
SESSION_ID=$(echo "$INPUT" | jq -r '.session_id // "unknown"' 2>/dev/null || echo "unknown")
SUBAGENT_TYPE=$(echo "$INPUT" | jq -r '.tool_input.subagent_type // "unknown"' 2>/dev/null || echo "unknown")
DESCRIPTION=$(echo "$INPUT" | jq -r '.tool_input.description // "No description"' 2>/dev/null || echo "No description")

echo "[HOOK] Validating delegation to $SUBAGENT_TYPE" >&2

# Setup logging
LOGS_BASE=".claude/logs"
mkdir -p "$LOGS_BASE"

# Extract task ID if present (format: XXXX.YY.ZZ)
TASK_PATTERN='[0-9]{4}\.[0-9]{2}\.[0-9]{2}'
TASK_ID=$(echo "$DESCRIPTION" | grep -oE "$TASK_PATTERN" | head -1)

# Log to appropriate file
LOG_FILE="${LOGS_BASE}/${TASK_ID:-orchestrator} - ${SESSION_ID}.log"
echo "[$TIMESTAMP] Delegation to $SUBAGENT_TYPE: ${DESCRIPTION:0:100}" >> "$LOG_FILE"

# Context-aware validation (informational only)
case "$SUBAGENT_TYPE" in
    "developer-"*)
        if echo "$DESCRIPTION" | grep -qiE "implement|build|create|fix|update"; then
            echo "[HOOK] Developer context found" >&2
        else
            echo "[HOOK] WARNING: Developer without clear implementation context" >&2
        fi
        ;;
    "quality-assurance")
        if [ -n "$TASK_ID" ] && [ -f "$LOG_FILE" ] && grep -q "developer-" "$LOG_FILE"; then
            echo "[HOOK] QA validation after implementation" >&2
        else
            echo "[HOOK] QA validation without prior implementation" >&2
        fi
        ;;
esac

echo "[HOOK] Delegation allowed" >&2
exit 0
