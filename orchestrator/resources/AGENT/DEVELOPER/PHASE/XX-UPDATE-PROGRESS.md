### Phase X: Update Progress
Update task/story/epic/roadmap documentation based on current work status

#### CRITICAL REQUIREMENTS
- **MUST** execute at two points: after Initialize Tasks and before Validation and Handoff
- **MUST** detect current Development Status and transition appropriately
- **MUST** propagate all status changes to parent documentation
- **MUST** update project roadmap

#### CRITICAL RESTRICTIONS
- **NEVER** skip this phase
- **NEVER** update only task file without propagating to parents
- **NEVER** assume status without reading current state
- **NEVER** set Completion Date in task files
- **NEVER** set story Status to COMPLETED
- **NEVER** set epic Status to COMPLETED

#### EXECUTION FLOW

- **Update phase tracking**
  - Update "Phase XX: Update Progress" task as in_progress

- **Get current timestamp in UTC**
  - **USE** `date -u` bash command

- **Locate and read task file**
  - Read current task file `docs/DEVELOPMENT-PLAN/{TASK_ID} - {TASK_NAME}.md`
  - **MUST** extract exact TASK_ID from delegation or context
  - **MUST** extract current **Development Status** and **QA Validation Status**

- **Determine status transition**
  - When **Development Status** is `NOT_STARTED`:
    - Set **Development Status**: `IN_PROGRESS`
    - Set **QA Validation Status**: `NOT_STARTED`
  - When **Development Status** is `IN_PROGRESS` and work is complete:
    - Set **Development Status**: `COMPLETED`
    - Set **QA Validation Status**: `QA_PENDING`
  - When **Development Status** is `COMPLETED`:
    - No change (already complete)

- **Update task file**
  - Apply status transition determined above
  - Set **Last Updated** to current UTC timestamp

- **Update parent story file**
  - Read current story file `docs/DEVELOPMENT-PLAN/{STORY_ID} - {STORY_NAME}.md`
  - **MUST** extract exact STORY_ID from file task name
  - Count tasks by status in story
  - Set **Progress** to `{COMPLETED}/{TOTAL} tasks completed`
  - Calculate and update **Status**:
    - All tasks with `QA_PASSED` → `COMPLETED`
    - Any task `IN_PROGRESS` or `COMPLETED` (not yet `QA_PASSED`) → `IN_PROGRESS`
    - All tasks `NOT_STARTED` → `NOT_STARTED`
  - Set **Last Updated** to current UTC timestamp
  - Set current task row in task table to new status

- **Update parent epic file**
  - Read current epic file `docs/DEVELOPMENT-PLAN/{EPIC_ID} - {EPIC_NAME}.md`
  - **MUST** extract exact EPIC_ID from file task name
  - Count stories by status in epic
  - Set **Progress** to `{COMPLETED}/{TOTAL} stories completed ({PERCENTAGE}%)`
  - Calculate and update **Status**:
    - All stories `COMPLETED` (all tasks `QA_PASSED`) → `COMPLETED`
    - Any story `IN_PROGRESS` → `IN_PROGRESS`
    - All stories `NOT_STARTED` → `NOT_STARTED`
  - Set **Last Updated** to current UTC timestamp
  - Set current story row in story table to new status

- **Update project roadmap**
  - Read development roadmap file `docs/DEVELOPMENT-PLAN.md`
  - Set task row Status and Progress columns to current values
  - Set story row Status and Progress columns to current values
  - Set epic row Status and Progress columns to current values
  - Set **Last Updated** to current UTC timestamp

- **Complete phase**
  - Update "Phase XX: Update Progress" task as completed
  - Transition to next phase based on position in workflow
