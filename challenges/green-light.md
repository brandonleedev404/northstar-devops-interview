# Green Light

Stop shipping failed builds

**Timebox:** 75–90 minutes. **Scenario company:** Southstar (fictional).

## Scenario

A test failure appeared green in the build and a broken image was published.

## Scope

Work in `.github/workflows/ci.yml`. Complete this challenge if it is the one specified in your invitation email. Other challenges are not prerequisites; address existing defects only when needed for the acceptance criteria below. Add validation and record results in `SOLUTION.md`. The supplied files contain starter material, not completed solutions.

## Acceptance criteria

- A deliberately failing test must fail CI and prevent the image-build job.
- Use minimal workflow permissions, run tests on pull requests, and keep secrets unavailable to untrusted code.
- Build the Docker image only after successful tests; describe how you verified the negative case.

## Discussion

Explain the tradeoff you made, how you would roll out the change, and what evidence would cause you to roll back. State which checks were actually run and which require infrastructure.
