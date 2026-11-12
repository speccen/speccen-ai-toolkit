---
type: Summary
phase: "05 — Implementation"
status: COMPLETE
phase_file: ./phase.md
description: The fixes budget is in the governing skill, the Phase 05 skill and the README; text checks T-1 – T-19 pass; changes uncommitted for the Architect
---

# Phase 05 Summary — Implementation

[Index](../index.md) · [State](../STATE.md) · [Log](../log.md)

---

**Work completed:** one iteration, accepted by the delegate after verifier run 8 (failed rows per run 1 → 1 → 2 → 2 → 2 → 1 → 1 → 0; three stop rounds answered by the Architect, 05/1 – 05/3; delegate repairs DD-30 – DD-32); plan phases 1 – 5 executed in order, every checklist item
ticked → [implementation summary](./phase.md#implementation-summary).

**Outcome:** three files changed — `skills/sdd/00-governing-workflow/SKILL.md`,
`skills/sdd/05-implementation/SKILL.md`, `README.md` — left uncommitted for the Architect (DD-24).

**Tests:** the Test Plan's text checks T-1 – T-19 all pass; no waiver →
[results](./phase.md#test-results). No unit or integration test, as planned ("none, because the
change is prose and YAML inside Markdown").

**Deviations:** none → [deviations](./phase.md#deviations)

**Delegated decisions:** 3 — [DD-30 – DD-32](../delegated-decisions.md#dd-30)

**Extensions applied:** none

<a id="delegate-gate-check"></a>
## Delegate gate check

### Acceptance scenarios → tests

All fifteen rows confirmed in verifier run 1; their evidence files did not change after it, except the check script, which runs 6 and 8 confirmed.

| Requirement | Planned test(s) | Result | Delivered in |
|---|---|---|---|
| R-1 `fixes` key, five phases, autonomous only | T-2, T-3 | pass | governing Keys table and "Which phases take which key" |
| R-2 default `1` | T-7 | pass | governing Effective settings |
| R-3 fix and re-run up to the budget | T-8 | pass | governing Gate test, fix bullet |
| R-4 no progress stops | T-9, T-10 | pass | governing Gate test, stop bullet guard 3 |
| R-5 conclusion change stops | T-9 | pass | governing Gate test, stop bullet guard 1 |
| R-6 ceiling 3, invalid → `1` | T-7, T-9 | pass | governing Keys values, fail-safe line |
| R-7 log line per attempt | T-11 | pass | governing Gate test, stop bullet |
| R-8 after a stop | T-12 | pass | governing Gate test, after-a-stop bullet |
| R-9 stop condition 5 | T-13 | pass | governing Stop conditions |
| R-10 Phase 05 accept | T-14, T-15 | pass | `05-implementation/SKILL.md` Step 7 |
| R-11 template version 3 | T-1, T-4, T-16 | pass | governing template; README copy |
| R-12 upgrade, absence values | T-5, T-6, T-17 | pass | governing upgrade; README absence values |
| R-13 locks | T-19 | pass | Locks section unchanged |
| R-14 self-check line | T-18 | pass | governing Gate test, self-check |
| R-15 three files only | T-19 | pass | `git diff --stat` outside `.speccen/` |

### Gate table

Self-check: done — 0 fixes

| # | Item | Result | Evidence | Verified |
|---|---|---|---|---|
| 1 | Extensions: every file in `.speccen/extensions/implementation/` listed; active ones applied | pass | [phase.md#extensions](./phase.md#extensions) — the folder does not exist; one "No extensions" row || confirmed (run 1) |
| 2 | Project conventions re-read and re-confirmed before implementation started | pass | [phase.md#conventions](./phase.md#conventions); log 20:59 before the first edit || confirmed (run 1) |
| 3 | All Implementation Plan checklist items ticked | pass | [Phase 04 plan](../phase-04-specification/phase.md#implementation-plan) — 29 items `- [x]`, five phases ✅ || confirmed (run 1) |
| 4 | All deviations documented with decisions | n/a | no deviation ([phase.md#deviations](./phase.md#deviations)); the two edits the plan did not name are explained in [phase.md#implementation-summary](./phase.md#implementation-summary) and change no wording || confirmed (run 1) |
| 5 | Each deviation states whether its phase's Why still holds | n/a | no deviation || confirmed (run 1) |
| 6 | Each phase ended with a build-and-validate step | pass | plan items 1.5, 2.4, 3.2, 4.2, 5.2 ticked; one run of the checks covers them ([phase.md#test-results](./phase.md#test-results)) || confirmed (run 1) |
| 7 | Test Plan's tests written and passing, or waived | pass | `files/phase-05-text-checks.py`; T-1 – T-19 pass; no waiver. Fix attempt after verifier run 1 (log 21:05): T-9 now checks the three guards inside the "Stop (stop condition 5) when:" bullet, as its Test Plan row states, not anywhere in the Gate test section; re-run: all pass. Repair after verifier run 2 (log 21:08, [DD-30](../delegated-decisions.md#dd-30)): T-8, T-12 and T-14 narrowed to their bullets. Repair after the stop round 05/1 (log 21:14): T-1, T-5, T-13, T-15, T-17, T-18 and the `fixes` line of T-7 narrowed to their places. Repair after the stop round 05/2 (log 21:20): T-7 compares the whole unchanged fail-safe bullet ("A `phases` entry whose name …") with the same bullet at `a7c8206`, and T-12 also finds its "stays" sentence in the base bullet. Repair after verifier run 5 (log 21:24, [DD-31](../delegated-decisions.md#dd-31)): the unchanged bullets of T-13 and T-15 and the Locks text of T-19 are read only in their sections ("Proceeding on a proposal", "Mode behaviour", "Effective settings"), and when the text a check reads is not in its place, the check fails or the script stops with an error; the move test counts both as a fail (wording corrected after verifier runs 6 and 7, log 21:28 and 21:52, [DD-32](../delegated-decisions.md#dd-32), stop round 05/3); `files/phase-05-move-test.py` moves each check's expected text, bullet or block out of its place in memory (24 cases, all 19 checks), and every case fails; on the real text T-1 – T-19 pass || confirmed (run 6) |
| 8 | Test assertions derive from the plan/contract, not the code | pass | expected strings are the plan's checklist texts and the Test Plan rows; base text read from `a7c8206` for the "unchanged" and "stays" checks (T-7, T-12, T-13, T-15, T-19) || confirmed (run 6) |
| 9 | `STATE.md` updated after each phase | pass | [STATE.md](../STATE.md) — Implementation Phase 5 complete || confirmed (run 5) |
| 10 | `index.md` lists every file this phase wrote, with status and description | pass | [index.md](../index.md) → Phase 05; `files/phase-05-text-checks.py` under files || confirmed (run 6) |
| 11 | `autonomous`: `## Delegate gate check` with evidence for every item | pass | this section || confirmed (run 8) |
| 12 | Every acceptance scenario has a passing planned test (cited) | pass | [Acceptance scenarios → tests](#delegate-gate-check) above — R-1 – R-15 || confirmed (run 6) |
| 13 | No waiver | pass | none recorded in [phase.md](./phase.md) || confirmed (run 1) |
| 14 | Delivered behaviour matches the scenarios (files and tests cited) | pass | table above, "Delivered in" column; `git diff -- . ':(exclude).speccen'` || confirmed (run 6) |
| 15 | Only the three planned files changed; changes left uncommitted (DD-24) | pass | `git diff --stat -- . ':(exclude).speccen'` → 3 files; `git status` shows them modified, not staged || confirmed (run 1) |
| 16 | No question of this phase parked with "later" is still unanswered | pass | no question asked in this phase || confirmed (run 1) |
| 17 | Every quote and line reference points at the cited text | pass | [phase.md](./phase.md): SECURITY.md quotes; log 11:05 quote; plan items and Test Plan rows quoted by id || confirmed (run 6) |

<a id="stop"></a>
## Stop — check run 3 failed more rows than check run 2 (answered)

**Answered:** the Architect said "ok, continue" (log 21:13) to 05/1, read as yes. The repair is logged after that answer; check run 4 re-checks rows 7 and 11 and the rows that cite a changed file.

**Why the delegate halts:** the three verifier runs of the accept check failed 1, 1 and then 2
rows. Run 3 failed more rows than run 2, and the breach run 2 named is still there: some checks
search a wider area than their Test Plan rows name. By the progress guard (DD-14: "stop when a
breach the run before named is still there, or when more rows fail than in the run before"),
this is a stop, not another repair. The skill text is not in question: runs 1, 2 and 3 each
confirmed that the delivered text states R-1 – R-15.

**The two failed rows:**

- **[Row 7 | Seven checks still look at a wider area than their plan rows name]** — T-1 (Keys
  row), T-5 (the absence-values bullet), T-7 (the fail-safe list), T-13 (stop condition 5 in its
  place), T-15 (compare with `a7c8206`), T-17 (the README absence values), T-18 (the self-check
  line). The row's evidence and DD-30 also overstate the repair for T-5 and T-7.
- **[Row 11 | Two log times do not match the file times]** — the entry about the corrected times
  carries a time ahead of the clock, and "plan Phase 2 complete" is earlier than the last write
  to the governing skill.

The cause is the delegate's method: after run 2 it narrowed only the checks the verifier named,
and its own move test covered only those checks. The remedy is to apply the move test to all
nineteen checks before the next run, and to write log times from the clock, not from estimates.

**Question for the Architect**

**[05/1 | May the delegate narrow all seven checks, correct the two log times and the overstated
evidence, and run the checker again on rows 7 and 11?]** — The repair: each check reads only the
row, bullet or line that its Test Plan row names; a move test runs on all nineteen checks before
the checker; log times from `date`. The other option is the current Step 7 text: reject and
revert the three skill files (Phase 05b). → Proposed: yes, repair.

<a id="stop-2"></a>
## Stop — a breach that check run 3 named is still there (answered)

**Answered:** the Architect said "ok, continue" (log 21:20) to 05/2, read as yes. The repair is logged after that answer; check run 5 re-checks rows 7 and 11 and the rows that cite a changed file.

**Why the delegate halts:** check run 4 failed rows 7 and 11, as many as run 3. Run 3 named a
breach in T-7 that the delegate did not repair: the check looks for the unchanged fail-safe line
"a key on a phase that does not take it" anywhere in the fail-safe list, in both versions. It
does not compare that bullet in its place with `a7c8206`. By the progress guard (DD-14), a breach
that the run before named and that is still there is a stop. The skill text is still not in
question: runs 1 – 4 confirmed that it states R-1 – R-15.

**The two failed rows:**

- **[Row 7 | One check still does not compare an unchanged line with the base]** — T-7: the
  bullet "A `phases` entry whose name is not one of the eight phase keys …" must equal the same
  bullet at `a7c8206`. The verifier moved the sentence into another bullet, and edited the first
  line of the bullet, and T-7 still passed.
- **[Row 11 | Two records lag behind the last repair]** — the row-7 evidence says every check
  reads only its named place (false for T-7); the text-check record in `phase.md` names the
  repairs of 21:05 and 21:08, not the repair of 21:14.

The cause: the run-3 report named this T-7 weakness in a second sentence; the delegate read
only the first one and repaired the fail-safe `fixes` line only.

**Question for the Architect**

**[05/2 | May the delegate make T-7 compare the unchanged fail-safe bullet with the base, correct
the two records, and run the checker again on rows 7 and 11?]** — The repair: T-7 compares the
whole bullet with the same bullet at `a7c8206`; the move test gains a case that changes that
bullet; the two records name the 21:14 repair and this one. The other option is the current
Step 7 text: reject and revert the three skill files (Phase 05b). → Proposed: yes, repair.

<a id="stop-3"></a>
## Stop — the corrected claim is still not true in every case (answered)

**Answered:** the Architect said "ok, continue" (log 21:52) to 05/3, read as yes. The repair is logged after that answer; check run 8 re-checks row 11.

**Why the delegate halts:** check run 7 failed row 11 on the breach that run 6 named. The
records still describe how a check behaves when its place is gone, and the description is still
wrong for two bullets: a missing Step 7 or Phase 05b bullet stops the script with an error, not
with a plain fail. By the progress guard (DD-14), a breach that the run before named and that is
still there is a stop. The scripts themselves are not in question: run 6 confirmed them with 33
independent moves, and run 7 confirmed that the move test counts an error as a fail.

**Question for the Architect**

**[05/3 | May the delegate replace the claim with one plain sentence and run the checker again on
row 11?]** — The sentence: "When the text a check reads is not in its place, the check fails or
the script stops with an error; the move test counts both as a fail." It replaces the claim in
the summary, DD-31, DD-32 and the log entries of 21:24 and 21:28. The scripts do not change. →
Proposed: yes.
