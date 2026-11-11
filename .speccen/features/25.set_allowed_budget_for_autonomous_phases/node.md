---
id: 25.set_allowed_budget_for_autonomous_phases
kind: feature
work-kind: fix
status: active
evidence: confirmed
created: 2026-11-11T20:55Z
updated: 2026-11-11T20:55Z
date: 2026-11-11T20:55Z
touches: [governing-workflow, configuration, gate-test]
produced: []
specification: ./specification.html
---

# Set allowed budget for autonomous phases

[Index](../../index.md)

---

|     | Info |
| --- | --- |
| **What** | A `fixes` key (1 – 3, default 1) sets how many fix attempts the delegate makes on a failing gate test; three guards stop it sooner |
| **Outcome** | Template version 3; the gate test loops up to the budget and stops on a conclusion change or no progress; the Phase 05 accept uses the same budget and rejects |
| **Touches** | governing-workflow, configuration, gate-test |
| **Origin bundle** | bundles/25.set_allowed_budget_for_autonomous_phases (disposable; this node is the durable residue) |

| Related | |
| --- | --- |
| **Specification** | [specification.html](./specification.html) — intent |
| **Builds on** | [2026-11-05.use_cheaper_subagent_to_work](../2026-11-05.use_cheaper_subagent_to_work/node.md) — the gate-test self-check and delta re-check this budget extends |
| **Produced** | — (graduation proposal pending the Architect) |
