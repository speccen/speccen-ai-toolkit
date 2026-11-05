---
type: Index
---

# Use cheaper subagent to work — Analysis Bundle

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

## Files

| File |
|---|
| [gh-22-use-cheaper-subagent.md](./files/gh-22-use-cheaper-subagent.md) |
