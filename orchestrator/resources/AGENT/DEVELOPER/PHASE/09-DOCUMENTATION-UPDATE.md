<!-- Updated: 2025-10-17 11:46:57 UTC -->

### Phase X: Documentation Update
Update documentation and code comments

#### CRITICAL REQUIREMENTS
- **MUST** create comprehensive documentation
- **MUST** ensure documentation accuracy
- **MUST** maintain documentation standards

#### CRITICAL RESTRICTIONS
- **NEVER** skip documentation updates
- **NEVER** leave code undocumented
- **NEVER** provide outdated information

#### EXECUTION FLOW

- **Update phase tracking**
  - Update "Phase 09: Documentation Update" task as in_progress

- **Feature Documentation**
  - **MUST** create comprehensive feature documentation after loop completion
  - **MUST** store feature files in `docs/FEATURE/{FEATURE_ID} - {FEATURE_TITLE}.md` format
  - **MUST** use appropriate identifier based on work level:
    - Task level: `{EPIC_ID}.{STORY_ID}.{TASK_ID} - {TASK_TITLE}.md`
    - Story level: `{EPIC_ID}.{STORY_ID} - {STORY_TITLE}.md`
    - Epic level: `{EPIC_ID} - {EPIC_TITLE}.md`
  - **MUST** read and use `plugin:orchestrator:resources://TEMPLATE/DOCUMENTATION/FEATURE.md` as template
  - **MUST** read and follow requirements from `plugin:orchestrator:resources://CORE/TEMPLATE-REQUIREMENTS.md`
  - Document all code implementation details (functions, algorithms, patterns, examples, warnings)
  - Document all API changes (endpoints, contracts, authentication, errors, examples)
  - Document all system updates (architecture, configuration, deployment, operations, troubleshooting)
  - Document all implementation details (decisions, deviations, issues, metrics)
  - Capture all lessons learned (implementation decisions, challenges, insights, best practices)

- **Architecture Decision Records**
  - **MUST** create ADR for architectural decisions
  - **MUST** store ADR files in `docs/ADR/{XXXX} - {ADR_TITLE}.md` format
  - **MUST** use sequential numbering for {XXXX} (e.g., 0001, 0002, 0003)
  - **MUST** read and use `plugin:orchestrator:resources://TEMPLATE/DOCUMENTATION/ADR.md` as template
  - **MUST** read and follow requirements from `plugin:orchestrator:resources://CORE/TEMPLATE-REQUIREMENTS.md`
  - Document technology selection decisions with rationale
  - Record architectural pattern choices with trade-offs
  - Capture design decisions affecting system structure
  - Document integration approach decisions with consequences

- **Complete phase**
  - Update "Phase 09: Documentation Update" task as completed
  - Transition to "Phase XX: Update Progress"
