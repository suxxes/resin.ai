# Shared Components Architecture

This directory contains reusable components that power the multi-agent orchestration system. Components are organized into four categories based on their purpose and usage patterns.

## Directory Structure

```
shared/
├── core/          # Fundamental agent behaviors and standards
├── workflows/     # Developer and inter-agent workflows
├── orchestrator/  # Orchestrator-specific management logic
└── quality/       # Quality validation and assurance components
```

## Component Categories

### 1. Core Components (`core/`)

**Purpose**: Define fundamental behaviors, standards, and expectations that apply across all agents.

**Usage Pattern**: These components are typically included at the beginning of agent definitions to establish baseline behaviors and standards.

**Key Concepts**:
- **Agent Identity**: How agents announce and identify themselves
- **Understanding Boundaries**: What agents do and don't understand
- **Output Standards**: Consistent formatting and communication patterns
- **Code Architecture**: Structural patterns and design principles
- **Documentation Requirements**: Standards for maintaining documentation
- **Template Standards**: Requirements for using and creating templates

**Example Usage in Agent**:
```markdown
<!-- Critical Understanding Check -->
!`cat ~/.claude/shared/core/[understanding component]`

<!-- Agent Self-Reporting -->
!`cat ~/.claude/shared/core/[identity component]`

<!-- Architecture Components -->
!`cat ~/.claude/shared/core/[architecture component]`
```

### 2. Workflow Components (`workflows/`)

**Purpose**: Define how agents perform their work and interact with the orchestration system.

**Usage Pattern**: These components are included by developer agents to understand their implementation approach, quality requirements, and communication protocols.

**Key Concepts**:
- **Implementation Approach**: How developers implement tasks
- **Tool Usage**: How agents use TodoWrite and Task tools
- **Project Discovery**: How to understand and adapt to project conventions
- **Deliverable Management**: Tracking and validating completion
- **Quality Gates**: Standards that must be met before handoff
- **Inter-Agent Communication**: Protocols for handing off work

**Workflow Types**:

#### Developer Workflows
Components that guide how developers implement tasks:
- Task implementation strategies
- Project tooling discovery
- Implementation checklists
- Technical documentation practices
- Progress tracking mechanisms

#### Interface Workflows
Components that define agent-orchestrator communication:
- Return code definitions
- Handoff protocols
- Task verification procedures
- Quality gate requirements

#### Tool Workflows
Components for using system tools:
- TodoWrite patterns for developers
- Task tool usage for developers
- Base tool usage templates

**Example Usage in Developer Agent**:
```markdown
<!-- Task Implementation Strategy -->
!`cat ~/.claude/shared/workflows/[implementation strategy]`

<!-- Project Tooling Discovery -->
!`cat ~/.claude/shared/workflows/[discovery component]`

<!-- Quality Gates -->
!`cat ~/.claude/shared/workflows/[quality standards]`
```

### 3. Orchestrator Components (`orchestrator/`)

**Purpose**: Define how the orchestrator manages and coordinates agents throughout the development lifecycle.

**Usage Pattern**: These components are used exclusively by orchestrator commands to manage the multi-agent workflow.

**Key Concepts**:
- **Task Management**: How orchestrator tracks and manages tasks
- **Agent Delegation**: Logic for selecting and invoking appropriate agents
- **Todo Management**: Orchestrator-level todo tracking and state management

**Orchestrator Responsibilities**:
- Determining which agent to invoke based on current phase
- Managing state transitions between phases
- Tracking overall progress across epics, stories, and tasks
- Handling return codes and determining next actions
- Coordinating git workflow operations

**Example Orchestrator Logic**:
```markdown
<!-- The orchestrator uses these internally for management -->
- Task delegation to appropriate specialist agents
- Managing TodoWrite for phase tracking
- Coordinating multi-agent workflows
```

### 4. Quality Components (`quality/`)

**Purpose**: Define validation criteria and quality assurance standards that ensure complete, high-quality deliverables.

**Usage Pattern**: These components are included by both developer agents (to understand requirements) and QA agents (to perform validation).

**Key Concepts**:
- **Deliverable Validation**: Criteria for complete deliverables
- **Tool Validation**: Quality checks for tool usage
- **TodoWrite Validation**: Ensuring proper task tracking

**Quality Levels**:
- **BASE**: Standard implementation quality (developers)
- **ENHANCED**: Comprehensive validation (QA agents)
- **MAXIMUM**: Business validation (feature leads)
- **STRATEGIC**: Epic-level coherence (project managers)

**Example Usage**:
```markdown
<!-- Deliverable Validation -->
!`cat ~/.claude/shared/quality/[validation criteria]`
```

## Component Interaction Patterns

### Developer Agent Pattern
```
1. Core components establish identity and boundaries
2. Workflow components define implementation approach
3. Quality components set completion criteria
4. Return codes communicate status to orchestrator
```

### Orchestrator Pattern
```
1. Receives return codes from agents
2. Uses orchestrator components to determine next action
3. Delegates to next agent using task management logic
4. Tracks progress using todo management
```

### Quality Assurance Pattern
```
1. Receives completed work from developers
2. Applies quality validation components
3. Returns validation results via return codes
4. Documents issues for developer iteration if needed
```

## Design Principles

### 1. Modularity
Each component serves a single, well-defined purpose. Components can be combined to create agent behaviors without duplication.

### 2. Reusability
Components are written to be agent-agnostic where possible, allowing the same component to be used by multiple agent types.

### 3. Clear Boundaries
- **Core**: Universal standards and behaviors
- **Workflows**: How work gets done
- **Orchestrator**: How work is managed
- **Quality**: How work is validated

### 4. Composition Over Inheritance
Agents are composed by including relevant components rather than inheriting from base templates. This allows flexible, purpose-specific agent definitions.

### 5. Explicit Communication
Components define explicit interfaces (return codes, handoff protocols) for inter-agent communication, avoiding implicit dependencies.

## Usage Guidelines

### For Agent Developers

1. **Start with Core**: Include fundamental components first
2. **Add Workflows**: Include relevant workflow components for your agent type
3. **Include Quality Standards**: Add appropriate quality validation components
4. **Define Return Codes**: Specify your agent's return codes

### For Orchestrator Developers

1. **Use Orchestrator Components**: Leverage management and delegation logic
2. **Handle All Return Codes**: Ensure all possible agent responses are handled
3. **Maintain State**: Track progress across all phases
4. **Coordinate Workflows**: Manage transitions between agents

### For System Maintainers

1. **Preserve Modularity**: Keep components focused and single-purpose
2. **Document Changes**: Update this README when adding new component categories
3. **Maintain Boundaries**: Respect the separation between categories
4. **Test Integration**: Ensure components work together correctly

## Component Lifecycle

### Creation
1. Identify reusable pattern across multiple agents
2. Extract into appropriate category folder
3. Replace agent-specific content with template variables
4. Document usage pattern

### Modification
1. Consider impact across all agents using the component
2. Maintain backward compatibility where possible
3. Update affected agents if breaking changes required
4. Document changes in commit messages

### Deprecation
1. Mark component as deprecated with migration path
2. Update agents to use replacement components
3. Remove after all references updated
4. Archive if historical reference needed

## Best Practices

### Component Design
- Keep components small and focused
- Use clear, descriptive names
- Include usage comments within components
- Provide template variables for customization

### Component Usage
- Include components in logical order
- Group related components together
- Add section comments for clarity
- Don't duplicate component functionality

### Component Maintenance
- Regular review for redundancy
- Consolidate similar components
- Update outdated patterns
- Remove unused components

## Architecture Benefits

### 1. Consistency
All agents using the same components behave consistently, reducing surprises and bugs.

### 2. Maintainability
Changes to shared behavior only need to be made once, in the component.

### 3. Clarity
Clear categorization makes it obvious where functionality belongs and where to find it.

### 4. Flexibility
New agents can be quickly composed from existing components, accelerating development.

### 5. Testability
Components can be tested independently, ensuring reliability across all agents.

## Future Considerations

### Potential New Categories
- **Integrations**: Components for external service integration
- **Monitoring**: Observability and logging components
- **Security**: Security validation and enforcement components

### Evolution Path
The component system is designed to grow organically as patterns emerge. New categories should only be added when a clear, distinct purpose emerges that doesn't fit existing categories.

### Versioning Strategy
As the system matures, consider versioning components to support gradual migration and backward compatibility.

---

*This README provides a high-level overview of the shared component architecture. For specific component details, refer to the individual component files within each category folder.*