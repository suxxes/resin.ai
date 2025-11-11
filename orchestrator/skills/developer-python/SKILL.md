---
name: developer-python
description: Python development standards and best practices. Provides type safety requirements, code organization patterns, testing standards, and Pythonic coding guidelines.
---

<!-- Updated: 2025-11-11 19:00:00 UTC -->

# Python Development Skill

This skill provides Python-specific standards and best practices for TDD-based development.

## PYTHON STANDARDS

### Type Safety Requirements
- **Type Hints**: Use type hints for all function signatures and class attributes
- **Static Typing**: Run mypy in strict mode for type checking
- **Generic Types**: Use generics from typing module for reusable, type-safe code
- **Protocol Types**: Use Protocol for structural subtyping
- **Type Guards**: Implement proper type narrowing with isinstance checks

### Code Organization
- **Naming**: Use snake_case for functions/variables, PascalCase for classes
- **Imports**: Use absolute imports, avoid circular dependencies
- **Module Structure**: Group imports (stdlib, third-party, local) with blank lines between groups

### Testing Standards
- **Test Isolation**: Each test must be independent
- **Clear Names**: Test names describe behavior being tested (test_function_should_do_something)
- **Fixtures**: Use pytest fixtures for test setup
- **Test Coverage**: Minimum 80% code coverage
- **Fast Tests**: Keep tests fast and focused

### Best Practices
- **Pythonic Code**: Follow PEP 8 and write idiomatic Python
- **Context Managers**: Use with statements for resource management
- **Comprehensions**: Prefer list/dict comprehensions for clarity
- **Generators**: Use generators for memory-efficient iteration
- **Dataclasses**: Use dataclasses or Pydantic models for data structures
- **F-Strings**: Use f-strings for string formatting (not % or .format())

## COMMON PATTERNS

### Test File Organization
- Test files: `tests/test_*.py` or `tests/*_test.py`
- Test functions: `def test_function_name():`
- Test classes: `class TestClassName:`
- Test methods: `def test_method_name(self):`

### Fixture Usage
```python
import pytest

@pytest.fixture
def sample_data():
    return {"key": "value"}

def test_with_fixture(sample_data):
    assert sample_data["key"] == "value"
```

### Parametrized Tests
```python
import pytest

@pytest.mark.parametrize("input,expected", [
    (1, 2),
    (2, 4),
    (3, 6),
])
def test_double(input, expected):
    assert input * 2 == expected
```

### Type Annotations
```python
from typing import List, Optional, Dict, Protocol

def process_items(items: List[str]) -> Dict[str, int]:
    return {item: len(item) for item in items}

def find_user(id: str) -> Optional[User]:
    return database.get(id)

class Drawable(Protocol):
    def draw(self) -> None: ...
```
