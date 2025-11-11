---
name: developer-swift
description: Swift development standards and best practices for iOS, macOS, and Apple platforms. Provides type safety requirements, SwiftUI patterns, testing standards, and modern Swift guidelines.
---

<!-- Updated: 2025-11-11 19:15:00 UTC -->

# Swift Development Skill

This skill provides Swift-specific standards and best practices for Apple platform development with SwiftUI, UIKit, and the Swift ecosystem.

## SWIFT STANDARDS

### Type Safety Requirements
- **Strong Typing**: Leverage Swift's strong type system
- **Optionals**: Use optionals properly with safe unwrapping (`if let`, `guard let`, `??`)
- **Generics**: Use generics for reusable, type-safe code
- **Protocols**: Use protocol-oriented programming
- **Type Inference**: Let compiler infer types when clear, explicit when needed for clarity

### Code Organization
- **Naming**: Use camelCase for properties/methods/functions, PascalCase for types/protocols
- **Access Control**: Use appropriate access levels (private, fileprivate, internal, public, open)
- **Extensions**: Use extensions to organize code by protocol conformance
- **File Structure**: One primary type per file

### Testing Standards
- **Test Isolation**: Each test must be independent
- **Clear Names**: Test names describe behavior being tested (testUserLogin_WithValidCredentials_ShouldSucceed)
- **XCTest**: Use XCTest framework for unit and UI tests
- **Test Coverage**: Minimum 80% code coverage
- **Fast Tests**: Keep unit tests fast and focused

### Best Practices
- **Value Types**: Prefer structs and enums over classes when appropriate
- **Immutability**: Use `let` for constants, `var` only when mutation needed
- **Guard Statements**: Use guard for early returns and unwrapping
- **Result Types**: Use `Result<Success, Failure>` for error handling
- **Modern Concurrency**: Use async/await and actors for concurrent code
- **SwiftUI**: Prefer SwiftUI for new UI code on modern platforms
