# Right Address

Separate production configuration

**Timebox:** 75–90 minutes. **Scenario company:** Southstar (fictional).

## Scenario

A staging deployment used the production endpoint after a copy-and-paste change.

## Scope

Work in `config/, scripts/render_config.py`. Complete this challenge if it is the one specified in your invitation email. Other challenges are not prerequisites; address existing defects only when needed for the acceptance criteria below. Add validation and record results in `SOLUTION.md`. The checkpoint contains starter material, not completed solutions.

## Acceptance criteria

- Require an explicit supported environment; remove silent production fallback.
- Validate required endpoint and port settings and avoid printing secret values in errors or output.
- Test valid staging/production selection, unknown environments, and missing required keys using local fixtures.

## Discussion

Explain the tradeoff you made, how you would roll out the change, and what evidence would cause you to roll back. State which checks were actually run and which require infrastructure.
