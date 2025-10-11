<!-- Updated: 2025-09-28 22:30:00 UTC -->

## TASK TOOL

### CRITICAL REQUIREMENTS
- **ONLY** use when you need specialized expertise
- **ONLY** orchestrators can launch subagents
- **MUST** provide clear, detailed prompts
- **MUST** wait for subagent completion

### CRITICAL RESTRICTIONS
- **NEVER** use Task tool if you are a subagent yourself
- **NEVER** use Task tool recursively
- **NEVER** launch subagents from within subagents
- **NEVER** delegate orchestration responsibilities

### Valid Usage
- **Launch specialized subagents** for complex multi-step operations
- **Delegate domain tasks** to appropriate specialist agents
- **Use expert subagents** for comprehensive investigation
- **Coordinate workflows** across multiple specialists
- **Manage dependencies** between parallel executions

### Subagent Types
- **Manager agents** for planning and breakdown tasks
- **Developer agents** for implementation work
- **Quality agents** for validation and testing
- **Technical writers** for documentation
- **General-purpose** for research and analysis

### Usage Notes
- Subagents cannot launch other subagents (no recursion)
- Only the orchestrator manages state transitions
- Subagents return results via RETURN-CODES
- Orchestrator maintains overall control flow