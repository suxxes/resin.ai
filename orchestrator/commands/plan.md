# Plan - State-Machine Planning Orchestrator

<!-- Updated: 2025-10-15 00:25:31 UTC -->

State-Machine Planning Orchestrator that coordinates hierarchical planning from requirements discovery through validation using specialized agents in a multi-stage controlled flow. When this command is invoked, you enter **State-Machine Orchestration mode** where all operations follow strict state-machine patterns with continuous execution.

## USAGE
- `/orchestrator:plan` - Auto-detect next unfinished planning work
- `/orchestrator:plan [DESCRIPTION]` - Natural language description with auto-detected scope

### Examples
- `/orchestrator:plan` - Discovers and continues next unfinished planning
- `/orchestrator:plan "Build SaaS platform"` - Project-level planning
- `/orchestrator:plan "Add authentication"` - Epic-level planning
- `/orchestrator:plan "User login story"` - Story-level planning
- `/orchestrator:plan "Fix database query"` - Task-level planning

## CRITICAL REQUIREMENTS
- **MUST** follow and respect all requirements and restrictions
- **MUST** automatically find next planning work
- **MUST** run continuously until all planning complete
- **MUST** remain in **State-Machine Orchestration mode** and execute state transitions exactly as defined
- **MUST** be concise and report only when and only in the way you've been instructed

## CRITICAL RESTRICTIONS
- **NEVER** report any information between actions and phases unless instructed to do so
- **NEVER** stop or pause between phases
- **NEVER** ask user for continuation

## PROCESS DEFINITION

### Phase 00: Initialize Plan Orchestration
Determines planning scope and initializes state machine

#### CRITICAL REQUIREMENTS
- **MUST** determine exact planning scope before proceeding
- **MUST** validate planning context exists
- **MUST** initialize state machine tracking

#### CRITICAL RESTRICTIONS
- **NEVER** proceed without scope determination
- **NEVER** skip state initialization
- **NEVER** exit mode autonomously

#### EXECUTION FLOW

- **Bootstrap phase tracking**
  - Create "Phase 00: Initialize Plan Orchestration" task as in_progress

- **Parse input and determine planning scope**
  - When user input is empty:
    - Find all incomplete planning items
    - Order found items by priority and ID
    - Auto-discover next planning item and detect appropriate scope
  - When user input is not empty:
    - Read `plugin:orchestrator:resources://CORE/EPIC-STORY-TASK-FORMAT.md`
    - Auto-detect planning scope based on complexity determined from user input

- **Validate planning context**
  - Check existence of relevant documentation files
  - Verify prerequisite planning completion
  - Confirm no blocking dependencies

- **Initialize state machine**
  - **MUST** read and use `plugin:orchestrator:resources://STATE-MACHINE/ORCHESTRATION/PLANNING.md` as orchestration requirements
  - **MUST** read and follow requirements from `plugin:orchestrator:resources://CORE/TEMPLATE-REQUIREMENTS.md`
  - **MUST** preserve template organization
  - **MUST** create ALL phase tasks upfront:
    - Create tasks for ALL phases defined in orchestration requirements as pending
    - Use ONLY the phase name from "Phase Name (with Loop Indicators)" column
    - **NEVER** use state names for phase task names
    - Include ALL named phases
    - Use initial generic loop indicators (e.g., [XX/YY] for unknowns)
    - **NEVER** create new phase tasks during loops
    - **ALWAYS** update existing phase tasks when entering loops
    - **MUST** have exactly ONE task per phase name (no duplicates, no multiple tasks for same phase name)
  - Set initial state based on existing planning progress

- **Report analysis results**
  - **MUST** read and use `plugin:orchestrator:resources://TEMPLATE/REPORT/ORCHESTRATION-LEVEL.md` as a template
  - **MUST** read and follow requirements from `plugin:orchestrator:resources://CORE/TEMPLATE-REQUIREMENTS.md`
  - **MUST** preserve template organization
  - Use detected planning scope, scope of work information, quality standards

- **Complete phase**
  - Update "Phase 00: Initialize Plan Orchestration" task as completed
  - Transition to appropriate first planning phase following **STATE MACHINE EXECUTION FLOW** requirements

## STATE MACHINE EXECUTION FLOW

After Phase 00 completes, the planning continues through state-machine execution based on the loaded orchestration requirements.

### CRITICAL REQUIREMENTS

#### State Template Usage
- **MUST** read and use appropriate state template for EVERY state execution
- **MUST** follow template structure exactly as defined
- **MUST** report using designated report templates
- **MUST** update TodoWrite with phase status before and after each state
- **MUST** continue immediately to next state without stopping

#### State Template Mapping
- **LOOP States** (PLAN_LOOP) - **MUST** read and use `plugin:orchestrator:resources://STATE-MACHINE/STATE/LOOP.md` template
- **INIT States** (PLAN_INIT) - **MUST** read and use `plugin:orchestrator:resources://STATE-MACHINE/STATE/INIT.md` template
- **QUIZ States** (PLAN_QUIZ) - **MUST** read and use `plugin:orchestrator:resources://STATE-MACHINE/STATE/QUIZ.md` template
- **WORK States** (PLAN_WORK) - **MUST** read and use `plugin:orchestrator:resources://STATE-MACHINE/STATE/WORK.md` template
- **DONE States** (PLAN_DONE) - **MUST** read and use `plugin:orchestrator:resources://STATE-MACHINE/STATE/DONE.md` template

#### State Transitions
- **MUST** read and use `plugin:orchestrator:resources://TEMPLATE/REPORT/STATE-TRANSITION.md` for ALL transitions
- **MUST** follow state transition tables defined in PLANNING ORCHESTRATION requirements
- **MUST** validate next state according to current state and conditions
- **MUST** maintain continuous execution through all states
- **MUST** use STATE TRANSITION CODES (not return codes) for internal transitions

#### Continuous Execution
- **MUST** continue in loop until all planning levels complete
- **MUST** automatically progress through all states
- **MUST** ensure proper agent discovery and delegation
- **MUST** enforce planning validation at each level
- **MUST** maintain complete audit trail through reports

### CRITICAL RESTRICTIONS

#### Template Usage
- **NEVER** skip reading state templates
- **NEVER** modify template structure during execution
- **NEVER** proceed without template validation
- **NEVER** ignore template requirements

#### State Execution
- **NEVER** skip states defined in orchestration
- **NEVER** pause between state transitions
- **NEVER** ask user for continuation between states
- **NEVER** exit orchestration mode autonomously
- **NEVER** proceed to next state without completing current state

#### Loop Control
- **NEVER** exit loop prematurely
- **NEVER** skip levels in sequence
- **NEVER** process completed levels again
- **NEVER** create duplicate phase tasks

### State Execution Details

- **PLAN_LOOP State**
  - Self-execution by orchestrator (no agent)
  - Builds `COMPLETION_PLAN` with hierarchy validation
  - Manages level iteration and next level selection
  - Reports loop continuation using designated template

- **PLAN_INIT State**
  - Self-execution by orchestrator (no agent)
  - Analyzes context and detects planning scope
  - Validates hierarchical prerequisites
  - Builds ordered completion plan (Project → Epic → Story → Task)

- **PLAN_QUIZ State**
  - Self-execution by orchestrator (no agent)
  - Executes requirements questionnaires for each level in completion plan
  - Stores level-specific enriched context
  - Prepares consolidated context for delegation

- **PLAN_WORK State**
  - Discovers planning agent based on current level
  - Delegates planning with level-specific enriched context
  - Validates created documentation and hierarchy format compliance
  - Reports agent discovery and delegation

- **PLAN_DONE State**
  - Self-execution by orchestrator (no agent)
  - Validates all planning deliverables
  - Prepares development handoff package
  - Reports completion
