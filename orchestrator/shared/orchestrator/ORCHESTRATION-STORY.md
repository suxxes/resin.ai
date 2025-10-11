<!-- Updated: 2025-09-28 00:00:00 UTC -->

## STORY ORCHESTRATION

### CRITICAL REQUIREMENTS
- **MUST** follow **STATE TRANSITIONS** requirements impeccably and unquestioningly
- **MUST** create ALL phase tasks upfront during initialization
- **MUST** update existing phase task names when entering loops (never create new tasks)
- **MUST** dynamically update phase names based on current position in the orchestration loop
- **MUST** assume next available loop state, if not currently in the loop
- **MUST** use ordered numbering with the zero-padded value to the maximum length among the related values with minimum length of 2
- **{XX}** - Orchestration phase (XX = phase number in phases order)
- **{TT/ZZ}** - Task iteration (TT = current task in the loop, ZZ = total tasks in current story)
- **{II}** - Implementation and Quality Validation iteration cycle (II = iteration number)

### CRITICAL RESTRICTIONS
- **NEVER** leave placeholders without proper values
- **NEVER** create new phase tasks when entering loops (update existing ones)
- **NEVER** skip creating any phase task during initialization
- **NEVER** create multiple tasks for the same phase (exactly ONE task per phase)

### STORY CONTROLLER

| State               | Phase Name (with Loop Indicators)                           | Suitable Subagent (or fallback to General Purpose)  | Quality Standards                      |
|---------------------|-------------------------------------------------------------|-----------------------------------------------------|----------------------------------------|
| STORY_CONTROLLER    | -                                                           | -                                                   | -                                      |
| → STORY_INIT        | Phase {XX}: Story Discovery and Planning                    | Manager for story level breakdown and task planning | -                                      |
| → TASK_CONTROLLER   | -                                                           | -                                                   | -                                      |
| → → TASK_INIT       | Phase {XX}: [{TT/ZZ}] Task Discovery and Planning           | Manager for task breakdown and specification        | -                                      |
| → → TASK_WORK       | Phase {XX}: [{TT/ZZ}] [{II}] Implementation                 | Auto-discovered based on task requirements          | Standard implementation and validation |
| → → TASK_TEST       | Phase {XX}: [{TT/ZZ}] [{II}] Quality Validation             | Quality assurance specialist for task validation    | Through-the-roof validation            |
| → → TASK_DONE       | Phase {XX}: [{TT/ZZ}] Task Completion                       | Manager for task level acceptance criteria          | Ruthless business validation           |
| → STORY_DONE        | Phase {XX}: Story Completion                                | Manager for story level acceptance criteria         | Complete coherence validation          |

### STATE TRANSITIONS

#### Task Loop Transitions (Atomic)
| State              | Transition State    | Code     | Description                                                    |
|--------------------|---------------------|----------|----------------------------------------------------------------|
| TASK_INIT          | TASK_WORK           | CONTINUE | Begin task implementation based on task requirements           |
| TASK_WORK          | TASK_TEST           | CONTINUE | Implementation complete - proceed to quality validation        |
| TASK_WORK          | TASK_WORK           | RETRY    | Partial implementation - continue with remaining deliverables  |
| TASK_TEST          | TASK_DONE           | CONTINUE | Quality validation passed - proceed to business validation     |
| TASK_TEST          | TASK_WORK           | RETRY    | Quality validation failed - return to implementation           |
| TASK_TEST          | TASK_TEST           | LOOP     | Partial validation - continue testing remaining components     |
| TASK_DONE          | TASK_CONTROLLER     | CONTINUE | Business validation complete - return control to task loop     |

#### Story Loop Transitions (Contains Task Loops)
| State              | Transition State    | Code     | Description                                                    |
|--------------------|---------------------|----------|----------------------------------------------------------------|
| STORY_INIT         | TASK_CONTROLLER     | CONTINUE | Story initialized - enter task loop controller                 |
| TASK_CONTROLLER    | TASK_INIT           | LOOP     | Start next unfinished task in story                            |
| TASK_CONTROLLER    | STORY_DONE          | EXIT     | All tasks complete - exit story loop                           |
| STORY_DONE         | STORY_CONTROLLER    | CONTINUE | Return control to story loop controller                        |
| STORY_CONTROLLER   | STORY_INIT          | LOOP     | Start next unfinished story                                    |
| STORY_CONTROLLER   | EXIT                | EXIT     | All stories complete - exit orchestration                      |

#### Loop Controller Logic
| Controller         | Decision Logic                                                                         |
|--------------------|----------------------------------------------------------------------------------------|
| TASK_CONTROLLER    | Find next unfinished task in current story → LOOP or all done → EXIT                   |
| STORY_CONTROLLER   | Find next unfinished story in project → LOOP or all done → EXIT                        |
