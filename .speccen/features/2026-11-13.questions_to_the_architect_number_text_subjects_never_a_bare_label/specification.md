---
type: Specification
phase: "04 — Specification"
status: COMPLETE
description: Reduced projection of specification.html — every item put to the Architect carries a [number | text] subject; record repairs no longer stop an autonomous run
---

# Questions to the Architect: [number | text] subjects, never a bare label — Specification (reduced)

[Index](../../bundles/2026-11-13.questions_to_the_architect_number_text_subjects_never_a_bare_label/index.md) · [State](../../bundles/2026-11-13.questions_to_the_architect_number_text_subjects_never_a_bare_label/STATE.md) · [Log](../../bundles/2026-11-13.questions_to_the_architect_number_text_subjects_never_a_bare_label/log.md) · [Full specification](../../bundles/2026-11-13.questions_to_the_architect_number_text_subjects_never_a_bare_label/phase-04-specification/specification.html) · [Plan](../../bundles/2026-11-13.questions_to_the_architect_number_text_subjects_never_a_bare_label/phase-04-specification/phase.md#implementation-plan)

---

## What the update builds

speccen gives each question, decision and item a label, for example `DD-4` or `01/8`. Today a
stop round or a review round often shows the label alone. The Architect must open other files to
learn what the question is about.

The update adds one rule to the governing skill: each item that speccen puts to the Architect has
a subject `[INTERNAL-NUMBER | HUMAN UNDERSTANDABLE TEXT]`. The number keeps the item traceable.
The text tells the Architect what the item is. A label never stands alone. Each place that puts
items to the Architect points to the rule. The records in the bundle keep their form.

The Architect added a second change: a correction that only changes how a decision is recorded
is not a stop. The delegate keeps the answer, states the repair and continues.

Source: [issue #26](../../bundles/2026-11-13.questions_to_the_architect_number_text_subjects_never_a_bare_label/files/gh-26-questions-subjects.md),
[Phase 01](../../bundles/2026-11-13.questions_to_the_architect_number_text_subjects_never_a_bare_label/phase-01-feature-analysis/phase.md#feature-description),
[Phase 03 decisions](../../bundles/2026-11-13.questions_to_the_architect_number_text_subjects_never_a_bare_label/phase-03-compliance-review/phase.md#analysis-updates),
[scope addition](../../bundles/2026-11-13.questions_to_the_architect_number_text_subjects_never_a_bare_label/phase-03-compliance-review/phase.md#scope-addition).

## What exists today

The skills give each item a label, but no skill says that the label must have its text: the
interview round shows "`01/7 — [Short title]`", the review round names `DD-<n>` alone, and the
stop record asks for "the exact question, the options, your lean and the evidence". Stop
condition 5 stops on any fix that changes a delegated decision, a record repair included. Full
inventory (A-1 – A-20): [Phase 02](../../bundles/2026-11-13.questions_to_the_architect_number_text_subjects_never_a_bare_label/phase-02-code-analysis/phase.md#code-analysis).

## The files that change

| File | What changes |
|---|---|
| `skills/sdd/00-governing-workflow/SKILL.md` | The Subjects rule; pointers in the resume summary, the stop record, the `STATE.md` stop line, the `stops: proceed` open item and the end-of-run report; a sixth self-check item; the narrowed stop trigger, stop condition 5 and the config comment |
| `skills/sdd/interview/SKILL.md` | The round template, the review round, the closing summary |
| `skills/sdd/05-implementation/SKILL.md` | The completion notice; the accept trigger |
| `skills/sdd/reconcile/SKILL.md` | "Needs human resolution" items and the notice |
| `README.md` | The autonomous-mode section; the template comment |

`ARCHITECTURE.md` does not change.

## Decisions and constraints

No bundle ADR. Seven standing decisions checked, no conflict
([Phase 03](../../bundles/2026-11-13.questions_to_the_architect_number_text_subjects_never_a_bare_label/phase-03-compliance-review/phase.md#adrs)). Fourteen material answers wait for the
Architect in the review round ([O-8](../../bundles/2026-11-13.questions_to_the_architect_number_text_subjects_never_a_bare_label/phase-03-compliance-review/phase.md#open-items)).

## Requirements & acceptance scenarios

| Id | Requirement (SHALL) | Scenario (WHEN → THEN) | Source |
|---|---|---|---|
| R-1 | **Requirement: The rule, stated once.** The governing skill SHALL state once, at the end of Structured questions, that anything put to the Architect reads on its own: every question, decision, checklist row or open item it mentions has a `[INTERNAL-NUMBER \| HUMAN UNDERSTANDABLE TEXT]` subject, for every label kind including numbers a bundle invents; in a table the bar is escaped with a backslash. | **Scenario: A label in a stop round.** WHEN a stop round names DD-4 → THEN it reads `[DD-4 \| Does the fix budget also cover Phase 05's own fix rule?]`, never `DD-4` alone. **Scenario: A subject in a table.** WHEN the subject sits in a table cell → THEN its bar is escaped and the table renders. | brief §2, §2.1; 03/2, 03/10, 03/12 (DD-10, DD-18, DD-20); Phase 03 domain note |
| R-2 | **Requirement: Records keep their form.** The rule SHALL cover only what is put to the Architect; the gate-check, delegated-decision and interview tables, the Retrospective's delegation findings and the fix-attempt log line SHALL keep their form. | **Scenario: Gate-check rows.** WHEN a gate check is written → THEN its rows keep their numbers and form. **Scenario: Fix-attempt line.** WHEN a fix attempt is logged → THEN the line is `fix attempt <n> of <fixes>: run <N> failed rows <list>`. | brief §3, §5.2; 03/3, 03/7, 03/21 (DD-11, DD-15, DD-25) |
| R-3 | **Requirement: Tool questions.** In an `AskUserQuestion` call, question text that names an item SHALL give it a subject; the header SHALL be exempt. | **Scenario: A tool question names an item.** WHEN a tool question names O-3 → THEN its text carries `[O-3 \| …]`, and its header stays ≤ 12 characters. | 03/8 (DD-16) |
| R-4 | **Requirement: Round template.** The interview round template SHALL write each question as `[01/7 \| the decision, as a plain question]` and SHALL point to the rule for every item a question mentions; the stop round, the ADR and graduation interviews and the interviews outside a bundle SHALL follow it through the template. | **Scenario: A Phase 01 round.** WHEN a Phase 01 round is written → THEN each question leads with `[01/<n> \| …]`. **Scenario: An audit interview.** WHEN an audit interview is written → THEN it uses the same form without a pointer of its own. | brief §2.2; 03/9 (DD-17); Phase 02, A-4, A-9, A-10, A-13, A-14 |
| R-5 | **Requirement: Review round.** The review round SHALL put each delegated decision as `[DD-<n> \| what was decided]`, then why, with `adopt`, `override` or `later`; the material ones first. | **Scenario: Material decisions first.** WHEN a run ends with DD-12 `MATERIAL — unconfirmed` → THEN the review round opens with `[DD-12 \| …]` and its proposal. | brief §2.3 |
| R-6 | **Requirement: Stop record.** The stop record in `summary.md` SHALL give every item a subject, readable without the rest of the bundle. | **Scenario: A gate stop names a row.** WHEN a gate stop names row 16 → THEN the record reads `[Row 16 \| …]`. | brief §2.4 |
| R-7 | **Requirement: End-of-run report.** The end-of-run report SHALL use subjects for the phases, gate checks, decisions, stops and graduation proposal it names. | **Scenario: The report lists a stop.** WHEN the report lists a stop → THEN the stop's question carries its text. | brief §2.5 |
| R-8 | **Requirement: Sixth self-check item.** The gate-test self-check SHALL have six items, the sixth "Subjects". | **Scenario: The self-check runs.** WHEN the delegate runs the self-check → THEN it checks that no label stands alone. **Scenario: The lead-in counts.** WHEN a reader counts the items → THEN the lead-in says six. | brief §2.6; 03/4 (DD-12) |
| R-9 | **Requirement: `stops: proceed` open item.** The `stops: proceed` open item in `summary.md` SHALL carry a subject. | **Scenario: A decision under `proceed`.** WHEN a material decision is taken under `proceed` → THEN the open item reads `[DD-<n> \| …]`. | 03/5 (DD-13) |
| R-10 | **Requirement: Resume summary.** The resume summary SHALL name each stop and candidate with a subject. | **Scenario: A stop waits at resume.** WHEN a session resumes with a stop waiting → THEN the summary names the stop's question with its text. | 03/17 (DD-21) |
| R-11 | **Requirement: Closing summary.** The interview's closing summary SHALL give each decision its subject. | **Scenario: A `gated` interview closes.** WHEN a `gated` interview closes → THEN each summarised decision reads `[<phase>/<n> \| …]`. | 03/18 (DD-22) |
| R-12 | **Requirement: Phase 05 completion notice.** The Phase 05 completion notice SHALL name each waived test with a subject. | **Scenario: A test is waived.** WHEN a test is waived → THEN the notice reads `[T-<n> \| what the test checks]`. | 03/19 (DD-23) |
| R-13 | **Requirement: `STATE.md` stop line.** The `STATE.md` stop line SHALL give any item its reason names a subject. | **Scenario: A stop reason names a row.** WHEN a stop's reason names a row → THEN the line carries the row's text. | 03/20 (DD-24) |
| R-14 | **Requirement: Reconcile report.** The reconcile report's "Needs human resolution" items and its notice SHALL carry subjects. | **Scenario: Two decisions contradict.** WHEN two decisions contradict → THEN the report reads `[id-A \| what it decides] and [id-B \| what it decides]`. | 03/6 (DD-14) |
| R-15 | **Requirement: README.** `README.md` SHALL name the subject form where its autonomous-mode section describes the stop round and the review round; `ARCHITECTURE.md` SHALL stay unchanged. | **Scenario: The autonomous section.** WHEN a reader opens the README's autonomous section → THEN it says each item is named as `[number \| text]`. | 03/14, 03/15 (DD-26, DD-27) |
| R-16 | **Requirement: Stop condition 5 narrowed.** Stop condition 5 SHALL stop on a fix that changes a phase conclusion, an ADR, or what a delegated decision decides, and SHALL NOT stop on a fix that only repairs how a decision is recorded; each such repair keeps the answer and states the repair. The gate test, stop condition 5, Phase 05 Step 7 and the config comment (with its README copy) SHALL say so. | **Scenario: A record repair continues.** WHEN the only fix splits a question in two with the same answer each → THEN the delegate fixes, states the repair and re-runs the verifier. **Scenario: A changed answer stops.** WHEN the only fix changes a DD's answer → THEN the delegate stops. | 03/16, 03/24 (the Architect, log 07:32, 07:33); Phase 03 scope addition |
| R-17 | **Requirement: Scope.** The change SHALL touch only `gov`, `int`, `p05`, `rec` and `README.md`; labels themselves and the interview's Numbering SHALL stay. | **Scenario: The files that change.** WHEN the change lands → THEN `git diff --stat` outside `.speccen/` lists those five files. | brief §3, §4 ("Drop the labels" rejected); 03/15 |

## The plan

Six implementation phases: the rule → governing pointers → interview → Phase 05 and reconcile →
stop condition 5 → README and verification. Twenty text checks (T-1 – T-20) verify the edited
text → [Test Plan](../../bundles/2026-11-13.questions_to_the_architect_number_text_subjects_never_a_bare_label/phase-04-specification/phase.md#implementation-plan).

## Not included

- The labels stay; the record tables, the Retrospective's findings and the fix-attempt log line keep their form.
- `ARCHITECTURE.md` does not change.
- The rule "an answered stop gives the full fix budget again" applied to this run only.
