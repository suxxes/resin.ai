<!-- Updated: 2025-10-10 18:36:41 UTC -->

# Story Scope Questions Template

Structured question set for enriching story-level planning context.


## QUESTION SET OVERVIEW

**Total Questions**: 4 questions
**Estimated Time**: 2-3 minutes
**User Option**: Can skip any or all questions for informed assumptions


## STORY CONTEXT QUESTIONS

### Question 1: Functionality
**Ask**: "What specific functionality or capability does this story deliver?"

**Listening For**:
- Specific features or behaviors
- System functionality
- Component interactions
- Data operations

**Follow-up if unclear**: "What should the system be able to do after this story is complete?"


### Question 2: Acceptance Criteria
**Ask**: "What are the key acceptance criteria - how will we know this story is done?"

**Listening For**:
- Observable outcomes
- Specific behaviors
- Data requirements
- UI/UX expectations

**Follow-up if unclear**: "Can you describe what 'done' looks like for this story?"


### Question 3: Dependencies
**Ask**: "Does this story depend on other stories, components, or external services?"

**Listening For**:
- Story dependencies
- Component dependencies
- External service dependencies
- Data dependencies

**Follow-up if unclear**: "Can this be implemented independently, or does it need something else first?"


### Question 4: Edge Cases
**Ask**: "What edge cases, error scenarios, or validation rules should we consider?"

**Listening For**:
- Input validation requirements
- Error handling scenarios
- Business rule exceptions
- Boundary conditions

**Follow-up if unclear**: "What could go wrong, and what should happen?"


### Question 5: Technical Approach (Optional)
**Ask**: "Do you have preferences for the technical approach or implementation strategy?"

**Listening For**:
- Preferred patterns
- Technology constraints
- Performance requirements
- Specific libraries or tools

**Follow-up if unclear**: "Any technical constraints I should know about?"


## VALIDATION CHECKLIST

After collecting answers, validate understanding:

```
Let me confirm my understanding of this story:

**Functionality**: [restate]
**Acceptance Criteria**: [restate]
**Dependencies**: [restate]
**Edge Cases**: [restate]
**Technical Approach**: [restate if provided]

Is this an accurate understanding of the story scope?
```


## SKIP ASSUMPTIONS

If user skips questions, document these assumptions:

**Story Assumptions**:
- Delivers functionality within parent epic scope
- Standard acceptance criteria (functionality works, all tests pass, documented)
- No blocking dependencies beyond parent epic
- Standard edge case handling (input validation, error messages, logging)
- Follows project technical conventions and patterns
- Comprehensive testing coverage (unit + integration tests)
