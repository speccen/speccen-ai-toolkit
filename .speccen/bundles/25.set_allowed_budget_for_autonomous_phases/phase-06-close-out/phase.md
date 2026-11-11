---
type: Phase
phase: "06 — Close-out"
status: COMPLETE
description: Three audience seeds, feature node and graduated specification written; graduation proposal and the skill-file commit pending the Architect
---

<a id="phase-top"></a>
# set allowed budget for autonomous phases — Close-out

[Index](../index.md) · [State](../STATE.md) · [Log](../log.md)

---

<a id="extensions"></a>
## Extensions applied

| Extension | Why | Where it applies | Outcome |
|---|---|---|---|
| — | — | — | No extensions for this phase: `.speccen/extensions/close-out/` does not exist |

## Checklist

All 29 Implementation Plan items are ticked; none skipped →
[Phase 04 plan](../phase-04-specification/phase.md#implementation-plan),
[Phase 05 Implementation Summary](../phase-05-implementation/phase.md#implementation-summary).

<a id="documentation"></a>
## Documentation

- [doc-executive.md](./doc-executive.md), [doc-business.md](./doc-business.md),
  [doc-technical.md](./doc-technical.md) — written inline, STE-styled with the Phase 04 word
  list ("stop", "answer", "fix attempt" nouns; "halt", "reply", "correct", "examine" verbs;
  "project file"). The executive and business seeds link their Phase 04 intent seeds;
  intended → delivered is the same, no deviation.

## Durable store

- Feature node `.speccen/features/25.set_allowed_budget_for_autonomous_phases/node.md` —
  `work-kind: fix`, `touches: [governing-workflow, configuration, gate-test]` (tags reused from
  the store), `produced: []`, `specification: ./specification.html`, a `builds-on` link to
  `2026-11-05.use_cheaper_subagent_to_work`.
- The specification (`specification.html` + `.md`) copied into the feature folder; its relative
  links rebased onto `../../bundles/25.set_allowed_budget_for_autonomous_phases/`, every target
  checked to exist.
- Store `index.md` (Features) and `timeline.md` updated.
- Overrides (path 1): none — no bundle ADR exists.
- Nothing discretionary written before the Architect decides the proposal below.

<a id="graduation-proposal"></a>
## Graduation Proposal

Pending the Architect (end-of-run review).

| # | Candidate | Kind | Proposed | Evidence |
|---|---|---|---|---|
| G-1 | Progress is measured by rule breaches that come back, or more failed rows — not by fewer failed rows (DD-14) | decision | promote, if the review confirms DD-14 | A fence: a later change may return to the brief's "fewer rows"; Phase 02 runs 4 – 6 converged with the same row count ([DD-14](../delegated-decisions.md#dd-14)) |
| G-2 | The fix budget is capped at 3; an invalid value counts as 1 (DD-12) | decision | promote, if the review confirms DD-12 | A fence against "loop until it passes"; the Architect's 15:45 words point the other way ([DD-12](../delegated-decisions.md#dd-12)) |
| G-3 | Lesson: a text check reads only the place its Test Plan row names, and an "unchanged" part compares that place with the base; run a move test before the verifier | lesson | promote | Most failures of the Phase 05 accept's eight verifier runs and three stop rounds ([Phase 05 summary](../phase-05-implementation/summary.md#delegate-gate-check)) |
| G-4 | Lesson: repair every case of a breach type, not only the cases the verifier names | lesson | promote | Phase 05 runs 3 – 7 each found the next case of the same type ([log.md](../log.md)) |
| G-5 | Lesson: write decision records and final edits first; lists, render and summary last; no decision ranges in lists | lesson | promote | Phase 04 stop round 04/2 ([Phase 04 summary](../phase-04-specification/summary.md#stop)) |
| G-6 | Lesson: read log times from `date`, never estimate | lesson | keep local | A single slip, corrected at once (log 21:08); the governing rule already asks for a correct log |
| G-7 | DD-10 / DD-16 — Phase 05 accept uses the budget; self-check line "N corrections" | decision | keep local | Both are stated in the skill text itself; no fence beyond it |

<a id="outcome"></a>
## Outcome

Close-out complete under delegation. The three skill files remain uncommitted in the working
tree (DD-24); the end-of-run report asks the Architect whether to commit them.

<a id="open-items"></a>
## Open Items

| # | Item | Status |
|---|---|---|
| DD-12, DD-14 | `MATERIAL — unconfirmed` decisions | pending the Architect (review round) |
| DD-30 – DD-32 | repairs past the current Step 7 text ("If it still fails, the delegate rejects") | pending the Architect (review round) |
| G-1 – G-7 | Graduation proposal | pending the Architect |
| C-1 | Commit the three skill files (DD-24 leaves them uncommitted) | pending the Architect |
| C-2 | The first measurement of the budget comes from the next autonomous bundle ([doc-technical.md](./doc-technical.md) Results) | follow-up |
