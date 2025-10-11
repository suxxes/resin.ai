### Phase X: Project Discovery
Discover project structure and conventions

#### CRITICAL REQUIREMENTS
- **MUST** identify configuration
- **MUST** discover testing framework
- **MUST** understand project structure

#### CRITICAL RESTRICTIONS
- **NEVER** assume project conventions
- **NEVER** skip tooling discovery
- **NEVER** ignore existing patterns

#### EXECUTION FLOW

- **Update phase tracking**
  - Update "Phase X: Project Discovery" task as in_progress

- **Configuration Analysis**
  - Examine project configuration analyzing build configuration files, package managers, and compiler settings
  - Review manifest files understanding dependencies and project metadata
  - Check environment setup reviewing variables, virtual environments, and deployment configs
  - Identify build systems detecting available build tools
  - Analyze tool versions ensuring compatibility with project requirements

- **Architecture Discovery**
  - Deep dive architecture completing comprehensive review of conventions
  - Review project structure understanding source organization and directory layout
  - Identify module patterns detecting architectural conventions and design patterns
  - Review existing code examining similar implementations for consistency
  - Analyze component organization understanding separation of concerns
  - Discover service boundaries identifying microservices or module boundaries
  - Map dependency graph understanding component relationships

- **Technology Stack**
  - Identify frameworks detecting all major frameworks in use
  - Catalog libraries listing third-party dependencies and utilities
  - Review databases identifying data storage technologies
  - Check API patterns understanding REST, GraphQL, or RPC usage
  - Discover integrations finding external service connections

- **Development Workflow**
  - Study project setup understanding project-specific tooling before implementation
  - Examine build scripts understanding compilation and packaging processes
  - Review test setup identifying testing frameworks and strategies
  - Check CI/CD configuration understanding automation pipelines and compliance requirements
  - Identify development tools finding debuggers, profilers, and analyzers
  - Discover deployment process understanding release mechanisms
  - Learn pre-commit checks understanding automated quality gates

- **Quality Standards**
  - Identify linters detecting code style enforcement tools
  - Review formatters finding automatic code formatting configuration
  - Check type systems understanding static type checking setup
  - Discover pre-commit hooks identifying automated quality gates
  - Analyze code coverage understanding testing requirements

- **Analyze code patterns**
  - Review existing components/modules
  - Identify naming conventions
  - Understand file organization
  - Note import patterns

- **Complete phase**
  - Update "Phase X: Project Discovery" task as completed
  - Transition to "Phase X: Test Design"