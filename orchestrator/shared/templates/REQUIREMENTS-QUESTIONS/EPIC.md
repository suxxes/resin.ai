<!-- Updated: 2025-10-10 18:36:41 UTC -->

# Epic Requirements Discovery

Structured question set for enriching epic-level planning context.


## QUESTION SET OVERVIEW

**Total Questions**: 4-5 questions
**Estimated Answer Time**: 2-3 minutes
**User Option**: Can skip any or all questions for informed assumptions


## TECHNICAL CONTEXT QUESTIONS

### Question 1: Epic Scope
**Ask**: "What functionality or capabilities should this epic deliver?"

**Listening For**:
- Specific features or components
- User-facing functionality
- System capabilities
- Scope boundaries

**Follow-up if unclear**: "Can you describe what the system should be able to do after this epic is complete?"

### Question 2: Integration Points
**Ask**: "What existing system components, services, or APIs will this epic integrate with?"

**Listening For**:
- Internal system dependencies
- External service integrations
- Data flow requirements
- API contracts

**Follow-up if unclear**: "Is this adding to existing functionality or creating something new?"

### Question 3: Technical Constraints
**Ask**: "Are there specific technical constraints, requirements, or preferred approaches for this epic?"

**Listening For**:
- Technology requirements
- Performance constraints
- Security requirements
- Scalability needs
- Compliance requirements

**Follow-up if unclear**: "What technical challenges do you foresee?"

### Question 4: Dependencies (Optional)
**Ask**: "Does this epic depend on other epics, external systems, or specific infrastructure?"

**Listening For**:
- Epic dependencies
- External service requirements
- Infrastructure prerequisites
- Data migration needs

**Follow-up if unclear**: "Can this epic be implemented independently?"

### Question 5: Edge Cases & Risks (Optional)
**Ask**: "What edge cases, error scenarios, or risks should we plan for?"

**Listening For**:
- Known failure scenarios
- Data validation requirements
- Error handling needs
- Business rule exceptions

**Follow-up if unclear**: "What could go wrong, and how should we handle it?"


## VALIDATION CHECKLIST

After collecting answers, validate understanding:

```
Let me confirm my understanding of this epic:

**Epic Scope**:
- Functionality: [restate]
- Integrations: [restate]
- Constraints: [restate]
- Dependencies: [restate if answered]
- Risks: [restate if answered]

Did I capture the epic scope correctly? Any corrections?
```


## SKIP ASSUMPTIONS

When user skips questions, document these assumptions:

**Technical Assumptions**:
- Integrates with existing project architecture
- Follows established project patterns and conventions
- Standard error handling and validation
- No extraordinary performance requirements
- Consistent with project security model

**Scope Assumptions**:
- Epic scope limited to described functionality
- Standard edge cases and error scenarios covered
- Comprehensive testing coverage required
- Documentation updated as part of epic
- No blocking dependencies on external systems
