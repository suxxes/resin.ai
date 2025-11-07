<!-- Updated: 2025-10-17 12:14:58 UTC -->

### Phase {PHASE_NUMBER}: {PHASE_NAME}
Requirements discovery through structured questionnaires

#### CRITICAL REQUIREMENTS
- **MUST** assess context completeness before proceeding
- **MUST** execute questionnaires for each level in completion plan
- **MUST** validate and store enriched context
- **MUST** be transparent about questioning process

#### CRITICAL RESTRICTIONS
- **NEVER** skip for new projects without complete context
- **NEVER** make assumptions without documenting them
- **NEVER** re-ask questions if context already complete
- **NEVER** proceed with incomplete requirements without user consent

#### EXECUTION FLOW

- **Update phase tracking**
  - Update "Phase {PHASE_NUMBER}: {PHASE_NAME}" task as in_progress

- **Assess context completeness**
  - **MUST** read and follow `plugin:orchestrator:resources://AGENT/MANAGER/REQUIREMENTS-DISCOVERY.md` workflow
  - Get `COMPLETION_PLAN` from previous state
  - Evaluate if user description contains sufficient planning detail
  - Check against scope-specific required information checklist
  - Determine if questionnaire is required for any level in `COMPLETION_PLAN`

- **Check skip conditions**
  - When existing project has complete documentation, or:
  - When user description is comprehensive and complete, or
  - When user explicitly requests to skip or use assumptions:
    - **MUST** skip questionnaire execution and proceed to enriched context storage

- **Execute questionnaire for each level in completion plan**
  - Set `ENRICHED_CONTEXT = {}`
  - For each level in `COMPLETION_PLAN`:

    - **Select questionnaire template**
      - **MUST** read and use `plugin:orchestrator:resources://TEMPLATE/QUESTIONNAIRE.md` as a template
      - **MUST** set `{SCOPE_LEVEL}` to current level from `COMPLETION_PLAN` (PROJECT, EPIC, STORY, or TASK)
      - **MUST** set `{SCOPE_LEVEL_LOWERCASE}` to lowercase version of scope level (project, epic, story, or task)
      - **MUST** read and follow requirements from `plugin:orchestrator:resources://CORE/TEMPLATE-REQUIREMENTS.md`
      - **MUST** preserve template organization

    - **Present questions with transparency**
      - Announce: "Requirements Discovery for [level] level"
      - Announce total question count and categories
      - Group questions by category
      - Number questions sequentially
      - Allow user to skip at any time

    - **Collect and validate answers**
      - Ask questions one category at a time
      - Restate understanding after each category
      - Get explicit user confirmation
      - Allow corrections and refinements

    - **Handle user skip request**
      - When user types "skip" or requests assumptions:
        - Acknowledge request
        - Apply level-appropriate default assumptions
        - Document assumptions clearly
        - Continue to next level in `COMPLETION_PLAN`

    - **Store level-specific enriched context**
      - Add to `ENRICHED_CONTEXT[level]`:
        - Original user request
        - Validated answers from questionnaire
        - Applied assumptions for skipped questions
        - Enrichment timestamp

- **Consolidate enriched context**
  - Combine all level-specific contexts into single structure
  - Ensure no redundant information across levels
  - Prepare consolidated context for agent delegation

- **Complete phase**
  - Update "Phase {PHASE_NUMBER}: {PHASE_NAME}" task as completed
  - Transition to {NEXT_STATE}
