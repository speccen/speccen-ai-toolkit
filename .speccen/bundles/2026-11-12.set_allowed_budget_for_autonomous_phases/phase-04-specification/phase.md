---
type: Phase
phase: "04 — Specification"
status: COMPLETE
description: Five-phase plan — the fixes key and template version 3, the gate-test budget with its three guards, the Phase 05 accept, the restated copies, text verification
revised: 2026-11-12 — ceiling 10 and default 5, by the Architect (Phase 6 of the plan)
---

<a id="phase-top"></a>
# set allowed budget for autonomous phases — Specification

[Index](../index.md) · [State](../STATE.md) · [Log](../log.md)

> **Revised 2026-11-12.** The Architect raised the ceiling from 3 to 10
> ([ADR 2026-11-11](../adrs/2026-11-11.fix_budget_ceiling_10.md)) and set the default to 5
> ([ADR 2026-11-12](../adrs/2026-11-12.fix_budget_default_5.md)). The requirements, the risks and the
> Test Plan below say the new values. Phases 1 – 5 record the plan as first carried out, with
> `1` – `3` and default `1`; [Phase 6](#plan-revision) brings the text to the new values.

---

<a id="extensions"></a>
## Extensions applied

| Extension | Why | Where it applies | Outcome |
|---|---|---|---|
| — | — | — | No extensions for this phase |

`.speccen/extensions/` does not exist in this repository.

<a id="interview"></a>
## Interview

Mode: `autonomous` (bundle config); `stops: proceed` (project config). The Phase 03 decisions
(DD-9 – DD-20) leave no contract, data-model, dependency or plan-structure choice open. One
non-material choice remains; the delegate answers it from the basis.

**Round 1**

| # | Question | Depends on | Proposed | Answer |
|---|---|---|---|---|
| 04/1 | [04/1 \| Are the skill-text changes left uncommitted in the working tree for the Architect, with only the bundle files committed at each phase transition?] | — | yes | delegate: yes — basis: Phase Transition Protocol, which commits "the changed bundle files — only those"; precedent: bundle `2026-11-05.use_cheaper_subagent_to_work`, its Phase 04 question 04/2; the Architect: "feature branch, no push on main is allowed" (log 11:05) — [DD-24](../delegated-decisions.md#dd-24) |

**Round 2 — stop round** (stop condition 5 and the progress guard of DD-14: check run 4 failed more rows than run 3, and a run-3 fault came back) — answered by the Architect

| # | Question | Depends on | Proposed | Answer |
|---|---|---|---|---|
| 04/2 | [04/2 \| May the delegate repair the three rows and run the checker again on rows 15, 17 and 22?] See [summary → Stop](./summary.md#stop). | — | yes | Architect: "yes" (log 20:48) |

<a id="implementation-plan"></a>
## Implementation Plan

All line numbers are at commit `a7c8206` (the plugin source is unchanged since `8ecb30a`,
26.1108.1) and shift as edits land. Each checklist item names the text it changes, so it can be
found after a shift. "Governing" is `skills/sdd/00-governing-workflow/SKILL.md`; "the brief" is
[files/gh-25-gate-test-fix-budget.md](../files/gh-25-gate-test-fix-budget.md).

### Proposed Changes Summary

| File | Change | What |
|---|---|---|
| `skills/sdd/00-governing-workflow/SKILL.md` | modify | Keys: `version` row (`:691`), two new rows after `phases.<phase>.stops` (`:695`), a `fixes` bullet after the `stops` bullet (`:707`); template (`:731-798`): `version: 3`, `fixes` comment and key, legend line, `fixes: inherit` on five phases; upgrade: absence values (`:857-861`), a version-3 sentence after `:907-908`; Effective settings (`:925-926`); fail-safe, a `fixes` line after the `prototypes` line (`:941`); Gate test: self-check record line (`:1168`) and the fix rule (`:1176-1182`); Stop conditions: condition 5 (`:1212`) |
| `skills/sdd/05-implementation/SKILL.md` | modify | Step 7 accept (`:324-325`): the fix rule follows the budget |
| `README.md` | modify | absence values (`:193`); template copy (`:238-305`) kept identical to the governing template |

No file is created or deleted. No new pattern is introduced: `fixes` follows the `stops` pattern
(a top-level default plus `phases.<phase>` with `inherit`, the same five phases) and the
`prototypes` pattern (a numeric budget with a fail-safe value) — [Phase 02 Coding
Patterns](../phase-02-code-analysis/phase.md#code-analysis).

Sites that stay true and do not change (Phase 02 sites S-14 – S-19, DD-20): the fail-safe rule
for a key on a phase that does not take it (`:944-946`); the template's hard-stop comment and
its README copy; ARCHITECTURE.md (`:142-143`); "Conditions 2 to 8 stay hard stops"
(`:1249-1250`); the Step 0 upgrade example (`:416-419`); the opening of Phase 05
(`05-implementation/SKILL.md:27-28`).

### Target-State Execution Flow

The gate test at the end of an `autonomous` phase, after the change. Phase 05 Step 7 runs the
same loop on its accept check; where its outcome differs, the box says so.

```
      ┌─────────────────────────────┐
      │ gate test: rows, self-check;│
      │ verifier run 1, every row   │
      └──────────────┬──────────────┘
                     ▼
          ┌─────────────────────┐         ┌────────────────────────────┐
          │ a row failed?       ├─── no ─►│ gate passes                │
          └──────────┬──────────┘         └────────────────────────────┘
                     │ yes
                     ▼
          ┌─────────────────────┐         ┌────────────────────────────┐
          │ next fix changes a  ├─── yes ►│ STOP (condition 5),        │
          │ conclusion, a DD    │         │ in every phase             │
          │ or an ADR?          │         └────────────────────────────┘
          └──────────┬──────────┘
                     │ no
                     ▼
          ┌─────────────────────┐         ┌────────────────────────────┐
          │ budget used up, or  ├─── yes ►│ STOP (condition 5);        │
          │ no progress (from   │         │ Phase 05 accept: reject    │
          │ run 2): a breach of │         │ → 05b                      │
          │ run N back, or more │         └────────────────────────────┘
          │ failed rows?        │
          └──────────┬──────────┘
                     │ no
                     ▼
          ┌─────────────────────┐
          │ fix; log "fix       │
          │ attempt n of fixes" │
          └──────────┬──────────┘
                     │
                     ▼
          ┌─────────────────────┐
          │ verifier run N+1:   │
          │ failed rows and rows│
          │ that cite a changed │
          │ file                │
          └──────────┬──────────┘
                     │
                     └──► back to "a row failed?"
```

What changed relative to the current state: the single "fix once, then stop" step becomes a loop
bounded by the effective `fixes` (`1` – `10`, default `5`). Before each fix, the conclusions guard comes first;
then the budget and, from run 2 on, the progress guard. Phase 05 accept follows the same loop and
keeps its reject outcome for the budget and progress guards. With `fixes: 1` the loop runs once,
as before. Compare the
[current-state flow](../phase-02-code-analysis/phase.md#code-analysis).

### Strategy Evaluation

One approach remains after Phase 03: the brief's §2 change, as refined by DD-9 – DD-20. No
prototype ran, so no strategy table is needed.

### Implementation Phases

#### Phase 1: Configuration — the `fixes` key, the template and the upgrade ✅

**Why:** The key must exist, with its values, default, template entry and upgrade rule, before
any rule refers to "the phase's effective `fixes`". Keys, template, upgrade and fail-safe
change together, as for `stops` — source: brief §2.3 – §2.6; DD-11, DD-15, DD-17, DD-18;
[Phase 02 Data Model](../phase-02-code-analysis/phase.md#code-analysis).

##### 1.1 Keys
- [x] Governing Keys table, `version` row (`:691`): "the current version is `2`" → "the current version is `3`" (DD-15).
- [x] Governing Keys table, after the `phases.<phase>.stops` row (`:695`): add the two rows of brief §2.3 — `` | `fixes` | `1` · `2` · `3` | `autonomous` only; the default at that level. How many fix attempts the delegate makes on a failing gate test before it stops (Autonomous Execution → Gate test). Independent of `stops` | `` and `` | `phases.<phase>.fixes` | `inherit` · `1` · `2` · `3` | `autonomous` only; the fix budget for one phase. `inherit` means no value at this level | ``.
- [x] Governing "Which phases take which key", after the `stops` bullet (`:707`): add "- `fixes`: the same five phases as `mode`. It has no effect in a `gated` phase."

##### 1.2 Template (`:731-798`)
- [x] `version: 2` → `version: 3` (DD-18).
- [x] After `stops: ask`: add the two comment lines and the key of brief §2.4 — "# How many times the delegate repairs a failing gate test before it stops (autonomous only, 1–3).", "# It stops sooner when a repair makes no progress or would change a conclusion.", "fixes: 1".
- [x] Per-phase legend, after the `stops` line: add "#   fixes       inherit · 1 · 2 · 3 — autonomous only: see the top-level fixes".
- [x] Add `fixes: inherit` after `stops: inherit` in `feature-analysis`, `code-analysis`, `compliance-review`, `specification` and `implementation`.

##### 1.3 Upgrade (`:857-861`, `:907-908`)
**Why:** the Architect asked that the upgrade bring in the new version key on its own — source: log 11:05.
- [x] Absence values: "`mode: gated`, `stops: ask` and `lock: false` at the top; `inherit` for a phase's `mode`, `stops` and `model`" → "`mode: gated`, `stops: ask`, `fixes: 1` and `lock: false` at the top; `inherit` for a phase's `mode`, `stops`, `fixes` and `model`" (brief §2.5).
- [x] After the version-2 sentence (`:907-908`): add "An upgrade to version 3 adds `fixes: 1` at the top and `fixes: inherit` to the five phases that take `stops`, and sets `version: 3`. Behaviour is unchanged until the Architect raises `fixes`."

##### 1.4 Effective settings and fail-safe (`:925-926`, `:941`)
- [x] "The other per-phase keys (`stops`, `model`, `prototypes`) … (`ask`, `inherit`, `0`)" → "The other per-phase keys (`stops`, `fixes`, `model`, `prototypes`) … (`ask`, `1`, `inherit`, `0`)" (brief §2.6).
- [x] After the `prototypes` fail-safe line (`:941`): add "- A `fixes` value that is not `1`, `2` or `3` counts as `1`." (brief §2.6; the ceiling, DD-12).
- [x] Leave the "key on a phase that does not take it" line (`:944-946`) unchanged (DD-20).

##### 1.5 Build and Validate
- [x] No build exists (Markdown only). Validate: T-1, T-2, T-3, T-4, T-5, T-6, T-7 pass.

#### Phase 2: Gate test — the fix budget and its guards ✅

**Why:** This is the change itself: the delegate repairs its own work up to the budget, and stops
sooner when a repair would change a conclusion or the runs stop converging. It needs the key
from Phase 1 — source: brief §2.1, §2.2; DD-12, DD-13, DD-14; the Architect: "loop until issues
are fixed" (log 15:45).

##### 2.1 The fix rule (`:1176-1182`)
**Why:** progress counts breaches, not failed rows, because a later run re-checks another set of rows; the verifier already lists every breach of a failed row (`:1181-1182`) — source: DD-14.
- [x] Replace the bullet "If any item fails, fix it once and run the test again. … If a re-checked row still fails, stop." with: "If any item fails, fix it and run the test again — up to the phase's effective `fixes` attempts (Configuration; default `1`). Each later verifier run re-checks (a) every row that failed in the run before, and (b) every row whose evidence is in a file you changed during the fix. Rows it does not re-check keep their last `confirmed (run N)`."
- [x] Add after it the stop bullet: "Stop (stop condition 5) when: 1. the fix you would make next changes a phase conclusion, a delegated decision or an ADR; or 2. a re-checked row still fails and the budget is used up; or 3. a run makes no progress: a rule breach the run before named is still there, or more rows fail than in the run before. Log each attempt as `fix attempt <n> of <fixes>: run <N> failed rows <list>`."
- [x] Replace the "After a stop" bullet with brief §2.1's text: "After a stop, the Architect's answer sets which rows the next verifier run re-checks, and whether further fix attempts are allowed; without that, one run, and a failing row stops again. Rows it does not re-check keep their last `confirmed (run N)`. A verifier that fails a row lists every rule breach it finds in that row at once."

##### 2.2 Self-check record line (`:1168`)
- [x] "`Self-check: done — N fixes`" → "`Self-check: done — N corrections`" (DD-16).

##### 2.3 Stop condition 5 (`:1212`)
- [x] "5. a gate test still fails after one fix attempt;" → "5. a gate test still fails after the fix budget, makes no progress, or needs a fix that changes a conclusion, a delegated decision or an ADR (Gate test);" (brief §2.2).

##### 2.4 Build and Validate
- [x] Validate: T-8, T-9, T-10, T-11, T-12, T-13 pass.

#### Phase 3: Phase 05 accept — the same budget ✅

**Why:** `phases.implementation.fixes` must have an effect, so the Phase 05 accept check uses the
budget and the guards; it keeps its own outcome — reject and 05b — when the budget is spent or
the runs stop converging. It needs the Phase 2 rule to point to — source: DD-10, DD-13;
[Phase 02 site S-12](../phase-02-code-analysis/phase.md#restated-sites).

##### 3.1 Step 7 (`05-implementation/SKILL.md:324-325`)
- [x] "If it fails, fix once and test again. If it still fails, the delegate rejects: run Phase 05b." → "If it fails, fix and test again, up to the phase's effective `fixes` attempts, with the gate test's guards (governing skill → Autonomous Execution → Gate test). If the next fix would change a phase conclusion, a delegated decision or an ADR, stop. If it still fails when the budget is used up, or a run makes no progress, the delegate rejects: run Phase 05b."
- [x] Leave "After two rejected iterations, stop." (`:330`) and the opening sentence (`:27-28`) unchanged.

##### 3.2 Build and Validate
- [x] Validate: T-14, T-15 pass.

#### Phase 4: Restated copies ✅

**Why:** The README restates the absence values and copies the template; a copy that differs from
its source tells the reader something false. It comes after Phases 1 and 2, because it copies the
final template block and absence values from Phase 1 — source: DD-19; done-when hypothesis H-4 (DD-7);
[restated sites](../phase-02-code-analysis/phase.md#restated-sites) S-5, S-11.

##### 4.1 README
- [x] `README.md:193`: "(`inherit`, `ask`, `0`, `false`)" → "(`inherit`, `ask`, `1`, `0`, `false`)" (DD-19).
- [x] `README.md:238-305`: replace the template block with the new governing template block, character for character.

##### 4.2 Build and Validate
- [x] Validate: T-16, T-17 pass.

#### Phase 5: Verification and hand-over ✅

**Why:** The skills have no test runner, so the planned text checks are the evidence that the
text says what the requirements state. It comes last, because it checks the text that Phases 1 – 4 change — source: [Phase 02 test
conventions](../phase-02-code-analysis/phase.md#code-analysis); precedent
`.speccen/bundles/2026-11-05.use_cheaper_subagent_to_work/files/phase-05-text-checks.py`.

##### 5.1 Run all checks
- [x] Write the checks T-1 – T-19 as `files/phase-05-text-checks.py` (run with `python3 -I` from the repository root) and record each result in `phase-05-implementation/phase.md`.
- [x] `git diff --stat -- . ':(exclude).speccen'` shows only the three files of the Proposed Changes Summary.
- [x] Leave the skill changes uncommitted for the Architect (DD-24).

##### 5.2 Build and Validate
- [x] All checks pass, or each failure is a deviation.

<a id="plan-revision"></a>
#### Phase 6: Revision — ceiling 10, default 5 ✅

**Why:** the Architect raised the ceiling to 10 at the end-of-run review (ADR 2026-11-11) and,
on 2026-11-12, set the default to 5 and asked that the specification steer the implementation
again — source: [ADR 2026-11-11](../adrs/2026-11-11.fix_budget_ceiling_10.md),
[ADR 2026-11-12](../adrs/2026-11-12.fix_budget_default_5.md).

##### 6.1 Ceiling 10 (applied after the Phase 05 accept, commit `77fb4f4`)
- [x] Keys rows, template comment and legend, fail-safe line and the README copy say `1` – `10`.

##### 6.2 Default 5
- [x] Template and README copy: `fixes: 1` → `fixes: 5`.
- [x] Upgrade absence values: `fixes: 1` → `fixes: 5`; the version-3 upgrade sentence adds `fixes: 5` and ends "An autonomous phase then makes up to five fix attempts; set `fixes: 1` to keep one."
- [x] Effective settings defaults: (`ask`, `1`, `inherit`, `0`) → (`ask`, `5`, `inherit`, `0`).
- [x] Gate test fix rule: "default `1`" → "default `5`".
- [x] `README.md:193`: "with the value that keeps today's behaviour (`inherit`, `ask`, `1`, `0`, `false`)" → "with the value its absence means (`inherit`, `ask`, `5`, `0`, `false`)".
- [x] The fail-safe stays: an invalid value counts as `1`.

##### 6.3 Build and Validate
- [x] T-1 – T-19 updated to the new values; all pass.

### Risk Mitigation

| Risk | Impact | Mitigation |
|---|---|---|
| The README template drifts from the governing template | Medium | T-16 compares the two blocks; Phase 4 copies the block from its source |
| Keys, template, upgrade and fail-safe disagree on the values or the default | High — a `fixes` value is ignored or misread | Phase 1 changes all four together; T-2 – T-7 check each |
| Default behaviour changes for existing projects | Accepted — the Architect chose default 5 (ADR 2026-11-12) | absence and the upgrade both mean `fixes: 5` (T-5, T-6), so the upgrade still writes the effective value; the upgrade sentence tells the Architect to set `fixes: 1` to keep one attempt; the progress and conclusions guards bound every loop |
| The conclusions guard is a new stop even with `fixes: 1` | Low — it stops only on a fix that would change a conclusion, which today's text does not allow either | stated in the stop bullet; R-5 scenario |
| The progress guard misreads a run with a different re-check set | Medium | measured by breaches (DD-14), which the verifier lists per row (`:1181-1182`); T-10 |
| The budget loops at cost | Medium | ceiling 10 (ADR 2026-11-11); invalid values count as `1` (T-7); every attempt is logged (T-11) |
| Line numbers shift during editing | Low | each item names the text it changes |

### Test Plan

The repository has no test framework (Phase 02). Unit and integration tests: **none, because the
change is prose and YAML inside Markdown with no executable code**. The planned tests are **text
checks** — a Python script run in Phase 05 after the edits, derived from the requirements below,
not from the edited text. The script is a bundle file (`files/`), not a repository test.

| Id | Check | Requirement |
|---|---|---|
| T-1 | Keys `version` row says "the current version is `3`"; no "the current version is `2`" remains | R-11 |
| T-2 | Keys table has the `fixes` row (`1` – `10`, "Independent of `stops`") and the `phases.<phase>.fixes` row (`inherit` · `1` – `10`), directly after `phases.<phase>.stops` | R-1 |
| T-3 | "Which phases take which key" has "- `fixes`: the same five phases as `mode`. It has no effect in a `gated` phase." | R-1 |
| T-4 | Template block: `version: 3`; the two `fixes` comment lines ("1–10") and `fixes: 5` after `stops: ask`; the legend line; `fixes: inherit` after `stops: inherit` in exactly the five phases, and not in `close-out`, `retrospective`, `reference` | R-11 |
| T-5 | Upgrade absence values name `fixes: 5` at the top and `fixes` among the phase keys added as `inherit` | R-12 |
| T-6 | The version-3 sentence follows the version-2 sentence: it adds `fixes: 5` and ends "set `fixes: 1` to keep one." | R-12 |
| T-7 | Effective settings list `fixes` with default `5`; the fail-safe has "A `fixes` value that is not a whole number from `1` to `10` counts as `1`."; the line "a key on a phase that does not take it" is unchanged | R-2, R-6 |
| T-8 | Gate test: the fix rule names "the phase's effective `fixes` attempts" and "default `5`"; the old "fix it once and run the test again" is gone | R-3 |
| T-9 | Gate test: the stop bullet holds the three guards — conclusion/DD/ADR, budget used up, no progress | R-4, R-5, R-6 |
| T-10 | Gate test: no progress is "a rule breach the run before named is still there, or more rows fail than in the run before"; the brief's "as many rows or more" is absent | R-4 |
| T-11 | Gate test: the log line `fix attempt <n> of <fixes>: run <N> failed rows <list>` is present | R-7 |
| T-12 | Gate test: the after-a-stop bullet names "whether further fix attempts are allowed" and "without that, one run, and a failing row stops again"; "lists every rule breach it finds in that row at once" stays | R-8 |
| T-13 | Stop condition 5 is the new text; "after one fix attempt" appears nowhere in the governing skill; "Conditions 2 to 8 stay hard stops" is unchanged | R-9 |
| T-14 | Phase 05 Step 7 names "the phase's effective `fixes` attempts", stops on a fix that changes a conclusion, and rejects (05b) when the budget is used up or a run makes no progress; "fix once and test again" is gone | R-10 |
| T-15 | Phase 05 "After two rejected iterations, stop." and the opening sentence at `:27-28` are unchanged | R-10 |
| T-16 | The README template block equals the governing template block | R-11 |
| T-17 | README absence values read "(`inherit`, `ask`, `5`, `0`, `false`)" | R-12 |
| T-18 | Self-check record line is "`Self-check: done — N corrections`"; "N fixes" appears nowhere in the governing skill | R-14 |
| T-19 | Nothing else changed: `git diff --stat` outside `.speccen/` lists only the governing skill, `05-implementation/SKILL.md` and `README.md`; the Locks section is unchanged | R-13, R-15 |

**Behaviours to cover** (what must be true): absence and the upgrade both mean the default `5`
(R-2, R-12); an invalid value falls back to `1`, never to more attempts (R-6, error path); a fix
that changes a conclusion stops at once, whatever the budget (R-5, error path); a run that
brings back a breach stops even with budget left (R-4, error path); Phase 05 rejects, not stops,
when the budget runs out (R-10); every attempt is logged (R-7); `fixes` has no effect in a
`gated` phase (R-1).

**Coverage intent:** every requirement R-1 – R-15 has at least one check; every error path above
has one.

### Deviations Protocol

> "Any deviation from this Implementation Plan during Phase 05 must be:
> 1. Stopped immediately
> 2. Documented in `phase-05-implementation/phase.md` under the `deviations` anchor
> 3. Reviewed by the Architect before implementation continues"

In `autonomous` mode, a deviation within implementation detail is decided and recorded by the
delegate; one that changes a requirement, a contract, the scope or a phase's Why is a stop
(stop condition 4).

<a id="requirements"></a>
## Requirements & acceptance scenarios

Each requirement cites its source. They are restated in the [specification](./specification.html).

| Id | Requirement (SHALL) | Scenario (WHEN → THEN) | Source |
|---|---|---|---|
| R-1 | The configuration SHALL take a `fixes` key — top level and on the five phases that take `stops` — with the whole numbers `1` to `10` (phase level also `inherit`), effective only in `autonomous` phases and independent of `stops`. | WHEN a project file sets `phases.code-analysis.fixes: 2` and the phase is `autonomous` → THEN its gate test allows two fix attempts. WHEN the phase is `gated` → THEN `fixes` has no effect. | brief §2, §2.3; DD-11 |
| R-2 | The default SHALL be `5`. | WHEN no file sets `fixes` → THEN the gate test allows up to five fix attempts, then stops. | ADR 2026-11-12 (overrides brief §3, DD-17) |
| R-3 | A failing gate test SHALL be fixed and re-run up to the effective `fixes` attempts; each later run re-checks the rows that failed in the run before and the rows that cite a changed file. | WHEN `fixes: 3` and run 1 fails two rows → THEN the delegate fixes them and run 2 re-checks those rows and the rows citing the files it changed; the others keep their last `confirmed (run N)`. | brief §2.1 |
| R-4 | The delegate SHALL stop when a run makes no progress: a rule breach the run before named is still there, or more rows fail than in the run before. | WHEN run 3 fails a row on the same breach as run 2 → THEN the delegate stops, even with budget left. WHEN run 3 fails one row on a new breach after run 2 failed one → THEN it continues. | DD-14; brief §2 guard 1 |
| R-5 | The delegate SHALL stop at once when the next fix would change a phase conclusion, a delegated decision or an ADR. | WHEN the only fix for a failing row is to change a delegated decision → THEN the delegate stops before fixing, whatever the budget. | DD-13; brief §2 guard 2 |
| R-6 | The budget SHALL be at most 10; a `fixes` value that is not a whole number from `1` to `10` SHALL count as `1`. | WHEN a file sets `fixes: 12` or `fixes: many` → THEN the effective budget is `1`. | ADR 2026-11-11 (overrides DD-12); brief §2.6 |
| R-7 | Each fix attempt SHALL be logged as `fix attempt <n> of <fixes>: run <N> failed rows <list>`. | WHEN the delegate makes its second fix attempt with `fixes: 3` → THEN `log.md` gets `fix attempt 2 of 3: run 2 failed rows …`. | brief §2.1 |
| R-8 | After a stop, the Architect's answer SHALL set which rows the next run re-checks and whether further fix attempts are allowed; without that, one run, and a failing row stops again. | WHEN the Architect answers a stop with "yes" to re-checking two rows → THEN one run re-checks them, and a failing row is a new stop. | brief §2.1 |
| R-9 | Stop condition 5 SHALL name the three causes: the budget is used up, no progress, a fix that changes a conclusion, a delegated decision or an ADR. | WHEN a reader looks up why a gate test stopped → THEN condition 5 names all three. | brief §2.2 |
| R-10 | The Phase 05 accept check SHALL use the same budget and guards; when the budget is used up or a run makes no progress, the delegate SHALL reject (05b); a fix that changes a conclusion SHALL stop. | WHEN `phases.implementation.fixes: 2` and the accept check fails twice with progress → THEN the delegate makes two fix attempts, then rejects and runs 05b. | DD-10, DD-13 |
| R-11 | The template SHALL be version 3 with `fixes: 5` at the top, its comment, its legend line and `fixes: inherit` on the five phases; the Keys row SHALL say the current version is `3`; the README copy SHALL equal it. | WHEN a new project file is written → THEN it has `version: 3` and every `fixes` line; the README shows the same block. | brief §2.4; DD-15, DD-18 |
| R-12 | Upgrading a project file to version 3 SHALL add `fixes: 5` and `fixes: inherit` on the five phases and set `version: 3`; the value added is the value its absence means, so every effective setting is kept; both lists of absence values SHALL name `5`. | WHEN this repository's version-2 project file is upgraded → THEN it gains `fixes: 5`, `fixes: inherit` × 5 and `version: 3`, and no value it had changes. | brief §2.5; DD-19; ADR 2026-11-12; the Architect: "introduce version key, should be auto while upgrading skills" (log 11:05) |
| R-13 | A project `lock` SHALL stop a bundle or local file from raising `fixes`, as for every other key. | WHEN the project file locks `code-analysis` and a bundle file sets `phases.code-analysis.fixes: 3` → THEN the bundle value is skipped and the session says so once. | brief §2.6 |
| R-14 | The self-check record line SHALL read `Self-check: done — N corrections`. | WHEN a gate test records its self-check → THEN the line reads "N corrections", and "fix" means only a gate-test fix attempt. | DD-16 |
| R-15 | The change SHALL touch only the governing skill, the Phase 05 skill and the README. | WHEN the change lands → THEN `git diff --stat` outside `.speccen/` lists those three files. | DD-3; DD-20 |

<a id="outcome"></a>
## Outcome

Selected approach: the brief's §2 change as refined by the Phase 03 decisions (DD-9 – DD-20), in
five implementation phases (configuration → gate test → Phase 05 accept → restated copies →
verification). Fifteen requirements, nineteen text checks. The plan, the Test Plan and the intent
seeds are approved when the delegate's gate test passes (autonomous).

<a id="open-items"></a>
## Open Items

| # | Item | Settles in |
|---|---|---|
| O-6 | Acceptance and "done when" (Phase 01 hypothesis H-4) — settled by R-1 – R-15 | settled |
| — | `MATERIAL — unconfirmed`: the ceiling of 3 (DD-12) and progress by breaches (DD-14) | settled at the end-of-run review: DD-12 OVERRIDDEN (ceiling 10), DD-14 ADOPTED |

Residual assumption: the verifier lists every breach per row (`:1181-1182`), which the progress
guard relies on.
