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

### Phase 03 — Compliance & Review

| File | Type | Status | Description |
|---|---|---|---|
| [phase](./phase-03-compliance-review/phase.md) | Phase | COMPLETE | No bundle ADR; nine standing decisions are compatible; the interview settles kind, version bump, reach, claim-list place, template place and the noticed-line answer — Definition of Ready met |
| [summary](./phase-03-compliance-review/summary.md) | Summary | COMPLETE | Definition of Ready met — compliant with nine standing decisions; reach, claim-list place, template place and the version bump settled in the interview |

### Phase 04 — Specification

| File | Type | Status | Description |
|---|---|---|---|
| [phase](./phase-04-specification/phase.md) | Phase | COMPLETE | Four implementation phases rewrite the Gate test's verifier rules, the verifier unit and work order, the worker bullet and five claim-source lines, then bump the version; checked by text checks T-1 – T-19 |
| [summary](./phase-04-specification/summary.md) | Summary | COMPLETE | Four implementation phases with the exact text in Appendices A – F; 13 requirements, 19 text checks; specification assembled |
| [doc-executive](./phase-04-specification/doc-executive.md) | Doc (executive) | COMPLETE | Intent — the autonomous gate check costs less time and fewer tokens, and an independent checker run on code facts stays |
| [doc-business](./phase-04-specification/doc-business.md) | Doc (business) | COMPLETE | Intent — the delegate lists the code facts behind each phase in a fact list, and a checker run confirms only those facts |
| [specification](./phase-04-specification/specification.html) | Specification | COMPLETE | Intent specification — the gate-check verifier settles a capped list of code and repository claims; slips cost no fix attempt |
| [specification (md)](./phase-04-specification/specification.md) | Specification | COMPLETE | Reduced projection of specification.html — the narrow gate-check verifier |

### Phase 05 — Implementation

| File | Type | Status | Description |
|---|---|---|---|
| [phase](./phase-05-implementation/phase.md) | Phase | COMPLETE | The narrow gate-check verifier written into the governing skill, the worker and Phases 01 – 05; version bumped; text checks T-1 – T-19 |
| [summary](./phase-05-implementation/summary.md) | Summary | COMPLETE | Narrow verifier written into the governing skill, the worker and Phases 01 – 05; version 26.1116.1; T-1 – T-19 pass; two delegated deviations |

## Files

- [phase-05-text-checks.py](./files/phase-05-text-checks.py)
