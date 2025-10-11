<!-- Updated: 2025-09-28 00:00:00 UTC -->

### Phase {PHASE_NUMBER}: {CONTROLLER_TYPE} Controller
Manages loop iteration and determines next work item

#### CRITICAL REQUIREMENTS
- **MUST** find next unfinished item in scope
- **MUST** update loop indicators accurately
- **MUST** determine correct next state

#### CRITICAL RESTRICTIONS
- **NEVER** skip items in sequence
- **NEVER** process completed items
- **NEVER** exit loop prematurely

#### EXECUTION FLOW

- **Update phase tracking**
  - Update "Phase {PHASE_NUMBER}: {CONTROLLER_TYPE} Controller" task as in_progress

- **Scan for next item**
  - Query all {ITEM_TYPE} in {PARENT_CONTEXT}
  - Filter for status != completed
  - Sort by priority and identifier
  - Select first unfinished item

- **Evaluate loop state**
  - When next item found:
    - Set current item: {NEXT_ITEM_IDENTIFIER}
    - Update loop position: {UPDATED_LOOP_INDICATORS}
    - **Report loop status (only after first iteration)**
      - When this is NOT the first iteration (processed count > 0):
        - **MUST** read and use `~/.claude/shared/templates/REPORT/STATE-CONTROLLER-LOOP.md` file as a template
        - **MUST** read and follow requirements from `~/.claude/shared/core/TEMPLATE-REQUIREMENTS.md` file
      - When this is the first iteration (processed count = 0):
        - Skip reporting, proceed directly to next state
    - Transition to: {INIT_STATE}
  - When no items remaining:
    - Mark loop as complete
    - Transition to: {DONE_STATE}

- **Update iteration tracking**
  - Increment processed count: {COMPLETED_COUNT}/{TOTAL_ITEMS}
  - **NEVER** create new phase tasks
  - **MUST** update existing phase tasks and their counters:
    - Find existing phase tasks for upcoming states
    - Update their names with current loop counter indicators
  - Record state transition

- **Complete phase**
  - Update "Phase {PHASE_NUMBER}: {CONTROLLER_TYPE} Controller" task as completed
  - Transition to determined next state
