<!-- Updated: 2025-11-08 14:35:31 UTC -->

## TMUX ENVIRONMENT REQUIREMENTS

Universal requirements that ALL orchestrator commands MUST follow for TMUX environment verification. Every command MUST verify TMUX before proceeding.

### CRITICAL REQUIREMENTS
- **MUST** verify `$TMUX_PANE` environment variable is set before proceeding
- **MUST** stop immediately and report error if not running in TMUX
- **MUST** provide clear instructions for starting TMUX session
- **MUST** log TMUX pane ID when verification succeeds

### CRITICAL RESTRICTIONS
- **NEVER** proceed without TMUX verification

## PROCESS DEFINITION

### Phase 00: Verify TMUX Environment
Verify that orchestrator is running in a TMUX session

#### CRITICAL REQUIREMENTS
- **MUST** check `$TMUX_PANE` environment variable
- **MUST** stop execution if not in TMUX
- **MUST** provide clear error message with instructions
- **MUST** log pane ID on success

#### CRITICAL RESTRICTIONS
- **NEVER** proceed without TMUX verification
- **NEVER** continue if `$TMUX_PANE` is empty or undefined

#### EXECUTION FLOW

- **Check TMUX environment**
  - Execute: `echo $TMUX_PANE`
  - Store result in variable

- **Evaluate result**
  - **When empty or undefined**:
    - **MUST** read and use `plugin:orchestrator:resources://TEMPLATE/REPORT/TMUX-ERROR.md` to report error
    - **MUST** read and follow requirements from `plugin:orchestrator:resources://CORE/TEMPLATE-REQUIREMENTS.md`
    - **MUST** preserve template organization  
    - **STOP** immediately
    - **DO NOT PROCEED** - exit orchestration

  - **When valid pane ID** (e.g., "%0", "%1", etc.):
    - Log: "TMUX verified: pane {TMUX_PANE}"
    - Continue to next phase
