<!--
---
type: Reference
phase: "08 — Reference"
status: COMPLETE
description: Reduced Markdown view of reference.html — [number | text] subjects and the narrowed stop condition 5
---
-->

<a id="phase-top"></a>
# Questions to the Architect: `[number | text]` subjects, never a bare label

[Index](../../bundles/2026-11-13.questions_to_the_architect_number_text_subjects_never_a_bare_label/index.md) · [State](../../bundles/2026-11-13.questions_to_the_architect_number_text_subjects_never_a_bare_label/STATE.md) · [Log](../../bundles/2026-11-13.questions_to_the_architect_number_text_subjects_never_a_bare_label/log.md)

---

> This is the reduced view. [reference.html](./reference.html) is the full, authoritative reference, with the diagrams drawn.

speccen puts questions, stops and reviews to the Architect. Before this change, these messages named items by label only: `DD-19`, `01/7`, row 16. The Architect had to open other files to know what a label meant. Now every item put to the Architect has a subject: the number, a bar, and the item in plain words. A second change narrows stop condition 5: a fix that only repairs a record no longer stops an autonomous run. The change is prose in five files. No code runs.

- **20/20** — text checks T-1 – T-20 pass at `dcccc2b`
- **19/20** — checks fail on the text before the change (`67c6ad8`), as they must
- **5** — files changed, 71 lines added, 31 removed
- **28** — delegated decisions, all ADOPTED by the Architect
- **0** — deviations from the plan
- **dcccc2b** — implementation commit

<a id="system"></a>
## 1 · The system — Where the change lives

speccen is a plugin of skills. A skill is a text file. The host, Claude Code, reads the skills and runs the workflow. The workflow has phases. In `autonomous` mode, a delegate decides for the Architect, and stops when its recorded basis does not decide.

The workflow gives numbers to its items. A delegated decision is `DD-<n>`. An interview question is `01/<n>`. A gate-check row has a row number. The numbers make the decision tree traceable across `log.md`, the delegated decisions and the review.

The evidence for issue 26 is a stop round of an earlier bundle. The round named items by number only. The Architect answered: "do you really think a human knows what these numbers mean?" The numbers stay. The change puts the words next to them.

> **Diagram.** Level 1, context. The host (Claude Code) reads the speccen plugin (changed: the subject rule and the narrowed stop condition 5). The host sends questions, stops and the review round to the Architect, each item with a [number | text] subject. The Architect answers by number. The host writes stop records into the bundle; the Architect reads the stop record later.
>
> L1 — **Context.** The plugin changed. The host and the bundle did not. The accent arrows carry subjects: the messages to the Architect, and the records the Architect reads later.

<a id="files"></a>
## 2 · The five files — The parts the change touched

The governing skill holds the rule, once. The rule is the last paragraph of its section "Structured questions". The other four files point to the rule. They do not restate it.

Other skills put items to the Architect through the interview round. Phase 03 asks its ADR questions as a round. Phase 06 asks its graduation question as a round. The audit and code-documentation skills use the same round. These skills get the rule through the round template, so their text does not change.

> **Diagram.** Level 2, files. The governing skill (changed, +44 −16) holds the subject rule and the narrowed stop condition 5. Four files (changed) point to the rule: interview (+10 −6), 05-implementation (+5 −2), reconcile (+5 −3), README.md (+7 −4). Unchanged: 03-compliance-review and 06-close-out use the interview round; the audit and code skills use the interview round; ARCHITECTURE.md stays unchanged (DD-27).
>
> L2 — **Files.** Five files changed (accent). Each of the four lower files points up to the rule. The muted skills use the interview round template (dashed) and get the rule from it.

<a id="places"></a>
## 3 · Where items reach the Architect — Twenty places, three outcomes

Phase 02 searched the plugin for every place that puts an item to the Architect. It found twenty places, A-1 to A-20. Phase 03 decided each one. Eleven places now point to the rule. Five places get the rule through the round template. Four places stay outside the rule: two are records, and two name no item.

The gate test also changed. Its stop condition 5 sits in the governing skill. It is not one of the twenty places, because it does not put an item to the Architect. It decides when the delegate stops.

> **Diagram.** Level 3, places. Governing skill: the Subjects rule (changed); A-3 stop record, A-5 end-of-run report, A-6 self-check item 6, A-7 proceed open item, A-8 resume summary, A-18 STATE.md stop line (changed); A-4 stop round (inherits through the round template); A-20 fix-attempt log line (outside: a record); stop condition 5 (changed: narrowed). Interview: A-1 round template, A-2 review round, A-16 closing summary (changed). 05-implementation: A-17 completion notice (changed); A-11 deviation notice (outside: names no item). Reconcile: A-19 needs-human items (changed). Other skills: A-9 Phase 06 graduation, A-10 Phase 03 ADR interview, A-13 audit scorecard, A-14 code-documentation (inherit); A-12 phase-end notices (outside: names no item); A-15 Retrospective delegation findings (outside: a record).
>
> L3 — **Places.** Every place that puts an item to the Architect, grouped by file. Accent: the text changed. White: the place uses the round template (A-1), so the rule reaches it without a change. Muted: the rule does not apply.

<a id="contracts"></a>
## 4 · Contracts — No service contract, no component API

The change has no business service contract and no component API. The five files are prose that an AI host reads. The contract of the change is a writing rule: the subject form. Section 6 gives its exact text.

<a id="run"></a>
## 5 · One stop round — A stop, from the failing row to the answer

This run is from this bundle. In Phase 03, on 2026-11-13 at 07:41, verifier run 2 failed rows 7, 16 and 17. Breaches that run 1 named were still there. The run made no progress, so stop condition 5 stopped it. The delegate wrote the stop line, the stop record and the stop round. Each one named its items with subjects.

> **Diagram.** Level 4, one stop round. 1. The delegate asks the verifier to re-check rows 7, 16 and 17 (run 2). 2. The verifier returns: rows 7, 16 and 17 fail. 3. The delegate finds no progress and stops (stop condition 5). 4. The delegate writes the STATE.md stop line, with subjects (changed). 5. The delegate writes the stop record in summary.md: question, options, lean, evidence, with subjects (changed). 6. The delegate sends the stop round in one message: [03/22 | May the delegate repair rows 7, 16 and 17 with record-only fixes, within the phase's fix budget, stopping only on a fix that changes what a decision decides?] and [03/23 | For the rest of this run, does an answered stop allow the phase's full fix budget again, unless the answer says otherwise?] (changed). 7. The Architect answers yes. 8. The delegate makes fix attempt 1 of 5, a record-only repair.
>
> L4 — **One stop round.** Solid arrows are calls; dashed arrows are returns. The accent steps 4 – 6 are what changed: each item the Architect reads has its subject. The subjects in step 6 are cut short here; the record holds them in full.

<a id="rule"></a>
## 6 · The rule, as written — The text the delegate follows

The rule is the last paragraph of "Structured questions" in the governing skill. It comes after "A series of decisions". This is the full text at `dcccc2b`:

```markdown
**Subjects: `[INTERNAL-NUMBER | HUMAN UNDERSTANDABLE TEXT]`.** Anything put to the Architect —
an interview round, a stop, the review round, the end-of-run report — reads on its own. Give
every question, decision, checklist row or open item it mentions a subject in this form, for
example `[01/7 | Which queue carries the retry?]` or `[DD-4 | Does the fix budget also cover
Phase 05's own fix rule?]`. The number (`DD-<n>`, `01/<n>`, `<skill>/<n>`, `Deviation [N]`,
`O-<n>`, `H-<n>`, `P02-<n>`, a gate-check row, or any number a bundle gives its items) keeps it
traceable; the text says what it is, so the Architect can answer without opening another file.
A label never stands alone.
- In an `AskUserQuestion` call, question text that names an item gives it a subject; the
  header is exempt.
- Inside a markdown table, write the subject's bar as `\|`.
- Records are not questions and keep their form: the gate-check, delegated-decision and
  interview tables, the Retrospective's delegation findings, and the fix-attempt log line.
```

The number leads. The Architect answers by number, for example "22 yes". The text follows the bar. The text says what the item is, as a plain question or a short statement.

A markdown table uses the bar as a cell border. In a table cell, the subject's bar takes a backslash in front of it. The rendered table then shows a plain bar.

<a id="why"></a>
## 7 · What changed, and why — Each change, with an honest verdict

A verdict of *required* means the issue or a Phase 03 decision needs the change. *required for correctness* means another text would contradict the rule without it. *placement choice* means the change could live elsewhere.

| Where | Change | Verdict | Source |
|---|---|---|---|
| `00-governing-workflow` → Structured questions | The Subjects rule, stated once, with the label list and three bullets | *required* | brief §2.1; 03/2; DD-10, DD-18, DD-20 |
| `00-governing-workflow` → resume summary, `STATE.md` stop line, stop record, `stops: proceed` open item, end-of-run report | Each place points to the rule | *required* | brief §2.4, §2.5; 03/5, 03/17, 03/20; DD-13, DD-21, DD-24 |
| `00-governing-workflow` → gate-test self-check | "five" becomes "six"; item 6 is **Subjects** | *required* | brief §2.6; 03/4; DD-12 |
| `00-governing-workflow` → gate test trigger 1, stop condition 5, config comment | A fix stops only if it changes a conclusion, an ADR or what a delegated decision decides; the record-repair paragraph | *placement choice* | the Architect, log 2026-11-13 07:32 and 07:33; 03/16, 03/24 |
| `interview` | Round template `[01/7 \| The decision, as a plain question]`; a Subject format bullet; review round `[DD-<n> \| what was decided]`; closing summary with subjects | *required* | brief §2.2, §2.3; 03/9, 03/18; DD-22 |
| `05-implementation` | Waived-test template `[T-<n> \| what the test checks]`; the accept rule narrowed like trigger 1 | *required for correctness* | 03/19; DD-23; R-16 |
| `reconcile` | Needs-human items and the notice name each item with a subject | *required* | 03/6; DD-14 |
| `README.md` | The autonomous section names the subject form in the stop round and the review round; the config comment matches the governing skill | *required for correctness* | 03/14, 03/15; DD-26, DD-27 |

The narrowed stop condition 5 is a placement choice. It is a separate change from the subject rule. The Architect asked for it during this run, and asked to put it in this bundle. It could be its own issue.

### Rejected alternatives

| Alternative | Why it was not taken | Source |
|---|---|---|
| Drop the labels | The labels make the decision tree traceable across `log.md`, the delegated decisions and the review. The Retrospective uses them. | brief §4 |
| A glossary of labels | The Architect still opens another place before answering. | brief §4 |
| Plain words, with the number as a trailing pointer | The Architect answers by number. The number must lead, next to its text. | brief §4 |
| Fix it in chat only | The Architect answers from the stop record in `summary.md` later. The record must read on its own too. | brief §4 |
| Repeat the rule at each place | Copies drift. One rule with pointers keeps one text to change. | 03/2; DD-10 |
| Put subjects in the record tables too | A table row already holds the item's text in its own columns. | 03/3; DD-11 |
| Put subjects in the fix-attempt log line | The line is a record. The stop round that quotes its rows gives them subjects. | 03/21; DD-25 |
| Keep trigger 1 as "a delegated decision" | Every record repair touched a delegated decision, so every repair stopped the run. The Architect answered "yes" to each such stop. | the Architect, log 2026-11-13 07:32 |

<a id="repair"></a>
## 8 · Record repair or changed answer — The one point that decides a stop

Trigger 1 of the gate test stops the run when the next fix changes a decision. Before this change, the text said "a delegated decision". A fix that only split a question touched a delegated decision, so it stopped the run. Now the text says "what a delegated decision decides". The test is the answer: if the answer stays the same, the fix is a record repair, and the run continues.

> **Diagram.** Argument diagram. The verifier fails a row and the delegate plans the next fix. Question: does the next fix change a conclusion, an ADR, or what a delegated decision decides? No: a record repair. Example from this bundle: split 03/16 into 03/16 and 03/24 with the same answer each; raise DD-19 to MATERIAL — unconfirmed with its answer unchanged. Result: continue; the fix counts as one fix attempt and is logged; the review round still puts every entry to the Architect. Yes: a changed answer. Example (no such fix ran): change what DD-19 decides, from README.md mentions the subject form to it does not. Result: stop, stop condition 5, trigger 1; the Architect answers in a stop round.
>
> **Argument diagram.** Both fixes touch DD-19. Only the right one changes its answer. Before the change, both fixes stopped the run. Now only the right one does.

The skill lists the record repairs: split a question into one per decision with the same answer each; move a question to the round its dependencies allow; correct a citation; raise a decision's materiality to `MATERIAL — unconfirmed`. Each new or changed entry keeps the decision's answer and states the repair in a Repair row. The review round still puts every entry to the Architect. Conditions 2 to 8 stay hard stops.

<a id="decisions"></a>
## 9 · Delegated decisions — Twenty-eight decisions, all adopted

The run was `autonomous` with `stops: proceed`. The delegate took 28 decisions and recorded each one. Fifteen were material. The Architect reviewed all 28 in the review round on 2026-11-15 and answered "yes" to each. Every status is ADOPTED. The full record is in [delegated-decisions.md](../../bundles/2026-11-13.questions_to_the_architect_number_text_subjects_never_a_bare_label/delegated-decisions.md).

| Decision | Phase | Materiality | Status |
|---|---|---|---|
| [DD-1](../../bundles/2026-11-13.questions_to_the_architect_number_text_subjects_never_a_bare_label/delegated-decisions.md#dd-1) — Issue #26 counts as the Architect's own words | Feature Analysis | *not material* | *ADOPTED* |
| [DD-2](../../bundles/2026-11-13.questions_to_the_architect_number_text_subjects_never_a_bare_label/delegated-decisions.md#dd-2) — Target: the plugin source in this repository | Feature Analysis | *not material* | *ADOPTED* |
| [DD-3](../../bundles/2026-11-13.questions_to_the_architect_number_text_subjects_never_a_bare_label/delegated-decisions.md#dd-3) — The rule's reach: every place, as a working hypothesis | Feature Analysis | *not material* | *ADOPTED* |
| [DD-4](../../bundles/2026-11-13.questions_to_the_architect_number_text_subjects_never_a_bare_label/delegated-decisions.md#dd-4) — The §5 proposals are the starting proposal for Phase 03 | Feature Analysis | *not material* | *ADOPTED* |
| [DD-5](../../bundles/2026-11-13.questions_to_the_architect_number_text_subjects_never_a_bare_label/delegated-decisions.md#dd-5) — Earlier bundles and the durable store are not rewritten | Feature Analysis | *not material* | *ADOPTED* |
| [DD-6](../../bundles/2026-11-13.questions_to_the_architect_number_text_subjects_never_a_bare_label/delegated-decisions.md#dd-6) — This bundle already uses the subject form | Feature Analysis | *not material* | *ADOPTED* |
| [DD-7](../../bundles/2026-11-13.questions_to_the_architect_number_text_subjects_never_a_bare_label/delegated-decisions.md#dd-7) — `AskUserQuestion`: question text covered, headers exempt, as a working hypothesis | Feature Analysis | *not material* | *ADOPTED* |
| [DD-8](../../bundles/2026-11-13.questions_to_the_architect_number_text_subjects_never_a_bare_label/delegated-decisions.md#dd-8) — Done when, as a working hypothesis | Feature Analysis | *not material* | *ADOPTED* |
| [DD-9](../../bundles/2026-11-13.questions_to_the_architect_number_text_subjects_never_a_bare_label/delegated-decisions.md#dd-9) — Kind of request confirmed: feature | Compliance & Review | *not material* | *ADOPTED* |
| [DD-10](../../bundles/2026-11-13.questions_to_the_architect_number_text_subjects_never_a_bare_label/delegated-decisions.md#dd-10) — The rule is stated once and pointed to | Compliance & Review | *material* | *ADOPTED* |
| [DD-11](../../bundles/2026-11-13.questions_to_the_architect_number_text_subjects_never_a_bare_label/delegated-decisions.md#dd-11) — Record tables stay outside the rule | Compliance & Review | *material* | *ADOPTED* |
| [DD-12](../../bundles/2026-11-13.questions_to_the_architect_number_text_subjects_never_a_bare_label/delegated-decisions.md#dd-12) — A sixth self-check item: Subjects | Compliance & Review | *material* | *ADOPTED* |
| [DD-13](../../bundles/2026-11-13.questions_to_the_architect_number_text_subjects_never_a_bare_label/delegated-decisions.md#dd-13) — The `stops: proceed` open item points to the rule | Compliance & Review | *material* | *ADOPTED* |
| [DD-14](../../bundles/2026-11-13.questions_to_the_architect_number_text_subjects_never_a_bare_label/delegated-decisions.md#dd-14) — The reconcile report's questions follow the rule | Compliance & Review | *material* | *ADOPTED* |
| [DD-15](../../bundles/2026-11-13.questions_to_the_architect_number_text_subjects_never_a_bare_label/delegated-decisions.md#dd-15) — Retrospective findings stay outside | Compliance & Review | *material* | *ADOPTED* |
| [DD-16](../../bundles/2026-11-13.questions_to_the_architect_number_text_subjects_never_a_bare_label/delegated-decisions.md#dd-16) — `AskUserQuestion`: question text covered, header exempt | Compliance & Review | *material* | *ADOPTED* |
| [DD-17](../../bundles/2026-11-13.questions_to_the_architect_number_text_subjects_never_a_bare_label/delegated-decisions.md#dd-17) — Audit and code interviews inherit the rule | Compliance & Review | *material* | *ADOPTED* |
| [DD-18](../../bundles/2026-11-13.questions_to_the_architect_number_text_subjects_never_a_bare_label/delegated-decisions.md#dd-18) — The rule goes at the end of Structured questions | Compliance & Review | *not material* | *ADOPTED* |
| [DD-19](../../bundles/2026-11-13.questions_to_the_architect_number_text_subjects_never_a_bare_label/delegated-decisions.md#dd-19) — `README.md` mentions the subject form; `ARCHITECTURE.md` unchanged | Compliance & Review | *material* | *ADOPTED* |
| [DD-20](../../bundles/2026-11-13.questions_to_the_architect_number_text_subjects_never_a_bare_label/delegated-decisions.md#dd-20) — The label list adds `<skill>/<n>` and `Deviation [N]` | Compliance & Review | *not material* | *ADOPTED* |
| [DD-21](../../bundles/2026-11-13.questions_to_the_architect_number_text_subjects_never_a_bare_label/delegated-decisions.md#dd-21) — The resume summary points to the rule | Compliance & Review | *material* | *ADOPTED* |
| [DD-22](../../bundles/2026-11-13.questions_to_the_architect_number_text_subjects_never_a_bare_label/delegated-decisions.md#dd-22) — The interview's closing summary points to the rule | Compliance & Review | *material* | *ADOPTED* |
| [DD-23](../../bundles/2026-11-13.questions_to_the_architect_number_text_subjects_never_a_bare_label/delegated-decisions.md#dd-23) — The Phase 05 completion notice points to the rule | Compliance & Review | *material* | *ADOPTED* |
| [DD-24](../../bundles/2026-11-13.questions_to_the_architect_number_text_subjects_never_a_bare_label/delegated-decisions.md#dd-24) — The `STATE.md` stop line points to the rule | Compliance & Review | *material* | *ADOPTED* |
| [DD-25](../../bundles/2026-11-13.questions_to_the_architect_number_text_subjects_never_a_bare_label/delegated-decisions.md#dd-25) — The fix-attempt log line stays outside | Compliance & Review | *material* | *ADOPTED* |
| [DD-26](../../bundles/2026-11-13.questions_to_the_architect_number_text_subjects_never_a_bare_label/delegated-decisions.md#dd-26) — `README.md` mentions the subject form | Compliance & Review | *material* | *ADOPTED* |
| [DD-27](../../bundles/2026-11-13.questions_to_the_architect_number_text_subjects_never_a_bare_label/delegated-decisions.md#dd-27) — `ARCHITECTURE.md` stays unchanged | Compliance & Review | *not material* | *ADOPTED* |
| [DD-28](../../bundles/2026-11-13.questions_to_the_architect_number_text_subjects_never_a_bare_label/delegated-decisions.md#dd-28) — Skill-text changes stay uncommitted for the Architect | Specification | *not material* | *ADOPTED* |

DD-19 held two decisions. Phase 03 replaced it with DD-26 and DD-27 and kept its entry as recorded. DD-28 kept the skill-text changes uncommitted for the Architect. After the review, the Architect committed them at close-out, in `dcccc2b`.

Two decisions graduated to the durable store: [labels travel inside subjects](../../decisions/2026-11-15.labels_travel_inside_subjects.md) and [a record repair is not a stop](../../decisions/2026-11-15.record_repair_is_not_a_stop.md).

<a id="testing"></a>
## 10 · Testing — Twenty text checks, and a control run

The change is prose, so there are no unit tests. A script, [phase-05-text-checks.py](../../bundles/2026-11-13.questions_to_the_architect_number_text_subjects_never_a_bare_label/files/phase-05-text-checks.py), reads the five files and checks the exact text in the right section. It compares unchanged passages and the list of changed files with `67c6ad8`, the last commit before the change.

All 20 checks pass at `dcccc2b`. On the text at `67c6ad8`, 19 checks fail. T-19 passes there, because it checks passages that must not change.

| Check | What it checks | Requirement |
|---|---|---|
| T-1 | The rule is at the end of Structured questions, after "A series of decisions", with both examples and the full label list | R-1 |
| T-2 | The three bullets: the `AskUserQuestion` header, the escaped bar in tables, the records | R-1, R-2, R-3 |
| T-3 | The rule is defined once in all skills | R-1 |
| T-4 | The round template uses subjects; "[Short title]" is gone; the Subject format bullet follows "One decision per question" | R-4 |
| T-5 | The review round names each decision as `[DD-<n> \| what was decided]` | R-5 |
| T-6 | The stop record gives every item a subject | R-6 |
| T-7 | The end-of-run report uses subjects | R-7 |
| T-8 | The self-check has six items; item 6 is Subjects | R-8 |
| T-9 | The `stops: proceed` open item has a subject | R-9 |
| T-10 | The resume summary names each item with a subject | R-10 |
| T-11 | The interview closing summary uses subjects | R-11 |
| T-12 | The waived-test notice uses `[T-<n> \| what the test checks]` | R-12 |
| T-13 | The `STATE.md` stop line gives a named item its subject | R-13 |
| T-14 | The reconcile report and notice use subjects | R-14 |
| T-15 | `README.md` names the form; `ARCHITECTURE.md` has no change | R-15 |
| T-16 | Trigger 1 is narrowed; the record-repair paragraph comes before the log line | R-16 |
| T-17 | Stop condition 5 and the Phase 05 accept rule are narrowed the same way | R-16 |
| T-18 | The config comment is the same in the governing skill and `README.md` | R-16 |
| T-19 | Unchanged passages: the tool constraints, the interview numbering, the log line, conditions 2 to 8 | R-2, R-17 |
| T-20 | Only the five files changed | R-4, R-17 |

Each autonomous phase also passed its gate test. The verifier subagent re-checked every row. Phase 04 used 5 of its 5 fix attempts, with progress at each run. Phase 05 used 1 of 5.

<a id="limits"></a>
## 11 · Known limits — What the change does not do

- **No move test.** The text checks find exact sentences inside a section. A check does not prove that a sentence fails when it moves to a wrong place inside that section. The store lesson [text checks read their place](../../lessons/2026-11-11.text_checks_read_their_place.md) asks for a move test. This run did not make one.
- **A prose rule.** No code enforces the rule. Self-check item 6 and the verifier check it at each gate test. Between gate tests, the delegate follows it as text.
- **Old bundles keep bare labels.** Earlier bundles and the durable store are not rewritten (DD-5).
- **Headers stay short.** An `AskUserQuestion` header holds at most 12 characters, so it is exempt (DD-16). The question text carries the subject.
- **Records keep their form.** The record tables, the Retrospective's delegation findings and the fix-attempt log line keep bare labels (DD-11, DD-15, DD-25).

<a id="sources"></a>
## 12 · Sources — Source map

Line numbers are at `dcccc2b`.

| Place | What is there |
|---|---|
| `skills/sdd/00-governing-workflow/SKILL.md:403-415` | The Subjects rule |
| `skills/sdd/00-governing-workflow/SKILL.md:554` | Resume summary pointer |
| `skills/sdd/00-governing-workflow/SKILL.md:765` | Config template comment |
| `skills/sdd/00-governing-workflow/SKILL.md:1198-1208` | Self-check, six items; item 6 Subjects |
| `skills/sdd/00-governing-workflow/SKILL.md:1222-1233` | Trigger 1 and the record-repair paragraph |
| `skills/sdd/00-governing-workflow/SKILL.md:1269` | Stop condition 5 |
| `skills/sdd/00-governing-workflow/SKILL.md:1284-1288` | `STATE.md` stop line and stop record |
| `skills/sdd/00-governing-workflow/SKILL.md:1307-1309` | `stops: proceed` open item; conditions 2 to 8 |
| `skills/sdd/00-governing-workflow/SKILL.md:1365` | End-of-run report |
| `skills/sdd/interview/SKILL.md:88-97` | Round template and the Subject format bullet |
| `skills/sdd/interview/SKILL.md:160`, `:178` | Review round; closing summary |
| `skills/sdd/05-implementation/SKILL.md:293`, `:327` | Waived-test notice; accept rule |
| `skills/sdd/reconcile/SKILL.md:158`, `:176` | Needs-human items; the notice |
| `README.md:220`, `:232`, `:256` | Stop round; review round; config comment |

Bundle basis: [the brief (issue 26)](../../bundles/2026-11-13.questions_to_the_architect_number_text_subjects_never_a_bare_label/files/gh-26-questions-subjects.md), [Phase 01](../../bundles/2026-11-13.questions_to_the_architect_number_text_subjects_never_a_bare_label/phase-01-feature-analysis/phase.md), [Phase 02](../../bundles/2026-11-13.questions_to_the_architect_number_text_subjects_never_a_bare_label/phase-02-code-analysis/phase.md) (the inventory A-1 to A-20), [Phase 03](../../bundles/2026-11-13.questions_to_the_architect_number_text_subjects_never_a_bare_label/phase-03-compliance-review/phase.md) (the decisions), [Phase 04](../../bundles/2026-11-13.questions_to_the_architect_number_text_subjects_never_a_bare_label/phase-04-specification/phase.md) (the plan, R-1 to R-17, T-1 to T-20), [Phase 05](../../bundles/2026-11-13.questions_to_the_architect_number_text_subjects_never_a_bare_label/phase-05-implementation/phase.md), [the technical close-out](../../bundles/2026-11-13.questions_to_the_architect_number_text_subjects_never_a_bare_label/phase-06-close-out/doc-technical.md), [the delegated decisions](../../bundles/2026-11-13.questions_to_the_architect_number_text_subjects_never_a_bare_label/delegated-decisions.md), [the log](../../bundles/2026-11-13.questions_to_the_architect_number_text_subjects_never_a_bare_label/log.md). The bundle has no ADR of its own; Phase 03 found seven standing decisions in the store, and the change touches none of them.

Durable store: [labels travel inside subjects](../../decisions/2026-11-15.labels_travel_inside_subjects.md), [a record repair is not a stop](../../decisions/2026-11-15.record_repair_is_not_a_stop.md), [escape the bar in table cells](../../lessons/2026-11-15.escape_bar_in_table_cells.md), [a kept breach is no progress](../../lessons/2026-11-15.kept_breach_is_no_progress.md), [a stop question proposes a fix budget](../../lessons/2026-11-15.stop_question_proposes_fix_budget.md).

Reference for bundle `2026-11-13.questions_to_the_architect_number_text_subjects_never_a_bare_label`. Intent: [specification](./specification.html). Generated from the whole bundle and the code at `dcccc2b`.
