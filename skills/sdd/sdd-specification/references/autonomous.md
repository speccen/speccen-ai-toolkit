# Specification Phase (04) — autonomous mode

**Applies when:** the effective mode of this phase is `autonomous`. Read it together with
`skills/sdd/sdd-governing-workflow/references/autonomous-execution.md`.

> Part of the `sdd-specification` skill (`../SKILL.md`). Step numbers, the Quality Criteria and section
> names refer to that file. This file is the single source of truth for its content.

**`autonomous`** — Steps 1–8 are unchanged. The delegate approves the Implementation Plan and
the Test Plan as part of the gate test (a recorded decision; waiving a test is never delegated)
and replaces Steps 9 and 10 with:

- Run the Quality Criteria of `../SKILL.md` item by item with cited evidence.
- **Traceability check.** Write a table under `## Delegate gate check`: every requirement stated
  in the Architect's prompts (`log.md`) and every ADR, the acceptance scenario(s) that cover it,
  and the Test Plan entries that test those scenarios. A requirement or ADR with no scenario
  fails. A scenario with no test fails. A specification item with no source — Phase 01 intent,
  a Phase 03 decision or an ADR — is invented scope and fails. Each implementation phase's
  **Why** must cite such a source too, or the phase fails.
- **Material choices.** Work through them with the interview. A contract, data-model,
  persistence, security, dependency or plan-structure choice that the basis does not determine
  goes to the Architect in one stop round, with your proposed answer.
- A passed gate test is the go for Phase 05. It freezes the specification and the intent seeds,
  exactly as closing Phase 04 does today. Send no Step 10 message.
- **Verifier claims.** The plan's anchors in the existing code: every file, symbol and integration
  point the plan changes or extends exists as described. At most one claim per plan step that
  touches existing code. The traceability rows stay with the self-check
  (`skills/sdd/sdd-governing-workflow/references/autonomous-execution.md` → Gate test).
- Decision basis, stop conditions and records: **Autonomous Execution** (`skills/sdd/sdd-governing-workflow/references/autonomous-execution.md`).
