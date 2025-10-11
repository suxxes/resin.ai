<!-- Updated: 2025-09-28 00:00:00 UTC -->

### Phase {PHASE_NUMBER}: {PHASE_NAME}
Quality validation for {WORK_LEVEL} scope

#### CRITICAL REQUIREMENTS
- **MUST** discover QA specialist subagent
- **MUST** perform comprehensive validation
- **MUST** enforce quality standards

#### CRITICAL RESTRICTIONS
- **NEVER** pass failing tests
- **NEVER** ignore critical issues
- **NEVER** skip security validation

#### EXECUTION FLOW

- **Update phase tracking**
  - Update "Phase {PHASE_NUMBER}: {PHASE_NAME}" task as in_progress

- **Define validation scope**
  - Work identifier: {WORK_IDENTIFIER}
  - Implementation reference: {IMPLEMENTATION_REFERENCE}
  - Quality standards: {QUALITY_STANDARDS}
  - Coverage requirements: {COVERAGE_REQUIREMENTS}
  - Iteration count: {ITERATION_COUNT}

- **Discover appropriate subagent**
  - Define QA specialist requirements
  - Find all available QA subagents
  - Score based on validation capabilities
  - Select highest scoring QA specialist

  - **Report subagent selection**
    - **MUST** read and use `~/.claude/shared/templates/REPORT/SUBAGENT-DISCOVERY.md` file as a template
    - **MUST** read and follow requirements from `~/.claude/shared/core/TEMPLATE-REQUIREMENTS.md` file

- **Prepare delegation context**
  - Package implementation details
  - Specify validation criteria
  - Include quality thresholds
  - Provide previous iteration issues if applicable

- **Delegate to subagent**
  - **MUST** read and use `~/.claude/shared/templates/REPORT/SUBAGENT-DELEGATION.md` file as a template
  - **MUST** read and follow requirements from `~/.claude/shared/core/TEMPLATE-REQUIREMENTS.md` file
  - Invoke selected QA specialist
  - Monitor validation progress

- **Validate test output**
  - Check all tests pass
  - Verify coverage achieved
  - Review security findings
  - Assess performance metrics
  - Identify critical issues

- **Determine transition**
  - When validation passes:
    - No critical issues found
    - Coverage requirements met
    - Transition to {DONE_STATE}
  - When validation fails:
    - Collect information about found issues
    - Prepare feedback report
    - **MUST** read and use `~/.claude/shared/templates/REPORT/ITERATION-FEEDBACK.md` file as a template
    - **MUST** read and follow requirements from `~/.claude/shared/core/TEMPLATE-REQUIREMENTS.md` file
    - Transition to {WORK_STATE} with feedback

- **Complete phase**
  - Update "Phase {PHASE_NUMBER}: {PHASE_NAME}" task as completed
  - Transition to determined state
