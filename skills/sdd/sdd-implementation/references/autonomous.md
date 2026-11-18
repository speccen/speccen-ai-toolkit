# Implementation Phase (05) — autonomous mode

**Applies when:** the effective mode of this phase is `autonomous`. Read it together with
`skills/sdd/sdd-governing-workflow/references/autonomous-execution.md`.

> Part of the `sdd-implementation` skill (`../SKILL.md`). Step numbers, the Quality Criteria and section
> names refer to that file. This file is the single source of truth for its content.

**`autonomous`** — the delegate takes the Architect's decisions in this phase:

- **Step 2.** Write the Project Conventions Re-Confirmation as usual. Confirm the Implementation
  Plan yourself: record "Plan confirmed by the delegate" with the date in `{{PHASE_FILE}}`, and do
  not wait.
- **Step 3.** Execute as written. The report after each plan phase (Step 6) is a progress report
  and does not stop the run. A new dependency, a build error you cannot resolve and a
  null-safety risk the plan does not address are stops.
- **Step 5 (deviation).** Stop implementing and document the deviation (steps 1–2). Then, if it
  changes no acceptance scenario, no contract and no scope, and the phase's **Why** still holds,
  decide it: set `Decision` to
  `APPROVED (delegated) — [rationale]` or `REJECTED (delegated) — [rationale]`, record it in
  `delegated-decisions.md`, and continue. If it changes any of them, or defeats the phase's **Why**, stop. Never waive a planned
  test.
- **Step 7 (accept).** Instead of notifying and waiting, run the gate test: the Phase 05a
  criteria of `../SKILL.md`; every acceptance scenario of the specification has a passing planned test
  (cite the test); no waiver; every deviation has a decision; the delivered behaviour matches the
  scenarios (cite files and tests). If it passes, the delegate accepts and the workflow advances
  to Phase 06. If it fails, fix and test again, up to the phase's effective `fixes` attempts,
  with the gate test's guards (`skills/sdd/sdd-governing-workflow/references/autonomous-execution.md` → Gate test). If the next
  fix would change a phase conclusion, an ADR, or what a delegated decision decides, stop; a fix
  that only repairs how a decision is recorded is not such a change (`skills/sdd/sdd-governing-workflow/references/autonomous-execution.md` → Gate test). If it still fails
  when the budget is used up, or a run makes no progress, the delegate rejects: run Phase 05b.
- **Phase 05b.** The rejection reason is the failed check, recorded verbatim. Revert only the
  files this iteration changed; if that cannot be established — unrelated uncommitted changes in
  those files, or no repository — stop. Verify the revert instead of asking the Architect to
  confirm it. Record plan updates as delegated decisions, not ADRs, and re-enter Phase 05a.
  After two rejected iterations, stop.
- **Verifier claims.** The implementation does what the row says: a single named test run, a
  symbol present, a pattern absent. Never the full suite — the main session runs that itself
  (`skills/sdd/sdd-governing-workflow/references/autonomous-execution.md` → Gate test).
- Write `## Delegate gate check` into `{{SUMMARY_FILE}}`. Decision basis, stop conditions and
  records: **Autonomous Execution** (`skills/sdd/sdd-governing-workflow/references/autonomous-execution.md`).
