---
name: developer-swift
description: Swift development standards and best practices for iOS, macOS, and Apple platforms. Provides type safety requirements, SwiftUI patterns, testing standards, and modern Swift guidelines.
---

<!-- Updated: 2025-11-11 19:00:00 UTC -->

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

## SWIFT PATTERNS

### SwiftUI View
```swift
import SwiftUI

struct ContentView: View {
    @State private var count = 0

    var body: some View {
        VStack {
            Text("Count: \(count)")
            Button("Increment") {
                count += 1
            }
        }
    }
}
```

### Async/Await
```swift
func fetchUser(id: String) async throws -> User {
    let url = URL(string: "https://api.example.com/users/\(id)")!
    let (data, _) = try await URLSession.shared.data(from: url)
    return try JSONDecoder().decode(User.self, from: data)
}

// Usage
Task {
    do {
        let user = try await fetchUser(id: "123")
        print(user.name)
    } catch {
        print("Error: \(error)")
    }
}
```

### Protocol-Oriented Design
```swift
protocol Drawable {
    func draw()
}

extension Drawable {
    func draw() {
        print("Drawing...")
    }
}

struct Circle: Drawable {
    let radius: Double
}
```

### Result Type
```swift
func loadUser(id: String) -> Result<User, Error> {
    do {
        let user = try database.fetchUser(id: id)
        return .success(user)
    } catch {
        return .failure(error)
    }
}

// Usage
switch loadUser(id: "123") {
case .success(let user):
    print(user.name)
case .failure(let error):
    print("Error: \(error)")
}
```

### Optional Handling
```swift
// Guard let (early return)
guard let user = optionalUser else {
    return
}

// If let (conditional)
if let user = optionalUser {
    print(user.name)
}

// Nil coalescing
let name = optionalName ?? "Unknown"

// Optional chaining
let city = user?.address?.city
```

### Generics
```swift
func swap<T>(_ a: inout T, _ b: inout T) {
    let temp = a
    a = b
    b = temp
}

struct Stack<Element> {
    private var items: [Element] = []

    mutating func push(_ item: Element) {
        items.append(item)
    }

    mutating func pop() -> Element? {
        return items.popLast()
    }
}
```

### XCTest Example
```swift
import XCTest
@testable import MyApp

final class UserLoginTests: XCTestCase {
    var sut: LoginViewModel!

    override func setUp() {
        super.setUp()
        sut = LoginViewModel()
    }

    override func tearDown() {
        sut = nil
        super.tearDown()
    }

    func testLoginWithValidCredentials_ShouldSucceed() async throws {
        // Arrange
        let email = "test@example.com"
        let password = "password123"

        // Act
        let result = try await sut.login(email: email, password: password)

        // Assert
        XCTAssertTrue(result.isSuccess)
    }
}
```

### Actor (Concurrency)
```swift
actor UserCache {
    private var cache: [String: User] = [:]

    func getUser(id: String) -> User? {
        cache[id]
    }

    func setUser(_ user: User) {
        cache[user.id] = user
    }
}

// Usage
let cache = UserCache()
await cache.setUser(user)
let cachedUser = await cache.getUser(id: "123")
```
