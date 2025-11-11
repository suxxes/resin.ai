<!-- Updated: 2025-11-11 18:03:58 UTC -->

## ASK USER QUESTION TOOL REQUIREMENTS

Universal requirements for using the AskUserQuestion tool when gathering user input, clarifying requirements, and making implementation decisions during planning orchestration.

### CRITICAL REQUIREMENTS
- **MUST** use AskUserQuestion tool for ALL user input gathering
- **MUST** provide 2-4 structured options per question (minimum 2, maximum 4)
- **MUST** include 1-4 questions per tool call (minimum 1, maximum 4)
- **MUST** provide clear trade-off descriptions for each option
- **MUST** end all questions with a question mark
- **MUST** keep headers under 12 characters

### CRITICAL RESTRICTIONS
- **NEVER** ask questions in plain text
- **NEVER** provide more than 4 options per question
- **NEVER** provide fewer than 2 options per question
- **NEVER** include manual "Other" option - automatically provided
- **NEVER** use emojis in questions or options

## WHEN TO USE

### Requirements Gathering
- Technology stack choices (frameworks, libraries, databases)
- Architecture patterns (MVC, microservices, serverless)
- Feature prioritization and scope decisions
- Design approach selection

### Clarifying Ambiguity
- Multiple valid interpretations of requirements
- Unclear implementation details
- Missing specifications
- Conflicting requirements

### Implementation Choices
- Algorithm selection (performance vs simplicity trade-offs)
- Data structure choices
- API design patterns
- Error handling strategies

### User Preferences
- Code style preferences
- Testing approach (unit vs integration vs e2e)
- Documentation level (minimal vs comprehensive)
- Deployment strategies

## TOOL STRUCTURE

### Input Schema

```json
{
  "questions": [
    {
      "question": "Full question ending with ?",
      "header": "Short label (max 12 chars)",
      "multiSelect": false,
      "options": [
        {
          "label": "Option name (1-5 words)",
          "description": "What this means and implications"
        }
      ]
    }
  ]
}
```

### Key Constraints

- **1-4 questions** per tool call (minimum 1, maximum 4)
- **2-4 options** per question (minimum 2, maximum 4)
- **No "Other" option needed** - automatically provided
- **Header max 12 characters** - displayed as chip/tag
- **Options must be distinct** unless multiSelect enabled

## EXAMPLES

### Example 1: Technology Choice (Single Select)

```json
{
  "questions": [
    {
      "question": "Which database should we use for user data storage?",
      "header": "Database",
      "multiSelect": false,
      "options": [
        {
          "label": "PostgreSQL",
          "description": "Relational database with ACID guarantees, best for structured data"
        },
        {
          "label": "MongoDB",
          "description": "Document database, flexible schema, good for rapid iteration"
        },
        {
          "label": "Redis",
          "description": "In-memory cache/database, extremely fast but volatile"
        }
      ]
    }
  ]
}
```

### Example 2: Feature Selection (Multi-Select)

```json
{
  "questions": [
    {
      "question": "Which authentication features do you want to enable?",
      "header": "Auth",
      "multiSelect": true,
      "options": [
        {
          "label": "Email/Password",
          "description": "Traditional username and password authentication"
        },
        {
          "label": "OAuth 2.0",
          "description": "Third-party login (Google, GitHub, Facebook)"
        },
        {
          "label": "2FA",
          "description": "Two-factor authentication for enhanced security"
        },
        {
          "label": "Magic Links",
          "description": "Passwordless login via email links"
        }
      ]
    }
  ]
}
```

### Example 3: Multiple Related Questions

```json
{
  "questions": [
    {
      "question": "Which API architecture should we implement?",
      "header": "API Style",
      "multiSelect": false,
      "options": [
        {
          "label": "REST",
          "description": "Traditional HTTP methods, widely supported, simple"
        },
        {
          "label": "GraphQL",
          "description": "Flexible queries, reduces over-fetching, steeper learning curve"
        },
        {
          "label": "gRPC",
          "description": "High performance, binary protocol, good for microservices"
        }
      ]
    },
    {
      "question": "Should we implement API versioning from the start?",
      "header": "Versioning",
      "multiSelect": false,
      "options": [
        {
          "label": "Yes, URL-based",
          "description": "Versions in URL path (/v1/users). Explicit but verbose."
        },
        {
          "label": "Yes, header",
          "description": "Versions in headers. Cleaner URLs but less discoverable."
        },
        {
          "label": "Not yet",
          "description": "Start simple, add versioning when needed. Faster initial development."
        }
      ]
    }
  ]
}
```

### Example 4: Architectural Decision

```json
{
  "questions": [
    {
      "question": "How should we structure the application architecture?",
      "header": "Architecture",
      "multiSelect": false,
      "options": [
        {
          "label": "Monolith",
          "description": "Single codebase, simpler deployment, easier to start. May scale less flexibly."
        },
        {
          "label": "Microservices",
          "description": "Independent services, better scalability, more operational complexity."
        },
        {
          "label": "Modular Monolith",
          "description": "Monolith with clear module boundaries. Best of both worlds initially."
        }
      ]
    }
  ]
}
```

## BEST PRACTICES

### Write Clear Questions

**Good:**
- "Which caching strategy should we implement?"
- "What level of test coverage do you require?"
- "How should we handle user authentication?"

**Bad:**
- "Cache?" (too vague)
- "What do you think about testing?" (open-ended)
- "Authentication stuff?" (unclear)

### Provide Informative Descriptions

**Good:**
```json
{
  "label": "JWT",
  "description": "Stateless tokens stored client-side. Scales well but tokens can't be revoked easily."
}
```

**Bad:**
```json
{
  "label": "JWT",
  "description": "Token-based auth"
}
```

### Make Options Mutually Exclusive (unless multiSelect)

**Good (single select):**
- Option 1: "REST API"
- Option 2: "GraphQL API"
- Option 3: "gRPC API"

**Bad (single select):**
- Option 1: "REST API"
- Option 2: "Also add GraphQL"
- Option 3: "No API"

### Keep Headers Concise

**Good:**
- "Database"
- "Auth method"
- "Test type"
- "Deploy"

**Bad:**
- "Database Selection"
- "Authentication Method Choice"
- "Type of Testing Approach"

### Use multiSelect Appropriately

**Use multiSelect when:**
- User can choose multiple non-exclusive options
- Feature flags or configuration options
- Multiple integrations or plugins

**Don't use multiSelect when:**
- Choices are mutually exclusive
- Only one implementation path makes sense
- Combining options would cause conflicts

## COMMON MISTAKES

### Asking questions in plain text
```
BAD: "Should I use PostgreSQL or MongoDB?"
GOOD: Use AskUserQuestion tool with both options
```

### Too many options (>4)
```
BAD: Providing 6 framework choices
GOOD: Group into categories or ask in multiple rounds
```

### Not ending questions with "?"
```
BAD: "Select a database"
GOOD: "Which database should we use?"
```

### Vague option descriptions
```
BAD: "description": "Fast database"
GOOD: "description": "In-memory cache, <1ms latency, volatile storage"
```

### Including "Other" option manually
```
BAD: Adding {"label": "Other", "description": "Something else"}
GOOD: Remove it - "Other" is added automatically
```

## WORKFLOW INTEGRATION

### Typical Flow

1. **Identify decision point** requiring user input
2. **Formulate clear question** ending with "?"
3. **Research 2-4 valid options** with trade-offs
4. **Create option objects** with concise labels and informative descriptions
5. **Use AskUserQuestion tool** with proper structure
6. **Wait for user response** before proceeding
7. **Acknowledge choice** and implement accordingly

### After Receiving Answer

```markdown
User selected: [Option Label]

Proceeding with [Option Label] because [reason based on description].

Next steps:
1. [Implementation step 1]
2. [Implementation step 2]
```
