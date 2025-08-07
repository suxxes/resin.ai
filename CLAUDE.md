# AI Code Quality Assistant Guide

<!-- Generated: 2025-01-27 11:51:27 UTC -->

## Overview

This guide provides AI assistants with comprehensive code quality standards based on bulletproof coding principles. The standard operates on four distinct scales (Functions → APIs/Packages → Applications → Systems) with specific requirements, enforcement mechanisms, and quality measures for each level.

## Core Philosophy: Bulletproof Code

**Definition**: Code is bulletproof when written to make most errors expected, leaving as few as possible in the unexpected category.

**Primary Error Sources**:
- Unexpected input (explicit variables, implicit state)
- Lack of documentation and readability
- Implicit coupling between components
- Lack of comprehensive testing

**Key Principle**: Higher quality code requires more time and effort because developers must anticipate future errors and design appropriate responses.

## Multi-Scale Code Architecture

### 1. Functions
**Scope**: Smallest code units - encapsulate actions, computations, state changes

**Requirements**:
- Expect wrong input types: prevent, handle, or raise appropriate errors
- Document function purpose in one sentence
- State output types and potential errors
- Use standard style formatting
- Choose meaningful variable names (follow language conventions)
- Add unit tests for non-straightforward functions
- Test encapsulation quality:
  - Can users use function without reading implementation?
  - Is function affected by internal changes in other functions?
  - Are all failure scenarios documented?

**Enforcement**:
- **Responsibility**: Individual developers/engineers
- **Tools**: Code formatters, linters, automated unit test runners, PR code reviews
- **Metrics**: Formatting/linting failures, test failures, bugs per PR, test coverage

### 2. APIs / Packages / Modules
**Scope**: Code organized around single concepts (user management API, numpy arrays)

**Requirements**:
- **Documentation**: Separate specs (comprehensive/precise) from guides (explanatory)
- **Core concept clarity**: Document the central "thing" the module handles
- **Consistent naming**: Routes, files, folders follow established conventions
- **Requirements documentation**: README or Confluence with functional test cases
- **User consideration**:
  - Internal vs external users
  - Error message clarity without code reading
  - Detailed but customizable logging

**Enforcement**:
- **Primary responsibility**: Developers/engineers
- **Secondary responsibility**: QA team members
- **Dev tasks**: Write specs/guides, follow naming conventions
- **QA tasks**: Verify requirements documentation, test case validity, error message clarity
- **Metrics**: Percentage of APIs/packages/modules meeting all standards

### 3. Applications
**Scope**: User-facing software requiring support for less technical users

**Requirements**:
- **Human-readable documentation**: Explain API/package interactions in natural language
- **User-centric design**:
  - UI: Users always have way to proceed (no dead ends requiring support)
  - API-only: Provide functionality verification (heartbeats, sample I/O)
- **Error handling**: Applications handle errors or crash gracefully (no unhandled exceptions)
- **Versioning & release process**:
  - Release notes
  - Sequential deployment: QA → Stable → Staging → Production
  - Team handoffs and sign-offs
- **Comprehensive testing**: Automated component testing + manual testing + UAT

**Enforcement**:
- **Primary responsibility**: QA team
- **Supporting roles**: PMs (organization), Support (user issues), Developers (bug fixes), DevOps (deployment)
- **QA tasks**: Error handling verification, user workflow testing, comprehensive functionality testing
- **PM tasks**: Team coordination, change management, requirement documentation
- **Metrics**: Support tickets (patches/bugfixes/hotfixes), log errors/crashes, test coverage

### 4. Systems
**Scope**: Networked application groups working together

**Requirements**:
- **Complex documentation**: Focus on component connections (network diagrams, system design, access patterns, request flows)
- **Connectivity focus**:
  - Users need system-wide health visibility with friendly error messages
  - Maintainers need component-to-outcome traceability
- **Resilient error handling**: Point to potential failing components with resolution suggestions
- **Advanced testing**: Standard application testing + connectivity loss scenarios + high load testing

**Enforcement**:
- **Status**: Too complex for current standard enforcement
- **Future consideration**: Will require specialized processes and tools

## Implementation Guidelines for AI Assistants

### Code Review Priorities
1. **Input validation**: Check for explicit input validation and error handling
2. **Documentation quality**: Verify one-sentence function summaries and type documentation
3. **Coupling assessment**: Identify implicit dependencies and global variable usage
4. **Test coverage**: Ensure non-trivial functions have corresponding unit tests

### Quality Assessment Framework
- **Function level**: Focus on encapsulation, type safety, readability
- **Module level**: Evaluate documentation completeness, naming consistency, requirement clarity
- **Application level**: Assess user experience, error handling, release process compliance
- **System level**: Analyze component interactions, resilience patterns, monitoring capabilities

### Common Anti-Patterns to Flag
- Functions without input validation
- Missing or unclear documentation
- Implicit coupling through global state
- Untested complex logic
- Inconsistent naming conventions
- Applications that crash on errors
- Systems without health monitoring

## Enforcement Integration

### Automated Tools Integration
- Code formatters and linters for style compliance
- Unit test runners for PR validation
- Test coverage tools for quality metrics
- Documentation generators for consistency

### Process Integration
- PR review checklists based on code level
- Release process validation for applications
- Cross-team handoff requirements
- Quality metrics tracking and reporting

# Important Instruction Reminders
- Do what has been asked; nothing more, nothing less.
- NEVER create files unless they're absolutely necessary for achieving your goal.
- ALWAYS prefer editing an existing file to creating a new one.
- NEVER proactively create documentation files (*.md) or README files. Only create documentation - files if explicitly requested by the User.
- ALWAYS use system date (YYYY-MM-DD format) when managing documents, files, folders, and any date-related operations.
