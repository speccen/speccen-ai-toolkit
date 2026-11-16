---
id: 2026-11-15.use_narrow_verifier_for_phase_checks
kind: feature
work-kind: refactoring
status: active
evidence: confirmed
created: 2026-11-16T07:42:56Z
updated: 2026-11-16T07:42:56Z
date: 2026-11-16T07:42:56Z
touches: [governing-workflow, subagent-execution, gate-test]
produced: []
builds-on: [2026-11-13.questions_to_the_architect_number_text_subjects_never_a_bare_label]
specification: ./specification.html
---

# Use narrow verifier for phase checks

[Index](../../index.md)

---

|     | Info |
| --- | --- |
| **What** | The gate-check verifier settles only a capped list of code and repository claims (≤ 15 per run), recorded with the gate rows and run beside the self-check; the self-check owns everything inside the bundle |
| **Outcome** | New Gate test rules (claims, `slip` vs. `wrong`, `noticed:` lines, the `verified` column, claim-based later runs), a narrow Units row and verifier work order, a worker bullet, a claim-source bullet in Phases 01 – 05; version `26.1116.1` |
| **Touches** | governing-workflow, subagent-execution, gate-test |
| **Origin bundle** | bundles/2026-11-15.use_narrow_verifier_for_phase_checks (disposable; this node is the durable residue) |

| Related | |
| --- | --- |
| **Specification** | [specification.html](./specification.html) — intent |
| **Builds on** | [2026-11-13.questions_to_the_architect_number_text_subjects_never_a_bare_label](../2026-11-13.questions_to_the_architect_number_text_subjects_never_a_bare_label/node.md) — the six self-check items and stop condition 5 this feature keeps |
