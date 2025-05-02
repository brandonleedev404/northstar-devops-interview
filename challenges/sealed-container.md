# Sealed Container

Harden the container

**Timebox:** 75–90 minutes. **Scenario company:** Southstar (fictional).

## Scenario

The security review found a root process and unnecessary files in the image.

## Scope

Work in `Dockerfile, .dockerignore`. Complete this challenge if it is the one specified in your invitation email. Other challenges are not prerequisites; address existing defects only when needed for the acceptance criteria below. Add validation and record results in `SOLUTION.md`. The supplied files contain starter material, not completed solutions.

## Acceptance criteria

- Use a versioned Python base, a non-root runtime user, and only required runtime files.
- The container must serve shipments on port 8080 with a read-only root filesystem.
- Document build/run validation and how base-image updates will be maintained.

## Discussion

Explain the tradeoff you made, how you would roll out the change, and what evidence would cause you to roll back. State which checks were actually run and which require infrastructure.
