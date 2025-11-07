# Dry Run - Orchestration test mode

<!-- Updated: 2025-10-19 10:02:16 UTC -->

Enables simulation mode for orchestration commands. When active, all commands execute their real flows but with simulated agent responses instead of actual delegations. Supports testing both work orchestration and context enrichment flows.

## USAGE
- `/orchestrator:dryrun on` - Enable simulation mode
- `/orchestrator:dryrun off` - Disable simulation mode
- `/orchestrator:dryrun status` - Check current simulation mode

### With Simulation Mode Enabled
Execute actual commands which will use simulated responses:
- `/orchestrator:work` - Runs work orchestration with simulated agents
- `/orchestrator:work 0001` - Runs epic orchestration with simulated responses
- `/orchestrator:plan "Build feature"` - Runs plan orchestration with simulated responses

### Examples
```
/orchestrator:dryrun on
Simulation mode: ENABLED
All agent delegations will be simulated

/orchestrator:work "Fix authentication bug"
[Executes actual work command with simulated responses]

/orchestrator:dryrun off
Simulation mode: DISABLED
Normal operation restored
```

## CRITICAL REQUIREMENTS
- **MUST** set global SIMULATION_MODE flag when enabled
- **MUST** execute actual command flows (work, plan, etc.)
- **MUST** intercept agent delegations when in simulation mode
- **MUST** use standardized return codes from `plugin:orchestrator:resources://STATE-MACHINE/RETURN-CODES.md`
- **MUST** provide realistic simulated responses with proper structure

## CRITICAL RESTRICTIONS
- **NEVER** create actual files when in simulation mode
- **NEVER** invoke real agents when in simulation mode
- **NEVER** modify existing files when in simulation mode
- **NEVER** make git commits when in simulation mode
- **NEVER** skip any orchestration steps

## REPORTING WITH TEMPLATES

### Use Existing Report Templates

All reporting in dry run mode **MUST** use existing templates:

#### State Transitions
```
Read `plugin:orchestrator:resources://TEMPLATE/REPORT/STATE-TRANSITION.md`
```
Fill placeholders:
- `{FROM_STATE}`, `{TO_STATE}`, `{RETURN_CODE}`
- `{EPIC_NAME}`, `{STORY_NAME}`, `{TASK_NAME}`
- `{PHASE_ACCOMPLISHMENT_DESCRIPTION}`
- `{LOOP_INDICATORS}`, `{PROGRESS_PERCENTAGE}`

#### Agent Delegation
```
Read `plugin:orchestrator:resources://TEMPLATE/REPORT/AGENT-DELEGATION.md`
```
Fill placeholders:
- `{AGENT_NAME}`, `{WORK_IDENTIFIER}`
- `{DELEGATION_TYPE}`, `{QUALITY_STANDARDS}`
- `{PROVIDED_CONTEXT}`, `{EXPECTED_OUTPUTS}`

#### Iteration Feedback
```
Read `plugin:orchestrator:resources://TEMPLATE/REPORT/ITERATION-FEEDBACK.md`
```
Fill placeholders:
- `{WORK_IDENTIFIER}`, `{CURRENT_STATE}`
- `{ITERATION_NUMBER}`, `{MAX_ITERATIONS}`
- `{FAILURE_ANALYSIS}`, `{SPECIFIC_FIXES_REQUIRED}`

## IMPLEMENTATION

### Simulation Mode Flag
When `/dryrun on` is executed:
1. Set global `SIMULATION_MODE = true`
2. All subsequent commands check this flag
3. When `SIMULATION_MODE = true`:
   - Agent Task tool calls are intercepted
   - Instead of invoking agent, return simulated response
   - All other operations execute normally

### Integration Points
Commands that support simulation mode:
- `/work` - All orchestration levels
- `/plan` - All planning scopes
- Any command that uses agent delegation

### Context Enrichment Simulation

When simulating context enrichment flow:

1. **Question Phase** - Simulate user responses to requirements questions
2. **Validation Phase** - Confirm simulated requirements
3. **Documentation Phase** - Generate simulated enriched context ADR
4. **Delegation Phase** - Pass simulated enriched context to next agent

#### Simulated Requirements Questionnaire Flow

```
SIMULATING: Requirements Discovery

Loading questionnaire template: QUESTIONNAIRE.md (PROJECT level)

Question 1: Platform & Deployment
Simulated Answer: Web application, cloud deployment on AWS
Validated: ✓

Question 2: Technology Preferences
Simulated Answer: React, TypeScript, Node.js, PostgreSQL
Validated: ✓

[... additional questions ...]

VALIDATION CHECKLIST
✓ Technical Requirements captured
✓ Team Context documented
✓ Assumptions recorded

GENERATING: Enriched Context ADR
Format: Architecture Decision Record
Content: Validated requirements + documented assumptions
Status: Ready for delegation
```

#### Simulated Enriched Context Structure

```
SIMULATED ENRICHED CONTEXT

**Technical Requirements**:
- Platform: Web application (React/TypeScript)
- Deployment: AWS (ECS, RDS PostgreSQL)
- Integration: Auth0 for authentication, Stripe for payments
- Performance: Sub-200ms response time, 1000 concurrent users
- Security: SOC2 compliance, PII encryption

**Documented Assumptions** (ADR format):
- Modern web stack with TypeScript
- Cloud-native architecture
- Standard security practices
- Comprehensive testing coverage

**Enrichment Status**: COMPLETE
**Validation**: All requirements captured and validated
**Next Phase**: Pass to project-manager for epic planning
```

### How It Works
1. User runs `/orchestrator:dryrun on`
2. User runs actual command like `/orchestrator:work 0001.02.03` or `/orchestrator:plan "New feature"`
3. Command executes normally through all phases
4. When reaching agent delegation or requirements questions:
   - Check `if SIMULATION_MODE == true`
   - Skip actual Task tool invocation or user interaction
   - Generate appropriate simulated response
   - Continue with normal flow using simulated data
5. All state transitions, reports, and TodoWrite updates execute normally
6. Use existing report templates for all output
7. No actual files/code/documentation created

## SIMULATION RESPONSES

### Manager Agent Responses (with Enriched Context)

#### Product Manager (PROJECT level)
```
SIMULATED RESPONSE: Product Manager
Return Code: SUCCESS
Summary: Project architecture and epics defined

Enriched Context Used: YES
- Technical requirements validated
- Assumptions documented in ADR format
- No redundant questioning required

Deliverables:
- docs/OVERVIEW.md created
- docs/ARCHITECTURE.md created
- docs/TECH-STACK.md created
- docs/DEVELOPMENT-PLAN.md created
- 3 epics identified and documented

Validation: All project documentation complete
```

#### Project Manager (EPIC level)
```
SIMULATED RESPONSE: Project Manager
Return Code: SUCCESS
Summary: Epic broken down into stories

Enriched Context Used: YES
- Epic requirements from enriched context
- Scope boundaries respected
- Dependencies identified

Deliverables:
- 5 stories created for Epic 0001
- Story objectives defined
- Story dependencies mapped
- Epic updated with story references

Validation: All stories have clear scope
```

#### Feature Manager (STORY level)
```
SIMULATED RESPONSE: Feature Manager
Return Code: SUCCESS
Summary: Story decomposed into tasks

Enriched Context Used: YES
- Story requirements from enriched context
- Technical approach validated
- Implementation sequence planned

Deliverables:
- 7 tasks created for Story 0001.01
- Task specifications complete
- Technical dependencies identified
- Story updated with task references

Validation: All tasks are implementable
```

### Developer Responses

#### Success Case
```
SIMULATED RESPONSE: Developer (React/TypeScript)
Return Code: SUCCESS
Summary: Implementation completed successfully
Deliverables:
- Created RegistrationForm.tsx component
- Added form validation logic
- Wrote 8 unit tests (100% passing)
- Updated component documentation
Validation: All linting and type checks passed
```

#### Partial Case
```
SIMULATED RESPONSE: Developer (Node.js/Express)
Return Code: PARTIAL
Completed:
- User registration endpoint (100%)
- Email validation (100%)
- Password hashing (100%)
Remaining:
- Session management (0%)
- Remember me functionality (0%)
Progress: 3/5 tasks (60%)
Reason: Complex session logic requires additional design input
```

### QA Specialist Responses

#### Failure Case
```
SIMULATED RESPONSE: QA Specialist
Return Code: FAILURE
Error: Quality validation failed
Attempted: Full test suite execution and coverage analysis
Blockers:
- 7/8 tests passing (1 test failing)
- Edge case not handled: empty email validation
- Coverage: 85% (required 90%)
Suggestion: Fix email validation edge case and add missing tests
```

#### Success Case
```
SIMULATED RESPONSE: QA Specialist
Return Code: SUCCESS
Summary: All quality validations passed
Deliverables:
- 8/8 tests passing
- All edge cases covered
- Coverage: 92% (exceeds 90% requirement)
- Performance benchmarks met
Validation: Code quality score A, no security issues found
```

## AGENT INTERCEPTION

### When SIMULATION_MODE is Active

In any command, when reaching agent delegation:

```pseudocode
if SIMULATION_MODE == true:
    # Read delegation template
    delegation_report = fill_template(
        "`plugin:orchestrator:resources://TEMPLATE/REPORT/AGENT-DELEGATION.md`",
        agent_name=detected_type,
        work_identifier=work_id,
        delegation_type=state,
        ...
    )

    # Output delegation report
    print(delegation_report)

    # Generate simulated response
    response = generate_simulated_response(
        agent_type=detected_type,
        state=current_state,
        iteration=current_iteration,
        context=delegation_context
    )

    # Output simulated response
    print("SIMULATED RESPONSE:", response)
else:
    # Normal delegation with templates
    delegation_report = fill_template(...)
    print(delegation_report)
    response = Task(agent_type=..., prompt=...)
```

### Simulated Response Generation

Based on current state and context:

1. **Manager Agents (with enrichment)** - Always return SUCCESS with planning deliverables and enriched context usage
2. **Developer Agents** - Return SUCCESS (70%), PARTIAL (15%), FAILURE (10%), TIMEOUT (5%)
3. **QA Subaagents** - Return FAILURE (30% first iteration), SUCCESS (95% after retry)
4. **Validation** - Return SUCCESS (95%), MISSING (5% for dependencies)

### Return Code Selection Logic

```
function select_return_code(agent_type, state, iteration, complexity):
    if agent_type in ["product-manager", "project-manager", "feature-manager"]:
        return SUCCESS  # Manager agents always succeed in simulation

    if agent_type starts_with "developer":
        if iteration > 1:
            return SUCCESS  # Usually succeeds after retry
        if complexity == "high":
            return random_choice([SUCCESS:60%, PARTIAL:25%, FAILURE:10%, TIMEOUT:5%])
        else:
            return random_choice([SUCCESS:80%, PARTIAL:10%, FAILURE:8%, TIMEOUT:2%])

    if agent_type == "quality-assurance":
        if iteration == 1:
            return random_choice([SUCCESS:70%, FAILURE:30%])
        else:
            return SUCCESS  # Almost always succeeds after fix

    return SUCCESS  # Default for other agents
```

## OUTPUT EXAMPLE WITH TEMPLATES

```
/dryrun on

SIMULATION MODE: ENABLED
- All agent delegations will be simulated
- No files will be created or modified
- All orchestration flows will execute normally
- Using existing report templates

/plan "User authentication system"

## PHASE 00: INITIALIZE ORCHESTRATION

Detected Orchestration Level: PROJECT
Planning Context: User authentication system
Loading: ${CLAUDE_PLUGIN_ROOT}/resources/STATE-MACHINE/ORCHESTRATION/PROJECT.md

Creating TodoWrite tasks...

## PHASE 01: REQUIREMENTS ENRICHMENT

SIMULATING: Requirements Discovery (PROJECT level)
Loading: ${CLAUDE_PLUGIN_ROOT}/resources/TEMPLATE/QUESTIONNAIRE.md

[Simulated questionnaire interaction...]

GENERATING: Enriched Context ADR
Status: COMPLETE

## PHASE 02: ORCHESTRATION

Read `plugin:orchestrator:resources://TEMPLATE/REPORT/AGENT-DELEGATION.md`
[Filled with product-manager delegation details]

SIMULATED RESPONSE: Product Manager
Return Code: SUCCESS
Enriched Context Used: YES
[Full response details...]

Read `plugin:orchestrator:resources://TEMPLATE/REPORT/STATE-TRANSITION.md`
[Filled with transition details: PROJECT_INIT → SUCCESS → PROJECT_DONE]

PROJECT ORCHESTRATION COMPLETED
All documentation created (simulated)
```

## BENEFITS

1. **Risk-Free Testing** - No artifacts created
2. **Flow Validation** - Verify orchestration logic
3. **Template Testing** - Ensure all templates work correctly
4. **Enrichment Testing** - Validate context enrichment flow
5. **Training Mode** - Learn the orchestration patterns
6. **Debugging** - Identify flow issues without side effects
