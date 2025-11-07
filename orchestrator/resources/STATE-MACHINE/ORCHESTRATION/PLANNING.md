<!-- Updated: 2025-10-17 02:10:21 UTC -->

## PLANNING ORCHESTRATION

Planning orchestration coordinates hierarchical planning from requirements discovery through validation. It builds the completion plan based on detected scope, enriches context for each level, and delegates to appropriate planning specialists.

### CRITICAL REQUIREMENTS
- **MUST** follow **STATE TRANSITIONS** requirements impeccably and unquestioningly
- **MUST** create ALL phase tasks upfront during initialization
- **MUST** use values from "Phase Name" column for phase task names
- **MUST** update existing phase task names when entering loops (never create new phase tasks)
- **MUST** dynamically update phase names based on current position in the planning loop
- **MUST** assume next available loop state, if not currently in the loop
- **MUST** use ordered numbering with the zero-padded value to the maximum length among the related values with minimum length of 2
- **{XX}** - Orchestration phase (XX = phase number in phases order)
- **{LL}** - Level iteration (LL = current level index in `COMPLETION_PLAN`)
- **{TT}** - Total levels (TT = total number of levels in `COMPLETION_PLAN`)

### CRITICAL RESTRICTIONS
- **NEVER** leave placeholders without proper values
- **NEVER** create new phase tasks when entering loops (update existing ones)
- **NEVER** skip creating any phase task during initialization
- **NEVER** create multiple tasks for the same phase state (exactly ONE task per phase state)
- **NEVER** include planning levels beyond the detected scope in `COMPLETION_PLAN`
- **NEVER** create tasks for creating stories or stories for creating epics
- **NEVER** create "Research"-type stories or tasks unless research is the sole and explicit purpose of the planning request
  - Research is performed during Comprehensive Research phase
  - Stories and tasks must represent implementable deliverables, not research activities
  - When requested "research X technology", that's acceptable research scope
  - When planning a feature, NEVER create separate research stories or tasks

### PLANNING SCOPE BOUNDARIES

Planning scope determines the maximum depth of the `COMPLETION_PLAN`

#### CRITICAL REQUIREMENTS
- Parent levels must only be included when they don't exist
- Epics are created as part of Project planning. When Project-level planning is happening, all its epics breakdown must be included.
- Stories are created as part of Epic planning. When Epic-level planning is happening, all its stories breakdown must be included.
- Tasks are created as part of Story planning. When Story-level planning is happening, all its tasks breakdown must be included.

| Detected Scope | Maximum Levels in COMPLETION_PLAN | Description                                                           |
|----------------|-----------------------------------|-----------------------------------------------------------------------|
| **Project**    | [Project]                         | Project-level planning - creates project docs and all epics breakdown |
| **Epic**       | [Project, Epic]                   | Epic-level planning - breaks down an epic into all its stories        |
| **Story**      | [Project, Epic, Story]            | Story-level planning - breaks down a story into all its tasks         |


### CRITICAL REQUIREMENTS: PLAN_INIT

In addition to standard INIT template requirements, PLAN_INIT **MUST**:

- **Determine requested scope** from user input or auto-discovery
- **Check for missing parent levels** (bottom-up)
- **Add missing parents** to plan (top-down order)
- **Stop at requested scope** - DO NOT add child levels

- **Apply critical thinking to evaluate appropriate planning scope**
  - **MUST** read and use `plugin:orchestrator:resources://CORE/EPIC-STORY-TASK-FORMAT.md` to understand hierarchy
  - Consider existing project state and documentation maturity
  - Analyze input and description complexity, size, and impact
  - Use judgment to determine most appropriate planning level
  - **CRITICAL THINKING CRITERIA**:
    - **Project scope** - New systems, platforms, major initiatives requiring full architectural planning with breakdown into epics
    - **Epic scope** - Major features, significant capabilities, multi-story initiatives with breakdown into stories
    - **Story scope** - Discrete features, user-facing capabilities, complete user value with breakdown into tasks
  - **RED FLAGS** that indicate scope underestimation:
    - Input says "simple" but describes complex integration points
    - Request involves multiple systems, or technologies
    - Solution requires new architecture, patterns, or infrastructure
    - Changes affect multiple workflows or processes
    - Implementation requires significant research or proof-of-concept
  - **JUDGMENT CRITERIA**:
    - When input is vague
      - Assume higher scope (Epic > Story)
    - When impact spans multiple areas
      - Escalate to Epic or Project
    - When work seems atomic/simple
      - It's likely a Story (not a separate task planning session)
    - When dependencies are unclear
      - Choose scope that allows proper discovery
    - When similar past work was larger
      - Match or exceed that scope
    - When in doubt
      - Choose higher scope for better planning
  - Document scope rationale in analysis report

- **Detect requested planning scope** (Project, Epic, or Story) based on critical evaluation
- **Validate hierarchical prerequisites using scope boundaries table**
- **Build `COMPLETION_PLAN` following construction rules**
  - **MUST** read and use `plugin:orchestrator:resources://CORE/EPIC-STORY-TASK-FORMAT.md` to understand hierarchy format requirements
  - Initialize `COMPLETION_PLAN` as empty list
  - Initialize flags: `NEEDS_PROJECT = false`, `NEEDS_EPIC = false`, `NEEDS_STORY = false`

  - Check hierarchy from bottom to top (set flags based on detected scope and missing parents):
    - When Story scope detected:
      - Set `NEEDS_STORY = true`
      - When NO Story files exist in `docs/DEVELOPMENT-PLAN/` matching `{EPIC_ID}.{STORY_ID} - *.md` pattern:
        - When NO Epic files exist in `docs/DEVELOPMENT-PLAN/` matching `{EPIC_ID} - *.md` pattern:
          - Set `NEEDS_EPIC = true`
    - When Epic scope detected:
      - Set `NEEDS_EPIC = true`
    - When Project scope detected:
      - Set `NEEDS_PROJECT = true`
    - When `NEEDS_EPIC = true` AND `docs/DEVELOPMENT-PLAN.md` does NOT exist:
      - Set `NEEDS_PROJECT = true`

  - Build `COMPLETION_PLAN` in top-down order (add levels based on flags):
    - When `NEEDS_PROJECT = true`:
      - Add "Project" to `COMPLETION_PLAN`
    - When `NEEDS_EPIC = true`:
      - Add "Epic" to `COMPLETION_PLAN`
    - When `NEEDS_STORY = true`:
      - Add "Story" to `COMPLETION_PLAN`

- **Store requested scope** for validation in PLAN_DONE state
- **Report completion plan** showing all levels to be created with examples of what will be created

### CRITICAL REQUIREMENTS: PLAN_QUIZ STATE

In addition to standard QUIZ template requirements, PLAN_QUIZ **MUST**:

- **Execute questionnaires only for levels in COMPLETION_PLAN**
- **Store level-specific enriched context** in `ENRICHED_CONTEXT` dictionary
- **Consolidate context** for PLAN_WORK state consumption

### CRITICAL REQUIREMENTS: PLAN_WORK STATE

In addition to standard WORK template requirements, PLAN_WORK **MUST**:

- **Use current level from COMPLETION_PLAN** to determine appropriate agent
- **Pass level-specific enriched context** from `ENRICHED_CONTEXT[CURRENT_LEVEL]`
- **Validate hierarchy format compliance** after delegation
- **Extract created IDs** for passing to next level:
  - When Epic created: Extract `EPIC_ID`
  - When Story created: Extract `STORY_ID` and verify tasks created

### CRITICAL REQUIREMENTS: PLAN_DONE STATE

PLAN_DONE follows the standard DONE template (`plugin:orchestrator:resources://STATE-MACHINE/STATE/DONE.md`) which handles branch operations at the orchestration level.

In addition to standard DONE template requirements, PLAN_DONE **MUST**:

- **Verify actual created files against requirements**

  - **NEVER** trust agents report

  - When Project level in `COMPLETION_PLAN`:
    - **MUST** verify these files exist and are complete:
      - `docs/OVERVIEW.md` - Project description and goals
      - `docs/ARCHITECTURE.md` - System architecture and design
      - `docs/TECH-STACK.md` - Technology choices and rationale
      - `docs/DEPLOYMENT.md` - Deployment procedures
      - `docs/DEVELOPMENT.md` - Development setup and workflow
      - `docs/FILES.md` - File structure documentation
      - `docs/DEVELOPMENT-PLAN.md` - Roadmap table with Epics/Stories/Tasks structure
    - **MUST** verify Epic files matching `docs/DEVELOPMENT-PLAN/{EPIC_ID} - {EPIC_NAME}.md` pattern exist
      - **MUST** read and use `plugin:orchestrator:resources://CORE/EPIC-STORY-TASK-FORMAT.md`
      - **MUST** validate Epic IDs follow `{EPIC_ID}` format
      - **MUST** verify Epic files contain required sections
      - **MUST** validate Epic IDs are sequential within Project
    - **MUST** validate each file has substantial content (not just headers)
    - **MUST** verify `docs/DEVELOPMENT-PLAN.md` contains proper roadmap table structure with links to Epic files

  - When Epic level in `COMPLETION_PLAN`:
    - **MUST** read and use `plugin:orchestrator:resources://CORE/EPIC-STORY-TASK-FORMAT.md`
      - **MUST** verify Story file exists matching `docs/DEVELOPMENT-PLAN/{EPIC_ID}.{STORY_ID} - {STORY_NAME}.md` pattern
      - **MUST** validate Story ID follows `{EPIC_ID}.{STORY_ID}` format
      - **MUST** verify Epic ID matches existing parent Epic
      - **MUST** verify Story file contains required sections
      - **MUST** validate Story ID is sequential within Epic
    - **MUST** verify `docs/DEVELOPMENT-PLAN.md` contains proper roadmap table structure with links to Story files

  - When Story level in `COMPLETION_PLAN`:
    - **MUST** read and use `plugin:orchestrator:resources://CORE/EPIC-STORY-TASK-FORMAT.md`
      - **MUST** verify Task file exists matching `docs/DEVELOPMENT-PLAN/{EPIC_ID}.{STORY_ID}.{TASK_ID} - {TASK_NAME}.md` pattern
      - **MUST** validate Task ID follows `{EPIC_ID}.{STORY_ID}.{TASK_ID}` format
      - **MUST** verify Epic ID and Story ID match existing parent hierarchy
      - **MUST** verify Task file contains required sections
      - **MUST** validate Task ID is sequential within Story
    - **MUST** verify `docs/DEVELOPMENT-PLAN.md` contains proper roadmap table structure with links to Task files

- **Prepare handoff package** with:
  - List of all created file paths
  - Created IDs (Epic ID, Story ID) and task count for each story
  - Validation summary showing all checks passed
  - Branch merge confirmation
  - Next steps for development (if applicable)

### PLANNING CONTROLLER

| State Name        | Phase Name (with Loop Indicators)                                     | Suitable Agent (or fallback to General Purpose)     | Quality Standards                      |
|-------------------|-----------------------------------------------------------------------|-----------------------------------------------------|----------------------------------------|
| PLAN_LOOP         | -                                                                     | -                                                   | -                                      |
| → PLAN_INIT       | Phase {XX}: Context Discovery and Hierarchy Analysis                  | -                                                   | -                                      |
| → PLAN_QUIZ       | Phase {XX}: Requirements Discovery                                    | -                                                   | -                                      |
| → PLAN_WORK       | Phase {XX}: [{LL}/{TT}] {PLANNING_SCOPE} Planning                     | Auto-discovered based on level requirements         | Standard planning and validation       |
| → PLAN_DONE       | Phase {XX}: Validation and Handoff                                    | -                                                   | -                                      |

### STATE TRANSITIONS

| State Name        | Transition State    | Code     | Description                                                    |
|-------------------|---------------------|----------|----------------------------------------------------------------|
| PLAN_LOOP         | PLAN_INIT           | CONTINUE | Start planning execution                                       |
| PLAN_LOOP         | EXIT                | EXIT     | No planning needed - exit orchestration                        |
| PLAN_INIT         | PLAN_QUIZ           | CONTINUE | Completion plan built - proceed to requirements discovery      |
| PLAN_INIT         | EXIT                | ERROR    | No levels in completion plan - exit with error                 |
| PLAN_QUIZ         | PLAN_LOOP           | CONTINUE | Requirements enrichment complete - start level loop            |
| PLAN_LOOP         | PLAN_WORK           | CONTINUE | Process next level in completion plan                          |
| PLAN_WORK         | PLAN_LOOP           | CONTINUE | Level planning complete - return to controller                 |
| PLAN_LOOP         | PLAN_DONE           | EXIT     | All levels complete - proceed to validation                    |
| PLAN_DONE         | EXIT                | EXIT     | Planning validation complete - exit orchestration              |
