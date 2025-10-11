<!-- Updated: 2025-10-16 13:30:00 UTC -->

### Phase X: Update Progress
Update task/story/epic/roadmap documentation based on current QA status

#### CRITICAL REQUIREMENTS
- **MUST** execute at two points: after Initialize Tasks and before Validation and Handoff
- **MUST** detect current QA Validation Status and transition appropriately
- **MUST** propagate all status changes to parent documentation
- **MUST** update project roadmap
- **MUST** set task Completion Date when setting QA_PASSED
- **MUST** set story/epic to COMPLETED only when all tasks have QA_PASSED

#### CRITICAL RESTRICTIONS
- **NEVER** skip this phase
- **NEVER** update only task file without propagating to parents
- **NEVER** assume status without reading current state

#### EXECUTION FLOW

- **Update phase tracking**
  - Update "Phase X: Update Progress" task as in_progress

- **Get current timestamp in UTC**
  - **USE** `date -u` bash command

- **Locate and read task file**
  - Read current task file `docs/DEVELOPMENT-PLAN/{TASK_ID} - {TASK_NAME}.md`
  - **MUST** extract exact TASK_ID from delegation or context
  - **MUST** extract current **Development Status** and **QA Validation Status**
  - Verify **Development Status** is `COMPLETED`

- **Determine status transition**
  - When **QA Validation Status** is `QA_PENDING`:
    - Set **QA Validation Status**: `QA_IN_PROGRESS`
  - When **QA Validation Status** is `QA_IN_PROGRESS` and validation complete:
    - Set **QA Validation Status**: `QA_PASSED` (if all standards met)
    - Set **QA Validation Status**: `QA_FAILED` (if critical issues found)
  - When **QA Validation Status** is already `QA_PASSED` or `QA_FAILED`:
    - No change (already complete)

- **Update task file**
  - Apply status transition determined above
  - Set **Last Updated** to current UTC timestamp
  - When setting **QA Validation Status** to `QA_PASSED`:
    - Set **Completion Date** to current UTC timestamp

- **Update parent story file**
  - Read current story file `docs/DEVELOPMENT-PLAN/{STORY_ID} - {STORY_NAME}.md`
  - **MUST** extract exact STORY_ID from file task name
  - Count tasks by QA status in story
  - Set **Progress** to `{QA_PASSED_COUNT}/{TOTAL} tasks completed`
  - Calculate and update **Status**:
    - All tasks with `QA_PASSED` → `COMPLETED`
    - Any task `IN_PROGRESS` or `QA_PENDING` or `QA_IN_PROGRESS` or `QA_FAILED` → `IN_PROGRESS`
    - All tasks `NOT_STARTED` → `NOT_STARTED`
  - Set **Last Updated** to current UTC timestamp
  - Set current task row in task table to new QA status
  - When status becomes `COMPLETED`:
    - Set **Completion Date** to current UTC timestamp

- **Update parent epic file**
  - Read current epic file `docs/DEVELOPMENT-PLAN/{EPIC_ID} - {EPIC_NAME}.md`
  - **MUST** extract exact EPIC_ID from file task name
  - Count stories by completion status in epic
  - Set **Progress** to `{COMPLETED_COUNT}/{TOTAL} stories completed ({PERCENTAGE}%)`
  - Calculate and update **Status**:
    - All stories `COMPLETED` (all tasks `QA_PASSED`) → `COMPLETED`
    - Any story `IN_PROGRESS` → `IN_PROGRESS`
    - All stories `NOT_STARTED` → `NOT_STARTED`
  - Set **Last Updated** to current UTC timestamp
  - Set current story row in story table to new status
  - When status becomes `COMPLETED`:
    - Set **Completion Date** to current UTC timestamp

- **Update project roadmap**
  - Read development roadmap file `docs/DEVELOPMENT-PLAN.md`
  - Set task row Status and Progress columns to current QA status
  - Set story row Status and Progress columns to current values
  - Set epic row Status and Progress columns to current values
  - Set **Last Updated** to current UTC timestamp

- **Complete phase**
  - Update "Phase X: Update Progress" task as completed
  - Transition to next phase based on position in workflow
