<!-- Updated: 2025-10-03 02:13:31 UTC -->

# Requirements Enrichment Workflow

Intelligent questionnaire workflow for enriching planning context when user descriptions lack sufficient detail. Based on framework.md's proven discovery approach.


## PURPOSE

Transform incomplete user descriptions into comprehensive planning context through structured questioning, enabling subagents to create high-quality plans without making assumptions.


## WHEN TO USE

Apply this workflow when:
- Planning new projects without existing documentation
- User description is brief or lacks technical details
- Critical planning information is missing or ambiguous
- Project scope requires specific architectural or technology decisions


## WHEN TO SKIP

Skip this workflow when:
- Existing project has complete documentation (docs/OVERVIEW.md, docs/ARCHITECTURE.md, docs/TECH-STACK.md exist)
- User explicitly requests "use your judgment" or "make reasonable assumptions"
- User description already contains comprehensive detail
- Planning for Task scope with clear technical specifications


## CONTEXT COMPLETENESS ASSESSMENT

### Required Information by Scope

#### Project Scope
**Business Context**:
- [ ] Project purpose and value proposition
- [ ] Target users and primary use cases
- [ ] Key success metrics and business goals
- [ ] Budget and timeline constraints

**Technical Context**:
- [ ] Platform requirements (web, mobile, desktop, etc.)
- [ ] Technology preferences or constraints
- [ ] Integration requirements with existing systems
- [ ] Performance and scalability needs
- [ ] Security and compliance requirements

**Team Context**:
- [ ] Team size and expertise
- [ ] Development methodology preference
- [ ] Deployment environment and infrastructure

#### Epic Scope
**Business Context**:
- [ ] Epic business value and strategic importance
- [ ] Target users affected by epic
- [ ] Success metrics for epic completion

**Technical Context**:
- [ ] Integration points with existing system
- [ ] Dependencies on other epics or external systems
- [ ] Technical constraints or requirements
- [ ] Performance or scalability considerations

#### Story Scope
**Business Context**:
- [ ] User value and acceptance criteria
- [ ] Priority and business justification

**Technical Context**:
- [ ] Dependencies on other stories or components
- [ ] Edge cases and error scenarios
- [ ] Technical approach preferences

#### Task Scope
**Technical Context**:
- [ ] Technical approach and implementation strategy
- [ ] Testing requirements and coverage expectations
- [ ] Dependencies on other tasks or components


## QUESTION GENERATION PATTERNS

### Transparency First
Always announce questioning approach:
```
I need to ask [N] questions in [M] categories to ensure complete planning context:
- [Category 1]: [X] questions
- [Category 2]: [Y] questions
- [Category 3]: [Z] questions

You can answer briefly, or type "skip" to have me make informed assumptions based on best practices.
```

### Question Quality Standards
**DO**: Ask specific, actionable questions
- ✅ "Who are the 3 primary user types and their main goals?"
- ✅ "What's your target response time for API calls?"
- ✅ "Do you have existing infrastructure constraints (AWS, Azure, on-prem)?"

**DON'T**: Ask vague, open-ended questions
- ❌ "Tell me about your users"
- ❌ "What are your performance needs?"
- ❌ "What technology do you want?"

### Question Categories

#### Business Questions
- Project purpose and value proposition
- Target users and use cases
- Success metrics and business goals
- Budget and timeline constraints
- Competitive positioning and market context

#### Technical Questions
- Platform and deployment requirements
- Technology preferences or constraints
- Integration requirements
- Performance and scalability needs
- Security and compliance requirements

#### Constraint Questions
- Team size and expertise
- Timeline and budget limitations
- Regulatory or compliance requirements
- Existing system dependencies
- Infrastructure availability


## QUESTION PRESENTATION PROTOCOL

### Format
1. **Announce Total**: State total questions and categories upfront
2. **Group by Category**: Ask related questions together
3. **Number Questions**: "Question 1 of 8:", "Question 2 of 8:", etc.
4. **Allow Skip**: Remind user they can type "skip" to proceed with assumptions
5. **Validate Understanding**: Restate answers to confirm comprehension

### Example Presentation
```
I need to ask 8 questions in 3 categories to complete the planning context:
- Business Context: 3 questions
- Technical Requirements: 4 questions
- Constraints: 1 question

You can answer each question, or type "skip" at any time to proceed with informed assumptions.

## Business Context

**Question 1 of 8**: Who are the primary user types (e.g., end users, admins, API consumers)?

[Wait for answer]

**Question 2 of 8**: What are the top 3 business goals this project must achieve?

[Wait for answer]

...

Let me confirm my understanding:
- Primary users: [restate]
- Business goals: [restate]
- ...

Is this correct? (yes/no/corrections)
```


## CONTEXT ENRICHMENT STORAGE

### Enriched Context Structure
Store validated answers in structured format:

```markdown
# Enriched Planning Context

## Source
- Original Request: "[user's original description]"
- Enrichment Date: [YYYY-MM-DD HH:MM:SS UTC]
- Scope Level: [Project|Epic|Story|Task]

## Business Context
- **Purpose**: [validated purpose]
- **Target Users**: [validated user types]
- **Success Metrics**: [validated metrics]
- **Constraints**: [validated constraints]

## Technical Context
- **Platform**: [validated platform]
- **Technology Preferences**: [validated tech]
- **Integration Requirements**: [validated integrations]
- **Performance Needs**: [validated performance]
- **Security Requirements**: [validated security]

## Team Context
- **Team Size**: [validated size]
- **Expertise**: [validated expertise]
- **Methodology**: [validated methodology]

## Assumptions
[List any assumptions made for unanswered questions]
```

### Delegation Package
Pass enriched context to subagent:
```
ENRICHED_CONTEXT:
[Complete enriched context structure]

Use this validated context for planning. Do not re-ask these questions.
Assumptions are marked clearly - validate these during your planning phases.
```


## VALIDATION PROTOCOL

### Answer Validation
After receiving answers:
1. **Restate Understanding**: Paraphrase answers in different words
2. **Identify Gaps**: Note any ambiguities or missing details
3. **Confirm Accuracy**: Get explicit user confirmation
4. **Document Assumptions**: Record any assumptions for unclear areas

### Example Validation
```
Let me confirm my understanding of your responses:

✓ You're building a SaaS platform for small businesses (10-50 employees)
✓ Primary users are business owners and accountants
✓ Must integrate with QuickBooks and Stripe
✓ Target is sub-2-second page loads for 1000 concurrent users
✓ Must be GDPR and SOC2 compliant

Did I understand correctly? Any corrections or additions?
```


## SKIP HANDLING

### User Initiates Skip
When user types "skip":
1. **Acknowledge**: "Understood, I'll proceed with informed assumptions"
2. **Document**: Mark which questions were skipped
3. **Make Assumptions**: Apply best practices and industry standards
4. **Communicate Assumptions**: List assumptions in delegation to subagent
5. **Enable Validation**: Allow subagent to validate assumptions in their planning

### Example Skip Response
```
Understood - I'll proceed with planning using these informed assumptions:
- Modern web application (React/Next.js or similar)
- Cloud deployment (AWS/Vercel/similar)
- Standard security practices (OAuth2, encryption at rest)
- Agile development methodology
- Team familiar with modern JavaScript ecosystem

The planning subagent will document these assumptions in the project documentation for your review and adjustment.
```


## INTEGRATION WITH PLAN COMMAND

### Execution Flow
1. **Context Discovery Phase** determines if enrichment needed
2. **Requirements Enrichment Phase** (if needed):
   - Assess context completeness
   - Generate scope-specific questions
   - Present questions with transparency
   - Validate and enrich context
   - Store enriched context
3. **Subagent Discovery Phase** proceeds with enriched context
4. **Documentation Orchestration Phase** receives enriched context in delegation


## BEST PRACTICES

### Question Design
- Start with high-impact questions (business value, users, core requirements)
- Group related questions together
- Keep questions concise and specific
- Avoid technical jargon unless appropriate for user
- Allow partial answers and iteration

### User Experience
- Be transparent about process and time investment
- Respect user's time - keep question count reasonable (5-10 max)
- Allow flexible responses - don't force rigid formats
- Accept "I don't know" or "you decide" for specific questions
- Provide option to skip entire questionnaire

### Context Quality
- Validate understanding after each category
- Document both answers and assumptions clearly
- Distinguish between validated facts and informed assumptions
- Preserve user's exact language for key requirements
- Note areas of uncertainty for subagent attention

### Efficiency
- Skip redundant questions if user already provided answer
- Combine related questions when appropriate
- Don't ask questions answerable from existing documentation
- Terminate early if user requests to skip
- Cache enriched context to avoid re-asking in same session
