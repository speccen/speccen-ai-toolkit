---
type: Specification
phase: "04 — Specification"
status: COMPLETE
description: Reduced projection of specification.html — search work on the phase tier, a five-point self-check and a delta re-check
---

# Use cheaper subagent to work — Specification (reduced)

[Index](../../bundles/2026-11-05.use_cheaper_subagent_to_work/index.md) · [Full specification](./specification.html) · [Reference](./reference.html) (what was actually built) · [Plan](../../bundles/2026-11-05.use_cheaper_subagent_to_work/phase-04-specification/phase.md#implementation-plan)

---

## What is being built

speccen sends search work to the model tier of each phase. The main session keeps every decision.
The gate test runs five self-checks before the verifier. A second verifier run checks only failed
rows and rows whose evidence file changed. Source: [issue #22](../../bundles/2026-11-05.use_cheaper_subagent_to_work/files/gh-22-use-cheaper-subagent.md),
[Phase 01](../../bundles/2026-11-05.use_cheaper_subagent_to_work/phase-01-feature-analysis/phase.md#feature-description).

## What changes

| File | Change |
|---|---|
| `skills/sdd/00-governing-workflow/SKILL.md` | keys and fail-safe accept `model` on 04/05; template `version: 2`; Units row and section *Search*; gate-test self-check and delta re-check |
| `skills/sdd/02-code-analysis/SKILL.md` | pointer in Steps 2 and 3 |
| `skills/sdd/05-implementation/SKILL.md` | pointer in Step 3 |
| `skills/sdd/interview/SKILL.md` | lookup rule points to the search unit |
| `README.md` | template copy identical; Model tiers names searches |
| `ARCHITECTURE.md` | units list names the search; verifier on the session model |
| `agents/speccen-worker.md` | description names a search |

## Decisions

| ADR | Decision | Rejected |
|---|---|---|
| [code_search_tier](../../bundles/2026-11-05.use_cheaper_subagent_to_work/adrs/2026-11-05.code_search_tier.md) | searches use the phase `model` tier | a separate search key |
| [template_version_2](../../bundles/2026-11-05.use_cheaper_subagent_to_work/adrs/2026-11-05.template_version_2.md) | template `version: 2`; missing keys as `inherit` | keep version 1 |
| [code_search_agent](../../bundles/2026-11-05.use_cheaper_subagent_to_work/adrs/2026-11-05.code_search_agent.md) | `speccen-worker` with the tier model | a host built-in agent |
| [bundle_store_lookup_unit](../../bundles/2026-11-05.use_cheaper_subagent_to_work/adrs/2026-11-05.bundle_store_lookup_unit.md) | one unit, "a search": code 02–05, bundle and store any phase | a separate Units row for the lookup |
| [self_check_interview_structure](../../bundles/2026-11-05.use_cheaper_subagent_to_work/adrs/2026-11-05.self_check_interview_structure.md) | fifth self-check for interview structure | four checks |

## Requirements & acceptance scenarios

| Id | Requirement (SHALL) | Scenario (WHEN → THEN) | Source |
|---|---|---|---|
| R-1 | The governing skill SHALL list a search as a subagent unit: code in Phases 02–05, bundle and store in any phase. | WHEN a phase needs evidence for one question → THEN the Units table names a search unit for that phase and source. | brief A1; ADR `bundle_store_lookup_unit` |
| R-2 | A search SHALL return findings only — `path:line`, verbatim quote, what was not found — and write no file. | WHEN a search unit returns → THEN its report has no conclusion and no file was written. | brief A2 |
| R-3 | The main session SHALL re-open every finding it uses before citing it, and never cite a search report alone. | WHEN a finding is cited in a phase file → THEN the citation points at the code, not at the report. | brief A2 |
| R-4 | A search SHALL run on `speccen-worker` with the phase's `model` tier; with no `model` key, on the session model. | WHEN Phase 02 searches with `model: economy` → THEN the worker is launched with the economy model. WHEN Phase 01 searches the store → THEN it runs on the session model. | ADRs `code_search_tier`, `code_search_agent`, `bundle_store_lookup_unit` |
| R-5 | A search not launched as the unit SHALL run inline. | WHEN the host cannot launch the worker → THEN the search runs inline on the session model and the session says so once. | brief A1; governing Host support |
| R-6 | `model` SHALL be a valid key on `specification` and `implementation`. | WHEN a project file sets `phases.implementation.model: economy` → THEN it is honoured. WHEN it sets `phases.feature-analysis.model` → THEN it is ignored and mentioned once. | brief A3; ADR `code_search_tier` |
| R-7 | The template SHALL be `version: 2` with `model: economy` on `specification` and `implementation`. | WHEN a new project file is written → THEN it has `version: 2` and both keys. | brief A4; ADR `template_version_2` |
| R-8 | Upgrading an existing project file SHALL keep its effective settings. | WHEN a version-1 file is upgraded → THEN it gains `model: inherit` on 04 and 05 and `version: 2`, and no setting changes. | ADR `template_version_2`; governing `:855–859` |
| R-9 | Phase skills 02, 05 and `interview` SHALL point to the search unit. | WHEN a reader is at 02 Steps 2/3, 05 Step 3 or the interview lookup rule → THEN one line points to Subagent Execution → Search. | brief A5; DD-3 |
| R-10 | The gate test SHALL run a five-point self-check before the verifier and record it. | WHEN a phase's gate test starts → THEN the summary shows `Self-check: done — N fixes` above the gate table. | brief B1; ADR `self_check_interview_structure` |
| R-11 | A second verifier run SHALL re-check only failed rows and rows whose evidence file changed, and the workflow SHALL stop if a re-checked row still fails. | WHEN run 1 fails one row and the fix edits one file → THEN run 2 re-checks that row and the rows citing that file; others read `confirmed (run 1)`. WHEN a re-checked row still fails → THEN the workflow stops (a stop). | brief B2 |
| R-12 | The verifier and every decision seat SHALL stay on the session model. | WHEN any tier mapping is set → THEN the verifier still runs on the session model. | brief §4 |
| R-13 | Restated copies SHALL match their source. | WHEN the change lands → THEN the README template equals the governing template, and ARCHITECTURE, README tiers and the worker description name the search. | DD-12 |
| R-14 | Each launched search SHALL be logged with the existing subagent line, naming the tier and the model. | WHEN a search unit is launched → THEN `log.md` gets `- **HH:MM — [PHASE] subagent** — search: <question> · model: <tier> → <model> (<source>)`, and the log format section is unchanged. | brief A6 |
| R-15 | A search work order SHALL state the question, the breadth (`quick` · `medium` · `thorough`) and the start place if known; independent searches MAY run in parallel. | WHEN two searches answer independent questions → THEN both may run at once, each with its own work order. | brief A2 |
| R-16 | The change SHALL NOT add a host-wide default subagent model. | WHEN the change lands → THEN the only model settings are `phases.<phase>.model` and `models.<tier>`. | brief §4 |

## How it will be built and checked

Six phases: configuration → search unit → gate test → pointers → restated copies → verification.
Nineteen text checks T-1 – T-19 ([Test Plan](../../bundles/2026-11-05.use_cheaper_subagent_to_work/phase-04-specification/phase.md#implementation-plan)).
