### Phase X: Validation and Handoff
Validate implementation and prepare handoff

#### CRITICAL REQUIREMENTS
- **MUST** complete all validation checks
- **MUST** ensure production readiness
- **MUST** prepare comprehensive handoff

#### CRITICAL RESTRICTIONS
- **NEVER** skip validation steps
- **NEVER** handoff incomplete work
- **NEVER** ignore quality issues

#### EXECUTION FLOW

- **Update phase tracking**
  - Update "Phase X: Validation and Handoff" task as in_progress

- **Static Analysis**
  - Run type checking ensuring type safety and correctness
  - Execute linting enforcing code style and conventions with zero errors
  - Perform security scanning detecting vulnerabilities and passing security validation
  - Check complexity analyzing maintainability and readability
  - Validate dependencies ensuring compatibility and security
  - Run pre-commit checks passing all automated quality gates

- **Dynamic Validation**
  - Run test suites executing all unit and integration tests
  - Perform load testing verifying performance under stress
  - Execute smoke tests confirming basic functionality
  - Check regression ensuring no breaking changes
  - Validate integrations confirming external connections work

- **Quality Verification**
  - Measure coverage ensuring adequate test protection
  - Review metrics analyzing performance and efficiency
  - Check standards confirming CI/CD compliance and pipeline requirements
  - Validate documentation ensuring completeness and accuracy
  - Assess maintainability evaluating code clarity and structure
  - Verify deliverable completion confirming ALL functionality is complete and operational

- **Handoff Preparation**
  - **MUST** read and use `~/.claude/shared/orchestrator/RETURN-CODES.md` file
  - **MUST** read and use `~/.claude/shared/orchestrator/HANDOFF-PROTOCOL.md` file
  - **MUST** follow requirements from `~/.claude/shared/core/TEMPLATE-REQUIREMENTS.md` file
  - Compile deliverables listing all created and modified artifacts
  - Document changes describing modifications and additions
  - Report metrics providing quality and performance measurements
  - Include instructions detailing deployment and usage procedures
  - Note considerations highlighting limitations and future work

- **Complete phase**
  - Update "Phase X: Validation and Handoff" task as completed
  - Return to orchestrator with results