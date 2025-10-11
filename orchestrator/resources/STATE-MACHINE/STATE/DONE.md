<!-- Updated: 2025-10-17 20:32:34 UTC -->

### Phase {PHASE_NUMBER}: {PHASE_NAME}
Completion validation for {WORK_LEVEL} scope

#### CRITICAL REQUIREMENTS
- **MUST** discover validation agent
- **MUST** verify all acceptance criteria
- **MUST** confirm business value delivered
- **MUST** transition immediately after validation
- **MUST** never wait for user acknowledgment during autonomous execution
- **MUST** use radical brevity in completion reports (template only, no elaboration)

#### CRITICAL RESTRICTIONS
- **NEVER** mark incomplete work as done
- **NEVER** skip acceptance validation
- **NEVER** ignore integration issues
- **NEVER** pause after completion for reporting
- **NEVER** wait for user input during loop execution
- **NEVER** add verbose summaries or multi-paragraph context to completion reports

#### EXECUTION FLOW

- **Update phase tracking**
  - Update "Phase {PHASE_NUMBER}: {PHASE_NAME}" task as in_progress

- **Define acceptance scope**
  - Work identifier: {WORK_IDENTIFIER}
  - Business criteria: {BUSINESS_CRITERIA}
  - Technical criteria: {TECHNICAL_CRITERIA}
  - Integration requirements: {INTEGRATION_REQUIREMENTS}
  - Quality standards: {QUALITY_STANDARDS}

- **Discover appropriate agent**
  - Define validation agent requirements
  - Use internal knowledge of available agents and their capabilities
  - Filter agents to match agent expertise against {WORK_LEVEL} expertise
  - Score each agent based on {WORK_LEVEL} expertise compatibility
  - Only keep highest scoring agents with score > 75
  - Select highest scoring validator

  - **Report agent selection**
    - **MUST** read and use `plugin:orchestrator:resources://TEMPLATE/REPORT/AGENT-DISCOVERY.md` as a template
    - **MUST** read and follow requirements from `plugin:orchestrator:resources://CORE/TEMPLATE-REQUIREMENTS.md`

- **Prepare delegation context**
  - Package completed work details
  - Include acceptance criteria
  - Provide test results
  - Set validation expectations

- **Delegate to agent**
  - **MUST** read and use `plugin:orchestrator:resources://TEMPLATE/REPORT/AGENT-DELEGATION.md` as a template
  - **MUST** read and follow requirements from `plugin:orchestrator:resources://CORE/TEMPLATE-REQUIREMENTS.md`
  - Invoke selected validator
  - Monitor validation progress

- **Validate acceptance output**
  - Verify business requirements met
  - Confirm technical criteria satisfied
  - Check integration successful
  - Validate documentation complete
  - Assess production readiness

- **Manage branch operations**:
  - When branch merging is required for {WORK_LEVEL}:
    - **MUST** merge work branch into appropriate target branch
    - **MUST** ensure all commits are included in merge
    - **MUST** use meaningful merge commit message describing completion
    - **MUST** include work identifier in merge message (e.g., "type({WORK_ID}): complete {WORK_NAME}")
    - **MUST** verify merge completes successfully
    - **NEVER** leave work branch unmerged

- **Determine completion status**
  - When validation succeeds:
    - Mark work item as completed
    - Update progress tracking
    - **MUST** read and use `plugin:orchestrator:resources://TEMPLATE/REPORT/STATE-DONE.md` as a template
    - **MUST** read and follow requirements from `plugin:orchestrator:resources://CORE/TEMPLATE-REQUIREMENTS.md`
    - **MUST** include branch merge confirmation when applicable
    - **MUST** use radical brevity (template only, no additional context)
    - **MUST** output completion report inline without stopping
    - Set `NEXT_STATE` to {PARENT_LOOP_STATE}
  - Otherwise:
    - Mention unmet criteria
    - Determine corrective action
    - Set `NEXT_STATE` to appropriate next state

- **Complete phase**
  - Update "Phase {PHASE_NUMBER}: {PHASE_NAME}" task as completed
  - Update parent context with completion status
  - **MUST** transition IMMEDIATELY to {NEXT_STATE} without pausing
  - **NEVER** wait for user acknowledgment
