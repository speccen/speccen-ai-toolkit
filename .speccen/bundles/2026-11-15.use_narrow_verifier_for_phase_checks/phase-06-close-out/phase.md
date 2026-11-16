---
type: Phase
phase: "06 — Close-out"
status: COMPLETE
description: Three outcome seeds written; feature node and specification graduated; three lessons proposed for graduation, pending the Architect
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

Pending the Architect (`autonomous` mode: discretionary promotions are not decided by the
delegate). Nothing below is written to `.speccen/`.

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

<a id="outcome"></a>
## Outcome

Core workflow complete. The feature node and specification are in the store; the three lessons
above wait for the Architect.

<a id="open-items"></a>
## Open Items

- Graduation proposal 06/1 – 06/3 — pending the Architect.
- Review round: DD-1 – DD-27, all `DELEGATED`; DD-14, DD-20, DD-21 `MATERIAL — unconfirmed`.
- Results: the "After" values in [doc-technical.md](./doc-technical.md) need the first bundle on `26.1116.1`.
