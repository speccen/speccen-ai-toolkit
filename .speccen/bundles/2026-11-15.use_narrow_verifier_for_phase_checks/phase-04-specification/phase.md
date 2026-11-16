---
type: Phase
phase: "04 — Specification"
status: COMPLETE
description: Four implementation phases rewrite the Gate test's verifier rules, the verifier unit and work order, the worker bullet and five claim-source lines, then bump the version; checked by text checks T-1 – T-19
---

<a id="phase-top"></a>
# use narrow verifier for phase checks — Specification

[Index](../index.md) · [State](../STATE.md) · [Log](../log.md)

---

<a id="extensions"></a>
## Extensions applied

| Extension | Why | Where it applies | Outcome |
|---|---|---|---|
| — | — | — | No extensions for this phase |

<a id="interview"></a>
## Interview

Mode: `autonomous` (bundle config); `stops: proceed` (project config). Basis: the brief (log
2026-11-15 21:14), the Architect's stop answers (log 2026-11-16 06:19), the Phase 02 conventions,
the Phase 03 decisions DD-9 – DD-21 and the standing decisions.

**Round 1** — no question depends on another.

| # | Question | Depends on | Proposed | Answer |
|---|---|---|---|---|
| 04/1 | Test approach — verify the change with a throwaway text-check script in the bundle's `files/`, run by the main session, as earlier bundles did? The repository has no test framework. | — | yes | delegate: as proposed — basis: Phase 02 [conventions](../phase-02-code-analysis/phase.md#conventions) ("Tests of skill text") — [DD-22](../delegated-decisions.md#dd-22) |
| 04/2 | Version value — set the next version by the CI's own rule (`YY.MDD.N`: today's prefix, `.N` + 1 if the current version has today's prefix, else `.1`), on the day Phase 05 runs? | — | yes | delegate: as proposed — basis: brief item 4; `bump-version.yml` (Phase 02); DD-10 — [DD-23](../delegated-decisions.md#dd-23) |
| 04/3 | Claim-source line — add it to each phase's Mode behaviour as one bullet, `**Verifier claims.**`, directly before the line that points to the governing skill? | — | yes | delegate: as proposed — basis: brief "Files to change" item 3 ("add that phase's line from rule 5, and refer to the governing skill for the rest") — [DD-24](../delegated-decisions.md#dd-24) |
| 04/4 | Plan structure — four implementation phases, one per group in the brief's "Files to change" (governing Gate test; Subagent Execution and the worker; phase skills; version and checks)? | — | yes | delegate: as proposed — basis: brief "Files to change" items 1 – 4 — [DD-25](../delegated-decisions.md#dd-25) |

No question was answered "later". All four are `not material`: the basis decides each one.

**Round 2 — stop round** (stop condition 5: a breach run 1 named is partly still there) — see
[summary → Stop](./summary.md#stop).

| # | Question | Depends on | Proposed | Answer |
|---|---|---|---|---|
| 04/5 | [04/5 \| May the delegate make this repair and run the checker once more?] | — | yes | Architect: yes ([log](../log.md), 2026-11-16 06:35) |
| 04/6 | [04/6 \| Should "one rule per bullet" be checked by hand, not by the script?] | — | yes | Architect: yes ([log](../log.md), 2026-11-16 06:35) |

**Round 3 — stop round** (stop condition 5: fix budget used; more items fail) — see
[summary → Second stop](./summary.md#stop-2).

| # | Question | Depends on | Proposed | Answer |
|---|---|---|---|---|
| 04/7 | [04/7 \| May the delegate make this repair, with one more checker run?] | — | yes | Architect: yes ([log](../log.md), 2026-11-16 08:17) |
| 04/8 | [04/8 \| Should that run re-check only the breaches run 6 named?] | 04/7 | yes | Architect: yes ([log](../log.md), 2026-11-16 08:17) |

**Round 4 — stop round** (the Architect's 04/8: a breach in the fix text stops the run) — see
[summary → Third stop](./summary.md#stop-3).

| # | Question | Depends on | Proposed | Answer |
|---|---|---|---|---|
| 04/9 | [04/9 \| May the delegate make this one-word repair, with one more checker run?] | — | yes | Architect: yes ([log](../log.md), 2026-11-16 08:20) |
| 04/10 | [04/10 \| Should that run re-check only step 6 of the business seed?] | 04/9 | yes | Architect: yes ([log](../log.md), 2026-11-16 08:20) |

**Round 5 — stop round** (the Architect's 04/10: a breach in the changed step stops the run) — see
[summary → Fourth stop](./summary.md#stop-4).

| # | Question | Depends on | Proposed | Answer |
|---|---|---|---|---|
| 04/11 | [04/11 \| Which wording should step 6 use?] | — | B | Architect: yes — B ([log](../log.md), 2026-11-16 08:21) |
| 04/12 | [04/12 \| If B, should that run re-check only that one sentence, with no further fix attempt?] | 04/11 | yes | Architect: yes ([log](../log.md), 2026-11-16 08:21) |

<a id="implementation-plan"></a>
## Implementation Plan

### Proposed Changes Summary

| File | Change | What |
|---|---|---|
| `skills/sdd/00-governing-workflow/SKILL.md` | modified | Gate test: replace the self-check heading, the verifier bullet and the later-runs rule (lines 1197 – 1220), and the after-a-stop bullet (1235 – 1238) with Appendix A. Units: the verifier row (1390) → Appendix B. The worker and the work order: add the verifier template after the generic one (after 1409) → Appendix C |
| `agents/speccen-worker.md` | modified | One bullet under **Do:** → Appendix D |
| `skills/sdd/01-feature-analysis/SKILL.md` … `05-implementation/SKILL.md` | modified | One `**Verifier claims.**` bullet in each Mode behaviour → Appendix E |
| `.claude-plugin/plugin.json`, `.claude-plugin/marketplace.json` | modified | `version` (1 line), `metadata.version` and `plugins[0].version` (2 lines) → Appendix F |
| `{{FOLDER_NAME}}/files/phase-05-text-checks.py` | created | Text checks T-1 – T-19 (bundle file, not shipped) |

No file is deleted. No new pattern is introduced in code; the skill gains one data structure
(the claim list, DD-14, DD-20, DD-21). Unchanged by decision: Phase 07 (DD-12), README and
ARCHITECTURE (DD-13), the six self-check items (DD-15), the stop conditions (DD-16), the generic
work-order template (DD-17), the verifier model (brief rule 12).

<a id="target-flow"></a>
### Target-State Execution Flow

```
   ┌───────────────────────────────────────────┐
   │ phase work; each gate row with code or    │
   │ repository evidence records its claims    │
   └─────────────────────┬─────────────────────┘
                         ▼
               ┌───────────────────┐
               │ any claim listed? │
               └───┬───────────┬───┘
                 no│           │yes
                   ▼           ▼
   ┌────────────────────┐ ┌────────────────────┐
   │ no verifier; rows  │ │ subagents?         │
   │ n/a — bundle-      │ └───┬────────────┬───┘
   │ internal           │   no│            │yes
   └─────────┬──────────┘     ▼            ▼
             │      ┌──────────────┐ ┌───────────────────────────┐
             │      │ verified =   │ │ launch verifier (≤ 15     │
             │      │ "not run"    │ │ claims) ║ self-check runs │
             │      └──────┬───────┘ │ at the same time          │
             │             │         └─────────────┬─────────────┘
             │             │                       ▼
             │             │         ┌───────────────────────────┐
             │             │         │ per claim: confirmed /    │
             │             │         │ slip / wrong; ≤ 2 noticed │
             │             │         └─────────────┬─────────────┘
             │             │                       ▼
             │             │         ┌───────────────────────────┐
             │             │         │ slip → correct citation   │
             │             │         │ (no fix attempt, no run)  │
             │             │         └─────────────┬─────────────┘
             └─────────────┴───────────┬───────────┘
                                       ▼
                             ┌──────────────────┐
                             │ any item fails?  │◄───────────────────────┐
                             │ (wrong claim, or │                        │
                             │ self-check item) │                        │
                             └──┬────────────┬──┘                        │
                              no│            │yes                        │
                                ▼            ▼                           │
                  ┌──────────────────┐ ┌──────────────────────────────┐  │
                  │ gate passes →    │ │ next fix changes a           │  │
                  │ transition       │ │ conclusion / ADR / DD, or    │  │
                  └──────────────────┘ │ budget used, or no progress? │  │
                                       └──┬────────────────────────┬──┘  │
                                       yes│                        │no   │
                                          ▼                        ▼     │
                               ┌───────────────────┐ ┌───────────────────┴──┐
                               │ stop (condition 5)│ │ fix; re-run only the │
                               └───────────────────┘ │ wrong claims, claims │
                                                     │ whose file changed,  │
                                                     │ promoted noticed     │
                                                     └──────────────────────┘
```

What changes against the [current-state flow](../phase-02-code-analysis/phase.md#behaviour):
claims are recorded with the rows; a phase with no claim runs no verifier; the verifier runs
beside the self-check and settles only listed claims; a `slip` is corrected without a fix
attempt; a later run re-checks claims, not rows. The stop triggers are unchanged (DD-16).

<a id="strategy"></a>
### Strategy Evaluation

No competing approaches: the brief fixes the rules and the template; Phase 03 settled the open
choices (DD-9 – DD-21). No prototype ran.

<a id="phases"></a>
### Implementation Phases

#### Phase 1: Gate test — the narrow verifier rules ✅

**Why:** The verifier's breadth and the cost of slips come from three places in the Gate test:
"re-open the evidence of every row", a failure rule with no slip, and a later-runs rule keyed
to changed files. This phase replaces them first, because every other edit points to it. —
source: [Phase 02 #outcome](../phase-02-code-analysis/phase.md#outcome); brief rules 1 – 4, 6 – 11
(log 2026-11-15 21:14)

##### 1.1 Replace the self-check, verifier and later-runs text
- [x] In `skills/sdd/00-governing-workflow/SKILL.md`, replace the block from `- **Self-check before the verifier.**` through `fix. Rows it does not re-check keep their last \`confirmed (run N)\`.` (lines 1197 – 1220 at `92ee62f`) with Appendix A, part 1
- [x] Keep the six self-check items word for word (1199 – 1208) and the `Record the self-check…` line
- [x] Keep the parked-question and extension bullets (1214 – 1216) in place, after the `verified` column bullet

##### 1.2 Restate the after-a-stop bullet
**Why:** It speaks of rows and "every rule breach it finds in that row", which a claim-based run does not produce. — source: DD-11 (03/3)
- [x] Replace the bullet `- After a stop, the Architect's answer sets which rows…` (1235 – 1238) with Appendix A, part 2
- [x] Leave the stop triggers (1221 – 1226), the recording-repair paragraph (1228 – 1232) and the log-line paragraph (1234) unchanged

##### 1.3 Build and Validate
- [x] Run T-1 – T-9, T-15, T-17 (`files/phase-05-text-checks.py`)
- [x] Render the governing skill's Gate test section and check the nesting of the new bullets

#### Phase 2: Subagent Execution and the worker ✅

**Why:** The unit registry and the work order tell the main session how to launch the verifier; the worker bullet tells the worker how to behave, because the narrow template has no `Follow:` line. It comes after Phase 1 because it points to the rules Phase 1 writes. — source: brief "Files to change" items 1 – 2; [Phase 02 #patterns](../phase-02-code-analysis/phase.md#patterns); DD-17

##### 2.1 Units row
- [x] Replace the row `| any \`autonomous\` phase | the gate-check verifier (Autonomous Execution → Gate test) | — | the gate decision |` (line 1390) with Appendix B

##### 2.2 Verifier work order
- [x] After the generic template's closing fence (line 1409), add Appendix C
- [x] Leave the generic template unchanged (DD-17)

##### 2.3 Worker bullet
- [x] In `agents/speccen-worker.md`, under **Do:**, after the search bullet, add Appendix D

##### 2.4 Build and Validate
- [x] Run T-10 – T-12, T-14

#### Phase 3: Claim sources in the phase skills ✅

**Why:** Each phase names what its claims are drawn from, so the delegate knows what to list. — source: brief rule 5 and "Files to change" item 3; DD-24

##### 3.1 One bullet per phase
- [x] `01-feature-analysis/SKILL.md` Mode behaviour: add Appendix E (01) directly before `- Decision basis, stop conditions and records: …` (line 245)
- [x] `02-code-analysis/SKILL.md`: Appendix E (02) directly before the same `- Decision basis, stop conditions and records: …` line (line 440)
- [x] `03-compliance-review/SKILL.md`: Appendix E (03) directly before the same line (line 441)
- [x] `04-specification/SKILL.md`: Appendix E (04) directly before the same line (line 497)
- [x] `05-implementation/SKILL.md`: Appendix E (05) before the bullet `- Write \`## Delegate gate check\` into \`{{SUMMARY_FILE}}\`. Decision basis…` (line 336)

##### 3.2 Build and Validate
- [x] Run T-13, T-14

#### Phase 4: Version and the full check ✅

**Why:** The brief asks for a version bump in both manifests; the last phase runs every check over the finished text. — source: brief "Files to change" item 4; DD-10, DD-23

##### 4.1 Version
- [x] Compute the next version by the CI rule on the day of Phase 05 (Appendix F)
- [x] Set it in `.claude-plugin/plugin.json` `.version` and `.claude-plugin/marketplace.json` `.metadata.version` and `.plugins[0].version`

##### 4.2 Build and Validate
- [x] Run T-1 – T-19; all pass
- [x] `python3 -c "import json;json.load(open(...))"` on both manifests
- [x] `git diff --stat` touches only the files in the Proposed Changes Summary

<a id="risks"></a>
### Risk Mitigation

| Risk | Impact | Mitigation |
|---|---|---|
| A restated site still says "every row" for the verifier | Medium | T-14 greps every skill and the agent for verifier lines with "every row" / "every quote" / "re-open the evidence of every" |
| The rewrite drops a kept rule (a self-check item, a stop trigger, the session model) | High | T-15 compares the kept passages with `92ee62f` character for character |
| The manual bump collides with the CI bump on merge | Low | Recorded as DD-10 for the review round; the CI re-bumps from the manual value, so no version is lost |
| The verifier template is read as replacing the generic one | Medium | T-11 checks both templates exist; DD-17 |
| Line numbers shift between phases of the edit | Low | Edits anchor on quoted text, not line numbers |

<a id="test-plan"></a>
### Test Plan

Framework: none in the repository. A throwaway script, `files/phase-05-text-checks.py`, run by
the main session with `python3 -I`, asserts on the edited text (DD-22). One part is checked by
hand: whether each inserted bullet states one rule (T-19, 04/6). Each check reads its
place in the file, not the whole file (lesson `2026-11-11.text_checks_read_their_place`).

| Target | Test type | Why |
|---|---|---|
| Gate test section of the governing skill | text check | the rules 1 – 4, 6 – 11 and the after-a-stop restatement |
| Units row, verifier template, worker bullet | text check | the unit and its work order |
| Mode behaviour of Phases 01 – 05 | text check | each names its claim source |
| Kept passages | text check (diff against `92ee62f`) | rule 12 and DD-12, DD-13, DD-15, DD-16, DD-17 |
| Manifests | text check | the bump |
| Runtime behaviour of a narrow run | none | the change is instructions; it takes effect only in later bundles. Phase 07 can review a later run |

Behaviours to cover (from the brief and Phase 03, not from the written text):

| Test | What must be true |
|---|---|
| T-1 | Gate test states the split: the self-check owns everything inside the bundle; the verifier owns only code and repository claims and never reads the bundle |
| T-2 | Claims are recorded in the same step as the row; the list exists at the gate |
| T-3 | Claim list place: directly under the gate table, under `Claims` (DD-14); claim form `K-<n> (row <N>) · claim · how to check · expected`; a command preferred; content not line number, with `path:line` allowed; one or two tool calls, else split or drop |
| T-4 | Exhaustive claims first, with the whole-scope count or "none found"; spot checks never confirm such a row alone; other rows at most 3; every load-bearing count; binding convention quotes only; a rule from an untouched technology is cited by file, not listed |
| T-5 | Cap of 15 per run; the rest `not on list — low risk` |
| T-6 | Parallel launch: verifier as soon as the list is final, self-check at the same time, with the reason |
| T-7 | `slip` and `wrong` defined; slip uses no fix attempt and no re-run; unsure → `wrong`; result appended after `→` |
| T-8 | The verifier reads nothing beyond what settles its claims; at most 2 `noticed:` lines; answered in a `noticed-<n>` row; promoted to a `wrong` claim if it affects a conclusion |
| T-9 | `verified` values: `confirmed (run N)` rule, `n/a — bundle-internal`, `not on list — low risk`, no-claim → no verifier, `not run` without subagents; later runs re-check only wrong, changed-file and promoted claims; slips never; rows not re-checked keep their last `confirmed (run N)`; after a stop, the Architect sets which claims; without that answer, one run follows, and a `wrong` claim stops again; the verifier reports on every listed claim in one run |
| T-10 | Units row names the narrow verifier and keeps the gate decision in the main session |
| T-11 | Verifier template has `Unit: … — NARROW`, `do not read bundle files`, `Claims:`, `Stop:`, `Outputs: none — report only`, the three-value return and at most 2 `noticed:`; the verifier template sits directly after the generic one; generic template unchanged |
| T-12 | Worker bullet: narrow; one or two tool calls per claim; does not read the bundle; return format one line per claim — `confirmed`, `slip — <correct value>` or `wrong — <actual value>` — then at most 2 `noticed:` lines |
| T-13 | Each of Phases 01 – 05 Mode behaviour has its `**Verifier claims.**` bullet with the rule-5 source; each bullet ends with `(governing skill → Gate test)`; 01 says no verifier run; 04 names every file, symbol and integration point the plan changes or extends, at most one claim per plan step that touches existing code, and the traceability rows with the self-check; 05 says the main session runs the full suite itself |
| T-14 | **Error case:** no single line of a skill or the agent that mentions the verifier says "every row", "every quote" or "re-open the evidence of every" (checked line by line, so the self-check's own "Check every row yourself" line does not count) |
| T-15 | **Unchanged:** the six self-check items, the stop triggers, the `fixes` budget sentence, the recording-repair paragraph, the log-line paragraph, the parked/extension bullets, the session-model sentences (governing 778, 1453 – 1454), the generic template — identical to `92ee62f` |
| T-16 | Both manifests carry the same new version, in `YY.MDD.N` form, greater than `26.1115.1` |
| T-17 | **Edge:** the Gate test still has exactly one `Self-check: done — N corrections` instruction and one `fixes` budget sentence |
| T-18 | Phase 07, README and ARCHITECTURE have no diff against `92ee62f` |
| T-19 | **Wording:** in the text Phases 1 – 3 insert, every sentence has at most 30 words; a code span counts as one word, and a bold label ending in a full stop is its own sentence (script). Every inserted bullet states one rule (by hand: the main session reads each bullet and records "one rule" or the split it made, 04/6) |

Coverage intent: every acceptance scenario (specification R-1 – R-13) has at least one check.

<a id="deviations-protocol"></a>
### Deviations Protocol

> "Any deviation from this Implementation Plan during Phase 05 must be:
> 1. Stopped immediately
> 2. Documented in `phase-05-implementation/phase.md` under the `deviations` anchor
> 3. Reviewed by the Architect before implementation continues"

In `autonomous` mode, step 3 is the delegate's decision within Phase 05's Mode behaviour.

<a id="appendix"></a>
### Appendices — the exact text

#### Appendix A, part 1 — replaces governing lines 1197 – 1220

```markdown
- **Who checks what.** The self-check owns everything inside the bundle. The verifier owns only
  claims about the code and the repository. The verifier never reads the bundle.
- **Claims.** When you write a gate row that rests on code or repository evidence, record that
  row's load-bearing claims in the same step. At the gate the list already exists.
  - Record the claims directly under the gate table, under `Claims`, one line each:
    `K-<n> (row <N>) · claim · how to check · expected`.
  - **How to check** is preferably a command whose output settles the claim.
  - A `path:line` is allowed. The claim is about the content, not the line number.
  - Each claim is settled in one or two tool calls. If it cannot be, split it or drop it.
- **What goes on the list.**
  - **Exhaustive claims first.** A row that claims something holds everywhere, or nowhere,
    carries one claim that covers the whole scope: a count or a "none found" check. For
    example: `grep -rn 'new HttpClient(' src | wc -l` = 0. Spot checks never confirm such a row
    on their own.
  - Other rows: at most 3 claims, the ones the row's conclusion rests on.
  - Every count that a conclusion depends on.
  - Verbatim quotes only of convention rules that bind the change. A rule from a technology the
    change does not touch is cited by file and is not on the list.
  - **Hard cap: 15 claims per run.** If more qualify, keep the 15 whose failure would change a
    conclusion, and mark the rest `not on list — low risk`.
  - Each phase's **Mode behaviour** names the source of its claims.
- **Self-check.** Check every row yourself for the six common failures, and fix what you find.
  Run it at the same time as the verifier (next bullet):
  1. **Quotes** — every quote of the Architect matches `log.md` word for word.
  2. **References** — every `path:line` and anchor still points at what the row says; re-open
     the files you edited after you wrote the row.
  3. **Latest answer** — no record (phase file, DD, ADR, summary) is behind the newest Architect
     statement in `log.md`.
  4. **Index** — `index.md` lists every file this phase wrote.
  5. **Interview structure** — every round holds only the frontier, and every question one
     decision.
  6. **Subjects** — every question and item put to the Architect has a `[number | text]`
     subject; no label stands alone.
  Record the self-check in one line above the gate table: `Self-check: done — N corrections`.
- **Verifier.** Where the host can run subagents, launch the **verifier** (`speccen-worker`, on
  the session model — see Subagent Execution) with the verifier work order. Launch it as soon as
  the claim list is final. This is safe beside the self-check: the self-check edits only bundle
  files, and the verifier reads only code and the repository.
  - The verifier settles the listed claims and reads nothing beyond what settles them.
  - It returns one result per claim. Append each result to its claim line, after `→`.
  - **`slip`** — the content is there, but the line number, path or count is a little off, and
    the conclusion stands.
  - For a slip, the verifier gives the correct value, and you correct the citation.
  - A slip is not a failed row: it uses no fix attempt and triggers no re-run.
  - **`wrong`** — the content is not there, or the value differs in a way the conclusion depends
    on.
  - A `wrong` claim fails its row, and the fix loop below applies.
  - If the verifier is unsure which kind it is, it reports `wrong`.
  - It may add at most 2 `noticed:` lines about something adjacent that looks wrong.
  - Answer each `noticed:` line in a row at the foot of the gate table:
    `noticed-<n> | <the line> | corrected, or not relevant, because … | <evidence> | —`.
  - A `noticed:` line that affects a conclusion becomes a `wrong` claim in the next run.
- **The `verified` column.**
  - A row is `confirmed (run N)` when every claim it has is `confirmed`, or `slip` with the
    citation corrected.
  - A row without claims reads `n/a — bundle-internal`.
  - A row whose claims the cap left off the list reads `not on list — low risk`.
  - If no row cites code or repository evidence, launch no verifier. Every row then reads
    `n/a — bundle-internal`.
  - Without subagent support, write `not run` in that column.
```

Then the two kept bullets (parked question; extensions), then:

```markdown
- If any item fails, fix it and run the test again — up to the phase's effective `fixes`
  attempts (Configuration; default `5`). A later verifier run re-checks only (a) the `wrong`
  claims, (b) the claims whose file changed during the fix, and (c) any `noticed:` line promoted
  to a claim. Slips are never re-checked. Rows it does not re-check keep their last
  `confirmed (run N)`.
```

#### Appendix A, part 2 — replaces governing lines 1235 – 1238

```markdown
- After a stop, the Architect's answer sets which claims the next verifier run re-checks, and
  whether further fix attempts are allowed. Without that, one run follows, and a `wrong` claim
  stops again. Claims it does not re-check keep their last result. The verifier reports on every
  listed claim in one run.
```

#### Appendix B — replaces the Units row (governing line 1390)

```markdown
| any `autonomous` phase with a code or repository claim | the gate-check verifier — narrow: settles the listed claims only, never reads the bundle (Autonomous Execution → Gate test) | — | the gate decision; the self-check; every row without a claim |
```

#### Appendix C — added after the generic template (after governing line 1409)

````markdown
The gate-check verifier has its own, narrow work order:

```markdown
**speccen work order**
- Unit: gate-check verifier (Phase NN, run N) — NARROW
- Bundle: [{{FOLDER_NAME}}] — do not read bundle files
- Claims: [≤15, numbered — id · claim · how to check · expected]
- Stop: once every listed claim is settled; one or two tool calls per claim; batch independent checks
- Outputs: none — report only
- Return: one line per claim — `confirmed` · `slip — <correct value>` · `wrong — <actual value>`; then at most 2 `noticed:` lines
```
````

#### Appendix D — added to `agents/speccen-worker.md`, under **Do:**, after the search bullet

```markdown
- For a gate-check verifier, the work order is narrow: settle only the listed claims, in one or
  two tool calls each, and do not read the bundle. Return one line per claim — `confirmed`,
  `slip — <correct value>` or `wrong — <actual value>` — then at most 2 `noticed:` lines.
```

#### Appendix E — one bullet per phase Mode behaviour

- **01:** `- **Verifier claims.** None: Phase 01 has no codebase access, so no verifier runs (governing skill → Gate test).`
- **02:** `- **Verifier claims.** Convention quotes that bind the change, counts, "none found" claims, and the code facts behind each pattern or risk conclusion (governing skill → Gate test).`
- **03:** `- **Verifier claims.** The code facts behind an ADR's rationale or a prototype's result (governing skill → Gate test).`
- **04:** `- **Verifier claims.** The plan's anchors in the existing code: every file, symbol and integration point the plan changes or extends exists as described. At most one claim per plan step that touches existing code. The traceability rows stay with the self-check (governing skill → Gate test).`
- **05:** `- **Verifier claims.** The implementation does what the row says: a single named test run, a symbol present, a pattern absent. Never the full suite — the main session runs that itself (governing skill → Gate test).`

Wrap each at the file's usual width (about 98 characters), with a two-space hanging indent.

#### Appendix F — the version

`NEW = <YY>.<M without leading zero><DD>.<N>`, where `N` = current `N` + 1 if `26.1115.1` already
has the day's prefix, else `1`. On 2026-11-16 this is `26.1116.1`. Set the same value in all
three places.

<a id="outcome"></a>
## Outcome

Selected approach: the brief's rules, written into the Gate test as Appendix A, with the unit,
work order, worker bullet and claim-source lines around it, and the version bumped by hand.
Four implementation phases; text checks T-1 – T-19. Approved under delegation as part of the
gate test (Test Plan included; no test waived).

<a id="open-items"></a>
## Open Items

| # | Item | Settles in |
|---|---|---|
| R-1 | [R-1 \| Review round: manual version bump against the CI bump (DD-10); claim-list place, form and result, `MATERIAL — unconfirmed` (DD-14, DD-20, DD-21)] | end of run |

No residual assumption: every edit site is anchored on quoted text at `92ee62f`.
