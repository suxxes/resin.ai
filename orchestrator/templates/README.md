# Claude Code Development Templates

This folder contains **meta-templates** for creating and updating Claude Code agents and commands. These templates ensure structural alignment and consistency across all agent and command instructions.

## Purpose

**This folder contains templates FOR creating agents and commands, NOT templates used BY agents and commands.**

- ✅ Agent instruction structure templates
- ✅ Command instruction structure templates
- ✅ Guidelines for agent and command development
- ❌ Internal templates that agents use (those go in agent instructions)
- ❌ Internal templates that commands use (those go in command instructions)

## Template Usage

### For Agent and Command Developers

When creating or updating agents:
1. **Use AGENT-STRUCTURE.md** as the base template
2. **Follow the established sections** and naming conventions
3. **Include Templates section** at the end with internal agent templates
4. **Use CAPITAL_CASE** for internal template names
5. **Reference templates** in workflow steps, not as appendices

When creating or updating commands:
1. **Use COMMAND-STRUCTURE.md** as the base template
2. **Follow established command structure** and naming conventions
3. **Include Templates section** at the end with internal command templates (if needed)
4. **Use CAPITAL_CASE** for internal template names
5. **Reference templates** in command workflow steps

### Template Guidelines

#### Agent Structure Requirements
- **Header section** with name, description, tools, color
- **Expertise/Non-expertise** sections clearly defined
- **Agent self-reporting** patterns integrated into opening definition
- **Phase-specific workflows** with detailed steps
- **Return codes** integrated into workflow completion
- **Templates section** at end with internal templates

#### Command Structure Requirements
- **Header section** with command name, description, and detailed purpose
- **Features section** documenting key capabilities and functionality
- **Usage section** with command syntax and practical examples
- **Process/Workflow section** for complex multi-step commands
- **Command-specific sections** (Parameters, Output Format, Best Practices, etc.)
- **Templates section** at end with internal command templates (if needed)

#### Internal Template Standards
- Place all agent/command-specific templates **inside the respective instructions**
- Use **CAPITAL_CASE** naming: `TEMPLATE-NAME`
- Format as code blocks with `template` language
- Use `[PLACEHOLDER]` format for variables
- Reference templates in workflow: "using **TEMPLATE-NAME** template"

## Available Meta-Templates

### AGENT-STRUCTURE.md
Complete structural template for agent instructions including:
- Header format and required fields
- Expertise/limitation sections
- Workflow organization patterns
- Return code integration
- Internal template placement

### COMMAND-STRUCTURE.md
Complete structural template for command instructions including:
- Command header format and detailed purpose description
- Features section with key capabilities documentation
- Usage section with syntax and practical examples
- Process/workflow organization for complex commands
- Command-specific sections (parameters, output, best practices)
- Internal template placement and usage guidelines

## Development Standards

### Structural Consistency
- All agents and commands follow consistent basic structures
- Agent phase workflows are clearly separated
- Command workflow steps are logically organized
- Return codes are integrated into workflow steps
- Templates are placed at the end, not embedded in workflow

### Content Standards
- Avoid monetary estimates and time-based targets
- Focus on qualitative business outcomes
- Use professional, business-focused communication
- Include clear orchestrator integration (for agents)
- Provide clear usage examples (for commands)

### Template Integration
- Internal templates are part of agent/command instructions
- Templates are referenced in workflow steps
- Templates use consistent placeholder formatting
- Templates follow established naming conventions

### Status Progression Standards
- **Epic Status Progression**: `NOT_STARTED` → `IN_PROGRESS (PLANNING)` → `READY_FOR_DEVELOPMENT` → `IN_DEVELOPMENT` → `COMPLETED`
- **Story Status Progression**: `NOT_STARTED` → `IN_PROGRESS (PLANNING)` → `READY_FOR_DEVELOPMENT` → `IN_DEVELOPMENT` → `COMPLETED`
- **Task Status Progression**: `NOT_STARTED (PENDING)` → `IN_PROGRESS` → `COMPLETED`
- **QA Iteration Handling**: Task `COMPLETED` status persists through QA failure cycles - orchestrator handles iteration without status reversion
- **Visual Task Indicators**: ⬜ (pending) → 🔄 (in progress) → ✅ (completed)
- **Phase Mapping**: Each orchestrator phase maps to specific status transitions
- **Status Validation**: Quality Assurance validates proper status progression compliance

## Development Process

### For Agents:
1. **Copy AGENT-STRUCTURE.md** as starting point
2. **Customize for specific agent role** and responsibilities
3. **Define phase workflows** with specific steps
4. **Create internal templates** in Templates section
5. **Reference templates** in workflow steps
6. **Test agent integration** with orchestrator system

### For Commands:
1. **Copy COMMAND-STRUCTURE.md** as starting point
2. **Customize for specific command purpose** and functionality
3. **Define command workflow** with clear steps (if multi-step command)
4. **Add command-specific sections** as needed (parameters, output format, etc.)
5. **Create internal templates** in Templates section (if needed)
6. **Reference templates** in command workflow
7. **Test command functionality** and integration

This ensures all agents and commands have consistent structure while keeping their internal templates accessible within their own instructions.