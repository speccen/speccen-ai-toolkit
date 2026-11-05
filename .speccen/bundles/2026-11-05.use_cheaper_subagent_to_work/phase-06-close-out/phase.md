---
type: Phase
phase: "06 — Close-out"
status: COMPLETE
description: Three audience seeds, feature node and graduated specification written; graduation proposal pending the Architect
---

<a id="phase-top"></a>
# Use cheaper subagent to work — Close-out

[Index](../index.md) · [State](../STATE.md) · [Log](../log.md)

---

<a id="extensions"></a>
## Extensions applied

| Extension | Why | Where it applies | Outcome |
|---|---|---|---|
| — | — | — | No extensions for this phase: `.speccen/extensions/close-out/` does not exist |

## Checklist

All Implementation Plan items are ticked; none skipped →
[Phase 05 Implementation Summary](../phase-05-implementation/phase.md#implementation-summary)
(Phase 04 is closed, so the ticks are recorded in Phase 05).

<a id="documentation"></a>
## Documentation

- [doc-executive.md](./doc-executive.md), [doc-business.md](./doc-business.md),
  [doc-technical.md](./doc-technical.md) — written inline (Steps 3–5), STE-styled with the
  Phase 04 term list (main session, worker, verifier, model tier, search question, evidence).
  Each links its Phase 04 intent seed; intended → delivered is the same, no deviation.

## Durable store

- `.speccen/` had no store yet; created: `index.md`, `timeline.md`,
  `features/2026-11-05.use_cheaper_subagent_to_work/` (`node.md`, `specification.html`,
  `specification.md`).
- Overrides (path 1): none — no Tier-2 decision exists, so no Phase 03 ADR overrides one.
- The graduated specification's relative links were rebased onto
  `../../bundles/2026-11-05.use_cheaper_subagent_to_work/` so they resolve from the feature
  folder; every link was checked to exist. They break once the bundle is deleted (git history
  keeps the targets).
- `produced: []` — nothing discretionary is written before the Architect decides the proposal.

<a id="graduation-proposal"></a>
## Graduation Proposal

Pending the Architect (autonomous: path 2 is not decided by the delegate). Default is *keep local*.

| # | Candidate | Kind | Proposed | Evidence |
|---|---|---|---|---|
| G-1 | ADR `code_search_tier` — searches share the phase `model` tier; no separate key | decision | promote | A fence: a later change may "add a search key"; the ADR records why not. [ADR](../adrs/2026-11-05.code_search_tier.md) |
| G-2 | ADR `code_search_agent` — searches run on `speccen-worker`, not a host's built-in search agent | decision | promote | A fence: a built-in agent looks simpler but ignores the tier model and the no-decision rule. [ADR](../adrs/2026-11-05.code_search_agent.md) |
| G-3 | ADR `bundle_store_lookup_unit` — one search unit for code, bundle and store | decision | promote | Explains the Units row's scope across phases. [ADR](../adrs/2026-11-05.bundle_store_lookup_unit.md) |
| G-4 | ADR `self_check_interview_structure` — the fifth self-check | decision | promote | Explains why the self-check has five checks, not the brief's four. [ADR](../adrs/2026-11-05.self_check_interview_structure.md) |
| G-5 | ADR `template_version_2` — template `version: 2`; missing keys added as `inherit` | decision | keep local | Follows the standing rule "When the template gains a key, its `version` goes up by one"; no new fence. [ADR](../adrs/2026-11-05.template_version_2.md) |
| G-6 | Lesson: the verifier finds new STE defects on each re-check of a seed; fix the term list before writing | lesson | promote | Phase 04 row 12 needed six verifier runs and four stop rounds (04/4 – 04/7) → [Phase 04 summary](../phase-04-specification/summary.md#delegate-gate-check) |
| G-7 | Lesson: the README holds a full copy of the config template; change both together | lesson | promote | Restated site S-1; check T-11 → [Phase 02 restated sites](../phase-02-code-analysis/phase.md#restated-sites) |

<a id="outcome"></a>
## Outcome

Close-out complete under delegation. The skill changes remain uncommitted in the working tree
(DD-15); whether the final commit includes them is put to the Architect in the end-of-run report.

<a id="open-items"></a>
## Open Items

| # | Item | Status |
|---|---|---|
| O-10 | The brief's §6 cost measurement on the next bundle | follow-up |
| G-1 – G-7 | Graduation proposal | pending the Architect |
| C-1 | Commit the seven skill files: Step 10 commits the implementation; DD-15 leaves it uncommitted for the Architect | pending the Architect |
| C-2 | The project config `.speccen/speccen-config.yaml` follows the 26.1103.1 template (no `version` key); a session on the new skill upgrades it to version 2 | note |
