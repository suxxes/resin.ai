<!-- Updated: 2025-09-20 00:00:00 UTC -->

# Task {XXXX.YY.ZZ} - {TASK_NAME}

**Epic**: [{XXXX} - {EPIC_NAME}](<./{XXXX} - {EPIC_NAME}.md>)
**Story**: [{XXXX.YY} - {STORY_NAME}](<./{XXXX.YY} - {STORY_NAME}.md>)
**Development Status**: [NOT_STARTED (PENDING) | IN_PROGRESS | COMPLETED]
**QA Validation Status**: [QA_PENDING | QA_IN_PROGRESS | QA_PASSED | QA_FAILED]

## Overview

{TASK_DESCRIPTION}

## Objectives
- **{OBJECTIVE}**: {OBJECTIVE_DESCRIPTION}
<!-- CRITICAL: REPEAT PATTERN FOR EACH ITEM -->

### Dependencies
- **Required Completion**: {PREREQUISITE_TASKS}
- **Technical Dependencies**: {TECHNICAL_DEPENDENCIES}
- **Resource Dependencies**: {RESOURCE_DEPENDENCIES}

## Decision Record

### Key Decisions Made During Planning
<!-- CRITICAL: This section MUST be present in all task documents and should NOT be modified -->

1. **DECISION**: {DECISION_TITLE}
   - **ALTERNATIVES**: {DECISION_ALTERNATIVES}
   - **RATIONALE**: {DECISION_RATIONALE}
   - **TRADE-OFFS**: {DECISION_TRADEOFFS}
   - **VALIDATION**: {DECISION_VALIDATION}

<!-- CRITICAL: REPEAT PATTERN FOR EACH ITEM -->

## IMPLEMENTATION
<!-- CRITICAL: The following sections MUST maintain strict order and presence in all task documents -->

### Step 1: Modern Approach Research
<!-- CRITICAL: This section MUST be present and completed before implementation -->
- [ ] Research latest technologies for: {RESEARCH_AREA}
- [ ] Evaluate modern frameworks/libraries: {FRAMEWORKS_TO_EVALUATE}
- [ ] Research security best practices for: {SECURITY_RESEARCH_AREA}
- [ ] Document chosen approach: {APPROACH_DOCUMENTATION}
- [ ] Verify compatibility with: {COMPATIBILITY_CHECK}
<!-- CRITICAL: REPEAT PATTERN FOR EACH ITEM -->

### Step 2: Branch Validation
<!-- CRITICAL: Branch existence and naming MUST be validated immediately. Exit and report if validation fails -->
- [ ] Verify current branch is a task branch
- [ ] Confirm currently on correct feature branch
- [ ] **MUST** exit immediately and report error if branch does not exist or naming is incorrect

<!-- CRITICAL: Test-first approach MUST be maintained. Tests MUST be written before implementation -->
<!-- CRITICAL: Limited to maximum 5 implementation items. Each item MUST follow test-first pattern -->

### Step 3: {IMPLEMENTATION_1_NAME}

#### Test Development (MUST complete before implementation)
- [ ] Write test file: {TEST_FILE_1_PATH}
- [ ] Implement test case: {TEST_CASE_1_DESCRIPTION}
- [ ] Write mock for: {MOCK_1_DESCRIPTION}
- [ ] Verify tests fail initially (red phase)

#### Implementation
- [ ] Create/Update file: {IMPLEMENTATION_1_FILE}
- [ ] Implement: {IMPLEMENTATION_1_DESCRIPTION}
- [ ] Verify tests pass (green phase)
- [ ] Refactor if needed (refactor phase)

<!-- CRITICAL: REPEAT PATTERN FOR EACH ITEM -->

### Step 4+N: Quality Assurance
- [ ] Run test suite - ALL tests must pass
- [ ] Run linting checks - ALL must pass
- [ ] Run code formatting - ALL files must be properly formatted
- [ ] Verify no console errors/warnings
- [ ] Check code coverage meets standards
- [ ] Validate performance requirements
- [ ] Security validation completed

### Step 5+N: Triple-Subagent Sign-Off Process
<!-- CRITICAL: This section MUST be present in all task documents and MUST NOT be modified -->
<!-- CRITICAL: ALL three subagents MUST provide explicit approval before task completion -->
<!-- CRITICAL: This is the FINAL step in implementation before validation -->

#### Developer Subagent Validation
- [ ] Technical implementation complete and verified
- [ ] All tests passing with required coverage
- [ ] Code quality standards met
- [ ] **Developer Sign-off**: {DEVELOPER_APPROVAL_STATUS}

#### QA Subagent Validation
- [ ] Integration testing complete
- [ ] Performance requirements validated
- [ ] Security testing passed
- [ ] **QA Sign-off**: {QA_APPROVAL_STATUS}

#### Manager Subagent Validation
- [ ] Business requirements satisfied
- [ ] User value delivered
- [ ] Strategic alignment confirmed
- [ ] **Manager Sign-off**: {MANAGER_APPROVAL_STATUS}

<!-- ==================== VALIDATION ==================== -->

## Success Criteria

### Functional Requirements
- [ ] {FUNCTIONAL_REQUIREMENT}
<!-- CRITICAL: REPEAT PATTERN FOR EACH ITEM -->

### Technical Requirements
- [ ] {TECHNICAL_REQUIREMENT}
<!-- CRITICAL: REPEAT PATTERN FOR EACH ITEM -->

### User Experience Requirements
- [ ] {UX_REQUIREMENT}
<!-- CRITICAL: REPEAT PATTERN FOR EACH ITEM -->

## Risk Assessment

**Technical Risk Level**: [LOW | MEDIUM | HIGH]

**Primary Risk**: {PRIMARY_RISK}
**Mitigation**: {PRIMARY_RISK_MITIGATION}

**Secondary Risk**: {SECONDARY_RISK}
**Mitigation**: {SECONDARY_RISK_MITIGATION}

## DELIVERABLE COMPLETION REQUIREMENTS
Task is considered complete ONLY when ALL deliverables are fully functional

**Functional Deliverable Completion:**
- ALL functional requirements must be implemented and working as specified
- NO stub implementations or placeholders - all functionality must be complete
- Evidence of working functionality must be provided and validated
- All functional requirements must pass validation testing

**Technical Deliverable Completion:**
- ALL technical requirements must be met with validated functionality
- All technical specifications must be implemented according to requirements
- Integration points must be functional and tested
- All technical quality standards must be satisfied

**Quality Deliverable Completion:**
- ALL quality requirements must be satisfied with evidence
- All testing requirements must be met with passing results
- Performance requirements must be validated and met
- All quality gates must be passed successfully

### Developer Handoff Criteria
- ALL functional requirements implemented and working
- ALL technical requirements met with evidence
- ALL integration points functional and tested
- NO partial implementations or placeholders

### Quality Assurance Validation
- ALL deliverables tested and validated as working
- ALL acceptance criteria verified with evidence
- ALL quality standards confirmed with validation results
- NO incomplete functionality accepted

### Business Acceptance
- ALL functional deliverables working as specified
- ALL user experience requirements satisfied
- ALL business requirements met with evidence
- Complete deliverable validation confirmed
