# Room to Grow

Right-size autoscaling

**Timebox:** 75–90 minutes. **Scenario company:** Southstar (fictional).

## Scenario

The service stayed at one pod while CPU saturation increased latency.

## Scope

Work in `deploy/hpa.yaml, fixtures/load.csv, deploy/k8s.yaml`. Complete this challenge if it is the one specified in your invitation email. Other challenges are not prerequisites; address existing defects only when needed for the acceptance criteria below. Add validation and record results in `SOLUTION.md`. The checkpoint contains starter material, not completed solutions.

## Acceptance criteria

- Align HPA target and Deployment identity; choose consistent CPU requests and a 3–8 replica range.
- Explain desired replicas using ceil(current replicas × observed utilization / target utilization) for the supplied load points.
- Configure scale-down stabilization; explain metrics-server prerequisites and why memory limits alone do not fix CPU saturation.

## Discussion

Explain the tradeoff you made, how you would roll out the change, and what evidence would cause you to roll back. State which checks were actually run and which require infrastructure.
