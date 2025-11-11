<!-- Updated: 2025-11-11 18:03:58 UTC -->

## {SCOPE_LEVEL} REQUIREMENTS DISCOVERY

Structured question set for enriching {SCOPE_LEVEL_LOWERCASE}-level planning context using **AskUserQuestion tool**.

### CRITICAL REQUIREMENTS

- **MUST** use AskUserQuestion tool for ALL questions
- **MUST** read and follow `plugin:orchestrator:resources://CORE/ASK-USER-QUESTION-TOOL.md`
- **NEVER** ask questions in plain text
- **MUST** provide 2-4 structured options with trade-off descriptions

### Question Set Overview

**Total Question Categories**: {TOTAL_CATEGORIES}
**Questions Per Category**: 1-4
**User Option**: Can select "Other" for custom input or skip entire category

### Requirements Clarification Questions

#### Question Category X: {QUESTION_X_AREA}

**Use AskUserQuestion tool with structure**:
```json
{
  "questions": [
    {
      "question": "{QUESTION_X_TEXT}?",
      "header": "{HEADER}",
      "multiSelect": false,
      "options": [
        {
          "label": "{OPTION_1_LABEL}",
          "description": "{OPTION_1_DESCRIPTION_WITH_TRADEOFFS}"
        },
        {
          "label": "{OPTION_2_LABEL}",
          "description": "{OPTION_2_DESCRIPTION_WITH_TRADEOFFS}"
        },
        {
          "label": "{OPTION_3_LABEL}",
          "description": "{OPTION_3_DESCRIPTION_WITH_TRADEOFFS}"
        }
      ]
    }
  ]
}
```

**Listening For**:
- User selection from options
- Custom input if "Other" selected
- Request to skip category

**Follow-up if "Other" selected**: Use AskUserQuestion to clarify custom input if ambiguous

<!-- CRITICAL: REPEAT PATTERN FOR EACH CATEGORY -->

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
