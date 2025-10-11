# Work - State-Machine Implementation Orchestrator

<!-- Updated: 2025-10-17 00:37:59 UTC -->

State-Machine Implementation Orchestrator that coordinates complete implementation from planning through validation using specialized agents in a multi-stage controlled flow with escalating quality standards. When this command is invoked, you enter **State-Machine Orchestration mode** where all operations follow strict state-machine patterns with **autonomous continuous execution**. You MUST complete ALL work items without stopping to ask for user input, continuation preferences, or approval. The orchestration runs to completion or error - never pauses mid-workflow.

## USAGE
- `/orchestrator:work` - Auto-detect next unfinished work and execute appropriate orchestration
- `/orchestrator:work 0003` - Work on Epic 0003 (full epic orchestration)
- `/orchestrator:work 0003.02` - Work on Story 0003.02 (story-level orchestration)
- `/orchestrator:work 0003.02.01` - Work on Task 0003.02.01 (task-level orchestration)
- `/orchestrator:work [DESCRIPTION]` - Natural language description with auto-detected orchestration

### Examples
- `/orchestrator:work` - Discovers and continues next unfinished task
- `/orchestrator:work "Fix authentication bug"` - Task-level implementation
- `/orchestrator:work "Add user profile feature"` - Story-level orchestration
- `/orchestrator:work "Build payment system"` - Epic-level orchestration

## CRITICAL REQUIREMENTS
- **MUST** follow and respect all requirements and restrictions
- **MUST** automatically find next work
- **MUST** run continuously until all work complete
- **MUST** remain in **State-Machine Orchestration mode** and execute state transitions exactly as defined
- **MUST** be concise and report only when and only in the way you've been instructed
- **MUST** complete ALL work items autonomously without pauses or interruption
- **MUST** continue through entire master loop until full completion or error

## CRITICAL RESTRICTIONS
- **NEVER** report any information between actions and phases unless instructed to do so
- **NEVER** ask user for continuation, preferences, suggest anything, or request approval while in the workflow
- **NEVER** provide progress summaries and never ask questions unless those are defined in workflow
- **NEVER** pause to ask user about anything that is not clearly defined in the instructions
- **NEVER** stop or pause between phases for any reason other than error

## PROCESS DEFINITION

### Phase 00: Initialize Work Orchestration
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
  - Create "Phase 00: Initialize Work Orchestration" task as in_progress

- **Parse input and determine orchestration level**
  - When user input is empty:
    - Find all unfinished work items
    - Order found work items by importance and ID
    - Auto-discover next work item and detect appropriate orchestration level
  - When user input is not empty:
    - Read `plugin:orchestrator:resources://CORE/EPIC-STORY-TASK-FORMAT.md`
    - When user input aligns with "EPIC.STORY.TASK FORMAT":
      - Using "EPIC.STORY.TASK FORMAT" align orchestration level to user input
    - Otherwise:
      - Auto-detect orchestration level based on complexity determined from user input

- **Validate work context**
  - Check existence of relevant documentation files
  - Verify prerequisite work completion
  - Confirm no blocking dependencies

- **Initialize state machine**
  - When orchestration level is detected as project:
    - **MUST** read and use `plugin:orchestrator:resources://STATE-MACHINE/ORCHESTRATION/PROJECT.md` as orchestration requirements
  - When orchestration level is detected as epic:
    - **MUST** read and use `plugin:orchestrator:resources://STATE-MACHINE/ORCHESTRATION/EPIC.md` as orchestration requirements
  - When orchestration level is detected as story:
    - **MUST** read and use `plugin:orchestrator:resources://STATE-MACHINE/ORCHESTRATION/STORY.md` as orchestration requirements
  - When orchestration level is detected as task:
    - **MUST** read and use `plugin:orchestrator:resources://STATE-MACHINE/ORCHESTRATION/TASK.md` as orchestration requirements
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
  - Set initial state based on existing work progress

- **Report analysis results**
  - **MUST** read and use `plugin:orchestrator:resources://TEMPLATE/REPORT/ORCHESTRATION-LEVEL.md` as a template
  - **MUST** read and follow requirements from `plugin:orchestrator:resources://CORE/TEMPLATE-REQUIREMENTS.md`
  - **MUST** preserve template organization
  - Use detected orchestration level, scope of work information, quality standards

- **Complete phase**
  - Update "Phase 00: Initialize Work Orchestration" task as completed
  - Transition to appropriate first implementation phase following **STATE MACHINE EXECUTION FLOW** requirements

## STATE MACHINE EXECUTION FLOW

After Phase 00 completes, the orchestration continues through state-machine execution based on the loaded orchestration requirements.

### CRITICAL REQUIREMENTS

- **State Template Usage**
  - **MUST** read and use appropriate state template for EVERY state execution
  - **MUST** follow template structure exactly as defined
  - **MUST** report using designated report templates
  - **MUST** update TodoWrite with phase status before and after each state
  - **MUST** continue immediately to next state without stopping

- **State Template Mapping**
  - **LOOP States** - **MUST** read and use `plugin:orchestrator:resources://STATE-MACHINE/STATE/LOOP.md` template
  - **INIT States** - **MUST** read and use `plugin:orchestrator:resources://STATE-MACHINE/STATE/INIT.md` template
  - **WORK States** - **MUST** read and use `plugin:orchestrator:resources://STATE-MACHINE/STATE/WORK.md` template
  - **TEST States** - **MUST** read and use `plugin:orchestrator:resources://STATE-MACHINE/STATE/TEST.md` template
  - **DONE States** - **MUST** read and use `plugin:orchestrator:resources://STATE-MACHINE/STATE/DONE.md` template

- **State Transitions**
  - **MUST** read and use `plugin:orchestrator:resources://TEMPLATE/REPORT/STATE-TRANSITION.md` for ALL transitions
  - **MUST** follow state transition tables defined in orchestration requirements
  - **MUST** validate next state according to current state and conditions
  - **MUST** maintain continuous execution through all states
  - **MUST** use `RETURN_CODE` for internal transitions and transition reporting

- **Continuous Execution**
  - **MUST** continue in loop until all work items complete
  - **MUST** automatically progress through all states
  - **MUST** ensure proper agent discovery and delegation
  - **MUST** enforce quality validation at each level
  - **MUST** maintain complete audit trail through reports

### CRITICAL RESTRICTIONS

- **Template Usage**
  - **NEVER** skip reading state templates
  - **NEVER** modify template structure during execution
  - **NEVER** proceed without template validation
  - **NEVER** ignore template requirements

- **State Execution**
  - **NEVER** skip states defined in orchestration
  - **NEVER** pause between state transitions
  - **NEVER** ask user for continuation between states
  - **NEVER** stop or exit orchestration mode autonomously
  - **NEVER** proceed to next state without completing current state

- **Loop Control**
  - **NEVER** exit loop prematurely
  - **NEVER** skip items in sequence
  - **NEVER** process completed items again
  - **NEVER** create duplicate phase tasks

### State Execution Details

- **LOOP States**
  - Self-execution by orchestrator (no agent)
  - Manages loop iteration and next item selection
  - Reports loop continuation using designated template

- **INIT States**
  - Discovers planning/management agent
  - Creates breakdown if needed
  - Reports agent discovery and delegation

- **WORK States**
  - Discovers developer based on technology/requirements
  - Executes implementation
  - Reports agent discovery and delegation

- **TEST States**
  - Discovers QA agent
  - Performs validation
  - Reports agent discovery, status and failures

- **DONE States**
  - Discovers validation agent
  - Verifies acceptance criteria
  - Reports completion
