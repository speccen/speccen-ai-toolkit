---
type: Index
---

# use narrow verifier for phase checks — Analysis Bundle

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
| [phase](./phase-01-feature-analysis/phase.md) | Phase | COMPLETE | Narrow the gate-check verifier to a capped list of code and repository claims, run it beside the self-check, and stop line-number slips from failing rows |
| [summary](./phase-01-feature-analysis/summary.md) | Summary | COMPLETE | A provisional refactoring — narrow the gate-check verifier to a capped claim list run beside the self-check, with slip vs. wrong; reach and record place go to Phase 03 |

### Phase 02 — Code Analysis

| File | Type | Status | Description |
|---|---|---|---|
| [phase](./phase-02-code-analysis/phase.md) | Phase | COMPLETE | The verifier rule lives in one Gate-test bullet plus the later-runs and after-a-stop paragraphs; the brief's edit list misses the after-a-stop paragraph and the Phase 07 spot-check, and its manual version bump conflicts with the CI bump |
| [summary](./phase-02-code-analysis/summary.md) | Summary | COMPLETE | The verifier's breadth comes from one "every row" sentence and row-keyed failure and re-run rules; the change slots into existing text, with three sites outside or against the brief |
