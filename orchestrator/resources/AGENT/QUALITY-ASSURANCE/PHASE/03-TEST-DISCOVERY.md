### Phase 03: Test Discovery
Discover and analyze testing requirements

#### CRITICAL REQUIREMENTS
- **MUST** identify all test files and testing framework
- **MUST** understand existing test coverage
- **MUST** determine additional test requirements

#### CRITICAL RESTRICTIONS
- **NEVER** assume testing framework without verification
- **NEVER** skip test discovery
- **NEVER** trust developer test results without re-verification

#### EXECUTION FLOW

- **Update phase tracking**
  - Update "Phase 03: Test Discovery" task as in_progress

- **Discover testing framework**
  - Check package.json, Cargo.toml, or equivalent
  - Identify test commands and scripts
  - Locate test files and directories
  - Determine test coverage tools

- **Analyze existing tests**
  - Review current test coverage
  - Identify gaps in test coverage
  - Note edge cases requiring validation
  - Acknowledge integration test requirements

- **Complete phase**
  - Update "Phase 03: Test Discovery" task as completed
  - Transition to "Phase 04: Test Execution"
