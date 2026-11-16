---
type: Summary
phase: "04 — Specification"
status: COMPLETE
phase_file: ./phase.md
description: Four implementation phases with the exact text in Appendices A – F; 13 requirements, 19 text checks; specification assembled
---

# Phase 04 Summary — Specification

[Index](../index.md) · [State](../STATE.md) · [Log](../log.md)

---

**Work completed:** Interview 04/1 – 04/4 and stop rounds 04/5 – 04/6, 04/7 – 04/8, 04/9 – 04/10, 04/11 – 04/12 (Architect); Implementation Plan with four phases and the exact
text (Appendices A – F); Test Plan T-1 – T-19; specification and two intent seeds.

**Outcome:** The brief's rules written into the Gate test, with the unit, work order, worker
bullet and claim-source lines around it; version bumped by the CI rule →
[full detail](./phase.md#implementation-plan)

**Specification (the complete, assembled spec — intent + requirements/scenarios):**
- [specification.html](./specification.html) — full, authoritative (reduced view: [specification.md](./specification.md))

**Stakeholder seeds (intent — expansion seeds, not for verbatim external sharing):**
- Executive → [doc-executive.md](./doc-executive.md)
- Business → [doc-business.md](./doc-business.md)

**Open items carried forward:** [R-1 | Review round: manual version bump against the CI bump
(DD-10); claim-list place, form and result, `MATERIAL — unconfirmed` (DD-14, DD-20, DD-21)] →
[detail](./phase.md#open-items)

**Delegated decisions:** 4 this phase — [DD-22 – DD-25](../delegated-decisions.md#dd-22), all
`not material`.

**Extensions applied:** none

<a id="delegate-gate-check"></a>
## Delegate gate check

Self-check: done — 0 corrections (quotes scanned against `log.md` and the governing skill; edit-site line numbers re-read at `92ee62f`; ASCII loop-back aligned at column 73); verifier run 1 failed rows 10, 12 and the traceability table; fix attempt 1 of 5; run 2 failed rows 6, 12 and the traceability table — stopped, see below; after the Architect's yes (06:35), fix attempt 2 of 5 (06:37): wording split, seeds' terms, five traceability items added, DD-22 count; run 3 failed row 12 and the traceability table (new breaches, none of run 2's left — progress); fix attempt 3 of 5 (06:42): seeds' "list" / "review" / "hint" / "run" terms, R-5 result scenario, R-7 slip-row scenario, round 2 named in row 22; run 4 failed row 12 and the traceability table (new breaches, none of run 3's left, 2 items fail against 2 — progress); fix attempt 4 of 5 (06:45): business seed "takes place", "last checker run", hint defined; a scenario for every rule, DD and SHALL clause (14 added); run 5 failed row 12 and the traceability table (new breaches; run 4's gone; 2 against 2 — progress); fix attempt 5 of 5 (06:49): seed sentence split, "gate table", "rests on", "phase records"; 11 scenarios added and three corrected (R-2, R-3, R-5, R-7, R-8, R-9, R-10); T-3, T-4, T-9, T-11, T-13 extended; DD-10, DD-15, DD-16, DD-19 traced; run 6 failed rows 12, 15 and the traceability table — budget used, stopped, see the second stop below; after the Architect's yes (08:17, 04/7 – 04/8), fix attempt 6 (08:18): seed wordings, sentences split, one line per text check, six traceability details; run 7 (scope: run 6's breaches only) confirmed all 11 fixed, and named one new breach in the fix text — stopped, see the third stop below; after the Architect's yes (08:20, 04/9 – 04/10), fix attempt 7: "adds the hint"; run 8 (scope: step 6 only) confirmed the pronoun fixed and named a new breach — stopped, see the fourth stop below; after the Architect's yes (08:21, 04/11 B – 04/12), fix attempt 8: the checker's wording; run 9 (scope: that sentence only) confirmed it — gate check passed

| # | Item | Result | Evidence | Verified |
|---|---|---|---|---|
| 1 | Extensions: every file in `.speccen/extensions/specification/` in the table | pass | [phase.md#extensions](./phase.md#extensions) — no `.speccen/extensions/`; one "No extensions" row | confirmed (run 1) |
| 2 | Proposed changes summary lists all affected files with change type | pass | [phase.md → Proposed Changes Summary](./phase.md#implementation-plan) — 5 rows; each edit site anchored on text at `92ee62f`: governing 1197 – 1220, 1235 – 1238, 1390, 1409; worker **Do:**; Mode behaviour 01:245, 02:440, 03:441, 04:497, 05:336; manifests | confirmed (run 2) |
| 3 | Target-state flow as ASCII, linking the Phase 02 diagram | pass | [phase.md#target-flow](./phase.md#target-flow) — links `../phase-02-code-analysis/phase.md#behaviour` | confirmed (run 2) |
| 4 | Strategy evaluation if multiple approaches | n/a | [phase.md#strategy](./phase.md#strategy) — none; the brief fixes the approach | confirmed (run 1) |
| 5 | Phases numbered and sequenced | pass | [phase.md#phases](./phase.md#phases) — Phases 1 – 4 | confirmed (run 2) |
| 6 | Checklist items specific, actionable, traceable | pass | each item names a file and quoted anchor text or an appendix; the Appendix A, D, E text meets T-19's sentence rule (no sentence over 30 words, a code span = one word; counted after fix attempt 2); multi-rule bullets split (`slip`, `wrong`, `noticed:`, `verified` column) | confirmed (run 6) |
| 7 | Each phase ends with Build and Validate | pass | 1.3, 2.4, 3.2, 4.2 | confirmed (run 2) |
| 8 | Every phase states a Why with a source | pass | Phases 1 – 4 each cite Phase 02 anchors, the brief or DDs; subtask 1.2 has a Why (DD-11) | confirmed (run 2) |
| 9 | Risk table populated | pass | [phase.md#risks](./phase.md#risks) — 5 risks | confirmed (run 2) |
| 10 | Test Plan present (scope, behaviours incl. error/edge, coverage) | pass | [phase.md#test-plan](./phase.md#test-plan) — T-1 – T-19; error case T-14, edge T-17, unchanged-text check T-15; "none, because" row for runtime behaviour | confirmed (run 2) |
| 11 | Both seeds written, `expandable: true` | pass | [doc-executive.md](./doc-executive.md), [doc-business.md](./doc-business.md) | confirmed (run 2) |
| 12 | Seeds in STE style | pass | sentences ≤ 25 words; one term per concept: "gate check" (the whole check), "gate table" (the written table), "rests on", "checker run" (the verifier), "the delegate's own review" (the self-check), "slip", "fact"; "check" not used as a verb; a hint is not a kind of fact (step 6) | confirmed (run 9) — step 6 reads "adds a wrong fact for the problem that the hint names" (04/11 B) |
| 13 | Executive seed keeps TCO out of scope | pass | doc-executive "Scope Note" | confirmed (run 2) |
| 14 | Deviations protocol stated | pass | [phase.md#deviations-protocol](./phase.md#deviations-protocol) | confirmed (run 2) |
| 15 | `specification.html` assembled, with `specification.md` | pass | [specification.html](./specification.html), [specification.md](./specification.md) — sections What, L1, L2, L3, Decisions, Requirements, Plan, Tests, Not included; every sentence ≤ 25 words (WHEN + THEN as one); one line per text check | confirmed (run 7) |
| 16 | Specification has Requirements & acceptance scenarios (SHALL / WHEN–THEN), incl. error/edge | pass | R-1 – R-13; error/edge scenarios in R-2, R-3, R-5, R-7, R-11 | confirmed (run 2) |
| 17 | Specification diagrams verified to render | pass | both SVGs parse as XML; rendered with `qlmanage` (L1 context and L3 gate flow) — log 06:25 | confirmed (run 2) |
| 18 | `summary.md` links plan, specification and both seeds | pass | this file | confirmed (run 2) |
| 19 | `index.md` lists every bundle file this phase wrote | pass | [index.md](../index.md) — Phase 04 section, 6 files | confirmed (run 2) |
| 20 | `gated`: STATE `AWAITING ARCHITECT REVIEW` | n/a | phase is `autonomous` | confirmed (run 1) |
| 21 | `autonomous`: gate check written with evidence for every item | pass | this section | confirmed (run 2) |
| 22 | Interview: frontier, one decision per question, who answered, linked DDs | pass | [phase.md#interview](./phase.md#interview) — round 1: 04/1 – 04/4, no dependencies, DD-22 – DD-25 link back; round 2 (stop): 04/5 – 04/6 with subjects, answered by the Architect; rounds 3 – 5 (stops): 04/7 – 04/12, answered by the Architect | confirmed (run 2) |
| 23 | No question parked with "later" | pass | none answered "later" | confirmed (run 1) |
| 24 | Plan and Test Plan approved under delegation; no test waived | pass | [phase.md#outcome](./phase.md#outcome) | confirmed (run 2) |

<a id="traceability"></a>
### Traceability check

**Verified:** confirmed (run 7) — run 6's six details fixed.

| Source (`log.md` 2026-11-15 21:14 unless noted) | Scenario(s) | Test(s) |
|---|---|---|
| Rule 1 — who checks what | R-1 | T-1 |
| Rule 2 — build the claim list as you go | R-2 | T-2 |
| Rule 3 — what a claim is | R-2 | T-3 |
| Rule 4 — what goes on the list, cap 15 | R-3 | T-4, T-5 |
| Rule 5 — claim sources per phase | R-10 | T-13 |
| Rule 6 — run in parallel | R-4 | T-6 |
| Rule 7 — `slip` vs. `wrong` | R-5 | T-7 |
| Rule 8 — `noticed:` lines; the verifier reads nothing beyond its claims | R-6 | T-8 |
| Rule 9 — no verifier run | R-7 | T-9 |
| Rule 10 — later runs; rows not re-checked keep their `confirmed (run N)` | R-8 | T-9 |
| Rule 11 — filling the gate table | R-7 | T-9 |
| Rule 12 — unchanged (self-check items, `fixes` budget, stop conditions, log-line format, session model) | R-11 | T-15, T-17 |
| Work-order template (`Unit:`, `Bundle:`, `Claims:`, `Stop:`, `Outputs:`, `Return:`) | R-9 | T-11 |
| Files to change 1 (Gate test, Units, work order) | R-1 – R-9 | T-1 – T-11 |
| Files to change 2 (worker bullet, with its return format) | R-9 | T-12 |
| Files to change 3 (phase skills: claim source, Phase 04 detail, the `(governing skill → Gate test)` pointer) | R-10 | T-13 |
| Files to change 4 (version) | R-12 | T-16 |
| Acceptance — the governing skill states the split, the claim list with its cap, and exhaustive claims first | R-1, R-2, R-3 | T-1 – T-5 |
| Acceptance — the parallel launch, `slip` vs. `wrong`, the handling of `noticed:` lines | R-4, R-5, R-6 | T-6, T-7, T-8 |
| Acceptance — the `n/a` case and the later-runs rule | R-7, R-8 | T-9 |
| Acceptance — each phase skill 01 – 05 names its claim source | R-10 | T-13 |
| Acceptance — the template has `Claims:`, `Stop:` and the three-value return | R-9 | T-11 |
| Acceptance — "No skill tells the verifier to check "every row" or "every quote"." | R-11 | T-14 |
| Acceptance — "Wording: short sentences, one rule per bullet." | R-13 (two scenarios) | T-19 (sentence length by script; one rule per bullet by hand, 04/6) |
| DD-11 (after a stop, in claims; without an answer, one run follows) | R-8 | T-9 |
| DD-12, DD-13 (Phase 07, README, ARCHITECTURE unchanged) | R-11 | T-18 |
| DD-14, DD-20, DD-21 (claim list place, form, result) | R-2 (place, form), R-5 (result) | T-3, T-7 |
| DD-17 (generic template kept; verifier block directly after it) | R-9 | T-11, T-15 |
| DD-10 (manual version bump) | R-12 | T-16 |
| DD-15 (six self-check items unchanged; rule 1 as an ownership split) | R-1, R-11 | T-1, T-15 |
| DD-16 (stop triggers unchanged; a failed row has a `wrong` claim) | R-11, R-5 | T-15, T-7 |
| DD-19 (done when the Acceptance holds plus 03/2, 03/3, 03/6, 03/9, 03/10, 03/12, 03/13) | R-1 – R-13 | T-1 – T-19 |
| DD-18 (`noticed-<n>` rows) | R-6 | T-8 |
| Standing decisions (9) — no change required (Phase 03) | R-11 (kept rules) | T-15 |

Every requirement has a scenario; every scenario has a test; every R-n cites the brief or a
Phase 03 decision; each implementation phase's Why cites a source. No invented scope.

<a id="stop"></a>
## Stop — part of a problem the checker named last time is still there

Before Phase 04 can close, a checker re-reads the evidence behind the phase checklist. Run 1
said your wording requirement ("short sentences, one rule per bullet") had no scenario and no
test. Fix attempt 1 covered only the sentence length. The "one rule per bullet" half still has
neither, so a problem the last run named is still there, and the run stops (stop condition 5,
progress counted by breaches as you decided in 03/15). The budget is not used up (1 of 5), and
no problem changes a phase conclusion or a decision.

**What run 2 found**

- **[Row 6 | The planned text fails its own wording check]** — two planned sentences have more
  than 30 words (Appendix A part 2; Appendix E 04). The `slip` bullet holds three rules, and one
  `verified` column bullet holds two. The check does not say how a code span counts.
- **[Row 12 | The two intent seeds use "check" for different things]** — the executive seed uses
  "check" for the gate check, the checker run and the delegate's own review. The business seed
  uses "check" as a verb and a noun, "phase checklist" and "gate check" for the same table, and
  "small citation error" and "slip" for the same thing.
- **[Traceability | Five rules are traced to scenarios that do not cover them]** — "rows not
  re-checked keep their confirmation" (rule 10); "the verifier reads nothing beyond its claims"
  (rule 8); the `fixes` budget and log format kept (rule 12); "one rule per bullet" (wording);
  the claim list's place under the gate table (DD-14).
- Outside the rows: DD-22 still says "T-1 – T-18".

**The repair** (all recording and wording; no answer changes): split the two long sentences and
the two multi-rule bullets; make code spans count as one word; give each seed one term per
concept ("gate check", "checker run", "the delegate's own review", "slip"); add the five missing
items to R-2, R-6, R-8, R-11 and R-13 and to T-3, T-8, T-9, T-15 and T-19; update DD-22.

**Questions for the Architect** — one "yes" takes both proposed answers.

**[04/5 | May the delegate make this repair and run the checker once more?]** — The re-check
covers rows 6 and 12, the traceability table, and the rows whose evidence is in a file the repair
changes. Fix attempts 2 – 5 stay available.
→ Proposed: yes. **Architect: yes** ([log](../log.md), 2026-11-16 06:35).

**[04/6 | Should "one rule per bullet" be checked by hand, not by the script?]** — A script can
count words, but it cannot tell one rule from two. The proposal: the script checks sentence
length (at most 30 words, a code span counts as one word). In Phase 05 the main session reads
each inserted bullet and records "one rule" or the split it made, bullet by bullet.
→ Proposed: yes. **Architect: yes** ([log](../log.md), 2026-11-16 06:35).

<a id="stop-2"></a>
## Second stop — the fix budget is used up

All 5 fix attempts are used, and run 6 still fails 3 items (run 5 failed 2). Both are stop
triggers (stop condition 5: budget used; more items fail). No breach in runs 3 – 6 changes a
conclusion, a DD, the plan or the appendix text that Phase 05 will apply. Every breach is in
the wording of the intent seeds or the specification, or in how fine the traceability goes.

Each run found new breaches that the run before did not name: 2, 2, 2, 3 items, all different.
A whole-phase re-read keeps finding the next layer of detail. This is the pattern the brief
sets out to remove.

**What run 6 found**

- **[Row 12 | Two seed wordings]** — the business seed's description says "the code facts it
  rests on" (unclear "it"); line 21 calls a hint a "kind of fact" and then "outside the fact
  list".
- **[Row 15 | Specification sentences over 25 words]** — the SHALL sentences of R-1, R-2, R-3,
  R-8 and R-9, and the R-10 Phase 05 scenario; the "Text checks" section lists only IDs. Runs
  2 – 5 confirmed this same text.
- **[Traceability | Six scenario details]** — "(governing skill → Gate test)" in each phase
  bullet; the worker's return format; "without it, one run follows" in T-9; the Phase 04 claim
  detail; DD-15 also to R-1 / T-1; the template's `Unit:` and `Bundle:` lines.

**The repair** (wording and records only; no answer changes): fix the two seed wordings; split
the six long sentences; give each text check one line in the specification; add the six
details to their scenarios and checks.

**Questions for the Architect** — one "yes" takes both proposed answers.

**[04/7 | May the delegate make this repair, with one more checker run?]** — One extra attempt
beyond the budget of 5.
→ Proposed: yes.

**[04/8 | Should that run re-check only the breaches run 6 named?]** — The run would confirm
that each named breach is fixed, and would not re-read the phase for new detail. This applies
the brief's rule 10 to this run. If a fix itself is wrong, the run reports it and stops again.
→ Proposed: yes.


<a id="stop-3"></a>
## Third stop — the fix text has one new breach

Run 7 re-checked only the 11 breaches run 6 named (04/8). All 11 are fixed: row 15 and the
traceability table are confirmed. The run found one new breach in the text that fix attempt 6
wrote. Your answer to 04/8 says the run stops in that case.

**What run 7 found**

- **[Row 12 | Unclear "it" in the business seed]** — step 6 says "the delegate adds it to the
  fact list as a wrong fact". "It" can mean the hint or the conclusion.

**The repair** (one word, no answer changes): write "adds the hint to the fact list as a wrong
fact".

**Questions for the Architect** — one "yes" takes both proposed answers.

**[04/9 | May the delegate make this one-word repair, with one more checker run?]** — A second
attempt beyond the budget of 5.
→ Proposed: yes.

**[04/10 | Should that run re-check only step 6 of the business seed?]** — Same rule as 04/8: the
run confirms the named breach and the changed sentence, nothing else.
→ Proposed: yes.

<a id="stop-4"></a>
## Fourth stop — the checker reads the new sentence as making a hint a fact

Run 8 re-checked only step 6 of the business seed (04/10). The unclear "it" is gone. The run
then named a new breach: "the delegate adds the hint to the fact list as a wrong fact" makes the
hint itself a fact.

**A note on the evidence.** The rule "a hint is not a kind of fact" comes from run 6's finding,
and the work order for run 8 stated it as a check. The specification says a promoted hint
*becomes* a `wrong` claim (R-6, "A hint affects a conclusion"). So the current wording matches
the specification, and the checker's reading is arguable. The checker's own suggestion is
clearer, and it matches R-6 too.

**Questions for the Architect** — one "yes" takes both proposed answers.

**[04/11 | Which wording should step 6 use?]**
- A: keep "adds the hint to the fact list as a wrong fact" (it matches R-6), and count row 12 as
  confirmed.
- B: use the checker's wording, "the delegate adds a wrong fact for the problem that the hint
  names", with one more checker run.
→ Proposed: B.

**[04/12 | If B, should that run re-check only that one sentence, with no further fix attempt?]**
— If it fails again, the run stops and you choose the wording directly.
→ Proposed: yes.
