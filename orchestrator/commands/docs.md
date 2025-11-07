# Docs - Create comprehensive project documentation

<!-- Updated: 2025-10-19 10:02:16 UTC -->

Create comprehensive LLM-optimized technical documentation for the codebase. This command complements the plan command by focusing on technical implementation details while plan focuses on project planning and specifications.

## CRITICAL REQUIREMENTS
- **MUST** follow template requirements from TEMPLATE-REQUIREMENTS
- **MUST** create comprehensive LLM-optimized documentation
- **MUST** include concrete file references throughout
- **MUST** eliminate all duplication across files
- **MUST** update Phases numbering order when new Phases list or ordering changes
- **MUST** use ordered numbering with the zero-padded value to the maximum length among the related values with minimum length of 2
- **MUST** keep overview sections to 2-3 paragraphs maximum
- **MUST** include key files and examples with concrete references for each topic
- **MUST** provide common workflows with practical guidance and file locations
- **MUST** create reference sections with quick lookup tables and file paths
- **MUST** use token-efficient writing without redundant explanations
- **MUST** include actual code examples from the codebase, not generic examples
- **MUST** focus on what LLMs need to work with code

## CRITICAL RESTRICTIONS
- **NEVER** duplicate information across files
- **NEVER** create generic examples - use actual code from codebase
- **NEVER** skip file reference verification
- **NEVER** create verbose explanations or redundant content
- **NEVER** create `docs/DEVELOPMENT-PLAN.md` (reserved for plan command)
- **NEVER** exceed 2-3 paragraphs for overview sections
- **NEVER** use placeholder code examples

## PROCESS DEFINITION

### Phase X: Initialize Tasks
Create and track all documentation tasks

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
  - Create "Phase X: Project Discovery" task as pending
  - Create "Phase X: Create ARCHITECTURE.md" task as pending
  - Create "Phase X: Create TECH-STACK.md" task as pending
  - Create "Phase X: Create DEPLOYMENT.md" task as pending
  - Create "Phase X: Create DEVELOPMENT.md" task as pending
  - Create "Phase X: Create FILES.md" task as pending
  - Create "Phase X: Create OVERVIEW.md" task as pending
  - Create "Phase X: Create README.md" task as pending
  - Create "Phase X: Validation & Cleanup" task as pending

- **Complete phase**
  - Update "Phase X: Initialize Tasks" task as completed
  - Transition to "Phase X: Project Discovery"

### Phase X: Project Discovery
Discover project structure and technology stack

#### CRITICAL REQUIREMENTS
- **MUST** identify project structure
- **MUST** detect technology stack
- **MUST** find key entry points

#### CRITICAL RESTRICTIONS
- **NEVER** assume project conventions
- **NEVER** skip technology detection
- **NEVER** proceed without understanding structure

#### EXECUTION FLOW

- **Update phase tracking**
  - Update "Phase X: Project Discovery" task as in_progress

- **Analyze project structure**
  - Examine directory layout and organization
  - Identify source code locations
  - Find configuration files
  - Detect build system files
  - Locate test directories

- **Detect technology stack**
  - Identify programming languages
  - Detect frameworks and libraries
  - Find package management files
  - Discover build tools
  - Identify testing frameworks

- **Extract key information**
  - Main entry points
  - Core configuration files
  - Build commands
  - Test commands
  - Deployment scripts

- **Complete phase**
  - Update "Phase X: Project Discovery" task as completed
  - Transition to "Phase X: Create ARCHITECTURE.md"

### Phase X: Create ARCHITECTURE.md
Create system architecture documentation

#### CRITICAL REQUIREMENTS
- **MUST** check if `docs/ARCHITECTURE.md` exists before creating
- **MUST** document system organization
- **MUST** include component mappings

#### CRITICAL RESTRICTIONS
- **NEVER** overwrite existing file without explicit user approval
- **NEVER** create without file references
- **NEVER** skip data flow documentation
- **NEVER** omit timestamp header

#### EXECUTION FLOW

- **Update phase tracking**
  - Update "Phase X: Create ARCHITECTURE.md" task as in_progress

- **Evaluate file existence**
  - When `docs/ARCHITECTURE.md` already exists:
    - Skip creation to avoid overwriting
    - Mark phase as completed
    - Proceed to next phase
  - When `docs/ARCHITECTURE.md` does not exist:
    - Proceed with documentation creation

- **Create documentation**
  - **MUST** read and use `plugin:orchestrator:resources://TEMPLATE/DOCUMENTATION/ARCHITECTURE.md` as a template
  - **MUST** read and follow requirements from `plugin:orchestrator:resources://CORE/TEMPLATE-REQUIREMENTS.md`
  - **MUST** preserve template organization
  - Document high-level system organization
  - Map major components with source file locations
  - List core headers and implementations
  - Document data flow with function/file references
  - Add timestamp header

- **Complete phase**
  - Update "Phase X: Create ARCHITECTURE.md" task as completed
  - Transition to "Phase X: Create TECH-STACK.md"

### Phase X: Create TECH-STACK.md
Create technology stack documentation

#### CRITICAL REQUIREMENTS
- **MUST** check if `docs/TECH-STACK.md` exists before creating
- **MUST** inventory all technologies
- **MUST** include versions and dependencies

#### CRITICAL RESTRICTIONS
- **NEVER** overwrite existing file without explicit user request
- **NEVER** skip dependency analysis
- **NEVER** omit development tools
- **NEVER** forget timestamp header

#### EXECUTION FLOW

- **Update phase tracking**
  - Update "Phase X: Create TECH-STACK.md" task as in_progress

- **Evaluate file existence**
  - When `docs/TECH-STACK.md` already exists:
    - Skip creation to avoid overwriting
    - Mark phase as completed
    - Proceed to next phase
  - When `docs/TECH-STACK.md` does not exist:
    - Proceed with documentation creation

- **Create documentation**
  - **MUST** read and use `plugin:orchestrator:resources://TEMPLATE/DOCUMENTATION/TECH-STACK.md` as a template
  - **MUST** read and follow requirements from `plugin:orchestrator:resources://CORE/TEMPLATE-REQUIREMENTS.md`
  - **MUST** preserve template organization
  - Document complete technology inventory
  - List languages, frameworks, runtime environments
  - Document package management and libraries
  - Include build systems and testing frameworks
  - Add deployment platforms and services
  - Add timestamp header

- **Complete phase**
  - Update "Phase X: Create TECH-STACK.md" task as completed
  - Transition to "Phase X: Create DEPLOYMENT.md"

### Phase X: Create DEPLOYMENT.md
Create build and deployment documentation

#### CRITICAL REQUIREMENTS
- **MUST** check if `docs/DEPLOYMENT.md` exists before creating
- **MUST** document build system
- **MUST** document deployment process

#### CRITICAL RESTRICTIONS
- **NEVER** overwrite existing file without explicit user approval
- **NEVER** skip platform-specific details
- **NEVER** omit script references
- **NEVER** forget timestamp header

#### EXECUTION FLOW

- **Update phase tracking**
  - Update "Phase X: Create DEPLOYMENT.md" task as in_progress

- **Evaluate file existence**
  - When `docs/DEPLOYMENT.md` already exists:
    - Skip creation to avoid overwriting
    - Mark phase as completed
    - Proceed to next phase
  - When `docs/DEPLOYMENT.md` does not exist:
    - Proceed with documentation creation

- **Create documentation**
  - **MUST** read and use `plugin:orchestrator:resources://TEMPLATE/DOCUMENTATION/DEPLOYMENT.md` as a template
  - **MUST** read and follow requirements from `plugin:orchestrator:resources://CORE/TEMPLATE-REQUIREMENTS.md`
  - **MUST** preserve template organization
  - Document build system and deployment pipeline
  - Include build configuration and workflows
  - Add platform-specific requirements
  - Document packaging and distribution
  - Include deployment scripts and configurations
  - Add timestamp header

- **Complete phase**
  - Update "Phase X: Create DEPLOYMENT.md" task as completed
  - Transition to "Phase X: Create DEVELOPMENT.md"

### Phase X: Create DEVELOPMENT.md
Create development and testing documentation

#### CRITICAL REQUIREMENTS
- **MUST** check if `docs/DEVELOPMENT.md` exists before creating
- **MUST** document development environment
- **MUST** document testing approach

#### CRITICAL RESTRICTIONS
- **NEVER** overwrite existing file without explicit user request
- **NEVER** skip code conventions
- **NEVER** omit test examples
- **NEVER** forget timestamp header

#### EXECUTION FLOW

- **Update phase tracking**
  - Update "Phase X: Create DEVELOPMENT.md" task as in_progress

- **Evaluate file existence**
  - When `docs/DEVELOPMENT.md` already exists:
    - Skip creation to avoid overwriting
    - Mark phase as completed
    - Proceed to next phase
  - When `docs/DEVELOPMENT.md` does not exist:
    - Proceed with documentation creation

- **Create documentation**
  - **MUST** read and use `plugin:orchestrator:resources://TEMPLATE/DOCUMENTATION/DEVELOPMENT.md` as a template
  - **MUST** read and follow requirements from `plugin:orchestrator:resources://CORE/TEMPLATE-REQUIREMENTS.md`
  - **MUST** preserve template organization
  - Document development environment and testing approach
  - Include code conventions from codebase
  - Add development workflows and patterns
  - Document test types and organization
  - Include test commands and examples
  - Add timestamp header

- **Complete phase**
  - Update "Phase X: Create DEVELOPMENT.md" task as completed
  - Transition to "Phase X: Create FILES.md"

### Phase X: Create FILES.md
Create file catalog documentation

#### CRITICAL REQUIREMENTS
- **MUST** check if `docs/FILES.md` exists before creating
- **MUST** catalog all significant files
- **MUST** organize by function

#### CRITICAL RESTRICTIONS
- **NEVER** overwrite existing file without explicit user approval
- **NEVER** create verbose descriptions
- **NEVER** skip dependency mappings
- **NEVER** forget timestamp header

#### EXECUTION FLOW

- **Update phase tracking**
  - Update "Phase X: Create FILES.md" task as in_progress

- **Evaluate file existence**
  - When `docs/FILES.md` already exists:
    - Skip creation to avoid overwriting
    - Mark phase as completed
    - Proceed to next phase
  - When `docs/FILES.md` does not exist:
    - Proceed with documentation creation

- **Create documentation**
  - **MUST** read and use `plugin:orchestrator:resources://TEMPLATE/DOCUMENTATION/FILES.md` as a template
  - **MUST** read and follow requirements from `plugin:orchestrator:resources://CORE/TEMPLATE-REQUIREMENTS.md`
  - **MUST** preserve template organization
  - Discover all source files, configs, and build files
  - Organize files into logical categories
  - Add brief one-line descriptions per file
  - Highlight main entry points
  - Document file dependencies
  - Add timestamp header

- **Complete phase**
  - Update "Phase X: Create FILES.md" task as completed
  - Transition to "Phase X: Create OVERVIEW.md"

### Phase X: Create OVERVIEW.md
Create project overview documentation

#### CRITICAL REQUIREMENTS
- **MUST** check if `docs/OVERVIEW.md` exists before creating
- **MUST** include concrete file references

#### CRITICAL RESTRICTIONS
- **NEVER** overwrite existing file without explicit user request
- **NEVER** create generic content
- **NEVER** skip file references
- **NEVER** omit timestamp header

#### EXECUTION FLOW

- **Update phase tracking**
  - Update "Phase X: Create OVERVIEW.md" task as in_progress

- **Evaluate file existence**
  - When `docs/OVERVIEW.md` already exists:
    - Skip creation to avoid overwriting
    - Mark phase as completed
    - Proceed to next phase
  - When `docs/OVERVIEW.md` does not exist:
    - Proceed with documentation creation

- **Create documentation**
  - **MUST** read and use `plugin:orchestrator:resources://TEMPLATE/DOCUMENTATION/OVERVIEW.md` as a template
  - **MUST** read and follow requirements from `plugin:orchestrator:resources://CORE/TEMPLATE-REQUIREMENTS.md`
  - **MUST** preserve template organization
  - Include project purpose and key value proposition
  - Add main entry points and configuration files
  - Include technology stack with file examples
  - Add platform support with specific locations
  - Add timestamp header

- **Complete phase**
  - Update "Phase X: Create OVERVIEW.md" task as completed
  - Transition to "Phase X: Create README.md"

### Phase X: Create README.md
Synthesize documentation into README

#### CRITICAL REQUIREMENTS
- **MUST** check if `README.md` exists before creating
- **MUST** keep under 50 lines
- **MUST** include documentation index

#### CRITICAL RESTRICTIONS
- **NEVER** overwrite existing file without explicit user request
- **NEVER** duplicate documentation content
- **NEVER** exceed line limit
- **NEVER** omit quick start commands

#### EXECUTION FLOW

- **Update phase tracking**
  - Update "Phase X: Create README.md" task as in_progress

- **Evaluate file existence**
  - When `README.md` already exists:
    - Skip creation to avoid overwriting
    - Mark phase as completed
    - Proceed to next phase
  - When `README.md` does not exist:
    - Proceed with documentation creation

- **Create documentation**
  - **MUST** read and use `plugin:orchestrator:resources://TEMPLATE/DOCUMENTATION/README.md` as a template
  - **MUST** read and follow requirements from `plugin:orchestrator:resources://CORE/TEMPLATE-REQUIREMENTS.md`
  - **MUST** preserve template organization
  - Read all `docs/*.md` files for reference
  - Write concise project description (2-3 sentences)
  - Add key entry points and configuration files
  - Include quick start commands
  - Create comprehensive documentation index
  - Add timestamp header

- **Complete phase**
  - Update "Phase X: Create README.md" task as completed
  - Transition to "Phase X: Validation & Cleanup"

### Phase X: Validation & Cleanup
Validate completeness and remove duplication

#### CRITICAL REQUIREMENTS
- **MUST** validate all documentation
- **MUST** remove duplication
- **MUST** verify accuracy

#### CRITICAL RESTRICTIONS
- **NEVER** leave duplicated content
- **NEVER** skip validation
- **NEVER** leave broken references

#### EXECUTION FLOW

- **Update phase tracking**
  - Update "Phase X: Validation & Cleanup" task as in_progress

- **Validate documentation**
  - Verify all required files exist
  - Check timestamp headers
  - Validate file references accuracy
  - Confirm no duplication
  - Verify cross-references work

- **Remove duplication**
  - Scan all files for duplicated information
  - Consolidate any repeated content
  - Update cross-references as needed

- **Complete phase**
  - Update "Phase X: Validation & Cleanup" task as completed

## DOCUMENTATION STRUCTURE

### Core Documentation

**Project Overview** (`docs/OVERVIEW.md`):
- What the project is, core purpose, key value proposition
- Main entry points and core configuration files
- Technology stack with specific file examples
- Platform support with platform-specific file locations

**Architecture** (`docs/ARCHITECTURE.md`):
- High-level system organization
- Major components with their source file locations
- Core headers and implementations with descriptions
- Data flow with specific function/file references

**Technology Stack** (`docs/TECH-STACK.md`):
- Complete technology inventory
- Languages, frameworks, and runtime environments
- Package management and third-party libraries
- Build systems, testing frameworks, and toolchain
- Deployment platforms and services

### Technical Documentation

**Build & Deployment** (`docs/DEPLOYMENT.md`):
- Build system and deployment pipeline
- Build configuration, workflows, and commands
- Platform-specific requirements and paths
- Packaging, distribution, and deployment scripts
- Combined build and deployment reference

**Development & Testing** (`docs/DEVELOPMENT.md`):
- Development environment and testing approach
- Code conventions and patterns from codebase
- Development workflows and test organization
- Test types, commands, and expected outputs
- File organization and naming conventions

**Files Catalog** (`docs/FILES.md`):
- Comprehensive file catalog with descriptions
- Core source files and their purposes
- Platform-specific implementations
- Build configuration and helper modules
- File organization patterns and dependencies

## FORMAT REQUIREMENTS

### LLM-OPTIMIZED FORMAT
- **Token efficient**: Avoid redundant explanations, focus on essential information
- **Concrete file references**: Always include specific file paths, line numbers when possible
- **Flexible formatting**: Use subsections, code blocks, examples instead of rigid step-by-step instructions
- **Pattern examples**: Show actual code from the codebase, not generic examples

### NO DUPLICATION
- Each piece of information appears in EXACTLY ONE file
- Build and deployment information only in BUILD-DEPLOYMENT.md
- Development and testing information only in DEVELOPMENT-TESTING.md
- Cross-references using: "See [docs/FILENAME.md](<./docs/FILENAME.md>)"
