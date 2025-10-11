<!-- Updated: 2025-09-28 22:30:00 UTC -->

## TASK TOOL

### CRITICAL REQUIREMENTS
- **ONLY** use when you need specialized expertise
- **ONLY** orchestrators can launch agents
- **MUST** provide clear, detailed prompts
- **MUST** wait for agent completion

### CRITICAL RESTRICTIONS
- **NEVER** use Task tool if you are a agent yourself
- **NEVER** use Task tool recursively
- **NEVER** launch agents from within agents
- **NEVER** delegate orchestration responsibilities

### Valid Usage
- **Launch specialized agents** for complex multi-step operations
- **Delegate domain tasks** to appropriate agent
- **Use expert agents** for comprehensive investigation
- **Coordinate workflows** across multiple agents
- **Manage dependencies** between parallel executions

### Usage Notes
- Agents cannot launch other agents (no recursion)
- Only the orchestrator manages state transitions
- Orchestrator maintains overall control flow
