<!-- Updated: 2025-09-28 00:00:00 UTC -->

### Phase {PHASE_NUMBER}: {PHASE_NAME}
Discovery and planning for {WORK_LEVEL} scope

#### CRITICAL REQUIREMENTS
- **MUST** analyze work scope and complexity
- **MUST** discover appropriate planning subagent
- **MUST** create comprehensive breakdown if needed

#### CRITICAL RESTRICTIONS
- **NEVER** proceed without scope validation
- **NEVER** skip dependency analysis
- **NEVER** create incomplete breakdowns

#### EXECUTION FLOW

- **Update phase tracking**
  - Update "Phase {PHASE_NUMBER}: {PHASE_NAME}" task as in_progress

- **Define scope and requirements**
  - Work identifier: {WORK_IDENTIFIER}
  - Work description: {WORK_DESCRIPTION}
  - Complexity assessment: {COMPLEXITY_LEVEL}
  - Breakdown requirements: {BREAKDOWN_NEEDED}

- **Discover appropriate subagent**
  - Define discovery limitations based on {WORK_LEVEL} requirements
  - Find all available and active subagents
  - Filter and score based on planning capabilities
  - Select highest scoring planning specialist

  - **Report subagent selection**
    - **MUST** read and use `~/.claude/shared/templates/REPORT/SUBAGENT-DISCOVERY.md` file as a template
    - **MUST** read and follow requirements from `~/.claude/shared/core/TEMPLATE-REQUIREMENTS.md` file

- **Prepare delegation context**
  - Extract relevant project information
  - Specify expected deliverables for {WORK_LEVEL}
  - Determine quality standards
  - Package into planning context

- **Delegate to subagent**
  - **MUST** read and use `~/.claude/shared/templates/REPORT/SUBAGENT-DELEGATION.md` file as a template
  - **MUST** read and follow requirements from `~/.claude/shared/core/TEMPLATE-REQUIREMENTS.md` file
  - Invoke selected planning specialist
  - Monitor delegation progress

- **Validate planning output**
  - Verify breakdown completeness
  - Check dependency mapping
  - Validate acceptance criteria
  - Ensure naming conventions

- **Complete phase**
  - Update "Phase {PHASE_NUMBER}: {PHASE_NAME}" task as completed
  - Transition to {NEXT_STATE}
