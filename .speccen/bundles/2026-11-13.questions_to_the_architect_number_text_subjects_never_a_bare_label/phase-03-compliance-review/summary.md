---
type: Summary
phase: "03 — Compliance & Review"
status: COMPLETE
phase_file: ./phase.md
description: Definition of Ready met — the rule's reach, form and place decided under delegation, fourteen material answers wait for the Architect; stop condition 5 narrowed by the Architect
---

# Phase 03 Summary — Compliance & Review

[Index](../index.md) · [State](../STATE.md) · [Log](../log.md)

---

**Work completed:** two iterations. Iteration 1: the seven standing decisions checked (no
bundle ADR); the open items of Phases 01 and 02 settled in an interview answered under
delegation (autonomous, `stops: proceed`). Iteration 2, after a stop: the Architect added the
narrowing of stop condition 5 to the scope and applied it to this run (03/16, log 07:32); the
interview was re-recorded under it — questions split one per decision, rounds corrected, every
answer kept.

**Outcome:** Definition of Ready satisfied. The rule is stated once at the end of Structured
questions; it points from the brief's places (§2.2 – §2.5), the `stops: proceed` open item, the
resume summary, the interview's closing summary, the Phase 05 completion notice, the `STATE.md`
stop line and the reconcile report; record tables, the Retrospective's findings and the
fix-attempt log line stay outside; the self-check gets a sixth item; `README.md` mentions the
form; and stop condition 5 stops only on a fix that changes what a decision decides →
[full detail](./phase.md#analysis-updates)

**ADRs in scope:** 7 standing, 0 bundle → [table](./phase.md#adrs)

**Extensions applied:** none

**Delegated decisions:** 19 in this phase (DD-9 – DD-27), 15 of them `MATERIAL — unconfirmed` (DD-19 and DD-26 hold the
same README decision); five repaired in iteration 2 and DD-19 again after stop 2, each with a Repair row → [delegated-decisions.md](../delegated-decisions.md)

**Stop 2 (answered):** [stop 2](#stop-2) — [03/22 \| May the delegate repair rows 7, 16 and 17 with record-only fixes …?] and [03/23 \| For the rest of this run, does an answered stop allow the phase's full fix budget again …?] — Architect: "continue?" (log 2026-11-15 20:08), read as yes. Repaired as fix attempts 1 – 3 of 5.

**Stop 1 (answered):** [the stop](#stop) put [03/13 \| May the delegate re-record the Phase 03
interview …, keeping every answer as it stands?] (03/14 and 03/15 with it); the Architect then asked the question that became 03/16, since split into [03/16 \| Does the narrowing of stop
condition 5 join this bundle's scope?] and [03/24 \| Does the narrowed stop condition 5 apply to this run from now on, before the skill text changes in Phase 05?] — Architect: "include and apply
this immediately in this refactoring" (log 07:32). 03/14 and 03/15 were answered under delegation.

**Open items carried forward** → [detail](./phase.md#open-items)

- [O-4 | What are the acceptance scenarios — when is this done?] Now including the narrowed stop
  condition 5. → Phase 04
- [O-8 | Fourteen material answers taken under `stops: proceed` wait for the Architect] —
  [03/2 | rule stated once], [03/3 | record tables outside], [03/4 | sixth self-check item],
  [03/5 | `stops: proceed` open item], [03/6 | reconcile report covered], [03/7 | Retrospective
  findings outside], [03/8 | `AskUserQuestion` question text covered], [03/9 | audit and code
  interviews through the template], [03/14 | `README.md` mention], [03/17 | resume summary],
  [03/18 | closing summary], [03/19 | Phase 05 completion notice], [03/20 | `STATE.md` stop
  line], [03/21 | fix-attempt log line outside] → the review round after the run

<a id="delegate-gate-check"></a>
## Delegate gate check

Self-check: done — 0 corrections (run 1); done — 3 corrections before run 2 (the material count in phase.md made fourteen; DD-16's basis without H-3; the O-subjects made the same as Phase 02's); done — 0 corrections before run 3; done — 0 corrections before run 4; done — 0 corrections before run 5

| # | Item | Result | Evidence | Verified |
|---|---|---|---|---|
| 1 | [1 \| Extensions: every file in `.speccen/extensions/compliance-review/` is in the table; active ones applied] | pass | [phase.md#extensions](./phase.md#extensions) — `.speccen/extensions/` does not exist; one "No extensions" row | confirmed (run 1) |
| 2 | [2 \| Every ADR file has a compliance response appended within it] | pass | the bundle's `adrs/` holds no ADR file; [phase.md#compliance](./phase.md#compliance) | confirmed (run 2) |
| 3 | [3 \| All open questions are resolved or explicitly escalated] | pass | [phase.md#compliance](./phase.md#compliance) open-items table: O-1, O-2, O-3, O-6, O-7 and the kind settled by 03/1 – 03/21; every question 03/1 – 03/24 answered (03/13, 03/16, 03/22 – 03/24 by the Architect); O-4 to Phase 04; O-8 to the review round | confirmed (run 5) |
| 4 | [4 \| Affected phase files are updated to reflect ADR constraints] | n/a | no bundle ADR; no standing decision requires a change ([phase.md#compliance](./phase.md#compliance)) | confirmed (run 1) |
| 5 | [5 \| Domain understanding deepened where ADRs indicate it is needed] | pass | [phase.md](./phase.md) → Domain understanding (the `\|` escape in tables); no ADR asked for more | confirmed (run 1) |
| 6 | [6 \| `phase.md` opens with the ADR table, current after the last iteration] | pass | [phase.md#adrs](./phase.md#adrs) — 7 standing decisions, first section under the navigation bar | confirmed (run 2) |
| 7 | [7 \| Definition of Ready evaluated against all eight criteria] | pass | [phase.md#outcome](./phase.md#outcome) — eight rows with evidence | confirmed (run 3) |
| 8 | [8 \| Every prototype run has a record and its worktree was removed] | n/a | no prototype run; `prototypes: 0` (project config) | confirmed (run 1) |
| 9 | [9 \| `summary.md` is written and links back to the phase file] | pass | this file — links to `./phase.md#compliance`, `#adrs`, `#open-items` | confirmed (run 3) |
| 10 | [10 \| `index.md` lists every bundle file this phase wrote, with current status and description] | pass | [index.md](../index.md) → Phase 03; `delegated-decisions.md` in Bundle Control | confirmed (run 4) |
| 11 | [11 \| `gated` only: `STATE.md` reflects `AWAITING ARCHITECT REVIEW`] | n/a | the phase is `autonomous` (bundle `speccen-config.yaml`) | confirmed (run 1) |
| 12 | [12 \| `autonomous`: this gate check is written with evidence for every item] | pass | this section | confirmed (run 3) |
| 13 | [13 \| `autonomous`: no `status: PENDING` placeholder ADR remains] | pass | the bundle's `adrs/` holds no ADR file | confirmed (run 2) |
| 14 | [14 \| `autonomous`: at most two iterations] | pass | two iterations ([phase.md#compliance](./phase.md#compliance) → Iteration 1, Iteration 2) | confirmed (run 2) |
| 15 | [15 \| `autonomous`: no conflict between ADRs, or with the brief, and no standing decision overridden] | pass | [phase.md#compliance](./phase.md#compliance) — standing-decision table: no divergence | confirmed (run 2) |
| 16 | [16 \| Interview: each round holds the whole frontier, one decision per question, with reference, dependencies and who answered; every delegate answer is a linked DD] | pass | [phase.md#interview](./phase.md#interview) Round 1 (03/1 – 03/4, 03/8, 03/12, 03/14, 03/15 — no dependencies), Round 2 (03/5 – 03/7, 03/9, 03/10, 03/17 – 03/21, each on 03/2 and/or 03/3), Rounds 3 – 5 first stop (03/16; 03/24 on 03/16; 03/13 on 03/24 — Architect), Round 6 second stop (03/22 on 03/24, 03/23 — Architect); 03/11 under [Replaced questions](./phase.md#replaced-questions); [delegated-decisions.md](../delegated-decisions.md) DD-9 – DD-27, each linking its `03/n` | confirmed (run 5) |
| 17 | [17 \| Every material answer the basis does not decide is marked `MATERIAL — unconfirmed` and listed as an open item] | pass | DD-10 – DD-17, DD-19, DD-21 – DD-26 (`MATERIAL — unconfirmed`); [phase.md#open-items](./phase.md#open-items) O-8 lists all fourteen questions; DD-19 holds the same README decision as DD-26 (03/14) | confirmed (run 3) |
| 18 | [18 \| No question parked with "later" is still unanswered for this phase] | pass | [phase.md#interview](./phase.md#interview) "No question was answered "later"." | confirmed (run 2) |


<a id="stop"></a>
## Stop — repairing the interview would change delegated decisions

**Answered:** the Architect said "include and apply this immediately in this refactoring" (log
07:32), after asking "What needs to be changed so you would not stop here in a [autonomous +
proceed] mode?" (log 07:29). Read as: yes to 03/13, and stop condition 5 narrowed (03/16, see
[phase.md#scope-addition](./phase.md#scope-addition)) for this bundle and this run. 03/14 and
03/15 were then answered under delegation (`stops: proceed`), as stop condition 1 allows.

The checker confirms 16 of 18 rows. Two fail:

- [Row 16 | Does each round hold its whole frontier, with one decision per question?] — three
  questions (03/8 `AskUserQuestion`, 03/11 README, 03/12 label list) do not depend on 03/2 and
  belonged in round 1; three questions hold more than one decision: 03/5 (five places), 03/7
  (Retrospective findings and the fix-attempt log line), 03/11 (`README.md` and
  `ARCHITECTURE.md`).
- [Row 17 | Is every material answer the basis does not decide marked `MATERIAL — unconfirmed`?]
  — the README mention (03/11) adds something the brief does not ask for, so it is material by
  this phase's own reading, and the brief does not decide it; it is marked `not material`.

The repair splits questions into new delegated decisions and changes one decision's materiality.
A fix that changes a delegated decision is a stop (stop condition 5). No answer changes: every
split question keeps the answer it has now.

**Stop round**

**[03/13 | May the delegate re-record the Phase 03 interview — 03/8 and 03/12 moved into round 1,
and 03/5 and 03/7 split into one question per place — keeping every answer as it stands?]** The
split questions stay `MATERIAL — unconfirmed` and go to the review round.
→ Proposed: yes.

**[03/14 | Should `README.md` mention the subject form in its autonomous-mode section, where it
describes the stop round and the review round?]** The brief does not ask for it; Phase 02 found
that the README describes those messages to the Architect (`README.md:217-231`).
→ Proposed: yes.

**[03/15 | Should `ARCHITECTURE.md` stay unchanged?]** It describes the interview skill, not the
messages (`ARCHITECTURE.md:76-81`).
→ Proposed: yes.

03/14 and 03/15 replace 03/11. *(Corrected after the second stop: under `stops: proceed` both were answered under delegation; 03/14 is `MATERIAL — unconfirmed` and waits for the review round.)*

Lean: yes to all three. Evidence: [phase.md#interview](./phase.md#interview),
[delegated-decisions.md](../delegated-decisions.md) (DD-13, DD-15, DD-19).


<a id="stop-2"></a>
## Stop 2 — three rows still fail after the re-recording

The checker (run 2) confirms eleven re-checked rows. Three fail; every fix is a record repair
that keeps all answers:

- [Row 7 | Does the Definition of Ready name every passage to change?] — two places that restate
  stop condition 5 are missing: `skills/sdd/05-implementation/SKILL.md:326` ("If the next fix
  would change a phase conclusion, a delegated decision or an ADR, stop.") and the config comment
  "It stops sooner when a repair makes no progress or would change a conclusion." at
  `skills/sdd/00-governing-workflow/SKILL.md:750`, copied in `README.md:254`.
- [Row 16 | Does each round hold its frontier, one decision per question, each answer in an
  allowed form?] — 03/11 was kept whole in round 2 and marked "replaced"; the stop round lists
  03/14 and 03/15 in one row; 03/16 holds two decisions (scope, and this run).
- [Row 17 | Is every material answer marked `MATERIAL — unconfirmed`?] — DD-19 still says
  `not material` for the README half that DD-26 now holds.

Two of these (03/11 in round 2, DD-19's materiality) were named by the run before, so the
no-progress rule applies; and the answer at 07:32 did not set further fix attempts, so the
default — "one run, and a failing row stops again" (`gov :1210-1212`) — applies too.

**Stop round**

**[03/22 | May the delegate repair rows 7, 16 and 17 with record-only fixes, within the phase's
fix budget, stopping only on a fix that changes what a decision decides?]** The fixes: name the
two missing passages; record 03/11 as replaced in its own answer form and move the replacement
note out of round 3; split 03/16 into its two decisions with the Architect's same answer; raise
DD-19 to `MATERIAL — unconfirmed`, noting that DD-26 holds the same decision.
→ Proposed: yes.

**[03/23 | For the rest of this run, does an answered stop allow the phase's full fix budget again,
unless the answer says otherwise?]** Today's default after a stop is one checker run; it is what
makes this second stop. This applies to this run only; making it part of speccen would be a
scope question of its own.
→ Proposed: yes.

Lean: yes to both.

**Answered:** Architect, "continue?" (log 2026-11-15 20:08) — read as yes to 03/22 and 03/23. Repaired as fix attempts 1 – 3 of 5.
