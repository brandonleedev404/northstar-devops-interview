# Northstar Logistics — DevOps interview

This coding exercise is for **Northstar Logistics**, a fictional company running a parcel tracking API. This is synthetic interview material, not a real company's repository or employment history. All Git authors, backdated timestamps, incidents, and business data were created for this exercise.

## Candidate brief

Our small platform team runs a Python service on Kubernetes. Traffic and operational requirements have grown over time. The interview challenge grows by one stage each quarter. Complete the stages in order, carrying your implementation and tests forward. Allow 75–90 minutes per stage; your interviewer will set the stopping stage for the session. Each stage asks for a focused change, tests or executable checks, and a short operational explanation. External cloud accounts and paid services are unnecessary.

Use Python 3.11 or later and Git. Docker and a local Kubernetes cluster are optional for relevant exercises. The service has no third-party Python dependencies.

```sh
python3 -m unittest discover -s tests -v
python3 -m app.server
# In another terminal:
curl -i http://127.0.0.1:8080/healthz
curl -i http://127.0.0.1:8080/readyz
```

`GET /shipments/PKG-1001` returns a sample parcel. `DATA_FILE` selects the JSON data file; `PORT` defaults to 8080. Bind address is localhost by default; containers set `HOST=0.0.0.0`. Do not expose the exercise to the public internet.

## Stages added each quarter

**Latest addition: Stage 6 (2025 Q2).** Each quarterly commit introduces the next stage and its supporting files. Earlier stages remain available, so this checkpoint contains Stages 1–6.

| Stage | Added | Focus |
| --- | --- | --- |
| [Stage 1](challenges/2024-Q1.md) | 2024 Q1 | Health and readiness |
| [Stage 2](challenges/2024-Q2.md) | 2024 Q2 | Container hardening |
| [Stage 3](challenges/2024-Q3.md) | 2024 Q3 | CI quality gate |
| [Stage 4](challenges/2024-Q4.md) | 2024 Q4 | Kubernetes rollout safety |
| [Stage 5](challenges/2025-Q1.md) | 2025 Q1 | Availability during maintenance |
| [Stage 6](challenges/2025-Q2.md) | 2025 Q2 | Actionable SLO alerting |

Start a solution branch from this checkpoint and work through the stages without switching tags between them:

```sh
git switch -c candidate/solution
cat challenges/2024-Q1.md
python3 -m unittest discover -s tests -v
```

The starter intentionally leaves each stage unsolved. Preserve fixes from completed stages and add regression checks as you progress. Later fixtures may describe a separate environment or incident; reconcile their assumptions with your implementation in `SOLUTION.md`.

To inspect how the challenge grew:

```sh
git log --format='%h %ad %s' --date=short
git tag --list 'stage-*' --sort=version:refname
git show stage-1:README.md
```

`stage-N` records the addition of Stage N. The matching `challenge-YYYY-qN` tag is a date-based alias for the same checkpoint. Historical snapshots list only stages introduced by that quarter. Reviewers should use `INTERVIEWER.md` on the default branch.

## Deliverable

Commit your solution on a new branch. Include a section for each completed stage in `SOLUTION.md` with assumptions, commands run and results, rollout and rollback steps, and remaining risks. Explain how you would validate cluster-dependent behavior when no cluster is available. Never add real credentials. Manifests and workflows are interview fixtures; they deliberately contain defects and require review before use.
