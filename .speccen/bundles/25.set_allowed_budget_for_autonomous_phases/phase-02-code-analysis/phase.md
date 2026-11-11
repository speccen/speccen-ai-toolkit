---
type: Phase
phase: "02 — Code Analysis"
status: COMPLETE
description: The one-fix rule lives in two places with different outcomes; the brief's seven diffs (six subsections) miss four restated sites; the upgrade rule already carries a version-3 bump
---

<a id="phase-top"></a>
# set allowed budget for autonomous phases — Code Analysis

[Index](../index.md) · [State](../STATE.md) · [Log](../log.md)

---

<a id="extensions"></a>
## Extensions applied

| Extension | Why | Where it applies | Outcome |
|---|---|---|---|
| — | — | — | No extensions for this phase |

`.speccen/extensions/code-analysis/` does not exist in this repository.

<a id="code-analysis"></a>
## Code Analysis

The "code" is the speccen plugin source of 26.1108.1 (commit `8ecb30a`,
`.claude-plugin/plugin.json`). The branch HEAD `f371eb9` adds only `.speccen/` files on top of
it, so every source line reference below holds at both. The source is Markdown skills, one agent, commands, `README.md` and
`ARCHITECTURE.md`. All line references below are to that HEAD. Searches ran inline on the session
model (the governing skill allows a search unit; none was launched).

### Architecture Overview

- **Single source of truth.** `skills/sdd/00-governing-workflow/SKILL.md` (2 230 lines) holds
  Configuration (`:666-986`) and Autonomous Execution (`:1093-1313`). The phase skills
  `01`–`05` point to it: each **Mode behaviour** section ends "Decision basis, stop conditions and
  records: **Autonomous Execution** in the governing skill" (`01:245`, `02:440`, `03:441`,
  `04:497`, `05:331`).
- **The gate test** is defined once (`:1148-1185`) and is run at the end of every `autonomous`
  core phase. One phase adds its own repair rule on top: Phase 05 Step 7
  (`05-implementation/SKILL.md:320-325`).
- **Stop conditions** are a numbered list (`:1205-1219`); condition 5 is the gate-test stop
  (`:1212`). `stops: proceed` removes only condition 1 (`:1249-1250`).
- **Configuration** is three layers of YAML files (project, bundle, each with a personal file)
  resolved per phase (`:917-953`). The project file is kept current by the Step 0 upgrade
  (`:409-419`, `:846-915`), driven by the template's `version` (`:691`, `:735`).
- **Copies outside the skill.** `README.md:238-305` repeats the project template block character
  for character (checked: `diff` of `SKILL.md:732-797` and `README.md:239-304` is empty), and
  `README.md:191-195` restates the upgrade rule with its absence values. `ARCHITECTURE.md:140-175`
  summarises configuration and the delegate without naming `stops`, `prototypes` or the gate-test
  repair rule.
- **Dependents.** The gate-check verifier runs on `agents/speccen-worker.md` on the session model
  (`:1169-1172`, `:1388-1394`); the Retrospective audits the gate checks
  (`07-retrospective/SKILL.md:27`, `:134-140`).

### Behavioural Analysis

The current gate-test behaviour in an `autonomous` phase (`:1148-1185`, `:1205-1239`):

1. Evaluate the phase's Quality Criteria row by row with cited evidence; write
   `## Delegate gate check` (`:1152-1157`).
2. Self-check five common failures and record `Self-check: done — N fixes` (`:1158-1168`).
3. If the host can run subagents, verifier run 1 re-opens every row (`:1169-1171`); without
   subagent support, the `verified` column says `not run` and no verifier runs (`:1172`).
4. If any row fails: **fix it once**, then run 2 re-checks failed rows and rows whose evidence is
   in a changed file; others say `confirmed (run 1)` (`:1176-1178`).
5. If a re-checked row still fails: **stop** (`:1179`; condition 5 `:1212`). A stop writes STATE,
   a summary open item, a log entry and a stop round (`:1224-1232`).
6. After a stop, the Architect's answer sets which rows the next run re-checks (`:1180-1182`).
   No limit on the number of post-stop runs and no progress rule exist.

Phase 05 Step 7 has a different outcome for the same "fix once" (`05:320-325`): if the accept gate
fails, "fix once and test again. If it still fails, the delegate rejects: run Phase 05b". Phase
05b (`05:326-330`) reverts only the files this iteration changed — if that cannot be established,
it stops — and re-enters Phase 05a; "After two rejected iterations, stop" (stop condition 6,
`:1213-1214`). It does not stop on condition 5.

**Execution flow (current text):**

```
            ┌──────────────────────────────────────┐
            │ gate test, autonomous  :1152-1168    │
            │ rows + evidence, self-check          │
            └──────────────────┬───────────────────┘
                               ▼
                  ┌──────────────────────────┐
                  │ host can run subagents?  │
                  └─────┬──────────────┬─────┘
                      no│              │yes
                        ▼              ▼
          ┌───────────────────┐   ┌──────────────────────┐
          │ verified =        │   │ verifier run 1       │
          │ "not run"  :1172  │   │ (session model)      │
          └─────────┬─────────┘   └──────────┬───────────┘
                    └──────────┬─────────────┘
                               ▼
                      ┌─────────────────┐
                      │ any row failed? │
                      └───┬─────────┬───┘
                        no│         │yes
                          ▼         ▼
             ┌────────────────┐   ┌─────────────────────────────┐
             │ transition     │   │ Phase 05 accept (Step 7)?   │
             └────────────────┘   └───┬─────────────────────┬───┘
                                    no│                     │yes
                                      ▼                     ▼
               ┌──────────────────────────┐   ┌──────────────────────────┐
               │ fix ONCE; run 2 re-checks│   │ fix ONCE; test again     │
               │ failed + changed-file    │   │ 05:324                   │
               │ rows  :1176-1178         │   └─────────────┬────────────┘
               └─────────────┬────────────┘                 ▼
                             ▼                      ┌──────────────┐
                  ┌──────────────────────┐          │ still fails? │
                  │ re-checked row still │          └──┬────────┬──┘
                  │ fails?               │           no│        │yes
                  └───┬──────────────┬───┘             ▼        ▼
                    no│              │yes      ┌──────────┐ ┌───────────────────────┐
                      ▼              ▼         │ accept → │ │ reject → 05b 05:326   │
               ┌────────────┐ ┌──────────────┐ │ Phase 06 │ └───────────┬───────────┘
               │ transition │ │ STOP — cond. │ └──────────┘             ▼
               └────────────┘ │ 5  :1212     │            ┌──────────────────────────┐
                              │ stop round   │            │ revert limited to this   │
                              └──────┬───────┘            │ iteration's files?       │
                                     ▼                    └──┬────────────────────┬──┘
                    ┌──────────────────────────┐           no│                    │yes
                    │ Architect's answer sets  │             ▼                    ▼
                    │ rows of next run :1180   │      ┌────────────┐  ┌──────────────────────┐
                    │ (no limit, no progress   │      │ STOP       │  │ 2nd rejection?       │
                    │ rule) → back to "re-     │      │ 05:327-328 │  └───┬──────────────┬───┘
                    │ checked row still fails?"│      └────────────┘    no│              │yes
                    └──────────────────────────┘                          ▼              ▼
                                                              ┌──────────────┐ ┌──────────────┐
                                                              │ re-enter 05a │ │ STOP — cond. │
                                                              │ 05:329       │ │ 6  05:330    │
                                                              └──────────────┘ └──────────────┘
```

Side effects of a stop: `STATE.md` `AWAITING ARCHITECT REVIEW`, a summary open item, a `log.md`
entry, an interview stop round (`:1224-1232`). State read: the phase's effective `mode` and
`stops` (`:917-953`), read again before every gate decision (`:956-957`).

### Data Model

**Configuration keys** (`:687-700`, Keys table):

| Key | Values | Default | Levels | Phases |
|---|---|---|---|---|
| `version` | whole number | none (absent = predates versioning) | project file only | — |
| `mode` | `gated` · `autonomous` | `gated` | top + per phase | 01–05 |
| `stops` | `ask` · `proceed` (`inherit` per phase) | `ask` | top + per phase | 01–05 (`:707`) |
| `model` | `inherit` · tiers | `inherit` | per phase | 02–08 except 01 (`:708-709`) |
| `prototypes` | `0` or more | `0` | per phase, `compliance-review` only | 03 |
| `lock` | `true` · `false` | `false` | committed files only | all eight |

`stops` is the precedent for a key with a top-level default **and** a per-phase override with
`inherit` (`:694-695`). `prototypes` is the precedent for a **numeric autonomous budget** with a
fail-safe ("not a whole number of `0` or more counts as `0`", `:941`).

**Template version.** The current version is `2` (`:691`, `:735`). Version 1 added `version` and
`stops` (example `:872-905`); version 2 added `model` on `specification` and `implementation`
(`:907-908`). The rule for a new key: "When the template gains a key, its `version` goes up by
one, and the key, its comment and the value that means its absence are added above"
(`:914-915`).

**Gate-check table:** columns `item | result | evidence | verified` (`:1156-1157`); `verified`
values `confirmed`, `confirmed (run N)`, or a failure; `not run` without subagents
(`:1172`).

**Cardinalities** (observed): a gate check holds 15–24 rows (this bundle's Phase 01: 17; the 2026-11-05 bundle's Phase 04: 24, its `summary.md` "Verifier run 1: 20 of 24 rows confirmed"). Runs per
gate: 1 to 6 (brief §1: 4 runs; 2026-11-05 bundle Phase 04 row 12: 6 runs through four stop
rounds, retrospective `:55-60`; this bundle's Phase 01: 3 runs, one stop, failed rows 5 → 2 → 0).

### Coding Patterns & Style

- **Prose rules, not code.** Each rule is a bullet or numbered item; cross-references name the
  section ("Autonomous Execution → Gate test") rather than a line.
- **Where a key is stated.** A key can appear in up to six places: the Keys table, "Which phases
  take which key", the template, the upgrade absence values, effective settings and the fail-safe.
  `stops` appears in five (`:694-695`, `:707`, `:741-745` and per phase, `:858-859`,
  `:925-926`) and has no fail-safe line. `prototypes` appears in the Keys table (`:698`), the
  template, the upgrade (`:859`), effective settings (`:925-926`) and the fail-safe (`:941`), but
  not under "Which phases take which key". A budget key like `fixes` would touch the places
  `stops` touches plus a fail-safe line like `prototypes`.
- **Upgrade examples.** The version-1 upgrade has a full worked example (`:872-905`); version 2
  has one sentence (`:907-908`). A version-3 sentence follows the version-2 precedent.
- **Fail-safe phrasing.** Most invalid values resolve to the restrictive meaning — `mode` to
  `gated`, `lock` to `true`, `prototypes` to `0`, an unreadable file to a `gated` bundle
  (`:937-943`). Two do not: an invalid `model`, or a tier the host cannot run, counts as
  `inherit`, the session's model (`:947-948`); an unknown `phases` entry or a key on a phase that
  does not take it is ignored and mentioned once (`:944-946`).
- **Restating copies** in `README.md` are prose for readers plus the verbatim template.
- **Naming.** The self-check line already uses the word "fixes" for a different count:
  `Self-check: done — N fixes` (`:1168`).

**Test conventions.** The repository has no test suite and no test runner; `.github/workflows/`
holds only `bump-version.yml`, which bumps the calendar version on push to `main`
(paths-ignore: `.github/**`, `README.md`, `ARCHITECTURE.md`, `LICENSE`). The previous bundle
verified its text changes with an ad-hoc Python script of string checks
(`.speccen/bundles/2026-11-05.use_cheaper_subagent_to_work/files/phase-05-text-checks.py`,
checks `T-1` … `T-19`, including `T-11`: README template block equals the skill's). The Phase 04
Test Plan can follow that approach.

<a id="conventions"></a>
## Project Conventions Confirmation

`.claude/` does not exist in this repository. `.github/` holds one `.md` file, `SECURITY.md`, plus
`CODEOWNERS` and `workflows/bump-version.yml` (not Markdown; read for context).

#### `.github/SECURITY.md`
**Read:** ✓  
**CRITICAL/MANDATORY Rules:** "Please do not report security vulnerabilities through public GitHub issues, discussions, or pull requests."  
**Architecture Boundaries:** N/A  
**Technology Constraints:** "This project uses calendar-based versions (`YY.MDD.N`). Security fixes are applied to the latest release only."  
**Naming Conventions:** N/A  
**Critical Workflows:** private vulnerability reporting via the Security tab, or speccen@cucurbit.be; acknowledgement within 5 working days.  
**Hard Constraints:** In scope: "Instructions or commands that could cause an assistant to run unintended or destructive actions"; "Prompt-injection weaknesses in the skills and workflows"; "Vulnerabilities in the GitHub Actions workflows (for example, script injection or token misuse)"; "Secrets or credentials committed to the repository".

#### `.github/CODEOWNERS` (context, not Markdown)
**Read:** ✓  
**Hard Constraints:** `*` → `@speccen/team-leads`; `/.github/` and `/.claude-plugin/` → `@speccen/team-leads`. Every file this change touches is owned by `@speccen/team-leads`.

#### Durable store (`.speccen/`) — prior art
- Lesson `2026-11-05.readme_restates_config_template`: "`README.md` repeats the governing
  skill's project config template character for character … A rule change that edits only the
  governing skill leaves the README and ARCHITECTURE contradicting it. A string-equality check of
  the two template blocks catches drift (check T-11)."
- Lesson `2026-11-05.ste_term_list_before_writing`: one STE row needed six verifier runs and four
  stop rounds; a full rewrite with one fixed term per actor and thing then passed after one more
  cycle, and the lesson advises setting that list before writing.
- Decision `2026-11-05.self_check_interview_structure`: the fifth self-check item.
- No decision governs the number of fix attempts. The Architect stated on 2026-11-11 "no push on
  main is allowed" (log 11:05); this bundle runs on a feature branch.

### Performance Characteristics

The cost unit is a **verifier run on the session model** (`:1388-1394`) plus, on a stop, one
Architect round.

- Today: at most 2 runs before a stop; after a stop, unbounded (`:1180-1182`; retrospective
  finding "runs after a stop are unruled and unbounded").
- Delta re-check scope is often most of the table: this bundle's run 2 and run 3 each re-checked
  14 of 17 rows, because the fixes touched `phase.md`, which most rows cite. The 2026-11-05
  retrospective records the same as a LOW finding, titled `B2's "evidence in a file you changed" will
  often re-select most rows`.
- With the brief's budget: at most `fixes + 1` runs per gate before a stop (brief §3), each about
  the cost of run 2 today.

### Relationship to Similar Components

| Budget | Where | Bound | Configurable | Outcome when spent |
|---|---|---|---|---|
| Gate-test repair | `:1176-1179` | 1 fix | no | stop (condition 5) |
| Phase 05 accept repair | `05:324` | 1 fix | no | reject → 05b |
| Phase 05 reject-and-retry | `05:330`, `:1213-1214` | 2 iterations | no | stop (condition 6) |
| Phase 03 loop | `:1214` | 2 iterations | no | stop (condition 6) |
| Prototypes | `:698`, Phase 03 Step 5a | `prototypes` | yes, `compliance-review` only | stop |
| Failed subagent unit | `:1355-1356` | 1 inline re-run | no | gate-test failure (`autonomous`) |

`prototypes` is the only configurable budget today. The brief adds the second and makes it the
first with a top-level default.

### Known Issues & Code Commentary

- 2026-11-05 retrospective, MEDIUM: "B2 governs only the second verifier run; runs after a stop
  are unruled and unbounded" (`retrospective.md:55`). Its recommendation added the post-stop
  re-check sentence (now `:1180-1182`); 26.1108.1 shipped it. The brief cites this finding.
- 2026-11-05 retrospective, `[Delegation]`: the delegate answered a brief decision listed "for the
  Architect" (DD-13) while deferring its siblings on the same basis. That brief's heading was
  "## 7. Decisions for the Architect (yes / no)"; this brief's §5 is a similar heading, "Decisions
  for the plugin Architect", and is empty.
- 2026-11-05 retrospective, INFO: "Phase 05's accept path still reads "fix once and test again"
  (pre-existing)" (`retrospective.md:149-150`) — the same finding as S-12.
- No TODO, FIXME or HACK markers in the sites below (searched).

<a id="restated-sites"></a>
### Sites the change touches

| # | Site | What it says today | In the brief? |
|---|---|---|---|
| S-1 | `SKILL.md:1176-1182` gate test | "fix it once … If a re-checked row still fails, stop." + after-stop rule | yes, §2.1 (cites `:1176-1182`) |
| S-2 | `SKILL.md:1212` stop condition 5 | "a gate test still fails after one fix attempt;" | yes, §2.2 |
| S-3 | `SKILL.md:694-695`, `:707` Keys + "Which phases take which key" | `stops` rows and line | yes, §2.3 (cites `:694-698`) |
| S-4 | `SKILL.md:731-798` template | `version: 2`, `stops` block, legend, per-phase `stops: inherit` | yes, §2.4 (cites `:741-790`) |
| S-5 | `README.md:238-305` template copy | identical to S-4 | yes, §2.4 (cites `:245-290`) |
| S-6 | `SKILL.md:857-861` upgrade absence values | "`mode: gated`, `stops: ask` and `lock: false` …" | yes, §2.5 |
| S-7 | `SKILL.md:907-908` version-2 sentence | "An upgrade to version 2 also adds …" | yes, §2.5 (cites `:902-905`; the sentence is at `:907-908`) |
| S-8 | `SKILL.md:925-926` effective settings | "(`stops`, `model`, `prototypes`) … (`ask`, `inherit`, `0`)" | yes, §2.6 |
| S-9 | `SKILL.md:941` fail-safe | `prototypes` line | yes, §2.6 |
| S-10 | `SKILL.md:691` Keys table, `version` row | "the current version is `2`" | **no** |
| S-11 | `README.md:193` upgrade prose | "with the value that keeps today's behaviour (`inherit`, `ask`, `0`, `false`)" | **no** — `fixes: 1` adds `1` |
| S-12 | `05-implementation/SKILL.md:324` | "If it fails, fix once and test again. If it still fails, the delegate rejects" | **no** — the reach question (Phase 01 hypothesis H-2) |
| S-13 | `SKILL.md:1168` self-check line | "`Self-check: done — N fixes`" — same word, other count | **no** |
| S-14 | `SKILL.md:944-946` fail-safe, "a key on a phase that does not take it" | names `mode` and `model` examples only | **no** — covers `fixes` on 06–08 generically |
| S-15 | `README.md:217-219`; `SKILL.md:744`, `README.md:251` comment | "a gate test keeps failing"; "Hard stops (… failed gate or tests) always halt." | no — both stay true after a budget is spent |
| S-16 | `ARCHITECTURE.md:142-143` | "it adds to the project file any key a newer template introduced, with the value that means what its absence meant, and bumps its `version`" | no — stays true for a version-3 upgrade |
| S-17 | `SKILL.md:1249-1250` | "Conditions 2 to 8 stay hard stops" — covers condition 5 | no — stays true; condition 5 stays a hard stop |
| S-18 | `SKILL.md:416-419` Step 0 | the upgrade trigger and its one-line notice | no — stays true |
| S-19 | `05-implementation/SKILL.md:27-28` | "in `autonomous` mode the delegate also rejects it when the gate test fails" | no — stays true; restates the Phase 05 outcome behind S-12 |

One more brief reference is off by one: §4 cites `:1183-1184` for "evidence that does not show
what the row claims has not passed"; line 1183 is blank and the sentence ("You review your own
work … an item without cited evidence has not passed.") is at `:1184-1185`. The brief's `:1249`
holds ("Condition 1 is the **only** stop `proceed` removes", `:1249-1250`).

<a id="interview"></a>
## Interview

**Round 1 — stop round** (stop condition 5: the gate test still failed after one fix attempt) —
answered by the Architect

| # | Question | Depends on | Proposed | Answer |
|---|---|---|---|---|
| 02/1 | [02/1 \| May the delegate fix the four remaining problems and run the checker once more?] Rows 5, 8, 10, 19 and every row that cites a changed file. | — | yes | Architect: "ok, continue" (log 15:31) |
| 02/2 | [02/2 \| Should the Phase 05 opening sentence be added to the list of sites as "stays true"?] | — | yes | Architect: "ok, continue" (log 15:31) — added as S-19 |
| 02/3 | [02/3 \| Should the phase description say "seven diffs in six subsections" instead of "six diffs"?] | — | yes | Architect: "ok, continue" (log 15:31) |

"ok, continue" is read as yes to every proposal of the round, and logged that way.

**Round 2 — stop round** (check run 3 failed row 20 after the first stop) — answered by the
Architect

| # | Question | Depends on | Proposed | Answer |
|---|---|---|---|---|
| 02/4 | [02/4 \| May the delegate reword the row 20 evidence and re-check only rows 14, 17 and 20?] | 02/1 | yes | Architect: "ok, continue" (log 15:41) |

<a id="outcome"></a>
## Executive Summary

- **Dominant finding:** the one-fix rule exists twice with different outcomes. The governing gate
  test stops after one fix (S-1, S-2); Phase 05's accept gate also fixes once but then rejects
  and reverts instead of stopping (S-12). The brief's "applies to every `autonomous` phase" meets
  both, but its diffs change only the first.
- **Root cause of the problem the brief states:** the repair limit is a constant (1) tied to stop
  condition 5, with no progress measure; after a stop the number of runs is unbounded. Observed
  in three bundles: the brief's client bundle, the 2026-11-05 bundle, and this bundle's own
  Phase 01 (failed rows 5 → 2, stopped, then 0 after the Architect's "yes").
- **Key insight:** the change slots into existing patterns — `stops` for a top-level key with a
  per-phase `inherit`, `prototypes` for a numeric budget with a fail-safe, and the upgrade rule
  ("its `version` goes up by one", `:914-915`) for the template bump. Four restated sites are
  outside the brief's diffs (S-10, S-11, S-13, S-14), besides the reach question (S-12).

<a id="open-items"></a>
## Open Items

| # | Item | Settles in |
|---|---|---|
| O-1 | Reach: does `fixes` also govern the Phase 05 accept repair (S-12), whose spent budget leads to reject-and-revert, not a stop? (Phase 01 H-2) | Phase 03 |
| O-2 | The decisions the brief's empty §5 should hold: default `1`, values `1`–`3`, ceiling `3`, the progress measure, the conclusions guard, template `version: 3` (Phase 01 H-3). Its heading reserves them "for the plugin Architect" (see the `[Delegation]` retrospective finding). | Phase 03 |
| O-3 | Sites outside the brief's diffs: S-10 (version row), S-11 (README absence values), S-14 (fail-safe example) — include as consequences of the change? | Phase 03 |
| O-4 | S-13: the self-check line uses "fixes" for another count — rename, or keep? | Phase 03 |
| O-5 | Progress measure: the brief compares the number of failed rows run to run; a later run re-checks a different set of rows (failed + changed-file rows). Is "fewer failed rows among the rows re-checked" the measure? | Phase 03 |
| O-6 | Acceptance scenarios and "done when" (Phase 01 H-4). | Phase 04 |

None of these blocks Phase 03: each is a decision or an acceptance item, and the facts behind
them are recorded above.

<a id="evolution-gap"></a>
## Evolution-gap determination

Not generated. No structural-blockage indicator fires: the change adds a key and rewords rules in
Markdown skills, along the existing `stops` and `prototypes` patterns and the existing upgrade
rule (`:914-915`). No boundary conflict, missing seam, contract limit, scaling wall or
entanglement was found.
