#!/bin/bash
# Ping-pong hook - tracks active sessions via file presence
# Creates session file ONLY on active work events, deletes on SessionEnd
# File existence = session is actively working (not just open)
# Renames tmux session to match Claude Code session ID
# Updated: 2025-11-08 22:43:51 UTC

# Enable debug logging by setting PING_PONG_DEBUG=1 or DEBUG=1
DEBUG="${PING_PONG_DEBUG:-${DEBUG:-0}}"

# Parse session info from stdin JSON
STDIN_INPUT=$(cat)
SESSION_ID=$(echo "$STDIN_INPUT" | jq -r '.session_id // empty')
EVENT_NAME=$(echo "$STDIN_INPUT" | jq -r '.hook_event_name // "unknown"')
TOOL_NAME=$(echo "$STDIN_INPUT" | jq -r '.tool_name // empty')
PROJECT_DIR=$(echo "$STDIN_INPUT" | jq -r '.cwd // empty')
TMUX_SESSION=$(echo "$STDIN_INPUT" | jq -r '.tmux_session // empty')

# Read todos from file (stored in ~/.claude/todos/)
TODO_FILE="$HOME/.claude/todos/${SESSION_ID}-agent-${SESSION_ID}.json"
if [ -f "$TODO_FILE" ]; then
  TODOS=$(cat "$TODO_FILE")
else
  TODOS=""
fi

# Fallback to environment variables if JSON parsing fails
EVENT_NAME="${EVENT_NAME:-${hook_event_name:-unknown}}"
PROJECT_DIR="${PROJECT_DIR:-${CLAUDE_PROJECT_DIR:-.}}"

# Use CLAUDE_PLUGIN_ROOT for .sessions storage (system-wide)
PLUGIN_ROOT="${CLAUDE_PLUGIN_ROOT:-.}"

# Normalize project folder name to safe directory name
# Example: /Users/dev/My Project -> users_dev_my_project
NORMALIZED_DIR=$(echo "$PROJECT_DIR" | tr '[:upper:]' '[:lower:]' | sed 's|^/||' | tr '/ ' '__')

# Session directory and file paths (stored in plugin root)
SESSION_DIR="$PLUGIN_ROOT/.sessions/$NORMALIZED_DIR"
SESSION_FILE="$SESSION_DIR/${SESSION_ID}.txt"
LOG_DIR="$SESSION_DIR/logs"
LOG_FILE="$LOG_DIR/${SESSION_ID}.log"

# Helper function for debug logging
log_debug() {
  if [ "$DEBUG" = "1" ]; then
    mkdir -p "$LOG_DIR"
    echo "$@" >> "$LOG_FILE"
  fi
}

# Helper function to rename tmux session to match Claude Code session
rename_tmux_session() {
  if [ -n "$TMUX_PANE" ] && [ -n "$SESSION_ID" ]; then
    # Get current tmux session name
    CURRENT_SESSION=$(tmux display-message -p "#{session_name}" 2>/dev/null)

    # Only rename if it's different from SESSION_ID
    if [ -n "$CURRENT_SESSION" ] && [ "$CURRENT_SESSION" != "$SESSION_ID" ]; then
      tmux rename-session -t "$CURRENT_SESSION" "$SESSION_ID" 2>/dev/null
      if [ $? -eq 0 ]; then
        log_debug "Renamed tmux session from '$CURRENT_SESSION' to '$SESSION_ID'"
      else
        log_debug "Failed to rename tmux session (may already be named correctly)"
      fi
    else
      log_debug "Tmux session already named '$SESSION_ID' or no session found"
    fi
  fi
}

# Define which events indicate active work
# ONLY these events create/update the session file
ACTIVE_EVENTS="UserPromptSubmit PreToolUse PostToolUse"

# Define events that ALWAYS indicate work completion (delete session file unconditionally)
FINAL_EVENTS="SubagentStop"

# Define events that check for todos before deleting (todo-aware cleanup)
TODO_AWARE_EVENTS="SessionEnd Stop"

# All other events are passive - they don't create/update session files
# This means a session that's just open but not doing work won't be tracked


# Log timestamp and event (only if DEBUG enabled)
log_debug "========================================"
log_debug "Timestamp: $(date -u '+%Y-%m-%d %H:%M:%S UTC')"
log_debug "Event: $EVENT_NAME"
log_debug "Tool: $TOOL_NAME"
log_debug "Session ID: $SESSION_ID"
log_debug "Working Dir: $PROJECT_DIR"
log_debug ""

# Log all CLAUDE_ environment variables (only if DEBUG enabled)
if [ "$DEBUG" = "1" ]; then
  log_debug "CLAUDE_ Environment Variables:"
  env | grep '^CLAUDE_' | sort >> "$LOG_FILE"
  log_debug ""

  # Log stdin input (pretty-printed JSON)
  log_debug "Stdin Input (Full JSON):"
  echo "$STDIN_INPUT" | jq '.' 2>/dev/null >> "$LOG_FILE" || echo "$STDIN_INPUT" >> "$LOG_FILE"
  log_debug ""
fi

# Rename tmux session to match Claude Code session ID on SessionStart and UserPromptSubmit
if [ "$EVENT_NAME" = "SessionStart" ] || [ "$EVENT_NAME" = "UserPromptSubmit" ]; then
  rename_tmux_session
fi

# Handle FINAL completion events - always delete session file
for FINAL_EVENT in $FINAL_EVENTS; do
  if [ "$EVENT_NAME" = "$FINAL_EVENT" ]; then
    if [ -f "$SESSION_FILE" ]; then
      rm -f "$SESSION_FILE"
      log_debug "Final event: $EVENT_NAME - removed session file"
    else
      log_debug "Final event: $EVENT_NAME - no session file to remove"
    fi
    exit 0
  fi
done

# Handle todo-aware events - only delete session file if no active/pending todos
for TODO_EVENT in $TODO_AWARE_EVENTS; do
  if [ "$EVENT_NAME" = "$TODO_EVENT" ]; then
    # Check if there are any active or pending todos from the transcript
    TRANSCRIPT_PATH=$(echo "$STDIN_INPUT" | jq -r '.transcript_path // empty')

    log_debug "$EVENT_NAME event: checking for active todos"
    log_debug "Todos from stdin: $TODOS"

    # Check if todos are provided directly in stdin JSON
    if [ -n "$TODOS" ] && [ "$TODOS" != "null" ] && [ "$TODOS" != "empty" ]; then
      # Parse todos from stdin JSON
      HAS_ACTIVE_TODOS=$(echo "$TODOS" | jq -r '.[] | select(.status == "in_progress" or .status == "pending") | .content' 2>/dev/null | head -n 1)

      if [ -n "$HAS_ACTIVE_TODOS" ]; then
        log_debug "$EVENT_NAME event: has active/pending todos - keeping session file"
        log_debug "  First active todo: $HAS_ACTIVE_TODOS"

        # Log all active/pending todos for debugging
        ALL_TODOS=$(echo "$TODOS" | jq -r '.[] | select(.status == "in_progress" or .status == "pending") | "  - [\(.status)] \(.content)"' 2>/dev/null)

        if [ -n "$ALL_TODOS" ]; then
          log_debug "All active/pending todos found:"
          echo "$ALL_TODOS" | while IFS= read -r line; do
            log_debug "$line"
          done
        fi

        exit 0
      else
        log_debug "$EVENT_NAME event: no active todos found"
      fi
    else
      log_debug "$EVENT_NAME event: no todos provided in stdin, assuming no active todos"
    fi

    # No active todos, safe to delete session file
    if [ -f "$SESSION_FILE" ]; then
      rm -f "$SESSION_FILE"
      log_debug "$EVENT_NAME event: removed session file"
    else
      log_debug "$EVENT_NAME event: no session file to remove"
    fi
    exit 0
  fi
done

# Handle Notification events - check for idle_prompt
if [ "$EVENT_NAME" = "Notification" ]; then
  NOTIFICATION_TYPE=$(echo "$STDIN_INPUT" | jq -r '.notification_type // empty')
  log_debug "Notification event: type=$NOTIFICATION_TYPE"

  if [ "$NOTIFICATION_TYPE" = "idle_prompt" ]; then
    log_debug "Idle prompt notification detected - checking for active todos"

    # Check transcript for active/pending todos
    TRANSCRIPT_PATH=$(echo "$STDIN_INPUT" | jq -r '.transcript_path // empty')

    # Check if todos are provided directly in stdin JSON
    if [ -n "$TODOS" ] && [ "$TODOS" != "null" ] && [ "$TODOS" != "empty" ]; then
      # Parse todos from stdin JSON
      HAS_ACTIVE_TODOS=$(echo "$TODOS" | jq -r '.[] | select(.status == "in_progress" or .status == "pending") | .content' 2>/dev/null | head -n 1)

      if [ -n "$HAS_ACTIVE_TODOS" ]; then
        log_debug "Idle prompt: Found active todos:"
        log_debug "  First active todo: $HAS_ACTIVE_TODOS"

        # Log all active/pending todos for debugging
        ALL_TODOS=$(echo "$TODOS" | jq -r '.[] | select(.status == "in_progress" or .status == "pending") | "  - [\(.status)] \(.content)"' 2>/dev/null)

        if [ -n "$ALL_TODOS" ]; then
          log_debug "All active/pending todos found:"
          echo "$ALL_TODOS" | while IFS= read -r line; do
            log_debug "$line"
          done
        fi

        log_debug "Preparing to send continuation prompt"
        log_debug "Note: May occasionally interrupt user typing - accepted limitation"

        # Send continuation prompt to tmux pane
        if [ -n "$TMUX_PANE" ]; then
          # Pick random continuation message
          MESSAGES=(
            "Please continue working..."
            "Continue with the next tasks..."
            "Let's keep going..."
            "Please proceed..."
            "Continue..."
          )
          RANDOM_INDEX=$((RANDOM % ${#MESSAGES[@]}))
          MESSAGE="${MESSAGES[$RANDOM_INDEX]}"

          # Send message and Enter as separate commands with small delay
          tmux send-keys -t "$TMUX_PANE" "$MESSAGE" 2>/dev/null
          sleep 0.1
          tmux send-keys -t "$TMUX_PANE" Enter 2>/dev/null
          log_debug "Sent continuation to tmux pane $TMUX_PANE: $MESSAGE"
        else
          log_debug "No TMUX_PANE available for continuation"
        fi
      else
        log_debug "Idle prompt: No active todos found"
      fi
    else
      log_debug "Idle prompt: No todos provided in stdin"
    fi
  fi

  # Notifications are passive - don't update session file
  exit 0
fi

# Check if this is an active work event
IS_ACTIVE=0
for ACTIVE_EVENT in $ACTIVE_EVENTS; do
  if [ "$EVENT_NAME" = "$ACTIVE_EVENT" ]; then
    IS_ACTIVE=1
    break
  fi
done

# Only create/update session file for active work events
if [ $IS_ACTIVE -eq 1 ]; then
  # Create session directory if needed
  mkdir -p "$SESSION_DIR"

  # Create or update session file
  if [ -f "$SESSION_FILE" ]; then
    touch "$SESSION_FILE"
    log_debug "Activity: $EVENT_NAME (updated session file mtime)"
  else
    # Create new session file with tmux pane ID
    echo "${TMUX_PANE:-none}" > "$SESSION_FILE"
    log_debug "Activity: $EVENT_NAME (created session file for active work)"
  fi
else
  # Passive event - just log it, don't create/update session file
  log_debug "Event: $EVENT_NAME (passive - no session file update)"
fi

exit 0
