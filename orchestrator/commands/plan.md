# Plan - Planning Orchestrator

<!-- Updated: 2025-10-03 09:34:15 UTC -->

Planning Orchestrator that coordinates planning through formalized algorithms and specialized subagents. Maintains architectural coherence while ensuring deterministic execution paths through scope-based routing and template-driven documentation.

**CRITICAL**: When this command is invoked, you enter **Planning mode** where all operations follow strict algorithmic patterns.
- You **MUST** execute algorithms exactly as defined and in defined order.
- You **MUST** follow and respect all requirements and restrictions.
- You **MUST** be concise and report only when and only in the way you've been instructed.
- You **MUST NOT** report any information between actions and phases unless instructed to do so.
- You **MUST** use ordered numbering for Phases instead of X.
- You **MUST** update Phases numbering order when new Phases list or ordering changes.


## USAGE
- `/plan [DESCRIPTION]` - Initiates algorithmic planning

### Examples
- `/plan "Build SaaS platform"` - Project-level orchestration
- `/plan "Add authentication"` - Epic-level orchestration
- `/plan "User login story"` - Story-level orchestration
- `/plan "Fix database query"` - Task-level orchestration


## PROCESS DEFINITION


### Phase X: Initialize Tasks
Creates planning tasks for progress tracking

#### CRITICAL REQUIREMENTS
- **MUST** create all phase tracking tasks
- **MUST** use TodoWrite for task management
- **MUST** proceed through all phases

#### CRITICAL RESTRICTIONS
- **NEVER** skip this phase
- **NEVER** proceed without task initialization
- **NEVER** create phases out of order

#### EXECUTION FLOW

- **Initialize phase tracking**
  - Create "Phase X: Initialize Tasks" task as in_progress
  - Create "Phase X: Context Discovery" task as pending
  - Create "Phase X: Requirements Discovery" task as pending
  - Create "Phase X: Subagent Discovery" task as pending
  - Create "Phase X: Documentation Creation" task as pending
  - Create "Phase X: Validation and Handoff" task as pending

- **Complete phase**
  - Update "Phase X: Initialize Tasks" task as completed
  - Transition to "Phase X: Context Discovery"


### Phase X: Context Discovery
Analyzes request and establishes planning context

#### CRITICAL REQUIREMENTS
- **MUST** determine exact scope level before proceeding
- **MUST** assess existing project structure if present
- **MUST** create tracking tasks in TodoWrite

#### CRITICAL RESTRICTIONS
- **NEVER** proceed without scope determination
- **NEVER** assume context without verification
- **NEVER** skip technology assessment

#### EXECUTION FLOW

- **Update phase tracking**
  - Update "Phase X: Context Discovery" task as in_progress

- **Check for existing project structure**
  - When `docs/OVERVIEW.md` file does not exist:
    - **MUST** treat as new project
  - Otherwise:
    - **MUST** treat as existing project

- **Analyze project context**
  - Read `README.md` file

- **Analyze existing project context (if applicable)**
  - Read `docs/OVERVIEW.md` file
  - Read `docs/ARCHITECTURE.md` file
  - Read `docs/TECH-STACK.md` file

- **Determine planning scope level**
  - Extract and analyze project structure
  - Detect scope as one of Project, Epic, Story, or Task from user description and project context

- **Identify technology requirements**
  - Analyze detected scope for technology needs
  - Determine required frameworks and tools

- **Report project analysis**
  - **MUST** read and use `~/.claude/shared/templates/REPORT/PROJECT-OVERVIEW.md` file as a template
  - **MUST** read and follow requirements from `~/.claude/shared/core/TEMPLATE-REQUIREMENTS.md` file
  - **MUST** preserve template organization

- **Complete phase**
  - Update "Phase X: Context Discovery" task as completed
  - Transition to "Phase X: Requirements Discovery"


### Phase X: Requirements Discovery
Enriches planning context through structured questioning when needed

#### CRITICAL REQUIREMENTS
- **MUST** assess context completeness before proceeding
- **MUST** follow requirements enrichment workflow
- **MUST** validate and store enriched context
- **MUST** be transparent about questioning process

#### CRITICAL RESTRICTIONS
- **NEVER** skip for new projects without complete context
- **NEVER** make assumptions without documenting them
- **NEVER** re-ask questions if context already complete
- **NEVER** proceed with incomplete requirements without user consent

#### EXECUTION FLOW

- **Update phase tracking**
  - Update "Phase X: Requirements Discovery" task as in_progress

- **Assess context completeness**
  - **MUST** read and follow `~/.claude/shared/workflows/REQUIREMENTS-DISCOVERY.md` workflow
  - Evaluate if user description contains sufficient planning detail
  - Check against scope-specific required information checklist
  - Determine if questionnaire is required

- **Check skip conditions**
  - When existing project has complete documentation, or:
  - When user description is comprehensive and complete, or
  - When user explicitly requests to skip or use assumptions:
    - **MUST** skip to "Phase X: Subagent Discovery"

- **Execute questionnaire**
  - When project level planning:
    - **MUST** read and use `~/.claude/shared/templates/REQUIREMENTS-QUESTIONS/PROJECT.md` file as a template
  - When epic level planning:
    - **MUST** read and use `~/.claude/shared/templates/REQUIREMENTS-QUESTIONS/EPIC.md` file as a template
  - When story level planning:
    - **MUST** read and use `~/.claude/shared/templates/REQUIREMENTS-QUESTIONS/STORY.md` file as a template
  - When task level planning:
    - **MUST** read and use `~/.claude/shared/templates/REQUIREMENTS-QUESTIONS/TASK.md` file as a template
  - **MUST** read and follow requirements from `~/.claude/shared/core/TEMPLATE-REQUIREMENTS.md` file
  - **MUST** preserve template organization

  - Present questions with transparency:
    - Announce total question count and categories
    - Group questions by category
    - Number questions sequentially
    - Allow user to skip at any time

  - Collect and validate answers:
    - Ask questions one category at a time
    - Restate understanding after each category
    - Get explicit user confirmation
    - Allow corrections and refinements

- **Handle user skip request**
  - When user types "skip" or requests assumptions:
    - Acknowledge request
    - Apply scope-appropriate default assumptions
    - Document assumptions clearly
    - Proceed to enriched context storage

- **Store enriched context**
  - Create enriched context structure with:
    - Original user request
    - Validated answers from questionnaire
    - Applied assumptions for skipped questions
    - Enrichment timestamp and scope level
  - Prepare for subagent delegation

- **Complete phase**
  - Update "Phase X: Requirements Discovery" task as completed
  - Transition to "Phase X: Subagent Discovery"


### Phase X: Subagent Discovery
Discovers an appropriate planning subagent

#### CRITICAL REQUIREMENTS
- **MUST** use scope level to determine required capability
- **MUST** use internal knowledge of all available subagents, their specializations and capabilities
- **MUST** follow subagent discovery protocol
- **MUST** discover or exit - no direct planning

#### CRITICAL RESTRICTIONS
- **NEVER** skip subagent discovery
- **NEVER** proceed if subagent unavailable
- **NEVER** attempt planning yourself
- **NEVER** execute discovered subagent in this phase
- **NEVER** use files to determine available subagents

#### EXECUTION FLOW

- **Update phase tracking**
  - Update "Phase X: Subagent Discovery" task as in_progress

- **Define discovery limitations based on scope-specific requirements**
  - When project level planning:
    - System architecture, epic discovery, technology stack
  - When epic level planning:
    - Feature architecture, integration design, success criteria
  - When story level planning:
    - Story breakdown, acceptance criteria, task decomposition
  - When task level planning:
    - Task specification, implementation notes, testing approach

  - **Discover and filter subagents**
    - Find all available and active subagents
    - Filter subagents to match subagent discovery limitations
    - Score each subagent based on discovery limitations compatibility
    - Only keep highest scoring subagents with score > 75
    - Select top-most subagent from the list of highest scoring subagents

  - **Ensure subagent unavailability**
    - When no suitable subagent found:
      - **MUST** stop and exit immediately with error report

  - **Report subagent selection**
    - **MUST** read and use `~/.claude/shared/templates/REPORT/SUBAGENT-DISCOVERY.md` file as a template
    - **MUST** read and follow requirements from `~/.claude/shared/core/TEMPLATE-REQUIREMENTS.md` file
    - **MUST** preserve template organization
    - Include each and every discovered subagent, including irrelevant ones
    - Include each and every highest scoring subagent

- **Prepare delegation context**
  - Extract delegation context from project information
  - Include enriched context from Requirements Enrichment phase (if available)
  - Specify expected deliverables based on scope
  - Determine quality standards for the scope level
  - Combine into planning context package with enriched requirements

- **Complete phase**
  - Update "Phase X: Subagent Discovery" task as completed
  - Transition to "Phase X: Documentation Orchestration"


### Phase X: Documentation Orchestration
Coordinates parallel documentation creation

#### CRITICAL REQUIREMENTS
- **MUST** create appropriate documentation for scope
- **MUST** verify documentation completeness
- **MUST** use parallel execution when possible

#### CRITICAL RESTRICTIONS
- **NEVER** create documentation directly
- **NEVER** skip required documentation
- **NEVER** proceed with incomplete documentation

#### EXECUTION FLOW

- **Update phase tracking**
  - Update "Phase X: Documentation Creation" task as in_progress

- **Delegate to selected subagent**

  - **Report subagent selection**
    - **MUST** read and use `~/.claude/shared/templates/REPORT/SUBAGENT-DELEGATION.md` file as a template
    - **MUST** read and follow requirements from `~/.claude/shared/core/TEMPLATE-REQUIREMENTS.md` file
    - **MUST** preserve template organization

  - **Invoke selected subagent**
    - Task selected subagent with prepared context including enriched requirements
    - Include scope definition, expected deliverables, and quality standards
    - Pass enriched context with validated requirements and documented assumptions
    - Wait for selected subagent to complete

  - **Collect subagent outputs**
    - Gather outputs from subagent results
    - Extract list of completed work

- **Verify required documentation exists**
  - When Project scope planning, check for files:
    - `docs/OVERVIEW.md`
    - `docs/ARCHITECTURE.md`
    - `docs/TECH-STACK.md`
    - `docs/DEPLOYMENT.md`
    - `docs/DEVELOPMENT.md`
    - `docs/FILES.md`
    - `docs/DEVELOPMENT-PLAN.md`
  - When Epic scope planning, check for files:
    - `docs/DEVELOPMENT-PLAN/{EPIC_ID} - {EPIC_NAME}.md`
  - When Story scope planning, check for files:
    - `docs/DEVELOPMENT-PLAN/{EPIC_ID}.{STORY_ID} - {STORY_NAME}.md`
  - When Task scope planning, check for files:
    - `docs/DEVELOPMENT-PLAN/{EPIC_ID}.{STORY_ID}.{TASK_ID} - {TASK_NAME}.md`

- **Handle documentation failures**
  - When any of the files are missing or incomplete:
    - **MUST** stop and exit immediately with error report

- **Complete phase**
  - Update "Phase X: Documentation Creation" task as completed
  - Transition to "Phase X: Validation & Handoff"


### Phase X: Validation & Handoff
Validates completeness and prepares development handoff

#### CRITICAL REQUIREMENTS
- **MUST** validate all deliverables
- **MUST** ensure specifications are complete
- **MUST** prepare clear handoff package

#### CRITICAL RESTRICTIONS
- **NEVER** handoff incomplete work
- **NEVER** skip validation
- **NEVER** proceed without success criteria

#### EXECUTION FLOW

- **Update phase tracking**
  - Update "Phase X: Validation and Handoff" task as in_progress

- **Build validation checklist**
  - Generate scope-specific validation checklist
  - Include requirements for deliverables, specifications, and documentation

- **Execute validation checks**
  - Validate each item in checklist
  - When any validation fails:
    - **MUST** stop and exit immediately with error report

- **Prepare handoff package**
  - Compile prioritized backlog items
  - Include technical specifications
  - Document success criteria
  - Define next steps for development

- **Complete phase**
  - Update "Phase X: Validation and Handoff" task as completed

- **Clean up planning tasks**
  - Remove all phase tasks from todo list
  - Log successful completion
  - Return success status
