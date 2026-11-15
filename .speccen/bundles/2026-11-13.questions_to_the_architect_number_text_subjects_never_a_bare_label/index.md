---
type: Index
---

# Questions to the Architect: [number | text] subjects, never a bare label — Analysis Bundle

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
| [phase](./phase-01-feature-analysis/phase.md) | Phase | COMPLETE | Make every question, decision and item that speccen puts to the Architect carry a `[number \| text]` subject, so the Architect can answer without opening the bundle |
| [summary](./phase-01-feature-analysis/summary.md) | Summary | COMPLETE | A feature to the skills — one rule that everything put to the Architect carries `[number \| text]` subjects; the rule's reach and the three §5 decisions go to Phase 03 |

### Phase 02 — Code Analysis

| File | Type | Status | Description |
|---|---|---|---|
| [phase](./phase-02-code-analysis/phase.md) | Phase | COMPLETE | The skills give items labels but nowhere ask that the item's text travel with the label; the brief's edits fit, and several Architect-facing places the brief does not list also name items by label |
| [summary](./phase-02-code-analysis/summary.md) | Summary | COMPLETE | The brief's six edits fit the skills as they are; several more Architect-facing places name items by label, and three governing line references have drifted |

### Phase 03 — Compliance & Review

| File | Type | Status | Description |
|---|---|---|---|
| [phase](./phase-03-compliance-review/phase.md) | Phase | COMPLETE | The rule's reach, form and place decided under delegation, with fourteen material answers left unconfirmed for the review round; the Architect added the narrowing of stop condition 5 to the scope |
| [summary](./phase-03-compliance-review/summary.md) | Summary | COMPLETE | Definition of Ready met — the rule's reach, form and place decided under delegation, fourteen material answers wait for the Architect; stop condition 5 narrowed by the Architect |

### Phase 04 — Specification

| File | Type | Status | Description |
|---|---|---|---|
| [phase](./phase-04-specification/phase.md) | Phase | COMPLETE | Six-phase plan — the subject rule in Structured questions, its pointers in the governing, interview, Phase 05 and reconcile skills, the narrowed stop condition 5, the README, and text verification |
| [specification](./phase-04-specification/specification.html) | Specification | COMPLETE | Intent specification — every item put to the Architect carries a [number \| text] subject; record repairs no longer stop an autonomous run |
| [specification (reduced)](./phase-04-specification/specification.md) | Specification | COMPLETE | Reduced projection of specification.html — every item put to the Architect carries a [number \| text] subject; record repairs no longer stop an autonomous run |
| [doc-executive](./phase-04-specification/doc-executive.md) | Doc (executive) | COMPLETE | Every question that speccen puts to the Architect names its subject in plain words, so the Architect answers from the message alone |
| [doc-business](./phase-04-specification/doc-business.md) | Doc (business) | COMPLETE | The Architect reads every question, stop and review item with its subject in plain words |
| [summary](./phase-04-specification/summary.md) | Summary | COMPLETE | Six-phase plan, seventeen requirements and twenty text checks — the subject rule with its pointers, and the narrowed stop condition 5 |

### Phase 05 — Implementation

| File | Type | Status | Description |
|---|---|---|---|
| [phase](./phase-05-implementation/phase.md) | Phase | COMPLETE | The subject rule, its pointers and the narrowed stop condition 5 applied to five files; twenty text checks pass |
| [summary](./phase-05-implementation/summary.md) | Summary | COMPLETE | Five files changed as planned; twenty text checks pass, and fail on the unedited text; no deviation |

## Files

| File | Description |
|---|---|
| [gh-26-questions-subjects.md](./files/gh-26-questions-subjects.md) | Issue #26, the brief, copied verbatim |
| [phase-05-text-checks.py](./files/phase-05-text-checks.py) | Phase 05 text checks T-1 – T-20, run from the repository root |
