<!-- Updated: 2025-10-16 18:37:16 UTC -->

## PHASE EXECUTION RESTRICTIONS

Universal restrictions that ALL agents MUST observe when executing their phase-based workflows. Every agent that has a PROCESS DEFINITION with multiple phases MUST observe these restrictions.

### CRITICAL RESTRICTIONS

- **NEVER** skip any phase unless explicitly instructed in phase definition
- **NEVER** proceed to next phase without completing current phase
- **NEVER** violate phase-specific CRITICAL RESTRICTIONS

### Purpose

These restrictions ensure:
- **No shortcuts**: Every phase executed fully, no skipping allowed
- **Sequential integrity**: Phases build upon each other correctly
- **Rule compliance**: Phase-specific rules always enforced
- **Predictable behavior**: Workflow always follows documented process
- **Quality maintenance**: No compromises on defined standards
