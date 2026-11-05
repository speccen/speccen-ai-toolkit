---
type: Phase
phase: "04 — Specification"
status: COMPLETE
description: Six-phase plan — config keys and template v2, the search unit, the gate-test self-check and delta re-check, phase pointers, restated copies, text verification
---

<a id="phase-top"></a>
# Use cheaper subagent to work — Specification

[Index](../index.md) · [State](../STATE.md) · [Log](../log.md)

---

<a id="extensions"></a>
## Extensions applied

| Extension | Why | Where it applies | Outcome |
|---|---|---|---|
| — | — | — | No extensions for this phase |

`.speccen/extensions/specification/` does not exist in this repository.

<a id="interview"></a>
## Interview

Mode: `autonomous` (bundle config), `stops: ask`. The analysis and the five ADRs leave no
contract, data-model, dependency or plan-structure choice open. Two non-material choices remain;
the delegate answers them from the basis.

**Round 1**

| # | Question | Depends on | Proposed | Answer |
|---|---|---|---|---|
| 04/1 | The v1 upgrade example (governing `:418`, `:876`, `:902`) — leave it as the worked example of the v1 upgrade, rather than rewrite it for v2? | — | leave it | delegate: leave it — basis: the example describes the v1 upgrade and stays true; ADR `template_version_2` compliance names it a Phase 04 choice — [DD-14](../delegated-decisions.md#dd-14); superseded by 04/3 (DD-16) |
| 04/2 | Who commits the skill-text change — leave it uncommitted in the working tree for the Architect, with only the bundle files committed at the phase transition? | — | leave it uncommitted | delegate: leave it uncommitted — basis: Phase Transition Protocol step 6 commits "the changed bundle files — only those"; Invariant 6 — [DD-15](../delegated-decisions.md#dd-15) |

**Round 2**

| # | Question | Depends on | Proposed | Answer |
|---|---|---|---|---|
| 04/3 | Reopen 04/1: after the change, the v1 example (`:870–903`) says a pre-versioning file gets its lines "and nothing else", which a v2 upgrade makes untrue. Mark the example as the v1 upgrade and add one sentence for v2? (The Step 0 example at `:418` is an "e.g." of a v1 upgrade line and stays valid.) | 04/1 | yes | delegate: yes — basis: verifier run 1 finding; governing `:909–910` ("When the template gains a key, its `version` goes up by one, and the key, its comment and the value that means its absence are added above"); supersedes DD-14 — [DD-16](../delegated-decisions.md#dd-16) |

**Round 3 — stop round** (stop condition 5: gate rows 12 and 15 failed on verifier run 2) — answered by the Architect

| # | Question | Depends on | Proposed | Answer |
|---|---|---|---|---|
| 04/4 | The row 12 and 15 wording is now corrected (one name per actor in the seeds; DD-1 to DD-16 on the spec page). Re-check only rows 12 and 15, and pass the gate if both are confirmed? | — | yes | Architect: yes ("go ahead") |

**Round 4 — stop round** (stop condition 5: row 12 not confirmed on verifier run 3) — answered by the Architect

| # | Question | Depends on | Proposed | Answer |
|---|---|---|---|---|
| 04/5 | The run-3 row 12 wording is now corrected (the main session corrects record errors; one phrase for the re-checked rows, taken from R-11; the main session sends search work). Re-check only row 12, and pass the gate if it is confirmed? | — | yes | Architect: yes ("proceed") |

**Round 5 — stop round** (stop condition 5: row 12 not confirmed on verifier run 4) — answered by the Architect

| # | Question | Depends on | Proposed | Answer |
|---|---|---|---|---|
| 04/6 | Both seeds are now rewritten with one term per actor (main session, worker, verifier, model tier, search question, evidence) and no sentence over 20 words. Re-check only row 12, and pass the gate if it is confirmed? | — | yes | Architect: yes |

**Round 6 — stop round** (stop condition 5: row 12 not confirmed on verifier run 5) — answered by the Architect; row 12 confirmed on run 6

| # | Question | Depends on | Proposed | Answer |
|---|---|---|---|---|
| 04/7 | The four run-5 rule breaches are corrected (one idea per frontmatter description; "use" no longer a noun; "evidence" has one sense, so the re-checked rows are now "the rows that cite a changed file"), and "team" is now "the Architect". Re-check only row 12, and pass the gate if it is confirmed? | — | yes | Architect: yes |

<a id="implementation-plan"></a>
## Implementation Plan

All line numbers are at commit `b59e7ab` and shift as edits land; each checklist item names the
text it changes so it can be found after a shift. "Governing" is
`skills/sdd/00-governing-workflow/SKILL.md`.

### Proposed Changes Summary

| File | Change | What |
|---|---|---|
| `skills/sdd/00-governing-workflow/SKILL.md` | modify | Keys `version` row (`:691`); `model` phase list (`:708–709`); template `version` and `model` on 04/05 (`:735`, `:772–779`); v1 upgrade example intro (`:870–871`) and closing line (`:902`); fail-safe list (`:940–941`); Units row and sentence (`:1300–1310`); new section `### Search` after **The worker and the work order**; Gate test self-check and delta re-check (`:1153–1160`) |
| `skills/sdd/02-code-analysis/SKILL.md` | modify | one pointer line at the end of Step 2 and of the Step 3 intro |
| `skills/sdd/05-implementation/SKILL.md` | modify | one pointer line in Step 3 |
| `skills/sdd/interview/SKILL.md` | modify | the lookup rule (`:63–67`) points to the search unit for bundle, store and code facts |
| `README.md` | modify | template copy (`:238–303`, S-1) kept identical to governing; "Model tiers" (`:305–329`, S-2) |
| `ARCHITECTURE.md` | modify | Model tiers and Subagents bullets (`:153–158`, S-3), including the verifier fix |
| `agents/speccen-worker.md` | modify | `description` names a search among the unit kinds (S-4) |

No file is created or deleted. No new pattern is introduced: the search unit reuses the work
order, the one-writer rule, the tier resolution and the host-support fallback; its report-only
output follows the verifier's precedent.

### Target-State Execution Flow

What changes relative to the current state: a search is now a listed unit on the phase's tier,
and the gate test gains a self-check before the verifier and a delta-only second run. Compare the
[current-state flows](../phase-02-code-analysis/phase.md#code-analysis).

**Path 1 — launching a unit (to be).**

```
          ┌───────────────────────────────┐
          │ phase step reaches some work  │
          └───────────────┬───────────────┘
                          ▼
              ┌───────────────────────┐
              │ listed in Units table?│  (new row: a search)
              └────┬─────────────┬────┘
                 no│             │yes
                   ▼             ▼
       ┌──────────────────┐  ┌───────────────────────┐
       │ run inline in the│  │ is the unit the gate- │
       │ main session     │  │ check verifier?       │
       │ (a search not    │  └────┬─────────────┬────┘
       │ launched as the  │    yes│             │no
       │ unit runs inline)│       ▼             ▼
       └──────────────────┘  ┌────────────┐  ┌──────────────────────────┐
                             │ session    │  │ tier = phases.<p>.model  │
                             │ model      │  │ (04, 05 now take model;  │
                             └─────┬──────┘  │ no key → inherit)        │
                                   │         └────────────┬─────────────┘
                                   └──────────┬───────────┘
                                              ▼
                               ┌──────────────────────────────┐
                               │ host cannot launch speccen-  │
                               │ worker, or the launch fails? │
                               └──────┬────────────────┬──────┘
                                   yes│                │no
                                      ▼                ▼
                         ┌─────────────────────┐ ┌──────────────────────────┐
                         │ run inline, session │ │ launch speccen-worker:   │
                         │ model; say so once  │ │ work order, model        │
                         └─────────────────────┘ └────────────┬─────────────┘
                                                              ▼
                                               ┌──────────────────────────────┐
                                               │ unit is a search?            │
                                               └──────┬────────────────┬──────┘
                                                   yes│                │no
                                                      ▼                ▼
                               ┌─────────────────────────────┐ ┌──────────────────────┐
                               │ report only: path:line +    │ │ check outputs exist  │
                               │ verbatim quote + not found; │ │ (unchanged)          │
                               │ main session re-opens every │ └──────────────────────┘
                               │ finding before citing it    │
                               └─────────────────────────────┘
```

**Path 2 — the gate test (to be).**

```
     ┌──────────────────────────────────────┐
     │ end of an autonomous phase: evaluate │
     │ criteria with evidence; write table  │
     └──────────────────┬───────────────────┘
                        ▼
     ┌──────────────────────────────────────┐
     │ SELF-CHECK (new): quotes · references│
     │ · latest answer · index · interview  │
     │ structure — fix; record "Self-check: │
     │ done — N fixes"                      │
     └──────────────────┬───────────────────┘
                        ▼
              ┌──────────────────────┐
              │ host runs subagents? │
              └────┬────────────┬────┘
                 no│            │yes
                   ▼            ▼
      ┌──────────────────┐  ┌──────────────────────────────┐
      │ "not run"        │  │ verifier run 1 (session      │
      └────────┬─────────┘  │ model): every row            │
               │            └──────────────┬───────────────┘
               └───────────────┬───────────┘
                               ▼
                     ┌───────────────────┐
                     │ any item failed?  │
                     └───┬───────────┬───┘
                       no│           │yes
                         ▼           ▼
              ┌──────────────┐  ┌─────────────────────────────┐
              │ transition   │  │ fix once; verifier run 2    │
              └──────────────┘  │ re-checks ONLY: rows that   │
                                │ failed + rows whose evidence│
                                │ file changed in the fix;    │
                                │ others "confirmed (run 1)"  │
                                └──────────────┬──────────────┘
                                               ▼
                                     ┌───────────────────┐
                                     │ re-checked row    │
                                     │ still failing?    │
                                     └───┬───────────┬───┘
                                       no│           │yes
                                         ▼           ▼
                                 ┌────────────┐ ┌──────────┐
                                 │ transition │ │  STOP    │
                                 └────────────┘ └──────────┘
```

### Strategy Evaluation

One approach exists: the brief's Changes A and B as refined by the five ADRs. Alternatives were
settled by ADR in Phase 03 (separate search key, host built-in agent, separate lookup row,
four-check self-check), so no strategy table is needed. No prototype ran.

### Implementation Phases

#### Phase 1: Configuration — keys, fail-safe and template version 2 ⬜

**Why:** The `model` key must be accepted on `specification` and `implementation` before any text
gives those phases subagent work; otherwise the fail-safe ignores it. Keys list, fail-safe and
template change together — source: [Phase 02 Data Model](../phase-02-code-analysis/phase.md#code-analysis), ADRs `code_search_tier`, `template_version_2`.

##### 1.1 Keys and fail-safe
- [ ] Governing Keys table, `version` row (`:691`): "the current version is `1`" → "the current version is `2`".
- [ ] Governing "Which phases take which key", `model` bullet (`:708–709`): list `code-analysis`, `compliance-review`, `specification`, `implementation`, `close-out`, `retrospective`, `reference`.
- [ ] Governing Effective settings fail-safe (`:940–941`): "a `model` on `feature-analysis`, `specification` or `implementation`" → "a `model` on `feature-analysis`".

##### 1.2 Template
- [ ] Governing template (`:735`): `version: 1` → `version: 2`.
- [ ] Governing template, `specification:` entry: add `model: economy           # searches` after `stops: inherit`. (Brief A4 writes `# code searches`; the comment is widened because ADR `bundle_store_lookup_unit` widens the unit.)
- [ ] Governing template, `implementation:` entry: add `model: economy           # searches` after `stops: inherit`.

##### 1.3 v1 upgrade example (04/3)
- [ ] Governing example intro (`:870–871`): "gets these lines, marked `+`, and nothing else:" → "gets these lines, marked `+`, and nothing else, when it is upgraded to version 1:".
- [ ] After the example's closing paragraph (`:901–903`), add: "An upgrade to version 2 also adds `model: inherit` to `specification` and `implementation`, and sets `version: 2`."

##### 1.4 Build and Validate
- [ ] No build exists (markdown only). Validate: T-1, T-2, T-3, T-14, T-18, T-19 in the Test Plan pass.

#### Phase 2: Subagent Execution — the search unit ⬜

**Why:** This is Change A: searching becomes a listed unit on the phase tier, so the rule and the
practice agree — source: brief §2 A1–A2, ADRs `code_search_tier`, `code_search_agent`, `bundle_store_lookup_unit`.

##### 2.1 Units table and rule
- [ ] Governing Units table: add the first row `| any phase (bundle and store); 02, 03, 04, 05 (code) | a **search**: find and quote evidence that answers one stated question (Search below) | yes | every conclusion drawn from it; the re-check of every finding it uses |`.
- [ ] Governing `:1309`: "Nothing else runs in a subagent." → "Nothing else runs in a subagent — a search that is not launched as this unit runs inline."

##### 2.2 New section `### Search` (after **The worker and the work order**, before **Model**)
- [ ] State: a search answers one stated question with evidence; read-only; takes no decision.
- [ ] State the work order: the question, the breadth (`quick` · `medium` · `thorough`), where to start if known; `Outputs: none — report only`.
- [ ] State the report: findings only — each a `path:line` and a short verbatim quote — plus what was not found; no conclusions, no recommendations.
- [ ] State: the worker writes no files; the main session re-opens every finding it uses before citing it; a search report is never cited as evidence on its own.
- [ ] State: independent searches may run in parallel (R-15).
- [ ] State the tier: the phase's `model`; in a phase without a `model` key (Phase 01; any phase set to `inherit`) the search runs on the session model. A search in Phase 05 uses `phases.implementation.model`. **Why:** Phase 01 may search the bundle and store but has no `model` key — source: ADR `bundle_store_lookup_unit` compliance.
- [ ] State: the search runs on `speccen-worker`, launched with the tier's model, not on a host's built-in search agent. **Why:** the worker takes the model at launch and already forbids decisions — source: ADR `code_search_agent`.
- [ ] Keep A6 (R-14): no new log format; the existing line serves (`- **HH:MM — [PHASE] subagent** — search: <question> · model: <tier> → <model> (<source>)`).

##### 2.3 Build and Validate
- [ ] Validate: T-4, T-5, T-6, T-15, T-16 pass.

#### Phase 3: Gate test — self-check and delta re-check ⬜

**Why:** This is Change B: fewer and smaller verifier runs, with a fifth check for the failure kind
this bundle met three times — source: brief §3 B1–B2, ADR `self_check_interview_structure`, [Phase 01 gate check](../phase-01-feature-analysis/summary.md#delegate-gate-check) runs 1–3.

##### 3.1 Self-check (B1)
- [ ] Governing Gate test: insert before the verifier bullet a **Self-check before the verifier** bullet with five numbered checks — Quotes, References, Latest answer, Index, Interview structure ("every round holds only the frontier, and every question one decision") — and "Record the self-check in one line above the gate table: `Self-check: done — N fixes`."

##### 3.2 Delta re-check (B2)
- [ ] Governing Gate test (`:1160`): replace "If any item fails, fix it once and run the test again. If it still fails, stop." with the B2 text: the second verifier run re-checks (a) every row that failed and (b) every row whose evidence is in a file changed during the fix; rows not re-checked keep `confirmed (run 1)`; if a re-checked row still fails, stop.

##### 3.3 Build and Validate
- [ ] Validate: T-7, T-8, T-9 pass.

#### Phase 4: Phase skills — pointer lines ⬜

**Why:** Phase skills point into the governing skill with one italic line; the search unit needs
that pointer where searches happen — source: brief §2 A5; Phase 02 Coding Patterns (pointer pattern, 02 `:259`).

##### 4.1 Pointers
- [ ] `02-code-analysis` end of Step 2 and end of the Step 3 intro paragraph: "*Questions about the code may run as search units (governing skill → Subagent Execution → Search). The analysis itself stays in the main session.*"
- [ ] `05-implementation` Step 3, after the per-item list: "*A question that comes up during a checklist item may run as a search unit (governing skill → Subagent Execution → Search). The analysis itself stays in the main session.*" (brief A5: "add the same line")
- [ ] `interview` `:63–67`: the bundle/store lookup becomes "look it up — inline, or as a search unit (governing skill → Subagent Execution → Search)"; the code lookup line for Phases 03 and 04 becomes "Phases 03 and 04 may look it up in the code — inline, or as a search unit."

##### 4.2 Build and Validate
- [ ] Validate: T-10 passes.

#### Phase 5: Restated copies ⬜

**Why:** Restated copies change in the same commit as their source, or the README and ARCHITECTURE
contradict the skill — source: DD-12; [restated sites](../phase-02-code-analysis/phase.md#restated-sites).

##### 5.1 Copies
- [ ] README template block (`:238–303`, S-1): replace with the new governing template block, character for character.
- [ ] README "Model tiers" (`:305–329`, S-2): add one sentence — "Searches (finding and quoting evidence for one question) run on the phase's tier, in Phases 02 to 05 for code and in any phase for the bundle and store."
- [ ] ARCHITECTURE Subagents bullet (`:156–158`, S-3): add the search to the unit list, and change "run in a `speccen-worker` subagent on their tier's model" so the verifier is named as running on the session model.
- [ ] `agents/speccen-worker.md` `description` (S-4): add "a search" to the listed unit kinds.

##### 5.2 Build and Validate
- [ ] Validate: T-11, T-12, T-13, T-17 pass.

#### Phase 6: Verification and hand-over ⬜

**Why:** The skills have no test runner, so the planned checks are the evidence that the text says
what the specification requires — source: [Phase 02 test conventions](../phase-02-code-analysis/phase.md#code-analysis).

##### 6.1 Run all checks
- [ ] Run T-1 – T-19 and record each command and result in `phase-05-implementation/phase.md`.
- [ ] `git diff --stat -- . ':(exclude).speccen'` shows only the seven files of the Proposed Changes Summary.
- [ ] Leave the skill changes uncommitted for the Architect (DD-15).

##### 6.2 Build and Validate
- [ ] All checks pass, or each failure is a deviation.

### Risk Mitigation

| Risk | Impact | Mitigation |
|---|---|---|
| README template drifts from the governing template | Medium | T-11 diffs the two blocks; both edited in Phase 5 from one source |
| Keys list changed but fail-safe not (or the reverse) | High — `model` on 04/05 silently ignored | Phase 1 changes both; T-2 and T-3 check both |
| A cheap model quotes code wrongly | Medium | the main session re-opens every finding before citing it (Phase 2.2); verifier on session model |
| The delta re-check misses a row broken by the fix | Medium | rows whose evidence file changed are always re-checked (Phase 3.2) |
| Line numbers shift during editing | Low | each item names the text it changes |
| Existing projects change behaviour on upgrade | High if it happened | upgrade adds `model: inherit` (`:855–859`); T-14 checks the rule bullets are unchanged |

### Test Plan

The repository has no test framework (Phase 02). Unit and integration tests: **none, because the
change is prose and YAML inside markdown with no executable code**. The planned tests are
**text checks** — shell commands run in Phase 05 after the edits, derived from the requirements
below, not from the edited text. They are not committed (no test location exists).

| Id | Check | Requirement |
|---|---|---|
| T-1 | Governing template block contains `version: 2`, and `model: economy` under both `specification:` and `implementation:`; Keys row says "the current version is `2`"; no other "current version is `1`" | R-7 |
| T-2 | Governing `model` bullet lists exactly the seven phases, including `specification` and `implementation` | R-6 |
| T-3 | Governing fail-safe names only `feature-analysis` for `model` | R-6 |
| T-4 | Units table has the search row; the sentence "a search that is not launched as this unit runs inline" is present; the old bare "Nothing else runs in a subagent." line is gone | R-1, R-5 |
| T-5 | `### Search` section exists between "The worker and the work order" and "Model", and states: one question; `Outputs: none — report only`; `path:line` + verbatim quote + not found; no conclusions; re-open before citing; never cited alone; read-only, takes no decision; `speccen-worker`; tier rule with the no-key case and "A search in Phase 05 uses `phases.implementation.model`" | R-1 – R-4 |
| T-6 | "verifier … session model" statements unchanged (`:1344`, template comment) | R-12 |
| T-7 | Gate test has the self-check bullet with five checks and the `Self-check: done — N fixes` line | R-10 |
| T-8 | Gate test has the delta re-check text and `confirmed (run 1)`; the old "run the test again. If it still fails, stop." is gone | R-11 |
| T-9 | Gate test still requires a stop when a re-checked row fails | R-11 (error path) |
| T-10 | Pointers present in 02 (two), 05 (one), interview (bundle/store and code) | R-1, R-9 |
| T-11 | `diff` of the governing template block and the README template block is empty | R-13 |
| T-12 | ARCHITECTURE units list names the search and no longer puts the verifier on a tier | R-12, R-13 |
| T-13 | Worker description names a search | R-13 |
| T-14 | Upgrade rule bullets (`:852–868`) unchanged: missing phase `model` added as `inherit` | R-8 |
| T-15 | Section *Search* gives the log line in the existing format; the "Log each launched unit" text (`:1336–1337`) is unchanged | R-14 |
| T-16 | Section *Search* states the work-order breadth (`quick` · `medium` · `thorough`) and that independent searches may run in parallel | R-15 |
| T-17 | README "Model tiers" names searches and their phases | R-13 |
| T-18 | No text adds a host-wide default subagent model: Configuration keys gain no new key; `models.<tier>` and the Model section are unchanged apart from the phase list | R-16 |
| T-19 | v1 example intro says "when it is upgraded to version 1" and the v2 sentence follows its closing paragraph | R-8 |

**Behaviours to cover** (what must be true): the search never writes files or decides (R-2);
an unlaunched search runs inline, not silently on a cheap model (R-5); a `model` on 04/05 is
honoured, a `model` on 01 still ignored (R-6, error path); an old project file keeps its
behaviour after upgrade (R-8); a second verifier run still stops on a failing re-checked row
(R-11, error path); the verifier never moves to a cheap tier (R-12).

**Coverage intent:** every requirement R-1 – R-16 has at least one check; every error path above
has one.

### Deviations Protocol

> "Any deviation from this Implementation Plan during Phase 05 must be:
> 1. Stopped immediately
> 2. Documented in `phase-05-implementation/phase.md` under the `deviations` anchor
> 3. Reviewed by the Architect before implementation continues"

In `autonomous` mode, a deviation within implementation detail is decided and recorded by the
delegate; one that changes a requirement, a contract, the scope or a phase's Why is a stop.

<a id="requirements"></a>
## Requirements & acceptance scenarios

Each requirement cites its source. They are restated in the [specification](./specification.html).

| Id | Requirement (SHALL) | Scenario (WHEN → THEN) | Source |
|---|---|---|---|
| R-1 | The governing skill SHALL list a search as a subagent unit: code in Phases 02–05, bundle and store in any phase. | WHEN a phase needs evidence for one question → THEN the Units table names a search unit for that phase and source. | brief A1; ADR `bundle_store_lookup_unit` |
| R-2 | A search SHALL return findings only — `path:line`, verbatim quote, what was not found — and write no file. | WHEN a search unit returns → THEN its report has no conclusion and no file was written. | brief A2 |
| R-3 | The main session SHALL re-open every finding it uses before citing it, and never cite a search report alone. | WHEN a finding is cited in a phase file → THEN the citation points at the code, not at the report. | brief A2 |
| R-4 | A search SHALL run on `speccen-worker` with the phase's `model` tier; with no `model` key, on the session model. | WHEN Phase 02 searches with `model: economy` → THEN the worker is launched with the economy model. WHEN Phase 01 searches the store → THEN it runs on the session model. | ADRs `code_search_tier`, `code_search_agent`, `bundle_store_lookup_unit` |
| R-5 | A search not launched as the unit SHALL run inline. | WHEN the host cannot launch the worker → THEN the search runs inline on the session model and the session says so once. | brief A1; governing Host support |
| R-6 | `model` SHALL be a valid key on `specification` and `implementation`. | WHEN a project file sets `phases.implementation.model: economy` → THEN it is honoured. WHEN it sets `phases.feature-analysis.model` → THEN it is ignored and mentioned once. | brief A3; ADR `code_search_tier` |
| R-7 | The template SHALL be `version: 2` with `model: economy` on `specification` and `implementation`. | WHEN a new project file is written → THEN it has `version: 2` and both keys. | brief A4; ADR `template_version_2` |
| R-8 | Upgrading an existing project file SHALL keep its effective settings. | WHEN a version-1 file is upgraded → THEN it gains `model: inherit` on 04 and 05 and `version: 2`, and no setting changes. | ADR `template_version_2`; governing `:855–859` |
| R-9 | Phase skills 02, 05 and `interview` SHALL point to the search unit. | WHEN a reader is at 02 Steps 2/3, 05 Step 3 or the interview lookup rule → THEN one line points to Subagent Execution → Search. | brief A5; DD-3 |
| R-10 | The gate test SHALL run a five-point self-check before the verifier and record it. | WHEN a phase's gate test starts → THEN the summary shows `Self-check: done — N fixes` above the gate table. | brief B1; ADR `self_check_interview_structure` |
| R-11 | A second verifier run SHALL re-check only failed rows and rows whose evidence file changed, and the workflow SHALL stop if a re-checked row still fails. | WHEN run 1 fails one row and the fix edits one file → THEN run 2 re-checks that row and the rows citing that file; others read `confirmed (run 1)`. WHEN a re-checked row still fails → THEN the workflow stops (a stop). | brief B2 |
| R-12 | The verifier and every decision seat SHALL stay on the session model. | WHEN any tier mapping is set → THEN the verifier still runs on the session model. | brief §4 |
| R-13 | Restated copies SHALL match their source. | WHEN the change lands → THEN the README template equals the governing template, and ARCHITECTURE, README tiers and the worker description name the search. | DD-12 |
| R-14 | Each launched search SHALL be logged with the existing subagent line, naming the tier and the model. | WHEN a search unit is launched → THEN `log.md` gets `- **HH:MM — [PHASE] subagent** — search: <question> · model: <tier> → <model> (<source>)`, and the log format section is unchanged. | brief A6 |
| R-15 | A search work order SHALL state the question, the breadth (`quick` · `medium` · `thorough`) and the start place if known; independent searches MAY run in parallel. | WHEN two searches answer independent questions → THEN both may run at once, each with its own work order. | brief A2 |
| R-16 | The change SHALL NOT add a host-wide default subagent model. | WHEN the change lands → THEN the only model settings are `phases.<phase>.model` and `models.<tier>`. | brief §4 |

<a id="outcome"></a>
## Outcome

Selected approach: the brief's Changes A and B as refined by the five Phase 03 ADRs, in six
implementation phases (configuration → search unit → gate test → pointers → restated copies →
verification). Sixteen requirements, nineteen text checks. The plan, the Test Plan and the
intent seeds are approved by the delegate's passed gate test (autonomous).

<a id="open-items"></a>
## Open Items

| # | Item | Settles in |
|---|---|---|
| O-6 | Acceptance — settled by R-1 – R-16; the brief's §6 measurement on a next bundle is a follow-up, not acceptance (H-5) | settled |
| O-10 | The §6 measurement (log subagent lines per model; verifier runs per phase; `/usage`) — a follow-up for the Architect after the next bundle | after close-out |

Residual assumption: the host honours the model passed at launch; where it does not, Host support
already requires saying so.
