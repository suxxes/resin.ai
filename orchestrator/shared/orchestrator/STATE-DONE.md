<!-- Updated: 2025-09-28 00:00:00 UTC -->

### Phase {PHASE_NUMBER}: {PHASE_NAME}
Completion validation for {WORK_LEVEL} scope

#### CRITICAL REQUIREMENTS
- **MUST** discover validation specialist subagent
- **MUST** verify all acceptance criteria
- **MUST** confirm business value delivered

#### CRITICAL RESTRICTIONS
- **NEVER** mark incomplete work as done
- **NEVER** skip acceptance validation
- **NEVER** ignore integration issues

#### EXECUTION FLOW

- **Update phase tracking**
  - Update "Phase {PHASE_NUMBER}: {PHASE_NAME}" task as in_progress

- **Define acceptance scope**
  - Work identifier: {WORK_IDENTIFIER}
  - Business criteria: {BUSINESS_CRITERIA}
  - Technical criteria: {TECHNICAL_CRITERIA}
  - Integration requirements: {INTEGRATION_REQUIREMENTS}
  - Quality standards: {QUALITY_STANDARDS}

- **Discover appropriate subagent**
  - Define validation specialist requirements
  - Find all available validation subagents
  - Score based on {WORK_LEVEL} expertise
  - Select highest scoring validator

  - **Report subagent selection**
    - **MUST** read and use `~/.claude/shared/templates/REPORT/SUBAGENT-DISCOVERY.md` file as a template
    - **MUST** read and follow requirements from `~/.claude/shared/core/TEMPLATE-REQUIREMENTS.md` file

- **Prepare delegation context**
  - Package completed work details
  - Include acceptance criteria
  - Provide test results
  - Set validation expectations

- **Delegate to subagent**
  - **MUST** read and use `~/.claude/shared/templates/REPORT/SUBAGENT-DELEGATION.md` file as a template
  - **MUST** read and follow requirements from `~/.claude/shared/core/TEMPLATE-REQUIREMENTS.md` file
  - Invoke selected validator
  - Monitor validation progress

- **Validate acceptance output**
  - Verify business requirements met
  - Confirm technical criteria satisfied
  - Check integration successful
  - Validate documentation complete
  - Assess production readiness

- **Determine completion status**
  - When validation passes:
    - Mark work item as completed
    - Update progress tracking
    - **Report completion**
      - **MUST** read and use `~/.claude/shared/templates/REPORT/STATE-DONE.md` file as a template
      - **MUST** read and follow requirements from `~/.claude/shared/core/TEMPLATE-REQUIREMENTS.md` file
    - Transition to {CONTROLLER_STATE}
  - When validation fails:
    - Document unmet criteria
    - Determine corrective action
    - Transition to appropriate state

- **Complete phase**
  - Update "Phase {PHASE_NUMBER}: {PHASE_NAME}" task as completed
  - Update parent context with completion status
  - Transition to determined state
