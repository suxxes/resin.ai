### Phase X: Test Design
Design tests before implementation (TDD approach)

#### CRITICAL REQUIREMENTS
- **MUST** design tests before writing code
- **MUST** define test cases for all requirements
- **MUST** specify expected behaviors

#### CRITICAL RESTRICTIONS
- **NEVER** write implementation before tests
- **NEVER** skip test design phase
- **NEVER** leave behaviors unspecified

#### EXECUTION FLOW

- **Update phase tracking**
  - Update "Phase X: Test Design" task as in_progress

- **Behavior Specification**
  - Design interfaces first establishing contracts before implementation
  - Define expected behaviors describing what the system should do
  - Specify acceptance criteria establishing measurable success conditions
  - Document user scenarios describing real-world usage patterns
  - Identify edge cases determining boundary and error conditions
  - Establish invariants defining conditions that must always hold
  - Ensure complete end-to-end functionality planning

- **Test Case Design**
  - Design unit tests specifying individual component behaviors
  - Plan integration tests defining component interaction scenarios
  - Create acceptance tests establishing user-level functionality
  - Define property tests specifying invariant conditions
  - Design performance tests establishing efficiency requirements

- **Test Data Planning**
  - Define fixtures creating reusable test data structures
  - Plan mocks specifying external dependency simulations
  - Design stubs establishing controlled component responses
  - Create factories generating test data variations
  - Establish seeds providing deterministic random data

- **Assertion Planning**
  - Define success conditions specifying expected outcomes
  - Plan failure scenarios describing error handling expectations
  - Specify state changes defining before and after conditions
  - Design output validation establishing result verification
  - Create metric assertions defining performance expectations

- **Complete phase**
  - Update "Phase X: Test Design" task as completed
  - Transition to "Phase X: Test Implementation"