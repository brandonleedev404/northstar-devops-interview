# Safe Landing

Make rollouts safe

**Timebox:** 75–90 minutes. **Scenario company:** Southstar (fictional).

## Scenario

A deployment replaced working pods before replacements could serve traffic.

## Scope

Work in `deploy/k8s.yaml`. Complete this challenge if it is the one specified in your invitation email. Other challenges are not prerequisites; address existing defects only when needed for the acceptance criteria below. Add validation and record results in `SOLUTION.md`. The checkpoint contains starter material, not completed solutions.

## Acceptance criteria

- Use the distinct health/readiness endpoints correctly and allow startup time.
- Define resource requests/limits and a rolling strategy that preserves two ready replicas at desired capacity three.
- Describe observable rollout success and a rollback command; validate YAML locally or on a disposable cluster.

## Discussion

Explain the tradeoff you made, how you would roll out the change, and what evidence would cause you to roll back. State which checks were actually run and which require infrastructure.
