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
| **Status** | ADOPTED — the Architect, review round (log 2026-11-18 09:16, "other 16 is 'yes'") |

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
| **Status** | ADOPTED — the Architect, review round (log 2026-11-18 09:16, "other 16 is 'yes'") |

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
| **Status** | ADOPTED — the Architect, review round (log 2026-11-18 09:16, "other 16 is 'yes'") |

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
| **Status** | ADOPTED — the Architect, review round (log 2026-11-18 09:16, "other 16 is 'yes'") |

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
| **Status** | ADOPTED — the Architect, review round (log 2026-11-18 09:16, "other 16 is 'yes'") |

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
| **Status** | ADOPTED — the Architect, review round (log 2026-11-18 09:16, "other 16 is 'yes'") |

<a id="dd-7"></a>
## DD-7 — Verification 1: append `\b` to the `sdd-(…)` group

|     | Info |
| --- | --- |
| **Phase** | COMPLIANCE & REVIEW PHASE |
| **When** | 2026-11-18 07:07 UTC |
| **Question** | Tighten the brief's Verification 1 search so `sdd-reconcile` no longer matches, and keep its expected result "matches only in the README upgrade note"? |
| **Interview question** | [`03/1`](./phase-03-compliance-review/phase.md#interview) |
| **Decision** | Decided under delegation (autonomous): append `\b` to the `sdd-(governing-audit\|recon\|dimension-analysis\|scorecard-review\|synthesis)` group; the rest of the search is unchanged. At HEAD it gives 32 hits, none `sdd-reconcile`. |
| **Basis** | Brief, Verification 1 expected result ([log.md](./log.md), 07:58); Phase 02 restatement inventory group C (9 `sdd-reconcile` hits); the HEAD check in [phase-03 Compliance Iterations](./phase-03-compliance-review/phase.md#compliance). |
| **Alternatives** | a trailing `/` after the group (misses a bare `sdd-recon` without a slash); `\| grep -v sdd-reconcile` (hides any line that holds both) |
| **Materiality** | MATERIAL — unconfirmed (changes an acceptance check; taken under `stops: proceed`) |
| **Status** | ADOPTED — the Architect, review round (log 2026-11-18 09:16, "other 16 is 'yes'") |

<a id="dd-8"></a>
## DD-8 — Leave the stale `ARCHITECTURE.md:307` sdd path

|     | Info |
| --- | --- |
| **Phase** | COMPLIANCE & REVIEW PHASE |
| **When** | 2026-11-18 07:07 UTC |
| **Question** | Leave `ARCHITECTURE.md:307` (`skills/sdd/NN-*/SKILL.md`) as it is and name it in the end-of-run report as a follow-up? |
| **Interview question** | [`03/2`](./phase-03-compliance-review/phase.md#interview) |
| **Decision** | Decided under delegation (autonomous): leave it; report it as a follow-up. |
| **Basis** | Brief, "keep this commit a pure rename" and Goal limited to `skills/audit/` ([log.md](./log.md), 07:58). |
| **Alternatives** | fix it in this commit |
| **Materiality** | not material |
| **Status** | OVERRIDDEN — the Architect, review round 06/12 (log 2026-11-18 08:46): "dd-8 update both readme and architecture md's". Override ADR and Phase 03 re-entry pending (ADR Protocol). |

<a id="dd-9"></a>
## DD-9 — Stage `description:` lines: name only

|     | Info |
| --- | --- |
| **Phase** | COMPLIANCE & REVIEW PHASE |
| **When** | 2026-11-18 07:07 UTC |
| **Question** | In the four stage skills, replace `app-maturity-audit` with `audit-maturity` in `description:` and change no other word? |
| **Interview question** | [`03/3`](./phase-03-compliance-review/phase.md#interview) |
| **Decision** | Decided under delegation (autonomous): yes. |
| **Basis** | Brief, Required change 8 and Invariant "No content changes to the skills beyond path and name references" ([log.md](./log.md), 07:58); Phase 02 restatement inventory group B. |
| **Alternatives** | leave the descriptions (Verification 1 would then fail) |
| **Materiality** | not material |
| **Status** | ADOPTED — the Architect, review round (log 2026-11-18 09:16, "other 16 is 'yes'") |

<a id="dd-10"></a>
## DD-10 — README upgrade note names the audit rename

|     | Info |
| --- | --- |
| **Phase** | SPECIFICATION PHASE |
| **When** | 2026-11-18 07:10 UTC |
| **Question** | Besides the two README edits the brief names, also say in the note's first sentence that the audit folders were renamed? |
| **Interview question** | [`04/1`](./phase-04-specification/phase.md#interview) |
| **Decision** | Decided under delegation (autonomous): yes — the planned note in [phase-04 Proposed Changes Summary](./phase-04-specification/phase.md#implementation-plan). |
| **Basis** | Brief, Goal "Use `1c41496` as the model for scope and style" ([log.md](./log.md), 07:58); the `1c41496` note names the renamed folders. |
| **Alternatives** | only the two named edits, leaving "from before the `sdd-` prefix" as the note's opening |
| **Materiality** | not material |
| **Status** | ADOPTED — the Architect, review round (log 2026-11-18 09:16, "other 16 is 'yes'") |

<a id="dd-11"></a>
## DD-11 — Verification 4 on a synthetic run in the scratchpad

|     | Info |
| --- | --- |
| **Phase** | SPECIFICATION PHASE |
| **When** | 2026-11-18 07:10 UTC |
| **Question** | Run the scripts on a synthetic 11-dimension run in the session scratchpad, beside a baseline stamped at `e824b5c`, and commit nothing? |
| **Interview question** | [`04/2`](./phase-04-specification/phase.md#interview) |
| **Decision** | Decided under delegation (autonomous): yes (T-4). |
| **Basis** | Brief, Verification 4 ([log.md](./log.md), 07:58); Phase 02 baseline `212cd4db08e1`. |
| **Alternatives** | a run under `.speccen/audits/` of this repository |
| **Materiality** | not material |
| **Status** | ADOPTED — the Architect, review round (log 2026-11-18 09:16, "other 16 is 'yes'") |

<a id="dd-12"></a>
## DD-12 — Checks in `files/phase-05-text-checks.py`

|     | Info |
| --- | --- |
| **Phase** | SPECIFICATION PHASE |
| **When** | 2026-11-18 07:10 UTC |
| **Question** | Keep the checks as `files/phase-05-text-checks.py` in this bundle, outside the code commit? |
| **Interview question** | [`04/3`](./phase-04-specification/phase.md#interview) |
| **Decision** | Decided under delegation (autonomous): yes. |
| **Basis** | DD-2; earlier bundles keep their checks in `files/`. |
| **Alternatives** | run the checks inline only, with no script kept |
| **Materiality** | not material |
| **Status** | ADOPTED — the Architect, review round (log 2026-11-18 09:16, "other 16 is 'yes'") |

<a id="dd-13"></a>
## DD-13 — Deviation 1: run T-4 in Python UTF-8 mode

|     | Info |
| --- | --- |
| **Phase** | IMPLEMENTATION PHASE |
| **When** | 2026-11-18 07:17 UTC |
| **Question** | `build_scorecard.py` fails on this Windows host with a cp1252 `UnicodeEncodeError`; run the T-4 commands with `-X utf8` and leave the unchanged scorer as it is? |
| **Interview question** | — (Phase 05 deviation, [Deviation 1](./phase-05-implementation/phase.md#deviations)) |
| **Decision** | Decided under delegation (autonomous): APPROVED — T-4 runs with `-X utf8`; the encoding defect is a follow-up outside this change. |
| **Basis** | Brief, Invariant "Do **not** edit … `build_scorecard.py` (not even its docstring)" ([log.md](./log.md), 07:58); T-6 (the scorer is byte-identical to `e824b5c`). |
| **Alternatives** | fix `build_scorecard.py` here (breaks the hash invariant); stop and ask |
| **Materiality** | not material |
| **Status** | ADOPTED — the Architect, review round (log 2026-11-18 09:16, "other 16 is 'yes'") |
