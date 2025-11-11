<!-- Updated: 2025-11-11 18:03:58 UTC -->

### Phase {PHASE_NUMBER}: {PHASE_NAME}
Requirements discovery through **structured AskUserQuestion tool usage**

#### CRITICAL REQUIREMENTS
- **MUST** assess context completeness before proceeding
- **MUST** use AskUserQuestion tool for ALL questions
- **MUST** execute questionnaires for each level in completion plan
- **MUST** validate and store enriched context
- **MUST** be transparent about questioning process

#### CRITICAL RESTRICTIONS
- **NEVER** skip for new projects without complete context
- **NEVER** make assumptions without documenting them
- **NEVER** re-ask questions if context already complete
- **NEVER** proceed with incomplete requirements without user consent
- **NEVER** ask questions in plain text - **ALWAYS use AskUserQuestion tool**

#### EXECUTION FLOW

- **Update phase tracking**
  - Update "Phase {PHASE_NUMBER}: {PHASE_NAME}" task as in_progress

- **Assess context completeness**
  - **MUST** read and follow `plugin:orchestrator:resources://AGENT/MANAGER/REQUIREMENTS-DISCOVERY.md` workflow
  - **MUST** read and follow `plugin:orchestrator:resources://CORE/ASK-USER-QUESTION-TOOL.md` for tool usage guidelines
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

    - **Present questions with AskUserQuestion tool**
      - Announce: "Requirements Discovery for [level] level"
      - Formulate structured questions with 2-4 options each
      - **MUST** use AskUserQuestion tool - NEVER ask in plain text
      - Group related questions (max 4 questions per tool call)
      - Provide clear option descriptions with trade-offs
      - Each option must be concise (1-5 words) with informative description

    - **Collect and validate answers**
      - Execute AskUserQuestion tool calls for each category
      - User can select from options or choose "Other" for custom input
      - Restate understanding after each category
      - Get explicit user confirmation
      - Allow corrections and refinements via follow-up AskUserQuestion calls

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
