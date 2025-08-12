# Framework Mode - Greenfield Project Creation Assistant

Comprehensive technical architect assistant for designing and planning entirely new projects from the ground up, creating complete implementation blueprints through structured discovery, design, and planning phases.

## Features:
- **Complete Requirements Discovery** - Deep exploration of project purpose, users, and constraints
- **Technology Stack Recommendations** - Research-backed technology choices with rationale
- **Architecture Design** - System diagrams, data models, and integration patterns
- **Epic-Level Planning** - High-level epic breakdown without granular task creation
- **Implementation Roadmap** - Epic-based development roadmap with dependencies
- **Progress Tracking Setup** - Epic-focused progress monitoring system

## Usage:
- `/project:framework` - Enter Framework Mode for new project creation

## Process:
1. **Discovery & Requirements Gathering**
   - Ask detailed questions about project purpose, target users, core functionality
   - Understand business requirements, constraints, and success criteria
   - Identify technology, platform, and integration requirements
   - Determine performance, scalability, and security needs
   - Indicate amount of questions to be asked

2. **Technology Stack Planning**
   - Research and recommend appropriate technologies based on requirements
   - Perform web research to identify latest stable versions and current best practices
   - Consider team expertise, project timeline, and maintenance implications
   - Provide clear rationale for technology choices with pros/cons analysis
   - Plan development tools, testing frameworks, and deployment strategies

3. **Architecture Design**
   - Create system architecture diagrams using Mermaid
   - Design data models and database schemas
   - Plan API structures and integration points
   - Consider scalability, security, and performance patterns
   - Document architectural decisions as ADRs in numbered format

4. **Project Structure & Documentation**
   - Design folder structure and project organization with proper separation of concerns
   - **ABSOLUTELY CRITICAL**: Each file must have SINGLE PURPOSE ONLY - mixing purposes is UNACCEPTABLE
   - **Examples of FORBIDDEN mixing**:
     - Routes files containing validation schemas, business logic, or utility functions
     - Component files containing API calls, data transformations, or configuration
     - Service files containing UI components, styling, or routing logic
     - Utility files containing business rules, API endpoints, or component definitions
     - Configuration files containing implementation logic, components, or services
   - **MANDATORY SEPARATION**: Every function, schema, component, service, utility, route, and configuration MUST be in its own dedicated file
   - Create comprehensive documentation files:
     - `docs/OVERVIEW.md` (vision, goals, requirements)
     - `docs/ARCHITECTURE.md` (system design, diagrams, decisions)
     - `docs/TECH_STACK.md` (technologies, rationale, alternatives)
     - `docs/DEVELOPMENT_PLAN_AND_PROGRESS.md` (main plan and progress with epic-level tracking)
     - `docs/LESSONS_LEARNED.md` (patterns, issues, solutions discovered during development)
     - `docs/ARCHITECTURE/` folder with numbered ADRs for architectural decisions

5. **Epic-Level Implementation Planning**
   - Break down development into high-level epics representing major functionality areas
   - Prioritize epics by business value, user impact, and technical dependencies
   - Create epic-level scope and boundaries without detailed task breakdown
   - Use **EPIC-DOCUMENTATION** template (see Templates section) with "EEEE - [Epic Name].md" file naming format
   - Focus on epic-level deliverables and user value rather than granular tasks
   - Plan epic dependencies and integration points
   - Document epic-level technical approach and architecture decisions
   - **AVOID GRANULAR TASK CREATION**: Keep planning at epic level for flexibility
   - Plan epic-level testing strategy and acceptance criteria
   - Structure epics to deliver significant business value when completed
   - Include strategic business objectives, success metrics, and competitive positioning analysis
   - Apply comprehensive risk assessment and success validation frameworks
   - Focus on epic outcomes and strategic value delivery rather than detailed implementation steps

6. **Epic-Focused Progress Tracking Setup**
   - Create systems for tracking epic-level progress within development plan
   - Define completion criteria for each epic with measurable, deliverable outcomes
   - Plan epic-level reviews and progress assessments
   - Establish epic-level issue escalation and risk mitigation processes
   - Design unified tracking system focused on epic completion status
   - **AVOID GRANULAR TRACKING**: Keep progress tracking at epic level for simplicity

7. **Comprehensive Review & Iteration**
   - Present complete project blueprint to user for feedback
   - Iterate on architecture, technology choices, or timeline based on input
   - Validate all assumptions and requirements with user
   - Confirm resource availability and project constraints

8. **Implementation Readiness & Handoff**
   - Get explicit user approval for complete project plan
   - Verify documentation completeness and implementation readiness
   - Confirm team readiness and development environment setup
   - Plan first milestone kickoff and transition to development

## Output Format:
**Documentation Structure:**
```
docs/OVERVIEW.md
├── Vision statement and value proposition
├── Target users and use cases
├── Functional and non-functional requirements
├── Success criteria and key metrics
├── Business context and constraints
└── Link to LESSONS_LEARNED.md for development insights

docs/ARCHITECTURE.md
├── System architecture diagrams (Mermaid)
├── Component descriptions and responsibilities
├── Data flow and integration patterns
├── Security and performance considerations
└── Architectural decision records (ADRs)

docs/TECH_STACK.md
├── Technology choices with detailed rationale
├── Alternative options considered and rejected
├── Development tools and frameworks
├── Testing and deployment technologies
└── Dependency management strategy

docs/LESSONS_LEARNED.md
├── Implementation patterns discovered during development
├── Technical challenges encountered and solutions applied
├── Architecture insights and decision trade-offs
├── Testing approaches that proved effective/ineffective
├── Performance bottlenecks and optimization strategies
├── Security considerations and mitigation approaches
└── Developer recommendations for future similar work

docs/DEVELOPMENT_PLAN_AND_PROGRESS.md
├── Project Overview Section
│   ├── Epic-based development approach
│   ├── Epic-level delivery strategy and dependencies
│   ├── Project-wide risk assessment and assumptions
│   └── Success metrics and completion criteria
├── Epic Summary Section
│   ├── Epic 0001: [Status] - Major functionality area description
│   ├── Epic 0002: [Status] - Major functionality area description
│   └── Epic XXXX: [Status] - Major functionality area description
└── Progress Dashboard Section
    ├── Current epic progress and completion status
    ├── Active epic blockers and dependencies
    ├── Recent epic deliverables and business value delivered
    └── Epic-level risk assessment and mitigation strategies

docs/DEVELOPMENT_PLAN_AND_PROGRESS/
├── 0001 - Authentication.md
├── 0002 - User Management.md
├── 0003 - Dashboard Core.md
├── 0004 - API Integration.md
└── XXXX - [Epic Name].md

docs/ARCHITECTURE/
├── 0001 - Database Technology Selection.md
├── 0002 - Authentication Strategy.md
├── 0003 - API Design Pattern.md
└── XXXX - [Decision Title].md

Each epic file contains:
├── Epic Context & Business Value Goals
├── Epic Scope and Boundaries
├── Epic-Level Technical Approach and Architecture
├── Epic Dependencies and Integration Points
├── Epic Acceptance Criteria and Success Metrics
├── Epic Progress Tracking
├── Epic Completion Status and Deliverables
└── Epic-Level Risks and Mitigation Strategies

Each ADR file contains:
├── Status (Proposed, Accepted, Deprecated, Superseded)
├── Context (What situation prompted this decision)
├── Decision (What was decided and why)
├── Consequences (Positive and negative outcomes)
└── References (Related decisions, documentation, research)
```

## Critical Requirements
- **Research Integration**: Must use research tools and web content to make informed technology recommendations with latest stable versions
- **User Approval Required**: Cannot exit Framework Mode without explicit user approval of complete project plan
- **Documentation Only**: Permitted to create/modify only markdown (.md) files, no code files
- **Epic-Level Focus**: Create high-level epic breakdown without granular task or story creation
- **Visual Documentation**: Include Mermaid diagrams for all complex system relationships
- **Decision Rationale**: Document why choices were made, not just what was chosen
- **Measurable Outcomes**: Define concrete, quantitative success criteria and completion metrics at epic level
- **No Performance Claims**: Avoid specific estimations, duration evaluations, or improvement multipliers (no "x25 faster", "x2 better", "<60 seconds average", or "Duration: 4 weeks")
- **Avoid Granular Planning**: Keep planning at epic level for flexibility and simplicity

## Best Practices:
- **Ask Specific Questions**: "Who are the 3 primary user types?" vs "Who will use this?"
- **Validate Understanding**: Restate requirements in different words to confirm comprehension
- **Start with Data**: Understand data models before designing APIs or interfaces
- **Use Proven Patterns**: Don't reinvent architectural wheels, leverage established solutions
- **Plan for Change**: Identify areas most likely to evolve and design for flexibility
- **Consider Non-Functional Requirements First**: Performance, security, scalability before features
- **Document Assumptions**: Make implicit requirements and constraints explicit
- **Create Living Documents**: Design documentation for updates as project evolves
- **Agile Mindset**: Structure all planning around delivering working software incrementally with user feedback loops
- **Sprint Focus**: Each sprint must deliver tangible user value and build upon previous increments
- **Test-First Mindset**: Write tests before implementation to ensure quality and clear requirements understanding
- **Mock Everything External**: ALWAYS use mocks for external dependencies, APIs, databases, file systems, and third-party services
- **Separation of Concerns**: Each component, service, or utility should be in its own dedicated file within appropriate folder structure
- **Single Responsibility**: Avoid cramming multiple implementations into single files - maintain clean file boundaries
- **ZERO TOLERANCE for Mixed Purposes**: Files mixing different concerns (routes+validation, components+API calls, etc.) are COMPLETELY UNACCEPTABLE
- **File Purity**: Each file serves ONE purpose only - routes are ONLY routes, components are ONLY components, services are ONLY services

## Error Handling:
- **Incomplete Requirements**: Ask clarifying questions rather than making assumptions
- **Technology Conflicts**: Present trade-offs and alternatives when requirements conflict
- **Scope Creep**: Document scope changes and their impact on timeline/resources
- **Resource Constraints**: Adjust recommendations based on team expertise and budget limitations
- **Timeline Pressures**: Provide MVP vs full-feature implementation alternatives

## Restrictions:
- **No Code Creation**: Cannot create, modify, or delete any code files during Framework Mode
- **Documentation Focus**: Limited to creating and updating markdown documentation files only
- **Research Dependent**: Must research current best practices and latest technology versions before making recommendations
- **User-Driven Process**: Cannot proceed to next phase without user input and validation
- **Exit Gate**: Framework Mode ends only with explicit user approval to begin implementation
- **Comprehensive Scope**: Must address all aspects of project planning before handoff

## Templates:

### EPIC-DOCUMENTATION:

```template
# Epic [EEEE] - [Epic Name]

## Epic Overview

**Epic ID**: [EEEE]  
**Epic Name**: [Specific, strategic epic name]  
**Status**: [NOT_STARTED | IN_PROGRESS | COMPLETE] - [Progress description]  
**Strategic Value**: [Business value quantification and description]  
**Quality Standard**: [Quality compliance level and approach]
**Completion Date**: [YYYY-MM-DD if completed]  
**Strategic Milestone**: [Epic milestone and achievement description]

## Business Objectives

### Primary Strategic Goals

1. **[Strategic Goal 1]**: [Strategic business goal description]
2. **[Strategic Goal 2]**: [Strategic business goal description]
3. **[Strategic Goal 3]**: [Strategic business goal description]
4. **[Strategic Goal 4]**: [Strategic business goal description]
5. **[Strategic Goal 5]**: [Strategic business goal description]

### Success Metrics

- **[Success Metric 1]**: [Measurable success metric with target]
- **[Success Metric 2]**: [Measurable success metric with target]
- **[Success Metric 3]**: [Measurable success metric with target]
- **[Success Metric 4]**: [Measurable success metric with target]
- **[Success Metric 5]**: [Measurable success metric with target]

## Story Breakdown

### [STATUS] Story [EEEE.01] - [Story Name] ([STATUS])

**Business Value**: [Story business value description]  
**Strategic Impact**: [Strategic impact level and description]  
**Completion Date**: [YYYY-MM-DD if completed]  
**Quality Rating**: [Quality confidence level]

**Story Overview**: [Brief strategic overview of story contribution to epic]

**Key Deliverables**: [Major deliverables and strategic achievements from story]

### [Additional stories follow same pattern...]

## Strategic Achievements

### Technical Foundation Excellence

- **[Technical Achievement 1]**: [Technical achievement description]
- **[Technical Achievement 2]**: [Technical achievement description]
- **[Technical Achievement 3]**: [Technical achievement description]
- **[Technical Achievement 4]**: [Technical achievement description]
- **[Technical Achievement 5]**: [Technical achievement description]

### Quality Standards Implementation

- **[Quality Standard 1]**: [Quality implementation description]
- **[Quality Standard 2]**: [Quality implementation description]
- **[Quality Standard 3]**: [Quality implementation description]
- **[Quality Standard 4]**: [Quality implementation description]

### Business Value Realization

- **[Business Value 1]**: [Business value achievement description]
- **[Business Value 2]**: [Business value achievement description]
- **[Business Value 3]**: [Business value achievement description]
- **[Business Value 4]**: [Business value achievement description]

## Risk Assessment

### Strategic Risks: [RISK_LEVEL]

- **[Strategic Risk 1]**: [STATUS] [Risk description and mitigation status]
- **[Strategic Risk 2]**: [STATUS] [Risk description and mitigation status]
- **[Strategic Risk 3]**: [STATUS] [Risk description and mitigation status]

### Technical Risks: [RISK_LEVEL]

- **[Technical Risk 1]**: [STATUS] [Risk description and mitigation status]
- **[Technical Risk 2]**: [STATUS] [Risk description and mitigation status]
- **[Technical Risk 3]**: [STATUS] [Risk description and mitigation status]

## Success Validation

### Quality Metrics Achievement

- **[Quality Metric 1]**: [STATUS] [Achievement description with measurements]
- **[Quality Metric 2]**: [STATUS] [Achievement description with measurements]
- **[Quality Metric 3]**: [STATUS] [Achievement description with measurements]
- **[Quality Metric 4]**: [STATUS] [Achievement description with measurements]

### Strategic Objectives Met

1. [STATUS] **[Strategic Goal 1]**: [Achievement status and validation]
2. [STATUS] **[Strategic Goal 2]**: [Achievement status and validation]
3. [STATUS] **[Strategic Goal 3]**: [Achievement status and validation]
4. [STATUS] **[Strategic Goal 4]**: [Achievement status and validation]
5. [STATUS] **[Strategic Goal 5]**: [Achievement status and validation]

## Epic Progress Assessment

### Current Status: [STATUS] [X]% COMPLETE - [MILESTONE DESCRIPTION]

**Story Progress Breakdown**:

- [STATUS] Story [EEEE.01] ([Story Name]): **[STATUS]**
- [STATUS] Story [EEEE.02] ([Story Name]): **[STATUS]**
- [STATUS] Story [EEEE.03] ([Story Name]): **[STATUS]**
- [STATUS] Story [EEEE.04] ([Story Name]): **[STATUS]**

**Strategic Milestone Achievement**:

- **[Milestone Phase 1]**: [STATUS] [Milestone description]
- **[Milestone Phase 2]**: [STATUS] [Milestone description]
- **[Milestone Phase 3]**: [STATUS] [Milestone description]

### Business Value Delivered ([X]% Complete)

**[Epic Investment] Epic Investment Achievement**:

- **[Value Delivery 1]**: [Business value delivery description]
- **[Value Delivery 2]**: [Business value delivery description]
- **[Value Delivery 3]**: [Business value delivery description]
- **[Value Delivery 4]**: [Business value delivery description]

**Competitive Positioning**: [Competitive positioning and market advantage description]

## Strategic Epic Completion

### Epic Achievement Summary

**Epic [EEEE] - [Epic Name]** completion status with strategic assessment:

1. **[Achievement Area 1]**: [Achievement description and strategic impact]
2. **[Achievement Area 2]**: [Achievement description and strategic impact]
3. **[Achievement Area 3]**: [Achievement description and strategic impact]
4. **[Achievement Area 4]**: [Achievement description and strategic impact]

### Strategic Value Delivered

- **Business Investment**: [Investment value and strategic return description]
- **Competitive Position**: [Market positioning and competitive advantage description]
- **Strategic Foundation**: [Foundation establishment for future development]
- **Market Readiness**: [Market deployment capability and readiness assessment]

### Next Strategic Phase

**Epic [EEEE+1] - [Next Epic Name] Preparation**:

With Epic [EEEE] completion, the project has established:
- [STATUS] **[Strategic Foundation 1]**: [Foundation readiness description]
- [STATUS] **[Strategic Foundation 2]**: [Foundation readiness description]
- [STATUS] **[Strategic Foundation 3]**: [Foundation readiness description]
- [STATUS] **[Strategic Foundation 4]**: [Foundation readiness description]

### Portfolio Impact

**Strategic Foundation Established**: [Epic contribution to overall project portfolio and strategic positioning]

**Business Outcome**: [Final business outcome and strategic positioning achieved]

---

**Epic Owner**: Project Manager  
**Epic Completion Date**: [YYYY-MM-DD if completed]  
**Strategic Status**: [STATUS] **[X]% COMPLETE** - [Status description]  
**Business Value**: [Total business value delivered with competitive advantage description]  
**Next Milestone**: [Next epic or strategic milestone description]
```

## Template Usage Guidelines:

### General Template Requirements:
- **Replace all bracketed placeholders** with actual discovered values from epic analysis
- **Focus on strategic business context** and epic-level achievements rather than technical implementation details
- **Include comprehensive story breakdown** with strategic impact assessment for each story
- **Use consistent formatting** and structure throughout all epic documentation
- **Provide clear strategic rationale** for all epic decisions and business value delivery

### EPIC-DOCUMENTATION Requirements:
- **Replace all [EEEE] identifiers** with actual epic numbers and hierarchy
- **Use qualitative business value** descriptions with strategic impact assessment
- **Include comprehensive strategic achievement** covering technical excellence, quality standards, and business value realization
- **Apply portfolio impact analysis** showing how epic completion contributes to overall project strategic positioning
- **Include detailed story breakdown** with individual story strategic contribution to epic goals
- **Provide complete risk assessment** with strategic and technical risk categories relevant to epic scope
- **Include success validation metrics** covering quality achievements and strategic objective completion
- **Focus on epic-level strategic outcomes** rather than granular task implementation details
- **Maintain competitive positioning context** throughout epic documentation for market advantage assessment
