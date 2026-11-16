---
type: Phase
phase: "06 — Close-out"
status: COMPLETE
description: Three outcome seeds written; feature node and specification graduated; two lessons promoted, one kept local; delegated decisions adopted
---

<a id="phase-top"></a>
# use narrow verifier for phase checks — Close-out

[Index](../index.md) · [State](../STATE.md) · [Log](../log.md)

---

<a id="extensions"></a>
## Extensions applied

| Extension | Why | Where it applies | Outcome |
|---|---|---|---|
| — | — | — | No extensions for this phase |

<a id="documentation"></a>
## Documentation

- Checklist: all 23 items of the [Implementation Plan](../phase-04-specification/phase.md#phases) ticked; none skipped. Step 1.3 carries [Deviation 2](../phase-05-implementation/phase.md#deviation-2) as its record.
- Seeds written inline (no subagent): [doc-executive.md](./doc-executive.md), [doc-business.md](./doc-business.md), [doc-technical.md](./doc-technical.md). Each links its Phase 04 intent seed where one exists.
- Graduated (mechanical): the feature node `.speccen/features/2026-11-15.use_narrow_verifier_for_phase_checks/node.md`, with `specification.html` and `specification.md` (links repointed into the bundle); the store `index.md` and `timeline.md` updated.
- Overrides: none — the bundle has no ADR, and Phase 03 found no override of a standing decision.

<a id="graduation-proposal"></a>
## Graduation Proposal

Decided by the Architect in the review round (log 09:03, "accept"): 06/1 and 06/2 promoted,
06/3 kept local.

**[06/1 | Lesson: run a plan's error-case text checks on the planned text in Phase 04]** — The
planned text failed its own search check (T-14) in Phase 05: two appendix lines said "every
row" beside "verifier". Evidence: [Deviation 1](../phase-05-implementation/phase.md#deviations),
DD-26, log 08:24. Project-wide: every speccen change to the skill files is checked by text checks.
→ Proposed: promote (lesson, `weight: brief`).

**[06/2 | Lesson: a full-phase verifier finds a new layer of detail on every run]** — Phase 04
needed 9 verifier runs and 4 stops; runs 3 – 6 each found breaches the run before had not
named, almost all in wording and records. This is the reason the verifier is narrow — the sign on the fence if someone
widens it again. Evidence: [Phase 04 summary → Second stop](../phase-04-specification/summary.md#stop-2),
log 06:25 – 08:22.
→ Proposed: promote (lesson, `weight: full`).

**[06/3 | Lesson: a plan step that renders text names a tool the host has]** — Plan step 1.3 asked
for a rendered view; the host had no Markdown renderer. Evidence:
[Deviation 2](../phase-05-implementation/phase.md#deviation-2), DD-27, log 08:32.
→ Proposed: keep local (a host detail, seen once).

<a id="interview"></a>
## Interview

**Review round** (after the `autonomous` run; graduation candidates and every delegated decision,
material first) — answered by the Architect with one "accept" (log 2026-11-16 09:03).

| # | Question | Depends on | Proposed | Answer |
|---|---|---|---|---|
| 06/1 | [06/1 \| Lesson: run error-case checks on the planned text] | — | promote | Architect: "accept" — promoted as `2026-11-16.run_error_checks_on_planned_text` |
| 06/2 | [06/2 \| Lesson: a full-phase verifier finds new detail on every run] | — | promote | Architect: "accept" — promoted as `2026-11-16.full_phase_verifier_finds_new_detail` |
| 06/3 | [06/3 \| Lesson: a render step names a tool the host has] | — | keep local | Architect: "accept" — kept local |
| 06/4 | [06/4 \| DD-14] | — | adopt | Architect: "accept" — [DD-14](../delegated-decisions.md#dd-14) ADOPTED |
| 06/5 | [06/5 \| DD-20] | — | adopt | Architect: "accept" — [DD-20](../delegated-decisions.md#dd-20) ADOPTED |
| 06/6 | [06/6 \| DD-21] | — | adopt | Architect: "accept" — [DD-21](../delegated-decisions.md#dd-21) ADOPTED |
| 06/7 | [06/7 \| DD-10] | — | adopt | Architect: "accept" — [DD-10](../delegated-decisions.md#dd-10) ADOPTED |
| 06/8 | [06/8 \| DD-26] | — | adopt | Architect: "accept" — [DD-26](../delegated-decisions.md#dd-26) ADOPTED |
| 06/9 | [06/9 \| DD-27] | — | adopt | Architect: "accept" — [DD-27](../delegated-decisions.md#dd-27) ADOPTED |
| 06/10 | [06/10 \| DD-11] | — | adopt | Architect: "accept" — [DD-11](../delegated-decisions.md#dd-11) ADOPTED |
| 06/11 | [06/11 \| DD-15] | — | adopt | Architect: "accept" — [DD-15](../delegated-decisions.md#dd-15) ADOPTED |
| 06/12 | [06/12 \| DD-16] | — | adopt | Architect: "accept" — [DD-16](../delegated-decisions.md#dd-16) ADOPTED |
| 06/13 | [06/13 \| DD-17] | — | adopt | Architect: "accept" — [DD-17](../delegated-decisions.md#dd-17) ADOPTED |
| 06/14 | [06/14 \| DD-18] | — | adopt | Architect: "accept" — [DD-18](../delegated-decisions.md#dd-18) ADOPTED |
| 06/15 | [06/15 \| DD-12] | — | adopt | Architect: "accept" — [DD-12](../delegated-decisions.md#dd-12) ADOPTED |
| 06/16 | [06/16 \| DD-13] | — | adopt | Architect: "accept" — [DD-13](../delegated-decisions.md#dd-13) ADOPTED |
| 06/17 | [06/17 \| DD-19] | — | adopt | Architect: "accept" — [DD-19](../delegated-decisions.md#dd-19) ADOPTED |
| 06/18 | [06/18 \| DD-22] | — | adopt | Architect: "accept" — [DD-22](../delegated-decisions.md#dd-22) ADOPTED |
| 06/19 | [06/19 \| DD-23] | — | adopt | Architect: "accept" — [DD-23](../delegated-decisions.md#dd-23) ADOPTED |
| 06/20 | [06/20 \| DD-24] | — | adopt | Architect: "accept" — [DD-24](../delegated-decisions.md#dd-24) ADOPTED |
| 06/21 | [06/21 \| DD-25] | — | adopt | Architect: "accept" — [DD-25](../delegated-decisions.md#dd-25) ADOPTED |
| 06/22 | [06/22 \| DD-9] | — | adopt | Architect: "accept" — [DD-9](../delegated-decisions.md#dd-9) ADOPTED |
| 06/23 | [06/23 \| DD-1] | — | adopt | Architect: "accept" — [DD-1](../delegated-decisions.md#dd-1) ADOPTED |
| 06/24 | [06/24 \| DD-2] | — | adopt | Architect: "accept" — [DD-2](../delegated-decisions.md#dd-2) ADOPTED |
| 06/25 | [06/25 \| DD-3] | — | adopt | Architect: "accept" — [DD-3](../delegated-decisions.md#dd-3) ADOPTED |
| 06/26 | [06/26 \| DD-4] | — | adopt | Architect: "accept" — [DD-4](../delegated-decisions.md#dd-4) ADOPTED |
| 06/27 | [06/27 \| DD-5] | — | adopt | Architect: "accept" — [DD-5](../delegated-decisions.md#dd-5) ADOPTED |
| 06/28 | [06/28 \| DD-6] | — | adopt | Architect: "accept" — [DD-6](../delegated-decisions.md#dd-6) ADOPTED |
| 06/29 | [06/29 \| DD-7] | — | adopt | Architect: "accept" — [DD-7](../delegated-decisions.md#dd-7) ADOPTED |
| 06/30 | [06/30 \| DD-8] | — | adopt | Architect: "accept" — [DD-8](../delegated-decisions.md#dd-8) ADOPTED |

<a id="outcome"></a>
## Outcome

Core workflow complete. The feature node, its specification and two promoted lessons are in the
store; all 27 delegated decisions are ADOPTED.

<a id="open-items"></a>
## Open Items

- Results: the "After" values in [doc-technical.md](./doc-technical.md) need the first bundle on `26.1116.1`.
