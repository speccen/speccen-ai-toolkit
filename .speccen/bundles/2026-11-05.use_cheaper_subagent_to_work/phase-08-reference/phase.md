---
type: Phase
phase: "08 — Reference"
status: COMPLETE
description: Working notes for the optional technical reference of the search unit and the gate-test changes
---

<a id="phase-top"></a>
# Use cheaper subagent to work — Reference

[Index](../index.md) · [State](../STATE.md) · [Log](../log.md)

---

<a id="extensions"></a>
## Extensions applied

| Extension | Why | Where it applies | Outcome |
|---|---|---|---|
| — | — | — | No extensions for this phase: `.speccen/extensions/reference/` does not exist |

## Working notes

- Requested by the Architect: "proceed to reference" (2026-11-06).
- Scope (Architect, 2026-11-06): the changed rules in the seven files, the rest of speccen as context only. Content: C4 + runtime; why + alternatives (incl. delegated decisions with status); config reference; limits + follow-ups. Source: bundle + the committed code.
- Steps 3–7 run as one subagent unit: `speccen-worker`, tier `balanced` → `sonnet` (project config).

## Verification (main session)

- 7 inline SVGs parse (`xml.etree`); the only external assets are Google Fonts.
- "Claude" and "AI" appear only as the product and the workflow actor, never as author.
- Phone width: the first render clipped text, because grid tracks grew to the diagrams'
  minimum width. CSS fix: `grid-template-columns: minmax(0, 1fr)` on the grid containers and
  flexible fact tiles. Re-rendered in a 390 px frame: prose and tables fit; wide diagrams
  scroll inside their own panel. No content changed, so `reference.md` stays a valid projection.
- Worker notes accepted: the three LOW findings shown as OPEN are open; DD-15 and staging are
  resolved by R/1 (commit `835cd78`).

<a id="outcome"></a>
## Outcome

`reference.html` and `reference.md` written and approved by the Architect ("accept ref", 2026-11-06).
Both are copied into the durable store at `features/2026-11-05.use_cheaper_subagent_to_work/`,
with bundle links rewritten for that folder. The node's `reference` edge is set, the specification
links forward to the reference, and `timeline.md` is regenerated.

<a id="open-items"></a>
## Open Items

| # | Item | Status |
|---|---|---|
| — | Scope | agreed |
