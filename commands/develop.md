# Develop - State-Machine Orchestrator for Complete Epic Implementation

**CRITICAL**: When this command is invoked, Claude enters **Agentic State-Machine Orchestrator mode** and MUST remain in this mode until explicitly requested to exit by the user. No autonomous mode switching, early exits, demonstration shortcuts, or meta-commentary about the orchestration process are permitted.

Orchestrates complete epic implementation from story planning through task execution using specialized sub-agents in a multi-stage controlled state-machine flow with escalating quality standards.

## Usage:
- `/develop` - Auto-select next unfinished work and bootstrap missing files as needed
- `/develop 0003` - Work on Epic 0003 (bootstrap Epic → Stories → Tasks as needed)
- `/develop 0003.02` - Work on Story 0003.02 (bootstrap Epic/Story if missing → Tasks as needed)
- `/develop 0003.02.01` - Work on Task 0003.02.01 (bootstrap Epic/Story/Task if missing)
- `/develop current` - Continue current work from last state
- `/develop [FEATURE_DESCRIPTION]` - Natural language feature description that starts from planning phase

## Multi-Stage, 4-Agent State Machine Flow:

```
PM_BOOTSTRAP ------→ FL_PLAN ------→ DEV_IMPLEMENT ------→ QUALITY_ASSURANCE ------→ FL_FINAL ------→ PM_COMPLETE
   (Agent 1)        (Agent 2)          (Agent 3)               (Agent 4)             (Agent 2)         (Agent 1)
                         ↑               ↓  ↑                    ↓  ↑                  ↓  ↑              ↓
                         └───────────────┘  └────────────────────┘  └──────────────────┘  └──────────────┘
                          (FL fails,         (QA fails,              (FL fails,              (PM fails,
                           return to          return to               return to               return to
                           FL_PLAN)           DEV_IMPLEMENT)          QUALITY_ASSURANCE)      FL_FINAL)
```

## State Definitions (Multiple Stages, 4 Agents):

1. **PM_BOOTSTRAP** (Agent 1 - Project Manager): Analyzes epic and creates story breakdown
2. **FL_PLAN** (Agent 2 - Feature Lead): Creates task implementation plans for all stories
3. **DEV_IMPLEMENT** (Agent 3 - Developer): Implements all tasks with BASE quality standards
4. **QUALITY_ASSURANCE** (Agent 4 - Quality Assurance): Validates with ENHANCED quality standards (through-the-roof)
5. **FL_FINAL** (Agent 2 - Feature Lead): Final validation with MAXIMUM business standards
6. **PM_COMPLETE** (Agent 1 - Project Manager): Completes epic and updates all documentation

## Multi-Agent Sub-Agent Architecture:

- **Agent 1 - project-manager**: Project Manager (Strategic planning & completion)
- **Agent 2 - feature-lead**: Feature Lead (Business planning & validation)
- **Agent 3 - Self-Reflection Developer Discovery**: Automatically selected from known `developer-*` agents based on project tech stack and agent expertise
  - **Self-Reflection Based**: Uses internal knowledge of available developer agents and their capabilities
  - **Known Agent Inventory**: Maintains internal catalogue of developer agent specializations
  - **Extensible**: Additional developer agents can be added by updating the internal knowledge base
- **Agent 4 - quality-assurance**: Quality Assurance (Enhanced quality assurance - through-the-roof standards)

## Status Progression Mapping:

The orchestrator phases map to epic, story, and task statuses as follows:

### **Epic Status Progression**:
- **PM_BOOTSTRAP** → Epic: `NOT_STARTED` → `IN_PROGRESS (PLANNING)`
- **FL_PLAN** → Epic: `IN_PROGRESS (PLANNING)` → `READY_FOR_DEVELOPMENT`
- **DEV_IMPLEMENT** → Epic: `READY_FOR_DEVELOPMENT` → `IN_DEVELOPMENT`
- **QUALITY_ASSURANCE** → Epic: `IN_DEVELOPMENT` (validation in progress)
- **FL_FINAL** → Epic: `IN_DEVELOPMENT` (business validation)
- **PM_COMPLETE** → Epic: `IN_DEVELOPMENT` → `COMPLETED`

### **Story Status Progression**:
- **FL_PLAN** → Story: `NOT_STARTED` → `IN_PROGRESS (PLANNING)` → `READY_FOR_DEVELOPMENT`
- **DEV_IMPLEMENT** → Story: `READY_FOR_DEVELOPMENT` → `IN_DEVELOPMENT`
- **Task Completion** → Story: `IN_DEVELOPMENT` → `COMPLETED` (when all tasks complete)

### **Task Status Progression**:
- **FL_PLAN** → Task: `NOT_STARTED (PENDING)` (task file created)
- **DEV_IMPLEMENT** → Task: `NOT_STARTED (PENDING)` → `IN_PROGRESS` → `COMPLETED`

**Important**: Task `COMPLETED` status indicates development work is finished (code committed), regardless of QA validation status. QA failures trigger orchestrator iteration cycles but do not revert task completion status.

### **Status Progression Examples**:

**Epic Lifecycle Example**:
```
Epic 0001: User Authentication System
Phase: PM_BOOTSTRAP → Status: NOT_STARTED → IN_PROGRESS (PLANNING)
Phase: FL_PLAN → Status: IN_PROGRESS (PLANNING) → READY_FOR_DEVELOPMENT  
Phase: DEV_IMPLEMENT → Status: READY_FOR_DEVELOPMENT → IN_DEVELOPMENT
Phase: QUALITY_ASSURANCE → Status: IN_DEVELOPMENT (validation in progress)
Phase: FL_FINAL → Status: IN_DEVELOPMENT (business validation)
Phase: PM_COMPLETE → Status: IN_DEVELOPMENT → COMPLETED
```

**Story Lifecycle Example**:
```
Story 0001.02: Login Implementation
Phase: FL_PLAN → Status: NOT_STARTED → IN_PROGRESS (PLANNING) → READY_FOR_DEVELOPMENT
Phase: DEV_IMPLEMENT → Status: READY_FOR_DEVELOPMENT → IN_DEVELOPMENT
All Tasks Complete → Status: IN_DEVELOPMENT → COMPLETED
```

**Task Lifecycle Example**:
```
Task 0001.02.03: Password Validation Logic
Phase: FL_PLAN → Dev Status: NOT_STARTED (PENDING), QA Status: QA_PENDING [task file created]
Phase: DEV_IMPLEMENT → Dev Status: NOT_STARTED (PENDING) → IN_PROGRESS → COMPLETED, QA Status: QA_PENDING
Phase: QUALITY_ASSURANCE → Dev Status: COMPLETED, QA Status: QA_PENDING → QA_IN_PROGRESS → QA_PASSED/QA_FAILED
QA Iteration → If QA_FAILED: return to DEV_IMPLEMENT for rework (Dev status remains COMPLETED)
```

**QA Failure Handling Example**:
```
Task 0003.01.01: Hook Integration Setup
Development Status: COMPLETED (development work committed)
QA Validation Status: QA_FAILED (integration tests failing)
Epic/Story Status: Remains IN_DEVELOPMENT (QA iteration required)
Orchestrator Logic: QA_FAILED tasks require DEV_IMPLEMENT iteration
Orchestrator Action: Return to DEV_IMPLEMENT phase for task rework
After Rework: Dev Status: COMPLETED, QA Status: QA_PENDING (ready for re-validation)
```

**Orchestrator QA Determination Logic**:
```
FOR each task in story:
  IF development_status == COMPLETED AND qa_status == QA_PENDING:
    → Task needs QA validation
  IF development_status == COMPLETED AND qa_status == QA_FAILED:
    → Task needs rework (return to DEV_IMPLEMENT)
  IF development_status == COMPLETED AND qa_status == QA_PASSED:
    → Task fully complete

STORY TRANSITION LOGIC:
  IF all tasks have development_status == COMPLETED:
    IF any task has qa_status == QA_PENDING:
      → Transition to QUALITY_ASSURANCE phase
    IF any task has qa_status == QA_FAILED:
      → Return to DEV_IMPLEMENT phase for rework
    IF all tasks have qa_status == QA_PASSED:
      → Transition to FL_FINAL phase
```

## State Recovery and Initialization:

The orchestrator supports **state recovery** for pre-existing work that bypassed the orchestrator workflow:

### **State Recovery Logic**:
When hooks detect missing orchestrator state but find evidence of completed work:
1. **Git Commit Detection**: Search for commits related to task identifier
2. **Documentation Verification**: Confirm task documentation files exist
3. **State Initialization**: Initialize orchestrator tracking for discovered work
4. **Phase Validation**: Allow appropriate phase transitions based on actual state

### **Recovery Scenarios**:
- **Task developed outside orchestrator**: Git commits exist + documentation exists → Initialize as COMPLETED
- **Epic/Story planning done manually**: Documentation hierarchy exists → Initialize planning phases
- **Partial orchestrator execution**: Some phases logged, others missing → Resume from appropriate phase

### **Hook Recovery Process**:
```bash
# Hook detects missing orchestrator state
IF orchestrator_log_missing(REQUIRED_PHASE):
  IF git_commits_exist(TASK_ID) AND documentation_exists(TASK_ID):
    log_state_recovery(TASK_ID, REQUIRED_PHASE)
    initialize_orchestrator_state(TASK_ID)
    allow_phase_transition()
  ELSE:
    block_transition() # No actual work completed
```

## State Persistence:

All state tracking happens in the existing `docs/DEVELOPMENT_PLAN_AND_PROGRESS.md` file with additional agentic state tracking:
```markdown
## Epic Implementation State
- Current Phase: QUALITY_ASSURANCE
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
- 🔄 QUALITY_ASSURANCE (Quality Assurance Specialist) - Story 0003.04 validation - Iteration 1 - 2025-08-05 15:45
- ⏸ FL_FINAL (pending)
- ⏸ PM_COMPLETE (pending)

## Quality Standards Applied
- Developer: BASE technical standards (standard implementation and testing)
- Quality Assurance: ENHANCED quality standards (through-the-roof validation and testing)
- Feature Lead: MAXIMUM business standards (ruthless business validation)
- Project Manager: STRATEGIC oversight (complete epic coherence)
```

## Hook-Based Automation System:

### Automated State Transition Tracking:
TodoWrite hook automation eliminates manual orchestrator state management:
- **Auto State Updates**: Hook automation automatically updates `docs/DEVELOPMENT_PLAN_AND_PROGRESS.md` when phase todos change
- **Phase Tracking**: Each phase (PM_BOOTSTRAP → FL_PLAN → DEV_IMPLEMENT → QUALITY_ASSURANCE → FL_FINAL → PM_COMPLETE) tracked as todo item
- **Real-time Sync**: Hook detects completed/in_progress phase changes and updates documentation instantly
- **Session Tracking**: Automatic session ID and timestamp tracking in progress files

### Automated Documentation Synchronization:
TodoWrite hook automation eliminates manual agent documentation updates:
- **Auto Doc Sync**: Hook automation automatically syncs progress across Epic/Story/Task files
- **Progress Calculation**: Hooks automatically calculate and update task/story/epic completion percentages
- **Bidirectional Updates**: Changes propagate automatically from Task → Story → Epic documentation
- **Real-time Status**: All documentation files stay synchronized with current implementation status

### Automated Quality Gate Validation:
Task hook automation eliminates manual orchestrator quality gate checks:
- **Pre-delegation Validation**: Hook automation validates completion criteria before Task delegation
- **Phase Transition Control**: Hooks automatically block delegation unless previous phase is completed
- **Quality Standards**: Automatic enforcement of phase-specific completion requirements
- **Error Prevention**: Prevents invalid state transitions and ensures proper workflow progression

### Hook System Structure:
Located in `resinai/commands/` with 3 essential automation functions:
- **`progress.py`** (TodoWrite) - Updates orchestrator state in main progress file
- **`documentation.py`** (TodoWrite) - Syncs progress across Epic/Story/Task hierarchy  
- **`validation.py`** (Task) - Validates phase completion before delegation


## Orchestrator Execution Logic:

### Agentic State-Machine Orchestrator Mode Rules:
- **MODE LOCK**: Claude is now in **Agentic State-Machine Orchestrator mode** - cannot exit until user requests
- **NO AUTONOMOUS MODE SWITCHING**: Cannot switch to demonstration mode, explanation mode, or any other mode
- **CONTINUOUS ORCHESTRATION**: Must continue orchestrating through ALL 6 phases until completion or user intervention
- **AUTOMATIC TASK PROGRESSION**: When task/story/epic completes, AUTOMATICALLY discover and continue with next work
- **NO STOPPING FOR USER INPUT**: NEVER stop and wait for user `/develop` commands unless portfolio is complete
- **NO PAUSING AFTER AGENTS**: NEVER pause execution after any agent completes - immediately continue to next phase
- **NO PHASE SKIPPING**: Agents MUST NOT skip phases or transition early for "demonstration" purposes
- **NO AUTONOMOUS WORKFLOW DECISIONS**: Agents implement their specific phase only - orchestrator controls transitions
- **COMPLETE IMPLEMENTATION REQUIRED**: Each agent must complete their phase fully before returning control
- **NO SHORTCUT REASONING**: Agents cannot decide to "move forward to show complete workflow" or similar
- **STRICT RETURN CODE ADHERENCE**: Only use documented return codes, never create ad-hoc exit reasons
- **CONTINUOUS DISCOVERY**: Automatically update TodoWrite tasks and continue with discovered next work

### Prohibited Behaviors in Agentic State-Machine Orchestrator Mode:

**CRITICAL PROHIBITIONS:**
- **NO "READY FOR NEXT TASK" MESSAGES**: Never display "ready for next task" or similar stopping messages
- **NO ORCHESTRATOR READY ANNOUNCEMENTS**: Never announce orchestrator readiness and wait for user commands
- **NO CONTINUATION PROMPTS**: Never prompt user to run `/develop` again unless portfolio complete
- **NO STOPPING BETWEEN TASKS**: Must automatically continue from task to task without pause
- **NO USER INPUT REQUESTS**: Never request user input mid-orchestration unless critical failure

## Mode Exit Protocol (**CRITICAL AND IMPORTANT SECTION!!!**)

Claude remains in **Agentic State-Machine Orchestrator mode** until:

### Permitted Exits:
- **User explicitly requests exit**: "Exit orchestrator mode", "Stop develop", etc.
- **Complete epic implementation**: All phases successfully completed through PM_COMPLETE
- **Critical system failure**: Agent returns CRITICAL_FAILURE requiring user intervention

### Prohibited Autonomous Exits:
- **Demonstration purposes**: "Let me show the complete workflow"
- **Iterative reasoning**: "Given the iterative nature..."
- **Mode switching**: Switching to explanation, tutorial, or any other mode
- **Self-termination**: Any autonomous decision to end orchestration
- **Phase skipping**: Jumping ahead to demonstrate later phases without completing current phase requirements
- Autonomous exits from Agentic State-Machine Orchestrator mode
- Skipping implementation phases to demonstrate business validation
- Ending orchestration early for any reason except user request or completion

### Main Loop (Agentic State-Machine Orchestrator Mode):

**🚨 CRITICAL ORCHESTRATOR RULE 🚨**: After EVERY agent completion, the orchestrator MUST IMMEDIATELY continue to the next phase. NEVER stop, NEVER wait for user input, NEVER display completion messages that pause execution. The orchestrator runs continuously until portfolio completion or critical failure.

1. **CONFIRM MODE LOCK**: Verify Claude is in Agentic State-Machine Orchestrator mode - NO MODE SWITCHING ALLOWED
2. **Parse Input Identifier** - determine scope from user input:
   - **EEEE** (e.g., 0003) = Epic scope
   - **EEEE.SS** (e.g., 0003.02) = Story scope
   - **EEEE.SS.TT** (e.g., 0003.02.01) = Task scope
   - **No input** = Auto-discover next unfinished work
   - **Feature Description** (natural language) = Create new epic from feature description
3. **Analyze Planning File Hierarchy** - check what exists in `docs/DEVELOPMENT_PLAN_AND_PROGRESS/`:
   - **Epic file**: `EEEE - Epic Name.md` exists?
   - **Story files**: `EEEE.SS - Epic Name - Story Name.md` exist for all stories?
   - **Task files**: `EEEE.SS.TT - Epic Name - Story Name - Task Name.md` exist for all tasks?
4. **Determine Required Bootstrapping** based on missing files and scope:
   - **Missing Epic**: PM_BOOTSTRAP phase (create Epic + Stories)
   - **Missing Stories**: PM_BOOTSTRAP phase (create missing Stories for Epic)
   - **Missing Tasks**: FL_PLAN phase (create missing Tasks for Story)
   - **Feature Description**: PM_BOOTSTRAP phase (create new Epic from feature description)
   - **All exist**: Continue with implementation/validation phases
5. **Invoke Sub-Agent** using Task tool with complete file hierarchy context - MAINTAIN MODE LOCK
6. **Apply Safeguards** - Validate agent response and prevent stuck situations:
   - **Validate Return Code**: Ensure agent provides explicit, valid return code
   - **Verify Deliverables**: Confirm all required deliverables completed before accepting SUCCESS codes
   - **Check Progress**: Validate actual progress matches claimed status
   - **Handle Missing Codes**: If no return code, prompt agent for explicit status
   - **Context Monitoring**: Track token usage and prepare for context boundary recovery
7. **Process Return Code** and agent's file hierarchy assessment - WITH VALIDATION
8. **Git Workflow Orchestration** - Actively manage git operations:
   - **Branch Creation**: When transitioning FL_PLAN → DEV_IMPLEMENT, invoke Feature Lead to execute `/branch` command
   - **Commit Monitoring**: During DEV_IMPLEMENT, verify Developer is using `/commit` command for code changes
   - **Branch Merge**: When transitioning FL_FINAL → PM_COMPLETE, invoke Feature Lead to merge feature branch and execute `/commit` for documentation
   - **Final Commits**: During PM_COMPLETE, invoke Project Manager to execute `/commit` command for final epic documentation
   - **Error Handling**: If any git operation fails, log error and require agent retry
9. **State Transition Reporting** - Use **STATE-TRANSITION** template (see Templates section) for all phase transitions
10. **Update State** across complete task tree based on agent feedback
11. **IMMEDIATE PHASE TRANSITION** - CRITICAL: After processing return code, IMMEDIATELY continue to next phase:
    - **NO STOPPING**: Do not stop after reporting state transition
    - **NO WAITING**: Do not wait for user input or commands
    - **AUTO-INVOKE**: Immediately invoke the next appropriate agent for the next phase
    - **CONTINUOUS EXECUTION**: Continue orchestration loop until completion or critical failure
    - **MANDATORY CONTINUATION**: After every agent completion, automatically proceed to next phase
12. **Auto-Discovery and Continuation** - CRITICAL: Automatically discover and continue with next work:
    - **Task Completion**: When task completes, automatically discover next task in story
    - **Story Completion**: When story completes, automatically discover next story in epic
    - **Epic Completion**: When epic completes, automatically discover next epic in portfolio
    - **Continuous Loop**: NEVER stop and wait for user input unless explicitly requested
    - **Update TodoWrite Tasks**: Automatically update task list with discovered next work
13. **Continue Loop** with auto-continuation until:
    - Agent returns `SUCCESS_ALL_EPICS_COMPLETE` (natural portfolio completion)
    - Agent returns `CRITICAL_FAILURE` (error requiring user intervention)
    - User explicitly requests exit (manual override)
    - Auto-continue epic cycles: `SUCCESS_CONTINUE_NEXT_EPIC` → restart at PM_BOOTSTRAP
    - NEVER EXIT MODE AUTONOMOUSLY except for natural portfolio completion

### State Transitions:

**PM_BOOTSTRAP Phase:**
- **TodoWrite Orchestration Setup**: Create master todo list for 6-phase state machine:
  ```
  1. PM_BOOTSTRAP - Epic and story analysis and creation → in_progress
  2. FL_PLAN - Task planning and feature branch setup → pending
  3. DEV_IMPLEMENT - Technical implementation with deliverable completion → pending
  4. QUALITY_ASSURANCE - Enhanced quality validation and testing → pending
  5. FL_FINAL - Maximum business validation and stakeholder acceptance → pending
  6. PM_COMPLETE - Strategic epic completion and documentation → pending
  ```
- **TodoWrite Phase Tracking**: Mark PM_BOOTSTRAP as in_progress before agent invocation
- Invoke: `@agent-project-manager` with "hierarchical_bootstrap" mode
- Context: Target identifier (EEEE/EEEE.SS/EEEE.SS.TT/Feature Description), complete file hierarchy analysis, project strategy
- **Agent Must Analyze File Hierarchy** and determine what's missing:
  - Check existence of `docs/DEVELOPMENT_PLAN_AND_PROGRESS/EEEE - Epic Name.md`
  - Check existence of all `docs/DEVELOPMENT_PLAN_AND_PROGRESS/EEEE.SS - Epic Name - Story Name.md` files
  - **Return Codes Based on Analysis**:
    - `SUCCESS_TO_FL_PLAN` - Epic/Stories complete, ready for task planning
    - `SUCCESS_TO_DEV_IMPLEMENT` - All files exist, ready for implementation
    - `MISSING_EPIC_FILES` - Created Epic/Stories, return to orchestrator for next phase
    - `FAILURE_SCOPE_UNCLEAR` - Cannot determine what to bootstrap, need clearer requirements
- **TodoWrite Phase Completion**: On success, mark PM_BOOTSTRAP as completed and next phase as in_progress
- Success → **IMMEDIATELY** transition based on what was accomplished and what remains - NO STOPPING
- Failure → **IMMEDIATELY** retry PM_BOOTSTRAP with refined requirements - NO STOPPING
- **ORCHESTRATOR CONTINUATION**: After processing PM return code, IMMEDIATELY invoke next phase agent

**FL_PLAN Phase:**
- **TodoWrite Phase Tracking**: Mark FL_PLAN as in_progress, PM_BOOTSTRAP as completed
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
- **Git Workflow - Feature Branch Creation**: On `SUCCESS_TO_DEV_IMPLEMENT`
  - **Orchestrator Action**: Invoke Feature Lead to create feature branch using `/branch feature/EEEE.SS.TT-task-description`
  - **Branch Creation Verification**: Ensure branch was created successfully before proceeding to DEV_IMPLEMENT
  - **Error Handling**: If branch creation fails, log error and retry or escalate
- **TodoWrite Phase Completion**: On success, mark FL_PLAN as completed and DEV_IMPLEMENT as in_progress
- Success → **IMMEDIATELY** transition based on what was accomplished and what remains - NO STOPPING
- Failure → **IMMEDIATELY** return to PM_BOOTSTRAP with planning issues - NO STOPPING
- **ORCHESTRATOR CONTINUATION**: After processing FL return code, IMMEDIATELY invoke next phase agent

**DEV_IMPLEMENT Phase:**
- **TodoWrite Phase Tracking**: Mark DEV_IMPLEMENT as in_progress, FL_PLAN as completed
- **SELF-REFLECTION DEVELOPER DISCOVERY**: Use the **SELF-REFLECTION-DEVELOPER-DISCOVERY** template (see Templates section)
  - List ALL discovered developer agents, marking irrelevant ones as "(not relevant)"
  - Show scoring algorithm with specific compatibility reasoning
  - Clearly state final selection with percentage match
- **Invoke Discovered Developer Agent** with "implement_task" mode
- Context: Specific task (EEEE.SS.TT) implementation checklist, technical specifications, detected tech stack, feature branch context
- Apply: BASE technical standards (standard implementation and testing)
- **DELIVERABLE VERIFICATION CHECKPOINT**: Before proceeding to QUALITY_ASSURANCE, orchestrator MUST verify ALL deliverables are complete
  - **Functional Deliverable Verification**: Confirm ALL functional requirements have been implemented and are working
  - **Technical Deliverable Verification**: Validate ALL technical requirements are met with functional implementations
  - **Integration Deliverable Verification**: Ensure ALL integration points are implemented and functional
  - **Quality Deliverable Verification**: Check ALL quality requirements are satisfied with evidence
  - **REJECT PARTIAL IMPLEMENTATIONS**: If ANY deliverable is incomplete, return to developer for completion
- **Task-Specific Implementation**: Focus on single task completion with full interface contracts
- **Git Workflow - Development Commits**: Orchestrator ensures developer commits during implementation:
  - **Orchestrator Verification**: Monitor that developer agent actually uses `/commit` command during implementation
  - **Commit Requirement**: Developer MUST use `/commit` command for all code changes with conventional commit format
  - **Multiple Commits Allowed**: Developer may invoke `/commit` multiple times during task iterations
  - **Orchestrator Action**: If no commits detected after implementation, prompt developer to commit changes
  - **Error Handling**: If commits fail, log error and require developer to retry
- **MANDATORY**: Agent MUST complete implementation fully - NO early exits or shortcuts
- **DELIVERABLE COMPLETENESS GATE**: Orchestrator verifies ALL deliverables before success transition
  - **ALL Requirements Met**: Every functional, technical, integration, and quality requirement must be complete
  - **NO Stub Implementations**: All functionality must be fully implemented, not placeholder code
  - **Evidence Required**: Developer must provide evidence of working functionality for each deliverable
  - **Return Policy**: If ANY deliverable is incomplete, return `FAILURE_CONTINUE` until ALL are satisfied
- **TodoWrite Phase Completion**: On `SUCCESS_TO_QUALITY_ASSURANCE`, mark DEV_IMPLEMENT as completed and QUALITY_ASSURANCE as in_progress
- Success (`SUCCESS_TO_QUALITY_ASSURANCE`) → **IMMEDIATELY** transition to QUALITY_ASSURANCE ONLY after ALL deliverables verified complete - NO STOPPING
- Failure (`FAILURE_CONTINUE`) → **IMMEDIATELY** stay in DEV_IMPLEMENT, increment iteration - NO STOPPING
- **Update Task Tree**: Update task file progress and parent story/epic status
- **ORCHESTRATOR CONTINUATION**: After processing Developer return code, IMMEDIATELY invoke next phase agent
- **Task Completion Processing**: Use **TASK-COMPLETION** template (see Templates section) to:
  - Report task completion with progress statistics
  - Determine next action (task → task, task → story, task → epic)
  - **AUTOMATICALLY CONTINUE**: Immediately invoke appropriate next phase - DO NOT STOP
  - **UPDATE TODOWRITE**: Update task list with discovered next work
  - **CONTINUOUS EXECUTION**: Never pause for user input unless all work complete

**QUALITY_ASSURANCE Phase:**
- **TodoWrite Phase Tracking**: Mark QUALITY_ASSURANCE as in_progress, DEV_IMPLEMENT as completed
- **Task Tool Delegation**: QA agent may use Task tool to launch parallel validation agents for different quality aspects
- Invoke: `@agent-quality-assurance` with "enhanced_validation" mode
- Context: Completed implementation, Feature Lead feedback (if any)
- Apply: **ENHANCED quality standards** (through-the-roof validation)
- Standards: Far exceed Developer standards, comprehensive testing
- **CRITICAL VALIDATION REQUIREMENTS**:
  - **Code formatting and linting MUST pass** without any errors
  - **All tests MUST pass** without exception
  - **NEVER fix any errors** - only test and validate
  - **Return to DEV_IMPLEMENT immediately** if formatting, linting, or tests fail
- **MANDATORY**: Agent MUST complete full enhanced validation - NO skipping to demonstration phases
- **TodoWrite Phase Completion**: On `SUCCESS_TO_FL_FINAL`, mark QUALITY_ASSURANCE as completed and FL_FINAL as in_progress
- Success (`SUCCESS_TO_FL_FINAL`) → **IMMEDIATELY** transition to FL_FINAL - NO STOPPING
- Failure (`FAILURE_TO_DEV`) → **IMMEDIATELY** return to DEV_IMPLEMENT with enhanced Quality Assurance feedback - NO STOPPING
- Critical Failure → **IMMEDIATELY** escalate to Feature Lead for guidance - NO STOPPING
- **ORCHESTRATOR CONTINUATION**: After processing QA return code, IMMEDIATELY invoke next phase agent

**FL_FINAL Phase:**
- **TodoWrite Phase Tracking**: Mark FL_FINAL as in_progress, QUALITY_ASSURANCE as completed
- Invoke: `@agent-feature-lead` with "final_business_validation" mode
- Context: Quality Assurance-validated implementation, business requirements
- Apply: MAXIMUM business standards (ruthless business validation)
- **Git Workflow - Feature Completion**: On `SUCCESS_TO_PM_COMPLETE`
  - **Orchestrator Action**: Invoke Feature Lead to merge feature branch into main using git merge commands
  - **Documentation Commits**: Orchestrator ensures Feature Lead uses `/commit` command for all documentation updates
  - **Branch Merge Verification**: Ensure feature branch is successfully merged before proceeding
  - **Documentation Verification**: Verify all project documentation and status tracking files are committed
  - **Error Handling**: If merge or commits fail, log error and require retry
- **TodoWrite Phase Completion**: On `SUCCESS_TO_PM_COMPLETE`, mark FL_FINAL as completed and PM_COMPLETE as in_progress
- Success (`SUCCESS_TO_PM_COMPLETE`) → **IMMEDIATELY** transition to PM_COMPLETE - NO STOPPING
- Failure (`FAILURE_TO_QUALITY_ASSURANCE`) → **IMMEDIATELY** return to QUALITY_ASSURANCE with business feedback - NO STOPPING
- Critical Failure → **IMMEDIATELY** escalate to Project Manager - NO STOPPING
- **ORCHESTRATOR CONTINUATION**: After processing FL return code, IMMEDIATELY invoke next phase agent

**PM_COMPLETE Phase:**
- **TodoWrite Phase Tracking**: Mark PM_COMPLETE as in_progress, FL_FINAL as completed
- Invoke: `@agent-project-manager` with "complete_epic" mode
- Context: Fully validated epic implementation
- Apply: STRATEGIC oversight (complete epic coherence validation)
- **Git Workflow - Epic Documentation**: On successful completion
  - **Orchestrator Action**: Invoke Project Manager to use `/commit` command for final epic documentation updates
  - **Documentation Verification**: Ensure all epic status files, progress tracking, and main documentation are committed
  - **Commit Verification**: Verify commits were successful with proper conventional commit format
  - **Error Handling**: If documentation commits fail, log error and require retry
- **TodoWrite Final Completion**: On success, mark PM_COMPLETE as completed - all 6 phases completed successfully
- **Epic Portfolio Analysis**: Project Manager analyzes epic portfolio for continuation
  - **Epic Discovery**: Scan `docs/DEVELOPMENT_PLAN_AND_PROGRESS/` for unfinished epics
  - **Priority Assessment**: Identify next highest-priority unfinished epic
  - **Continuation Decision**: Return appropriate continuation code based on portfolio status
- **Auto-Continuation Processing**:
  - Success (`SUCCESS_CONTINUE_NEXT_EPIC`) → **IMMEDIATELY AND AUTOMATICALLY** transition to PM_BOOTSTRAP for next epic - NO STOPPING
  - Success (`SUCCESS_ALL_EPICS_COMPLETE`) → Portfolio complete - exit orchestration mode
  - Failure → **IMMEDIATELY** return to appropriate phase for epic-level issues - NO STOPPING
  - **CRITICAL**: NEVER report "ready for next task" and stop - ALWAYS continue automatically
- **ORCHESTRATOR CONTINUATION**: After processing PM return code, IMMEDIATELY invoke next phase agent or continue next epic

## Return Codes:

### project-manager:
- `SUCCESS_TO_FL_PLAN` - Epic/Stories complete, ready for task planning
- `SUCCESS_TO_DEV_IMPLEMENT` - All files exist, ready for implementation
- `SUCCESS_CONTINUE_NEXT_EPIC` - Current epic complete, next epic discovered, continue orchestration
- `SUCCESS_ALL_EPICS_COMPLETE` - All epics complete, no further work, exit orchestration mode
- `MISSING_EPIC_FILES` - Created Epic/Stories, return to orchestrator for next phase
- `FAILURE_EPIC_SCOPE` - Epic scope issues, needs refinement
- `FAILURE_SCOPE_UNCLEAR` - Cannot determine what to bootstrap, need clearer requirements
- `CRITICAL_FAILURE` - Major strategic issues, requires stakeholder input

### feature-lead:
- `SUCCESS_TO_DEV_IMPLEMENT` - All task files complete, ready for implementation
- `SUCCESS_TO_PM_COMPLETE` - Business validation passed, ready for strategic completion
- `MISSING_STORY_FILES` - Story file missing, return to orchestrator for PM_BOOTSTRAP
- `MISSING_TASK_FILES` - Created missing task files, return to orchestrator for next phase
- `FAILURE_TO_PM` - Planning issues, return to Project Manager
- `FAILURE_TO_QUALITY_ASSURANCE` - Business issues found, return to Quality Assurance with feedback
- `CRITICAL_FAILURE` - Major business issues, escalate to Project Manager

### developer-* (Self-Reflection Discovery):
All developer agents follow standardized return codes:
- `SUCCESS_TO_QUALITY_ASSURANCE` - Implementation complete, ready for enhanced Quality Assurance validation
- `FAILURE_CONTINUE` - Implementation issues, continuing development work
- `PARTIAL_SUCCESS` - Some tasks complete, continuing with remaining work
- `TIMEOUT_CONTINUE` - Progress update, continuing development
- `MISSING_TASK_FILES` - Task file missing, return to orchestrator for FL_PLAN

**Developer Agents** (Self-Reflection Discovery):
- All developer agents are discovered through self-reflection and internal knowledge
- Agent capabilities and specializations determined through self-reflection on agent descriptions and expertise
- Available agents discovered dynamically through internal contemplation

### quality-assurance:
- `SUCCESS_TO_FL_FINAL` - Enhanced quality validation passed, ready for business validation
- `FAILURE_TO_DEV` - Quality issues found, return to development with enhanced feedback
- `ENHANCEMENT_REQUIRED` - Quality standards not met, specific improvements needed
- `CRITICAL_FAILURE` - Major quality issues, escalate to Feature Lead

**QA Return Code Status Handling**:
- When QA returns `FAILURE_TO_DEV` or `ENHANCEMENT_REQUIRED`:
  - Task status remains `COMPLETED` (development work was done and committed)
  - Epic/Story status remains `IN_DEVELOPMENT` (QA iteration cycle required)
  - Orchestrator returns to DEV_IMPLEMENT phase for task rework/enhancement
  - Additional development commits do not change the fundamental `COMPLETED` task status

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
- **User Journey Validation**: Complete user workflows function perfectly
- **Stakeholder Acceptance**: All business requirements fully satisfied
- **Competitive Analysis**: Implementation meets or exceeds market standards
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
- **Story Files** (`docs/DEVELOPMENT_PLAN_AND_PROGRESS/EEEE.SS - Epic Name - Story Name.md`): Updated with strategic business objectives, story-level outcomes, and completion status
- **Task Files** (`docs/DEVELOPMENT_PLAN_AND_PROGRESS/EEEE.SS.TT - Epic Name - Story Name - Task Name.md`): Updated with implementation details, progress, and completion status
- **Main Progress** (`docs/DEVELOPMENT_PLAN_AND_PROGRESS.md`): Updated with overall epic progress and state transitions

**Update Responsibilities by Agent (Hook-Automated):**
- **Project Manager**: Focuses on strategic decisions and business-level planning (documentation auto-synced by hooks)
- **Feature Lead**: Focuses on business requirements and validation (task progress auto-synced by hooks)
- **Developer**: Focuses solely on technical implementation (progress auto-tracked by hooks)
- **Quality Assurance**: Focuses on quality validation and testing (results auto-documented by hooks)
- **Orchestrator**: Focuses on high-level coordination (state transitions auto-managed by hooks)

**File Update Frequency**: Automatic real-time updates via hook system - agents only need to update TodoWrite status.

## Orchestrator Responsibilities (Hook-Automated):

**CRITICAL**: The develop orchestrator handles these high-level responsibilities (with hook automation):
- **Agent Delegation**: Manages transitions between agents and handles return codes (quality gates auto-validated by hooks)
- **Workflow Coordination**: Orchestrates the 6-phase state machine flow (state transitions auto-tracked by hooks)
- **Return Code Processing**: Interprets agent responses and determines next actions (documentation auto-synced by hooks)
- **Epic Scope Management**: Handles epic-level workflow decisions and completion processing
- **Git Workflow Orchestration**: Actively manages and verifies git operations across all phases
  - **Branch Creation Orchestration**: Invokes Feature Lead to execute `/branch` commands during transitions
  - **Commit Verification**: Monitors and verifies that agents are actually executing `/commit` commands
  - **Merge Coordination**: Orchestrates Feature Lead branch merging and documentation commits
  - **Final Commit Management**: Ensures Project Manager executes final documentation commits
  - **Git Error Handling**: Manages git operation failures and requires agent retry
- **Completion Processing**: Handles task completion, next task discovery, and workflow continuation

**Developer Agent Responsibilities**: Developer focuses on technical implementation and commits during development:
- **Development Commits**: Uses `/commit` command during implementation for code changes
- **Conventional Commits**: `/commit` command automatically generates conventional commits with task scope: `type(EEEE.SS.TT): description`
- **Multiple Commits**: May invoke `/commit` command multiple times during task iterations
- **No Branch Management**: Does not create, merge, or delete branches - handled by Feature Lead

## Error Handling and Orchestrator Safeguards:

### Core Error Handling:
- **Sub-Agent Failures**: Capture error, add to feedback, retry appropriate phase
- **State Corruption**: Reset to last known good state with progress preservation
- **Quality-Based Progression**: Agents continue until deliverables meet required quality standards
- **Critical Failures**: Escalation paths to appropriate senior agent
- **Quality Gate Failures**: Automatic return to previous phase with enhanced feedback
- **Epic Scope Changes**: Automatic escalation to Project Manager for strategic decisions

### Orchestrator Safeguards (Anti-Stuck Mechanisms):

#### **1. Agent Response Validation**
- **Missing Return Codes**: If agent completes without proper return code, orchestrator prompts for explicit status
- **Ambiguous Responses**: Orchestrator requests clarification on unclear agent responses
- **Incomplete Handoffs**: Validate all required deliverables before accepting agent completion

#### **2. Progress Verification Checkpoints**
- **Before Phase Transitions**: Verify previous phase actually completed with evidence
- **Deliverable Confirmation**: Confirm all task requirements met before moving to next phase
- **Documentation Sync**: Ensure task documentation reflects current implementation status

#### **3. Context Management**
- **Token Usage Monitoring**: Track agent token consumption and provide continuation guidance
- **Session State Recovery**: Maintain orchestrator state across context boundaries
- **Graceful Degradation**: Handle context limits with proper state preservation

#### **4. Timeout and Recovery Mechanisms**
- **Agent Responsiveness**: Detect non-responsive agents and provide recovery options
- **State Persistence**: Save orchestrator state before each agent invocation
- **Resume Capability**: Allow orchestration to resume from last known good state

#### **5. Validation Gates**
- **Phase Completion Verification**: Validate each phase meets its quality gates before progression
- **Return Code Enforcement**: Require explicit, valid return codes from all agents
- **Deliverable Evidence**: Demand concrete evidence of deliverable completion

### Recovery Procedures:

#### **Stuck Agent Recovery**
```
1. Detect: Agent running without progress updates
2. Prompt: Request explicit status and deliverable completion evidence
3. Validate: Verify all requirements met or identify missing work
4. Decide: Continue current phase or escalate to next phase based on evidence
```

#### **Missing Return Code Recovery**
```
1. Detect: Agent completed without valid return code
2. Prompt: "Please provide explicit return code: SUCCESS_TO_[NEXT_PHASE] or FAILURE_CONTINUE"
3. Validate: Confirm return code matches actual deliverable completion status
4. Proceed: Process validated return code for state transition
```

#### **Context Boundary Recovery**
```
1. Detect: Approaching context limits during agent execution
2. Save: Preserve current orchestrator state and agent progress
3. Resume: Restart orchestration with saved state and continuation context
4. Validate: Confirm all deliverables and progress maintained across boundary
```

## Git Workflow Integration:

### Orchestrated Git Workflow:
Orchestrator actively manages and verifies git operations:

**1. Feature Branch Creation (Orchestrator → Feature Lead)**:
```
Orchestrator: Invoke Feature Lead to execute:
/branch feature/TASK-0001.02.03-password-validation-logic
```
- **Orchestrator Action**: Invokes Feature Lead at FL_PLAN → DEV_IMPLEMENT transition
- **Verification**: Confirms branch was created successfully before proceeding
- **Error Handling**: If branch creation fails, logs error and requires retry

**2. Development Commits (Orchestrator → Developer)**:
```
Orchestrator: Verify Developer executes:
/commit
```
- **Orchestrator Monitoring**: Monitors that developer actually uses `/commit` command during implementation
- **Verification**: Confirms commits are being made with conventional format
- **Error Handling**: If no commits detected, prompts developer to commit changes

**3. Feature Completion (Orchestrator → Feature Lead)**:
```
Orchestrator: Invoke Feature Lead to execute:
git merge feature/TASK-0001.02.03-password-validation-logic
/commit
```
- **Orchestrator Action**: Invokes Feature Lead at FL_FINAL → PM_COMPLETE transition
- **Merge Verification**: Ensures feature branch is successfully merged
- **Documentation Commits**: Verifies all documentation updates are committed
- **Error Handling**: If merge or commits fail, requires retry

**4. Epic Documentation (Orchestrator → Project Manager)**:
```
Orchestrator: Invoke Project Manager to execute:
/commit
```
- **Orchestrator Action**: Invokes Project Manager during PM_COMPLETE phase
- **Verification**: Confirms final epic documentation is committed
- **Error Handling**: If documentation commits fail, requires retry

### Branch Naming Conventions:
- **Task Branches**: `feature/EEEE.SS.TT-task-description`
- **Epic Context**: Always includes full task identifier for traceability
- **Description**: Task name converted to kebab-case
- **Examples**:
  - `feature/0001.02.03-password-validation-logic`
  - `feature/0001.04.01-integration-testing-setup`
  - `feature/0002.01.05-oauth-provider-configuration`

### Commit Message Conventions:
- **Format**: `type(EEEE.SS.TT): description`
- **Scoping**: Task identifier as scope for precise tracking
- **Types**: `feat`, `fix`, `refactor`, `test`, `docs`, `style`, `perf`
- **Examples**:
  - `feat(0001.02.03): implement password validation logic with security requirements`
  - `fix(0001.02.03): resolve password validation edge case for special characters`
  - `refactor(0001.02.03): optimize password validation performance`
  - `test(0001.02.03): add comprehensive password validation test coverage`

### Git Responsibility Separation:


## Documentation Linking Requirements:

**MANDATORY DOCUMENTATION HIERARCHY**: All documentation files must be linked together in a complete hierarchy with bidirectional cross-references:

### **Main Documentation File**:
- **ALWAYS** contains links to all epics
- Updated by Project Manager when epics are created or completed

### **Epic Files (`EEEE - Epic Name.md`)**:
- **Header Navigation**: Always include navigation header pointing back to main documentation
- **Story Links Section**: Always contain links to all related stories with current status
- **Bidirectional Links**: Linked from main documentation AND link to all stories
- **Progress Reflection**: Must reflect current status of all related stories and tasks
- **Maintained by**: Project Manager

### **Story Files (`EEEE.SS - Epic Name - Story Name.md`)**:
- **Header Navigation**: Always include navigation headers pointing to parent epic and main documentation
- **Task Links Section**: Always contain links to all related tasks with current status
- **Bidirectional Links**: Linked from parent epic AND link to all tasks
- **Progress Reflection**: Must reflect current status of all related tasks
- **Maintained by**: Feature Lead

### **Task Files (`EEEE.SS.TT - Epic Name - Story Name - Task Name.md`)**:
- **Header Navigation**: Always include navigation headers pointing to parent story and epic
- **Progress Status**: Must reflect current implementation status in real-time
- **Implementation Notes**: Document technical decisions and progress immediately
- **Maintained by**: Developer agents (immediate updates at every progression step)

### **Agent Documentation Responsibilities**:

**Project Manager**:
- Create and maintain epic links in main documentation
- Monitor story/task progress and update epic documentation immediately
- Ensure epic-story bidirectional linking integrity
- Validate main documentation ↔ epic ↔ story link chain

**Feature Lead**:
- Create and maintain task links in story documentation
- Monitor task progress and update story documentation immediately
- Ensure story-task bidirectional linking integrity
- Alert Project Manager when story completion requires epic updates

**Quality Assurance**:
- Verify task documentation has been updated by developers before validation
- Test all documentation navigation links and cross-references
- Confirm documentation status matches implementation reality
- Report documentation integrity issues to Feature Lead

**Developer Agents** (All):
- Update task documentation immediately at EVERY progression step
- Never delay documentation updates - real-time synchronization required
- Document technical decisions, blockers, and solutions as they occur
- Ensure task status always reflects current implementation progress

## Integration:

- Uses existing epic and story file structures from epic:bootstrap
- Creates task implementation checklists like task:execute
- Maintains all progress tracking and documentation standards
- Compatible with existing `docs/DEVELOPMENT_PLAN_AND_PROGRESS/` structure
- Uses correct file naming: Epic files (`EEEE - Epic Name.md`), Story files (`EEEE.SS - Epic Name - Story Name.md`), Task files (`EEEE.SS.TT - Epic Name - Story Name - Task Name.md`)
- **Enhanced Git Integration**: Complete feature branch workflow with `/branch` and `/commit` command patterns
- **MANDATORY DOCUMENTATION LINKING**: Complete documentation hierarchy with bidirectional cross-references
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

# Create new epic from feature description (starts from planning phase)
/develop "Add user authentication with OAuth2 and role-based permissions"
/develop "Implement real-time chat feature with message history"
/develop "Build responsive dashboard with data visualization charts"

# The orchestrator will:
# 1. Parse input identifier to determine scope (Epic/Story/Task/Feature Description)
# 2. Analyze complete planning file hierarchy in docs/DEVELOPMENT_PLAN_AND_PROGRESS/:
#    - Epic file: EEEE - Epic Name.md
#    - Story files: EEEE.SS - Epic Name - Story Name.md
#    - Task files: EEEE.SS.TT - Epic Name - Story Name - Task Name.md
# 3. Invoke agents who analyze hierarchy and report what's missing
# 4. Agents return to orchestrator with file hierarchy status codes
# 5. Orchestrator determines next phase based on agent assessments
# 6. **Git Workflow Integration**:
#    - Feature Lead uses /branch command to create feature branch before DEV_IMPLEMENT
#    - Developer uses /commit command during implementation (auto-generates: feat(0001.02.03): add validation rules)
#    - Feature Lead merges feature branch and uses /commit command for documentation updates
#    - Project Manager uses /commit command for final epic documentation updates
# 7. Continue until scope completion with progressive quality standards
# 8. Update complete task tree with results throughout process
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
- [ ] **DELIVERABLE COMPLETION VERIFICATION**: ALL task deliverables must be complete before proceeding
  - [ ] **Functional Requirements Complete**: Every functional requirement fully implemented and working
  - [ ] **Technical Requirements Complete**: Every technical requirement met with validated functionality
  - [ ] **Integration Requirements Complete**: Every integration point functional and tested
  - [ ] **Quality Requirements Complete**: Every quality standard satisfied with evidence
  - [ ] **NO PARTIAL IMPLEMENTATIONS**: All deliverables must be fully functional, not stub implementations
- [ ] All tasks implemented with basic quality
- [ ] Unit tests pass for all components
- [ ] Code formatting and linting pass
- [ ] Basic functionality demonstrated

### QUALITY_ASSURANCE Gate (ENHANCED Standards):
- [ ] **REQUIREMENT-BASED VALIDATION**: Focus validation on deliverable completion rather than implementation style
  - [ ] **Functional Requirement Validation**: ALL functional requirements implemented and working as specified
  - [ ] **Technical Requirement Validation**: ALL technical requirements met with validated functionality
  - [ ] **Integration Requirement Validation**: ALL integration points functional and properly tested
  - [ ] **Quality Requirement Validation**: ALL quality requirements satisfied with evidence
  - [ ] **DELIVERABLE COMPLETENESS GATE**: ALL task deliverables complete - NO partial implementations accepted
- [ ] **Code formatting and linting pass** (zero errors - CRITICAL REQUIREMENT)
- [ ] **All tests pass** (100% success rate - CRITICAL REQUIREMENT)
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
- [ ] **User journeys validated** (complete workflows function perfectly)
- [ ] **Stakeholder acceptance achieved** (all requirements satisfied)
- [ ] **Competitive analysis passed** (meets/exceeds market standards)
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
- [ ] All stories deliver measurable user value
- [ ] All tasks pass enhanced Quality Assurance validation
- [ ] Business requirements fully satisfied
- [ ] Technical implementation exceeds quality standards
- [ ] User experience meets maximum standards
- [ ] Strategic objectives achieved
- [ ] Complete documentation and knowledge transfer
- [ ] All agents provide explicit sign-off approval

## Templates:

### SELF-REFLECTION-DEVELOPER-DISCOVERY:

```template
SELF-REFLECTION DEVELOPER DISCOVERY

Let me analyze the project tech stack and discover appropriate developer agents:

Detected Technologies (from project analysis):
- [TECHNOLOGY_1] [VERSION] ([DESCRIPTION])
- [TECHNOLOGY_2] [VERSION] ([DESCRIPTION])
- [TECHNOLOGY_N] [VERSION] ([DESCRIPTION])

Developer Agent Discovery (self-reflection):
Available developer agents I know about:
- [agent-name-1]: [Agent description and specialization]
- [agent-name-2]: [Agent description and specialization]
- [agent-name-3]: [Agent description and specialization] (not relevant)
- [agent-name-N]: [Agent description and specialization] (not relevant)

Agent Matching Algorithm:
- [agent-name-1]: Score [XX]% ([Compatibility reasoning])
- [agent-name-N]: Score [XX]% ([Compatibility reasoning])

SELECTION: [selected-agent] (highest compatibility - [XX]% match)

TARGET: [Task/Story/Epic identifier] - [Task/Story/Epic name]
AGENT: [selected-agent] with "[mode]" mode and [QUALITY_STANDARD] standards
```

### STATE-TRANSITION:

```template
PHASE [N]: ORCHESTRATION

STATE: [FROM_PHASE] -> ([RETURN_CODE]) → [TO_PHASE]

EPIC: [EPIC_NAME]
STORY: [STORY_NAME]
TASK: [TASK_NAME]

[Brief description of what was accomplished in the previous phase and what the next phase will handle. Include any key context or feedback being passed forward.]
```

### TASK-COMPLETION:

```template
TASK [EEEE.SS.TT] COMPLETED - [TASK_NAME] ✅
STORY PROGRESS: [COMPLETED_TASKS]/[TOTAL_TASKS] tasks completed ([PERCENTAGE]%)
EPIC PROGRESS: [COMPLETED_STORIES]/[TOTAL_STORIES] stories completed ([EPIC_PERCENTAGE]%)

[NEXT_ACTION_TYPE]: [NEXT_IDENTIFIER] - [NEXT_NAME]

[NEXT_PHASE_INVOCATION]
```

### EPIC-CONTINUATION:

```template
EPIC [EEEE] STRATEGIC COMPLETION ✅ - [EPIC_NAME]
PORTFOLIO ANALYSIS: [COMPLETED_EPICS] of [TOTAL_EPICS] epics completed ([PORTFOLIO_PERCENTAGE]%)

NEXT EPIC DISCOVERY:
- Epic [NEXT_EEEE]: [NEXT_EPIC_NAME] ([STATUS])
- Priority: [HIGH|MEDIUM|LOW]
- Estimated Scope: [X] stories estimated

[CONTINUATION_TYPE]: [CONTINUATION_ACTION]

[NEXT_PHASE_INVOCATION]
```

**Next Action Types:**
- `CONTINUING TO NEXT STORY TASK` - More tasks remain in current story
- `STORY [EEEE.SS] COMPLETED - CONTINUING TO NEXT STORY` - Current story finished, next story available
- `EPIC [EEEE] COMPLETED - ALL STORIES FINISHED` - Entire epic completed
- `EPIC [EEEE] COMPLETED - CONTINUING TO NEXT EPIC` - Current epic finished, next epic discovered
- `ALL EPICS COMPLETED - PORTFOLIO FINISHED` - All epics completed, orchestration complete

## Template Usage Examples:

### Task Completion

Task → Task Transition:
```
TASK 0001.02.05 COMPLETED - Cross-Platform Compatibility Testing ✅
STORY PROGRESS: 5/6 tasks completed (83.3%)
EPIC PROGRESS: 1/4 stories completed (25.0%)

CONTINUING TO NEXT STORY TASK: 0001.02.06 - Performance Optimization and Validation

INVOKING DEV_IMPLEMENT PHASE for Task 0001.02.06 (Final Story 0001.02 Task)
```

Task → Story Transition:
```
TASK 0001.02.06 COMPLETED - Performance Optimization and Validation ✅
STORY PROGRESS: 6/6 tasks completed (100.0%)
EPIC PROGRESS: 2/4 stories completed (50.0%)

STORY 0001.02 COMPLETED - CONTINUING TO NEXT STORY: 0001.03 - User Interface Enhancement

INVOKING FL_PLAN PHASE for Story 0001.03 (Epic 0001 Story 3/4)
```

Task → Epic Completion:
```
TASK 0001.04.03 COMPLETED - Final Integration Testing ✅
STORY PROGRESS: 3/3 tasks completed (100.0%)
EPIC PROGRESS: 4/4 stories completed (100.0%)

EPIC 0001 COMPLETED - ALL STORIES FINISHED: User Authentication System

INVOKING PM_COMPLETE PHASE for Epic 0001 (Strategic Completion)
```

### State Transition

Forward Transition:
```
PHASE 3: ORCHESTRATION

STATE: DEV_IMPLEMENT -> (SUCCESS_TO_QUALITY_ASSURANCE) → QUALITY_ASSURANCE

EPIC: 0001 - User Authentication System
STORY: 0001.02 - Login Implementation
TASK: 0001.02.03 - Password Validation Logic

Developer completed task implementation with BASE standards. All unit tests passing and code formatting applied. Quality Assurance will now perform ENHANCED validation with through-the-roof standards.
```

Same-State Transition (Retry):
```
PHASE 3: ORCHESTRATION

STATE: QUALITY_ASSURANCE -> (FAILURE_TO_DEV) → DEV_IMPLEMENT

EPIC: 0001 - User Authentication System
STORY: 0001.02 - Login Implementation
TASK: 0001.02.03 - Password Validation Logic

Quality Assurance found integration issues and performance problems. Developer will address the enhanced feedback and continue implementation iteration 2.
```

Same-Agent Continuation:
```
PHASE 3: ORCHESTRATION

STATE: DEV_IMPLEMENT -> (PARTIAL_SUCCESS) → DEV_IMPLEMENT

EPIC: 0001 - User Authentication System
STORY: 0001.02 - Login Implementation
TASK: 0001.02.02 - Email Validation Logic

Developer completed 2 of 3 tasks in current story. Continuing with remaining task implementation while maintaining BASE technical standards.
```

### Epic Continuation

Epic → Next Epic Transition:
```
EPIC 0001 STRATEGIC COMPLETION ✅ - User Authentication System
PORTFOLIO ANALYSIS: 1 of 3 epics completed (33.3%)

NEXT EPIC DISCOVERY:
- Epic 0002: Payment Processing System (NOT_STARTED)
- Priority: HIGH
- Estimated Scope: 5 stories estimated

EPIC 0001 COMPLETED - CONTINUING TO NEXT EPIC: 0002 - Payment Processing System

INVOKING PM_BOOTSTRAP PHASE for Epic 0002 (Auto-continuation)
```

Portfolio Completion:
```
EPIC 0003 STRATEGIC COMPLETION ✅ - Notification System
PORTFOLIO ANALYSIS: 3 of 3 epics completed (100.0%)

PORTFOLIO STATUS: ALL EPICS COMPLETED

ALL EPICS COMPLETED - PORTFOLIO FINISHED

ORCHESTRATION COMPLETE: All epics implemented with progressive quality standards
```

Epic Continuation State Transition:
```
PHASE 6: ORCHESTRATION

STATE: PM_COMPLETE -> (SUCCESS_CONTINUE_NEXT_EPIC) → PM_BOOTSTRAP

COMPLETED EPIC: 0001 - User Authentication System
NEXT EPIC: 0002 - Payment Processing System
PORTFOLIO: 1/3 epics complete (33.3%)

Project Manager completed strategic validation of Epic 0001 and discovered Epic 0002 requires implementation. Auto-continuing orchestration with PM_BOOTSTRAP phase for next epic.
```

Portfolio Completion State Transition:
```
PHASE 6: ORCHESTRATION

STATE: PM_COMPLETE -> (SUCCESS_ALL_EPICS_COMPLETE) → ORCHESTRATION_COMPLETE

COMPLETED EPIC: 0003 - Notification System  
PORTFOLIO: 3/3 epics complete (100.0%)
FINAL STATUS: All epics implemented

Project Manager completed strategic validation of final epic. All epics in portfolio have been successfully implemented with progressive quality standards. Orchestration naturally complete.
```

## Template Usage Guidelines:

### General Template Requirements:
- **Replace all bracketed placeholders** with actual discovered values
- **Always show detected technologies** with versions and descriptions
- **Include target identifier** and selected agent with mode
- **Use consistent formatting** and structure throughout all templates
- **Provide clear rationale** for all decisions and selections made

### SELF-REFLECTION-DEVELOPER-DISCOVERY Requirements:
- **List ALL discovered developer agents**, marking irrelevant ones as "(not relevant)"
- **Show scoring algorithm** with specific compatibility reasoning
- **Clearly state final selection** with percentage match

### STATE-TRANSITION Requirements:
- **Use sequential phase numbering** (1-6) to track orchestration progress
- **Include hierarchical context**: Show Epic name, Story name, and Task name for full context
- **Include precise return codes** from previous agent for audit trail
- **Provide transition context** explaining what was accomplished and what's next
- **Maintain consistent STATE format**: FROM_PHASE -> (RETURN_CODE) → TO_PHASE
- **Handle different scope levels**: Epic-level, Story-level, or Task-level context as appropriate
- **Handle same-state transitions**: When FROM_PHASE equals TO_PHASE, provide clear iteration context

### TASK-COMPLETION Requirements:
- **Calculate accurate progress percentages** for both story and epic completion tracking
- **Use task completion checkmark** (✅) for visual confirmation
- **Show dual progress tracking**: Story progress and Epic progress percentages
- **Determine correct next action type** based on remaining work:
  - Task → Task: More tasks in current story
  - Task → Story: Current story complete, more stories in epic
  - Task → Epic: All stories complete, epic finished
- **Include proper phase invocation** for next step in workflow
- **Maintain hierarchical context** with Epic/Story/Task relationships
