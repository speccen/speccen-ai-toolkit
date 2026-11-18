---
type: Index
---

# rename audit skills — Analysis Bundle

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
| [phase](./phase-01-feature-analysis/phase.md) | Phase | COMPLETE | Pure rename of the five audit skills to audit-<role> (folder = frontmatter name), with every path, the script rubric paths, the command, ARCHITECTURE and README updated |
| [summary](./phase-01-feature-analysis/summary.md) | Summary | COMPLETE | Pure rename of the five audit skills to audit-<role>; Phase 02 confirms cited places, finds restatements and computes the hash baseline |

### Phase 02 — Code Analysis

| File | Type | Status | Description |
|---|---|---|---|
| [phase](./phase-02-code-analysis/phase.md) | Phase | COMPLETE | Every cited place matches HEAD; four more name references found; rubric hash is name-only (baseline 212cd4db08e1); Verification 1 regex also matches sdd-reconcile (9 hits) |
| [summary](./phase-02-code-analysis/summary.md) | Summary | COMPLETE | Cited places confirmed, 4 extra name references, rubric hash name-only (baseline 212cd4db08e1), Verification 1 regex needs tightening |

### Phase 03 — Compliance & Review

| File | Type | Status | Description |
|---|---|---|---|
| [phase](./phase-03-compliance-review/phase.md) | Phase | COMPLETE | No ADR in scope; O-4 – O-6 decided under delegation (tighten Verification 1 with , leave ARCHITECTURE.md:304, rename the stage description lines); Definition of Ready met |
| [summary](./phase-03-compliance-review/summary.md) | Summary | COMPLETE | Definition of Ready met; no ADR in scope; O-4 – O-6 decided (DD-7 material, unconfirmed) |
