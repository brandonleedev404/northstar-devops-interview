# Steady Ship

Survive node maintenance

**Timebox:** 75–90 minutes. **Scenario company:** Southstar (fictional).

## Scenario

A routine node drain interrupted shipment lookups for several minutes.

## Scope

Work in `deploy/k8s.yaml, deploy/pdb.yaml, fixtures/maintenance.md`. Complete this challenge if it is the one specified in your invitation email. Other challenges are not prerequisites; address existing defects only when needed for the acceptance criteria below. Add validation and record results in `SOLUTION.md`. The supplied files contain starter material, not completed solutions.

## Acceptance criteria

- Correct the PDB selector and budget so a healthy three-replica workload permits only one voluntary disruption at a time.
- Spread replicas across three hostnames and explain behavior if only two nodes are available.
- Describe drain verification and the difference between eviction protection and rolling-update strategy.

## Discussion

Explain the tradeoff you made, how you would roll out the change, and what evidence would cause you to roll back. State which checks were actually run and which require infrastructure.
