# Recovery Mission

Diagnose the failed rollout

**Timebox:** 75–90 minutes. **Scenario company:** Southstar (fictional).

## Scenario

A release stalled during planned node maintenance. Operations needs a safe recovery plan.

## Scope

Work in `fixtures/incident.log, deploy/, RUNBOOK.md`. Complete this challenge if it is the one specified in your invitation email. Other challenges are not prerequisites; address existing defects only when needed for the acceptance criteria below. Add validation and record results in `SOLUTION.md`. The checkpoint contains starter material, not completed solutions.

## Acceptance criteria

- Use the timestamped evidence to identify both the failed readiness check and blocked eviction without assuming one caused the other.
- Write RUNBOOK.md with diagnostic commands, safe recovery/rollback, and verification that service capacity is restored.
- Implement one bounded manifest or service fix and regression validation; explain what needs separate follow-up.

## Discussion

Explain the tradeoff you made, how you would roll out the change, and what evidence would cause you to roll back. State which checks were actually run and which require infrastructure.
