---
type: Index
---

# set allowed budget for autonomous phases — Analysis Bundle

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

## Files

| File |
|---|
| [gh-25-gate-test-fix-budget.md](./files/gh-25-gate-test-fix-budget.md) |
