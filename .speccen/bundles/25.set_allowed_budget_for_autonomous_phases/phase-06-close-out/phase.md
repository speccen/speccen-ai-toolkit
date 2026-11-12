---
type: Phase
phase: "06 — Close-out"
status: COMPLETE
description: Three audience seeds, feature node and graduated specification written; review decided — ceiling 10, five entries graduated, skill files committed
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

Decided by the Architect in the review round (log 21:58): "1 max loop 10; rest yes;". R/1 overrides DD-12 (ceiling 10); R/2 adopts DD-14; R/3 adopts DD-30 – DD-32; R/4 promotes G-1 – G-5 as proposed (G-2 with the ceiling 10) and keeps G-6, G-7 local; R/5 commits the three skill files. Written at 21:59: `.speccen/decisions/2026-11-11.fix_progress_by_breaches.md`, `2026-11-11.fix_budget_ceiling_10.md`; `.speccen/lessons/2026-11-11.text_checks_read_their_place.md`, `2026-11-11.repair_every_case_of_a_breach.md`, `2026-11-11.write_lists_and_summary_last.md`; the feature node's `produced` list; store index and timeline.

| # | Candidate | Kind | Proposed | Evidence |
|---|---|---|---|---|
| G-1 | Progress is measured by rule breaches that come back, or more failed rows — not by fewer failed rows (DD-14) | decision | promote, if the review confirms DD-14 | A fence: a later change may return to the brief's "fewer rows"; Phase 02 runs 4 – 6 converged with the same row count ([DD-14](../delegated-decisions.md#dd-14)) |
| G-2 | The fix budget is capped at 3; an invalid value counts as 1 (DD-12) — overridden to 10 | decision | promote, if the review confirms DD-12 | A fence against "loop until it passes"; the Architect's 15:45 words point the other way ([DD-12](../delegated-decisions.md#dd-12)) |
| G-3 | Lesson: a text check reads only the place its Test Plan row names, and an "unchanged" part compares that place with the base; run a move test before the verifier | lesson | promote | Most failures of the Phase 05 accept's eight verifier runs and three stop rounds ([Phase 05 summary](../phase-05-implementation/summary.md#delegate-gate-check)) |
| G-4 | Lesson: repair every case of a breach type, not only the cases the verifier names | lesson | promote | Phase 05 runs 3 – 7 each found the next case of the same type ([log.md](../log.md)) |
| G-5 | Lesson: write decision records and final edits first; lists, render and summary last; no decision ranges in lists | lesson | promote | Phase 04 stop round 04/2 ([Phase 04 summary](../phase-04-specification/summary.md#stop)) |
| G-6 | Lesson: read log times from `date`, never estimate | lesson | keep local | A single slip, corrected at once (log 21:08); the governing rule already asks for a correct log |
| G-7 | DD-10 / DD-16 — Phase 05 accept uses the budget; self-check line "N corrections" | decision | keep local | Both are stated in the skill text itself; no fence beyond it |

<a id="outcome"></a>
## Outcome

Close-out complete. The Architect's review set the ceiling to 10 and approved the rest; the three skill files are committed with the bundle.

<a id="open-items"></a>
## Open Items

| # | Item | Status |
|---|---|---|
| DD-12 | OVERRIDDEN (ceiling 10); ADR [2026-11-11.fix_budget_ceiling_10](../adrs/2026-11-11.fix_budget_ceiling_10.md) scribed on the Architect's request | closed |
| DD-14, DD-30 – DD-32 | ADOPTED | closed |
| G-1 – G-7 | Graduation proposal | decided |
| C-1 | Commit the three skill files | done (R/5) |
| C-3 | The specification stated a ceiling of 3 (R-6) after the override | closed 2026-11-12: specification amended to ceiling 10, default 5 (ADR 2026-11-12) |
| C-2 | The first measurement of the budget comes from the next autonomous bundle ([doc-technical.md](./doc-technical.md) Results) | follow-up |
