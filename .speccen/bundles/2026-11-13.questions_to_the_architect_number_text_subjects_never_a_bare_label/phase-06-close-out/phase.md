---
type: Phase
phase: "06 — Close-out"
status: COMPLETE
description: Three audience seeds, feature node and graduated specification written; graduation proposal and the review of the delegated decisions wait for the Architect
---

<a id="phase-top"></a>
# Questions to the Architect: [number | text] subjects, never a bare label — Close-out

[Index](../index.md) · [State](../STATE.md) · [Log](../log.md)

---

<a id="extensions"></a>
## Extensions applied

| Extension | Why | Where it applies | Outcome |
|---|---|---|---|
| — | — | — | No extensions for this phase: `.speccen/extensions/close-out/` does not exist |

## Checklist

Every Implementation Plan item is ticked; none skipped →
[Phase 04 plan](../phase-04-specification/phase.md#implementation-plan),
[Phase 05 Implementation Summary](../phase-05-implementation/phase.md#implementation-summary).

<a id="documentation"></a>
## Documentation

- [doc-executive.md](./doc-executive.md), [doc-business.md](./doc-business.md),
  [doc-technical.md](./doc-technical.md) — STE-styled seeds. The executive and business seeds
  link their Phase 04 intent seeds; intended → delivered is the same, no deviation.

## Durable store

- Feature node `.speccen/features/2026-11-13.questions_to_the_architect_number_text_subjects_never_a_bare_label/node.md`
  — `work-kind: feature`, `touches: [governing-workflow, interview, gate-test]` (`interview` is
  a new tag; the other two reused), `produced: []`, `specification: ./specification.html`, a
  `builds-on` link to `25.set_allowed_budget_for_autonomous_phases`.
- The specification (`specification.html` + `.md`) copied into the feature folder; relative links
  rebased onto `../../bundles/2026-11-13.questions_to_the_architect_number_text_subjects_never_a_bare_label/`,
  every target checked to exist.
- Store `index.md` (Features) and `timeline.md` updated.
- Overrides (path 1): none — no bundle ADR exists.
- Nothing discretionary written before the Architect decides the proposal below.

<a id="graduation-proposal"></a>
## Graduation Proposal

Pending — the Architect decides in the review round.

| # | Candidate | Kind | Proposed | Evidence |
|---|---|---|---|---|
| G-1 | [G-1 \| The labels stay and travel inside a `[number \| text]` subject; dropping them, a glossary, or a trailing number were rejected] | decision | promote, if the review adopts DD-10 and DD-11 | A fence: brief §4 lists the three rejected alternatives and why; a later change could try one again ([brief](../files/gh-26-questions-subjects.md)) |
| G-2 | [G-2 \| A fix that only repairs how a decision is recorded is not a stop; the review round still shows each repair] | decision | promote | The Architect's own change (03/16, log 07:32); a fence against widening it to fixes that change what a decision decides ([scope addition](../phase-03-compliance-review/phase.md#scope-addition)) |
| G-3 | [G-3 \| Escape `\|` in every table cell, also inside backticks; write a rule about the escape itself in words] | lesson | promote | Phase 04 runs 1 – 2: table rows split and the escape vanished from R-1 and T-2 ([log.md](../log.md)) |
| G-4 | [G-4 \| A named breach kept on purpose still counts as no progress — take it out of the round instead] | lesson | promote | Phase 03 stop 2: 03/11 kept "for traceability" tripped the no-progress trigger ([Phase 03 summary](../phase-03-compliance-review/summary.md#stop-2)) |
| G-5 | [G-5 \| A stop question should propose the fix budget after the answer; without it the default is one verifier run] | lesson | promote | Phase 03 stop 2 came only from that default (03/23) ([Phase 03 summary](../phase-03-compliance-review/summary.md#stop-2)) |
| G-6 | [G-6 \| A subject quoted in a summary equals its source word for word] | lesson | keep local | Now part of the Subjects rule and its self-check item; no fence beyond it |

<a id="outcome"></a>
## Outcome

Close-out complete under delegation. The five skill files stay uncommitted for the Architect
(DD-28); the review round decides the delegated decisions, the graduation proposal and the
commit of the skill files.

<a id="open-items"></a>
## Open Items

| # | Item | Settles in |
|---|---|---|
| O-8 | [O-8 \| Fourteen material answers taken under `stops: proceed` wait for the Architect] | the review round |
| O-9 | [O-9 \| Graduation proposal G-1 – G-6 waits for the Architect] | the review round |
| O-10 | [O-10 \| The five skill files are uncommitted; commit them with the bundle?] | the review round |
