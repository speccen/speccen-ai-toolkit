# Code Analysis Phase (02) — autonomous mode

**Applies when:** the effective mode of this phase is `autonomous`. Read it together with
`skills/sdd/sdd-governing-workflow/references/autonomous-execution.md`.

> Part of the `sdd-code-analysis` skill (`../SKILL.md`). Step numbers, the Quality Criteria and section
> names refer to that file. This file is the single source of truth for its content.

**`autonomous`** — the delegate ends the phase with its gate test, in place of Steps 7 and 8:

- Run the Quality Criteria of `../SKILL.md` item by item with cited evidence. The evolution-gap
  determination (Step 5) is already your call from evidence; the Architect's "generate it
  anyway" override has no counterpart here, so record the determination and its basis.
- Add one check: **no blocking open question**. An open question the basis cannot answer, whose
  answer is material, is a stop. A non-material one is decided and recorded in
  `delegated-decisions.md`.
- Write `## Delegate gate check` into `{{SUMMARY_FILE}}`, then transition (Phase Transition
  Protocol). Send no Step 8 message.
- **Verifier claims.** Convention quotes that bind the change, counts, "none found" claims, and
  the code facts behind each pattern or risk conclusion (`skills/sdd/sdd-governing-workflow/references/autonomous-execution.md` → Gate test).
- Decision basis, stop conditions and records: **Autonomous Execution** (`skills/sdd/sdd-governing-workflow/references/autonomous-execution.md`).
