# Feature Analysis Phase (01) — autonomous mode

**Applies when:** the effective mode of this phase is `autonomous`. Read it together with
`skills/sdd/sdd-governing-workflow/references/autonomous-execution.md`.

> Part of the `sdd-feature-analysis` skill (`../SKILL.md`). Step numbers, the Quality Criteria and section
> names refer to that file. This file is the single source of truth for its content.

**`autonomous`** — the delegate ends the phase with its gate test, in place of Steps 5 and 6:

- Run the interview yourself (Step 2a): the same numbered questions, answered from the decision
  basis and recorded with who answered. Phase 01 is discovery: an open question that Phase 02 can
  investigate becomes a **working hypothesis** with its target phase — not a stop. Only an open
  question that **blocks Phase 02** (for example, which system or area), and that the basis cannot
  answer, is a stop. A non-material choice is decided and recorded in `delegated-decisions.md`.
- Run the Quality Criteria of `../SKILL.md` item by item with cited evidence.
- Write `## Delegate gate check` into `{{SUMMARY_FILE}}`, then transition (Phase Transition
  Protocol). Send no Step 6 message.
- **Verifier claims.** None: Phase 01 has no codebase access, so no verifier runs
  (`skills/sdd/sdd-governing-workflow/references/autonomous-execution.md` → Gate test).
- Decision basis, stop conditions and records: **Autonomous Execution** (`skills/sdd/sdd-governing-workflow/references/autonomous-execution.md`).
