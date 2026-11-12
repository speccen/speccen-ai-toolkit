---
id: 25.set_allowed_budget_for_autonomous_phases
kind: feature
work-kind: fix
status: active
evidence: confirmed
created: 2026-11-11T20:55Z
updated: 2026-11-12T05:24:55Z
date: 2026-11-11T20:55Z
touches: [governing-workflow, configuration, gate-test]
produced: [2026-11-11.fix_progress_by_breaches, 2026-11-11.fix_budget_ceiling_10, 2026-11-12.fix_budget_default_5, 2026-11-11.text_checks_read_their_place, 2026-11-11.repair_every_case_of_a_breach, 2026-11-11.write_lists_and_summary_last]
specification: ./specification.html
reference: ./reference.html
---

# Set allowed budget for autonomous phases

[Index](../../index.md)

---

|     | Info |
| --- | --- |
| **What** | A `fixes` key (1 – 10, default 5) sets how many fix attempts the delegate makes on a failing gate test; three guards stop it sooner |
| **Outcome** | Template version 3; the gate test loops up to the budget and stops on a conclusion change or no progress; the Phase 05 accept uses the same budget and rejects |
| **Touches** | governing-workflow, configuration, gate-test |
| **Origin bundle** | bundles/25.set_allowed_budget_for_autonomous_phases (disposable; this node is the durable residue) |

| Related | |
| --- | --- |
| **Specification** | [specification.html](./specification.html) — intent, revised 2026-11-12: ceiling 10 ([2026-11-11.fix_budget_ceiling_10](../../decisions/2026-11-11.fix_budget_ceiling_10.md)) and default 5 ([2026-11-12.fix_budget_default_5](../../decisions/2026-11-12.fix_budget_default_5.md)) |
| **Reference** | [reference.html](./reference.html) — outcome |
| **Builds on** | [2026-11-05.use_cheaper_subagent_to_work](../2026-11-05.use_cheaper_subagent_to_work/node.md) — the gate-test self-check and delta re-check this budget extends |
| **Produced** | [2026-11-11.fix_progress_by_breaches](../../decisions/2026-11-11.fix_progress_by_breaches.md), [2026-11-11.fix_budget_ceiling_10](../../decisions/2026-11-11.fix_budget_ceiling_10.md), [2026-11-12.fix_budget_default_5](../../decisions/2026-11-12.fix_budget_default_5.md), [2026-11-11.text_checks_read_their_place](../../lessons/2026-11-11.text_checks_read_their_place.md), [2026-11-11.repair_every_case_of_a_breach](../../lessons/2026-11-11.repair_every_case_of_a_breach.md), [2026-11-11.write_lists_and_summary_last](../../lessons/2026-11-11.write_lists_and_summary_last.md) — decisions & lessons from this feature |
