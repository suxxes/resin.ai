<!-- Updated: 2025-09-28 00:00:00 UTC -->

## EPIC LEVEL ORCHESTRATION

### CRITICAL REQUIREMENTS
- **MUST** follow **STATE TRANSITIONS** requirements impeccably and unquestioningly
- **MUST** create ALL phase tasks upfront during initialization
- **MUST** update existing phase task names when entering loops (never create new tasks)
- **MUST** dynamically update phase names based on current position in the orchestration loop
- **MUST** assume next available loop state, if not currently in the loop
- **MUST** use ordered numbering with the zero-padded value to the maximum length among the related values with minimum length of 2
- **{XX}** - Orchestration phase (XX = phase number in phases order)
- **{SS/YY}** - Story iteration (SS = current story in the loop, YY = total stories in current epic)
- **{TT/ZZ}** - Task iteration (TT = current task in the loop, ZZ = total tasks in current story)
- **{II}** - Implementation and Quality Validation iteration cycle (II = iteration number)

### CRITICAL RESTRICTIONS
- **NEVER** leave placeholders without proper values
- **NEVER** create new phase tasks when entering loops (update existing ones)
- **NEVER** skip creating any phase task during initialization
- **NEVER** create multiple tasks for the same phase (exactly ONE task per phase)

### EPIC CONTROLLER

| State Name        | Phase Name (with Loop Indicators)                                     | Suitable Agent (or fallback to General Purpose)     | Quality Standards                      |
|-------------------|-----------------------------------------------------------------------|-----------------------------------------------------|----------------------------------------|
| EPIC_LOOP         | Phase {XX}: Epic Loop                                                 | -                                                   | -                                      |
| → EPIC_INIT       | Phase {XX}: Epic Discovery and Planning                               | Manager for epic level breakdown and story planning | -                                      |
| → STORY_LOOP      | Phase {XX}: [{SS/YY}] Story Loop                                      | -                                                   | -                                      |
| → → STORY_INIT    | Phase {XX}: [{SS/YY}] Story Discovery and Planning                    | Manager for story level breakdown and task planning | -                                      |
| → → TASK_LOOP     | Phase {XX}: [{SS/YY}] [{TT/ZZ}] Task Loop                             | -                                                   | -                                      |
| → → → TASK_INIT   | Phase {XX}: [{SS/YY}] [{TT/ZZ}] Task Discovery and Planning           | Manager for task breakdown and specification        | -                                      |
| → → → TASK_WORK   | Phase {XX}: [{SS/YY}] [{TT/ZZ}] [{II}] Implementation                 | Auto-discovered based on task requirements          | Standard implementation and validation |
| → → → TASK_TEST   | Phase {XX}: [{SS/YY}] [{TT/ZZ}] [{II}] Quality Validation             | Quality assurance agent for task validation         | Through-the-roof validation            |
| → → → TASK_DONE   | Phase {XX}: [{SS/YY}] [{TT/ZZ}] Task Completion                       | Manager for task level acceptance criteria          | Ruthless business validation           |
| → → STORY_DONE    | Phase {XX}: [{SS/YY}] Story Completion                                | Manager for story level acceptance criteria         | Complete coherence validation          |
| → EPIC_DONE       | Phase {XX}: Epic Completion                                           | Manager for strategic epic acceptance               | Strategic oversight                    |

### STATE TRANSITIONS

#### Task Loop Transitions (Atomic)
| State Name        | Transition State    | Code     | Description                                                    |
|-------------------|---------------------|----------|----------------------------------------------------------------|
| TASK_INIT         | TASK_WORK           | CONTINUE | Begin task implementation based on task requirements           |
| TASK_WORK         | TASK_TEST           | CONTINUE | Implementation complete - proceed to quality validation        |
| TASK_WORK         | TASK_WORK           | RETRY    | Partial implementation - continue with remaining deliverables  |
| TASK_TEST         | TASK_DONE           | CONTINUE | Quality validation passed - proceed to business validation     |
| TASK_TEST         | TASK_WORK           | RETRY    | Quality validation failed - return to implementation           |
| TASK_TEST         | TASK_TEST           | LOOP     | Partial validation - continue testing remaining components     |
| TASK_DONE         | TASK_LOOP           | CONTINUE | Business validation complete, start next unfinished task       |

#### Story Loop Transitions (Contains Task Loops)
| State Name        | Transition State    | Code     | Description                                                    |
|-------------------|---------------------|----------|----------------------------------------------------------------|
| STORY_INIT        | TASK_LOOP           | CONTINUE | Story initialized - enter task loop controller                 |
| TASK_LOOP         | TASK_INIT           | LOOP     | Start next unfinished task in story                            |
| TASK_LOOP         | STORY_DONE          | EXIT     | Only when all tasks complete - exit story loop                 |
| STORY_DONE        | STORY_LOOP          | CONTINUE | Return control to story loop, start next unfinished story      |

#### Epic Loop Transitions (Contains Story Loops)
| State Name        | Transition State    | Code     | Description                                                    |
|-------------------|---------------------|----------|----------------------------------------------------------------|
| EPIC_INIT         | STORY_LOOP          | CONTINUE | Epic initialized - enter story loop controller                 |
| STORY_LOOP        | STORY_INIT          | LOOP     | Start next unfinished story in epic                            |
| STORY_LOOP        | EPIC_DONE           | EXIT     | Only when all stories complete - exit epic loop                |

#### Project Loop Transitions (Contains Epic Loops)
| State Name        | Transition State    | Code     | Description                                                    |
|-------------------|---------------------|----------|----------------------------------------------------------------|
| EPIC_DONE         | EPIC_LOOP           | CONTINUE | Epic complete - return to epic loop controller for next epic   |
| EPIC_LOOP         | EPIC_INIT           | LOOP     | Start next unfinished epic                                     |
| EPIC_LOOP         | EXIT                | EXIT     | Only when all epics complete - exit orchestration              |

#### Loop Controller Logic
| Controller Name   | Decision Logic                                                                                  |
|-------------------|-------------------------------------------------------------------------------------------------|
| TASK_LOOP         | Find next unfinished task in current story → LOOP, only when all done → EXIT                    |
| STORY_LOOP        | Find next unfinished story in current epic → LOOP, only when all done → EXIT                    |
| EPIC_LOOP         | Find next unfinished epic in project → LOOP, only when all done → EXIT                          |
