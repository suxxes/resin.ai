<!-- Updated: 2025-10-17 20:32:34 UTC -->

### Phase {PHASE_NUMBER}: {CONTROLLER_TYPE} Loop Controller
Manages loop iteration and determines next work item

#### CRITICAL REQUIREMENTS
- **MUST** find next unfinished item in scope
- **MUST** update loop indicators accurately
- **MUST** determine correct next state
- **MUST** continue the loop until full completion
- **MUST** transition immediately without pausing for reports
- **MUST** never wait for user acknowledgment between loop iterations

#### CRITICAL RESTRICTIONS
- **NEVER** skip items in sequence
- **NEVER** process completed items
- **NEVER** pause or exit loop prematurely
- **NEVER** stop to report progress (brief inline status only)
- **NEVER** wait for user input during autonomous loop execution

#### EXECUTION FLOW

- **Update phase tracking**
  - Update "Phase {PHASE_NUMBER}: {CONTROLLER_TYPE} Loop Controller" task as in_progress

- **Scan for next item**
  - Query all {ITEM_TYPE} in {PARENT_CONTEXT}
  - Filter for status != completed
  - Sort by priority and identifier
  - Select first unfinished item

- **Evaluate loop state**
  - When next item found:
    - Set current item: {NEXT_ITEM_IDENTIFIER}
    - Update loop position: {UPDATED_LOOP_INDICATORS}
    - Set `NEXT_STATE` to {INIT_STATE}
  - When no items remaining:
    - Mark loop as complete
    - Set `NEXT_STATE` to {DONE_STATE}

- **Update iteration tracking**
  - Increment processed count: {COMPLETED_COUNT}/{TOTAL_ITEMS}
  - **NEVER** create new phase tasks
  - **MUST** update existing phase tasks and their counters:
    - Find existing phase tasks for upcoming states
    - Update their names with current loop counter indicators
  - Record state transition

- **Complete phase**
  - Update "Phase {PHASE_NUMBER}: {CONTROLLER_TYPE} Loop Controller" task as completed
  - **MUST** transition IMMEDIATELY to {NEXT_STATE} without pausing
