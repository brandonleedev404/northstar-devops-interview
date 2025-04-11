# Northstar — Interviewer guide

Northstar presents the interview challenge. Southstar is the fictional logistics company in every scenario; its incidents and infrastructure are exercise fixtures.

Assign one challenge by its exact nickname in the candidate's invitation email, and include submission instructions and any timebox adjustment. Give the candidate the current checkout. Challenges are independent; preceding challenges are not prerequisites. Score only the assigned brief and do not penalize unrelated inherited defects. No real cloud deployment is expected. All required outcomes are in the briefs.

The client-facing README links to an empty `challenge.zip` placeholder, as requested for this draft. It is not a runnable fallback package. Before distributing a usable fallback, replace it with the approved challenge bundle and update the README's placeholder notice.

Score each dimension 0–4 (0 absent; 1 partial; 2 works on the happy path; 3 meets criteria with useful validation; 4 also explains failure modes): correctness, verification, operational safety, communication. Suggested passing threshold: 12/16 with correctness and safety each at least 3. Calibrate against role seniority; speed and memorized syntax are not independent criteria.

Expected observations by challenge: health vs data readiness; least privilege and read-only operation; failure propagation and job dependencies; rollout availability; label matching, disruption budget and node spread; rates, denominators and sustained impact; explicit configuration and safe errors; atomic replacement and checksum verification; digest validation and failed rollout handling; utilization relative to requests and bounded scale behavior; separate rollout and eviction constraints, data path regression, and restore-first operations.

For the Recovery Mission incident, treat logs as the live-state evidence. They explicitly describe drift from the starter. Accept a fix preventing the missing data mount/path, a tested readiness improvement, or a justified rollout-availability correction. Reject force-deleting pods as the default recovery. Discuss scaling or restoring healthy capacity before eviction and retaining the previous working release.

Baseline service tests should pass at every tag. They intentionally do not assert every acceptance criterion. Ask candidates to demonstrate a failing regression test before a fix where appropriate. A local fake kubectl or numerical Prometheus fixture is acceptable when external runtimes are unavailable.

History was generated for this exercise as a synthetic stream of ticketed challenge additions. Tags are local and no remote is configured. No claims about real development dates or contributors are intended.

## Nicknames used in invitation emails

- **Pulse Check**
- **Sealed Container**
- **Green Light**
- **Safe Landing**
- **Steady Ship**
- **Signal Watch**
- **Right Address**
- **Safety Net**
- **Release Lock**
- **Room to Grow**
- **Recovery Mission**
