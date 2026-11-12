---
type: Index
---

# speccen-ai-toolkit — Durable Store

## Timeline
- [Timeline](./timeline.md) — features & refactorings, oldest-first

## Features
- [Use cheaper subagent to work](./features/2026-11-05.use_cheaper_subagent_to_work/node.md) — active
- [Set allowed budget for autonomous phases](./features/25.set_allowed_budget_for_autonomous_phases/node.md) — active

## Decisions
- [Searches share the phase's `model` tier — no separate search key](./decisions/2026-11-05.code_search_tier.md) — active
- [Searches run on `speccen-worker`, not on a host's built-in search agent](./decisions/2026-11-05.code_search_agent.md) — active
- [One search unit for code, bundle and store](./decisions/2026-11-05.bundle_store_lookup_unit.md) — active
- [The gate-test self-check has a fifth check: interview structure](./decisions/2026-11-05.self_check_interview_structure.md) — active
- [A gate test makes no progress when a breach comes back or more rows fail — not when fewer rows fail](./decisions/2026-11-11.fix_progress_by_breaches.md) — active
- [The fix budget is at most 10 fix attempts; an invalid value counts as 1](./decisions/2026-11-11.fix_budget_ceiling_10.md) — active
- [The fix budget defaults to 5 fix attempts; absence and the upgrade both mean 5](./decisions/2026-11-12.fix_budget_default_5.md) — active

## Lessons learned
- [Fix the term list before writing STE seeds](./lessons/2026-11-05.ste_term_list_before_writing.md) — active
- [The README holds a full copy of the config template — change both together](./lessons/2026-11-05.readme_restates_config_template.md) — active
- [A text check reads only the place its plan row names — test it with a move test](./lessons/2026-11-11.text_checks_read_their_place.md) — active
- [Repair every case of a breach type, not only the cases the verifier names](./lessons/2026-11-11.repair_every_case_of_a_breach.md) — active
- [Write decision records and final edits first; lists, render and summary last](./lessons/2026-11-11.write_lists_and_summary_last.md) — active

## Notes
