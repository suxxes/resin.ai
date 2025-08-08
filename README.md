# Research Institute of Artificial Intelligence (ResIn.AI)

This project implements a sophisticated 4-agent orchestration system for complete epic implementation with progressive quality standards using Claude Code's custom slash commands.

## System Overview

**Project Type**: Claude Code Agent System
**Purpose**: Multi-agent workflow orchestration for software development with progressive quality standards

### Core Architecture:
- **Multi-Agent System**: Project Manager, Feature Lead, Dynamic Developer Discovery, Quality Assurance
- **Multi-Stage State Machine**: PM_BOOTSTRAP → FL_PLAN → DEV_IMPLEMENT → QUALITY_ASSURANCE_VALIDATE → FL_FINAL → PM_COMPLETE
- **Dynamic Agent Discovery**: Automatically discovers and selects appropriate developer agent based on agent descriptions and project tech stack
- **Progressive Quality Standards**: BASE → ENHANCED → MAXIMUM → STRATEGIC
- **Hierarchical Task Management**: Epic → Story → Task with unique identifiers (EEEE.SS.TT)

### Technical Stacks (Developer Agents):

#### General TypeScript Developer Agent:
- **Core**: TypeScript, JavaScript (framework-agnostic)
- **Adaptation**: Learns project tooling (build systems, testing, deployment)
- **Frameworks**: Adapts to React, Vue, Angular, Node.js, Express, etc.
- **Package Managers**: npm, yarn, pnpm (respects project choice)
- **Testing**: Adapts to Vitest, Jest, Mocha, Playwright, Cypress, etc.
- **Build Tools**: Webpack, Vite, ESBuild, Parcel, Rollup, etc.

#### Next.js Specialist Developer Agent:
- **Core**: Next.js, React, TypeScript (Next.js focused)
- **Backend**: Prisma, ZenStack for database operations
- **Validation**: Zod for schema validation
- **Monorepo**: Turbo for workspace management
- **State**: Zustand + TanStack React Query
- **Testing**: Vitest, React Testing Library, Playwright
- **i18n**: i18next, react-i18next

#### Swift Developer Agent:
- **Core**: Swift, SwiftUI, UIKit
- **Platform**: iOS, macOS, iPadOS, watchOS
- **Backend**: URLSession, Combine, async/await
- **Data**: Core Data, CloudKit, UserDefaults
- **Testing**: XCTest framework
- **Development**: Xcode, Swift Package Manager

---

# Commands Directory

This section contains Claude Code custom slash commands for development workflow orchestration and project management.

## Active Commands

### `/develop` (`develop.md`)
**Agentic State-Machine Orchestrator for complete epic implementation**

- **Mode**: Enters **Agentic State-Machine Orchestrator mode** - locked until user exit or completion
- **Purpose**: Orchestrates multi-agent, multi-stage state machine for epic → story → task implementation
- **Architecture**: PM_BOOTSTRAP → FL_PLAN → DEV_IMPLEMENT → QUALITY_ASSURANCE_VALIDATE → FL_FINAL → PM_COMPLETE
- **Progressive Quality**: BASE → ENHANCED → MAXIMUM → STRATEGIC standards
- **Mode Lock**: Prevents autonomous exits, phase skipping, and demonstration shortcuts
- **Usage**:
  ```bash
  /develop                # Enter orchestrator mode, auto-discover work
  /develop 0003          # Enter orchestrator mode for Epic 0003
  /develop 0003.02       # Enter orchestrator mode for Story 0003.02
  /develop 0003.02.01    # Enter orchestrator mode for Task 0003.02.01
  ```

### `/prime` (`prime.md`)
**Context loading command for comprehensive project understanding**

- **Purpose**: Prime Claude with project overview, structure, and development context
- **Features**: README analysis, file structure review, configuration understanding
- **Usage**: `/prime` - Load complete project context

### `/framework` (`framework.md`)
**Comprehensive technical architect assistant for new project creation**

- **Purpose**: Comprehensive technical architect assistant for designing and planning entirely new projects from the ground up
- **Features**: Requirements discovery, technology stack recommendations, architecture design, epic-level planning, implementation roadmap
- **Process**: Discovery → Technology Stack → Architecture Design → Documentation → Epic Planning → Progress Tracking Setup
- **Output**: Complete project blueprint with documentation structure and epic-based development plan
- **Usage**: `/framework` - Enter Framework Mode for greenfield project creation

### Utility Commands

#### `/ask` (`ask.md`)
- **Purpose**: AI-powered question answering and research
- **Usage**: `/ask [question]` - Get intelligent responses with web search capability

#### `/branch` (`branch.md`)
- **Purpose**: Git branch management and workflow operations
- **Usage**: `/branch [branch-name]` - Create and manage feature branches

#### `/commit` (`commit.md`)
- **Purpose**: Intelligent commit message generation and git operations
- **Usage**: `/commit [message]` - Stage changes and create commits

#### `/docs` (`docs.md`)
- **Purpose**: Documentation generation and maintenance
- **Usage**: `/docs` - Generate or update project documentation

## Command Architecture

### Agentic State-Machine Orchestrator (`/develop`)
The `/develop` command operates in **Agentic State-Machine Orchestrator mode**:
- **Mode Lock**: Claude locked in orchestrator mode until user exit or completion
- **Single Command**: Handles Epic → Story → Task hierarchy
- **Multi-Agent Quality Progression**: Project Manager → Feature Lead → Developer → Quality Assurance
- **Multi-Stage State Machine**: Complete workflow from planning to strategic completion
- **Progressive Quality Standards**: Each phase applies increasingly strict standards
- **Anti-Early-Exit**: Prevents autonomous phase skipping and demonstration shortcuts
- **Hierarchical Identifier Support**: Works with EPIC, STORY, or TASK identifiers
- **Conditional Bootstrapping**: Only creates missing files as needed
- **Complete Task Tree Maintenance**: Updates all hierarchy files

### Quality Standards Progression

1. **Developer (BASE)**: Standard technical implementation and testing
2. **Quality Assurance (ENHANCED)**: Through-the-roof comprehensive validation
3. **Feature Lead (MAXIMUM)**: Ruthless business validation
4. **Project Manager (STRATEGIC)**: Complete epic coherence validation

### File Hierarchy Management

Commands work with structured file hierarchy:
```
docs/DEVELOPMENT_PLAN_AND_PROGRESS/
├── EEEE - Epic Name.md                                 # Epic files
├── EEEE.SS - Epic Name - Story Name.md                 # Story files
└── EEEE.SS.TT - Epic Name - Story Name - Task Name.md  # Task files
```

## State Persistence

All commands maintain state in:
- **Main Progress**: `docs/DEVELOPMENT_PLAN_AND_PROGRESS.md` with agentic state tracking
- **Hierarchy Files**: Epic, Story, and Task files with completion status
- **Iteration Tracking**: Failure reasons and retry counts
- **Quality Documentation**: Standards applied at each phase
- **Time Stamps**: All state transitions across file hierarchy

---

# Agents Directory

This section documents the specialized sub-agents used by the `/develop` orchestrator command for complete epic implementation with progressive quality standards and intelligent tech stack detection.

## Multi-Agent Architecture

### Agent 1: Project Manager (`project-manager.md`)
- **Role**: Strategic planning and completion specialist
- **Phases**: PM_BOOTSTRAP, PM_COMPLETE
- **Quality Standards**: STRATEGIC oversight
- **Expertise**: Epic analysis, story breakdown, strategic validation
- **Responsibilities**:
  - Analyze epics and create story breakdowns
  - Complete epic implementation with strategic coherence validation
  - Portfolio alignment and resource utilization optimization

### Agent 2: Feature Lead (`feature-lead.md`)
- **Role**: Business task planning and validation specialist
- **Phases**: FL_PLAN, FL_FINAL
- **Quality Standards**: MAXIMUM business standards
- **Expertise**: Business planning, user experience validation, stakeholder acceptance
- **Responsibilities**:
  - Create task implementation plans for all stories
  - Final business validation with ruthless business standards
  - User journey validation and stakeholder acceptance

### Agent 3: Developer (Dynamic Discovery)
- **Role**: Dynamically discovered based on project tech stack and agent expertise
- **Phases**: DEV_IMPLEMENT (All project types)
- **Quality Standards**: BASE technical standards
- **Discovery Process**: 
  - Scans `agents/developer-*` files for available specialists
  - Matches agent descriptions against project technology requirements
  - Selects highest compatibility score agent
- **Current Available Specialists**:
  - **General TypeScript** (`developer-typescript.md`): Adapts to any TypeScript project by learning tooling
  - **Next.js Specialist** (`developer-nextjs.md`): Next.js/React full-stack web applications
  - **Swift Specialist** (`developer-swift.md`): Native app development specialist for Apple platforms
- **Extensible**: New developer agents automatically discovered when added to `agents/` directory

### Agent 4: Quality Assurance (`quality-assurance.md`)
- **Role**: Enhanced quality validation specialist
- **Phases**: QUALITY_ASSURANCE_VALIDATE
- **Quality Standards**: ENHANCED (through-the-roof) standards
- **Expertise**: Comprehensive testing, security validation, performance benchmarking
- **Responsibilities**:
  - Enhanced quality validation far exceeding Developer standards
  - Integration testing, security scanning, accessibility compliance
  - Performance benchmarking and regression testing

## Multi-Stage State Machine Flow

```
PM_BOOTSTRAP → FL_PLAN → DEV_IMPLEMENT → QUALITY_ASSURANCE_VALIDATE → FL_FINAL → PM_COMPLETE
   (Agent 1)    (Agent 2)    (Agent 3)           (Agent 4)            (Agent 2)   (Agent 1)
                    ↑           ↓  ↑                  ↓  ↑               ↓
                    └───────────┘  └──────────────────┘  └───────────────┘
                    (FL fails,     (QA fails,            (PM fails,
                     return to      return to             return to
                     FL_PLAN)       DEV_IMPLEMENT)        FL_FINAL)
```

## Progressive Quality Standards

Each agent applies increasingly strict quality standards:

1. **Developer (BASE)**: Standard implementation and testing
2. **Quality Assurance (ENHANCED)**: Comprehensive validation and testing
3. **Feature Lead (MAXIMUM)**: Business value and user experience validation
4. **Project Manager (STRATEGIC)**: Epic coherence and portfolio alignment

## Agent Specialization

### What Each Agent DOES Understand:
- **Project Manager**: Strategic planning, epic coherence, portfolio alignment
- **Feature Lead**: Business requirements, user experience, stakeholder validation
- **Developer**: Technical implementation, code architecture, testing frameworks
- **Quality Assurance**: Quality standards, testing methodologies, performance validation

### What Each Agent DOES NOT Understand:
- **Project Manager**: Technical implementation details, code specifics
- **Feature Lead**: Technical architecture, programming languages, development tools
- **Developer**: Business strategy, user experience, market considerations
- **Quality Assurance**: Business requirements, strategic planning, user workflows

## Agentic State-Machine Orchestrator Mode

When `/develop` is invoked, Claude enters **Agentic State-Machine Orchestrator mode** and remains locked in this mode until explicitly requested to exit by the user. This prevents autonomous mode switching and early exits.

### Mode Lock Features:
- **Continuous Orchestration**: Must complete all 6 phases or receive user intervention
- **No Autonomous Exits**: Cannot exit for demonstration or explanation purposes
- **Strict Phase Adherence**: Each agent must complete their phase fully
- **Mode Discipline**: No switching to tutorial, demo, or other modes

### Mode Lock Rules:
- **LOCKED MODE**: Claude enters Agentic State-Machine Orchestrator mode and cannot exit autonomously
- **NO MODE SWITCHING**: Cannot switch to demonstration, explanation, or tutorial modes
- **CONTINUOUS ORCHESTRATION**: Must complete all 6 phases or receive user intervention
- **NO PHASE SKIPPING**: Commands cannot skip phases for demonstration purposes
- **COMPLETE IMPLEMENTATION**: Each phase must finish fully before proceeding
- **STRICT RETURN CODES**: Only documented state transitions allowed
- **NO AUTONOMOUS DECISIONS**: Commands follow orchestrator control only

### Prohibited Behaviors:
- ❌ "Given the iterative nature... let me move forward to show the complete workflow"
- ❌ "This is a demonstration of orchestrator capabilities"
- ❌ Autonomous mode switching or early exits
- ❌ Phase skipping for any reason except documented failure states

## File Structure

Each agent file contains:
- **Metadata**: name, description, tools, color
- **Professional Role**: Expertise and limitations
- **Implementation Approach**: Phase-specific methodology
- **Quality Gates**: Standards and validation criteria
- **Handoff Protocol**: Inter-agent communication
- **Return Codes**: State transition signals

## Mode Exit Protocol

### Permitted Exits:
- ✅ **User explicitly requests exit**: "Exit orchestrator mode", "Stop develop"
- ✅ **Complete epic implementation**: All 6 phases successfully completed through PM_COMPLETE
- ✅ **Critical system failure**: Agent returns CRITICAL_FAILURE requiring user intervention

### Prohibited Autonomous Exits:
- ❌ **Demonstration purposes**: "Let me show the complete workflow"
- ❌ **Iterative reasoning**: "Given the iterative nature..."
- ❌ **Mode switching**: Switching to explanation, tutorial, or any other mode
- ❌ **Self-termination**: Any autonomous decision to end orchestration
- ❌ **Phase skipping**: Jumping ahead to demonstrate later phases

### Agent Behavioral Rules:
- Complete their phase fully before returning control
- Use only documented return codes
- Never skip phases or make autonomous workflow decisions
- Never transition early for "demonstration" purposes
- Focus solely on their specialized domain expertise
- Maintain mode lock throughout their execution

---

## Usage Patterns

### Development Workflow
```bash
/prime                              # Load project context
/develop 0003                       # Enter orchestrator mode for Epic 0003
# Claude now locked in orchestrator mode until completion or user exit
/commit "feat: epic 0003 complete"  # Commit after orchestrator completion
```

### Project Setup
```bash
/framework               # Enter Framework Mode for new project creation
# Complete greenfield project planning and architecture design
/develop 0001           # Begin implementation of first epic from framework plan
/commit "feat: initial project setup complete"
```

### Research and Planning
```bash
/ask "Best practices for Next.js authentication"
/prime                   # Refresh context with new information
/develop 0004            # Apply research to new epic
```

## Command Development

New commands should follow the established patterns:
- Clear purpose and scope definition
- Integration with file hierarchy system
- Proper state persistence and tracking
- Progressive quality standard enforcement
- Agentic State-Machine Orchestrator mode compliance
- Anti-early-exit behavioral controls with mode lock enforcement
