---
type: Index
---

# rename audit skills — Analysis Bundle

## Architecture Decision Records

| ADR | Date | Status | Description |
|---|---|---|---|
| [2026-11-18.architecture_reading_guide_sdd_path](./adrs/2026-11-18.architecture_reading_guide_sdd_path.md) | 2026-11-18 | DECIDED | Fix the stale skills/sdd/NN-* path in ARCHITECTURE.md in this change, folded into the one code commit |

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
| [phase](./phase-03-compliance-review/phase.md) | Phase | COMPLETE | Iteration 2 — ADR 2026-11-18.architecture_reading_guide_sdd_path (overrides DD-8) processed; O-4 – O-6 decided under delegation (tighten Verification 1 with , leave ARCHITECTURE.md:307, rename the stage description lines); Definition of Ready met |
| [summary](./phase-03-compliance-review/summary.md) | Summary | COMPLETE | Iteration 2 — the DD-8 override ADR processed; Definition of Ready met; O-4 – O-6 decided (DD-7 material, unconfirmed) |

### Phase 04 — Specification

| File | Type | Status | Description |
|---|---|---|---|
| [phase](./phase-04-specification/phase.md) | Phase | COMPLETE | Four-phase plan plus an iteration-2 addendum (fix ARCHITECTURE.md:307, folded into the code commit) — move the five folders, rename the paths and the name, update command and docs, verify with 13 checks and make one commit |
| [summary](./phase-04-specification/summary.md) | Summary | COMPLETE | Four-phase plan plus an iteration-2 addendum (ADR: fix ARCHITECTURE.md:307), 8 requirements, 13 checks (T-1 – T-3 run against the planned text); plan and Test Plan approved under delegation |
| [doc-executive](./phase-04-specification/doc-executive.md) | Doc (executive) | COMPLETE | All speccen skill groups will use one naming rule; the audit keeps its results comparable |
| [doc-business](./phase-04-specification/doc-business.md) | Doc (business) | COMPLETE | The audit runs as before under /speccen:audit; only skill names and folders change |
| [specification](./phase-04-specification/specification.html) | Specification | COMPLETE | Intent specification — the five audit skills get audit- folder names equal to their skill names; the rubric hash stays 212cd4db08e1 ([md](./phase-04-specification/specification.md)) |

### Phase 05 — Implementation

| File | Type | Status | Description |
|---|---|---|---|
| [phase](./phase-05-implementation/phase.md) | Phase | COMPLETE | Rename implemented in one commit (fdbc357, incl. the iteration-2 ARCHITECTURE.md:307 fix); T-1 – T-14 pass; one deviation (T-4 runs Python in UTF-8 mode on this Windows host) |
| [summary](./phase-05-implementation/summary.md) | Summary | COMPLETE | Commit fdbc357 renames the five audit skills; T-1 – T-13 pass; rubric hash unchanged; one deviation (UTF-8 mode for T-4) |

### Phase 06 — Close-out

| File | Type | Status | Description |
|---|---|---|---|
| [phase](./phase-06-close-out/phase.md) | Phase | COMPLETE | Three outcome seeds written; feature node and specification graduated; review round decided — 2 lessons promoted, DD-8 overridden by ADR and fixed |
| [summary](./phase-06-close-out/summary.md) | Summary | COMPLETE | Audit skills renamed to audit-<role> in commit fdbc357 (with the ARCHITECTURE sdd path fix); review round decided; 2 lessons graduated |
| [doc-executive](./phase-06-close-out/doc-executive.md) | Doc (executive) | COMPLETE | All speccen skill groups now use one naming rule; audit results stay comparable |
| [doc-business](./phase-06-close-out/doc-business.md) | Doc (business) | COMPLETE | The audit runs as before under /speccen:audit; the five audit skills now have audit- names |
| [doc-technical](./phase-06-close-out/doc-technical.md) | Doc (technical) | COMPLETE | Five audit skill folders renamed to audit-<role> with git mv; nine files updated by a fixed substitution map; rubric hash unchanged |

### Phase 08 — Reference

| File | Type | Status | Description |
|---|---|---|---|
| [phase](./phase-08-reference/phase.md) | Phase | COMPLETE | Reference written by a worker unit, checked in the main session, approved by the Architect |
| [summary](./phase-08-reference/summary.md) | Summary | COMPLETE | Layered technical reference for the audit-skill rename — approved by the Architect |
| [reference](./phase-08-reference/reference.html) | Reference | COMPLETE | Layered technical reference for the audit-skill rename (commit fdbc357, PR #35) ([md](./phase-08-reference/reference.md)) |

## Files

| File | Description |
|---|---|
| [phase-05-text-checks.py](./files/phase-05-text-checks.py) | Phase 05 checks T-1 – T-3, T-5 – T-14 |
