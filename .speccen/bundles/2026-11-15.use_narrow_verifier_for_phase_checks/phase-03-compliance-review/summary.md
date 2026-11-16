---
type: Summary
phase: "03 — Compliance & Review"
status: COMPLETE
phase_file: ./phase.md
description: Definition of Ready met — compliant with nine standing decisions; reach, claim-list place, template place and the version bump settled in the interview
---

# Phase 03 Summary — Compliance & Review

[Index](../index.md) · [State](../STATE.md) · [Log](../log.md)

---

**Work completed:** Iteration 1 — nine standing decisions checked; interview rounds 1 – 3
(03/1 – 03/13) settled Phase 01 H-1, H-3 – H-5 and Phase 02 C-1 – C-5.

**Outcome:** Definition of Ready satisfied → [full detail](./phase.md#compliance) ·
[Definition of Ready](./phase.md#ready)

**ADRs in scope:** 9 standing, 0 bundle → [table](./phase.md#adrs)
**Open items carried forward:** O-4 acceptance scenarios (Phase 04); [R-1 | Review round: manual version bump against the CI bump (DD-10); claim-list place, form and result, `MATERIAL — unconfirmed` (DD-14, DD-20, DD-21)] → [detail](./phase.md#open-items)

**Delegated decisions:** 13 this phase — [DD-9 – DD-21](../delegated-decisions.md#dd-9); three
`MATERIAL — unconfirmed` (DD-14, DD-20, DD-21).

**Extensions applied:** none

<a id="delegate-gate-check"></a>
## Delegate gate check

Verifier run 1 failed rows 3, 6, 16 (log 21:39); fix attempt 1 of 5 applied; run 2 (2026-11-16 01:10) failed rows 3, 16; fix attempt 2 of 5 applied; run 3 (06:12) failed rows 3, 7, 9 — stopped, see below; the Architect answered 03/14 – 03/15; fix attempt 3 applied; run 4 (06:19) re-checked rows 3, 7, 9 (scope set by 03/14): confirmed. Self-check: done — 3 corrections (two quotes not word for word: the after-a-stop sentence in 03/3, the brief's template line in 03/9 and DD-17)

| # | Item | Result | Evidence | Verified |
|---|---|---|---|---|
| 1 | Extensions: every file in `.speccen/extensions/compliance-review/` is in the table; active ones applied | pass | [phase.md#extensions](./phase.md#extensions) — no `.speccen/extensions/` folder; one "No extensions" row | confirmed (run 3) |
| 2 | Every ADR file has a compliance response appended within it | pass (vacuous) | `adrs/` is empty; standing decisions checked in [phase.md#compliance](./phase.md#compliance) | confirmed (run 3) |
| 3 | All open questions resolved or explicitly escalated | pass | [phase.md#ready](./phase.md#ready) row 2 maps every H-n, C-n and O-1 – O-4 to its answer | confirmed (run 4) |
| 4 | Affected phase files updated to reflect ADR constraints | n/a | no bundle ADR; standing decisions need no change to Phases 01 – 02 ([phase.md#compliance](./phase.md#compliance) "Analysis updates this iteration: none") | confirmed (run 3) |
| 5 | Domain understanding deepened where ADRs indicate | n/a | no bundle ADR; the interview settled the open items instead | confirmed (run 3) |
| 6 | `phase.md` opens with the ADR table, current | pass | [phase.md#adrs](./phase.md#adrs) — first section; 9 standing rows, matching the 9 files in `.speccen/decisions/` | confirmed (run 3) |
| 7 | Definition of Ready evaluated against all eight criteria | pass | [phase.md#ready](./phase.md#ready) rows 1 – 8 | confirmed (run 4) |
| 8 | Prototypes: records, worktrees removed, no code in the tree | n/a | no prototype; `prototypes: 0` in `.speccen/speccen-config.yaml` | confirmed (run 1) |
| 9 | `summary.md` written and links back to the phase file | pass | this file — `./phase.md#compliance`, `#ready`, `#adrs`, `#open-items` | confirmed (run 4) |
| 10 | `index.md` lists every bundle file this phase wrote | pass | [index.md](../index.md) — Phase 03 section | confirmed (run 1) |
| 11 | `gated`: `STATE.md` reflects `AWAITING ARCHITECT REVIEW` | n/a | Phase is `autonomous` (bundle config) | confirmed (run 1) |
| 12 | `autonomous`: `## Delegate gate check` written with evidence for every item | pass | this section | confirmed (run 3) |
| 13 | Mode behaviour: at most two iterations | pass | one iteration ([phase.md#compliance](./phase.md#compliance)) | confirmed (run 3) |
| 14 | Mode behaviour: no `status: PENDING` placeholder ADR remains | pass | `adrs/` is empty | confirmed (run 1) |
| 15 | Mode behaviour: no conflict between ADRs, or an ADR and the brief; no Tier-2 override needed | pass | [phase.md#compliance](./phase.md#compliance) — all nine `compliant`; [phase.md#interview](./phase.md#interview) closing paragraph on 03/2 | confirmed (run 3) |
| 16 | Interview: whole frontier per round, one decision per question, reference, dependencies, who answered, linked DD both ways | pass | [phase.md#interview](./phase.md#interview) Round 1 (03/1 – 03/10, no dependencies), Round 2 (03/12, 03/13, each depends on 03/6), Round 3 (03/11, depends on 03/2, 03/3, 03/6, 03/9, 03/10, 03/12, 03/13); Round 4 — stop round (03/14, 03/15, answered by the Architect); DD-9 – DD-21 link `03/n` | confirmed (run 3) |
| 17 | No question parked with "later" | pass | [phase.md#interview](./phase.md#interview) — "No question was answered "later"." | confirmed (run 3) |

<a id="stop"></a>
## Stop — the checker failed more rows than the time before (answered)

**Answered:** the Architect said "yes" to 03/14 and 03/15 (log 06:19). Fix attempt 3 corrected the three records; verifier run 4 re-checks rows 3, 7 and 9 only; progress counts breaches only.

Before Phase 03 can close, a checker re-reads the evidence behind the phase checklist. Run 2
failed 2 rows; after the fix, run 3 failed 3 rows (rows 3, 7 and 9). The skill stops a run when
"more rows fail than in the run before", so the run stops here. The fix budget is not used up
(2 of 5 attempts), and no problem changes a conclusion or a decision.

**What the checker found** — all three are records that fix attempt 2 left behind; each is a
recording repair (standing decision `2026-11-15.record_repair_is_not_a_stop`):

- **[Row 3 | The question map misses one question]** — the Definition of Ready says H-4 and C-3
  are settled by 03/6 and 03/12; it must also name 03/13, which fix attempt 2 split out.
- **[Row 7 | The readiness evidence names too few rounds]** — it says "Round 1 and 2 cover every
  open item"; 03/11 is now in round 3. Same missing 03/13 as row 3.
- **[Row 9 | The summary miscounts the rounds]** — it says "rounds 1 – 2 (03/1 – 03/13, rounds
  1 – 3)"; it must say "rounds 1 – 3 (03/1 – 03/13)".

**Why this is a question for you:** by breaches, the run made progress — run 2 named 6 breaches
in rows 3 and 16, all fixed; run 3 names 3 new ones. Your standing decision
`2026-11-11.fix_progress_by_breaches` says progress is measured by breaches, not by failed rows.
The skill text still also says "or more rows fail than in the run before". The two disagree here.

**Questions for the Architect** — one "yes" takes both proposed answers.

**[03/14 | May the delegate fix the three records and run the checker once more?]** — The fix
corrects only the three records above. The re-check covers rows 3, 7 and 9 only: no other row
cites the changed text. Fix attempts 3 – 5 stay available.
→ Proposed: yes.

**[03/15 | Should progress count breaches, not failed rows, for the rest of this run?]** — Your
standing decision says breaches. The skill text says "a rule breach the run before named is
still there, or more rows fail than in the run before". With breaches, this run would not have
stopped.
→ Proposed: yes — breaches only, as the standing decision says.

