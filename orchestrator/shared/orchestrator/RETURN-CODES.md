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
All subagent delegations and state transitions MUST use one of these standardized return codes:

| Code      | Description                                           | Additional Information Required                                                                                                     |
|-----------|-------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------|
| SUCCESS   | Operation completed successfully                      | **MUST** provide: Summary of accomplishments, list of deliverables, validation checks passed, notable observations                  |
| FAILURE   | Operation failed and cannot proceed                   | **MUST** provide: Specific error reason, what was attempted, blocking issues, suggested remediation                                 |
| PARTIAL   | Operation partially completed                         | **MUST** provide: Items completed, items remaining, overall completion percentage, reason for partial completion                    |
| TIMEOUT   | Operation exceeded time limit                         | **MUST** provide: Last successful operation, time of timeout, estimated remaining work, checkpoint state for resume                 |
| MISSING   | Required resources or dependencies not found          | **MUST** provide: Specific missing items, where search was attempted, why items are required, possible alternatives                 |

### State Transition Mapping

| Current State | Return Code | Next State Action                                    |
|---------------|-------------|------------------------------------------------------|
| INIT          | SUCCESS     | Proceed to next state (CONTROLLER/WORK)             |
| INIT          | FAILURE     | Exit with error                                     |
| INIT          | MISSING     | Exit with missing requirements error                |
| WORK          | SUCCESS     | Proceed to TEST                                     |
| WORK          | FAILURE     | Exit with implementation error                       |
| WORK          | PARTIAL     | Continue WORK with remaining items                  |
| WORK          | TIMEOUT     | Save checkpoint and continue WORK                   |
| TEST          | SUCCESS     | Proceed to DONE                                     |
| TEST          | FAILURE     | Return to WORK with feedback                        |
| TEST          | PARTIAL     | Continue TEST with remaining validations            |
| DONE          | SUCCESS     | Return to CONTROLLER                                |
| DONE          | FAILURE     | Determine remediation path                          |
| DONE          | MISSING     | Return to appropriate state to fulfill requirements |