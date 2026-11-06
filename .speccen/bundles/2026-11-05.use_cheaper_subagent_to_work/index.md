---
type: Index
---

# Use cheaper subagent to work — Analysis Bundle

## Architecture Decision Records

| ADR | Date | Status | Description |
|---|---|---|---|
| [2026-11-05.bundle_store_lookup_unit](./adrs/2026-11-05.bundle_store_lookup_unit.md) | 2026-11-05 | DECIDED | How does the interview's existing bundle/store lookup relate to the new code-search unit? |
| [2026-11-05.code_search_agent](./adrs/2026-11-05.code_search_agent.md) | 2026-11-05 | DECIDED | Which agent runs a code-search unit: speccen-worker or the host's built-in read-only search agent? |
| [2026-11-05.code_search_tier](./adrs/2026-11-05.code_search_tier.md) | 2026-11-05 | DECIDED | Do code searches share the phase's model tier, with no separate search key? (brief 7/1) |
| [2026-11-05.self_check_interview_structure](./adrs/2026-11-05.self_check_interview_structure.md) | 2026-11-05 | DECIDED | Does the B1 self-check get a fifth check for interview structure? |
| [2026-11-05.template_version_2](./adrs/2026-11-05.template_version_2.md) | 2026-11-05 | DECIDED | Bring the new model keys to existing projects by raising the config template to version 2? (brief 7/3) |

## Bundle Control

| File | Type | Description |
|---|---|---|
| [STATE](./STATE.md) | State | Live workflow state |
| [log](./log.md) | Log | Prompt log & transition history |
| [delegated-decisions](./delegated-decisions.md) | DelegatedDecisions | Decisions taken under delegation in autonomous mode — review, adopt or override |
| [speccen-config](./speccen-config.yaml) | Config | Bundle overrides of the project configuration |

## Phases

### Phase 01 — Feature Analysis

| File | Type | Status | Description |
|---|---|---|---|
| [phase](./phase-01-feature-analysis/phase.md) | Phase | COMPLETE | Move read-only code searches onto the phase's cheap model tier, and cut the gate-check verifier to one run plus a delta re-check |
| [summary](./phase-01-feature-analysis/summary.md) | Summary | COMPLETE | Two-part refactoring of speccen's subagent cost model scoped; §7 decisions and search-agent choice carried to Phase 03 |

### Phase 02 — Code Analysis

| File | Type | Status | Description |
|---|---|---|---|
| [phase](./phase-02-code-analysis/phase.md) | Phase | COMPLETE | The subagent and gate-test rules live in one governing section each, but six restated sites (README, ARCHITECTURE, worker description, fail-safe, version row) sit beyond the brief's edit list |
| [summary](./phase-02-code-analysis/summary.md) | Summary | COMPLETE | Change slots into the governing skill's existing sections; six restated sites (README template and tiers, ARCHITECTURE units, worker description, fail-safe list, version row) widen the edit list |

### Phase 03 — Compliance & Review

| File | Type | Status | Description |
|---|---|---|---|
| [phase](./phase-03-compliance-review/phase.md) | Phase | COMPLETE | Five ADRs decided by the Architect and complied with; 7/2 follows; Definition of Ready satisfied |
| [summary](./phase-03-compliance-review/summary.md) | Summary | COMPLETE | Five ADRs decided by the Architect and complied with; 7/2 follows from 7/1; Definition of Ready satisfied |

### Phase 04 — Specification

| File | Type | Status | Description |
|---|---|---|---|
| [phase](./phase-04-specification/phase.md) | Phase | COMPLETE | Six-phase plan — config keys and template v2, the search unit, the gate-test self-check and delta re-check, phase pointers, restated copies, text verification |
| [summary](./phase-04-specification/summary.md) | Summary | COMPLETE | Six-phase plan over seven files; 16 requirements with scenarios, 19 text checks; gate passed after stops 04/4 – 04/7 |
| [doc-executive](./phase-04-specification/doc-executive.md) | Doc (executive) | COMPLETE | The main session sends simple search questions to a worker on a cheaper model tier |
| [doc-business](./phase-04-specification/doc-business.md) | Doc (business) | COMPLETE | The main session corrects common errors in the bundle files before it starts the verifier |
| [specification](./phase-04-specification/specification.html) | Specification | COMPLETE | Intent specification — search work on the phase tier, a five-point self-check and a delta re-check for the gate verifier |
| [specification (reduced)](./phase-04-specification/specification.md) | Specification | COMPLETE | Reduced projection of specification.html — search work on the phase tier, a five-point self-check and a delta re-check |

### Phase 05 — Implementation

| File | Type | Status | Description |
|---|---|---|---|
| [phase](./phase-05-implementation/phase.md) | Phase | COMPLETE | Plan executed in seven files — template v2 and model on 04/05, the search unit, the gate-test self-check and delta re-check, pointers, restated copies; T-1 – T-19 pass |
| [summary](./phase-05-implementation/summary.md) | Summary | COMPLETE | Plan implemented in seven files, uncommitted for the Architect; T-1 – T-19 pass; no deviations |

### Phase 06 — Close-out

| File | Type | Status | Description |
|---|---|---|---|
| [phase](./phase-06-close-out/phase.md) | Phase | COMPLETE | Three audience seeds, feature node and graduated specification written; graduation proposal pending the Architect |
| [summary](./phase-06-close-out/summary.md) | Summary | COMPLETE | Searches run on the phase tier and the gate test checks itself first; seven skill files changed, uncommitted for the Architect |
| [doc-executive](./phase-06-close-out/doc-executive.md) | Doc (executive) | COMPLETE | The main session now sends simple search questions to a worker on a cheaper model tier |
| [doc-business](./phase-06-close-out/doc-business.md) | Doc (business) | COMPLETE | The Architect sets a model tier for search questions in each phase from Code Analysis to Implementation |
| [doc-technical](./phase-06-close-out/doc-technical.md) | Doc (technical) | COMPLETE | Seven files changed — template version 2, model on 04 and 05, the search unit, the gate-test self-check and delta re-check, pointers and restated copies |

### Phase 07 — Retrospective

| File | Type | Status | Description |
|---|---|---|---|
| [phase](./phase-07-retrospective/phase.md) | Phase | COMPLETE | Working notes for the optional review of the implementation and the delegate's decisions |
| [retrospective](./phase-07-retrospective/retrospective.md) | Retrospective | COMPLETE | Plan delivered exactly and all checks hold, but the worker the search unit runs on is not fitted for a report-only search, and the delta re-check does not cover runs after a stop |
| [summary](./phase-07-retrospective/summary.md) | Summary | COMPLETE | Changes requested (proposed) — plan delivered exactly, but the search worker's body and the post-stop re-check need a few more lines |

## Files

| File |
|---|
| [gh-22-use-cheaper-subagent.md](./files/gh-22-use-cheaper-subagent.md) |
