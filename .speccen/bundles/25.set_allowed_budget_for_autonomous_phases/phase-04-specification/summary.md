---
type: Summary
phase: "04 — Specification"
status: COMPLETE
phase_file: ./phase.md
description: Five-phase plan for the fixes budget; fifteen requirements, nineteen text checks; specification assembled
---

# Phase 04 Summary — Specification

[Index](../index.md) · [State](../STATE.md) · [Log](../log.md)

---

**Work completed:** gate check passed in verifier run 7 (failed rows per run 5 → 3 → 1 → 3 → 3 → 1 → 0; one stop round, answered). Also: two interview rounds (04/1; the stop round 04/2); a five-phase Implementation Plan (configuration →
gate test → Phase 05 accept → restated copies → verification); fifteen requirements with
scenarios; a Test Plan of nineteen text checks; the specification and both intent seeds.

**Outcome:** the brief's §2 change as refined by the Phase 03 decisions → [full
detail](./phase.md#implementation-plan)

**Specification (the complete, assembled spec — intent + requirements/scenarios):**
- [specification.html](./specification.html) — full, authoritative (reduced view: [specification.md](./specification.md))

**Stakeholder seeds (intent — expansion seeds, not for verbatim external sharing):**
- Executive → [doc-executive.md](./doc-executive.md)
- Business → [doc-business.md](./doc-business.md)

**Open items carried forward:** the two `MATERIAL — unconfirmed` decisions — [DD-12 | Keep the
ceiling of 3 fix attempts?] and [DD-14 | Measure progress by breaches that come back?] — for the
end-of-run review → [detail](./phase.md#open-items)

**Delegated decisions:** 6 — [DD-24 – DD-29](../delegated-decisions.md#dd-24)

**Extensions applied:** none

<a id="delegate-gate-check"></a>
## Delegate gate check

<a id="traceability"></a>
### Traceability

| Source | Scenario(s) | Test(s) |
|---|---|---|
| brief §2 / §2.3; DD-11 — the `fixes` key, its values, five phases, autonomous only, independent of `stops` | R-1 | T-2, T-3 |
| brief §3 — unchanged by default; DD-17 | R-2 | T-7 |
| brief §2.1 — fix and re-run up to the budget; re-check scope | R-3 | T-8 |
| brief §2 guard 1; DD-14 — progress by breaches | R-4 | T-9, T-10 |
| brief §2 guard 2; DD-13 — conclusions guard | R-5 | T-9 |
| brief §2 guard 3, §2.6; DD-12 — ceiling 3, invalid → `1` | R-6 | T-7, T-9 |
| brief §2.1 — log line per attempt | R-7 | T-11 |
| brief §2.1 — after a stop | R-8 | T-12 |
| brief §2.2 — stop condition 5 | R-9 | T-13 |
| DD-10 — Phase 05 accept uses the budget, rejects | R-10 | T-14, T-15 |
| brief §2.4; DD-15, DD-18 — template version 3, Keys row | R-11 | T-1, T-4, T-16 |
| brief §2.5; DD-19 — upgrade, absence values | R-12 | T-5, T-6, T-17 |
| brief §2.6 — locks | R-13 | T-19 |
| DD-16 — self-check line | R-14 | T-18 |
| DD-3, DD-20 — scope; fail-safe example stays | R-15 | T-19 |
| Architect, log 11:05: "introduce version key, should be auto while upgrading skills" | R-12 | T-5, T-6 |
| Architect, log 15:45: "I don't know how to express in simple English that have to loop until issues are fixed" | R-3, R-4, R-6 | T-8, T-9, T-10 |
| Architect, log 11:05: "feature branch, no push on main is allowed" | process, not a product requirement — met by branch `feature/set-allowed-budget-for-autonomous-phases` and DD-24 | — |
| Architect, log 11:05: "update the speccen marketplace and plugins first" | process — done at 11:06 (log) | — |
| Architect, log 11:47: the question-subject format `[INTERNAL-NUMBER \| HUMAN UNDERSTANDABLE TEXT]` | process, not a product requirement — applied to every question put to the Architect (04/1; [phase.md#interview](./phase.md#interview)); the skill change is speccen issue #26 (log 11:55), outside this scope (DD-3) | — |
| Architect, log 15:43: "don't you understand that [ autonomous + stops:proceed] means that you are on your won to decide?" | R-3, R-4, R-6 (the fix loop; in this bundle also the basis for the gate repairs, each recorded as a delegated decision) | T-8, T-9, T-10 |
| Other Architect prompts (11:31 – 11:39 remarks; 11:52, 15:31, 15:41, 20:48 stop-round answers; 15:37 "ok, continue" with no open question; 11:05 "/speccen:start" and "analyse the gh issue on speccen-ai-tools", which start the run on the issue #25 brief (traced in the brief rows above); 11:05 session-start answers, folder and name) | answers and remarks, no product requirement | — |
| Bundle ADRs | none exist | — |
| Standing decisions (4) | not affected by the change — [Phase 03 compliance](../phase-03-compliance-review/phase.md#compliance) | — |

Every R-1 – R-15 cites a source (brief, DD or log prompt) in [phase.md#requirements](./phase.md#requirements); every implementation phase's Why cites one.

### Gate table

Self-check: done — 4 fixes

| # | Item | Result | Evidence | Verified |
|---|---|---|---|---|
| 1 | Extensions: every file in `.speccen/extensions/specification/` listed; active ones applied | pass | [phase.md#extensions](./phase.md#extensions) — the folder does not exist; one "No extensions" row || confirmed (run 3) |
| 2 | Proposed changes summary lists all affected files with their change type | pass | [Proposed Changes Summary](./phase.md#implementation-plan) — 3 files, all "modify", with line references || confirmed (run 3) |
| 3 | Target-state flow as an ASCII diagram, linked to the Phase 02 diagram | pass | Target-State Execution Flow, with the link `../phase-02-code-analysis/phase.md#code-analysis` || confirmed (run 3) |
| 4 | Strategy evaluation present if multiple approaches | n/a | one approach remains after Phase 03; Strategy Evaluation paragraph || confirmed (run 3) |
| 5 | Implementation phases numbered and sequenced logically | pass | Phases 1–5; each Why names what it depends on or why it comes at its place || confirmed (run 3) |
| 6 | Every checklist item specific, actionable and traceable | pass | each item names the file, the line and the text it changes || confirmed (run 3) |
| 7 | Each phase ends with Build and Validate | pass | 1.5, 2.4, 3.2, 4.2, 5.2 || confirmed (run 3) |
| 8 | Every phase states a Why with a source; subtask Why only where non-obvious | pass | five phase Whys with sources, each says why the phase comes at its place; subtask Whys on their own line under 1.3 and 2.1, none in a checklist item || confirmed (run 3) |
| 9 | Risk mitigation table populated | pass | Risk Mitigation, 7 rows || confirmed (run 3) |
| 10 | Test Plan present (scope incl. "none, because…", behaviours, coverage intent) | pass | Test Plan — "none, because the change is prose and YAML inside Markdown"; T-1 – T-19; behaviours; coverage intent || confirmed (run 3) |
| 11 | `doc-executive.md` and `doc-business.md` written, `expandable: true` | pass | [doc-executive.md](./doc-executive.md), [doc-business.md](./doc-business.md) || confirmed (run 3) |
| 12 | Both seeds STE-styled | pass | short active sentences; one term per actor (the Architect, the delegate, the verifier); one part of speech per word: "stop", "answer" and "fix attempt" only as nouns, "halt", "reply", "correct" and "examine" as the verbs; claims agree with brief §1 and §3 || confirmed (run 3) |
| 13 | Executive seed keeps TCO out of scope | pass | "TCO / cost / budget: out of scope for this feature-level brief." || confirmed (run 3) |
| 14 | Deviations protocol stated | pass | Deviations Protocol || confirmed (run 3) |
| 15 | `specification.html` assembled (projection, STE, depth-layered) with `specification.md` | pass | [specification.html](./specification.html) L1 → L2 → L3 → decisions → requirements → plan → text checks; same word rules as the seeds, active voice; the gate diagram separates the conclusions stop from the budget/progress stop; [specification.md](./specification.md) takes its requirement texts from the html || confirmed (run 6) |
| 16 | Specification has Requirements & acceptance scenarios incl. error/edge behaviour | pass | R-1 – R-15; error paths in R-4, R-5, R-6, R-8 || confirmed (run 6) |
| 17 | Specification diagrams verified to render | pass | both SVGs parse as XML; headless Chrome screenshot of the current file checked (log 20:55; file changed 20:54:23, screenshot 20:55:34) || confirmed (run 6) |
| 18 | `summary.md` links plan, specification and both seeds | pass | this file || confirmed (run 7) |
| 19 | `index.md` lists every file this phase wrote, with current status and description | pass | [index.md](../index.md) → Phase 04 || confirmed (run 7) |
| 20 | `gated`: `STATE.md` shows `AWAITING ARCHITECT REVIEW` | n/a | Phase is `autonomous` (bundle `speccen-config.yaml`) || confirmed (run 3) |
| 21 | `autonomous`: `## Delegate gate check` with evidence for every item | pass | this section || confirmed (run 7) |
| 22 | Traceability check (Mode behaviour) | pass | [Traceability](#traceability) above || confirmed (run 7) |
| 23 | Interview: frontier only; one decision per question; who answered; DD linked both ways | pass | [phase.md#interview](./phase.md#interview) round 1 (04/1, delegate, [DD-24](../delegated-decisions.md#dd-24)); round 2, the stop round (04/2, one decision, answered by the Architect, log 20:48; no DD needed) || confirmed (run 7) |
| 24 | Every quote and line reference points at the cited text | pass | phase.md line references at `a7c8206` (`:691`, `:695`, `:707`, `:731-798`, `:857-861`, `:907-908`, `:925-926`, `:941`, `:944-946`, `:1168`, `:1176-1182`, `:1181-1182`, `:1212`, `:1249-1250`, `:416-419`; `05-implementation/SKILL.md:27-28`, `:324-325`, `:330`; `README.md:193`, `:238-305`; `ARCHITECTURE.md:142-143`); log quotes 11:05, 15:45; DD-24 quote at governing `:611` || confirmed (run 3) |
| 25 | No question parked with "later" is still unanswered | pass | none parked || confirmed (run 3) |

<a id="stop"></a>
## Stop — check run 4 made no progress (answered)

**Answered:** the Architect said "yes" (log 20:48) to 04/2. The repair is logged after that answer; check run 5 re-checks rows 15, 17 and 22 and the rows that cite a changed file.

**Why the delegate halts:** check runs 1 – 4 failed 5, 3, 1 and then 3 rows. Run 4 failed more rows
than run 3, and one of run 3's faults came back: the specification again lists the delegated
decisions without the newest one. By the progress guard of this bundle (DD-14: "stop when a breach
the run before named is still there, or when more rows fail than in the run before") and by the
limit the Architect set on the loop at 15:43, this is a stop, not another repair. It is also stop
condition 5 of the current skill text. None of the faults changes a requirement, a decision or an
answer.

**The three failed rows:**

- **[Row 15 | The specification still uses some common words in two senses]** — "once" ("at once"
  and "one time"), "so", "follow", "take", "open", "come", "last"; "do not converge" next to "make
  no progress"; one unclear "It" and one unclear "Without that"; "No bundle ADR." has no verb; the
  decision list stops at DD-26 (the fault that came back).
- **[Row 17 | The render the record cites is older than the file]** — the delegate changed one
  diagram label after the 20:29 screenshot. The verifier's own render of the current file shows
  both diagrams correctly; only the citation is wrong.
- **[Row 22 | One traceability row leaves out the newest repair]** — the 15:43 row lists DD-8,
  DD-22, DD-23 and DD-26, not DD-27.

The cause of the faults that came back is the delegate's order of work: it added a decision and
changed a label after it had written the lists and the render. The remedy is to write the decision
records and the final edits first, and the lists, the render and the summary last.

**Question for the Architect**

**[04/2 | May the delegate repair the three rows and run the checker again on rows 15, 17 and 22?]** —
The repair: reword the listed words to one sense each across the specification, name DD-27 in both
lists, render the final file after the last edit and cite that render. → Proposed: yes.
