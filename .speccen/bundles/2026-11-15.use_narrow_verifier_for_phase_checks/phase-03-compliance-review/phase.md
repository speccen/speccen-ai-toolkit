---
type: Phase
phase: "03 — Compliance & Review"
status: COMPLETE
description: No bundle ADR; nine standing decisions are compatible; the interview settles kind, version bump, reach, claim-list place, template place and the noticed-line answer — Definition of Ready met
---

<a id="phase-top"></a>
# use narrow verifier for phase checks — Compliance & Review

[Index](../index.md) · [State](../STATE.md) · [Log](../log.md)

---

<a id="adrs"></a>
## ADRs in scope

| ADR | Tier | Status | Decision | Compliance |
|---|---|---|---|---|
| `.speccen/decisions/2026-11-05.bundle_store_lookup_unit.md` | standing | DECIDED (active) | A search unit covers code (Phases 02 – 05) and the bundle and store (any phase that interviews) | compliant |
| `.speccen/decisions/2026-11-05.code_search_agent.md` | standing | DECIDED (active) | A code-search unit runs on `speccen-worker`, launched with the phase tier's model | compliant |
| `.speccen/decisions/2026-11-05.code_search_tier.md` | standing | DECIDED (active) | Code searches share the phase's `model` tier | compliant |
| `.speccen/decisions/2026-11-05.self_check_interview_structure.md` | standing | DECIDED (active) | The self-check item "every round holds only the frontier, and every question one decision" | compliant |
| `.speccen/decisions/2026-11-11.fix_budget_ceiling_10.md` | standing | DECIDED (active) | `fixes` takes `1` – `10` | compliant |
| `.speccen/decisions/2026-11-11.fix_progress_by_breaches.md` | standing | DECIDED (active) | "No progress" is measured by breaches, not by the count of failed rows | compliant |
| `.speccen/decisions/2026-11-12.fix_budget_default_5.md` | standing | DECIDED (active) | With no `fixes` set, up to 5 fix attempts | compliant |
| `.speccen/decisions/2026-11-15.labels_travel_inside_subjects.md` | standing | DECIDED (active) | Anything put to the Architect carries `[number \| text]` subjects; records keep their form | compliant |
| `.speccen/decisions/2026-11-15.record_repair_is_not_a_stop.md` | standing | DECIDED (active) | Correcting a citation (and other recording repairs) is not a conclusion change under stop condition 5 | compliant |

No bundle ADR exists in `adrs/`. The **Decision** column paraphrases each entry's **What** row,
because store entries carry no `description` field.

<a id="extensions"></a>
## Extensions applied

| Extension | Why | Where it applies | Outcome |
|---|---|---|---|
| — | — | — | No extensions for this phase |

<a id="compliance"></a>
## Compliance Iterations

### Iteration 1 — 2026-11-15

No bundle ADR was added, so no ADR compliance response is due. The analysis was checked against
each standing decision:

| Standing decision | What the brief does to it | Compliance |
|---|---|---|
| `self_check_interview_structure` | Rule 12 keeps "the six self-check items"; the item stays | compliant |
| `fix_progress_by_breaches` | Rule 12 keeps the stop conditions. A `slip` is not a failed row (rule 7), so it is not a breach that a later run can "still" name; a `wrong` claim is a breach | compliant |
| `record_repair_is_not_a_stop` | Already names "correcting a citation" as a recording repair. Rule 7 goes one step further: a `slip` also costs no fix attempt and no re-run. It narrows when a fix is needed; it does not widen what a fix may change | compliant |
| `fix_budget_ceiling_10`, `fix_budget_default_5` | Rule 12 keeps the `fixes` budget | compliant |
| `code_search_agent`, `code_search_tier`, `bundle_store_lookup_unit` | The verifier stays a separate unit on the session model (rule 12); searches are untouched | compliant |
| `labels_travel_inside_subjects` | The verifier's return and the gate table are records and keep their form. Any stop round this change produces carries subjects | compliant |

Analysis updates this iteration: none to Phases 01 or 02. The interview below settles the open
items C-1 – C-5 (Phase 02) and H-1, H-3 – H-5 (Phase 01); H-2 was confirmed in Phase 02.

<a id="interview"></a>
## Interview

Mode: `autonomous` (bundle config); `stops: proceed` (project config). Basis: the brief (log
21:14) and the session-start answers (log 21:10) — the Architect's own words; the project
conventions confirmed in Phase 02; the standing decisions above. Basis order (governing skill →
Decision basis): ADRs, then the Architect's words, then conventions.

**Round 1** — no question depends on another.

| # | Question | Depends on | Proposed | Answer |
|---|---|---|---|---|
| 03/1 | Kind — confirm the kind as refactoring (H-1)? No new config key and no new artifact file are introduced; the change restructures an existing check. | — | yes — refactoring | delegate: refactoring, confirmed — basis: session-start Work kind "refactoring" (log 21:10); the brief's "Files to change" lists only existing files and no config key (log 21:14) — [DD-9](../delegated-decisions.md#dd-9) |
| 03/2 | Version bump — follow the brief's item 4 and bump `plugin.json` and `marketplace.json` by hand, although CI bumps on every push to `main` (C-1)? | — | yes — bump by hand, as the brief says; flag the CI double bump in the review round | delegate: bump by hand to the next `YY.MDD.N` — basis: brief "Bump the version in `.claude-plugin/plugin.json` and `marketplace.json`" (log 21:14) ranks above the observed CI convention — [DD-10](../delegated-decisions.md#dd-10) |
| 03/3 | After-a-stop paragraph — restate it in claims (the Architect's answer sets which claims the next run re-checks; the verifier reports on every listed claim), so it no longer says a verifier "lists every rule breach it finds in that row at once" (C-2)? | — | yes | delegate: restate in claims — basis: brief rule 10 and Acceptance "the later-runs rule"; governing 1235 – 1238 would contradict rule 10 otherwise — [DD-11](../delegated-decisions.md#dd-11) |
| 03/4 | Phase 07 — leave its gate-row spot-check unchanged (C-2)? It re-verifies a row's cited evidence, which still works for every row value. | — | yes — unchanged | delegate: unchanged — basis: brief "Files to change" lists no Phase 07 edit; 07: 134 – 136 does not describe the verifier — [DD-12](../delegated-decisions.md#dd-12) |
| 03/5 | README and ARCHITECTURE — leave them unchanged (H-3)? They mention only that the verifier runs on the session model, which rule 12 keeps. | — | yes — unchanged | delegate: unchanged — basis: brief rule 12; Phase 02 [architecture](../phase-02-code-analysis/phase.md#architecture) (README 269, 343; ARCHITECTURE 158) — [DD-13](../delegated-decisions.md#dd-13) |
| 03/6 | Claim-list place — record the claims in the phase `summary.md`, under `## Delegate gate check`, as a `Claims` list directly under the gate table (H-4, C-3)? | — | yes | delegate: as proposed — basis: brief rule 2 ("At the gate the list already exists."); the gate table already lives in `summary.md` — [DD-14](../delegated-decisions.md#dd-14), `MATERIAL — unconfirmed` |
| 03/7 | Self-check remit — keep the six items unchanged, and state rule 1 as an ownership split, not as a new item (H-5, C-4)? Item 2 (References) may still re-open code a row cites; that is the delegate's own pass, not the independent check. | — | yes | delegate: as proposed — basis: brief rules 1 and 12; standing decision `self_check_interview_structure` — [DD-15](../delegated-decisions.md#dd-15) |
| 03/8 | No-progress wording — keep stop trigger 3 as written ("a rule breach the run before named is still there, or more rows fail than in the run before"), with a failed row meaning a row with a `wrong` claim (C-5)? | — | yes | delegate: as proposed — basis: brief rule 12 (stop conditions unchanged), rules 7 and 11; standing decision `fix_progress_by_breaches` — [DD-16](../delegated-decisions.md#dd-16) |
| 03/9 | Template place — keep the generic work-order template for every other unit, and add the verifier template as a second block directly after it? | — | yes | delegate: as proposed — basis: brief, "Files to change" item 1, which puts "the template above" under Subagent Execution → The worker and the work order; the Search unit's own fields are the precedent (Phase 02 [patterns](../phase-02-code-analysis/phase.md#patterns)) — [DD-17](../delegated-decisions.md#dd-17) |
| 03/10 | `noticed:` answers — answer each `noticed:` line as one extra row at the foot of the gate table, `noticed-<n> \| <the line> \| corrected / not relevant, because … \| <evidence> \| —`? | — | yes | delegate: as proposed — basis: brief rule 8 "The delegate answers each one in the gate table" — [DD-18](../delegated-decisions.md#dd-18) |

**Round 2** — the frontier after round 1.

| # | Question | Depends on | Proposed | Answer |
|---|---|---|---|---|
| 03/12 | Claim-line form — write each claim in the brief's form `id · claim · how to check · expected`, with the id `K-<n> (row <N>)` so rule 11 can map rows to claims (`C-` is taken by Phase 02 open items)? | 03/6 | yes | delegate: as proposed — basis: brief rules 3 and 11 (log 21:14) — [DD-20](../delegated-decisions.md#dd-20), `MATERIAL — unconfirmed` |
| 03/13 | Claim result — append each claim's run result to its own line, after `→` (`confirmed (run N)`, `slip — <correct value>`, `wrong — <actual value>`)? | 03/6 | yes | delegate: as proposed — basis: brief rules 7 and 11 (log 21:14); split out of 03/12 by fix attempt 2 — [DD-21](../delegated-decisions.md#dd-21), `MATERIAL — unconfirmed` |

**Round 3** — 03/11 depends on 03/12 and 03/13. Fix attempt 2 moved it here from round 2 and
named 03/12 and 03/13 in it: before the split, 03/6 held the place, the line form and the result,
so DD-19 already covered them. The scope of DD-19 is unchanged — a recording repair.

| # | Question | Depends on | Proposed | Answer |
|---|---|---|---|---|
| 03/11 | Done when — the brief's Acceptance list, plus: the after-a-stop paragraph speaks of claims (03/3), the claim list has its place (03/6), its line form (03/12) and its result (03/13), the verifier template sits beside the generic one (03/9), `noticed:` answers have their row form (03/10), and both manifests carry the bumped version (03/2)? | 03/2, 03/3, 03/6, 03/9, 03/10, 03/12, 03/13 | yes, for Phase 04 to turn into scenarios | delegate: as proposed — carried to Phase 04 (O-4) — [DD-19](../delegated-decisions.md#dd-19) |

No question was answered "later". Three delegated decisions are `MATERIAL — unconfirmed` — DD-14,
DD-20 and DD-21: together they add the claim list to the bundle's data model; `stops: proceed`
lets the run carry on, and the review round puts them to the Architect. No conflict between basis sources: the brief and the CI
convention differ on the version bump (03/2), but a convention ranks below the Architect's words,
so this is not stop condition 2 (ADR against ADR or against the brief).

**Round 4 — stop round** (stop condition 5: run 3 failed more rows than run 2) — see
[summary → Stop](./summary.md#stop).

| # | Question | Depends on | Proposed | Answer |
|---|---|---|---|---|
| 03/14 | [03/14 \| May the delegate fix the three records and run the checker once more?] — re-check rows 3, 7, 9 only; attempts 3 – 5 stay available | — | yes | Architect: "yes" (log 06:19) |
| 03/15 | [03/15 \| Should progress count breaches, not failed rows, for the rest of this run?] — standing decision `fix_progress_by_breaches` vs. the skill's "more rows fail" | — | yes — breaches only | Architect: "yes" (log 06:19) |

<a id="ready"></a>
## Definition of Ready

| # | Criterion | Met | Evidence |
|---|---|---|---|
| 1 | Every ADR file has a compliance response appended within it | yes (vacuous) | `adrs/` is empty; standing decisions checked under [#compliance](#compliance) |
| 2 | All open questions from Phases 01 and 02 resolved or escalated | yes | H-1 → 03/1; H-2 confirmed in Phase 02; H-3 → 03/3, 03/4, 03/5; H-4 → 03/6, 03/12, 03/13; H-5 → 03/7; C-1 → 03/2; C-2 → 03/3, 03/4, 03/5; C-3 → 03/6, 03/12, 03/13; C-4 → 03/7; C-5 → 03/8; O-1 – O-3 through H-1 – H-5, C-5 (03/8) and P02-1 – P02-5; O-4 → 03/11 and Phase 04 |
| 3 | Project Conventions Confirmation exists and is complete | yes | [Phase 02 #conventions](../phase-02-code-analysis/phase.md#conventions) |
| 4 | Domain understanding sufficient for a phase-structured plan | yes | every edit site is located by file and line in Phase 02 [#architecture](../phase-02-code-analysis/phase.md#architecture) and [#known-issues](../phase-02-code-analysis/phase.md#known-issues); every open choice is settled in the interview |
| 5 | No unresolved ambiguity that could mislead the plan | yes | Rounds 1 – 3 cover every open item; none answered "later" |
| 6 | Phase 01 items for Phases 02 and 03 resolved, kind confirmed | yes | P02-1 – P02-5 answered in Phase 02 [#open-items](../phase-02-code-analysis/phase.md#open-items); kind confirmed in 03/1 |
| 7 | If prototypes were run: choice recorded, outcomes set | n/a | no prototype; `prototypes: 0` (project config) |
| 8 | The Architect or its delegate has signalled readiness | yes | delegate readiness decision, this section, on the evidence of rows 1 – 7 |

Definition of Ready satisfied. All criteria met. Ready for Phase 04 upon approval by the
Architect or its delegate.

<a id="open-items"></a>
## Open Items

| # | Item | Settles in |
|---|---|---|
| O-4 | The acceptance scenarios, from 03/11 | Phase 04 |
| R-1 | [R-1 \| Review round: manual version bump against the CI bump (DD-10); claim-list place, form and result, `MATERIAL — unconfirmed` (DD-14, DD-20, DD-21)] | end of run |

No placeholder ADR: nothing was answered "later".

<a id="outcome"></a>
## Outcome

Compliant with all nine standing decisions; no bundle ADR. The interview confirmed the kind
(refactoring) and settled the reach: the after-a-stop paragraph is restated in claims, Phase 07,
README and ARCHITECTURE stay as they are, and the version is bumped by hand as the brief says. The
claim list lives in the phase summary under the gate table. Definition of Ready met.
