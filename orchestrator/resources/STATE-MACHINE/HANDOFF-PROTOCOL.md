<!-- Updated: 2025-10-17 12:54:25 UTC -->

## HANDOFF PROTOCOL

### CRITICAL REQUIREMENTS
- **MUST** use radical brevity
- **MUST** provide concise, compact and accurate report
- **MUST** focus on actionable information for next phase
- **MUST** lead with blockers/issues if any exist

### CRITICAL RESTRICTIONS
- **NEVER** include play-by-play of how work was done
- **NEVER** repeat information available in git diff
- **NEVER** dump exhaustive test results (link to CI instead)
- **NEVER** restate requirements from task documentation
- **NEVER** include congratulatory or cheerleading content

### Handoff Format

### Standard Structure
- **Status**: Current state (COMPLETE, BLOCKED, IN_PROGRESS)
- **Deliverables**: Brief list of what was created/changed
- **Key Decisions**: Choices that affect downstream work
- **Quality**: One-line summary (tests passing, no errors, etc.)
- **Issues**: Blockers or known problems (or "None")
- **Next**: What needs to happen next
- **Return Code**: State transition code

### Information Hierarchy
- **Lead with problems** (blockers, errors, risks)
- **Then key deliverables** (what was built)
- **Then decisions** (choices affecting future work)
- **Skip obvious details** (provable via git/CI)
