---
type: Phase
phase: "03 — Compliance & Review"
status: COMPLETE
description: Five ADRs decided by the Architect and complied with; 7/2 follows; Definition of Ready satisfied
---

<a id="phase-top"></a>
# Use cheaper subagent to work — Compliance & Review

[Index](../index.md) · [State](../STATE.md) · [Log](../log.md)

---

<a id="adrs"></a>
## ADRs in scope

| ADR | Tier | Status | Decision | Compliance |
|---|---|---|---|---|
| [2026-11-05.bundle_store_lookup_unit](../adrs/2026-11-05.bundle_store_lookup_unit.md#decision) | bundle | DECIDED | How does the interview's existing bundle/store lookup relate to the new code-search unit? | compliant |
| [2026-11-05.code_search_agent](../adrs/2026-11-05.code_search_agent.md#decision) | bundle | DECIDED | Which agent runs a code-search unit: speccen-worker or the host's built-in read-only search agent? | compliant |
| [2026-11-05.code_search_tier](../adrs/2026-11-05.code_search_tier.md#decision) | bundle | DECIDED | Do code searches share the phase's model tier, with no separate search key? (brief 7/1) | compliant |
| [2026-11-05.self_check_interview_structure](../adrs/2026-11-05.self_check_interview_structure.md#decision) | bundle | DECIDED | Does the B1 self-check get a fifth check for interview structure? | compliant |
| [2026-11-05.template_version_2](../adrs/2026-11-05.template_version_2.md#decision) | bundle | DECIDED | Bring the new model keys to existing projects by raising the config template to version 2? (brief 7/3) | compliant |

No standing (Tier-2) ADRs: `.speccen/decisions/` does not exist.

<a id="extensions"></a>
## Extensions applied

| Extension | Why | Where it applies | Outcome |
|---|---|---|---|
| — | — | — | No extensions for this phase |

`.speccen/extensions/compliance-review/` does not exist in this repository.

<a id="compliance"></a>
## Compliance Iterations

### Iteration 1

- **ADRs at entry:** none. No bundle ADR, no standing ADR, so there is nothing to comply with yet
  and no override to detect.
- **Open items at entry** (from [Phase 01](../phase-01-feature-analysis/phase.md#open-items) and
  [Phase 02](../phase-02-code-analysis/phase.md#open-items)): O-1 (7/1), O-2 (7/2), O-3 (7/3),
  O-4 (search agent), O-7 (interview lookup), O-8 (fifth self-check), O-9 (restated sites), O-6
  (acceptance — Phase 04), and the kind (provisional until Phase 03, DD-1).
- **Placeholder ADRs created** for the five material questions the basis does not decide (Step 6;
  governing skill → What stays with the Architect, item 1): `code_search_tier` (O-1),
  `template_version_2` (O-3), `code_search_agent` (O-4), `bundle_store_lookup_unit` (O-7),
  `self_check_interview_structure` (O-8). They are questions, not decisions.
- **Analysis updates:** none yet — no ADR is decided. Once the stop round is answered, each decided
  ADR gets its compliance response and the affected sections are named here.

### Iteration 2

- **ADRs processed:** all five placeholders became `DECIDED` by the Architect's answer to the stop
  round (log 19:17) and were transcribed per **Scribing a stated decision**. Each now carries its
  compliance response.
- **7/2 settled** in round 3 (03/9, DD-13), now that its prerequisite 03/4 is decided.
- **Analysis updates.** The decisions refine the design that Phase 04 plans; they change no
  Phase 01 or Phase 02 finding, and those closed files are not edited (Invariant 1). Where a
  Phase 01 statement is now narrower than a decision — Phase 01 Scope names A5's interview line as
  "inline, or as a code-search unit", while ADR `bundle_store_lookup_unit` widens the unit to bundle
  and store lookups — the ADR governs. The design is now:
  - **Unit:** one Units row, "a search" — find and quote evidence for one question; code in
    Phases 02–05, bundle and store in any interviewing phase; `speccen-worker`, report only, on
    the phase's `model` tier (`inherit` where the phase has no `model`).
  - **Config:** `model` added to `specification` and `implementation` in the Keys list, the
    fail-safe list and the template (`model: economy`); template `version: 2`.
  - **Gate test:** B1 self-check with five checks; B2 delta re-check.
  - **Sync:** S-1 – S-6 change with their source (DD-12).

### Domain understanding (Step 5)

No ADR or Architect prompt asks for more depth. Two facts already in Phase 02 bear on the open
decisions and are restated here only as references:
- the upgrade rule adds a missing phase `model` as `inherit` (governing `:856–859`) — bears on 7/3;
- `speccen-worker` takes the resolved model at launch (`:1314–1315`); hosts may not honour it
  (`:1347–1356`) — bears on the search-agent choice.

### Prototypes

None. `phases.compliance-review.prototypes` is `0` (project config), and every open choice is a
policy choice that a spike would not decide better than reasoning.

<a id="interview"></a>
## Interview

Mode: `autonomous` (bundle config), `stops: ask` (project config). The delegate answers what the
basis decides; material questions the basis leaves open go to the Architect as one stop round.

**Round 1**

| # | Question | Depends on | Proposed | Answer |
|---|---|---|---|---|
| 03/1 | Kind — confirm refactoring (provisional since 01/1)? | — | refactoring | delegate: refactoring, confirmed — basis: session-start Work kind answer (log 17:03), DD-1 — [DD-10](../delegated-decisions.md#dd-10) |
| 03/2 | Design basis — are Changes A (A1–A6) and B (B1–B2) the intended design, with only the §7 questions and the Phase 02 open items open? | — | yes | delegate: yes — basis: brief §2–§4 and §7 heading "Decisions for the Architect (yes / no)" — [DD-11](../delegated-decisions.md#dd-11) |

**Round 2** — 03/3 answered by the delegate; 03/4 – 03/8 are the stop round (stop condition 1: material decisions the basis leaves open), answered by the Architect

| # | Question | Depends on | Proposed | Answer |
|---|---|---|---|---|
| 03/3 | Scope — are the restated sites S-1 – S-6 in scope, changed in the same commit as their source? | 03/2 | yes | delegate: yes — basis: project convention (Phase 02 Coding Patterns; commits `47ce36a`, `999c03e`) — [DD-12](../delegated-decisions.md#dd-12) |
| 03/4 | 7/1 — Code searches share the phase's `model` tier, with no separate search key? | 03/2 | yes | Architect: "yes" (log 19:17) — [ADR](../adrs/2026-11-05.code_search_tier.md) |
| 03/5 | 7/3 — Bring the new keys to existing projects by raising the template to `version: 2`, missing keys added as `inherit`? | 03/2 | yes | Architect: "yes" (log 19:17) — [ADR](../adrs/2026-11-05.template_version_2.md) |
| 03/6 | Search agent — a code-search unit runs on `speccen-worker`, launched with the phase tier's model (not a host built-in agent)? | 03/2 (and, for "the phase tier's model", 03/4 — a same-round dependency, see stop 2) | yes | Architect: "yes" (log 19:17) — [ADR](../adrs/2026-11-05.code_search_agent.md) |
| 03/7 | Interview lookup — widen the unit to "a search" (find and quote evidence for one question), in the code for Phases 02–05 and in the bundle and store for any phase that interviews, so the interview's lookup becomes a listed unit? | 03/2 (and 03/6 for what the unit is — a same-round dependency, see stop 2) | yes (option a — the widening this question describes; ADR options a–c) | Architect: "yes" (log 19:17) — [ADR](../adrs/2026-11-05.bundle_store_lookup_unit.md) |
| 03/8 | Self-check — add a fifth B1 check: "every round holds only the frontier, and every question one decision"? | 03/2 | yes | Architect: "yes" (log 19:17) — [ADR](../adrs/2026-11-05.self_check_interview_structure.md) |

03/3 is answered by the delegate and sits in this round because it depends on 03/2 (round 1).
03/5 is independent of 03/4: the version rises whichever keys 03/4 yields.

Closing question for this stop round: **Record these decisions into their ADRs? — yes / not yet**
— Architect: "yes" (log 19:17). The five decisions were transcribed into their placeholder ADRs per
**Scribing a stated decision**.

**Round 3**

| # | Question | Depends on | Proposed | Answer |
|---|---|---|---|---|
| 03/9 | 7/2 — Phase 03 code searches run on Phase 03's tier (`balanced`), not forced to `economy`? | 03/4 | yes | delegate: yes — basis: ADR `code_search_tier` (03/4), brief "Follows from 7/1" — [DD-13](../delegated-decisions.md#dd-13) |

**Round 4 — stop round 2** (stop condition 5: the gate test's fix cannot reach row 14 without
changing DECIDED ADRs, which only the Architect may allow) — answered by the Architect

| # | Question | Depends on | Proposed | Answer |
|---|---|---|---|---|
| 03/10 | Your "yes" at 19:17 answered the stop round and the closing question in one word. Confirm it was also your explicit request to record the five decisions into their ADRs? | — | yes | Architect: "yes" (log 19:23) |
| 03/11 | May the five ADR Decision rows be corrected to the exact transcription form — the proposal quoted from `log.md` (19:21 record) and marked "accepted by the Architect in interview question 03/N", with no other words (03/7 keeps "(option a)")? | 03/10 (same-round dependency, not recorded at the time — see stop 3) | yes | Architect: "yes" (log 19:23) |
| 03/12 | Accept the same-round dependencies of 03/6 and 03/7 as a record defect (your "yes" took every proposal together), as in 01/14? | — | yes | Architect: "yes" (log 19:23) |

**Round 5 — stop round 3** (stop condition 5: verifier run 2, row 15) — answered by the Architect

| # | Question | Depends on | Proposed | Answer |
|---|---|---|---|---|
| 03/13 | In stop round 2, 03/11 depended on 03/10 in the same round. Accept this as a record defect — your "yes" took both — and pass the gate? | — | yes | Architect: "go ahead" (log 19:26) |

<a id="open-items"></a>
## Open Items

| # | Item | Settles in |
|---|---|---|
| O-1 | 7/1 → decided: ADR `code_search_tier` (03/4) | settled |
| O-2 | 7/2 → decided: 03/9, DD-13 | settled |
| O-3 | 7/3 → decided: ADR `template_version_2` (03/5) | settled |
| O-4 | Search agent → decided: ADR `code_search_agent` (03/6) | settled |
| O-7 | Interview lookup → decided: ADR `bundle_store_lookup_unit` (03/7) | settled |
| O-8 | Fifth self-check → decided: ADR `self_check_interview_structure` (03/8) | settled |
| O-9 | Restated sites → settled by DD-12 (03/3); v1 example lines left to the plan | Phase 04 (plan) |
| O-6 | Acceptance and "done when" | Phase 04 |

<a id="outcome"></a>
## Definition of Ready

| Criterion | Status | Evidence |
|---|---|---|
| Every ADR file has a compliance response | met | each of the five ADRs has "## Compliance 2026-11-05" and a "(correction)" section ([ADRs in scope](#adrs)) |
| Open questions from 01 and 02 resolved or escalated | met | [Open Items](#open-items): O-1 – O-4, O-7, O-8 settled; O-9 settled for scope (DD-12); O-6 carried to Phase 04 |
| Project Conventions Confirmation exists and is complete | met | [Phase 02 conventions](../phase-02-code-analysis/phase.md#conventions) |
| Domain understanding sufficient for a phase-structured plan | met | [Iteration 2](#compliance) design summary; Phase 02 sites S-1 – S-6 with line numbers |
| No unresolved ambiguity that could mislead the plan | met | no `PENDING` ADR; the v1 example lines and acceptance are named Phase 04 choices, not ambiguities |
| Phase 01 items for 02/03 resolved; kind confirmed | met | P02-1 – P02-3 (Phase 02); O-1 – O-4 (here); kind: DD-10 |
| Prototypes: choice recorded, outcomes set | not applicable, because no prototype ran | `prototypes: 0` (project config) |
| Readiness signalled by the Architect or its delegate | met | delegate readiness decision below, basis: this table |

**Outcome:** Definition of Ready satisfied. All criteria met. Ready for Phase 04 upon approval by
the Architect or its delegate. Readiness decided under delegation (autonomous), basis: the five
DECIDED ADRs and this table; confirmed by the gate test.
