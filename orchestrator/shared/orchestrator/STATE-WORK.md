<!-- Updated: 2025-09-28 00:00:00 UTC -->

### Phase {PHASE_NUMBER}: {PHASE_NAME}
Implementation execution for {WORK_LEVEL} scope

#### CRITICAL REQUIREMENTS
- **MUST** discover developer based on task requirements
- **MUST** deliver complete implementation
- **MUST** validate against quality standards

#### CRITICAL RESTRICTIONS
- **NEVER** accept incomplete implementations
- **NEVER** skip validation checks
- **NEVER** allow placeholders or stubs

#### EXECUTION FLOW

- **Update phase tracking**
  - Update "Phase {PHASE_NUMBER}: {PHASE_NAME}" task as in_progress

- **Define implementation scope**
  - Work identifier: {WORK_IDENTIFIER}
  - Task requirements: {TASK_REQUIREMENTS}
  - Technology stack: {DETECTED_TECHNOLOGIES}
  - Quality standards: {QUALITY_STANDARDS}
  - Iteration count: {ITERATION_COUNT}

- **Discover appropriate subagent**
  - Analyze task type and requirements
  - Detect technology stack from codebase
  - Find all available developer subagents
  - Score based on technology compatibility
  - Select highest scoring developer

  - **Report subagent selection**
    - **MUST** read and use `~/.claude/shared/templates/REPORT/SUBAGENT-DISCOVERY.md` file as a template
    - **MUST** read and follow requirements from `~/.claude/shared/core/TEMPLATE-REQUIREMENTS.md` file

- **Prepare delegation context**
  - Package task specifications
  - Include acceptance criteria
  - Provide iteration feedback if applicable
  - Set quality expectations

- **Delegate to subagent**
  - **MUST** read and use `~/.claude/shared/templates/REPORT/SUBAGENT-DELEGATION.md` file as a template
  - **MUST** read and follow requirements from `~/.claude/shared/core/TEMPLATE-REQUIREMENTS.md` file
  - Invoke selected developer
  - Monitor implementation progress

- **Validate implementation output**
  - Verify code completeness
  - Check for placeholders/stubs
  - Validate build success
  - Ensure tests written
  - Confirm conventions followed

- **Determine transition**
  - When validation passes:
    - Transition to {TEST_STATE}
  - When validation fails:
    - Prepare iteration feedback
    - Transition to {WORK_STATE} with feedback

- **Complete phase**
  - Update "Phase {PHASE_NUMBER}: {PHASE_NAME}" task as completed
  - Transition to determined state
