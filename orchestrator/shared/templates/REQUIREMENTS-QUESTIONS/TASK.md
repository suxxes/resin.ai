<!-- Updated: 2025-10-03 02:13:31 UTC -->

# Task Scope Questions Template

Structured question set for enriching task-level planning context.


## QUESTION SET OVERVIEW

**Total Questions**: 2-3 questions
**Estimated Time**: 1-2 minutes
**User Option**: Can skip any or all questions for informed assumptions


## TASK CONTEXT QUESTIONS

### Question 1: Implementation Approach
**Ask**: "What's the preferred technical approach or implementation strategy for this task?"

**Listening For**:
- Specific algorithms or patterns
- Library or framework preferences
- Code organization
- Performance considerations

**Follow-up if unclear**: "Are there existing patterns in the codebase I should follow?"


### Question 2: Testing Requirements
**Ask**: "What testing approach and coverage level do you expect for this task?"

**Listening For**:
- Unit test requirements
- Integration test needs
- Test coverage expectations
- Specific test scenarios

**Follow-up if unclear**: "Should I focus on unit tests, integration tests, or both?"


### Question 3: Dependencies (Optional)
**Ask**: "Does this task depend on other tasks, components, or external libraries?"

**Listening For**:
- Task dependencies
- Component dependencies
- Library requirements
- Data dependencies

**Follow-up if unclear**: "Can this task be implemented independently?"


## VALIDATION CHECKLIST

After collecting answers, validate understanding:

```
Let me confirm my understanding of this task:

**Implementation**: [restate]
**Testing**: [restate]
**Dependencies**: [restate if provided]

Does this match your expectations for this task?
```


## SKIP ASSUMPTIONS

If user skips questions, document these assumptions:

**Task Assumptions**:
- Follow established project patterns and conventions
- Standard testing coverage (unit tests for logic, integration tests for interactions)
- Minimal external dependencies unless clearly needed
- Clean, maintainable code following project style guide
- Documentation comments for complex logic
- Error handling following project standards
