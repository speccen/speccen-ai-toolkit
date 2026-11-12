---
type: Specification
phase: "04 — Specification"
status: COMPLETE
description: Reduced projection of specification.html — a fixes budget for the gate test of autonomous phases, with three guards
revised: 2026-11-12 — ceiling 10 and default 5, by the Architect
---

# set allowed budget for autonomous phases — Specification (reduced)

[Index](../../bundles/25.set_allowed_budget_for_autonomous_phases/index.md) · [Full specification](./specification.html) · [Plan](../../bundles/25.set_allowed_budget_for_autonomous_phases/phase-04-specification/phase.md#implementation-plan)

---

## What the update builds

In an autonomous phase, the delegate corrects a failed gate test up to a number of fix attempts.
The key `fixes` in the project file sets that number: 1 to 10, default 5. The delegate halts
sooner in two cases. The next correction would change a conclusion, a delegated decision or an
ADR, or a verifier run makes no progress. Source: [issue #25](../../bundles/25.set_allowed_budget_for_autonomous_phases/files/gh-25-gate-test-fix-budget.md),
[Phase 01](../../bundles/25.set_allowed_budget_for_autonomous_phases/phase-01-feature-analysis/phase.md#feature-description),
[Phase 03 decisions](../../bundles/25.set_allowed_budget_for_autonomous_phases/phase-03-compliance-review/phase.md#outcome).

> **Revised 2026-11-12.** The Architect raised the ceiling from 3 to 10
> ([ADR 2026-11-11](../../bundles/25.set_allowed_budget_for_autonomous_phases/adrs/2026-11-11.fix_budget_ceiling_10.md)) and set the default to 5 ([ADR 2026-11-12](../../bundles/25.set_allowed_budget_for_autonomous_phases/adrs/2026-11-12.fix_budget_default_5.md)). R-1, R-2, R-6, R-11 and
> R-12 say the new values; an invalid value still counts as `1`.

## The files that change

| File | What changes |
|---|---|
| `skills/sdd/00-governing-workflow/SKILL.md` | Keys table and phase list; template `version: 3` with `fixes`; upgrade to version 3; effective settings and fail-safe; fix rule with three guards; self-check line; stop condition 5 |
| `skills/sdd/05-implementation/SKILL.md` | The Step 7 accept uses the budget and the guards |
| `README.md` | Absence values name `5`; the template copy stays identical |

## Decisions

Two bundle ADRs set the budget: the ceiling of 10
([2026-11-11.fix_budget_ceiling_10](../../bundles/25.set_allowed_budget_for_autonomous_phases/adrs/2026-11-11.fix_budget_ceiling_10.md)) and the default of 5
([2026-11-12.fix_budget_default_5](../../bundles/25.set_allowed_budget_for_autonomous_phases/adrs/2026-11-12.fix_budget_default_5.md)). The update complies with the four standing decisions. The delegated
decisions of this bundle are in [delegated-decisions.md](../../bundles/25.set_allowed_budget_for_autonomous_phases/delegated-decisions.md). Two of them
were `MATERIAL — unconfirmed` and went to the review: a ceiling of 3 fix attempts, OVERRIDDEN to 10 ([DD-12](../../bundles/25.set_allowed_budget_for_autonomous_phases/delegated-decisions.md#dd-12)),
and a progress guard that looks at breaches that come back, and at more failed rows, ADOPTED
([DD-14](../../bundles/25.set_allowed_budget_for_autonomous_phases/delegated-decisions.md#dd-14)).

## Requirements & acceptance scenarios

| Id | Requirement (SHALL) | Scenario (WHEN → THEN) | Source |
|---|---|---|---|
| R-1 | The project file SHALL have a `fixes` key at the top level and on the five phases that have a `stops` key. Its values SHALL be the whole numbers `1` to `10`, and also `inherit` at phase level. The key SHALL have an effect only in autonomous phases. It SHALL be independent of `stops`. | WHEN a project file sets `phases.code-analysis.fixes: 2` and the phase is autonomous → THEN the gate test of that phase allows two fix attempts. WHEN the phase is gated → THEN `fixes` has no effect. | brief §2, §2.3; DD-11 |
| R-2 | The default SHALL be `5`. | WHEN no file sets `fixes` → THEN the gate test allows up to five fix attempts, then a stop. | ADR 2026-11-12 (overrides brief §3, DD-17) |
| R-3 | The delegate SHALL correct a failed gate test and repeat the verifier run, up to the effective `fixes` attempts. Each later verifier run SHALL examine the rows that failed in the previous run and the rows that cite a changed file. | WHEN `fixes: 3` and run 1 fails two rows → THEN the delegate corrects them. Run 2 examines those rows and the rows that cite the changed files. The other rows keep their last `confirmed (run N)`. | brief §2.1 |
| R-4 | The delegate SHALL halt when a verifier run makes no progress. No progress means that a breach from the previous run is still there, or that more rows fail than in the previous run. | WHEN run 3 fails a row on the same breach as run 2 → THEN the delegate halts, also with fix attempts left. WHEN run 3 fails one row on a new breach, and run 2 failed one row → THEN the delegate continues. | DD-14; brief §2 guard 1 |
| R-5 | The delegate SHALL halt immediately when the next correction would change a phase conclusion, a delegated decision or an ADR. | WHEN the only correction for a failed row changes a delegated decision → THEN the delegate halts before the correction, whatever the budget. | DD-13; brief §2 guard 2 |
| R-6 | The budget SHALL be at most 10. A `fixes` value that is not a whole number from `1` to `10` SHALL count as `1`. | WHEN a file sets `fixes: 12` or `fixes: many` → THEN the effective budget is `1`. | ADR 2026-11-11 (overrides DD-12); brief §2.6 |
| R-7 | The delegate SHALL write one log line for each fix attempt: `fix attempt <n> of <fixes>: run <N> failed rows <list>`. | WHEN the delegate makes its second fix attempt with `fixes: 3` → THEN `log.md` gets `fix attempt 2 of 3: run 2 failed rows …`. | brief §2.1 |
| R-8 | After a stop, the Architect's answer SHALL set the rows for the next verifier run, and whether the delegate may make more fix attempts. Without such an answer, one verifier run SHALL follow, and a failed row SHALL be a new stop. | WHEN the Architect replies "yes" to a stop that names two rows → THEN one verifier run examines the two rows. A failed row is a new stop. | brief §2.1 |
| R-9 | Stop condition 5 SHALL name three causes: a used-up budget, no progress, and a correction that changes a conclusion, a delegated decision or an ADR. | WHEN a reader looks for the cause of a stop at a gate test → THEN condition 5 names all three causes. | brief §2.2 |
| R-10 | The Phase 05 accept step SHALL use the same budget and guards. When the delegate used all its fix attempts, or a verifier run makes no progress, the delegate SHALL reject the implementation (05b). A correction that changes a conclusion SHALL be a stop. | WHEN `phases.implementation.fixes: 2` and the accept step fails twice with progress → THEN the delegate makes two fix attempts, then rejects the implementation and starts 05b. | DD-10, DD-13 |
| R-11 | The template SHALL be version 3, with `fixes: 5`, its comment, its legend line and `fixes: inherit` on five phases. The Keys row SHALL say that the current version is `3`. The README copy SHALL be equal to the template. | WHEN speccen writes a new project file → THEN the file has `version: 3` and every `fixes` line, and the README shows the same block. | brief §2.4; DD-15, DD-18 |
| R-12 | The upgrade of a project file to version 3 SHALL add `fixes: 5` and `fixes: inherit` on five phases and set `version: 3`. The value added SHALL be the value its absence means, so the upgrade keeps every effective setting. Both lists of absence values SHALL name `5`. | WHEN speccen brings the version-2 project file of this repository to version 3 → THEN the file gets `fixes: 5`, five `fixes: inherit` lines and `version: 3`. No value the Architect set changes. | brief §2.5; DD-19; ADR 2026-11-12; log 11:05 |
| R-13 | A project `lock` SHALL prevent a higher `fixes` in a bundle file or a local file, as for every other key. | WHEN the project file sets `lock: true` on `code-analysis` and a bundle file sets `phases.code-analysis.fixes: 3` → THEN the session ignores the bundle value. The session shows one message about the lock. | brief §2.6 |
| R-14 | The self-check line SHALL be `Self-check: done — N corrections`. | WHEN a gate test writes its self-check line → THEN the line shows "N corrections", and "fix" means only a gate-test fix attempt. | DD-16 |
| R-15 | The update SHALL touch only the governing skill, the Phase 05 skill and the README. | WHEN the update lands → THEN `git diff --stat` outside `.speccen/` shows only those three files. | DD-3; DD-20 |

## The plan and the text checks

Five phases: configuration → gate test → Phase 05 accept → restated copies → verification.
Nineteen text checks: T-1 – T-19 ([Test Plan](../../bundles/25.set_allowed_budget_for_autonomous_phases/phase-04-specification/phase.md#implementation-plan)).
