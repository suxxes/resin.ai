<!-- Updated: 2025-09-28 23:00:00 UTC -->

## STATE TRANSITION CODES

Internal codes for orchestrator state machine transitions. These are distinct from subagent RETURN-CODES.

### CRITICAL REQUIREMENTS
- **MUST** use these codes for all state transitions
- **MUST** validate code against current state
- **MUST** follow transition table in orchestration requirements
- **NEVER** use return codes for state transitions
- **NEVER** use transition codes for subagent returns

### Transition Code Definitions

| Code | Usage | Description |
|------|-------|-------------|
| **CONTINUE** | Move to next state | Current state completed successfully, proceed to next state in sequence |
| **LOOP** | Continue iteration | Continue processing remaining items in current loop |
| **RETRY** | Retry current state | Re-execute current state with modifications or fixes |
| **SKIP** | Skip current item | Skip current item due to issues, continue with next item |
| **EXIT** | Exit loop/orchestration | Exit current loop level or complete orchestration |

### State-Specific Transitions

#### INIT States
| Code | Next State | Condition |
|------|------------|-----------|
| CONTINUE | WORK | Planning/discovery complete |
| SKIP | CONTROLLER | Item cannot be processed |
| EXIT | (Parent) | Critical error requiring intervention |

#### WORK States
| Code | Next State | Condition |
|------|------------|-----------|
| CONTINUE | TEST | Implementation complete |
| RETRY | WORK | Partial implementation, continue |
| SKIP | CONTROLLER | Cannot implement, skip item |

#### TEST States
| Code | Next State | Condition |
|------|------------|-----------|
| CONTINUE | DONE | All tests passed |
| RETRY | WORK | Tests failed, needs fixes |
| LOOP | TEST | More tests to run |

#### DONE States
| Code | Next State | Condition |
|------|------------|-----------|
| CONTINUE | CONTROLLER | Validation complete |
| EXIT | (Parent) | Level complete |

#### CONTROLLER States
| Code | Next State | Condition |
|------|------------|-----------|
| LOOP | INIT | Next item found |
| EXIT | DONE | All items processed |

### Transition Validation

Before using a transition code:
1. Verify current state allows the transition
2. Check orchestration requirements for state table
3. Ensure next state is valid from current state
4. Update TodoWrite before transition
5. Report transition using REPORT-STATE-TRANSITION template