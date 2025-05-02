# Pulse Check

Readiness lies during data outages

**Timebox:** 75–90 minutes. **Scenario company:** Southstar (fictional).

## Scenario

Support saw 503 shipment responses while every pod stayed ready.

## Scope

Work in `app/server.py, tests/`. Complete this challenge if it is the one specified in your invitation email. Other challenges are not prerequisites; address existing defects only when needed for the acceptance criteria below. Add validation and record results in `SOLUTION.md`. The supplied files contain starter material, not completed solutions.

## Acceptance criteria

- Make /readyz return 503 for missing, malformed, or non-object JSON data and 200 for valid data.
- Keep /healthz at 200 during a data outage; shipment requests must not crash on non-object JSON.
- Add regression tests for failure and recovery; explain why liveness must not depend on data.

## Discussion

Explain the tradeoff you made, how you would roll out the change, and what evidence would cause you to roll back. State which checks were actually run and which require infrastructure.
