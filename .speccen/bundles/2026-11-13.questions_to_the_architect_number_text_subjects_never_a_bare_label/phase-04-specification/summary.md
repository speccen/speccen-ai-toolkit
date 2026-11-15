---
type: Summary
phase: "04 — Specification"
status: COMPLETE
phase_file: ./phase.md
description: Six-phase plan, seventeen requirements and twenty text checks — the subject rule with its pointers, and the narrowed stop condition 5
---

# Phase 04 Summary — Specification

[Index](../index.md) · [State](../STATE.md) · [Log](../log.md)

---

**Work completed:** an Implementation Plan in six phases (the rule → governing pointers →
interview → Phase 05 and reconcile → stop condition 5 → README and verification); seventeen
requirements with acceptance scenarios; a Test Plan of twenty text checks; one delegate
interview question, [04/1 | Are the skill-text changes left uncommitted in the working tree for the Architect, with only
the bundle files committed at each phase transition?].

**Outcome:** the brief's §2 change as refined by the Phase 03 decisions, plus the Architect's
narrowing of stop condition 5, across five files → [full detail](./phase.md#implementation-plan)

**Specification (the complete, assembled spec — intent + requirements/scenarios):**
- [specification.html](./specification.html) — full, authoritative (reduced view: [specification.md](./specification.md))

**Stakeholder seeds (intent — expansion seeds, not for verbatim external sharing):**
- Executive → [doc-executive.md](./doc-executive.md)
- Business → [doc-business.md](./doc-business.md)

**Delegated decisions:** 1 in this phase, [DD-28 | Skill-text changes stay uncommitted for the Architect](../delegated-decisions.md#dd-28), not material.

**Open items carried forward** → [detail](./phase.md#open-items)

- [O-8 | Fourteen material answers taken under `stops: proceed` wait for the Architect] → the
  review round after the run

<a id="delegate-gate-check"></a>
## Delegate gate check

Self-check: done — 0 corrections (run 1); done — 0 corrections before run 2; done — 0 corrections before run 3; done — 0 corrections before run 4; done — 0 corrections before run 5; done — 0 corrections before run 6

| # | Item | Result | Evidence | Verified |
|---|---|---|---|---|
| 1 | [1 \| Extensions: every file in `.speccen/extensions/specification/` is in the table; active ones applied] | pass | [phase.md#extensions](./phase.md#extensions) — `.speccen/extensions/` does not exist | confirmed (run 1) |
| 2 | [2 \| Proposed changes summary lists all affected files with their change type] | pass | [phase.md#implementation-plan](./phase.md#implementation-plan) → Proposed Changes Summary: five files, `modify`; none created or deleted | confirmed (run 3) |
| 3 | [3 \| Target-state flow is an ASCII diagram linking to the Phase 02 as-is diagram] | pass | phase.md → Target-State Execution Flow; link `../phase-02-code-analysis/phase.md#code-analysis` | confirmed (run 3) |
| 4 | [4 \| Strategy evaluation present if multiple approaches] | n/a | one approach remains (phase.md → Strategy Evaluation); no prototype ran | confirmed (run 1) |
| 5 | [5 \| Implementation phases numbered and sequenced logically] | pass | Phases 1 – 6: the rule first, because every pointer names it | confirmed (run 3) |
| 6 | [6 \| Every checklist item specific, actionable, traceable] | pass | each item quotes the text it changes and its `path:line`; each subtask's source is in its heading (brief section or Phase 03 question), in its own one-line Why (1.1, 2.6, 5.4), or in its phase's Why (5.1 – 5.3, 6.2); the Build and Validate subtasks (1.2, 2.7, 3.4, 4.4, 5.5, 6.3) follow the skill's template | confirmed (run 5) |
| 7 | [7 \| Each phase ends with a Build and Validate step] | pass | 1.2, 2.7, 3.4, 4.4, 5.5, 6.3 | confirmed (run 3) |
| 8 | [8 \| Every phase states a Why with a source; subtask Whys only where non-obvious] | pass | Phases 1 – 6 each cite brief sections, Phase 03 questions or DDs; subtask Whys at 1.1, 2.6, 5.4 | confirmed (run 6) |
| 9 | [9 \| Risk mitigation table populated] | pass | phase.md → Risk Mitigation: six risks | confirmed (run 1) |
| 10 | [10 \| Test Plan: scope (or "none, because"), behaviours incl. error/edge/side effects, coverage intent] | pass | phase.md → Test Plan: "none, because the change is prose inside Markdown"; T-1 – T-20; Behaviours to cover; Coverage intent | confirmed (run 3) |
| 11 | [11 \| `doc-executive.md` and `doc-business.md` written, `expandable: true`] | pass | [doc-executive.md](./doc-executive.md), [doc-business.md](./doc-business.md) frontmatter | confirmed (run 1) |
| 12 | [12 \| Both seeds in STE style] | pass | short active sentences, one idea each, plain vocabulary | confirmed (run 1) |
| 13 | [13 \| Executive seed keeps TCO out of scope] | pass | doc-executive.md → Scope Note | confirmed (run 1) |
| 14 | [14 \| Deviations protocol stated] | pass | phase.md → Deviations Protocol | confirmed (run 1) |
| 15 | [15 \| `specification.html` assembled from the 01 – 04 phase files, STE, depth-layered; `specification.md` its reduced projection] | pass | [specification.html](./specification.html): current state from Phase 02, L1 context, L2 files, L3 flow and stop condition 5, the plan with each phase's Why; requirements and checks generated from phase.md tables; [specification.md](./specification.md) | confirmed (run 4) |
| 16 | [16 \| Specification has Requirements & acceptance scenarios (SHALL / WHEN–THEN), with error and edge behaviour] | pass | specification.html#requirements: R-1 – R-17; error path R-16 (a fix that changes a decision stops), edges R-1 (table cell), R-3 (header) | confirmed (run 3) |
| 17 | [17 \| Specification diagrams verified to render] | pass | three SVGs parsed as XML; rendered in headless Chrome and inspected (2026-11-15) | confirmed (run 3) |
| 18 | [18 \| `summary.md` links to the plan, the specification and both seeds] | pass | this file, top section | confirmed (run 3) |
| 19 | [19 \| `index.md` lists every bundle file this phase wrote, with status and description] | pass | [index.md](../index.md) → Phase 04 | confirmed (run 1) |
| 20 | [20 \| `autonomous`: this gate check written with evidence for every item] | pass | this section | confirmed (run 3) |
| 21 | [21 \| Traceability: every requirement and ADR has a scenario, every scenario a test, nothing invented; every phase Why cites a source] | pass | [Traceability](#traceability) below | confirmed (run 3) |
| 22 | [22 \| Material choices put through the interview; none left open] | pass | [phase.md#interview](./phase.md#interview): 04/1 (DD-28, not material); no contract, data-model, dependency or plan-structure choice open | confirmed (run 1) |
| 23 | [23 \| No question parked with "later" is still unanswered] | pass | phase.md: "No question was answered "later"." | confirmed (run 1) |

<a id="traceability"></a>
### Traceability

| Source | Requirement | Scenario | Tests |
|---|---|---|---|
| Brief §2, §2.1; 03/2, 03/10, 03/12 | R-1 | R-1 scenarios (DD-4 subject; table cell) | T-1, T-2, T-3 |
| Brief §3, §5.2; 03/3, 03/7, 03/21 | R-2 | gate check rows; fix-attempt line | T-2, T-19 |
| 03/8 | R-3 | tool question naming O-3 | T-2 |
| Brief §2.2; 03/9 | R-4 | Phase 01 round; audit interview | T-4, T-20 |
| Brief §2.3 | R-5 | review round with DD-12 | T-5 |
| Brief §2.4 | R-6 | gate stop naming row 16 | T-6 |
| Brief §2.5 | R-7 | report listing a stop | T-7 |
| Brief §2.6; 03/4 | R-8 | self-check run; item count | T-8 |
| 03/5 | R-9 | decision under `proceed` | T-9 |
| 03/17 | R-10 | resume with a stop waiting | T-10 |
| 03/18 | R-11 | `gated` interview closes | T-11 |
| 03/19 | R-12 | a waived test | T-12 |
| 03/20 | R-13 | stop reason naming a row | T-13 |
| 03/6 | R-14 | two contradictory decisions | T-14 |
| 03/14, 03/15 | R-15 | README autonomous section | T-15 |
| 03/16, 03/24; the Architect (log 07:32, 07:33) | R-16 | split question continues; changed answer stops | T-16, T-17, T-18 |
| Brief §3, §4; 03/15 | R-17 | `git diff --stat` | T-19, T-20 |
| ADRs | — | no bundle ADR; seven standing decisions, none touched ([Phase 03](../phase-03-compliance-review/phase.md#adrs)) | — |

Every implementation phase's Why cites a source (phase.md → Implementation Phases).
