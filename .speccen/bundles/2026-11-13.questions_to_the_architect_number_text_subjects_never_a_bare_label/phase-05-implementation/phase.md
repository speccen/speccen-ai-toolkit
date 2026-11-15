---
type: Phase
phase: "05 — Implementation"
status: COMPLETE
description: The subject rule, its pointers and the narrowed stop condition 5 applied to five files; twenty text checks pass
---

<a id="phase-top"></a>
# Questions to the Architect: [number | text] subjects, never a bare label — Implementation

[Index](../index.md) · [State](../STATE.md) · [Log](../log.md)

---

<a id="extensions"></a>
## Extensions applied

| Extension | Why | Where it applies | Outcome |
|---|---|---|---|
| — | — | — | No extensions for this phase |

`.speccen/extensions/` does not exist in this repository.

### Project Conventions Re-Confirmation (Phase 05)

No `.claude/` folder and no `CLAUDE.md` exist.

#### `.github/SECURITY.md`
**Re-Read:** ✓  
**CRITICAL/MANDATORY Rules Impacting This Implementation:** none. Its scope names "Instructions or
commands that could cause an assistant to run unintended or destructive actions" and
"Prompt-injection weaknesses in the skills and workflows"; the change adds wording rules only and
no command.

#### `.github/CODEOWNERS`
**Re-Read:** ✓  
**Other Rules Impacting This Implementation:** `*` is owned by `@speccen/team-leads`; the changed
files need their review at merge. `/.github/` and `/.claude-plugin/` are not touched.

#### `.github/workflows/bump-version.yml`
**Re-Read:** ✓  
**Other Rules Impacting This Implementation:** a change to `skills/` bumps the version on merge to
`main`; no manual version change.

### Plan confirmation

Plan confirmed by the delegate — 2026-11-15 (autonomous mode; the gate test of Phase 04 passed).

<a id="implementation-summary"></a>
## Implementation Summary

All six plan phases executed in order; every checklist item is ticked in
[the plan](../phase-04-specification/phase.md#implementation-plan). The skill-text changes stay
uncommitted in the working tree (04/1, [DD-28](../delegated-decisions.md#dd-28)).

| Plan phase | Files | Result |
|---|---|---|
| 1 — The rule | `skills/sdd/00-governing-workflow/SKILL.md` | Subjects paragraph at the end of Structured questions, after "A series of decisions" |
| 2 — Governing pointers | `skills/sdd/00-governing-workflow/SKILL.md` | resume summary, stop line, stop record, `stops: proceed` item, end-of-run report; self-check "six" and item 6 |
| 3 — Interview | `skills/sdd/interview/SKILL.md` | round template, Subject format bullet, review round, closing summary |
| 4 — Phase 05 and reconcile | `skills/sdd/05-implementation/SKILL.md`, `skills/sdd/reconcile/SKILL.md` | waived-test subject; "Needs human resolution" item and notice |
| 5 — Stop condition 5 | governing (trigger 1, repair paragraph, condition 5, config comment), Phase 05 Step 7, `README.md` template comment | narrowed in every place that states it |
| 6 — README and verification | `README.md` | stop round and review round name the form; text checks T-1 – T-20 pass |

`git diff --stat` outside `.speccen/`: five files, 71 insertions and 31 deletions — `README.md`,
the governing, interview, Phase 05 and reconcile skills, as planned.

Where an inserted text made a line longer than 100 columns, the edit rewraps the lines around it:
the README stop round and review round, the interview review round, the Phase 05 Step 7 trigger,
the reconcile item and notice, and the end-of-run report paragraph in the governing skill (plan
item 2.5, rewrapped as a whole). Every changed word is plan target text; the rewraps change no
wording, so they are implementation detail, not a deviation.

The checks compare unchanged passages and the file list with `67c6ad8`, the last commit before the
edits, so they stay valid after the skill edits are committed.

### Tests

The Test Plan's text checks are [files/phase-05-text-checks.py](../files/phase-05-text-checks.py),
run from the repository root. Each assertion is written from the requirement and the plan's
target text, not read back from the edited files.

| Run | Against | Result |
|---|---|---|
| 1 | the working tree after the edits | T-1 – T-20: all PASS |
| control | an unedited worktree at `67c6ad8` | T-1 – T-18 and T-20 FAIL; T-19 PASS (it checks passages that must stay unchanged) |

The control run shows that each check can fail, so a PASS is evidence.

<a id="deviations"></a>
## Deviations

None.

<a id="open-items"></a>
## Open Items

| # | Item | Settles in |
|---|---|---|
| O-8 | [O-8 \| Fourteen material answers taken under `stops: proceed` wait for the Architect] | the review round after the run |

<a id="outcome"></a>
## Outcome

The implementation matches the plan with no deviation, and the twenty planned text checks pass.
Accepted when the delegate's gate test passes (autonomous).
