## CODE STYLE AND STRUCTURE

**Pure Function Design**
- Write pure functions that return consistent outputs for given inputs without side effects
- No hidden dependencies on external state
- All data dependencies passed as explicit parameters
- Functions should do one thing well

**Immutability**
- Favor immutable data structures and avoid mutating state directly
- Prefer creating new objects/arrays over modifying existing ones
- Use const/final/let appropriately based on language

**Modular Decomposition**
- Break complex functionality into small, focused modules (≤250 lines per file)
- Each module should have a clear, single responsibility
- Prefer composition over inheritance
- Use dependency injection for flexibility

**Single Responsibility**
- Each function, class, and module should have one clear purpose
- If describing a module's purpose requires "and", it needs splitting
- Functions should be 20 lines or less (with reasonable exceptions)
- Clear separation between business logic and infrastructure

**Side Effect Isolation**
- Isolate side effects (API calls, database operations, external services) into dedicated modules
- Push side effects to system boundaries
- Use functional core, imperative shell pattern
- Make side effects explicit and documented

**Declarative Patterns**
- Prefer declarative over imperative programming styles
- Express the "what" rather than the "how"
- Use functional and declarative programming patterns where appropriate
- Prefer iteration and modularization over code duplication
