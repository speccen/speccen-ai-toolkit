---
type: Reference
phase: "08 — Reference"
status: COMPLETE
description: Technical reference for the gate-test fix budget — the fixes key (1–10, default 5), its three guards, template version 3 and the Phase 05 accept; what changed in three files, and why.
---

# Gate-Test Fix Budget — Reference (reduced view)

[Index](../index.md) · [State](../STATE.md) · [Log](../log.md) · [Specification](../phase-04-specification/specification.html) (what we set out to build)

---

> This file is the **reduced view** of the reference. [reference.html](./reference.html) is the full, authoritative reference. It holds the five diagrams (C4 levels 1 to 4 and the argument diagram). Here each diagram appears as described text.

*speccen plugin · GitHub issue 25 · fix · Reference (Phase 08)*

This change adds one configuration key, `fixes`. It sets how many times the delegate repairs a failing gate test before it stops. Three guards bound every repair loop. The key takes `1` to `10`. The default is `5`. The change is prose and YAML in three files. No code runs.

- 19/19 — text checks T-1 – T-19 pass
- all fail — checks in the move test, after it moves the text (the checks detect misplaced text)
- 3 — files changed
- 2 — bundle ADRs (ceiling 10, default 5)
- 26.1108.1 — plugin version
- 77fb4f4 — implementation commit
- 438e538 — ceiling ADR commit

**Current text.** The default-5 amendment of 2026-11-12 is committed after 438e538. The text in this reference is the current text of the three files. Where a bundle phase file still says "default 1", that wording is history. The code and the amended specification (revised 2026-11-12) are current.

*1 · The system*

## Where the change lives

speccen is a plugin of skills. A skill is a text file. The skills guide a Software Architect and an AI through a phased workflow. A phase runs in one of two modes. In `gated` mode, the Architect decides at the end of the phase. In `autonomous` mode, the Architect's delegate decides.

An autonomous phase ends with a **gate test**. The delegate checks the phase against its quality criteria and writes one row per item. A **verifier** subagent re-opens the evidence of every row. If a row fails, the delegate repairs the record and runs the test again.

Before this change, the delegate made one repair. A second failure was a stop. In the evidence of issue 25, most second failures were precision faults: a line number one off, a count that differed between two files. The Architect answered "yes, go ahead" to almost every such stop. The stop cost attention and added no decision.

This change makes the number of repairs a setting. The new key is `fixes`. It does not depend on `stops`. The key `stops` answers "may the delegate decide a material question". The key `fixes` answers "how often may the delegate repair its own work before it asks for help".

*Diagram (see reference.html for the drawing):* Level 1, context. The Architect sets the key fixes in the speccen config files and answers stops. The speccen plugin (changed: the gate-test rule and the config contract) is read by the host (Claude Code). The host runs the delegate and the verifier subagent. The delegate writes the gate rows into the bundle (summary.md, log.md). The config files (changed: a new key) are read by the plugin.

`L1` **Context.** Accent border: changed in this work. Muted: unchanged. The Architect edits the key. The plugin reads it. The host runs the delegate and the verifier. Nothing outside speccen is involved.

*2 · The three files*

## What the change touched

The change touches three files. All other skills and all code are unchanged. The other phase skills run their gate test through the governing skill, so they take the new rule without an edit.

*Diagram (see reference.html for the drawing):* Level 2, containers. Three changed files: the governing skill (skills/sdd/00-governing-workflow/SKILL.md), the Phase 05 skill (skills/sdd/05-implementation/SKILL.md) and README.md. The governing skill defines the rule. The Phase 05 skill points back to it in Step 7. The README holds a copy of the config template that must equal the template in the governing skill. Unchanged: the skills of phases 01 to 04 and 06, which run their gate test through the governing skill; and the project file .speccen/speccen-config.yaml, which speccen upgrades from the template at session start.

`L2` **The three files.** The governing skill is the only file that defines the rule. The two other changed files restate or point to it.

| File | What changed | Where (current text) |
|---|---|---|
| `skills/sdd/00-governing-workflow/SKILL.md` | Keys table and phase list; template `version: 3` with `fixes`; upgrade to version 3; effective settings; fail-safe; gate-test repair rule with three guards; self-check line; stop condition 5 | `:696-697`, `:710`, `:738-791`, `:870`, `:922-924`, `:941`, `:958`, `:1185`, `:1193-1208`, `:1237-1238` |
| `skills/sdd/05-implementation/SKILL.md` | The Step 7 accept uses the budget and the same guards. A spent budget or a run with no progress is a rejection (Phase 05b) | `:320-327` |
| `README.md` | The template copy gains `fixes: 5` and `version: 3`. The upgrade paragraph names `5` among the absence values | `:193`, `:242-295` |

*3 · Sections on the path*

## Which sections carry the rule

A skill has sections, not classes. This level shows each section that carries the rule, in the order a reader meets it. The accent path runs from the key definition to the stop condition.

1. **Keys** defines `fixes` and the values `1` – `10`.
2. **Effective settings, Locks and Fail-safe** turn the files into one number for a phase.
3. **Gate test** uses that number as the repair budget and applies the guards.
4. **Stop conditions**, condition 5, names the three causes of a stop.
5. **Phase 05 Step 7** reuses the same budget and guards for the accept.

The template, the upgrade text and the README copy keep the project file and its documentation in line with the key.

*Diagram (see reference.html for the drawing):* Level 3, components. Inside the governing skill: Keys and phase list (:696-710), Template (:738-791), Upgrading the project file (:870, :922-924), Effective settings plus Locks plus Fail-safe (:933-958), Gate test (:1165-1208) and Stop conditions, condition 5 (:1237-1238). All are changed. Unchanged: Proceeding on a proposal, which removes only stop condition 1. The accent path runs Keys, Effective settings, Gate test, Stop condition 5. In the Phase 05 skill, Step 7 accept (:320-327, changed) reuses the gate test; Phase 05b rejection (:328, unchanged text) runs when the budget is spent or a run makes no progress. In the README, the template copy (:242-295) and the upgrade paragraph (:190-196) are changed; the copy must equal the template.

`L3` **Sections on the path.** Solid accent arrows: the path of the rule. Dashed arrows: restated or reused text. The README boxes restate the template and the upgrade text. Every box with an accent border changed. The muted boxes did not change.

*4 · Contracts*

## Service Contracts and the key contract

**Service Contracts: none.** The scope is skill prose and YAML. No service is registered, no controller consumes an interface, and no external boundary exists. This reference does not make one up.

The equivalent of a component API here is the **key contract** and the **gate-test rule**. They are the interface between the Architect, the config files and the delegate. The next sections give both.

### Key contract

Input: a `fixes` value in a config file. Output: one effective number per autonomous phase. A value outside `1` – `10` gives `1`. No value gives `5`. See section 6.

### Gate-test rule

Precondition: the phase is `autonomous` and a gate-test row failed. Postcondition: the delegate stops, or the gate test passes, within the effective number of fix attempts. Invariant: no repair changes a conclusion, a delegated decision or an ADR. See section 7.

*5 · One gate-test run*

## One failing gate test, call by call

The diagram shows one representative run in an autonomous phase with the default `fixes: 5`. Steps 1 to 3 existed before. Steps 4 to 9 are the new repair loop. The three guards act inside the loop. A stop at any guard is stop condition 5.

*Diagram (see reference.html for the drawing):* Level 4, runtime sequence. Lifelines: Delegate, Verifier, Bundle files (summary.md and log.md), Architect. Unchanged steps: 1 the delegate writes the gate table and the line 'Self-check: done — N corrections'; 2 it launches verifier run 1; 3 the verifier returns the failed rows, for example 3 and 7. New repair loop: Guard 1, conclusions: if the next fix would change a phase conclusion, a delegated decision or an ADR, stop. 4 The delegate repairs and logs 'fix attempt 1 of 5: run 1 failed rows 3, 7'. Guard 2, budget: the attempt number must not pass the effective fixes (default 5, ceiling 10); when it does, stop (in Phase 05: reject). 5 The delegate launches run 2, which re-checks (a) the rows that failed and (b) the rows whose evidence is in a changed file. 6 The verifier returns, for example, row 7 failed on a new breach. Guard 3, progress: if a breach that the run before named is still there, or more rows fail than in the run before, stop; otherwise go on. 7 The loop repeats steps 4 to 6. 8 The verifier confirms every re-checked row. 9 The delegate writes 'confirmed (run N)' and advances. On any stop, the delegate asks the Architect through a stop round.

`L4` **One run.** Solid arrows are calls. Dashed arrows are returns. The shaded band is new. Accent arrows are the new calls. The numbers 3 and 7 in the example (rows, attempt number) are illustrative.

### What the run records

- One log line per attempt: `fix attempt <n> of <fixes>: run <N> failed rows <list>` (`:1203`).
- Rows that a later run does not re-check keep their last `confirmed (run N)` (`:1196`).
- After a stop, the Architect's answer sets which rows the next run re-checks, and whether more fix attempts are allowed. Without that answer, one run follows, and a failing row stops again (`:1204-1208`).
- Cost: one first run and at most `fixes` repeat runs, so at most `fixes + 1` verifier runs for each gate. Each run is on the session model.

### Evidence from this bundle

This bundle ran under the older one-fix text. The delegate repaired gate tests in a loop under the Architect's words at 15:43 and 15:45 (`log.md`). The table shows the failed rows per verifier run. These are the runs that showed the need for the rule. They are not tests of the new rule. The new rule is not yet measured in a release.

| Gate | Failed rows per verifier run | Source |
|---|---|---|
| Phase 02 | run 4: row 20 · run 5: row 20 (another defect) · run 6: none | DD-8, DD-14 |
| Phase 03 | 5 · 2 · 1 | DD-22, DD-23 |
| Phase 04 | 5 · 3 · 1 · (stop round) · 3 · 3 · 1 | DD-26 – DD-29 |
| Phase 05 | 1 → 1 → 2 → 2 → 2 → 1 → 1 → 0 (accepted after run 8) | Phase 05 summary, DD-30 – DD-32 |

*6 · Configuration reference*

## The `fixes` key

The key is in the Keys table of the governing skill (`:696-697`). Both rows say `autonomous` only.

| Key | Values | Meaning |
|---|---|---|
| `fixes` | `1` – `10` | The default at that level. The number of fix attempts the delegate makes on a failing gate test before it stops. Independent of `stops`. |
| `phases.<phase>.fixes` | `inherit` · `1` – `10` | The fix budget for one phase. `inherit` means no value at this level. |

### Which phases take the key

Five phases take `fixes`: `feature-analysis`, `code-analysis`, `compliance-review`, `specification` and `implementation`. These are the phases that take `mode` (`:710`). The key has no effect in a `gated` phase. Close-out has no exit gate and takes no `fixes`. A `fixes` key on a phase that does not take it is ignored and mentioned once (`:961-963` fail-safe).

### Resolution order

The text says `fixes` resolves "the same way" as the other per-phase keys (`:941`). The steps below follow the rule for `mode` (`:933-939`).

1. The phase-level value, in this order of files: bundle local, bundle, project local, project. `inherit` counts as no value.
2. The top-level `fixes`, in the same order of files.
3. The default `5`.

### Lock

- A lock in the project file binds every file below it. A locked phase, or a top-level `lock: true`, skips the bundle file and both local files. So a project lock stops a bundle or local file from raising `fixes`.
- A lock in the bundle file binds only the bundle's local file.
- A lock in a local file is ignored.
- When a lock overrides a setting, speccen says so once per session.

### Fail-safe

A `fixes` value that is not a whole number from `1` to `10` counts as `1` (`:958`). The fail-safe takes the smallest budget. Absence is different: absence means `5`.

| Input | Effective value | Reason |
|---|---|---|
| `3`, `10` | as written | A whole number from 1 to 10 |
| no `fixes` in any file | `5` | The default (`:941`) |
| `inherit` on a phase | the next level down the order | `inherit` counts as no value |
| `12`, `0`, `many` | `1` | Fail-safe: not a whole number from 1 to 10 |
| any value, phase is `gated` | no effect | The Architect is the gate |

### Template and upgrade to version 3

The template is `version: 3` (`:738`). It has `fixes: 5` at the top (`:751`), a comment and a legend line (`:757`), and `fixes: inherit` on the five phases (`:767`, `:772`, `:778`, `:785`, `:791`). The README holds a copy of this block (`README.md:242-295`).

At session start, speccen compares the project file with the template. A file of an earlier version gets the missing keys with the value that its absence meant. An upgrade to version 3 adds `fixes: 5` at the top and `fixes: inherit` to the five phases, and sets `version: 3` (`:922-924`). It never changes a value that is already there. It does not touch a bundle file or a local file.

An autonomous phase then makes up to five fix attempts. The upgrade sentence says: set `fixes: 1` to keep one.

```diff
+ # How many times the delegate repairs a failing gate test before it stops (autonomous only, 1–10).
+ # It stops sooner when a repair makes no progress or would change a conclusion.
+ fixes: 5
lock: false
#   stops       inherit · ask · proceed — autonomous only: see the top-level stops
+ #   fixes       inherit · 1 – 10 — autonomous only: see the top-level fixes
phases:
  feature-analysis:
    mode: inherit
    stops: inherit
+     fixes: inherit
    lock: false     # … and the same line in code-analysis, compliance-review, specification, implementation
```

Template lines for `fixes`, from `:738-791`. Added lines have a green background.

*7 · The three guards*

## The gate-test rule

The repair rule is in the Gate test section (`:1193-1208`). The delegate fixes a failing item and runs the test again, up to the phase's effective `fixes` attempts. Each later verifier run re-checks two sets of rows: (a) every row that failed in the run before, and (b) every row whose evidence is in a file the delegate changed during the fix.

Three conditions stop the loop. They are the three items under "Stop (stop condition 5) when" (`:1197-1201`). Stop condition 5 itself names the same three causes (`:1237-1238`).

| Guard | The text says | What the delegate does |
|---|---|---|
| **1 · Conclusions** | "the fix you would make next changes a phase conclusion, a delegated decision or an ADR" (`:1198`) | Stops at once, before the fix, with budget left. The budget repairs the record. It does not change what the record concludes. |
| **2 · Budget and ceiling** | "a re-checked row still fails and the budget is used up" (`:1199`) | Stops after `fixes` attempts. The ceiling is the largest value the key accepts, `10`. |
| **3 · Progress** | "a rule breach the run before named is still there, or more rows fail than in the run before" (`:1200-1201`) | Stops, also with attempts left. A run that fails the same number of rows on a new breach is progress. |

### Phase 05: reject, not stop

Step 7 of the Phase 05 skill (`:320-327`) uses the same budget and guards. The outcome differs. If the next fix would change a conclusion, a delegated decision or an ADR, the delegate stops. If the budget is used up, or a run makes no progress, the delegate rejects the implementation and runs Phase 05b (`:328`). Without this step, `phases.implementation.fixes` would have no effect (DD-10).

### Other changes in the same text

- The self-check line says `Self-check: done — N corrections` (`:1185`). The word "fix" now means only a gate-test fix attempt (DD-16).
- Stop condition 5 names three causes instead of one (`:1237-1238`).
- The unchanged rule stays: `stops: proceed` removes only condition 1. Conditions 2 to 8 stay hard stops.

*8 · What changed, and why*

## The decisions behind the numbers

Two bundle ADRs set the budget. Each one overrides a delegated decision. This section gives the reasoning on the page. The ADRs hold the full record.

### ADR 2026-11-11 — the ceiling is 10, not 3

The brief (issue 25, section 2, guard 3) capped the budget at 3. The delegate kept 3 (DD-12) and marked it `MATERIAL — unconfirmed`, because the Architect had also said "I don't know how to express in simple English that have to loop until issues are fixed" (log 15:45). The review put the question to the Architect as R/1. The answer was "1 max loop 10" (log 21:58). DD-12 is `OVERRIDDEN`. The ADR does not record a reason for the number 10. It records no consequences.

| Option | Outcome | Why |
|---|---|---|
| Ceiling 3 (brief, DD-12) | not taken | The Architect chose 10 in review R/1. |
| No ceiling: loop while the progress guard holds | not taken | The brief rejects "Unbounded retries" (section 4). One row failed five runs in a row in the 2026-11-05 bundle. The Architect named a maximum of 10. |
| Ceiling 10 | taken | The Architect's decision. ADR 2026-11-12 states that the progress guard and the conclusions guard bound every loop. |

### ADR 2026-11-12 — the default is 5, not 1

The specification set the default to `1`, so that a project keeps today's behaviour (brief section 3, DD-17). After close-out, the Architect said: "the max cap is raised to 10, and the default value should be 5". The follow-up answers: absence of `fixes`, the template and the version-3 upgrade all mean `5` ("5 everywhere"). An invalid value still counts as `1`. DD-17 is `OVERRIDDEN`. The Architect had the specification amended on 2026-11-12 (R-1, R-2, R-6, R-11, R-12). The skill and the README follow it.

| Option | Outcome | Why |
|---|---|---|
| Default 1 (brief, DD-17) | not taken | It kept today's behaviour. The Architect wanted a larger default. |
| Default 5; absence, template and upgrade all mean 5 | taken | The Architect's decision. The upgrade writes the value that absence means, so the rule "keep every effective setting" still holds. |
| Invalid value counts as 5 | not taken | The Architect answered "Counts as 1". The fail-safe takes the smallest budget. |
| Other defaults (2 – 4, 10) | not discussed | The ADR names only 1 and 5. |

**Consequence.** The default changes behaviour at upgrade. An autonomous project that upgrades to version 3 makes up to five fix attempts for each gate test, where it made one before. The upgrade sentence tells the Architect to set `fixes: 1` to keep one. The brief's claim "Unchanged by default" no longer holds. The progress guard and the conclusions guard bound every loop.

### Alternatives of the brief that stay rejected

| Alternative | Why it was not taken |
|---|---|
| Tie the budget to `stops: proceed` | `proceed` removes only stop condition 1. Conditions 2 to 8 mean the basis is broken or the action is not the delegate's to take. A single key would punish an Architect who wants `ask` for decisions with stops for typos. |
| Unbounded retries | A ceiling and a progress rule stop a costly loop. |
| Let the verifier ignore precision faults | That weakens the gate. Evidence that does not show what the row claims has not passed. |
| Count failed rows for progress (the brief's guard 1) | Not taken: see section 9 and DD-14. |

### Verdicts

Each change has an honest verdict. required means the request or the effect needs it. required for correctness means the rule fails without it. choice means the Architect or the delegate could have chosen otherwise.

| Change | Verdict | Reason |
|---|---|---|
| The `fixes` key, independent of `stops` | required | Issue 25 asks for it. The two keys answer two different questions. |
| Conclusions guard | required for correctness | Without it, a repair loop could rewrite a decision. DD-13, delegated and not reviewed. |
| Progress guard by breaches | required for correctness | A row count compares different sets of rows (section 9). DD-14, adopted. |
| Phase 05 Step 7 uses the budget | required | Without it, `phases.implementation.fixes` has no effect. DD-10, delegated and not reviewed. |
| Template version 3 and the upgrade text | required | The governing skill says a template with a new key goes up by one version. DD-18, delegated and not reviewed. |
| README copy equals the template | required | Specification R-11. The copy would otherwise drift. |
| Ceiling 10 | choice | The Architect's number. No reason is recorded. |
| Default 5 | choice | The Architect's number. It trades the "unchanged by default" property for fewer stops. |
| Invalid value counts as 1 | choice | A cautious fail-safe, in line with the other keys. Confirmed by the Architect in the 2026-11-12 answer. |
| Self-check line says "N corrections" | choice | A wording choice for STE rule 4, "one meaning per word". It could have kept "N fixes". DD-16, delegated and not reviewed. |

*9 · Why breaches, not counts*

## How the progress guard measures progress

The brief said a run makes no progress when it "fails as many rows or more than the run before". The delegate replaced that rule (DD-14). The Architect adopted the replacement ("rest yes", review R/2 – R/3). The text now says: a run makes no progress when a rule breach the run before named is still there, or when more rows fail than in the run before (`:1200-1201`).

The reason is in the re-check scope. Run 1 checks every row. Each later run checks only the rows that failed and the rows that cite a changed file. So two runs check different sets of rows. A row count compares two numbers from two different sets. A converging run can show the same count twice, because each run finds a new, smaller defect.

The Phase 02 gate of this bundle shows it. Run 4 failed row 20. Run 5 failed row 20 again, on a different mechanical defect (DD-8). Run 6 passed. The brief's rule would have stopped at run 5, because one failed row is "as many as" one failed row. The breach rule continues, because the defect of run 4 was gone.

*Diagram (see reference.html for the drawing):* Argument diagram. Phase 02 gate of this bundle, three verifier runs. Run 4 re-checked rows 14, 17 and 20; rows 14 and 17 passed and row 20 failed on defect A. Run 5 re-checked row 20 only; it failed on defect B, a different defect. Run 6 re-checked its rows and none failed. The rule that counts failed rows (rejected) compares 1 failed row with 1 failed row, finds 'as many', and stops at run 5, although defect A was repaired. The rule that follows breaches (taken) sees that the breach of run 4 is gone, and continues. Run 6 passes. The sets of rows differ between runs, so a count does not compare like with like.

**Argument diagram.** The two rules read the same facts. Only the breach rule keeps a converging run alive. The red box rejects the brief's rule. The green box shows the text now in the skill.

**The rule still has a guard against loops.** A breach that comes back stops the run. Also, more failed rows than in the run before stops the run. The ceiling of 10 bounds every other case.

*10 · Delegated decisions*

## Decisions that shaped the outcome

This bundle ran `autonomous`. The delegate took 32 decisions (DD-1 – DD-32). The table lists those that shaped the rule, with their status in `delegated-decisions.md`. A decision with status `DELEGATED` is unreviewed. The Architect has not adopted it. Do not read it as settled.

| Id | Decision | Status | Basis |
|---|---|---|---|
| DD-3 | Scope: only the `fixes` budget | DELEGATED | Brief section 2 |
| DD-10 | The budget also governs the Phase 05 accept check | DELEGATED | Brief: "every `autonomous` phase"; `fixes` takes the same five phases as `mode` |
| DD-11 | Values `1`, `2`, `3` (the range then; now `1` – `10` by the ADR) | DELEGATED | Brief section 2.3 |
| DD-12 | Ceiling: keep 3 | OVERRIDDEN | Architect, review R/1: "1 max loop 10". Basis of the delegate: brief guard 3 and section 4 |
| DD-13 | Conclusions guard: stop at once | DELEGATED | Brief section 2, guard 2 |
| DD-14 | Progress measured by breaches, not by the count of failed rows | ADOPTED | Architect, review R/2 – R/3: "rest yes". Basis: Phase 02 runs 4 – 6 of this bundle |
| DD-15 | The version row of the Keys table says version 3 | DELEGATED | Specification intent; DD-18 |
| DD-16 | Self-check line says "N corrections" | DELEGATED | STE rule 4, one meaning per word |
| DD-17 | Default `1` | OVERRIDDEN | Architect, 2026-11-12: "the default value should be 5"; ADR 2026-11-12 |
| DD-18 | Template version 3 | DELEGATED | Brief sections 2.4, 2.5; the template rule at `:914-915` |
| DD-19 | README absence values gain the value for `fixes` | DELEGATED | Specification intent; the value is now `5` (DD-17 overridden) |
| DD-20 | The fail-safe example stays; it does not name `fixes` | DELEGATED | The rule already covers a key on a phase that does not take it |
| DD-30 | Phase 05 accept after check run 2: repair the check script, do not reject | ADOPTED | "rest yes" (review R/2 – R/3) |
| DD-31 | Phase 05 accept after check run 5: repair the check script, no stop | ADOPTED | "rest yes" |
| DD-32 | Phase 05 accept after check run 6: correct one overstated claim | ADOPTED | "rest yes" |

Other decisions (DD-1 – DD-9, DD-21 – DD-29) are scope, working-hypothesis, evidence and gate-repair decisions of the bundle. They are `DELEGATED` and carry no rule of the skill text. DD-24 keeps the skill-text changes uncommitted for the Architect until the Architect commits them. DD-21 – DD-29 repeat the loop that this change makes official, under the Architect's words at 15:43 and 15:45.

*11 · Sources*

## Source map

This reference is generated from the whole bundle and the current text of the three files. Where the bundle says "default 1", that is the history before the 2026-11-12 amendment.

| What | Where |
|---|---|
| Brief (issue 25) | [files/gh-25-gate-test-fix-budget.md](../files/gh-25-gate-test-fix-budget.md) |
| Specification (revised 2026-11-12) | [phase-04-specification/specification.html](../phase-04-specification/specification.html) · [.md](../phase-04-specification/specification.md) |
| Bundle ADRs | [2026-11-11.fix_budget_ceiling_10](../adrs/2026-11-11.fix_budget_ceiling_10.md) · [2026-11-12.fix_budget_default_5](../adrs/2026-11-12.fix_budget_default_5.md) |
| Delegated decisions | [delegated-decisions.md](../delegated-decisions.md) |
| Durable decisions | `.speccen/decisions/2026-11-11.fix_budget_ceiling_10.md` · `2026-11-11.fix_progress_by_breaches.md` · `2026-11-12.fix_budget_default_5.md` |
| Phase files | [01](../phase-01-feature-analysis/phase.md) · [02](../phase-02-code-analysis/phase.md) · [03](../phase-03-compliance-review/phase.md) · [04](../phase-04-specification/phase.md) · [05](../phase-05-implementation/phase.md) · [06](../phase-06-close-out/phase.md) |
| Text checks T-1 – T-19 and the move test | [files/phase-05-text-checks.py](../files/phase-05-text-checks.py) · [files/phase-05-move-test.py](../files/phase-05-move-test.py) |
| Earlier change this one builds on | `.speccen/features/2026-11-05.use_cheaper_subagent_to_work/reference.html` (gate-test self-check and delta re-check) |
| The code | `skills/sdd/00-governing-workflow/SKILL.md` · `skills/sdd/05-implementation/SKILL.md` · `README.md` |

Reference (Phase 08) for bundle 25.set_allowed_budget_for_autonomous_phases. Plugin version 26.1108.1. Back to the [Index](../index.md).
