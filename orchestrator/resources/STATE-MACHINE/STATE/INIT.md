<!-- Updated: 2025-09-28 00:00:00 UTC -->

### Phase {PHASE_NUMBER}: {PHASE_NAME}
Discovery and planning for {WORK_LEVEL} scope

#### CRITICAL REQUIREMENTS
- **MUST** analyze work scope and complexity
- **MUST** discover appropriate planning agent
- **MUST** create comprehensive breakdown if needed

#### CRITICAL RESTRICTIONS
- **NEVER** proceed without scope validation
- **NEVER** skip dependency analysis
- **NEVER** create incomplete breakdowns

#### EXECUTION FLOW

- **Update phase tracking**
  - Update "Phase {PHASE_NUMBER}: {PHASE_NAME}" task as in_progress

- **Define scope and requirements**
  - Identifier: {IDENTIFIER}
  - Description: {DESCRIPTION}
  - Complexity assessment: {COMPLEXITY_LEVEL}
  - Breakdown requirements: {BREAKDOWN_NEEDED}

- **Discover and filter agents**
  - Define discovery limitations based on {WORK_LEVEL} requirements
  - Use internal knowledge of available agents and their capabilities
  - Filter agents to match agent expertise against discovery limitations
  - Score each agent based on discovery limitations compatibility
  - Only keep highest scoring agents with score > 75
  - Select top-most agent from the list of highest scoring agents

  - **Ensure agent availability**
    - When no suitable agent found:
      - **MUST** stop and exit immediately with error report

  - **Report agent selection**
    - **MUST** read and use `plugin:orchestrator:resources://TEMPLATE/REPORT/AGENT-DISCOVERY.md` as a template
    - **MUST** read and follow requirements from `plugin:orchestrator:resources://CORE/TEMPLATE-REQUIREMENTS.md`
    - Include each and every discovered agent, including irrelevant ones
    - Include each and every highest scoring agent

- **Prepare delegation context**
  - Extract relevant project information
  - Specify expected deliverables for {WORK_LEVEL}
  - Determine quality standards
  - Package into planning context

- **Delegate to agent**
  - **MUST** read and use `plugin:orchestrator:resources://TEMPLATE/REPORT/AGENT-DELEGATION.md` as a template
  - **MUST** read and follow requirements from `plugin:orchestrator:resources://CORE/TEMPLATE-REQUIREMENTS.md`
  - Invoke selected planning agent
  - Monitor delegation progress

- **Validate planning output**
  - Verify breakdown completeness
  - Check dependency mapping
  - Validate acceptance criteria
  - Ensure naming conventions

- **Complete phase**
  - Update "Phase {PHASE_NUMBER}: {PHASE_NAME}" task as completed
  - Transition to {NEXT_STATE}
