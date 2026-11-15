---
type: Doc
audience: technical
expandable: true
status: COMPLETE
description: One subject rule in the governing skill, its pointers in four skills and the README, and the narrowed stop condition 5
---

# Questions to the Architect: [number | text] subjects, never a bare label — Technical Documentation (seed)

Plan: [Phase 04 Implementation Plan](../phase-04-specification/phase.md#implementation-plan). Record: [Phase 05](../phase-05-implementation/phase.md#implementation-summary).

## Files Created
| File | Description |
|---|---|
| — | No file created in the repository. The bundle holds the check script `files/phase-05-text-checks.py`. |

## Files Modified
| File | Changes |
|---|---|
| `skills/sdd/00-governing-workflow/SKILL.md` | Structured questions: a Subjects paragraph — the form `[INTERNAL-NUMBER \| HUMAN UNDERSTANDABLE TEXT]`, two examples, the label kinds, the `AskUserQuestion` header exemption, the table escape, records excluded. Pointers to it: resume summary, `STATE.md` stop line, stop record in `summary.md`, `stops: proceed` open item, end-of-run report. Self-check: six items, item 6 "Subjects". Gate test: trigger 1 reads "an ADR, or what a delegated decision decides"; a paragraph says a record-only repair is not such a change. Stop condition 5 and the config template comment say the same. |
| `skills/sdd/interview/SKILL.md` | Round template `**[01/7 \| The decision, as a plain question]**`; a "Subject format" bullet; review round `[DD-<n> \| what was decided]`; closing summary with subjects. |
| `skills/sdd/05-implementation/SKILL.md` | Completion notice names waived tests as `[T-<n> \| what the test checks]`; Step 7 accept trigger narrowed as in the gate test. |
| `skills/sdd/reconcile/SKILL.md` | "Contradictory decisions" item `[id-A \| what it decides] and [id-B \| what it decides]`; the notice gives each item a subject. |
| `README.md` | Autonomous-mode section: the stop round and the review round name the form; the template comment equals the governing one. |

All five stay uncommitted for the Architect ([DD-28](../delegated-decisions.md#dd-28)). Diff: 71 insertions, 31 deletions.

## Files Deleted
| File | Reason |
|---|---|
| — | No file deleted. |

## Deviations from Plan
- None → [Phase 05 deviations](../phase-05-implementation/phase.md#deviations). Rewraps to 100 columns change no wording.

## Learnings & Pitfalls (this feature)
- A bare `|` inside a code span still splits a GitHub table row. Escape it as `\|` in every table cell, also inside backticks. Inside a code span in a table, `\|` renders as `|`, so a rule about the escape itself must be written in words there.
- The no-progress trigger looks only at named breaches. A repair that keeps a named breach on purpose (for traceability) still counts as no progress, so remove it from the round instead.
- An answered stop sets no fix budget unless the answer says so; the default is one verifier run. A stop question should propose the budget explicitly (03/22, 03/23).
- Subjects in a summary must equal their source word for word; a shortened subject is a breach (Phase 04 runs 2 – 3).
- Known limit: the checks were validated with a control run on the unedited text (19 of 20 fail), not with the move test of lesson `2026-11-11.text_checks_read_their_place`. Several checks search the whole file for a unique phrase, so a moved text would still pass.

## Results (if measured)
| Metric | Before | After | Improvement |
|---|---|---|---|
| Text checks T-1 – T-20 | 1 of 20 pass (the unchanged-passage check) | 20 of 20 pass | all requirements met |
| Phase 02 inventory sites changed (A-1 – A-3, A-5 – A-8, A-16 – A-19) | 0 of 11 carry the rule | 11 of 11 | the rule or a pointer to it at each; A-4, A-9, A-10, A-13, A-14 inherit it through the round template |
