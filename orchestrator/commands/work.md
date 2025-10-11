# Work - State-Machine Implementation Orchestrator

<!-- Updated: 2025-09-28 21:00:00 UTC -->

State-Machine Implementation Orchestrator that coordinates complete implementation from planning through validation using specialized subagents in a multi-stage controlled flow with escalating quality standards. When this command is invoked, you enter **State-Machine Orchestration mode** where all operations follow strict state-machine patterns with continuous execution.


## USAGE
- `/work` - Auto-detect next unfinished work and execute appropriate orchestration
- `/work 0003` - Work on Epic 0003 (full epic orchestration)
- `/work 0003.02` - Work on Story 0003.02 (story-level orchestration)
- `/work 0003.02.01` - Work on Task 0003.02.01 (task-level orchestration)
- `/work [DESCRIPTION]` - Natural language description with auto-detected orchestration

### Examples
- `/work` - Discovers and continues next unfinished task
- `/work "Fix authentication bug"` - Task-level implementation
- `/work "Add user profile feature"` - Story-level orchestration
- `/work "Build payment system"` - Epic-level orchestration


## CRITICAL REQUIREMENTS
- **MUST** follow and respect all requirements and restrictions
- **MUST** automatically find next work
- **MUST** run continuously until all work complete
- **MUST** remain in **State-Machine Orchestration mode** and execute state transitions exactly as defined
- **MUST** be concise and report only when and only in the way you've been instructed

## CRITICAL RESTRICTIONS
- **NEVER** report any information between actions and phases unless instructed to do so
- **NEVER** stop or pause between phases
- **NEVER** ask user for continuation


## PROCESS DEFINITION

### Phase 00: Initialize Orchestration
Determines orchestration level and initializes state machine

#### CRITICAL REQUIREMENTS
- **MUST** determine exact orchestration level before proceeding
- **MUST** validate work context exists
- **MUST** initialize state machine tracking

#### CRITICAL RESTRICTIONS
- **NEVER** proceed without level determination
- **NEVER** skip state initialization
- **NEVER** exit mode autonomously

#### EXECUTION FLOW

- **Bootstrap phase tracking**
  - Create "Phase 00: Initialize Orchestration" task as in_progress

- **Parse input and determine orchestration level**
  - When user input is empty:
    - Find all unfinished work items
    - Order found work items by importance and ID
    - Auto-discover next work item and detect appropriate orchestration level
  - When user input is not empty:
    - Read `~/.claude/shared/core/EPIC-STORY-TASK-FORMAT.md`
    - When user input aligns with "EPIC.STORY.TASK FORMAT":
      - Using "EPIC.STORY.TASK FORMAT" align orchestration level to user input
    - Otherwise:
      - Auto-detect orchestration level based on complexity determined from user input

- **Validate work context**
  - Check existence of relevant documentation files
  - Verify prerequisite work completion
  - Confirm no blocking dependencies

- **Initialize state machine**
  - When orchestration level is detected as epic:
    - **MUST** read and use `~/.claude/shared/orchestrator/ORCHESTRATION-EPIC.md` file as orchestration requirements
  - When orchestration level is detected as story:
    - **MUST** read and use `~/.claude/shared/orchestrator/ORCHESTRATION-STORY.md` file as orchestration requirements
  - When orchestration level is detected as task:
    - **MUST** read and use `~/.claude/shared/orchestrator/ORCHESTRATION-TASK.md` file as orchestration requirements
  - **MUST** read and follow requirements from `~/.claude/shared/core/TEMPLATE-REQUIREMENTS.md` file
  - **MUST** preserve template organization
  - **MUST** create ALL phase tasks upfront:
    - Create tasks for ALL phases defined in orchestration requirements as pending
    - Include ALL named phases
    - Use initial generic loop indicators (e.g., [XX/YY] for unknowns)
    - **NEVER** create new phase tasks during loops
    - **ALWAYS** update existing phase tasks when entering loops
    - **MUST** have exactly ONE task per phase (no duplicates, no multiple tasks for same phase)
  - Set initial state based on existing work progress

- **Report analysis results**
  - **MUST** read and use `~/.claude/shared/templates/REPORT/ORCHESTRATION-LEVEL.md` file as a template
  - **MUST** read and follow requirements from `~/.claude/shared/core/TEMPLATE-REQUIREMENTS.md` file
  - **MUST** preserve template organization
  - Use detected orchestration level, scope of work information, quality standards

- **Complete phase**
  - Update "Phase 00: Initialize Orchestration" task as completed
  - Transition to appropriate first implementation phase following **STATE MACHINE EXECUTION FLOW** requirements


## STATE MACHINE EXECUTION FLOW

After Phase 00 completes, the orchestration continues through state-machine execution based on the loaded orchestration requirements.

### CRITICAL REQUIREMENTS

#### State Template Usage
- **MUST** read and use appropriate state template for EVERY state execution
- **MUST** follow template structure exactly as defined
- **MUST** report using designated report templates
- **MUST** update TodoWrite with phase status before and after each state
- **MUST** continue immediately to next state without stopping

#### State Template Mapping
- **CONTROLLER States** - **MUST** read and use `~/.claude/shared/orchestrator/STATE-CONTROLLER.md` template
- **INIT States** - **MUST** read and use `~/.claude/shared/orchestrator/STATE-INIT.md` template
- **WORK States** - **MUST** read and use `~/.claude/shared/orchestrator/STATE-WORK.md` template
- **TEST States** - **MUST** read and use `~/.claude/shared/orchestrator/STATE-TEST.md` template
- **DONE States** - **MUST** read and use `~/.claude/shared/orchestrator/STATE-DONE.md` template

#### State Transitions
- **MUST** read and use `~/.claude/shared/templates/REPORT/STATE-TRANSITION.md` for ALL transitions
- **MUST** follow state transition tables defined in orchestration requirements
- **MUST** validate next state according to current state and conditions
- **MUST** maintain continuous execution through all states
- **MUST** use STATE TRANSITION CODES (not return codes) for internal transitions

#### Continuous Execution
- **MUST** continue in loop until all work items complete
- **MUST** automatically progress through all states
- **MUST** ensure proper subagent discovery and delegation
- **MUST** enforce quality validation at each level
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
- **NEVER** skip items in sequence
- **NEVER** process completed items again
- **NEVER** create duplicate phase tasks

### State Execution Details

- **CONTROLLER States**
  - Self-execution by orchestrator (no subagent)
  - Manages loop iteration and next item selection
  - Reports loop continuation using designated template

- **INIT States**
  - Discovers planning/management specialist
  - Creates breakdown if needed
  - Reports subagent discovery and delegation

- **WORK States**
  - Discovers developer based on technology/requirements
  - Executes implementation
  - Reports subagent discovery and delegation

- **TEST States**
  - Discovers QA specialist
  - Performs validation
  - Reports subagent discovery, status and failures

- **DONE States**
  - Discovers validation specialist
  - Verifies acceptance criteria
  - Reports completion
