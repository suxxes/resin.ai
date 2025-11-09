# Resin.ai Orchestrator

<!-- Updated: 2025-11-09 03:18:32 UTC -->

An autonomous multi-agent orchestration system for software development using Claude Code's plugin architecture. Built on state machine orchestration with deterministic execution, hierarchical planning, and specialized AI agents.

## Installation

### Prerequisites

**Required:**
- **tmux** - Session management and monitoring
  ```bash
  # macOS
  brew install tmux

  # Ubuntu/Debian
  sudo apt-get install tmux

  # Fedora/RHEL
  sudo dnf install tmux
  ```

**Automatically Available:**
- **Claude Code** - You're already using it
- **Python 3.10+** - Built into macOS/Linux
- **Git** - Pre-installed on most systems

### Install Plugin

```bash
# Add marketplace and install plugin (one command)
/plugin marketplace add suxxes/resin.ai && /plugin install orchestrator@resin-ai
```

That's it! The orchestrator is ready to use.

## System Overview

**Project Type**: Claude Code Plugin System
**Version**: 2.0.0
**Purpose**: Autonomous orchestration of complete software development lifecycle through specialized AI agents

### Core Architecture

- **Plugin-Based System**: Seamlessly integrated into Claude Code IDE via marketplace
- **MCP Server**: Zero-dependency Python implementation using Model Context Protocol
- **State Machine Orchestration**: Deterministic, repeatable execution through structured phases
- **Specialized AI Agents**: 9 domain-specific agents with hierarchical expertise
- **Resource-Driven**: All knowledge stored as structured Markdown (48 resource files)
- **Hierarchical Planning**: Project → Epic → Story → Task structure with enriched context

## Technology Stack

### Core Technologies
- **Python 3.10+**: MCP server implementation (zero external dependencies)
- **Model Context Protocol (MCP)**: JSON-RPC 2.0 over stdio
- **Markdown**: Knowledge base and documentation format
- **JSON Schema**: Tool parameter validation
- **Git**: Integrated version control workflow

### Architecture Pattern
- **Plugin Architecture**: Claude Code IDE marketplace integration
- **State Machine Design**: Deterministic phase transitions with return codes
- **Agent Delegation**: Hierarchical agent coordination
- **Template System**: Standardized output formats

## Directory Structure

```
orchestrator/
├── .claude-plugin/
│   └── plugin.json              # Plugin metadata (v2.0.0)
├── .mcp.json                    # MCP server configuration
├── resources.py                 # MCP server implementation (Python)
├── agents/                      # AI agent definitions (9 agents)
│   ├── product-manager.md       # Strategic project planning
│   ├── project-manager.md       # Epic-to-story breakdown
│   ├── feature-manager.md       # Story-to-task breakdown
│   ├── developer-python.md      # Python implementation specialist
│   ├── developer-typescript.md  # TypeScript/JavaScript specialist
│   ├── developer-nextjs.md      # Next.js full-stack specialist
│   ├── developer-swift.md       # Swift/SwiftUI specialist
│   └── quality-assurance.md     # Enhanced QA validation
├── commands/                    # CLI orchestrators (4 commands)
│   ├── plan.md                  # Planning state machine
│   ├── work.md                  # Implementation state machine
│   ├── dryrun.md                # Planning preview (no execution)
│   └── docs.md                  # Documentation generation
├── resources/                   # Markdown knowledge base (48 files)
│   ├── CORE/                    # Core requirements (5 files)
│   ├── STATE-MACHINE/           # State definitions (14 files)
│   ├── AGENT/                   # Agent phases (8+ directories)
│   └── TEMPLATE/                # Output templates (20+ files)
└── skills/                      # Custom skills (extensible)
```

## Key Features

### 1. Autonomous Multi-Agent Orchestration

Coordinates specialized AI agents through deterministic state machines where each agent has specific expertise:

- **Product Manager**: Strategic planning, architecture, technology stack selection
- **Project Manager**: Epic breakdown into stories with prioritization
- **Feature Manager**: Story breakdown into tasks with technical specifications
- **Developer Specialists**: Language-specific TDD implementation (Python, TypeScript, Next.js, Swift)
- **Quality Assurance**: Enhanced validation with 95%+ test coverage requirements

### 2. Hierarchical Planning System

Auto-detects planning scope and creates complete development plans:

```
Project Level → Epic Level → Story Level → Task Level
```

**Numbering Format**: `XXXX.YY.ZZ` (Epic.Story.Task)
- Epic: `0001`
- Story: `0001.01`
- Task: `0001.01.01`

**Generated Documentation**:
```
docs/
├── OVERVIEW.md                  # Project vision and goals
├── ARCHITECTURE.md              # System architecture
├── TECH-STACK.md                # Technology decisions
├── DEPLOYMENT.md                # Deployment strategy
├── DEVELOPMENT.md               # Development guidelines
├── FILES.md                     # File organization
├── DEVELOPMENT-PLAN.md          # Master plan with all epics/stories/tasks
└── DEVELOPMENT-PLAN/
    ├── 0001 - Epic Name.md
    ├── 0001.01 - Epic - Story.md
    └── 0001.01.01 - Epic - Story - Task.md
```

### 3. State Machine Execution

**Planning State Machine** (`/orchestrator:plan`):
```
PLAN_INIT → PLAN_LOOP → PLAN_QUIZ → PLAN_WORK → PLAN_DONE
```

**Implementation State Machine** (`/orchestrator:work`):
```
EPIC_LOOP → STORY_LOOP → TASK_LOOP
  ├── INIT: Initialize and prepare
  ├── WORK: Execute implementation
  ├── TEST: Validate and verify
  └── DONE: Complete and transition
```

**State Transitions**: Controlled by return codes (CONTINUE, EXIT, FAILURE)

### 4. Test-Driven Development (TDD) Enforcement

Developer agents follow strict TDD methodology with 11 phases:

1. Initialize Tasks
2. Requirements Analysis
3. Project Discovery
4. Test Design
5. Test Implementation
6. Code Implementation
7. Test Verification
8. Documentation
9. Validation & Handoff

### 5. Requirements Enrichment

Prevents re-asking questions through enriched context:

- **Questionnaire-based discovery** at each planning level
- **Context preservation** through hierarchical delegation
- **Parent context inheritance** (Story inherits Epic context, Task inherits Story context)
- **Scope-specific questions** only

### 6. Enhanced Quality Assurance

Through-the-roof quality standards:

- **95% minimum test coverage**
- **Multiple validation layers**: Unit, integration, E2E
- **Security vulnerability scanning**
- **Performance benchmarking**
- **Regression validation**
- **Zero tolerance for failures**: Returns to development on any test failure

### 7. Documentation Automation

Template-driven documentation generation:

- **LLM-optimized technical writing**
- **Eliminates duplication** across documentation files
- **Concrete code examples** with file references
- **Automatic updates** during implementation

### 8. MCP Server Implementation

Two zero-dependency MCP servers power the orchestrator:

**Resources Server** (`resources.py`):
- **JSON-RPC 2.0 protocol** over stdio
- **Single tool**: `read` for accessing Markdown resources
- **URI scheme**: `plugin:orchestrator:resources://path/to/file.md`
- **Security**: Directory traversal prevention, Markdown-only validation
- **Error handling**: Comprehensive JSON-RPC error responses

**Ping-Pong Server** (`ping-pong.py`):
- **Hook-based session monitoring** via file mtime tracking
- **Auto-discovery** of sessions from `$CLAUDE_PLUGIN_ROOT/.sessions/` directories
- **Stale detection** and automatic continuation prompts
- **Direct tmux session** communication for session revival
- **Randomized continuation messages** for natural interaction (5+ variants)
- **Debug-only logging** via `RESIN_AI_DEBUG=1` environment variable
- **System-wide session tracking** at plugin root level

### 9. Session Monitoring & Revival

Hooks-based ping/pong system ensures continuous agent operation:

**How it works**:
1. **Hooks track activity**: Every tool use updates session file with todos from `tool_input.todos`
2. **Ping-pong monitors**: Background process checks for stale sessions via file mtime
3. **Auto-continuation**: Sends prompts to tmux sessions by session ID when stale detected (only if active todos exist)
4. **Session files**: `$CLAUDE_PLUGIN_ROOT/.sessions/{normalized_project}/{session_id}.json`

**Session lifecycle**:
- **PreToolUse hook** (TodoWrite): Updates session file with todos array from `tool_input.todos`
- **PostToolUse hook**: Updates file mtime for activity tracking
- **UserPromptSubmit hook**: Ensures tmux session name stays synchronized with Claude Code session ID
- **SessionStart hook**: Renames tmux session to match Claude Code session ID
- **Background monitor**: Checks file mtime every 30 seconds, parses todos, counts active/pending tasks
- **Stale detection**: No activity for 150 seconds + active/pending todos triggers continuation
- **SessionEnd hook**: Deletes session file (todo-aware - preserves if active todos exist)

**Continuation messages**:
- **Randomized prompts**: 5+ message variants for natural interaction
- **Examples**: "Please continue working...", "Let's keep going...", "Continue..."

**Debug mode**:
- **Enable logging**: Set `RESIN_AI_DEBUG=1` environment variable
- **Production default**: Logging disabled for zero overhead
- **Log location**: `$CLAUDE_PLUGIN_ROOT/.sessions/logs/`

**Session file format**:
- **Filename**: `{session_id}.json` (session_id encoded in filename)
- **Contents**: JSON array of todos from `tool_input.todos` in PreToolUse hook payload
- **Example**: `[{"content":"Phase 1","activeForm":"Running Phase 1","status":"in_progress"}]`
- **Benefits**:
  - Self-contained (no dependency on `~/.claude/todos`)
  - Reads directly from hook payload (`tool_input.todos`)
  - Falls back to `~/.claude/todos` if needed
  - mtime-based staleness detection
  - Smart continuation (only when active/pending todos exist)

**Requirements**:
- **tmux required**: All orchestrator work must run in tmux
- **Automatic setup**: Hooks are plugin-native (no manual configuration)
- **Zero overhead**: File write operations on active events only (~1-2ms per event)

### 10. TMUX Environment Requirements

All orchestrator commands require tmux for session persistence and monitoring:

**Critical requirements**:
- **MUST** run in tmux session for orchestrator commands (`/orchestrator:plan`, `/orchestrator:work`, `/orchestrator:docs`)
- **Automatic verification**: Phase 00 checks `$TMUX_PANE` environment variable
- **Immediate stop**: Commands halt with clear error message if tmux not detected
- **Template-based errors**: Consistent error reporting via `TMUX-ERROR.md` template

**How to start tmux**:
```bash
# Create new session
tmux new -s resin-ai-orchestrator

# Or attach to existing session
tmux attach -t resin-ai-orchestrator
```

**Why tmux is required**:
- **Session persistence**: Long-running orchestrations survive terminal disconnects
- **Activity monitoring**: Ping-pong system tracks stale sessions via session IDs
- **Auto-revival**: Continuation prompts sent directly to tmux sessions by session ID
- **Session naming**: tmux sessions automatically renamed to match Claude Code session IDs
- **Simplified targeting**: Uses session IDs (e.g., `tmux send-keys -t $SESSION_ID`) instead of pane IDs for more robust communication
- **Stable references**: Session IDs don't change, unlike pane IDs which can shift

**Resources**:
- **TMUX requirements**: `orchestrator/resources/CORE/TMUX.md`
- **Error template**: `orchestrator/resources/TEMPLATE/REPORT/TMUX-ERROR.md`

## CLI Commands

### Planning Orchestrator

```bash
/orchestrator:plan                           # Auto-discover next planning level
/orchestrator:plan "Build SaaS platform"     # Project-level planning
/orchestrator:plan "Add authentication"      # Epic-level planning
/orchestrator:plan "User login story"        # Story-level planning
```

**Output**: Complete development plan with documentation hierarchy

### Implementation Orchestrator

```bash
/orchestrator:work                           # Auto-discover next task
/orchestrator:work 0003                      # Full epic orchestration
/orchestrator:work 0003.02                   # Story-level orchestration
/orchestrator:work 0003.02.01                # Task-level orchestration
```

**Process**: Autonomous execution through all implementation phases with TDD

### Documentation Generator

```bash
/orchestrator:docs                           # Generate technical documentation
```

**Output**: Complete LLM-optimized documentation suite

### Planning Preview

```bash
/orchestrator:dryrun [DESCRIPTION]           # Preview planning without execution
```

**Purpose**: Understand what will be created before committing

## Workflow Architecture

### Complete Development Lifecycle

```
1. Planning Phase (/orchestrator:plan)
   ↓
   Product Manager: Project architecture and epic discovery
   ↓
   Project Manager: Epic breakdown into stories
   ↓
   Feature Manager: Story breakdown into tasks
   ↓
   Output: Complete development plan

2. Implementation Phase (/orchestrator:work)
   ↓
   For each Task:
     ├── Developer: TDD implementation (11 phases)
     ├── Quality Assurance: Enhanced validation
     └── Transition to next task
   ↓
   For each Story:
     └── Complete all tasks → Story complete
   ↓
   For each Epic:
     └── Complete all stories → Epic complete
   ↓
   Output: Fully implemented, tested, validated code

3. Documentation Phase (/orchestrator:docs)
   ↓
   Auto-generate technical documentation
   ↓
   Output: LLM-optimized docs with code examples
```

### State Transition Flow

```
User Command
   ↓
Auto-detect Scope (Project/Epic/Story/Task)
   ↓
Load State Machine Definition
   ↓
Execute Current Phase
   ↓
Evaluate Return Code
   ├── CONTINUE → Next phase
   ├── EXIT → Complete orchestration
   └── FAILURE → Handle error
   ↓
Update State and Documentation
   ↓
Loop until completion
```

## Agent Specialization

### Product Manager
- **Expertise**: Strategic planning, architecture, technology selection
- **Phases**: Project initialization, epic discovery
- **Output**: OVERVIEW.md, ARCHITECTURE.md, TECH-STACK.md, DEPLOYMENT.md

### Project Manager
- **Expertise**: Epic decomposition, story prioritization
- **Phases**: Epic planning, story breakdown
- **Output**: Epic documentation with story definitions

### Feature Manager
- **Expertise**: Task specification, technical dependencies
- **Phases**: Story planning, task breakdown
- **Output**: Story documentation with task specifications

### Developer Specialists
- **Expertise**: Language-specific TDD implementation
- **Languages**: Python, TypeScript, Next.js, Swift
- **Methodology**: 11-phase TDD with zero-placeholder policy
- **Output**: Production-ready, fully-tested code

### Quality Assurance
- **Expertise**: Enhanced validation, comprehensive testing
- **Standards**: 95%+ coverage, security scanning, performance validation
- **Methodology**: Multi-layer testing (unit, integration, E2E)
- **Output**: Validation reports, test results, approval/rejection decisions

## Resource System

48 Markdown resource files organized by category:

### CORE Resources (6 files)
- **PHASE-EXECUTION-REQUIREMENTS.md**: Universal execution requirements
- **PHASE-EXECUTION-RESTRICTIONS.md**: Execution constraints
- **TEMPLATE-REQUIREMENTS.md**: Output template standards
- **EPIC-STORY-TASK-FORMAT.md**: Hierarchical ID format
- **TMUX.md**: TMUX environment requirements for all commands
- **YOU-DO-NOT-UNDERSTAND.md**: Error handling instructions

### STATE-MACHINE Resources (14 files)
- **Orchestration controllers**: PLANNING, PROJECT, EPIC, STORY, TASK
- **State templates**: INIT, LOOP, QUIZ, WORK, TEST, DONE
- **Protocols**: HANDOFF-PROTOCOL.md, RETURN-CODES.md

### AGENT Resources (8+ directories)
- **Developer phases**: 11 phases for TDD implementation
- **Manager requirements**: Planning and coordination guidelines
- **QA phases**: Validation and testing procedures

### TEMPLATE Resources (20+ files)
- **Documentation**: ARCHITECTURE, TECH-STACK, OVERVIEW, etc. (10 templates)
- **Development plans**: Epic, Story, Task templates
- **Reports**: STATE-TRANSITION, HANDOFF, VALIDATION (9 templates)
- **Questionnaires**: Requirements discovery templates

## Configuration

### Plugin Configuration

**Marketplace Entry** (`.claude-plugin/marketplace.json`):
```json
{
  "name": "resin-ai",
  "plugins": [{"name": "orchestrator", "source": "./orchestrator"}]
}
```

**Plugin Metadata** (`orchestrator/.claude-plugin/plugin.json`):
```json
{
  "name": "orchestrator",
  "version": "2.0.0",
  "description": "Autonomous agentic orchestration system..."
}
```

### MCP Server Configuration

**Server Definition** (`orchestrator/.mcp.json`):
```json
{
  "mcpServers": {
    "resources": {
      "type": "stdio",
      "command": "python3",
      "args": ["-c", "import os; os.chdir('${CLAUDE_PLUGIN_ROOT}'); exec(open('resources.py').read())"]
    }
  }
}
```

### Resource Resolution

- **Root Directory**: `orchestrator/resources/`
- **URI Scheme**: `plugin:orchestrator:resources://CATEGORY/FILE.md`
- **Special Variable**: `${CLAUDE_PLUGIN_ROOT}` for plugin root path
- **Security**: No directory traversal, Markdown-only files

## Usage Examples

### Complete Feature Development

```bash
# Step 1: Plan the project
/orchestrator:plan "Build a task management SaaS platform"

# Creates:
# - docs/OVERVIEW.md
# - docs/ARCHITECTURE.md
# - docs/TECH-STACK.md
# - docs/DEPLOYMENT.md
# - docs/DEVELOPMENT.md
# - docs/FILES.md
# - docs/DEVELOPMENT-PLAN.md
# - docs/DEVELOPMENT-PLAN/0001 - Task Management Core.md
# - docs/DEVELOPMENT-PLAN/0001.01 - User Authentication.md
# - docs/DEVELOPMENT-PLAN/0001.01.01 - Database Schema.md
# - ... (all epics, stories, tasks)

# Step 2: Implement the first epic
/orchestrator:work 0001

# Autonomous execution:
# 1. Developer implements Task 0001.01.01 (TDD, 11 phases)
# 2. QA validates (95%+ coverage, all tests pass)
# 3. Transitions to Task 0001.01.02
# 4. Repeats until all tasks complete
# 5. Story 0001.01 complete
# 6. Continues with Story 0001.02
# 7. Epic 0001 complete

# Step 3: Generate documentation
/orchestrator:docs

# Creates:
# - Complete technical documentation
# - Code examples and file references
# - LLM-optimized technical writing
```

### Incremental Development

```bash
# Plan just an epic
/orchestrator:plan "Add real-time notifications"

# Implement just a story
/orchestrator:work 0002.03

# Implement just a task
/orchestrator:work 0002.03.05
```

### Auto-Discovery

```bash
# Let the system find the next work
/orchestrator:work

# System will:
# 1. Analyze existing documentation
# 2. Find next unfinished task
# 3. Execute implementation automatically
```

## Quality Standards

### Developer Standards (BASE)
- Standard technical implementation
- TDD methodology (tests first)
- Zero placeholders or stubs
- Complete functional implementations
- Comprehensive test coverage

### Quality Assurance Standards (ENHANCED)
- 95% minimum test coverage
- All tests must pass (100% pass rate)
- Security vulnerability scanning
- Performance benchmarking
- Integration testing
- Regression validation
- Returns to development on any failure

### Feature Manager Standards (MAXIMUM)
- Business value validation
- User experience verification
- Stakeholder acceptance criteria
- Journey completion validation

### Product Manager Standards (STRATEGIC)
- Epic coherence validation
- Portfolio alignment
- Resource utilization optimization
- Strategic goal fulfillment

## Dependencies

### Zero External Dependencies

The MCP server uses **Python standard library only**:
- `json`: JSON parsing and serialization
- `sys`: stdio communication
- `pathlib`: File path operations
- `typing`: Type annotations

**Benefits**:
- Maximum portability
- No pip installation required
- Minimal attack surface
- Works in any Python 3.10+ environment

### Internal Dependencies

| Component | Depends On | Purpose |
|-----------|-----------|---------|
| Commands | Resources | Load state machine definitions |
| Commands | Agents | Agent delegation |
| Agents | Resources | Phase definitions |
| Agents | Templates | Output generation |
| MCP Server | None | Standalone server |

## Design Principles

### Autonomous Execution
- **Runs to completion** without user interruption
- **Deterministic state transitions** via return codes
- **Automatic error recovery** through retry mechanisms
- **Continuous progress** until success or critical failure

### Hierarchical Organization
- **Project → Epic → Story → Task** structure
- **Context enrichment** at each level
- **Progressive refinement** from high-level to detailed
- **Parent context inheritance** prevents duplicate questions

### Quality-First Development
- **TDD enforcement** (tests before implementation)
- **Zero tolerance** for test failures
- **Multiple validation layers** (unit, integration, E2E)
- **Comprehensive coverage** requirements (95%+ minimum)

### Template-Driven Consistency
- **Standardized outputs** across all agents
- **Predictable document structure** for LLMs
- **Eliminates duplication** through DRY principles
- **Concrete examples** with file references

### Resource-Driven Architecture
- **All knowledge in Markdown** for transparency
- **Version-controlled expertise** via Git
- **Easy customization** through file editing
- **No hardcoded logic** in orchestrators

## Advanced Features

### Loop Detection
- Prevents infinite loops in state machines
- Tracks iteration counts
- Updates phase names with iteration counters
- Triggers escalation on excessive retries

### Enriched Context
- Questionnaire-based requirements discovery
- Hierarchical context preservation
- Prevents re-asking answered questions
- Scope-specific question filtering

### Agent Delegation Protocol
- Standardized handoff between agents
- Return codes for state transitions
- Context transfer in reports
- Failure reason documentation

### Phase Numbering System
Zero-padded sequential numbering based on context:
- `{XX}`: Orchestration phase (01, 02, 03...)
- `{LL}/{TT}`: Level iteration (current/total)
- `{SS/YY}`: Story iteration (current/total)
- `{TT/ZZ}`: Task iteration (current/total)
- `{II}`: Implementation cycle number

## Troubleshooting

### Common Issues

**Issue**: MCP server not responding
- **Check**: Python 3.10+ installed
- **Check**: Working directory is plugin root
- **Solution**: Verify `.mcp.json` configuration

**Issue**: Resource files not found
- **Check**: URI scheme format (`plugin:orchestrator:resources://...`)
- **Check**: File exists in `orchestrator/resources/`
- **Solution**: Use correct path relative to resources directory

**Issue**: State machine stuck in loop
- **Check**: Return codes in agent outputs
- **Check**: Iteration counters in phase names
- **Solution**: Review agent logic for proper exit conditions

**Issue**: Planning creates wrong scope
- **Check**: Input description specificity
- **Solution**: Use explicit Epic/Story/Task IDs instead of descriptions

## Contributing

This system is designed for extensibility:

### Adding New Agents
1. Create agent file in `orchestrator/agents/`
2. Define expertise, phases, and return codes
3. Reference agent in orchestration commands

### Adding New Resources
1. Create Markdown file in appropriate `orchestrator/resources/` category
2. Follow template requirements
3. Reference via URI scheme

### Adding New Commands
1. Create command file in `orchestrator/commands/`
2. Define state machine flow
3. Specify agent delegation logic

### Adding New Templates
1. Create template in `orchestrator/resources/TEMPLATE/`
2. Follow standardized structure
3. Include concrete examples

## License

See [LICENSE](./LICENSE) file for details.

## Support

For issues, questions, or contributions, please refer to the project repository.

---

**Note**: This orchestrator system represents a sophisticated approach to autonomous software development, combining state machine determinism with AI agent flexibility to deliver complete, tested, production-ready software through hierarchical planning and TDD methodology.
