<!-- Updated: 2025-10-16 17:40:26 UTC -->

## PHASE EXECUTION REQUIREMENTS

Universal requirements that ALL agents MUST follow when executing their phase-based workflows. Every agent that has a PROCESS DEFINITION with multiple phases MUST follow these requirements.

### CRITICAL REQUIREMENTS

- **MUST** execute ALL phases in exact order as defined in PROCESS DEFINITION
- **MUST** complete current phase before proceeding to next phase
- **MUST** follow ALL phase-specific CRITICAL REQUIREMENTS without exception
- **MUST** create phase tasks during Initialize Tasks phase
- **MUST** update task status (in_progress/completed) as phases progress
- **MUST** use TodoWrite tool to track phase execution

### Purpose

These requirements ensure:
- **Systematic execution**: Phases execute in predictable, logical order
- **Completeness**: No phases skipped, all work thoroughly completed
- **Transparency**: Todo list provides clear visibility into progress
- **Accountability**: Each phase marked complete only when truly finished
- **Quality**: Phase-specific requirements enforced at every step
