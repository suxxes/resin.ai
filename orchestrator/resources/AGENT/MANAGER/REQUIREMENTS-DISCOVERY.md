<!-- Updated: 2025-10-16 15:22:14 UTC -->

## REQUIREMENTS ENRICHMENT WORKFLOW

Transform incomplete requirements into comprehensive planning context through structured questioning.

### When to Use

- Planning new projects without existing documentation
- User description lacks sufficient detail for planning
- Critical planning information is missing or ambiguous

### When to Skip
- Existing complete documentation exists (`docs/OVERVIEW.md`, `docs/ARCHITECTURE.md`, `docs/TECH-STACK.md`)
- User explicitly requests "use your judgment" or "make reasonable assumptions"
- User description is already comprehensive
- Planning at Task scope with clear specifications

### Questionnaire Execution

#### Announce Intent
Before asking questions, announce:
```
I need to ask {X} questions to complete planning context.
You can answer briefly, or type "skip" to proceed with informed assumptions.
```

#### Collect and Validate
1. Ask questions from template
2. Listen for answers and clarify if unclear
3. Restate understanding to confirm
4. Document any assumptions for skipped questions

#### Handle Skip
When user types "skip":
- Acknowledge request
- Apply scope-appropriate defaults based on best practices
- Document all assumptions clearly
- Continue to delegation

### Enriched Context Storage

Store validated context in structured format for agent delegation:

```markdown
## ENRICHED PLANNING CONTEXT

**Original Request**: {BRIEF_ORIGINAL_REQUIREMENTS}
**Scope Level**: {SCOPE_LEVEL}

### Validated Requirements
{REQUIREMENTS_FROM_QUESTIONNAIRE_ANSWERS}

### Assumptions Made
{LIST_ASSUMPTIONS_FOR_EACH_UNCLEAR_OR_SKIPPED_AREA}
```

### Delegation

Pass enriched context to planning agent with clear instruction:
```
ENRICHED_CONTEXT: {ENRICHED_PLANNING_CONTEXT}

Use this validated context. Do not re-ask these questions.
Validate assumptions during your planning phases as needed.
```
