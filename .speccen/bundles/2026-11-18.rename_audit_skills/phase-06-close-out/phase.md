---
type: Phase
phase: "06 — Close-out"
status: COMPLETE
description: Three outcome seeds written; feature node and specification graduated; review round decided — 2 lessons promoted, DD-8 overridden by ADR and fixed
---

<a id="phase-top"></a>
# rename audit skills — Close-out

[Index](../index.md) · [State](../STATE.md) · [Log](../log.md)

---

<a id="extensions"></a>
## Extensions applied

| Extension | Why | Where it applies | Outcome |
|---|---|---|---|
| — | — | — | No extensions for this phase |

<a id="documentation"></a>
## Documentation

- Checklist: 27 of 27 items ticked in the [Implementation Plan](../phase-04-specification/phase.md#implementation-plan); none skipped.
- Seeds written inline (short; no subagent): [doc-executive.md](./doc-executive.md), [doc-business.md](./doc-business.md), [doc-technical.md](./doc-technical.md). The executive and business seeds link the Phase 04 intent seeds; outcome = intent, plus one risk found (the scorer's encoding defect).
- Feature node: `.speccen/features/2026-11-18.rename_audit_skills/node.md` — spine `work-kind: refactoring`, `date`, `touches: [maturity-audit, readme]` (new tags; no existing tag names these components), `produced` lists the two promoted lessons (review round).
- Specification graduated: `specification.html` and `specification.md` copied into the feature folder, bundle links repointed to `../../bundles/2026-11-18.rename_audit_skills/…`; every relative link resolves. `specification` edge set.
- Store `index.md` (Features) and `timeline.md` regenerated with the new node. No override exists (no ADR), so path 1 writes nothing.

<a id="graduation-proposal"></a>
## Graduation Proposal

Decided by the Architect in the review round (log 09:16, "other 16 is 'yes'"): 06/1 and 06/2 promoted
and written to `.speccen/lessons/`; 06/3 and 06/4 kept local.

| # | Candidate | Kind | Evidence | Proposed |
|---|---|---|---|---|
| 06/1 | `[06/1 \| The audit scorer fails on Windows without UTF-8 mode, and a fix changes the rubric hash]` | lesson | [Deviation 1](../phase-05-implementation/phase.md#deviations); `build_scorecard.py:391` `write_text()` without `encoding`; the hash covers the scorer's bytes (`compare_scorecards.py:34`) | promote — every audit run on Windows hits it, and the hash coupling is a fence a later fix must know about |
| 06/2 | `[06/2 \| Audit runs on the same day sort by id, so a run named before "baseline" is taken as the earlier run]` | lesson | [Phase 05 T-4 fixture correction](../phase-05-implementation/phase.md#implementation-summary); `compare_scorecards.py` `load_all()` sorts by `(date, id)` | promote — it holds for every audit time series, not only this test |
| 06/3 | `[06/3 \| A rename check must not match a longer real name — end the pattern with \b]` | lesson | [DD-7](../delegated-decisions.md#dd-7); 9 `sdd-reconcile` false hits | keep local — the general rule is already in lesson `2026-11-11.text_checks_read_their_place` |
| 06/4 | `[06/4 \| Find a README block by its first line, not by a line number]` | note | Phase 04 verifier slip (K-7, line 129 blank) | keep local — a one-off citation slip |

Written: [`2026-11-18.audit_scorer_needs_utf8_and_fix_changes_hash`](../../../lessons/2026-11-18.audit_scorer_needs_utf8_and_fix_changes_hash.md), [`2026-11-18.same_day_audit_runs_sort_by_id`](../../../lessons/2026-11-18.same_day_audit_runs_sort_by_id.md) (`kind: lesson`, `weight: brief`, `produced-by` this feature); the feature node's `produced` lists both; store index and timeline regenerated.

DD-8 was overridden by the Architect (06/12) — ADR `2026-11-18.architecture_reading_guide_sdd_path`; the fix is in `fdbc357` (Phases 03 – 05, iteration 2). The specification was re-assembled and graduated again.

Follow-up outside this change (not a store entry): the stale counts named in the brief's Out of scope.

<a id="open-items"></a>
## Open Items

| # | Item | Settles in |
|---|---|---|
| O-9 | `[DD-3 \| Push and PR wait for the Architect]` | the Architect |

<a id="outcome"></a>
## Outcome

The core workflow is complete. The rename is in commit `fdbc357`; the bundle, the feature node
and the graduated specification are committed with the close-out commit. The review round is decided: 12 decisions adopted, DD-8 overridden (ADR), 2 lessons promoted.
