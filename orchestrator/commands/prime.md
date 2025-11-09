# Prime

<!-- Updated: 2025-09-30 10:55:00 UTC -->

Prime Claude with comprehensive project understanding and generate detailed project status report.


## CRITICAL REQUIREMENTS
- **MUST** load project context systematically
- **MUST** generate comprehensive status report
- **MUST** identify current progress and next steps
- **MUST** execute algorithms exactly as defined and in defined order
- **MUST** follow and respect all requirements and restrictions
- **MUST** be concise and report only when and only in the way you've been instructed.
- **MUST** use ordered numbering for Phases instead of X
- **MUST** update Phases numbering order when new Phases list or ordering changes

## CRITICAL RESTRICTIONS
- **NEVER** skip `README.md` or `CLAUDE.md` if they exist
- **NEVER** make assumptions about project state
- **NEVER** omit `git status` review
- **NEVER** create incomplete status reports
- **NEVER** report any information between actions and phases unless instructed to do so


## PROCESS DEFINITION


### Phase X: Initialize Tasks
Initialize context loading tasks

#### CRITICAL REQUIREMENTS
- **MUST** create all phase tracking tasks
- **MUST** use TodoWrite for task management
- **MUST** proceed through all phases

#### CRITICAL RESTRICTIONS
- **NEVER** skip task initialization
- **NEVER** proceed without task tracking
- **NEVER** create phases out of order

#### EXECUTION FLOW

- **Initialize phase tracking**
  - Create "Phase X: Initialize Tasks" task as in_progress
  - Create "Phase X: Load Documentation" task as pending
  - Create "Phase X: Analyze Repository" task as pending
  - Create "Phase X: Review Configuration" task as pending
  - Create "Phase X: Assess Progress" task as pending
  - Create "Phase X: Generate Report" task as pending

- **Complete phase**
  - Update "Phase X: Initialize Tasks" task as completed
  - Transition to "Phase X: Load Documentation"


### Phase X: Load Documentation
Load project documentation and guidelines

#### CRITICAL REQUIREMENTS
- **MUST** read `README.md` if exists
- **MUST** read `CLAUDE.md` if exists
- **MUST** identify project purpose

#### CRITICAL RESTRICTIONS
- **NEVER** skip existing documentation
- **NEVER** ignore AI guidelines
- **NEVER** make assumptions about missing docs

#### EXECUTION FLOW

- **Update phase tracking**
  - Update "Phase X: Load Documentation" task as in_progress

- **Load project overview**
  - Read `README.md` file if present
  - Identify project type and purpose
  - Note key technologies and dependencies

- **Load AI guidelines**
  - Read `CLAUDE.md` file if present
  - Load project-specific AI instructions
  - Note coding standards and preferences

- **Complete phase**
  - Update "Phase X: Load Documentation" task as completed
  - Transition to "Phase X: Analyze Repository"


### Phase X: Analyze Repository
Analyze repository structure and conventions

#### CRITICAL REQUIREMENTS
- **MUST** examine project structure
- **MUST** identify naming conventions
- **MUST** understand directory organization

#### CRITICAL RESTRICTIONS
- **NEVER** make assumptions about structure
- **NEVER** skip file analysis
- **NEVER** ignore patterns

#### EXECUTION FLOW

- **Update phase tracking**
  - Update "Phase X: Analyze Repository" task as in_progress

- **Examine structure**
  - Run: `git ls-files | head -50` for initial structure
  - Identify main directories and their purposes
  - Note naming conventions
  - Detect file organization patterns

- **Analyze architecture**
  - Identify project type (web app, CLI, library, etc.)
  - Detect architecture patterns
  - Note module organization
  - Understand separation of concerns

- **Complete phase**
  - Update "Phase X: Analyze Repository" task as completed
  - Transition to "Phase X: Review Configuration"


### Phase X: Review Configuration
Review project configuration and environment

#### CRITICAL REQUIREMENTS
- **MUST** examine package management
- **MUST** review build configuration
- **MUST** identify development tools

#### CRITICAL RESTRICTIONS
- **NEVER** skip configuration files
- **NEVER** ignore environment setup
- **NEVER** overlook dependencies

#### EXECUTION FLOW

- **Update phase tracking**
  - Update "Phase X: Review Configuration" task as in_progress

- **Package management**
  - Check `package.json`, `Cargo.toml`, `pyproject.toml`, etc.
  - Note dependencies and versions
  - Identify scripts and commands

- **Build and tooling**
  - Review build configuration
  - Identify test framework
  - Note CI/CD configuration
  - Check linting and formatting tools

- **Environment setup**
  - Check environment variables
  - Review deployment configuration
  - Note database or service connections

- **Complete phase**
  - Update "Phase X: Review Configuration" task as completed
  - Transition to "Phase X: Assess Progress"


### Phase X: Assess Progress
Assess current development progress

#### CRITICAL REQUIREMENTS
- **MUST** check git status and branch
- **MUST** review recent commits
- **MUST** identify current work

#### CRITICAL RESTRICTIONS
- **NEVER** skip git analysis
- **NEVER** ignore work in progress
- **NEVER** overlook test coverage

#### EXECUTION FLOW

- **Update phase tracking**
  - Update "Phase X: Assess Progress" task as in_progress

- **Git status review**
  - Check current branch
  - Run `git status`
  - Review recent commits
  - Identify latest achievements

- **Progress analysis**
  - Find documentation for current work
  - Identify completed functionalities
  - Review recent milestones
  - Analyze test coverage if available
  - Count test files and test cases

- **Next steps identification**
  - Determine work in progress
  - Identify next implementation target
  - Note any blockers or issues

- **Complete phase**
  - Update "Phase X: Assess Progress" task as completed
  - Transition to "Phase X: Generate Report"


### Phase X: Generate Report
Generate comprehensive project status report

#### CRITICAL REQUIREMENTS
- **MUST** include all discovered information
- **MUST** provide actionable status

#### CRITICAL RESTRICTIONS
- **NEVER** use placeholder values
- **NEVER** skip required sections
- **NEVER** provide incomplete information

#### EXECUTION FLOW

- **Update phase tracking**
  - Update "Phase X: Generate Report" task as in_progress

- **Generate status report**
  - **MUST** read and use `plugin:orchestrator:resources://TEMPLATE/DOCUMENTATION/REPORT/PROJECT-OVERVIEW.md` as a template
  - **MUST** read and follow requirements from `plugin:orchestrator:resources://CORE/TEMPLATE-REQUIREMENTS.md`
  - **MUST** preserve template organization
  - **MUST** preserve template organization
  - Include comprehensive project summary
  - Detail current status and progress
  - List technology stack components
  - Highlight architecture features
  - Document delivered features
  - Provide development context
  - List key development commands

- **Finalize report**
  - Add context-specific message about readiness to assist
  - Ensure all sections are complete
  - Verify accuracy of information

- **Complete phase**
  - Update "Phase X: Generate Report" task as completed
  - Present comprehensive project status report
