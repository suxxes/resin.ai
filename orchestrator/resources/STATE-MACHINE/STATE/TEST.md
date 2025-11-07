<!-- Updated: 2025-09-28 00:00:00 UTC -->

### Phase {PHASE_NUMBER}: {PHASE_NAME}
Quality validation for {WORK_LEVEL} scope

#### CRITICAL REQUIREMENTS
- **MUST** discover QA agent
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

- **Discover appropriate agent**
  - Define quality assurance agent requirements
  - Use internal knowledge of available agents and their capabilities
  - Filter agents to match agent expertise against quality assurance requirements
  - Score each agent based on quality assurance requirements compatibility
  - Only keep highest scoring agents with score > 75
  - Select highest scoring QA agent

  - **Report agent selection**
    - **MUST** read and use `plugin:orchestrator:resources://TEMPLATE/REPORT/AGENT-DISCOVERY.md` as a template
    - **MUST** read and follow requirements from `plugin:orchestrator:resources://CORE/TEMPLATE-REQUIREMENTS.md`

- **Prepare delegation context**
  - Package implementation details
  - Specify validation criteria
  - Include quality thresholds
  - Provide previous iteration issues if applicable

- **Delegate to agent**
  - **MUST** read and use `plugin:orchestrator:resources://TEMPLATE/REPORT/AGENT-DELEGATION.md` as a template
  - **MUST** read and follow requirements from `plugin:orchestrator:resources://CORE/TEMPLATE-REQUIREMENTS.md`
  - Invoke selected QA agent
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
    - Set `NEXT_STATE` to {DONE_STATE}
  - When validation fails:
    - Collect information about found issues
    - Prepare feedback report
    - **MUST** read and use `plugin:orchestrator:resources://TEMPLATE/REPORT/ITERATION-FEEDBACK.md` as a template
    - **MUST** read and follow requirements from `plugin:orchestrator:resources://CORE/TEMPLATE-REQUIREMENTS.md`
    - Set `NEXT_STATE` to {WORK_STATE} with feedback

- **Complete phase**
  - Update "Phase {PHASE_NUMBER}: {PHASE_NAME}" task as completed
  - Transition to determined {NEXT_STATE}
