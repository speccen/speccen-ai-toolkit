---
type: DelegatedDecisions
description: Decisions taken under delegation in autonomous mode — review, adopt or override
---

# rename audit skills — Delegated Decisions

[Index](./index.md) · [State](./STATE.md) · [Log](./log.md)

---

<a id="dd-1"></a>
## DD-1 — Store scope: the whole `.speccen/` stays unchanged

|     | Info |
| --- | --- |
| **Phase** | FEATURE ANALYSIS PHASE |
| **When** | 2026-11-18 07:00 UTC |
| **Question** | Leave the whole `.speccen/` unchanged (the durable store entries too, not only `bundles/**`), apart from this bundle and its Phase 06 graduation? |
| **Interview question** | [`01/1`](./phase-01-feature-analysis/phase.md#interview) |
| **Decision** | Decided under delegation (autonomous): yes — no file under `.speccen/` outside this bundle is edited by the rename. |
| **Basis** | Brief, Verification 1 (`--exclude-dir=.speccen`) and Invariant ".speccen/ history" ([log.md](./log.md), 07:58). |
| **Alternatives** | update old audit paths in durable store entries |
| **Materiality** | not material |
| **Status** | DELEGATED |

<a id="dd-2"></a>
## DD-2 — "One commit" means one code commit

|     | Info |
| --- | --- |
| **Phase** | FEATURE ANALYSIS PHASE |
| **When** | 2026-11-18 07:00 UTC |
| **Question** | Read "one commit" as one commit for the code change, with the bundle's phase-boundary commits as separate commits on the same branch? |
| **Interview question** | [`01/2`](./phase-01-feature-analysis/phase.md#interview) |
| **Decision** | Decided under delegation (autonomous): yes — the rename is one commit with the brief's message; the bundle's `chore: complete … PHASE [skip ci]` commits are separate. |
| **Basis** | Brief, Delivery ([log.md](./log.md), 07:58); governing skill, Phase Transition Protocol step 6. |
| **Alternatives** | squash the bundle into the code commit; keep the bundle on another branch |
| **Materiality** | not material |
| **Status** | DELEGATED |

<a id="dd-3"></a>
## DD-3 — Push and PR wait for the Architect's go

|     | Info |
| --- | --- |
| **Phase** | FEATURE ANALYSIS PHASE |
| **When** | 2026-11-18 07:00 UTC |
| **Question** | After close-out, wait for the Architect's go before `git push` and opening the PR to `main`? |
| **Interview question** | [`01/3`](./phase-01-feature-analysis/phase.md#interview) |
| **Decision** | Decided under delegation (autonomous): yes — the run commits locally on `refactor/audit-prefixed-skill-names`; push and PR are put to the Architect at the end of the run. |
| **Basis** | Governing skill, stop condition 7 (external side effects); brief, Delivery ([log.md](./log.md), 07:58) names the PR but not when. |
| **Alternatives** | push and open the PR at the end of Phase 05 |
| **Materiality** | not material |
| **Status** | DELEGATED |

<a id="dd-4"></a>
## DD-4 — Commit message verbatim, no attribution

|     | Info |
| --- | --- |
| **Phase** | FEATURE ANALYSIS PHASE |
| **When** | 2026-11-18 07:00 UTC |
| **Question** | Use the brief's commit message verbatim, with no attribution trailer? |
| **Interview question** | [`01/4`](./phase-01-feature-analysis/phase.md#interview) |
| **Decision** | Decided under delegation (autonomous): yes. |
| **Basis** | Brief, Delivery ([log.md](./log.md), 07:58); governing skill, Invariant 6. |
| **Alternatives** | a message written in the run |
| **Materiality** | not material |
| **Status** | DELEGATED |

<a id="dd-5"></a>
## DD-5 — Reach: every restatement of an old name (working hypothesis)

|     | Info |
| --- | --- |
| **Phase** | FEATURE ANALYSIS PHASE |
| **When** | 2026-11-18 07:00 UTC |
| **Question** | Bring every place that restates an old audit name into line, beyond the places the brief lists? |
| **Interview question** | [`01/5`](./phase-01-feature-analysis/phase.md#interview) |
| **Decision** | Decided under delegation (autonomous): yes, as working hypothesis H-3; places found in Phase 02 (P02-3); historic records settle in Phase 03 (O-2). |
| **Basis** | Brief, Required change 8 ([log.md](./log.md), 07:58); lesson `2026-11-05.readme_restates_config_template`. |
| **Alternatives** | only the places the brief lists |
| **Materiality** | not material |
| **Status** | DELEGATED |

<a id="dd-6"></a>
## DD-6 — Hash baseline at `e824b5c` (working hypothesis)

|     | Info |
| --- | --- |
| **Phase** | FEATURE ANALYSIS PHASE |
| **When** | 2026-11-18 07:00 UTC |
| **Question** | Take the `rubric_hash` computed on `main` at `e824b5c` before any move as the reference for Verification 4? |
| **Interview question** | [`01/6`](./phase-01-feature-analysis/phase.md#interview) |
| **Decision** | Decided under delegation (autonomous): yes, as working hypothesis H-4; computed in Phase 02 (P02-4), checked in Phase 04 (O-3). |
| **Basis** | Brief, Verification 4 ([log.md](./log.md), 07:58). |
| **Alternatives** | a hash computed on the branch before Phase 05 |
| **Materiality** | not material |
| **Status** | DELEGATED |
