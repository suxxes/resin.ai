<!-- Updated: 2025-10-17 12:14:01 UTC -->

## {SCOPE_LEVEL} REQUIREMENTS DISCOVERY

Structured question set for enriching {SCOPE_LEVEL_LOWERCASE}-level planning context.

### Question Set Overview

**Total Questions**: {TOTAL_QUESTIONS}
**Estimated Answer Time**: {ESTIMATED_TIME}
**User Option**: Request to skip at any time for informed assumptions

### Requirements Clarification Questions

#### Question X: {QUESTION_X_AREA}
**Ask**: "{QUESTION_X_TEXT}"

**Listening For**:
- {LISTENING_POINT_X}
<!-- CRITICAL: REPEAT PATTERN FOR EACH ITEM -->

**Follow-up if unclear**: "{QUESTION_X_FOLLOWUP}"

<!-- CRITICAL: REPEAT PATTERN FOR EACH ITEM -->

### Validation Checklist

After collecting answers, validate understanding:

```
Let me confirm my understanding of this {SCOPE_LEVEL_LOWERCASE}:

**{REQUIREMENT_SCOPE}**:
- {REQUIREMENT_AREA_X}: {REQUIREMENT_X_SUMMARY}
<!-- CRITICAL: REPEAT PATTERN FOR EACH ITEM -->

Did I capture the {SCOPE_LEVEL_LOWERCASE} scope correctly? Any corrections?
```

### Skip Assumptions

When user skips questions, document assumptions in form of an ADR:

**{ASSUMPTION_AREA_X}**:
- {ASSUMPTION_IN_ASSUMPTION_AREA_X}
<!-- CRITICAL: REPEAT PATTERN FOR EACH ITEM -->

<!-- CRITICAL: REPEAT PATTERN FOR EACH ITEM -->
