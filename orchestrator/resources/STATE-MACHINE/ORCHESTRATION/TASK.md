<!-- Updated: 2025-09-28 00:00:00 UTC -->

## TASK ORCHESTRATION

Task-level orchestration focuses solely on development and quality assurance. When running at task-level only, the flow exits directly after QA passes. TASK_DONE state is only used within story/epic orchestration for business validation and loop control.

### CRITICAL REQUIREMENTS
- **MUST** follow **STATE TRANSITIONS** requirements impeccably and unquestioningly
- **MUST** create ALL phase tasks upfront during initialization
- **MUST** update existing phase task names when entering loops (never create new tasks)
- **MUST** dynamically update phase names based on current position in the orchestration loop
- **MUST** assume next available loop state, if not currently in the loop
- **MUST** use ordered numbering with the zero-padded value to the maximum length among the related values with minimum length of 2
- **{XX}** - Orchestration phase (XX = phase number in phases order)
- **{II}** - Development/QA iteration cycle (II = iteration number)

### CRITICAL RESTRICTIONS
- **NEVER** leave placeholders without proper values
- **NEVER** create new phase tasks when entering loops (update existing ones)
- **NEVER** skip creating any phase task during initialization
- **NEVER** create multiple tasks for the same phase (exactly ONE task per phase)

### TASK CONTROLLER

| State Name        | Phase Name (with Loop Indicators)                                     | Suitable Agent (or fallback to General Purpose)     | Quality Standards                      |
|-------------------|-----------------------------------------------------------------------|-----------------------------------------------------|----------------------------------------|
| TASK_LOOP         | Phase {XX}: Task Loop                                                 | -                                                   | -                                      |
| → TASK_INIT       | Phase {XX}: Task Discovery and Planning                               | Manager for task breakdown and specification        | -                                      |
| → TASK_WORK       | Phase {XX}: [{II}] Implementation                                     | Auto-discovered based on task requirements          | Standard implementation and validation |
| → TASK_TEST       | Phase {XX}: [{II}] Quality Validation                                 | Quality assurance agent for task validation         | Through-the-roof validation            |

### STATE TRANSITIONS

| State Name        | Transition State    | Code     | Description                                                    |
|-------------------|---------------------|----------|----------------------------------------------------------------|
| TASK_LOOP         | TASK_INIT           | CONTINUE | Start task execution                                           |
| TASK_LOOP         | EXIT                | EXIT     | No tasks to process - exit orchestration                       |
| TASK_INIT         | TASK_WORK           | CONTINUE | Begin task implementation based on task requirements           |
| TASK_WORK         | TASK_TEST           | CONTINUE | Implementation complete - proceed to quality validation        |
| TASK_WORK         | TASK_WORK           | RETRY    | Partial implementation - continue with remaining deliverables  |
| TASK_TEST         | TASK_LOOP           | CONTINUE | Quality validation passed - return to controller               |
| TASK_TEST         | TASK_WORK           | RETRY    | Quality validation failed - return to implementation           |
| TASK_TEST         | TASK_TEST           | LOOP     | Partial validation - continue testing remaining components     |
| TASK_LOOP         | EXIT                | EXIT     | Task complete - exit orchestration (standalone execution)      |
