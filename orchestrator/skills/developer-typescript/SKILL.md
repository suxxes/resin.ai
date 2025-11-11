---
name: developer-typescript
description: TypeScript and JavaScript development standards and best practices. Provides type safety requirements, code organization patterns, testing standards, and modern TypeScript/JavaScript guidelines.
---

<!-- Updated: 2025-11-11 19:15:00 UTC -->

# TypeScript/JavaScript Development Skill

This skill provides TypeScript and JavaScript-specific standards and best practices for TDD-based development.

## TYPESCRIPT/JAVASCRIPT STANDARDS

### Type Safety Requirements
- **NEVER** use `any` without strong justification and a comment explaining why
- **MUST** use strict TypeScript settings (`strict: true` in tsconfig.json)
- **MUST** use generics for reusable, type-safe code
- **MUST** implement proper type guards for runtime checks
- **MUST** leverage TypeScript utility types effectively (Partial, Pick, Omit, Record, etc.)
- **Prefer** unknown over any for type-safe error handling

### Code Organization
- **Naming**: Use PascalCase for types/interfaces/classes, camelCase for variables/functions
- **Imports**: Use absolute imports via path aliases when available
- **Type Location**: Co-locate types with implementation
- **Barrel Exports**: Use index files for clean imports

### Testing Standards
- **Test Isolation**: Each test must be independent
- **Clear Names**: Test names describe behavior being tested
- **AAA Pattern**: Arrange-Act-Assert structure in tests
- **Test Coverage**: Minimum 80% code coverage
- **Fast Tests**: Keep tests fast and focused
- **Test Files**: `*.test.ts`, `*.spec.ts`, `*.test.tsx`, `*.spec.tsx`
- **Test Location**: Co-located with source files or in `__tests__/` directory
- **Setup Files**: `setupTests.ts`, `jest.setup.ts`, `vitest.setup.ts`

### Best Practices
- **MUST** use `as const` for literal types
- **MUST** use `?.` for safe property access
- **MUST** use `??` for default values (not `||` which treats 0/"" as falsy)
- **MUST** use template literal types when appropriate
- **Prefer** interfaces over type aliases for object shapes
- **Prefer** const and readonly over let and mutable
- **Use** destructuring for cleaner code
- **Use** async/await over raw promises
