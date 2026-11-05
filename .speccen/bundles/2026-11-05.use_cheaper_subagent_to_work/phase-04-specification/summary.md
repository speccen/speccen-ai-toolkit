---
type: Summary
phase: "04 — Specification"
status: COMPLETE
phase_file: ./phase.md
description: Six-phase plan over seven files; 16 requirements with scenarios, 19 text checks; gate passed after stops 04/4 – 04/7
---

# Phase 04 Summary — Specification

[Index](../index.md) · [State](../STATE.md) · [Log](../log.md)

---

**Work completed:** Implementation Plan in six phases (configuration, search unit, gate test,
pointers, restated copies, verification); target-state flows; risk table; Test Plan of 19 text
checks; 16 requirements with acceptance scenarios; two intent seeds; assembled specification.

**Outcome:** the brief's Changes A and B as refined by the five Phase 03 ADRs →
[full detail](./phase.md#implementation-plan)

**Specification (the complete, assembled spec — intent + requirements/scenarios):**
- [specification.html](./specification.html) — full, authoritative (reduced view: [specification.md](./specification.md))

**Stakeholder seeds (intent — expansion seeds, not for verbatim external sharing):**
- Executive → [doc-executive.md](./doc-executive.md)
- Business → [doc-business.md](./doc-business.md)

**Open items carried forward:** O-10 — the §6 cost measurement after the next bundle (follow-up,
not acceptance) → [detail](./phase.md#open-items)

**Delegated decisions:** 3 in this phase ([DD-14 – DD-16](../delegated-decisions.md#dd-14); DD-16 supersedes DD-14).
Plan and Test Plan approved under delegation by the passed gate test (verifier run 6, after Architect stop rounds 04/4 – 04/7).

**Extensions applied:** none

<a id="delegate-gate-check"></a>
## Delegate gate check

Self-check before the verifier (quotes · references · latest answer · index · interview
structure): done — 2 fixes (A6 had no requirement → R-14 and T-15 added; one unsourced sentence
removed from the 05 pointer text).

Verifier run 1: 20 of 24 rows confirmed; rows 6, 12, 15 and 21 not confirmed. Fixed once: check 6.1 limited to paths outside `.speccen`; seed wording (passive voice, one term for the main session, unsourced "most expensive"); specification "Why" column now taken from the plan, rejected alternative sourced from Phase 02 O-7; R-15 (work order, parallel), R-16 (no host-wide default) and T-16 – T-19 added, T-1 widened to both `model` keys; 04/3 reopened 04/1 (DD-16); `:772–779`; 05 pointer uses the brief's line; "the workflow stops".

### Traceability

| Source | Scenario(s) | Test(s) |
|---|---|---|
| brief A1 — search is a unit; inline rule | R-1, R-5 | T-4, T-10 |
| brief A2 — Search section: one question, findings only, re-open, tier | R-1, R-2, R-3, R-4 | T-5 |
| brief A2 — work order breadth; parallel searches | R-15 | T-16 |
| brief A3 — `model` on 04/05 | R-6 | T-2, T-3 |
| brief A4 — template `model: economy` on 04/05, version 2 | R-7 | T-1 (both keys and version), T-11 |
| brief A5 — pointers in 02, 05, interview | R-9 | T-10 |
| brief A6 — existing log line | R-14 | T-15 |
| brief B1 — self-check | R-10 | T-7 |
| brief B2 — delta re-check | R-11 | T-8, T-9 |
| brief §4 — verifier and decision seats on session model | R-12 | T-6, T-12 |
| brief §4 — no global default subagent model | R-16 | T-18 |
| brief §4 — one-writer rule | R-2 (worker writes no file) | T-5 |
| ADR `code_search_tier` | R-4, R-6 | T-2, T-3, T-5 |
| ADR `template_version_2` | R-7, R-8 | T-1, T-14, T-19 |
| ADR `code_search_agent` | R-4 | T-5 |
| ADR `bundle_store_lookup_unit` | R-1, R-4, R-9 | T-4, T-5, T-10 |
| ADR `self_check_interview_structure` | R-10 | T-7 |
| DD-12 — restated copies | R-13 | T-11, T-12, T-13, T-17 |

Every scenario has a test; every requirement cites a source in the Requirements table
([phase.md](./phase.md#requirements)); every plan phase's **Why** cites a source (Phase 02 anchor,
ADR, brief section or DD).

### Gate table

| Item | Result | Evidence | Verified |
|---|---|---|---|
| Extensions: every file in `.speccen/extensions/specification/` listed; active ones applied | pass | folder does not exist; [Extensions table](./phase.md#extensions) | confirmed (run 2) |
| Proposed changes summary lists all affected files with change type | pass | [Proposed Changes Summary](./phase.md#implementation-plan) — 7 files, all "modify" | confirmed (run 2) |
| Target-state flow as ASCII, linked to the Phase 02 diagram | pass | Target-State Execution Flow, Paths 1 and 2, with link to `../phase-02-code-analysis/phase.md#code-analysis` | confirmed (run 2) |
| Strategy evaluation if multiple approaches | not applicable, because one approach remains after the Phase 03 ADRs | Strategy Evaluation paragraph | confirmed (run 2) |
| Implementation phases numbered and sequenced | pass | Phases 1–6 | confirmed (run 2) |
| Every checklist item specific and traceable | pass | each item names file, line and text | not confirmed (run 1); confirmed (run 2) |
| Each phase ends with Build and Validate | pass | 1.4, 2.3, 3.3, 4.2, 5.2, 6.2 | confirmed (run 2) |
| Every phase states a Why with a source; subtask Why only where non-obvious | pass | six phase Whys; subtask Whys in 2.2 (two) | confirmed (run 2) |
| Risk mitigation table populated | pass | Risk Mitigation, 6 rows | confirmed (run 2) |
| Test Plan present (scope incl. "none, because…", behaviours, coverage intent) | pass | Test Plan — "none, because the change is prose and YAML…"; behaviours; coverage intent | confirmed (run 2) |
| `doc-executive.md` and `doc-business.md` written, `expandable: true` | pass | [doc-executive.md](./doc-executive.md), [doc-business.md](./doc-business.md) | confirmed (run 2) |
| Both seeds STE-styled | pass | short active sentences; consistent terms (search, tier, verifier) | confirmed (run 6) — earlier: not confirmed (runs 1–5); run 5: run-4 defects gone; two frontmatter descriptions held two ideas; "use" as noun and verb; "evidence bundle" gave "evidence" a second sense; corrected after stop 5, with "team" → "the Architect" and "a next bundle" → "the next bundle" |
| Executive seed keeps TCO out of scope | pass | "TCO / cost / budget: out of scope" | confirmed (run 2) |
| Deviations protocol stated | pass | Deviations Protocol | confirmed (run 2) |
| `specification.html` assembled (projection, STE, depth-layered) with `specification.md` | pass | [specification.html](./specification.html) L1 → L2 → L3 → decisions → requirements; [specification.md](./specification.md) | confirmed (run 3) — earlier: not confirmed (run 2) — html:221 "(DD-1 to DD-16)" |
| Specification has Requirements & acceptance scenarios incl. error/edge behaviour | pass | R-1 – R-16; error paths in R-5, R-6, R-11 | confirmed (run 2) |
| Specification diagrams verified to render | pass | both SVGs parse; headless Chrome render checked | confirmed (run 2) |
| `summary.md` links plan, specification and both seeds | pass | this file | confirmed (run 2) |
| `index.md` lists every file this phase wrote | pass | [index.md](../index.md) Phase 04 section | confirmed (run 2) |
| `## Delegate gate check` with evidence for every item | pass | this section | confirmed (run 2) |
| Traceability check (Mode behaviour) | pass | Traceability table above | not confirmed (run 1); confirmed (run 2) |
| Interview: frontier only; one decision per question; who answered; DDs linked both ways | pass | [Interview](./phase.md#interview) round 1 (04/1, 04/2, no dependencies); round 2 (04/3, depends on 04/1); DD-14 – DD-16 | confirmed (run 2) |
| No question parked with "later" | pass | none | confirmed (run 2) |
| `gated`: `STATE.md` shows AWAITING ARCHITECT REVIEW | not applicable, because the effective mode is `autonomous` (bundle config) | [speccen-config.yaml](../speccen-config.yaml) | confirmed (run 2) |

Verifier run 2: 22 of 24 rows confirmed; rows 12 and 15 not confirmed → stop (condition 5). After
the stop was recorded, rows 12 and 15 were corrected, together with the smaller run-2 findings
(`:901–903`, `:870–903`, `:855–859`, O-6 count, T-14 in 1.4, DD-14 superseded note, `:418` noted,
"three times" sourced, T-5 widened). ADR `template_version_2` still cites `:856–859`; it is
DECIDED, so it is not changed without the Architect's permission.

<a id="stop"></a>
## Stop (autonomous) — resolved

| | |
|---|---|
| **Reason** | Stop condition 5: rows 12 (seed STE) and 15 (spec DD range) still failed on verifier run 2 after the one allowed fix. Run 3 (04/4): row 15 confirmed; row 12 not confirmed (frontmatter actor name; "affected rows" vs "failed and affected rows"; search sender named "speccen"). |
| **Question** | 04/4 (answered: yes) → run 3: row 15 confirmed, row 12 not confirmed → 04/5 (answered: yes) → run 4: row 12 not confirmed → 04/6 (answered: yes) → run 5: row 12 not confirmed → 04/7 → [stop round](./phase.md#interview) |
| **Options** | re-check rows 12 and 15 only · re-check every row · other |
| **Lean** | re-check rows 12 and 15 only |
| **Resolution** | Architect answered 04/4 – 04/7 "yes"; row 15 confirmed on run 3, row 12 confirmed on run 6. |
| **Evidence** | verifier run 2; `doc-business.md`, `doc-executive.md`, `specification.html` |

Verifier runs 3–6 (delta, per 04/4 – 04/7): run 3 confirmed row 15; runs 3–5 each found new STE defects in the seeds; run 6 confirmed row 12 with only style preferences left (rule breaches alone fail the row). All 24 rows now confirmed.
