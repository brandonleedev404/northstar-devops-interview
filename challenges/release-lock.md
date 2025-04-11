# Release Lock

Deploy exactly the approved release

**Timebox:** 75–90 minutes. **Scenario company:** Southstar (fictional).

## Scenario

Rollback pulled a different image because the latest tag had moved.

## Scope

Work in `scripts/deploy.sh, release/example.env`. Complete this challenge if it is the one specified in your invitation email. Other challenges are not prerequisites; address existing defects only when needed for the acceptance criteria below. Add validation and record results in `SOLUTION.md`. The checkpoint contains starter material, not completed solutions.

## Acceptance criteria

- Require an explicit namespace and immutable image digest; reject empty or tag-only references.
- Update only the parcel-api container, wait for rollout with a timeout, and return nonzero on failure.
- Use a fake kubectl executable to verify argument handling and failure behavior without contacting a cluster; document rollback.

## Discussion

Explain the tradeoff you made, how you would roll out the change, and what evidence would cause you to roll back. State which checks were actually run and which require infrastructure.
