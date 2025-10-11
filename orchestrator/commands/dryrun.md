# Dry Run - Orchestration Test Mode

<!-- Updated: 2025-09-28 00:00:00 UTC -->

Enables simulation mode for actual orchestration commands. When active, all commands execute their real flows but with simulated subagent responses instead of actual delegations.

## USAGE
- `/dryrun on` - Enable simulation mode
- `/dryrun off` - Disable simulation mode
- `/dryrun status` - Check current simulation mode

### With Simulation Mode Enabled
Execute actual commands which will use simulated responses:
- `/work` - Runs actual work orchestration with simulated subagents
- `/work 0001` - Runs epic orchestration with simulated responses
- `/plan "Build feature"` - Runs plan orchestration with simulated responses

### Examples
```
/dryrun on
Simulation mode: ENABLED
All subagent delegations will be simulated

/work "Fix authentication bug"
[Executes actual work command with simulated responses]

/dryrun off
Simulation mode: DISABLED
Normal operation restored
```

## CRITICAL REQUIREMENTS
- **MUST** set global SIMULATION_MODE flag when enabled
- **MUST** execute actual command flows (work, plan, etc.)
- **MUST** intercept subagent delegations when in simulation mode
- **MUST** use standardized return codes from RETURN-CODES.md
- **MUST** provide realistic simulated responses with proper additional information

## CRITICAL RESTRICTIONS
- **NEVER** create actual files when in simulation mode
- **NEVER** invoke real subagents when in simulation mode
- **NEVER** modify existing files when in simulation mode
- **NEVER** make git commits when in simulation mode
- **NEVER** skip any orchestration steps

## IMPLEMENTATION

### Simulation Mode Flag
When `/dryrun on` is executed:
1. Set global `SIMULATION_MODE = true`
2. All subsequent commands check this flag
3. When `SIMULATION_MODE = true`:
   - Subagent Task tool calls are intercepted
   - Instead of invoking subagent, return simulated response
   - All other operations execute normally

### Integration Points
Commands that support simulation mode:
- `/work` - All orchestration levels
- `/plan` - All planning scopes
- Any command that uses subagent delegation

### How It Works
1. User runs `/dryrun on`
2. User runs actual command like `/work 0001.02.03`
3. Command executes normally through all phases
4. When reaching subagent delegation:
   - Check `if SIMULATION_MODE == true`
   - Skip actual Task tool invocation
   - Generate appropriate simulated response
   - Continue with normal flow using simulated response
5. All state transitions, reports, and TodoWrite updates execute normally
6. No actual files/code/documentation created

## SIMULATION RESPONSES

### Mock Data Patterns
When in simulation mode, use these patterns:

#### Epic Level
```
Epic 0001: User Authentication System
Stories:
  0001.01: User Registration Flow
  0001.02: Login and Session Management
  0001.03: Password Recovery System
```

#### Story Level
```
Story 0001.01: User Registration Flow
Tasks:
  0001.01.01: Create registration form UI
  0001.01.02: Implement email validation
  0001.01.03: Add password strength checker
  0001.01.04: Create user database schema
  0001.01.05: Implement registration API
```

#### Task Level
```
Task 0001.01.01: Create registration form UI
Type: Frontend Development
Tech Stack: React, TypeScript, TailwindCSS
Complexity: Medium
```

### Simulated Subagent Responses

#### Planning Specialist (INIT states)
```
SIMULATED RESPONSE: Planning Specialist
Return Code: SUCCESS
Summary: Successfully created work breakdown structure
Deliverables:
- 3 stories identified and documented
- 15 total tasks planned with specifications
- Dependencies mapped between tasks
- Acceptance criteria defined for all items
Validation: All stories have clear scope and requirements
```

#### Developer (WORK states) - Success Case
```
SIMULATED RESPONSE: Developer (React/TypeScript)
Return Code: SUCCESS
Summary: Registration form UI implemented successfully
Deliverables:
- Created RegistrationForm.tsx component
- Added form validation logic
- Wrote 8 unit tests (100% passing)
- Updated component documentation
Validation: All linting and type checks passed
```

#### Developer (WORK states) - Partial Case
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

#### QA Specialist (TEST states) - Failure Case
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

#### QA Specialist (TEST states) - Success Case
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

#### Validation Specialist (DONE states)
```
SIMULATED RESPONSE: Validation Specialist
Return Code: SUCCESS
Summary: Work item meets all acceptance criteria
Deliverables:
- Business requirements validated
- Technical criteria satisfied
- Integration tests passing
- Documentation complete
Validation: Ready for production deployment
```

#### Timeout Scenario
```
SIMULATED RESPONSE: Developer (Python/Django)
Return Code: TIMEOUT
Last Success: Completed 4/10 API endpoints
Timeout At: 300 seconds elapsed
Remaining: 6 endpoints, approximately 180 seconds
Checkpoint: Can resume from endpoint #5 (/api/users/profile)
```

#### Missing Dependencies Scenario
```
SIMULATED RESPONSE: Developer (Java/Spring)
Return Code: MISSING
Missing Items:
- Database schema: schema.sql
- API specification: openapi.yaml
- Environment config: application.properties
Searched: src/main/resources/, docs/, config/
Required For: Database setup and API implementation
Alternatives: Could generate from existing code or use templates
```

## SUBAGENT INTERCEPTION

### When SIMULATION_MODE is Active

In any command, when reaching subagent delegation:

```pseudocode
if SIMULATION_MODE == true:
    # Instead of: Task(subagent_type=developer, prompt=...)
    response = generate_simulated_response(
        subagent_type=detected_type,
        state=current_state,
        iteration=current_iteration,
        context=delegation_context
    )
else:
    # Normal delegation
    response = Task(subagent_type=..., prompt=...)
```

### Simulated Response Generation

Based on current state and context:

1. **INIT States** - Always return SUCCESS with planning deliverables
2. **WORK States** - Return SUCCESS (70%), PARTIAL (15%), FAILURE (10%), TIMEOUT (5%)
3. **TEST States** - Return FAILURE (30% first iteration), SUCCESS (95% after retry)
4. **DONE States** - Return SUCCESS (95%), MISSING (5% for dependencies)

### Return Code Selection Logic

```
function select_return_code(state, iteration, complexity):
    if state == "INIT":
        return SUCCESS  # Planning always succeeds in simulation

    if state == "WORK":
        if iteration > 1:
            return SUCCESS  # Usually succeeds after retry
        if complexity == "high":
            return random_choice([SUCCESS:60%, PARTIAL:25%, FAILURE:10%, TIMEOUT:5%])
        else:
            return random_choice([SUCCESS:80%, PARTIAL:10%, FAILURE:8%, TIMEOUT:2%])

    if state == "TEST":
        if iteration == 1:
            return random_choice([SUCCESS:70%, FAILURE:30%])
        else:
            return SUCCESS  # Almost always succeeds after fix

    if state == "DONE":
        return random_choice([SUCCESS:95%, MISSING:5%])
```

## OUTPUT EXAMPLE

```
/dryrun on

SIMULATION MODE: ENABLED
- All subagent delegations will be simulated
- No files will be created or modified
- All orchestration flows will execute normally

/work 0001.01.03

## PHASE 00: INITIALIZE ORCHESTRATION

Detected Orchestration Level: TASK (0001.01.03)
Work Context: Task - Create registration form UI
State Machine: TASK_ORCHESTRATION
Loading: ~/.claude/shared/orchestrator/ORCHESTRATION-TASK.md

Creating TodoWrite tasks...
✓ Phase 00: Initialize Orchestration
○ Phase 01: Task Discovery and Planning
○ Phase 02: [01] Implementation
○ Phase 03: [01] Quality Validation

## PHASE 01: ORCHESTRATION

STATE: TASK_CONTROLLER → (SUCCESS) → TASK_INIT

SIMULATING: Task Discovery and Planning
SIMULATED RESPONSE: Planning Specialist
Return Code: SUCCESS
Summary: Task requirements analyzed and documented
Deliverables:
- Task specification created
- Tech stack identified: React, TypeScript
- Acceptance criteria defined
Validation: Requirements complete and clear

## PHASE 02: ORCHESTRATION

STATE: TASK_INIT → (SUCCESS) → TASK_WORK

SIMULATING: Developer Discovery
Selected: React/TypeScript Developer (95% match)

SIMULATING: Implementation
SIMULATED RESPONSE: Developer
Return Code: SUCCESS
Summary: Registration form UI implemented successfully
Deliverables:
- Created RegistrationForm.tsx component
- Added form validation logic
- Wrote 8 unit tests (100% passing)
- Updated documentation
Validation: All linting and type checks passed

## PHASE 03: ORCHESTRATION

STATE: TASK_WORK → (SUCCESS) → TASK_TEST

SIMULATING: QA Discovery
Selected: QA Specialist (90% match)

SIMULATING: Quality Validation (First Attempt)
SIMULATED RESPONSE: QA Specialist
Return Code: FAILURE
Error: Quality validation failed
Blockers:
- Edge case not handled: empty email validation
- Coverage: 85% (required 90%)
Suggestion: Fix email validation edge case and add tests

## ITERATION FEEDBACK REPORT

Returning to TASK_WORK with feedback...

## PHASE 02: ORCHESTRATION (Iteration 2)

STATE: TASK_TEST → (FAILURE) → TASK_WORK

SIMULATING: Implementation Fix
SIMULATED RESPONSE: Developer
Return Code: SUCCESS
Summary: Fixed validation issues
Deliverables:
- Fixed empty email edge case
- Added 2 additional tests
- Coverage increased to 92%
Validation: All issues resolved

## PHASE 03: ORCHESTRATION (Iteration 2)

STATE: TASK_WORK → (SUCCESS) → TASK_TEST

SIMULATING: Quality Validation (Second Attempt)
SIMULATED RESPONSE: QA Specialist
Return Code: SUCCESS
Summary: All quality validations passed
Deliverables:
- 10/10 tests passing
- All edge cases covered
- Coverage: 92%
Validation: Code quality score A

TASK 0001.01.01 COMPLETED
Orchestration complete.
```

## BENEFITS

1. **Risk-Free Testing** - No artifacts created
2. **Flow Validation** - Verify orchestration logic
3. **Template Testing** - Ensure all templates work
4. **Training Mode** - Learn the orchestration patterns
5. **Debugging** - Identify flow issues without side effects