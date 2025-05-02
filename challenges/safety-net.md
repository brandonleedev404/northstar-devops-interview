# Safety Net

Prove backups can be restored

**Timebox:** 75–90 minutes. **Scenario company:** Southstar (fictional).

## Scenario

A successful backup job produced an empty file after a source path typo.

## Scope

Work in `scripts/backup.sh, scripts/restore.sh`. Complete this challenge if it is the one specified in your invitation email. Other challenges are not prerequisites; address existing defects only when needed for the acceptance criteria below. Add validation and record results in `SOLUTION.md`. The supplied files contain starter material, not completed solutions.

## Acceptance criteria

- Fail on missing source, invalid JSON, or copy errors and never overwrite the last good backup on failure.
- Publish backups atomically with a checksum and verify integrity before restoring.
- Exercise round trip, corruption, and interrupted or failed backup behavior in a temporary directory; existing data must survive a failed restore.

## Discussion

Explain the tradeoff you made, how you would roll out the change, and what evidence would cause you to roll back. State which checks were actually run and which require infrastructure.
