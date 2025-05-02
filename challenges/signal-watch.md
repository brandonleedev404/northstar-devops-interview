# Signal Watch

Alert on customer impact

**Timebox:** 75–90 minutes. **Scenario company:** Southstar (fictional).

## Scenario

The current alert pages on any 500 while sustained API unavailability goes unnoticed.

## Scope

Work in `observability/alerts.yml, observability/metrics.md`. Complete this challenge if it is the one specified in your invitation email. Other challenges are not prerequisites; address existing defects only when needed for the acceptance criteria below. Add validation and record results in `SOLUTION.md`. The supplied files contain starter material, not completed solutions.

## Acceptance criteria

- Replace the raw counter threshold with an error-ratio alert over a time window, including 503 responses.
- Protect against low-traffic noise and counter resets; exclude health endpoints.
- Supply promtool rule tests or documented numerical fixtures for healthy, sustained failure, reset, and zero-traffic cases.

## Discussion

Explain the tradeoff you made, how you would roll out the change, and what evidence would cause you to roll back. State which checks were actually run and which require infrastructure.
