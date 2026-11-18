---
type: Phase
phase: "06 — Close-out"
status: COMPLETE
description: Three outcome seeds written; feature node and specification graduated; graduation proposal (06/1 – 06/4) pending the Architect
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
- Feature node: `.speccen/features/2026-11-18.rename_audit_skills/node.md` — spine `work-kind: refactoring`, `date`, `touches: [maturity-audit, readme]` (new tags; no existing tag names these components), `produced: []` (nothing graduated yet — the proposal below is pending).
- Specification graduated: `specification.html` and `specification.md` copied into the feature folder, bundle links repointed to `../../bundles/2026-11-18.rename_audit_skills/…`; every relative link resolves. `specification` edge set.
- Store `index.md` (Features) and `timeline.md` regenerated with the new node. No override exists (no ADR), so path 1 writes nothing.

<a id="graduation-proposal"></a>
## Graduation Proposal

Pending the Architect (autonomous mode: path 2 is never decided by the delegate). Nothing
discretionary was written to `.speccen/`.

| # | Candidate | Kind | Evidence | Proposed |
|---|---|---|---|---|
| 06/1 | `[06/1 \| The audit scorer fails on Windows without UTF-8 mode, and a fix changes the rubric hash]` | lesson | [Deviation 1](../phase-05-implementation/phase.md#deviations); `build_scorecard.py:391` `write_text()` without `encoding`; the hash covers the scorer's bytes (`compare_scorecards.py:34`) | promote — every audit run on Windows hits it, and the hash coupling is a fence a later fix must know about |
| 06/2 | `[06/2 \| Audit runs on the same day sort by id, so a run named before "baseline" is taken as the earlier run]` | lesson | [Phase 05 T-4 fixture correction](../phase-05-implementation/phase.md#implementation-summary); `compare_scorecards.py` `load_all()` sorts by `(date, id)` | promote — it holds for every audit time series, not only this test |
| 06/3 | `[06/3 \| A rename check must not match a longer real name — end the pattern with \b]` | lesson | [DD-7](../delegated-decisions.md#dd-7); 9 `sdd-reconcile` false hits | keep local — the general rule is already in lesson `2026-11-11.text_checks_read_their_place` |
| 06/4 | `[06/4 \| Find a README block by its first line, not by a line number]` | note | Phase 04 verifier slip (K-7, line 129 blank) | keep local — a one-off citation slip |

Follow-ups outside this change (not store entries): `[DD-8 | ARCHITECTURE.md:307 stale skills/sdd/NN-* path]`; the stale counts named in the brief's Out of scope.

<a id="open-items"></a>
## Open Items

| # | Item | Settles in |
|---|---|---|
| O-7 | `[DD-7 \| Tighten Verification 1 with \b after the sdd- group?]` — `MATERIAL — unconfirmed` | review round |
| O-9 | `[DD-3 \| Push and PR wait for the Architect]` | the Architect |
| O-11 | Graduation proposal 06/1 – 06/4 | review round |

<a id="outcome"></a>
## Outcome

The core workflow is complete. The rename is in commit `fdbc357`; the bundle, the feature node
and the graduated specification are committed with the close-out commit. The delegated decisions
and the graduation proposal wait for the Architect's review round.
