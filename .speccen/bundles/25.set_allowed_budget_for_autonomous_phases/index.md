---
type: Index
---

# set allowed budget for autonomous phases — Analysis Bundle

## Architecture Decision Records

| ADR | Date | Status | Description |
|---|---|---|---|
| [2026-11-11.fix_budget_ceiling_10](./adrs/2026-11-11.fix_budget_ceiling_10.md) | 2026-11-11 | DECIDED | What is the highest number of fix attempts a phase's fix budget may allow? (review R/1, overrides DD-12) |

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
| [phase](./phase-01-feature-analysis/phase.md) | Phase | COMPLETE | Add a `fixes` config key that sets how many times the delegate may repair a failing gate test, with progress, conclusions and ceiling guards |
| [summary](./phase-01-feature-analysis/summary.md) | Summary | COMPLETE | A provisional fix — a `fixes` key bounds how often the delegate repairs a failing gate test; reach and §5 decisions go to Phase 03 |

### Phase 02 — Code Analysis

| File | Type | Status | Description |
|---|---|---|---|
| [phase](./phase-02-code-analysis/phase.md) | Phase | COMPLETE | The one-fix rule lives in two places with different outcomes; the brief's seven diffs (six subsections) miss four restated sites; the upgrade rule already carries a version-3 bump |
| [summary](./phase-02-code-analysis/summary.md) | Summary | COMPLETE | The one-fix rule exists twice (gate test stops, Phase 05 accept rejects); the change fits the stops/prototypes key patterns; four restated sites lie outside the brief's diffs |

### Phase 03 — Compliance & Review

| File | Type | Status | Description |
|---|---|---|---|
| [phase](./phase-03-compliance-review/phase.md) | Phase | COMPLETE | No bundle ADRs; four standing decisions, all compliant; twelve open questions settled by the delegate (two MATERIAL — unconfirmed); Definition of Ready met |
| [summary](./phase-03-compliance-review/summary.md) | Summary | COMPLETE | Definition of Ready met in one iteration; twelve open questions settled by the delegate, two of them MATERIAL — unconfirmed (ceiling 3, progress by breaches) |

### Phase 04 — Specification

| File | Type | Status | Description |
|---|---|---|---|
| [phase](./phase-04-specification/phase.md) | Phase | COMPLETE | Five-phase plan — the fixes key and template version 3, the gate-test budget with its three guards, the Phase 05 accept, the restated copies, text verification |
| [summary](./phase-04-specification/summary.md) | Summary | COMPLETE | Five-phase plan for the fixes budget; fifteen requirements, nineteen text checks; specification assembled |
| [doc-executive](./phase-04-specification/doc-executive.md) | Doc (executive) | COMPLETE | The Architect sets how many fix attempts the delegate makes on a failed gate test |
| [doc-business](./phase-04-specification/doc-business.md) | Doc (business) | COMPLETE | The delegate corrects a failed gate test up to the number of fix attempts that the Architect sets |
| [specification](./phase-04-specification/specification.html) | Specification | COMPLETE | Intent specification — a fixes budget for the gate test of autonomous phases, with three guards |
| [specification (reduced)](./phase-04-specification/specification.md) | Specification | COMPLETE | Reduced projection of specification.html — a fixes budget for the gate test of autonomous phases, with three guards |

### Phase 05 — Implementation

| File | Type | Status | Description |
|---|---|---|---|
| [phase](./phase-05-implementation/phase.md) | Phase | COMPLETE | The fixes budget written into the governing skill, the Phase 05 skill and the README; text checks T-1 – T-19 |
| [summary](./phase-05-implementation/summary.md) | Summary | COMPLETE | The fixes budget is in the governing skill, the Phase 05 skill and the README; text checks T-1 – T-19 pass; changes uncommitted for the Architect |

### Phase 06 — Close-out

| File | Type | Status | Description |
|---|---|---|---|
| [phase](./phase-06-close-out/phase.md) | Phase | COMPLETE | Three audience seeds, feature node and graduated specification written; review decided — ceiling 10, five entries graduated, skill files committed |
| [summary](./phase-06-close-out/summary.md) | Summary | COMPLETE | A fixes budget (1 – 10, default 1) for the gate test of autonomous phases, with three guards; skill files committed |
| [doc-executive](./phase-06-close-out/doc-executive.md) | Doc (executive) | COMPLETE | The Architect now sets how many fix attempts the delegate makes on a failed gate test |
| [doc-business](./phase-06-close-out/doc-business.md) | Doc (business) | COMPLETE | The delegate corrects a failed gate test up to the number of fix attempts that the Architect sets |
| [doc-technical](./phase-06-close-out/doc-technical.md) | Doc (technical) | COMPLETE | The fixes key, template version 3, the gate-test budget with three guards and the Phase 05 accept, in three files |

## Files

| File |
|---|
| [gh-25-gate-test-fix-budget.md](./files/gh-25-gate-test-fix-budget.md) |
| [phase-05-move-test.py](./files/phase-05-move-test.py) |
| [phase-05-text-checks.py](./files/phase-05-text-checks.py) |
