<!-- Updated: 2025-10-14 18:50:00 UTC -->

### Phase {PHASE_NUMBER}: {PHASE_NAME}
Work execution for {WORK_LEVEL} scope

#### CRITICAL REQUIREMENTS
- **MUST** discover appropriate agent based on work requirements
- **MUST** deliver complete work output
- **MUST** validate against quality standards

#### CRITICAL RESTRICTIONS
- **NEVER** accept incomplete deliverables
- **NEVER** skip validation checks
- **NEVER** proceed without quality verification

#### EXECUTION FLOW

- **Update phase tracking**
  - Update "Phase {PHASE_NUMBER}: {PHASE_NAME}" task as in_progress

- **Define work scope**
  - Work identifier: {WORK_IDENTIFIER}
  - Work description: {WORK_DESCRIPTION}
  - Work requirements: {WORK_REQUIREMENTS}
  - Quality standards: {QUALITY_STANDARDS}
  - Iteration count: {ITERATION_COUNT}

- **Discover appropriate agent**
  - Analyze work type and requirements
  - Define required capabilities and expertise
  - Use internal knowledge of available agents and their capabilities
  - Filter agents to match agent expertise against required capabilities and expertise
  - Score each agent based on required capabilities and expertise compatibility
  - Only keep highest scoring agents with score > 75
  - Select highest scoring agent

  - **Report agent selection**
    - **MUST** read and use `plugin:orchestrator:resources://TEMPLATE/REPORT/AGENT-DISCOVERY.md` as a template
    - **MUST** read and follow requirements from `plugin:orchestrator:resources://CORE/TEMPLATE-REQUIREMENTS.md`

- **Prepare delegation context**
  - Package work specifications
  - Include acceptance criteria
  - Provide iteration feedback if applicable
  - Set quality expectations
  - Include relevant context from previous states

- **Delegate to agent**
  - **MUST** read and use `plugin:orchestrator:resources://TEMPLATE/REPORT/AGENT-DELEGATION.md` as a template
  - **MUST** read and follow requirements from `plugin:orchestrator:resources://CORE/TEMPLATE-REQUIREMENTS.md`
  - Invoke selected agent
  - Monitor work progress

- **Validate work output**
  - Verify deliverable completeness
  - Check for missing components
  - Validate quality criteria met
  - Ensure conventions followed
  - Confirm acceptance criteria satisfied

- **Determine transition**
  - Use return code from agent execution
  - Follow state transition table from orchestration requirements
  - Prepare feedback if needed for next iteration

- **Complete phase**
  - Update "Phase {PHASE_NUMBER}: {PHASE_NAME}" task as completed
  - Transition to {NEXT_STATE} based on return code
