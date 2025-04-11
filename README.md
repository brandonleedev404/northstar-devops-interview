# Northstar — DevOps challenge

Welcome to the DevOps interview challenge for **Northstar**. In these exercises, you will work with **Southstar**, a fictional logistics company whose platform team supports a parcel tracking API. Each scenario explores an operational problem as Southstar’s service grows.

**The challenge required will be specified in your invitation email.** Find that nickname below and follow the linked brief. Each challenge is self-contained; you do not need to complete the others. Unless your email specifies otherwise, allow 75–90 minutes for your solution.

## Find your challenge

Challenges are added over time, with earlier challenges remaining available.

| Challenge |
| --- |
| [Pulse Check](challenges/pulse-check.md) |
| [Sealed Container](challenges/sealed-container.md) |
| [Green Light](challenges/green-light.md) |
| [Safe Landing](challenges/safe-landing.md) |
| [Steady Ship](challenges/steady-ship.md) |
| [Signal Watch](challenges/signal-watch.md) |
| [Right Address](challenges/right-address.md) |
| [Safety Net](challenges/safety-net.md) |
| [Release Lock](challenges/release-lock.md) |
| [Room to Grow](challenges/room-to-grow.md) |
| [Recovery Mission](challenges/recovery-mission.md) |

## Get started

Use Python 3.11 or later and Git. The API has no third-party Python dependencies. Docker and a local Kubernetes cluster are optional for relevant challenges; no paid services or cloud accounts are required.

Create a branch for your solution and run the baseline tests from this directory:

```sh
git switch -c candidate/solution
python3 -m unittest discover -s tests -v
python3 -m app.server
```

In another terminal:

```sh
curl -i http://127.0.0.1:8080/healthz
curl -i http://127.0.0.1:8080/readyz
curl -i http://127.0.0.1:8080/shipments/PKG-1001
```

`DATA_FILE` selects the JSON data file; `PORT` defaults to 8080. The service binds to localhost by default; containers set `HOST=0.0.0.0`.

Work from the supplied checkout. The starter contains deliberate defects. Keep your changes focused on the challenge named in your email and add checks demonstrating your solution.

## Having trouble running the challenge?

A ZIP is included at [challenge.zip](challenge.zip). **This copy is an empty placeholder and contains no challenge files.** If setup issues prevent you from proceeding, reply to your invitation email with the command you ran and the error output so your contact can help.

## What to submit

Return your solution using the submission instructions in your email. Include your code changes and a `SOLUTION.md` describing:

- Your assigned challenge nickname and the changes you made.
- Assumptions, checks you ran, and their results.
- Rollout and rollback steps, plus any remaining risks.

If a check requires infrastructure you do not have, explain how you would verify it. Do not include real credentials.

---

Southstar is a fictional company used for the scenarios. This repository is interview material with synthetic authors, incidents, and a simulated history of challenge additions. Its deployment fixtures intentionally contain defects and require review before use.
