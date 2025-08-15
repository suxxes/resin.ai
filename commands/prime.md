# Context Prime

Prime Claude with comprehensive project understanding and generate detailed project status report.

## Standard Context Loading:
1. Read README.md for project overview
2. Read CLAUDE.md for AI-specific instructions
3. List project files excluding ignored paths
4. Review key configuration files
5. Understand project structure and conventions
6. **Generate Comprehensive Project Status Report**

## Steps:
1. **Project Overview**:
   - Read README.md
   - Identify project type and purpose
   - Note key technologies and dependencies

2. **AI Guidelines**:
   - Read CLAUDE.md if present
   - Load project-specific AI instructions
   - Note coding standards and preferences

3. **Repository Structure**:
   - Run: `git ls-files | head -50` for initial structure
   - Identify main directories and their purposes
   - Note naming conventions

4. **Configuration Review**:
   - Package manager files (package.json, Cargo.toml, etc.)
   - Build configuration
   - Environment setup

5. **Development Context**:
   - Identify test framework
   - Note CI/CD configuration
   - Review contribution guidelines

6. **Epic and Progress Analysis**:
   - Check `docs/DEVELOPMENT_PLAN_AND_PROGRESS.md` for epic status
   - Identify current epic and completed epics
   - Review recent achievements and milestones
   - Analyze test coverage and quality metrics

7. **Git Status Review**:
   - Check current branch and git status
   - Review recent commits and progress
   - Identify latest achievements

## Advanced Options:
- Load specific subsystem context
- Focus on particular technology stack
- Include recent commit history
- Load custom command definitions

## Output Template:
Generate comprehensive project status report using this template:

```
Claude Context Primed - [PROJECT NAME] Project Overview

**Project Summary**

[PROJECT DESCRIPTION] - brief description of what the project does
and its key value proposition. Currently on Epic [CURRENT EPIC NUMBER]
([CURRENT EPIC NAME]) after successfully completing [COMPLETED EPICS SUMMARY].

**Current Status**

- Branch: [CURRENT BRANCH NAME]
- Epic Progress: [CURRENT EPIC] 🚀 [CURRENT_EPIC_STATUS], [COMPLETED EPICS] ✅ COMPLETED
- Status Progression: Epic: [EPIC_STATUS] | Story: [STORY_STATUS] | Task: [TASK_STATUS]
- Latest Achievement: [RECENT MAJOR ACCOMPLISHMENT]
- Test Coverage: [TEST COUNT] comprehensive tests with [COVERAGE DESCRIPTION]

**Technology Stack**

- Framework: [PRIMARY FRAMEWORK + VERSIONS]
- Database: [DATABASE + ORM + KEY FEATURES]
- Testing: [TEST FRAMEWORK + ENVIRONMENT + SPECIAL FEATURES]
- Code Quality: [LINTING/FORMATTING TOOLS]
- Styling: [UI FRAMEWORKS + COMPONENT LIBRARIES]
- Authentication: [AUTH METHOD + FEATURES]

**Architecture Highlights**

- [KEY ARCHITECTURAL FEATURE 1]
- [KEY ARCHITECTURAL FEATURE 2]
- [KEY ARCHITECTURAL FEATURE …]
- [PERFORMANCE CHARACTERISTICS]
- [SECURITY FEATURES]
- [SPECIAL TECHNICAL ACHIEVEMENTS]

**Development Commands**

[COMMAND 1]              # [DESCRIPTION]
[COMMAND 2]              # [DESCRIPTION]
[COMMAND …]              # [DESCRIPTION]

**Key Features Delivered**

- [MAJOR FEATURE 1] ([SUB-FEATURES])
- [MAJOR FEATURE 2] ([SUB-FEATURES])
- [MAJOR FEATURE …] ([SUB-FEATURES])

**Development Context**

- [DEVELOPMENT APPROACH/METHODOLOGY]
- [KEY DESIGN PRINCIPLES]
- [MONITORING/PERFORMANCE APPROACH]
- [COMPLETION STANDARDS]
- [DOCUMENTATION APPROACH]

Ready to assist with any development tasks on this [PROJECT CHARACTERISTICS] platform!
```

## Report Generation Requirements:
- **Dynamic Content**: Replace all bracketed placeholders with actual project data
- **Epic Analysis**: Parse development progress files for accurate epic status
- **Technology Detection**: Scan package.json/dependencies for accurate tech stack
- **Git Integration**: Use git commands to determine current branch and recent progress
- **Test Analysis**: Count test files and analyze test configuration
- **Command Discovery**: Extract npm/yarn scripts and key development commands
- **Architecture Assessment**: Identify key architectural patterns from codebase structure
- **Status Progression Analysis**: Determine current epic/story/task status progression using enhanced status system:
  - Epic: `NOT_STARTED` → `IN_PROGRESS (PLANNING)` → `READY_FOR_DEVELOPMENT` → `IN_DEVELOPMENT` → `COMPLETED`
  - Story: `NOT_STARTED` → `IN_PROGRESS (PLANNING)` → `READY_FOR_DEVELOPMENT` → `IN_DEVELOPMENT` → `COMPLETED`
  - Task: `NOT_STARTED (PENDING)` → `IN_PROGRESS` → `COMPLETED`

## Completion Criteria:
Establish clear understanding of:
- Project goals and constraints
- Technical architecture
- Development workflow
- Collaboration parameters
- **Current progress and achievements**
- **Immediate development context**
