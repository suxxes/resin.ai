<!-- Updated: 2025-09-28 00:00:00 UTC -->

## RETURN CODES

### CRITICAL REQUIREMENTS
- **MUST** use only standardized return codes (SUCCESS, FAILURE, PARTIAL, TIMEOUT, MISSING)
- **MUST** provide additional information for every return code
- **MUST** include return codes in all state transitions
- **MUST** log all return codes in audit trail
- **MUST** track return codes for progress metrics
- **MUST** escalate on consecutive failures (3x FAILURE or 2x TIMEOUT)
- **MUST** stop orchestration on MISSING after INIT

### CRITICAL RESTRICTIONS
- **NEVER** use custom or non-standard return codes
- **NEVER** return a code without required additional information
- **NEVER** ignore return codes in state transitions
- **NEVER** proceed without validating return code
- **NEVER** continue after escalation thresholds

### Standard Return Codes
All agent delegations and state transitions MUST use one of these standardized return codes:

| Code    | Description                                  |
|---------|----------------------------------------------|
| SUCCESS | Operation completed successfully             |
| FAILURE | Operation failed and cannot proceed          |
| PARTIAL | Operation partially completed                |
| TIMEOUT | Operation exceeded time limit                |
| MISSING | Required resources or dependencies not found |

### State Transition Mapping

| Current State | Return Code | Next State Action                                   |
|---------------|-------------|-----------------------------------------------------|
| INIT          | SUCCESS     | Proceed to next state (LOOP or WORK)                |
| INIT          | FAILURE     | Exit with error                                     |
| INIT          | MISSING     | Exit with missing requirements error                |
| WORK          | SUCCESS     | Proceed to TEST                                     |
| WORK          | FAILURE     | Exit with implementation error                      |
| WORK          | PARTIAL     | Continue WORK with remaining items                  |
| WORK          | TIMEOUT     | Save checkpoint and continue WORK                   |
| TEST          | SUCCESS     | Proceed to DONE                                     |
| TEST          | FAILURE     | Return to WORK with feedback                        |
| TEST          | PARTIAL     | Continue TEST with remaining validations            |
| DONE          | SUCCESS     | Return to LOOP                                      |
| DONE          | FAILURE     | Determine remediation path                          |
| DONE          | MISSING     | Return to appropriate state to fulfill requirements |
