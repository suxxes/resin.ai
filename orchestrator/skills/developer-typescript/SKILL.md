---
name: developer-typescript
description: TypeScript and JavaScript development standards and best practices. Provides type safety requirements, code organization patterns, testing standards, and modern TypeScript/JavaScript guidelines.
---

<!-- Updated: 2025-11-11 19:00:00 UTC -->

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

### Best Practices
- **MUST** use `as const` for literal types
- **MUST** use `?.` for safe property access
- **MUST** use `??` for default values (not `||` which treats 0/"" as falsy)
- **MUST** use template literal types when appropriate
- **Prefer** interfaces over type aliases for object shapes
- **Prefer** const and readonly over let and mutable
- **Use** destructuring for cleaner code
- **Use** async/await over raw promises

## COMMON PATTERNS

### Test File Organization
- Test files: `*.test.ts`, `*.spec.ts`, `*.test.tsx`, `*.spec.tsx`
- Location: Co-located with source files or in `__tests__/` directory
- Setup files: `setupTests.ts`, `jest.setup.ts`, `vitest.setup.ts`

### Test Structure (Jest/Vitest)
```typescript
describe('ComponentName', () => {
  beforeEach(() => {
    // Setup
  });

  afterEach(() => {
    // Cleanup
  });

  it('should do something', () => {
    // Arrange
    const input = 'test';

    // Act
    const result = functionUnderTest(input);

    // Assert
    expect(result).toBe('expected');
  });
});
```

### Type Guards
```typescript
function isString(value: unknown): value is string {
  return typeof value === 'string';
}

function isUser(obj: unknown): obj is User {
  return typeof obj === 'object' &&
         obj !== null &&
         'name' in obj &&
         'email' in obj;
}
```

### Generic Constraints
```typescript
function getProperty<T, K extends keyof T>(obj: T, key: K): T[K] {
  return obj[key];
}

function filterByType<T>(items: T[], predicate: (item: T) => boolean): T[] {
  return items.filter(predicate);
}
```

### Utility Types
```typescript
// Partial - make all properties optional
type PartialUser = Partial<User>;

// Required - make all properties required
type RequiredUser = Required<PartialUser>;

// Pick - select specific properties
type UserPreview = Pick<User, 'id' | 'name'>;

// Omit - exclude specific properties
type UserWithoutPassword = Omit<User, 'password'>;

// Record - create object type with specific keys
type UserMap = Record<string, User>;
```

### Async/Await
```typescript
async function fetchUser(id: string): Promise<User> {
  const response = await fetch(`/api/users/${id}`);
  if (!response.ok) {
    throw new Error('Failed to fetch user');
  }
  return await response.json();
}

// Error handling
try {
  const user = await fetchUser('123');
  console.log(user.name);
} catch (error) {
  console.error('Error:', error);
}
```
