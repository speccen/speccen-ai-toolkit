---
type: Summary
phase: "02 — Code Analysis"
status: COMPLETE
phase_file: ./phase.md
description: The brief's six edits fit the skills as they are; several more Architect-facing places name items by label, and three governing line references have drifted
---

# Phase 02 Summary — Code Analysis

[Index](../index.md) · [State](../STATE.md) · [Log](../log.md)

---

**Work completed:** the skills read as code — architecture, the paths by which an item reaches
the Architect (ASCII flow), an inventory of 20 Architect-facing places, the brief's line
references, where labels are defined, the `AskUserQuestion` calls, the restated copies in
`README.md` and `ARCHITECTURE.md`; `.github/` conventions confirmed.

**Outcome:** the skills label items (`DD-<n>`, `01/7`) but never ask that the item's text travel
with the label; the brief's edits land at the right places and still apply by content. Places
outside the brief also name items by label — the `stops: proceed` open item, the resume summary,
the interview's closing summary, the Phase 05 completion notice, the `STATE.md` stop line — and
so do records the Architect reads (Retrospective findings, the reconcile report, the fix-attempt
log line) → [full detail](./phase.md#outcome)

**Extensions applied:** none

**Delegated decisions:** none in this phase.

**Stops (answered):** [stop 1](#stop) — "yes" to 02/1 and 02/2 (log 07:03); [stop 2](#stop-2) —
"yes" to 02/3 and 02/4 (log 07:11): rows 3 and 4 accepted with their gaps recorded as known limits
of the diagrams; the inventory A-1 – A-20 is the complete list of paths.

**Open items carried forward** → [detail](./phase.md#open-items)

- [O-1 | Does the rule reach places the brief does not list — the `stops: proceed` open item,
  the resume summary, the interview's closing summary, the Phase 05 completion notice, the
  `STATE.md` stop line, and the records the Architect reads?] → Phase 03
- [O-2 | The three decisions in brief §5: state the rule once and point to it; cover only what
  is put to the Architect, not the record tables; add a sixth self-check item for subjects.]
  → Phase 03
- [O-3 | Does the rule cover the questions asked with the `AskUserQuestion` tool, and if so
  which parts?] — no call names a bundle item today → Phase 03
- [O-4 | What are the acceptance scenarios — when is this done?] → Phase 04
- [O-6 | Where in Structured questions does the rule go — after the tool's constraints, or after
  "A series of decisions"?] → Phase 03
- [O-7 | Should `README.md` and `ARCHITECTURE.md` mention the subject form where they describe
  stops and the review round?] → Phase 03

**Evolution-gap doc:** not generated — no structural evolution-blocker found; the rule slots into
**Structured questions** and the existing templates (no indicator fires: no boundary, stub,
contract, scaling, deferred-design or entanglement finding in [phase.md](./phase.md#code-analysis)).

<a id="delegate-gate-check"></a>
## Delegate gate check

Self-check: done — 4 corrections before run 1 (four `path:line` citations — `:429`, `:182`, `:360-363`, `:1183-1190`); done — 0 corrections before run 2 (two breaches of row 3 were missed — run-2 extra finding 4). Fix attempt 1 of 5 repaired rows 3, 4, 5, 7, 12 and the run-1 extra findings 1 – 9 (five missed places added as A-16 – A-20, the label list completed, the diagram's missing branches drawn, sections reordered). Before run 3: done — 0 corrections beyond fix attempt 2, which repaired rows 3 and 4 and run-2 extra findings 1 – 3. Before run 4: done — 2 corrections (two diagram citations re-opened: the record rule is `:1220-1222`, the basis and materiality `:1157-1169`, `:1228-1230`); fix attempt 3 of 5 repaired rows 3 and 4 and run-3 extra findings 1 – 4. Before run 5: done — 2 corrections (two diagram citations re-opened: the review round in the end-of-run text is `:1341-1343`; the decision basis is `:1157-1169`); fix attempt 4 of 5, after the stop, narrowed the flow (02/2) and repaired rows 3 and 4.

| # | Item | Result | Evidence | Verified |
|---|---|---|---|---|
| 1 | [1 \| Extensions: every file in `.speccen/extensions/code-analysis/` is in the table; active ones applied] | pass | [phase.md#extensions](./phase.md#extensions) — `.speccen/extensions/` does not exist; one "No extensions" row | confirmed (run 1) |
| 2 | [2 \| Architecture overview with position in the system] | pass | [phase.md#code-analysis](./phase.md#code-analysis) → Architecture Overview: position, hierarchy, where the change lives | confirmed (run 3) |
| 3 | [3 \| Full behavioural analysis with all execution paths] | accepted by the Architect (02/3) | phase.md → Behavioural Analysis: gated round, autonomous decide / stop (`ask`) / proceed, gate test, end of run, resume; known limits recorded in phase.md above the inventory | not confirmed (run 5) — accepted by the Architect, 02/3 (log 07:11) |
| 4 | [4 \| Primary flow as an ASCII diagram matching the real branches] | accepted by the Architect (02/3) | phase.md → Behavioural Analysis, narrowed by 02/2 to the paths by which an item reaches the Architect: a prose outline and three boxed diagrams — (1) `gated` interview: round loop, the five kinds of answer (int `:123-133`), closing summary and question with the \"not yet\" loop; (2) `autonomous` decision: decide and record-or-not (`:1220-1222`), `proceed` (`:1279-1282`), hard stops 2, 3, 4, 6, 7 and `ask` → stop, review round (int `:153-161`); (3) gate test result (`:1199-1207`, `:1251`), fix-and-retry (`:1209`), end of run (`:1337-1343`), the stop (`:1258-1264`) and its answers incl. \"later\" and the re-check default (`:1210-1212`, int `:143-146`), resume summary (`:533-540`), Phase 05 completion notice (p05 `:286-292`); known limits recorded in phase.md above the inventory | not confirmed (run 5) — accepted by the Architect, 02/3 (log 07:11) |
| 5 | [5 \| Data model with types, properties and cardinalities] | pass | phase.md → Data Model: subject shape, label kinds, `\|` escaping, round and DD counts | confirmed (run 3) |
| 6 | [6 \| `.claude/` and `.github/` scanned, every `.md` read] | pass | [phase.md#conventions](./phase.md#conventions) — no `.claude/`, no `CLAUDE.md`; `.github/SECURITY.md` read; `CODEOWNERS` and `workflows/bump-version.yml` read too | confirmed (run 3) |
| 7 | [7 \| Project Conventions Confirmation table created] | pass | [phase.md#conventions](./phase.md#conventions) | confirmed (run 3) |
| 8 | [8 \| Coding patterns and project practices identified, incl. test conventions] | pass | phase.md → Coding Patterns & Style: rule once and point; templates; self-check form; register; test conventions (text checks in `files/`, lesson `2026-11-11.text_checks_read_their_place`) | confirmed (run 3) |
| 9 | [9 \| Performance characteristics analysed] | pass | phase.md → Performance Characteristics (reading length; no runtime) | confirmed (run 3) |
| 10 | [10 \| Comparison with similar components] | pass | phase.md → Relationship to Similar Components (`doc-*.md` navigation rule, self-check item 5 decision) | confirmed (run 3) |
| 11 | [11 \| Known issues and code commentary captured verbatim] | pass | phase.md → Known Issues & Code Commentary (`skills/sdd/interview/SKILL.md:88`, `:158`; no TODO/FIXME) | confirmed (run 3) |
| 12 | [12 \| Executive Summary under the `outcome` anchor] | pass | [phase.md#outcome](./phase.md#outcome) | confirmed (run 4) |
| 13 | [13 \| Evolution-gap determination made, negative visible in the summary] | pass | this file → "Evolution-gap doc: not generated — …" | confirmed (run 3) |
| 14 | [14 \| `summary.md` written and linking back to the phase file] | pass | this file — links to `./phase.md#outcome`, `./phase.md#open-items`, `./phase.md#code-analysis` | confirmed (run 4) |
| 15 | [15 \| `index.md` lists every bundle file this phase wrote, with current status and description] | pass | [index.md](../index.md) → Phase 02 | confirmed (run 4) |
| 16 | [16 \| `gated` only: `STATE.md` reflects `AWAITING ARCHITECT REVIEW`] | n/a | Phase is `autonomous` (bundle `speccen-config.yaml`); the transition sets `STATE.md` | confirmed (run 1) |
| 17 | [17 \| `autonomous`: this gate check is written with evidence for every item] | pass | this section | confirmed (run 4) |
| 18 | [18 \| `autonomous`: no blocking open question] | pass | [phase.md#open-items](./phase.md#open-items) "No open item blocks Phase 03."; O-1, O-2, O-3, O-6, O-7 are Phase 03 decisions, O-4 is Phase 04 | confirmed (run 3) |
| 19 | [19 \| No question parked with "later" is still unanswered for this phase] | pass | Phase 02 ran no interview; no "later" in [log.md](../log.md) | confirmed (run 1) |


<a id="stop"></a>
## Stop — the flow analysis still fails the checker after three repairs

**Answered:** the Architect said "yes" to 02/1 and 02/2 (log 07:03). The flow was narrowed to the
paths by which an item reaches the Architect and repaired once (fix attempt 4 of 5); verifier run
5 re-checks rows 3 and 4 only.

The checker re-reads the evidence behind every row of the gate check. Two rows still fail after
four checker runs and three repairs:

- [Row 3 | Does the analysis cover every path by which an item reaches the Architect?] — it
  still misses the `gated` answers "stop", "later" and "don't know yet", and what happens after a
  gate stop when the Architect does not say which rows to re-check; it also draws a Phase 05
  notice at the end of an interview, a path that does not exist.
- [Row 4 | Does the flow diagram match the real branches of the rules, in the required box
  style?] — the endings after a stop still have no arrows back into the run, two conditions are
  written as box text instead of branches, and the resume-summary line is not in a box.

Two of these were already named by the run before (the endings after a stop, and a step not in a
box), so the rule "a run makes no progress" applies and the delegate must stop (stop condition 5).
No conclusion of Phase 02 is affected: every citation checks out, and the findings that matter for
this feature — the inventory of places, the label definitions, the line drift — are confirmed.

**Stop round**

**[02/1 | May the delegate make one more repair of the flow analysis and diagram, with the next
check limited to rows 3 and 4?]** One repair attempt is left in the budget (4 of 5 used). *Correction (log 07:05): 3 of 5 had been used; the stop came from the no-progress rule, not the budget. 02/1 allows exactly one more repair either way.*
→ Proposed: yes.

**[02/2 | Should the diagram show only the paths by which an item reaches the Architect, not
every branch of the workflow's decision rules?]** This feature changes what the Architect reads;
mapping every rule of the autonomous machinery is what keeps failing, and it is outside the
request. The narrower diagram keeps every place in the inventory and drops branches that never
put an item to the Architect.
→ Proposed: yes.

Lean: yes to both — narrow the diagram (02/2), then repair once (02/1). Evidence:
[verifier runs 1 – 4 in log.md](../log.md), [phase.md → Behavioural Analysis](./phase.md#code-analysis).


<a id="stop-2"></a>
## Stop 2 — the narrowed flow still misses paths

**Answered:** the Architect said "yes" to 02/3 and 02/4 (log 07:11). Rows 3 and 4 are accepted as
they are; the gaps are recorded as known limits in [phase.md](./phase.md#architect-facing-places).

The one repair that 02/1 allowed is done (fix attempt 4 of 5). The checker (run 5) confirms that
every gap from the run before is fixed, but it finds new ones in the same two rows:

- [Row 3 | Does the analysis cover every path by which an item reaches the Architect?] — six
  gaps: the answer "a question back" (the question goes back to the Architect); the `autonomous`
  Phase 01 working hypothesis; the review round when the Architect asks for it, not only at the
  end of a run; the `gated` Phase 05 deviation notice ("Please review and signal how to
  proceed"); the end of a `gated` phase that ran no interview; and the Retrospective findings and
  the reconcile report, which are neither drawn nor left out on purpose.
- [Row 4 | Does the flow diagram match the real branches of the rules?] — the same missing
  branches, plus: the `gated` "stop" answer skips the step that records it, and one citation
  (the decision basis) does not support the "not material" half of its label.

The rule after an answered stop is "one run, and a failing row stops again", so the delegate
stops. Every finding this feature needs is confirmed: the inventory of 20 places (A-1 – A-20)
already lists each of the paths the checker names — A-11 the deviation notice, A-12 the
phase-end notices, A-15 the Retrospective findings, A-19 the reconcile report. What fails is the
diagram's attempt to redraw that inventory as a flow.

**Stop round**

**[02/3 | May Phase 02 close with rows 3 and 4 accepted as they are, the six gaps recorded as known
limits of the diagram, and the inventory A-1 – A-20 as the complete list of paths?]** Every gap
is a place the inventory already lists; Phase 03 decides the rule's reach from the inventory
(O-1), not from the diagram.
→ Proposed: yes.

**[02/4 | Do records the Architect reads, and skills outside the speccen workflow — the
Retrospective, reconcile, audit, code review — stay out of the diagram, and inside the inventory
only?]** They are in the inventory (A-13 – A-15, A-19, A-20). Whether the rule reaches them is
Phase 03's question O-1.
→ Proposed: yes.

If 02/3 is "no", the next question is whether to repair once more; it is held back until 02/3 is
answered.

Lean: yes to both. Evidence: [verifier runs in log.md](../log.md), [phase.md →
inventory](./phase.md#architect-facing-places).
