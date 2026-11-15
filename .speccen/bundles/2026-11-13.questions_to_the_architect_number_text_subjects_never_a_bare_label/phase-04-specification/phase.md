---
type: Phase
phase: "04 — Specification"
status: COMPLETE
description: Six-phase plan — the subject rule in Structured questions, its pointers in the governing, interview, Phase 05 and reconcile skills, the narrowed stop condition 5, the README, and text verification
---

<a id="phase-top"></a>
# Questions to the Architect: [number | text] subjects, never a bare label — Specification

[Index](../index.md) · [State](../STATE.md) · [Log](../log.md)

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
(DD-9 – DD-27) and the Architect's scope addition (03/16, 03/24) leave no contract, data-model,
dependency or plan-structure choice open. One non-material choice remains; the delegate answers
it from the basis.

**Round 1**

| # | Question | Depends on | Proposed | Answer |
|---|---|---|---|---|
| 04/1 | [04/1 \| Are the skill-text changes left uncommitted in the working tree for the Architect, with only the bundle files committed at each phase transition?] | — | yes | delegate: yes — basis: Phase Transition Protocol, which commits "the changed bundle files — only those"; precedent: bundle `2026-11-12.set_allowed_budget_for_autonomous_phases`, its question 04/1 (its DD-24) — [DD-28](../delegated-decisions.md#dd-28) |

No question was answered "later".

<a id="implementation-plan"></a>
## Implementation Plan

All line numbers are at commit `aae4441` (the skills and `README.md` are unchanged since
`7cfcb66`) and shift as edits land. Each checklist item names the text it changes, so it can be
found after a shift. Abbreviations: `gov` = `skills/sdd/00-governing-workflow/SKILL.md`, `int` =
`skills/sdd/interview/SKILL.md`, `p05` = `skills/sdd/05-implementation/SKILL.md`, `rec` =
`skills/sdd/reconcile/SKILL.md`; "the brief" is
[files/gh-26-questions-subjects.md](../files/gh-26-questions-subjects.md).

### Proposed Changes Summary

| File | Change | What |
|---|---|---|
| `skills/sdd/00-governing-workflow/SKILL.md` | modify | Structured questions: the subject rule after "A series of decisions" (after `:401`); resume summary (`:539-540`); config template comment (`:750`); Gate test: self-check lead-in and sixth item (`:1182`, `:1189-1190`), stop trigger 1 and the record-repair paragraph (`:1204`, before `:1209`); Stop conditions: condition 5 (`:1243-1244`), the `STATE.md` stop line (`:1258-1259`), the stop record in `summary.md` (`:1260-1261`); Proceeding on a proposal (`:1279-1280`); end-of-run report (`:1337-1339`) |
| `skills/sdd/interview/SKILL.md` | modify | The round template and its bullet (`:88-96`); the review round (`:158-159`); the closing summary (`:174`) |
| `skills/sdd/05-implementation/SKILL.md` | modify | Completion notice (`:292`); Step 7 accept trigger (`:325-326`) |
| `skills/sdd/reconcile/SKILL.md` | modify | "Needs human resolution" item (`:158`); the notice (`:174-175`) |
| `README.md` | modify | Autonomous-mode section: the stop round and the review round (`:219-221`, `:230-231`); template copy comment (`:254`) |

No file is created or deleted. No new pattern is introduced: the change follows the Phase 02
convention "rule once, point from sites" ([Phase 02 Coding
Patterns](../phase-02-code-analysis/phase.md#code-analysis)). Unchanged by decision:
`ARCHITECTURE.md` (03/15); the audit and code-documentation interviews, which inherit the round
template (03/9); the record tables, the Retrospective's delegation findings and the fix-attempt
log line (03/3, 03/7, 03/21); the stop round, the Phase 03 ADR interview and the Phase 06
graduation interview, which use the round template (Phase 02, A-4, A-9, A-10).

### Target-State Execution Flow

How an item reaches the Architect after the change. Every path that puts an item to the
Architect passes the subject rule; the gate test's stop trigger 1 lets record repairs through.

```
 ┌──────────────────────────────────────────────┐
 │ something is put to the Architect:           │
 │ interview round · stop round · stop record   │
 │ in summary.md · `stops: proceed` open item · │
 │ STATE.md stop line · review round · end-of-  │
 │ run report · resume summary · closing        │
 │ summary · Phase 05 completion notice ·       │
 │ reconcile report · AskUserQuestion text      │
 └──────────────────────┬───────────────────────┘
                        ▼
              ┌───────────────────┐        ┌───────────────────────┐
              │ is it a record?   ├─ yes ─►│ unchanged: gate check,│
              │ (table, finding,  │        │ DD and interview      │
              │ fix-attempt line) │        │ tables, findings, log │
              └─────────┬─────────┘        └───────────────────────┘
                        │ no
                        ▼
 ┌──────────────────────────────────────────────┐
 │ each question, decision, row or item named   │
 │ gets `[number | text]`  (gov Structured      │
 │ questions → Subjects; the site points to it) │
 │ table cell: `\|` · AskUserQuestion header:   │
 │ exempt                                       │
 └──────────────────────┬───────────────────────┘
                        ▼
 ┌──────────────────────────────────────────────┐
 │ the Architect answers from the message alone │
 └──────────────────────────────────────────────┘

 Gate test (autonomous), at a failing row:
              ┌───────────────────┐        ┌───────────────────────┐
              │ next fix changes  ├─ yes ─►│ STOP (condition 5)    │
              │ a conclusion, an  │        └───────────────────────┘
              │ ADR, or what a DD │
              │ decides?          │
              └─────────┬─────────┘
                        │ no — incl. a record repair: split a question,
                        │ move it to its round, correct a citation,
                        │ raise materiality; the answer is kept and
                        ▼ the repair stated
              ┌───────────────────┐        ┌───────────────────────┐
              │ budget used up or ├─ yes ─►│ STOP (condition 5);   │
              │ no progress?      │        │ Phase 05: reject→05b  │
              └─────────┬─────────┘        └───────────────────────┘
                        │ no
                        ▼
              ┌───────────────────┐
              │ fix; log "fix     │
              │ attempt n of N"   │──► verifier run N+1
              └───────────────────┘
```

What changed relative to the current state: every path now ends in a message whose items carry
their text, and the self-check has a sixth item that checks it; a record-only repair no longer
counts as a change to a delegated decision. Compare the
[current-state flow](../phase-02-code-analysis/phase.md#code-analysis).

### Strategy Evaluation

One approach remains after Phase 03: the brief's §2 change, as refined by DD-9 – DD-27, plus the
Architect's scope addition (03/16, 03/24). No prototype ran, so no strategy table is needed.

### Implementation Phases

#### Phase 1: The rule — governing skill, Structured questions ✅

**Why:** Every pointer in later phases names this rule, so it comes first. It is stated once, at
the end of Structured questions, because it governs both the tool and the interview — source:
brief §2.1; 03/2 ([DD-10](../delegated-decisions.md#dd-10)), 03/10 ([DD-18](../delegated-decisions.md#dd-18)).

##### 1.1 Add the Subjects paragraph after "A series of decisions" (after `gov :401`, before `---`)
**Why:** the paragraph also carries 03/12, 03/8, 03/3, 03/7, 03/21 (DD-20, DD-16, DD-11, DD-15, DD-25), the Phase 02 finding on bundle-invented numbers and the Phase 03 escape note.
- [x] Insert, as a new paragraph:

  ```
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

##### 1.2 Build and Validate
- [x] Re-read Structured questions: the paragraph follows "A series of decisions" and precedes the
  section's `---`; the tool's constraints above it are unchanged.

#### Phase 2: Pointers in the governing skill ✅

**Why:** The governing skill writes the stop, the `stops: proceed` record, the resume summary and
the end-of-run report, so each must point to the rule; the self-check enforces it — source:
brief §2.4 – §2.6; 03/4 (DD-12), 03/5 (DD-13), 03/17 (DD-21), 03/20 (DD-24).

##### 2.1 Stop record in `summary.md` (`gov :1260-1261`, brief §2.4)
- [x] After "an open item with the exact question, the options, your lean and the evidence"
  add " — every item with a `[number | text]` subject, readable without the rest of the bundle
  (Structured questions)".

##### 2.2 `STATE.md` stop line (`gov :1258-1259`, 03/20)
- [x] After "`Stopped (autonomous) — <one-line reason>`" add ", where an item the reason names
  has its `[number | text]` subject".

##### 2.3 `stops: proceed` open item (`gov :1279-1280`, 03/5)
- [x] Change "and in the phase `summary.md` under its open items." to "and in the phase
  `summary.md` under its open items, with a `[number | text]` subject (Structured questions)."

##### 2.4 Resume summary (`gov :539-540`, 03/17)
- [x] Change "any stop awaiting the Architect, and any pending graduation proposal" to "any stop
  awaiting the Architect, and any pending graduation proposal — each named with a
  `[number | text]` subject (Structured questions)".

##### 2.5 End-of-run report (`gov :1337-1339`, brief §2.5)
- [x] Change "Then report to the Architect in one message: the phases run," to "Then report to
  the Architect in one message, with `[number | text]` subjects (Structured questions): the phases
  run,"; rewrap the paragraph to ≤ 100 columns.

##### 2.6 Self-check (`gov :1182`, `:1189-1190`, brief §2.6, 03/4)
**Why:** the lead-in counts the items, so "five" becomes "six" with the new item — source: Phase 02, A-6.
- [x] Change "for the five common failures" to "for the six common failures".
- [x] After item 5 add the brief's two lines:

  ```
    6. **Subjects** — every question and item put to the Architect has a `[number | text]`
       subject; no label stands alone.
  ```

##### 2.7 Build and Validate
- [x] Re-read each changed passage in context; list numbering of the self-check runs 1 – 6.

#### Phase 3: The interview skill ✅

**Why:** The round template is the shape of every interview, stop round and graduation question,
so its change reaches them all; the review round and the closing summary are its other
Architect-facing outputs — source: brief §2.2, §2.3; Phase 02, A-4, A-9 (the stop round and the
graduation question use the round template); 03/9 (DD-17), 03/18 (DD-22).

##### 3.1 Round template (`int :88-96`, brief §2.2)
- [x] Replace "**01/7 — [Short title]** — [The question: one decision, stated plainly, with one
  line on why it matters. Name the options if there are any.]" with "**[01/7 | The decision, as
  a plain question]** — [One line on why it matters. Name the options if there are any.]".
- [x] Replace "**01/8 — [Short title]** — [...]" with "**[01/8 | …]** — [...]".
- [x] After the bullet "**One decision per question**, …" add: "- **Subject format** (governing
  skill → Structured questions): `[01/7 | …]`; any decision, item or row the question mentions
  gets its own `[number | text]` subject."

##### 3.2 Review round (`int :158-159`, brief §2.3)
- [x] Replace "- **One question per delegated decision** (`DD-<n>`): `adopt`, `override` or
  `later`, with your proposed answer. Put the `MATERIAL — unconfirmed` decisions first." with the
  brief's text: "- **One question per delegated decision**, with the subject `[DD-<n> | what was
  decided]`, then why, and `adopt`, `override` or `later`, with your proposed answer. Put the
  `MATERIAL — unconfirmed` decisions first."

##### 3.3 Closing summary (`int :174`, 03/18)
- [x] Change "Give a short closing summary of the decisions — in the Architect's words where
  possible." to "Give a short closing summary of the decisions — in the Architect's words where
  possible, each with its `[number | text]` subject (governing skill → Structured questions)."

##### 3.4 Build and Validate
- [x] Re-read the round template as rendered markdown: the code block still opens and closes.

#### Phase 4: Phase 05 and reconcile ✅

**Why:** These two skills put items to a person outside the governing and interview skills — a
waived test, a contradictory decision — source: 03/19 (DD-23), 03/6 (DD-14).

##### 4.1 Phase 05 completion notice (`p05 :292`, 03/19)
- [x] Change "[or: with the following waived: …]" to "[or: with the following waived:
  [T-<n> | what the test checks], …]".

##### 4.2 Reconcile report (`rec :158`, 03/6)
- [x] Change "- [id-A] and [id-B] both govern" to "- [id-A | what it decides] and [id-B | what it
  decides] both govern".

##### 4.3 Reconcile notice (`rec :174-175`, 03/6)
- [x] Change "the list of items needing human resolution, pointing them at" to "the list of items
  needing human resolution, each with a `[id | text]` subject (governing skill → Structured
  questions), pointing them at".

##### 4.4 Build and Validate
- [x] Re-read both passages; the report template's headings are unchanged.

#### Phase 5: Stop condition 5 narrowed ✅

**Why:** The Architect added this to the scope and applied it to this run; the skill text must
say it, in every place that restates the trigger — source: 03/16, 03/24 (the Architect, log
07:32, 07:33); [Phase 03 scope addition](../phase-03-compliance-review/phase.md#scope-addition).

##### 5.1 Gate test trigger 1 and the repair paragraph (`gov :1204`, before `:1209`)
- [x] Replace "  1. the fix you would make next changes a phase conclusion, a delegated decision or
  an ADR; or" with "  1. the fix you would make next changes a phase conclusion, an ADR, or what a
  delegated" / "     decision decides; or".
- [x] After trigger 3 and before "Log each attempt as …", add the paragraph of the scope
  addition, indented two spaces: "A fix that only repairs how a decision is recorded is not such
  a change: splitting a question into one per decision with the same answer each, moving a
  question to the round its dependencies allow, correcting a citation, or raising a decision's
  materiality to `MATERIAL — unconfirmed`. Each new or changed entry keeps the decision's answer
  and states the repair; the review round still puts every one of them to the Architect."

##### 5.2 Stop condition 5 (`gov :1243-1244`)
- [x] Change "or needs a fix that changes a conclusion, a delegated decision or an ADR (Gate
  test);" to "or needs a fix that changes a conclusion, an ADR or what a delegated decision
  decides (Gate test);".

##### 5.3 Phase 05 accept (`p05 :325-326`)
- [x] Change "If the next fix would change a phase conclusion, a delegated decision or an ADR,
  stop." to "If the next fix would change a phase conclusion, an ADR, or what a delegated
  decision decides, stop; a fix that only repairs how a decision is recorded is not such a change
  (governing skill → Gate test)."

##### 5.4 Configuration comment (`gov :750`, `README.md:254`)
**Why:** the README block is a copy of the governing template and stays identical — source: lesson `2026-11-05.readme_restates_config_template`, cited by Phase 01; Phase 03 scope addition.
- [x] In both, replace "# It stops sooner when a repair makes no progress or would change a
  conclusion." with "# It stops sooner when a repair makes no progress, or would change a
  conclusion, an ADR" / "# or what a delegated decision decides." (two lines).

##### 5.5 Build and Validate
- [x] `gov`: no "a delegated decision or an ADR" remains in the Gate test or Stop conditions; the
  two template copies are identical.

#### Phase 6: README and verification ✅

**Why:** The README tells the Architect what an autonomous stop and review round look like, so it
names the form (03/14); then every requirement is checked against the edited text — source:
03/14 (DD-26); this plan's Test Plan.

##### 6.1 README autonomous-mode section (`README.md:219-221`, `:230-231`, 03/14)
- [x] Change "It collects those questions into one numbered round with its proposed answers;" to
  "It collects those questions into one numbered round with its proposed answers, each item
  named as `[number | text]` so you can answer from the message alone;".
- [x] Change "with one numbered review round: each delegated decision (adopt, override or
  later)" to "with one numbered review round: each delegated decision, named as
  `[DD-<n> | what was decided]` (adopt, override or later)".

##### 6.2 Run the text checks
- [x] Write `files/phase-05-text-checks.py` from the Test Plan below (T-1 – T-20) and run it from
  the repository root; every check passes.
- [x] `git diff --stat` outside `.speccen/` lists exactly the five files of the Proposed Changes
  Summary.

##### 6.3 Build and Validate
- [x] The repository has no build. Validation is 6.2.

### Risk Mitigation

| Risk | Impact | Mitigation |
|---|---|---|
| A pointer is missed, so one message still uses bare labels | Medium | the inventory A-1 – A-20 (Phase 02) is the list; T-3 – T-15 check each site |
| The subject's `\|` breaks a markdown table | Medium — a record table renders wrongly | the rule says to escape it (T-2) |
| The narrowing is read as allowing any change to a DD | High — a decision changes without the Architect | trigger 1 still names "what a delegated decision decides"; the paragraph lists the repairs and requires that each keeps the answer and states the repair (T-16) |
| The README template copy drifts from the governing template | Medium | T-18 compares the two blocks |
| The self-check count and item list disagree | Low | T-8 |
| Line numbers shift during editing | Low | each item names the text it changes |

### Test Plan

The repository has no test framework (Phase 02). Unit and integration tests: **none, because the
change is prose inside Markdown with no executable code**. The planned tests are **text checks**
— a Python script run in Phase 05 after the edits, derived from the requirements below, not from
the edited text. The script is a bundle file (`files/`), not a repository test.

| Id | Check | Requirement |
|---|---|---|
| T-1 | Structured questions ends with the Subjects paragraph, after "A series of decisions": it holds `[INTERNAL-NUMBER \| HUMAN UNDERSTANDABLE TEXT]`, "A label never stands alone.", both examples and every label kind (`DD-<n>`, `01/<n>`, `<skill>/<n>`, `Deviation [N]`, `O-<n>`, `H-<n>`, `P02-<n>`, a gate-check row) | R-1 |
| T-2 | The paragraph's bullets: the `AskUserQuestion` header exemption, the escape of the bar with a backslash, and the records sentence naming the gate-check, delegated-decision and interview tables, the delegation findings and the fix-attempt log line | R-1, R-2, R-3 |
| T-3 | The subject rule's form is defined once: "HUMAN UNDERSTANDABLE TEXT" appears exactly once in the skills | R-1 |
| T-4 | Round template: `**[01/7 \| The decision, as a plain question]**` and `**[01/8 \| …]**`; no "[Short title]" remains; the "Subject format" bullet follows "One decision per question" | R-4 |
| T-5 | Review round: "with the subject `[DD-<n> \| what was decided]`"; the old "(`DD-<n>`): `adopt`" is gone; "Put the `MATERIAL — unconfirmed` decisions first." stays | R-5 |
| T-6 | Stop record: "every item with a `[number \| text]` subject, readable without the rest of the bundle" | R-6 |
| T-7 | End-of-run report: "in one message, with `[number \| text]` subjects (Structured questions): the phases run" | R-7 |
| T-8 | Self-check: "for the six common failures"; item 6 "**Subjects**"; no "five common failures" remains | R-8 |
| T-9 | `stops: proceed`: "under its open items, with a `[number \| text]` subject" | R-9 |
| T-10 | Resume summary: "each named with a `[number \| text]` subject" | R-10 |
| T-11 | Closing summary: "each with its `[number \| text]` subject" | R-11 |
| T-12 | Phase 05 notice: "[T-<n> \| what the test checks]" | R-12 |
| T-13 | `STATE.md` stop line: "where an item the reason names has its `[number \| text]` subject" | R-13 |
| T-14 | Reconcile: "[id-A \| what it decides] and [id-B \| what it decides]" and the notice's "each with a `[id \| text]` subject" | R-14 |
| T-15 | README: "each item named as `[number \| text]`" and "`[DD-<n> \| what was decided]`" in the autonomous-mode section; `ARCHITECTURE.md` has no diff | R-15 |
| T-16 | Gate test: trigger 1 reads "an ADR, or what a delegated decision decides"; the repair paragraph lists the four repairs and "keeps the decision's answer and states the repair" and sits before "Log each attempt" | R-16 |
| T-17 | Stop condition 5 reads "an ADR or what a delegated decision decides"; Phase 05 Step 7 reads "an ADR, or what a delegated decision decides, stop"; "a delegated decision or an ADR" appears in neither skill | R-16 |
| T-18 | The config comment's new two lines are in the governing template and the README copy, and the two template blocks are identical | R-16 |
| T-19 | Unchanged: the tool's constraints in Structured questions; the fix-attempt log line format; the interview Numbering section; "Conditions 2 to 8 stay hard stops" | R-2, R-17 |
| T-20 | `git diff --stat` outside `.speccen/` lists exactly `gov`, `int`, `p05`, `rec` and `README.md` — so the audit and code-documentation skills get no pointer of their own | R-4, R-17 |

**Behaviours to cover** (what must be true): a label never stands alone in anything put to the
Architect (R-1); records keep their form, so no traceability is lost (R-2, edge); a subject
inside a table does not break it (R-1, edge); the header of a tool call stays within its
12-character limit (R-3, boundary); a fix that changes what a decision decides still stops
(R-16, error path); a record repair keeps the answer and is stated, and the review round still
shows it (R-16, side effect); the README template copy stays identical (R-16).

**Coverage intent:** every requirement R-1 – R-17 has at least one check; every error and edge
path above has one.

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

<a id="outcome"></a>
## Outcome

Selected approach: the brief's §2 change as refined by the Phase 03 decisions (DD-9 – DD-27), with
the Architect's narrowing of stop condition 5, in six implementation phases (rule → governing
pointers → interview → Phase 05 and reconcile → stop condition 5 → README and verification).
Seventeen requirements, twenty text checks. The plan, the Test Plan and the intent seeds are
approved when the delegate's gate test passes (autonomous).

<a id="open-items"></a>
## Open Items

| # | Item | Settles in |
|---|---|---|
| O-4 | [O-4 \| What are the acceptance scenarios — when is this done?] — settled by R-1 – R-17 | settled |
| O-8 | [O-8 \| Fourteen material answers taken under `stops: proceed` wait for the Architect] — carried from Phase 03; the plan implements them as answered | the review round after the run |

Residual assumption: the cache copy of the plugin (`~/.claude/plugins/cache/…/26.1112.2/`) is not
edited; the change reaches it with the next plugin version.
