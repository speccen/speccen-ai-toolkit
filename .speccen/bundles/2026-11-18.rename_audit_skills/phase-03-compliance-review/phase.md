---
type: Phase
phase: "03 — Compliance & Review"
status: COMPLETE
description: Iteration 2 — ADR 2026-11-18.architecture_reading_guide_sdd_path (overrides DD-8) processed; O-4 – O-6 decided under delegation (tighten Verification 1 with \b, leave ARCHITECTURE.md:307, rename the stage description lines); Definition of Ready met
---

<a id="phase-top"></a>
# rename audit skills — Compliance & Review

[Index](../index.md) · [State](../STATE.md) · [Log](../log.md)

---

<a id="adrs"></a>
## ADRs in scope

| ADR | Tier | Status | Decision | Compliance |
|---|---|---|---|---|
| [2026-11-18.architecture_reading_guide_sdd_path](../adrs/2026-11-18.architecture_reading_guide_sdd_path.md#decision) | bundle | DECIDED | Fix the stale skills/sdd/NN-* path in ARCHITECTURE.md in this change, folded into the one code commit | compliant |

The bundle holds one ADR, scribed in the review round (iteration 2). The nine standing decisions in `.speccen/decisions/` govern the
workflow's own mechanics (search units, fix budget, self-check items, subjects, record repairs);
none constrains skill folder names, skill paths or the audit scripts, so none is in scope and
no override arises.

<a id="extensions"></a>
## Extensions applied

| Extension | Why | Where it applies | Outcome |
|---|---|---|---|
| — | — | — | No extensions for this phase |

<a id="compliance"></a>
## Compliance Iterations

### Iteration 1

No ADR to process. The open items carried from Phases 01 and 02 were put through the interview
(below):

| Item | From | Resolution |
|---|---|---|
| O-1 (P02-1 – P02-5) | Phase 01 | resolved in Phase 02: cited places match (H-1), no other script holds a folder name (H-2), 4 more references (H-3), hash name-only and baseline `212cd4db08e1` (H-4), manifests name groups only (P02-5) |
| O-2 | Phase 01 | closed in Phase 02: no historic records outside `.speccen/` |
| O-3 | Phase 01 | carried to Phase 04 (Test Plan) |
| O-4 | Phase 02 | decided: 03/1 — [DD-7](../delegated-decisions.md#dd-7), `MATERIAL — unconfirmed` |
| O-5 | Phase 02 | decided: 03/2 — [DD-8](../delegated-decisions.md#dd-8) |
| O-6 | Phase 02 | decided: 03/3 — [DD-9](../delegated-decisions.md#dd-9) |

**Kind confirmed:** refactoring — no behaviour changes; the one runtime path
(`compare_scorecards.py` rubric paths) resolves to the same files and the same hash.

**Check of the 03/1 pattern at HEAD:** the tightened search (`\b` after the `sdd-` group) gives
32 hits, none of them `sdd-reconcile` — the 41 of Phase 02 minus the 9 of group C. GNU grep 3.0
on this host supports `\b` in `-E`.

### Iteration 2 — ADR `2026-11-18.architecture_reading_guide_sdd_path`

Entered by the ADR Protocol after the review round (log 08:46, 09:15). The ADR overrides
[DD-8](../delegated-decisions.md#dd-8) (now `OVERRIDDEN`): the stale path in the reading guide is
fixed in this change.

| Item | Analysis update |
|---|---|
| Place | `ARCHITECTURE.md:307` — `` | A specific phase's behaviour | that phase's `skills/sdd/NN-*/SKILL.md` | `` (at `e824b5c` and at `6c6187c`). Earlier bundle files cited it as `:304`; corrected. |
| Target text | `` that phase's `skills/sdd/sdd-*/SKILL.md` `` — every sdd skill folder is `sdd-<role>` (`ls skills/sdd/`, 11 folders). |
| README | 06/18: no change. No stale sdd skill path exists in `README.md` (every cited `skills/…` path resolves; the `0N-*` names are the upgrade note's intended list; `phase-0N-*` are bundle folders). |
| Commit | 06/19: the fix is folded into `6c6187c` (after the rebase: `fdbc357`) with the same message (fixup + autosquash rebase of the unpushed branch); "one commit" and T-11 still hold. |
| Effect on DD-7 / Verification 1 | none — `NN-*` is not matched by the search |
| Phase 02 | the restatement inventory's "Adjacent" note and O-5 now read as in scope (by the ADR) |
| Phase 04 | plan step 3.2 and checks T-8, T-10 change; a check T-14 is added (Phase 04 addendum) |

Definition of Ready re-evaluated below: met.

<a id="interview"></a>
## Interview

Mode: `autonomous` (bundle config); `stops: proceed` (project config). Basis: the brief (log
07:58), the Phase 02 findings, the standing decisions (none bears). The three questions are
independent: one round.

**Round 1**

| # | Question | Depends on | Proposed | Answer |
|---|---|---|---|---|
| 03/1 | Verification 1 — tighten the brief's search by appending `\b` to the `sdd-(…)` group, so `sdd-reconcile` no longer matches, and keep the expected result "matches only in the README upgrade note"? Options: `\b` after the group; a trailing `/`; filtering with `grep -v sdd-reconcile`. | — | `\b` after the `sdd-(…)` group | delegate: `\b` after the group — basis: brief Verification 1 expected result and Invariant "No content changes … beyond path and name references" (log 07:58); Phase 02 group C (9 `sdd-reconcile` hits); the check above (32 hits, 0 `reconcile`) — [DD-7](../delegated-decisions.md#dd-7), `MATERIAL — unconfirmed` (changes an acceptance check; taken under `stops: proceed`) |
| 03/2 | `ARCHITECTURE.md:307` *(DD-8 later OVERRIDDEN by the Architect — iteration 2)* — leave the stale `skills/sdd/NN-*/SKILL.md` path as it is, and name it in the end-of-run report as a follow-up? | — | leave; report | delegate: leave; report — basis: brief "keep this commit a pure rename" and Goal limited to `skills/audit/` (log 07:58) — [DD-8](../delegated-decisions.md#dd-8) |
| 03/3 | Stage `description:` lines — in the four stage skills, replace `app-maturity-audit` with `audit-maturity` and change no other word? | — | yes | delegate: yes — basis: brief Required change 8 and Invariant "No content changes to the skills beyond path and name references" (log 07:58); Phase 02 group B — [DD-9](../delegated-decisions.md#dd-9) |

No question was answered "later"; no placeholder ADR is needed.

<a id="open-items"></a>
## Open Items

| # | Open item | Settles in |
|---|---|---|
| O-3 | Test Plan: Verification 1 (with the 03/1 pattern) – 5 as scoped checks; a minimal `dimensions/` fixture for `build_scorecard.py`; the hash compared with `212cd4db08e1`. | Phase 04 |
| O-7 | `[DD-7 \| Tighten Verification 1 with \b after the sdd- group?]` is `MATERIAL — unconfirmed`: it goes to the Architect in the review round. | review round |

<a id="outcome"></a>
## Outcome

**Definition of Ready**

| # | Criterion | Met | Evidence |
|---|---|---|---|
| 1 | Every ADR file has a compliance response | yes | [the ADR](../adrs/2026-11-18.architecture_reading_guide_sdd_path.md) — Compliance 2026-11-18 (iteration 2) |
| 2 | All open questions from Phases 01 and 02 resolved or escalated | yes | Compliance Iterations table: O-1, O-2 resolved; O-4 – O-6 decided; O-3 carried to Phase 04 |
| 3 | Project Conventions Confirmation complete | yes | [Phase 02 conventions](../phase-02-code-analysis/phase.md#conventions) |
| 4 | Domain understanding sufficient for the plan | yes | Phase 02 restatement inventory lists every place to change (groups A, B) |
| 5 | No unresolved ambiguity | yes | 03/1 – 03/3 settled the three remaining ones |
| 6 | Phase 01 items for Phases 02 and 03 resolved; kind confirmed | yes | O-1, O-2 resolved; kind: refactoring, confirmed above |
| 7 | Prototypes: choice recorded | n/a | no prototype run (`prototypes: 0`; no material choice with competing approaches to build) |
| 8 | The Architect or its delegate signalled readiness | yes | delegate readiness decision, basis rows 1 – 7 |

Definition of Ready satisfied. All criteria met. Ready for Phase 04 upon approval by the
Architect or its delegate.
