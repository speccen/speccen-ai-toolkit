---
type: Phase
phase: "08 — Reference"
status: COMPLETE
description: Layered technical reference for the fix budget — approved, copied into the feature store
---

<a id="phase-top"></a>
# set allowed budget for autonomous phases — Reference

[Index](../index.md) · [State](../STATE.md) · [Log](../log.md)

---

<a id="extensions"></a>
## Extensions applied

| Extension | Why | Where it applies | Outcome |
|---|---|---|---|
| — | — | — | No extensions for this phase: `.speccen/extensions/reference/` does not exist |

## Working notes

- Scope (Architect, Step 2): the three changed files; content: C4 descent + runtime run, configuration reference, why (decisions and alternatives); the code read directly.
- Steps 3–7 ran on `speccen-worker` (balanced → sonnet). Outputs checked: both files present, valid frontmatter, 5 inline SVGs parse, no stale default `1`.
- Points for the Architect: (1) the page reads `fixes` resolution as phase level → top-level `fixes` → `5`, by analogy with `mode`; the skill (`:941`) says only "the same way at phase level, then fall back to their defaults". (2) ADR 2026-11-11 Decision line said "default `1`" — fixed on the Architect's request: it now says default `5` and links ADR 2026-11-12. (3) The page states that issue #25 §3 "Unchanged by default" no longer holds. (4) The header warns that the default-5 amendment is uncommitted.
- Approved by the Architect ("approved, finish phase 08 and commit"). The "not committed" callout was reworded before the commit; the reference was copied into `features/25.set_allowed_budget_for_autonomous_phases/`, cross-linked with the specification, the node's `reference` edge set and `timeline.md` updated.
