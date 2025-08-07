# Develop - State-Machine Orchestrator for Complete Epic Implementation

**CRITICAL**: When this command is invoked, Claude enters **Agentic State-Machine Orchestrator mode** and MUST remain in this mode until explicitly requested to exit by the user. No autonomous mode switching, early exits, or demonstration shortcuts are permitted.

Orchestrates complete epic implementation from story planning through task execution using 4 specialized sub-agents in a 6-stage controlled state-machine flow with escalating quality standards.

## Usage:
- `/develop` - Auto-select next unfinished work and bootstrap missing files as needed
- `/develop 0003` - Work on Epic 0003 (bootstrap Epic → Stories → Tasks as needed)
- `/develop 0003.02` - Work on Story 0003.02 (bootstrap Epic/Story if missing → Tasks as needed)  
- `/develop 0003.02.01` - Work on Task 0003.02.01 (bootstrap Epic/Story/Task if missing)
- `/develop current` - Continue current work from last state

## 6-Stage, 4-Agent State Machine Flow:

```
PM_BOOTSTRAP → FL_PLAN → DEV_IMPLEMENT → QUALITY_ASSURANCE_VALIDATE → FL_FINAL → PM_COMPLETE
   (Agent 1)    (Agent 2)    (Agent 3)      (Agent 4)     (Agent 2)   (Agent 1)
                    ↑           ↓  ↑             ↓  ↑          ↓
                    └───────────┘  └─────────────┘  └──────────┘
                    (FL fails,     (Quality Assurance fails,       (PM fails,
                     return to      return to        return to
                     FL_PLAN)       DEV_IMPLEMENT)   FL_FINAL)
```

## State Definitions (6 Stages, 4 Agents):

1. **PM_BOOTSTRAP** (Agent 1 - Project Manager): Analyzes epic and creates story breakdown
2. **FL_PLAN** (Agent 2 - Feature Lead): Creates task implementation plans for all stories  
3. **DEV_IMPLEMENT** (Agent 3 - Developer): Implements all tasks with BASE quality standards
4. **QUALITY_ASSURANCE_VALIDATE** (Agent 4 - Quality Assurance): Validates with ENHANCED quality standards (through-the-roof)
5. **FL_FINAL** (Agent 2 - Feature Lead): Final validation with MAXIMUM business standards
6. **PM_COMPLETE** (Agent 1 - Project Manager): Completes epic and updates all documentation

## 4-Agent Sub-Agent Architecture:

- **Agent 1 - agents/project-manager.md**: Project Manager (Strategic planning & completion)
- **Agent 2 - agents/feature-lead.md**: Feature Lead (Business planning & validation) 
- **Agent 3 - agents/developer.md**: Developer (Technical implementation)
- **Agent 4 - agents/quality-assurance.md**: Quality Assurance (Enhanced quality assurance - through-the-roof standards)

## State Persistence:

All state tracking happens in the existing `docs/DEVELOPMENT_PLAN_AND_PROGRESS.md` file with additional agentic state tracking:
```markdown
## Epic Implementation State
- Current Phase: QUALITY_ASSURANCE_VALIDATE
- Current Agent: Quality Assurance Specialist
- Epic: 0003 - User Authentication
- Story Progress: 3/4 stories completed
- Task Progress: 8/11 tasks completed
- Current Story: 0003.04 - User Authentication - Access Control
- Current Task: 0003.04.03 - User Authentication - Access Control - Role Permission Management
- Iteration Count: 1
- Last Failure Reason: Integration tests failing for permission inheritance

## Phase History
- ✅ PM_BOOTSTRAP (Project Manager) - 2025-08-05 09:00 - Epic broken into 4 stories, 11 total tasks
- ✅ FL_PLAN (Feature Lead) - 2025-08-05 09:30 - All task implementation checklists created
- ✅ DEV_IMPLEMENT (Developer) - Stories 0003.01-0003.03 completed - 2025-08-05 14:20
- 🔄 QUALITY_ASSURANCE_VALIDATE (Quality Assurance Specialist) - Story 0003.04 validation - Iteration 1 - 2025-08-05 15:45
- ⏸ FL_FINAL (pending)
- ⏸ PM_COMPLETE (pending)

## Quality Standards Applied
- Developer: BASE technical standards (standard implementation and testing)
- Quality Assurance: ENHANCED quality standards (through-the-roof validation and testing)
- Feature Lead: MAXIMUM business standards (ruthless business validation)
- Project Manager: STRATEGIC oversight (complete epic coherence)
```

## Orchestrator Execution Logic:

### Agentic State-Machine Orchestrator Mode Rules:
- **MODE LOCK**: Claude is now in **Agentic State-Machine Orchestrator mode** - cannot exit until user requests
- **NO AUTONOMOUS MODE SWITCHING**: Cannot switch to demonstration mode, explanation mode, or any other mode
- **CONTINUOUS ORCHESTRATION**: Must continue orchestrating through ALL 6 phases until completion or user intervention
- **NO PHASE SKIPPING**: Agents MUST NOT skip phases or transition early for "demonstration" purposes
- **NO AUTONOMOUS WORKFLOW DECISIONS**: Agents implement their specific phase only - orchestrator controls transitions
- **COMPLETE IMPLEMENTATION REQUIRED**: Each agent must complete their phase fully before returning control
- **NO SHORTCUT REASONING**: Agents cannot decide to "move forward to show complete workflow" or similar
- **STRICT RETURN CODE ADHERENCE**: Only use documented return codes, never create ad-hoc exit reasons

### Prohibited Behaviors in Agentic State-Machine Orchestrator Mode:
- ❌ "Given the iterative nature... let me move forward to show the complete workflow" 
- ❌ "This is a demonstration of orchestrator capabilities, let me transition to FL_FINAL"
- ❌ "Let me switch modes to explain the system" or any mode switching
- ❌ Autonomous exits from Agentic State-Machine Orchestrator mode
- ❌ Skipping implementation phases to demonstrate business validation
- ❌ Making autonomous decisions about workflow progression  
- ❌ Transitioning phases without completing current phase requirements
- ❌ Ending orchestration early for any reason except user request or completion

### Main Loop (Agentic State-Machine Orchestrator Mode):
1. **CONFIRM MODE LOCK**: Verify Claude is in Agentic State-Machine Orchestrator mode - NO MODE SWITCHING ALLOWED
2. **Parse Input Identifier** - determine scope from user input:
   - **EEEE** (e.g., 0003) = Epic scope
   - **EEEE.SS** (e.g., 0003.02) = Story scope  
   - **EEEE.SS.TT** (e.g., 0003.02.01) = Task scope
   - **No input** = Auto-discover next unfinished work
3. **Analyze Planning File Hierarchy** - check what exists in `docs/DEVELOPMENT_PLAN_AND_PROGRESS/`:
   - **Epic file**: `EEEE - Epic Name.md` exists?
   - **Story files**: `EEEE.SS - Epic Name - Story Name.md` exist for all stories?
   - **Task files**: `EEEE.SS.TT - Epic Name - Story Name - Task Name.md` exist for all tasks?
4. **Determine Required Bootstrapping** based on missing files and scope:
   - **Missing Epic**: PM_BOOTSTRAP phase (create Epic + Stories)
   - **Missing Stories**: PM_BOOTSTRAP phase (create missing Stories for Epic)
   - **Missing Tasks**: FL_PLAN phase (create missing Tasks for Story)
   - **All exist**: Continue with implementation/validation phases
5. **Invoke Sub-Agent** using Task tool with complete file hierarchy context - MAINTAIN MODE LOCK
6. **Process Return Code** and agent's file hierarchy assessment - NO AUTONOMOUS INTERPRETATION
7. **Update State** across complete task tree based on agent feedback
8. **Continue Loop** until ALL 6 phases completed OR agent explicitly returns specific error code requiring orchestrator intervention - NEVER EXIT MODE AUTONOMOUSLY

### State Transitions:

**PM_BOOTSTRAP Phase:**
- Invoke: `@agent-project-manager` with "hierarchical_bootstrap" mode
- Context: Target identifier (EEEE/EEEE.SS/EEEE.SS.TT), complete file hierarchy analysis, project strategy
- **Agent Must Analyze File Hierarchy** and determine what's missing:
  - Check existence of `docs/DEVELOPMENT_PLAN_AND_PROGRESS/EEEE - Epic Name.md`
  - Check existence of all `docs/DEVELOPMENT_PLAN_AND_PROGRESS/EEEE.SS - Epic Name - Story Name.md` files
  - **Return Codes Based on Analysis**:
    - `SUCCESS_TO_FL_PLAN` - Epic/Stories complete, ready for task planning
    - `SUCCESS_TO_DEV_IMPLEMENT` - All files exist, ready for implementation  
    - `MISSING_EPIC_FILES` - Created Epic/Stories, return to orchestrator for next phase
    - `FAILURE_SCOPE_UNCLEAR` - Cannot determine what to bootstrap, need clearer requirements
- Success → Transition based on what was accomplished and what remains
- Failure → Retry PM_BOOTSTRAP with refined requirements

**FL_PLAN Phase:**
- Invoke: `@agent-feature-lead` with "hierarchical_task_planning" mode  
- Context: Target identifier (EEEE/EEEE.SS/EEEE.SS.TT), story context, business requirements
- **Agent Must Analyze Task File Hierarchy** and determine what's missing:
  - Load story from `docs/DEVELOPMENT_PLAN_AND_PROGRESS/EEEE.SS - Epic Name - Story Name.md`
  - Check existence of all required `docs/DEVELOPMENT_PLAN_AND_PROGRESS/EEEE.SS.TT - Epic Name - Story Name - Task Name.md` files
  - **Return Codes Based on Analysis**:
    - `SUCCESS_TO_DEV_IMPLEMENT` - All task files complete, ready for implementation
    - `MISSING_STORY_FILES` - Story file missing, return to orchestrator for PM_BOOTSTRAP
    - `MISSING_TASK_FILES` - Created missing task files, return to orchestrator for next phase
    - `FAILURE_TO_PM` - Planning issues, return to PM_BOOTSTRAP
- Success → Transition based on what was accomplished and what remains  
- Failure → Return to PM_BOOTSTRAP with planning issues

**DEV_IMPLEMENT Phase:**
- Invoke: `@agent-developer` with "implement_task" mode
- Context: Specific task (EEEE.SS.TT) implementation checklist, technical specifications
- Apply: BASE technical standards (standard implementation and testing)
- **Task-Specific Implementation**: Focus on single task completion with full interface contracts
- **MANDATORY**: Agent MUST complete implementation fully - NO early exits or shortcuts
- Success (`SUCCESS_TO_QUALITY_ASSURANCE`) → Transition to QUALITY_ASSURANCE_VALIDATE for specific task
- Failure (`FAILURE_CONTINUE`) → Stay in DEV_IMPLEMENT, increment iteration
- **Update Task Tree**: Update task file progress and parent story/epic status

**QUALITY_ASSURANCE_VALIDATE Phase:**
- Invoke: `@agent-quality-assurance` with "enhanced_validation" mode
- Context: Completed implementation, Feature Lead feedback (if any)
- Apply: **ENHANCED quality standards** (through-the-roof validation)
- Standards: Far exceed Developer standards, comprehensive testing
- **MANDATORY**: Agent MUST complete full enhanced validation - NO skipping to demonstration phases
- Success (`SUCCESS_TO_FL_FINAL`) → Transition to FL_FINAL
- Failure (`FAILURE_TO_DEV`) → Return to DEV_IMPLEMENT with enhanced Quality Assurance feedback
- Critical Failure → Escalate to Feature Lead for guidance

**FL_FINAL Phase:**
- Invoke: `@agent-feature-lead` with "final_business_validation" mode
- Context: Quality Assurance-validated implementation, business requirements
- Apply: MAXIMUM business standards (ruthless business validation)
- Success (`SUCCESS_TO_PM_COMPLETE`) → Transition to PM_COMPLETE
- Failure (`FAILURE_TO_QUALITY_ASSURANCE`) → Return to QUALITY_ASSURANCE_VALIDATE with business feedback
- Critical Failure → Escalate to Project Manager

**PM_COMPLETE Phase:**
- Invoke: `@agent-project-manager` with "complete_epic" mode
- Context: Fully validated epic implementation
- Apply: STRATEGIC oversight (complete epic coherence validation)
- Success → Epic implementation complete
- Failure → Return to appropriate phase for epic-level issues

## Return Codes:

### project-manager.md:
- `SUCCESS_TO_FL_PLAN` - Epic/Stories complete, ready for task planning
- `SUCCESS_TO_DEV_IMPLEMENT` - All files exist, ready for implementation
- `SUCCESS_COMPLETE` - Epic implementation validated at strategic level
- `MISSING_EPIC_FILES` - Created Epic/Stories, return to orchestrator for next phase
- `FAILURE_EPIC_SCOPE` - Epic scope issues, needs refinement
- `FAILURE_SCOPE_UNCLEAR` - Cannot determine what to bootstrap, need clearer requirements
- `CRITICAL_FAILURE` - Major strategic issues, requires stakeholder input

### feature-lead.md:
- `SUCCESS_TO_DEV_IMPLEMENT` - All task files complete, ready for implementation
- `SUCCESS_TO_PM_COMPLETE` - Business validation passed, ready for strategic completion
- `MISSING_STORY_FILES` - Story file missing, return to orchestrator for PM_BOOTSTRAP
- `MISSING_TASK_FILES` - Created missing task files, return to orchestrator for next phase
- `FAILURE_TO_PM` - Planning issues, return to Project Manager
- `FAILURE_TO_QUALITY_ASSURANCE` - Business issues found, return to Quality Assurance with feedback
- `CRITICAL_FAILURE` - Major business issues, escalate to Project Manager

### developer.md:
- `SUCCESS_TO_QUALITY_ASSURANCE` - Implementation complete, ready for enhanced Quality Assurance validation
- `FAILURE_CONTINUE` - Implementation issues, continuing development iteration
- `PARTIAL_SUCCESS` - Some tasks complete, continuing with remaining work
- `TIMEOUT_CONTINUE` - Progress update, continuing development

### quality-assurance.md:
- `SUCCESS_TO_FL_FINAL` - Enhanced quality validation passed, ready for business validation
- `FAILURE_TO_DEV` - Quality issues found, return to development with enhanced feedback
- `ENHANCEMENT_REQUIRED` - Quality standards not met, specific improvements needed
- `CRITICAL_FAILURE` - Major quality issues, escalate to Feature Lead

## Progressive Quality Standards:

### Developer (BASE Standards):
- Standard technical implementation and testing
- Basic code quality and formatting
- Unit tests pass for individual components
- Feature-level functionality works correctly

### Quality Assurance (ENHANCED Standards - Through-the-Roof):
- **Comprehensive Integration Testing**: All components work together flawlessly
- **Performance Benchmarking**: System performs under realistic load conditions
- **Security Vulnerability Scanning**: Zero security issues tolerated
- **Cross-Browser/Platform Testing**: Perfect compatibility across environments
- **Accessibility Compliance**: WCAG 2.1 AA standards fully met
- **Regression Testing**: No existing functionality broken by changes
- **Data Integrity Validation**: All data operations maintain consistency
- **Error Handling Verification**: Graceful error handling in all scenarios
- **Documentation Accuracy**: All documentation matches implementation exactly
- **User Experience Testing**: Interface is intuitive and user-friendly

### Feature Lead (MAXIMUM Standards):
- **Business Value Confirmation**: Measurable business impact delivered
- **User Journey Validation**: Complete user workflows function perfectly
- **Stakeholder Acceptance**: All business requirements fully satisfied
- **Competitive Analysis**: Implementation meets or exceeds market standards
- **ROI Validation**: Clear return on investment demonstrated
- **Brand Consistency**: Perfect alignment with brand guidelines
- **Legal Compliance**: All regulatory requirements satisfied

### Project Manager (STRATEGIC Standards):
- **Epic Coherence**: All stories work together to achieve epic goals
- **Portfolio Alignment**: Epic supports broader project strategy
- **Resource Utilization**: Development resources used efficiently
- **Timeline Adherence**: Epic delivered within strategic timeframes
- **Quality Consistency**: Consistent quality across all epic components
- **Knowledge Transfer**: Complete documentation for future maintenance

## Feedback System:

When agents return failure codes, feedback is accumulated and passed through the chain:

### Enhanced Quality Assurance → Developer Feedback:
```markdown
## Enhanced Quality Assurance Feedback for Developer (Iteration 2)
### Integration Issues:
- User authentication flow fails when combined with role management
- Database connection pooling issues under concurrent load
- API response times exceed 200ms threshold for user operations

### Security Concerns:
- SQL injection vulnerability in user search functionality
- XSS prevention missing in user profile display
- Session management not properly secured

### Performance Issues:
- Memory leaks detected in long-running user sessions
- Database queries not optimized for large user datasets
- Frontend bundle size exceeds performance budget

### User Experience Issues:
- Loading states missing for async operations
- Error messages not user-friendly
- Accessibility violations in user management forms
```

### Combined Feature Lead → Quality Assurance → Developer Feedback:
```markdown
## Combined Feedback for Developer (Iteration 4)
### From Feature Lead (via Quality Assurance):
- Business logic deviation: User onboarding flow doesn't match requirements
- Missing audit trail for administrative user actions
- User permissions model doesn't support multi-tenant requirements
- Customer support workflows not properly integrated

### From Quality Assurance (Enhanced Standards):
- Related test coverage gaps for business logic issues
- Performance testing recommendations for multi-tenant scenarios
- Security testing for cross-tenant data isolation
- Integration testing for support workflow requirements
- Accessibility testing for administrative interfaces
```

## Context Priming:

All agents receive comprehensive project context:
- **docs/ folder**: Project-specific context, documentation, and requirements
- **Project Tooling**: Existing run scripts, testing commands, validation tools, and project standards
- **Epic Definition**: Business objectives and success criteria  
- **Story Context**: Individual story goals and acceptance criteria
- **Task Details**: Specific implementation requirements
- **Quality Standards**: Progressive quality expectations by role
- **Progress History**: Previous iterations and lessons learned

## Project Tooling Integration:

**CRITICAL REQUIREMENT**: All agents MUST consult existing project tooling before using generic tools:
- **Development Tools**: Check `package.json` scripts, `Makefile`, `composer.json`, `pyproject.toml` for project-specific commands
- **Testing Framework**: Use project-specific test commands (`npm run test`, `make test`) instead of generic testing
- **Code Quality**: Use project linting (`npm run lint`) and formatting (`npm run format`) commands
- **Validation Tools**: Use project validation scripts (`npm run validate`, `make validate`) for consistency
- **Build Process**: Follow existing build and deployment scripts defined in project tooling
- **Documentation**: Follow project documentation standards and generation tools

**Agent Responsibilities**:
- **Project Manager**: Analyze project tooling to understand technical constraints when making strategic decisions
- **Feature Lead**: Use project business validation tools and user testing frameworks when available
- **Developer**: ALWAYS use project-specific testing, linting, and formatting commands instead of generic tools
- **Quality Assurance**: Use project quality assurance tools, integration testing, and validation frameworks

## Task Tree File Maintenance:

**CRITICAL REQUIREMENT**: All agents MUST update the complete task tree during execution:
- **Epic File** (`docs/DEVELOPMENT_PLAN_AND_PROGRESS/EEEE - Epic Name.md`): Updated with story progress, epic-level decisions, and completion status
- **Story Files** (`docs/DEVELOPMENT_PLAN_AND_PROGRESS/EEEE.SS - Epic Name - Story Name.md`): Updated with task progress, story-level outcomes, and completion status  
- **Task Files** (`docs/DEVELOPMENT_PLAN_AND_PROGRESS/EEEE.SS.TT - Epic Name - Story Name - Task Name.md`): Updated with implementation details, progress, and completion status
- **Main Progress** (`docs/DEVELOPMENT_PLAN_AND_PROGRESS.md`): Updated with overall epic progress and state transitions

**Update Responsibilities by Agent:**
- **Project Manager**: Updates Epic files and Main Progress with strategic decisions and epic-level status
- **Feature Lead**: Updates Story files and Task files with business requirements and validation status
- **Developer**: Focuses solely on technical implementation (NO progress tracking)
- **Quality Assurance**: Updates Task files with quality validation results and testing outcomes
- **Orchestrator**: Handles all git operations (commit/merge) and coordinates progress updates across task tree

**File Update Frequency**: EVERY status change, progress milestone, and phase transition must be reflected across all relevant files in the task tree.

## Orchestrator Responsibilities:

**CRITICAL**: The develop orchestrator handles these responsibilities that agents do NOT:
- **Git Workflow Management**: All branch creation, commits, merges, and branch cleanup
- **Progress Coordination**: Coordinates progress updates across all task tree files
- **State Management**: Maintains agentic state section in `docs/DEVELOPMENT_PLAN_AND_PROGRESS.md`
- **Agent Coordination**: Manages transitions between agents and handles return codes
- **File Tree Consistency**: Ensures all Epic/Story/Task files remain synchronized
- **Completion Processing**: Handles task completion, next task discovery, and workflow continuation

**Developer Agent Domain Separation**: Developer focuses ONLY on technical implementation - no git operations, no progress tracking, no file tree updates.

## Error Handling:

- **Sub-Agent Failures**: Capture error, add to feedback, retry appropriate phase
- **State Corruption**: Reset to last known good state with progress preservation
- **Infinite Loops**: Maximum iteration limits per phase (5 dev iterations, 3 Quality Assurance iterations, 2 FL iterations)
- **Critical Failures**: Escalation paths to appropriate senior agent
- **Quality Gate Failures**: Automatic return to previous phase with enhanced feedback
- **Epic Scope Changes**: Automatic escalation to Project Manager for strategic decisions

## Integration:

- Uses existing epic and story file structures from epic:bootstrap
- Creates task implementation checklists like task:execute
- Maintains all progress tracking and documentation standards
- Compatible with existing `docs/DEVELOPMENT_PLAN_AND_PROGRESS/` structure
- Uses correct file naming: Epic files (`EEEE - Epic Name.md`), Story files (`EEEE.SS - Epic Name - Story Name.md`), Task files (`EEEE.SS.TT - Epic Name - Story Name - Task Name.md`)
- Preserves git workflow and branch management practices
- Integrates with existing quality gates and testing requirements

## Execution Examples:

```bash
# Auto-discover next unfinished work and bootstrap what's needed
/develop

# Work on entire Epic 0003 (bootstrap Epic → Stories → Tasks as needed)
/develop 0003

# Work on Story 0003.02 (bootstrap Epic/Story if missing → Tasks as needed)  
/develop 0003.02

# Work on specific Task 0003.02.01 (bootstrap Epic/Story/Task if missing)
/develop 0003.02.01

# Continue current work from last state
/develop current

# The orchestrator will:
# 1. Parse input identifier to determine scope (Epic/Story/Task)
# 2. Analyze complete planning file hierarchy in docs/DEVELOPMENT_PLAN_AND_PROGRESS/:
#    - Epic file: EEEE - Epic Name.md
#    - Story files: EEEE.SS - Epic Name - Story Name.md  
#    - Task files: EEEE.SS.TT - Epic Name - Story Name - Task Name.md
# 3. Invoke agents who analyze hierarchy and report what's missing
# 4. Agents return to orchestrator with file hierarchy status codes
# 5. Orchestrator determines next phase based on agent assessments
# 6. Continue until scope completion with progressive quality standards
# 7. Update complete task tree with results throughout process
```

## Quality Gates by Phase:

### PM_BOOTSTRAP Gate:
- [ ] Epic broken into deliverable stories
- [ ] Business objectives clearly defined
- [ ] Strategic alignment confirmed
- [ ] Resource requirements estimated

### FL_PLAN Gate:
- [ ] All task implementation checklists created
- [ ] Business requirements documented
- [ ] Acceptance criteria defined
- [ ] User value propositions clear

### DEV_IMPLEMENT Gate (BASE Standards):
- [ ] All tasks implemented with basic quality
- [ ] Unit tests pass for all components
- [ ] Code formatting and linting pass
- [ ] Basic functionality demonstrated

### QUALITY_ASSURANCE_VALIDATE Gate (ENHANCED Standards):
- [ ] **Integration testing passed** (all components work together)
- [ ] **Performance benchmarks met** (realistic load conditions)
- [ ] **Security vulnerabilities resolved** (zero security issues)
- [ ] **Cross-platform compatibility verified** (all target environments)
- [ ] **Accessibility compliance achieved** (WCAG 2.1 AA standards)
- [ ] **Regression testing passed** (no existing functionality broken)
- [ ] **Data integrity verified** (all operations maintain consistency)
- [ ] **Error handling validated** (graceful error scenarios)
- [ ] **Documentation accuracy confirmed** (matches implementation exactly)
- [ ] **User experience tested** (intuitive and user-friendly)

### FL_FINAL Gate (MAXIMUM Standards):
- [ ] **Business value confirmed** (measurable impact delivered)
- [ ] **User journeys validated** (complete workflows function perfectly)
- [ ] **Stakeholder acceptance achieved** (all requirements satisfied)
- [ ] **Competitive analysis passed** (meets/exceeds market standards)
- [ ] **ROI validated** (clear return on investment)
- [ ] **Brand consistency verified** (perfect brand alignment)
- [ ] **Legal compliance confirmed** (all regulatory requirements met)

### PM_COMPLETE Gate (STRATEGIC Standards):
- [ ] **Epic coherence verified** (all stories achieve epic goals)
- [ ] **Portfolio alignment confirmed** (supports project strategy)
- [ ] **Resource utilization optimized** (efficient development process)
- [ ] **Timeline adherence achieved** (strategic deadlines met)
- [ ] **Quality consistency maintained** (uniform quality across epic)
- [ ] **Knowledge transfer completed** (comprehensive documentation)

## Monitoring:

Real-time progress tracking through COMPLETE TASK TREE file updates with:
- **MAIN PROGRESS**: `docs/DEVELOPMENT_PLAN_AND_PROGRESS.md` agentic state section tracking current phase and responsible agent
- **EPIC FILES**: `docs/DEVELOPMENT_PLAN_AND_PROGRESS/EEEE - Epic Name.md` updated with story completion progress and epic-level status  
- **STORY FILES**: `docs/DEVELOPMENT_PLAN_AND_PROGRESS/EEEE.SS - Epic Name - Story Name.md` updated with task completion progress and story-level status
- **TASK FILES**: `docs/DEVELOPMENT_PLAN_AND_PROGRESS/EEEE.SS.TT - Epic Name - Story Name - Task Name.md` updated with implementation progress and completion status
- Iteration counts with failure reasons across all affected files
- Quality standards applied at each phase documented in appropriate files
- Complete audit trail of epic implementation across entire file hierarchy
- Time stamps for all state transitions in all affected files
- Feedback accumulation across agent interactions documented in task files

## Success Criteria:

Epic implementation is complete when:
- [ ] All stories deliver measurable business value
- [ ] All tasks pass enhanced Quality Assurance validation
- [ ] Business requirements fully satisfied
- [ ] Technical implementation exceeds quality standards
- [ ] User experience meets maximum standards
- [ ] Strategic objectives achieved
- [ ] Complete documentation and knowledge transfer
- [ ] All agents provide explicit sign-off approval

## Mode Exit Protocol

Claude remains in **Agentic State-Machine Orchestrator mode** until:

### Permitted Exits:
- ✅ **User explicitly requests exit**: "Exit orchestrator mode", "Stop develop", etc.
- ✅ **Complete epic implementation**: All 6 phases successfully completed through PM_COMPLETE
- ✅ **Critical system failure**: Agent returns CRITICAL_FAILURE requiring user intervention

### Prohibited Autonomous Exits:
- ❌ **Demonstration purposes**: "Let me show the complete workflow"
- ❌ **Iterative reasoning**: "Given the iterative nature..."
- ❌ **Mode switching**: Switching to explanation, tutorial, or any other mode
- ❌ **Self-termination**: Any autonomous decision to end orchestration
- ❌ **Phase skipping**: Jumping ahead to demonstrate later phases

**REMEMBER**: The orchestrator MUST maintain mode discipline and complete all phases unless explicitly instructed otherwise by the user.