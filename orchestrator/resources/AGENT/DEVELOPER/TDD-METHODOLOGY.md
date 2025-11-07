## TDD METHODOLOGY

### Red-Green-Refactor Cycle
- **Red Phase**: Write failing tests that define desired behavior
- **Green Phase**: Write minimal code to make tests pass
- **Refactor Phase**: Improve code quality while keeping tests green
- **Small Steps**: Work in small increments, one test at a time
- **Continuous Testing**: Run tests after every change

### Test-First Principles
- **Behavior Focus**: Tests describe what system should do, not how
- **Documentation**: Tests serve as living documentation
- **Design Driver**: Tests drive better design decisions
- **Safety Net**: Tests provide confidence for refactoring
- **Fast Feedback**: Tests give immediate feedback on changes

### Testing Hierarchy
- **Unit Tests**: Test individual functions and components (70%)
- **Integration Tests**: Test component interactions (20%)
- **E2E Tests**: Test complete user workflows (10%)
- **Property Tests**: Test invariants and properties
- **Performance Tests**: Test efficiency requirements

### Testing Standards
- **Test Isolation**: Each test must be independent
- **Clear Names**: Test names describe behavior being tested
- **AAA Pattern**: Arrange-Act-Assert structure in tests
- **Test Coverage**: Minimum 80% code coverage
- **Fast Tests**: Keep tests fast and focused
