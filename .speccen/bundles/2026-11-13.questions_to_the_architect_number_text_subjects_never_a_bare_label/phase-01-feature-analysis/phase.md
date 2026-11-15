---
type: Phase
phase: "01 — Feature Analysis"
status: COMPLETE
description: Make every question, decision and item that speccen puts to the Architect carry a `[number | text]` subject, so the Architect can answer without opening the bundle
---

<a id="phase-top"></a>
# Questions to the Architect: [number | text] subjects, never a bare label — Feature Analysis

[Index](../index.md) · [State](../STATE.md) · [Log](../log.md)

---

<a id="extensions"></a>
## Extensions applied

| Extension | Why | Where it applies | Outcome |
|---|---|---|---|
| — | — | — | No extensions for this phase (`.speccen/extensions/` does not exist) |

<a id="feature-description"></a>
## Request Description

The brief is GitHub issue #26, written by the Architect and copied verbatim to
[files/gh-26-questions-subjects.md](../files/gh-26-questions-subjects.md). It counts as the
Architect's own words (01/1, [DD-1](../delegated-decisions.md#dd-1)).

### Request Summary

**Kind:** feature — the Architect's session-start answer (log 06:28). It can still change in
Phase 03; nothing in the brief contradicts it.

speccen puts things to the Architect in several places: interview rounds, stop rounds, the
review round after an `autonomous` run, the end-of-run report, and the stop record in a phase
`summary.md`. In each of them the AI names questions, delegated decisions, checklist rows and
open items by their bookkeeping label alone (`DD-4`, `row 16`, `O-1`, `H-2`, `P02-3`, `01/8`).
To answer, the Architect has to open other files to find out what each label means.

The request adds one rule to the governing skill, and points to it from each place that puts
something to the Architect: **anything put to the Architect reads on its own**. Every question,
decision, checklist row or open item it mentions gets a subject of the form
`[INTERNAL-NUMBER | HUMAN UNDERSTANDABLE TEXT]` — for example
`[D-1 | What should be the button's color?]`. The number stays, so the item can still be traced.
The text says what the item is. A label never stands alone.

The brief proposes six text changes (§2.1 – §2.6):

| § | Where | Change |
|---|---|---|
| 2.1 | Governing skill → Structured questions | State the rule once, with examples and the list of label kinds |
| 2.2 | Interview → The round | The round template uses `[01/7 \| plain question]` as the subject; a new bullet requires subjects for every mentioned item |
| 2.3 | Interview → The review round | One question per delegated decision with subject `[DD-<n> \| what was decided]` |
| 2.4 | Governing skill → Stop conditions → A stop produces | The stop's open item in `summary.md` uses subjects and reads without the rest of the bundle |
| 2.5 | Governing skill → Transitions and the end of a run | The end-of-run report uses subjects |
| 2.6 | Governing skill → Gate test → Self-check | A sixth self-check item: **Subjects** |

**Done when:** open — Phase 04. Working hypothesis H-4 (01/8): the §2 changes are in the
skills, every place Phase 02 finds that puts something to the Architect follows the rule or
points to it, and the bundle's record tables are unchanged.

### Domain Context

speccen is a phase-gated, spec-driven development workflow shipped as a Claude Code plugin. Its
behaviour is defined only by the text of its skills (`skills/sdd/…`). The Architect is the sole
decision authority. In `autonomous` mode the AI acts as the Architect's delegate and records
its decisions for later review. That review, the stops and the interviews are the points where
the Architect reads what the AI put to them and answers.

The capability concerned is **communication with the Architect at decision points**. The labels
exist for traceability: they tie a question to its answer in `log.md`, to its delegated decision
and to the review, and the Retrospective (Phase 07) relies on them (brief §4). The problem is
not the labels. The problem is that the labels stand in for the words.

The brief's evidence is the Phase 01 stop round of the `set_allowed_budget_for_autonomous_phases`
bundle (2026-11-11). The Architect answered it with: "do you really think a human knows what
DD-*, P*, etc ... is?" (brief §1). The Architect then set the format
`[INTERNAL-NUMBER | HUMAN UNDERSTANDABLE TEXT]`.

<a id="known-facts"></a>
### Known Facts

From the brief and the session; none of these is a claim about the code.

- The Architect wrote issue #26 (author `petervyvey`) and chose the session-start answers
  (log 06:28).
- The format is set by the Architect: `[INTERNAL-NUMBER | HUMAN UNDERSTANDABLE TEXT]`, for
  example "[D-1 | What should be the button's color ?]" (brief §1).
- The number leads, next to the text: the Architect answers by number ("8 yes") (brief §4).
- The record in `summary.md` must read on its own too, not only the chat message: the Architect
  answers from it when they come back later (brief §1, §4).
- The brief states that bundle-internal tables (gate check, delegated decisions, interview
  tables) are records, not questions, and stay unchanged (§3); §5 still leaves this to the
  plugin Architect as decision 2 (H-2, O-2).
- Rejected: dropping the labels, a glossary of labels, the number as a trailing pointer, a
  chat-only fix (brief §4).
- Prior art in the durable store: the standing decision
  `2026-11-05.self_check_interview_structure` added the self-check item that §2.6 extends; the
  lesson `2026-11-05.readme_restates_config_template` says an edit list that changes only the
  governing skill misses the copies in `README.md` and `ARCHITECTURE.md` (→ P02-5).

### Scope

**In scope**

- The rule, stated once in the governing skill (§2.1).
- Pointers to the rule, and template changes, at: the interview round (§2.2), the review round
  (§2.3), the stop record (§2.4), the end-of-run report (§2.5) and the gate-test self-check
  (§2.6).
- Every other place in the skills that puts something to the Architect — as far as the rule
  reaches (01/3, H-1; O-1).

**Out of scope**

- The labels themselves: none is removed or renamed (brief §3, §4).
- Earlier bundles and durable-store entries: they are not rewritten (01/5,
  [DD-5](../delegated-decisions.md#dd-5)).

**Unclear — carried forward**

- [O-1 | Does the rule reach places the brief does not list?] → Phase 03, after the Phase 02
  inventory.
- [O-2 | The three decisions in brief §5: state the rule once and point to it; cover only what
  is put to the Architect, not the record tables; add a sixth self-check item for subjects.]
  Whether the record tables (gate check, delegated decisions, interview tables) stay out of the
  rule is its second decision: the brief says so (§3) but leaves it to the plugin Architect
  → Phase 03.
- [O-3 | Does the rule cover `AskUserQuestion` questions?] → Phase 03.

<a id="terminology"></a>
### Key Concepts & Terminology

| Term | As the Architect uses it |
|---|---|
| **Subject** | The `[INTERNAL-NUMBER \| HUMAN UNDERSTANDABLE TEXT]` pair that names a question, decision, row or item put to the Architect |
| **Internal number** (label) | The bookkeeping reference: `DD-<n>`, `01/<n>`, `O-<n>`, `H-<n>`, `P02-<n>`, a gate-check row |
| **Human understandable text** | The plain-words statement of what the item is — for a question, the question itself |
| **Bare label** | A label used without its text; the thing the rule forbids |
| **Put to the Architect** | Any message or record the Architect reads in order to answer or decide: an interview round, a stop, the review round, the end-of-run report, a stop's open item in `summary.md` |
| **Reads on its own** | The Architect can answer from the message or record alone, without opening another file |
| **Record tables** | Bundle-internal tables kept for traceability (gate check, delegated decisions, interview tables); not questions |
| **Stop round** | The numbered interview round a stop produces in `autonomous` mode |
| **Review round** | The interview after an `autonomous` run: one question per delegated decision and per graduation candidate |
| **End-of-run report** | The one message after Phase 06 completes under `autonomous` |
| **Self-check** | The delegate's own check of the gate-test rows before the verifier runs |
| **Plugin Architect** | The person who decides changes to speccen itself (brief §5) — here, the Architect of this bundle |

<a id="hypotheses"></a>
## Working Hypotheses

| # | Hypothesis | Confirms or refutes it | Settles in |
|---|---|---|---|
| H-1 | [H-1 \| The rule reaches every place that puts something to the Architect, not only the five places §2 changes.] The rule's own wording says "anything put to the Architect"; the pointers go where Phase 02 finds such a place. | Phase 02's inventory of those places (P02-1); then the decision in Phase 03 | Phase 03 (O-1) |
| H-2 | [H-2 \| The three §5 proposals — state the rule once; keep record tables out; add a sixth self-check item — are the proposal Phase 03 decides.] | Phase 03's decision on each | Phase 03 (O-2) |
| H-3 | [H-3 \| In an `AskUserQuestion` call the rule covers the question text that names an item; the 12-character header is a tab label and is exempt.] | Phase 02: how the skills use the tool (P02-4); Phase 03 decides | Phase 03 (O-3) |
| H-4 | [H-4 \| Done when the §2 changes are in the skills, every place found in Phase 02 follows or points to the rule, and record tables are unchanged.] | Phase 04's acceptance scenarios | Phase 04 (O-4) |

<a id="open-items"></a>
## Open Questions

| # | Open item | Settles in |
|---|---|---|
| O-1 | [O-1 \| Does the rule reach places the brief does not list — for example the Phase 06 graduation proposal, the resume summary, the `gated` phase-end notice, the audit and code skills?] (H-1) | Phase 03, on the Phase 02 inventory |
| O-2 | [O-2 \| The three decisions in brief §5: state the rule once and point to it; cover only what is put to the Architect, not the record tables; add a sixth self-check item for subjects.] (H-2) | Phase 03 |
| O-3 | [O-3 \| Does the rule cover the questions asked with the `AskUserQuestion` tool, and if so which parts?] (H-3) | Phase 03 |
| O-4 | [O-4 \| What are the acceptance scenarios — when is this done?] (H-4) | Phase 04 |
| O-5 | [O-5 \| The facts about the skills' text that Phase 02 must establish] — the five P02 items below | Phase 02 |

**For Phase 02** (facts in the code, carried by O-5):

- [P02-1 | Which places in the skills put something to the Architect, and which of them name
  items by label?] — an inventory across `skills/sdd/`, `skills/audit/`, `skills/code/`, the
  agent file and the commands.
- [P02-2 | Do the brief's line references still point at the cited text?] — §2.1 `:367`,
  §2.2 `interview :86-96`, §2.3 `:158-161`, §2.4 `:1228-1232`, §2.5 `:1305-1307`,
  §2.6 `:1158-1168`.
- [P02-3 | Where are the labels `O-<n>`, `H-<n>`, `P02-<n>` and the gate-check row numbers
  defined — in a skill, or only by habit in earlier bundles?]
- [P02-4 | Where do the skills call `AskUserQuestion`, and does any of those questions name a
  bundle item?]
- [P02-5 | Do `README.md`, `ARCHITECTURE.md` or other docs restate the round template, the review
  round, the stop record, the end-of-run report or the self-check list?] — the lesson
  `2026-11-05.readme_restates_config_template` says such copies are missed.

None of these blocks Phase 02: the brief names the files and sections to analyse.

<a id="interview"></a>
## Interview

Mode: `autonomous` (bundle config); `stops: proceed` (project config). The delegate answered
from the decision basis: the Architect's words in `log.md` (session-start answers, 06:28;
"proceed", 06:29) and the issue #26 brief, which the Architect wrote (01/1). No ADR and no
standing decision in `.speccen/decisions/` decides these questions;
`2026-11-05.self_check_interview_structure` bears on §2.6 and is prior art for Phase 03. Questions use the subject
form the brief asks for (01/6).

**Round 1**

| # | Question | Depends on | Proposed | Answer |
|---|---|---|---|---|
| 01/1 | [01/1 \| Does issue #26, which the Architect wrote, count as the Architect's own words for this bundle?] The rules accept chat prompts in `log.md`; the issue is in `files/`, referenced from log 06:30. | — | yes | delegate: yes — basis: the Architect's "yes" to the same question for issue #25 (bundle `2026-11-12.set_allowed_budget_for_autonomous_phases`, log 2026-11-11 11:52, its 01/9); session-start Name "Use issue #26 title" (log 06:28) — [DD-1](../delegated-decisions.md#dd-1) |
| 01/2 | [01/2 \| Is the text to change the plugin source in this repository, not the installed plugin copy?] | — | yes | delegate: yes, the plugin source in this repository — basis: the brief cites repository paths and lines (§1, §2); the session runs in this repository — [DD-2](../delegated-decisions.md#dd-2) |
| 01/3 | [01/3 \| Is the working hypothesis that the rule reaches every place that puts something to the Architect, not only the five places §2 changes?] Reach affects how many skill files change. | — | yes, as a working hypothesis | hypothesis: every place (H-1) — settles in Phase 03 (O-1); inventory in Phase 02 (P02-1) — [DD-3](../delegated-decisions.md#dd-3) |
| 01/4 | [01/4 \| Are the three §5 proposals the starting proposal for Phase 03?] §5 leaves them to the plugin Architect with "Proposed: yes". | — | yes, as a working hypothesis | hypothesis: yes (H-2) — settles in Phase 03 (O-2) — [DD-4](../delegated-decisions.md#dd-4) |
| 01/5 | [01/5 \| Are earlier bundles and durable-store entries left as they are, without rewriting their labels?] | — | yes | delegate: yes — basis: brief §2 changes only skill text; §3 "Traceability is unchanged: every number stays" — [DD-5](../delegated-decisions.md#dd-5) |
| 01/6 | [01/6 \| Should this bundle already write what it puts to the Architect in the `[number \| text]` form?] | — | yes | delegate: yes — basis: the Architect set the format (brief §1); presentation only — [DD-6](../delegated-decisions.md#dd-6) |

**Round 2** — the frontier after round 1: 01/7 depends on the reach (01/3); 01/8 depends on
the reach (01/3) and on the §5 proposals (01/4).

| # | Question | Depends on | Proposed | Answer |
|---|---|---|---|---|
| 01/7 | [01/7 \| Is the working hypothesis that, in an `AskUserQuestion` call, the rule covers the question text that names an item and exempts the header?] Headers are 12 characters at most, so a full subject cannot fit there. | 01/3 | yes, as a working hypothesis | hypothesis: as proposed (H-3) — settles in Phase 03 (O-3); facts → P02-4 — [DD-7](../delegated-decisions.md#dd-7) |
| 01/8 | [01/8 \| Is this done when the §2 changes are in the skills, every place Phase 02 finds follows or points to the rule, and record tables are unchanged?] | 01/3, 01/4 | yes, as a working hypothesis | hypothesis: as proposed (H-4) — settles in Phase 04 (O-4) — [DD-8](../delegated-decisions.md#dd-8) |

No question was answered "later". Every delegated decision of this phase is `not material`. The
reach of the rule (01/3) and the §5 decisions (01/4) could change the plan's scope if decided,
so Phase 01 does not decide them: they are working hypotheses H-1 and H-2, decided in Phase 03.

<a id="outcome"></a>
## Outcome

The request is a feature to the speccen skills: one rule, stated once in the governing skill,
that every question, decision, row or item put to the Architect carries a
`[INTERNAL-NUMBER | HUMAN UNDERSTANDABLE TEXT]` subject, with pointers and template changes at
the places the brief lists. Phase 02 inventories every place in the skills that puts something
to the Architect and checks the brief's references; Phase 03 decides the rule's reach and the
three §5 proposals.
