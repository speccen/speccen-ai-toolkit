---
type: Index
---

# speccen-ai-toolkit — Durable Store

## Timeline
- [Timeline](./timeline.md) — features & refactorings, oldest-first

## Features
- [Use cheaper subagent to work](./features/2026-11-05.use_cheaper_subagent_to_work/node.md) — active
- [Set allowed budget for autonomous phases](./features/2026-11-12.set_allowed_budget_for_autonomous_phases/node.md) — active
- [Questions to the Architect: [number | text] subjects, never a bare label](./features/2026-11-13.questions_to_the_architect_number_text_subjects_never_a_bare_label/node.md) — active
- [Use narrow verifier for phase checks](./features/2026-11-15.use_narrow_verifier_for_phase_checks/node.md) — active
- [Rename audit skills](./features/2026-11-18.rename_audit_skills/node.md) — active

## Decisions
- [Searches share the phase's `model` tier — no separate search key](./decisions/2026-11-05.code_search_tier.md) — active
- [Searches run on `speccen-worker`, not on a host's built-in search agent](./decisions/2026-11-05.code_search_agent.md) — active
- [One search unit for code, bundle and store](./decisions/2026-11-05.bundle_store_lookup_unit.md) — active
- [The gate-test self-check has a fifth check: interview structure](./decisions/2026-11-05.self_check_interview_structure.md) — active
- [A gate test makes no progress when a breach comes back or more rows fail — not when fewer rows fail](./decisions/2026-11-11.fix_progress_by_breaches.md) — active
- [The fix budget is at most 10 fix attempts; an invalid value counts as 1](./decisions/2026-11-11.fix_budget_ceiling_10.md) — active
- [The fix budget defaults to 5 fix attempts; absence and the upgrade both mean 5](./decisions/2026-11-12.fix_budget_default_5.md) — active
- [Labels stay and travel inside a `[number | text]` subject — never a bare label](./decisions/2026-11-15.labels_travel_inside_subjects.md) — active
- [A fix that only repairs how a decision is recorded is not a stop](./decisions/2026-11-15.record_repair_is_not_a_stop.md) — active

## Lessons learned
- [Fix the term list before writing STE seeds](./lessons/2026-11-05.ste_term_list_before_writing.md) — active
- [The README holds a full copy of the config template — change both together](./lessons/2026-11-05.readme_restates_config_template.md) — active
- [A text check reads only the place its plan row names — test it with a move test](./lessons/2026-11-11.text_checks_read_their_place.md) — active
- [Repair every case of a breach type, not only the cases the verifier names](./lessons/2026-11-11.repair_every_case_of_a_breach.md) — active
- [Write decision records and final edits first; lists, render and summary last](./lessons/2026-11-11.write_lists_and_summary_last.md) — active
- [Escape `|` in every table cell, also inside backticks](./lessons/2026-11-15.escape_bar_in_table_cells.md) — active
- [A breach kept on purpose still counts as no progress — take it out of the round](./lessons/2026-11-15.kept_breach_is_no_progress.md) — active
- [A gate stop question proposes the fix budget that follows the answer](./lessons/2026-11-15.stop_question_proposes_fix_budget.md) — active
- [Run a plan's error-case text checks on the planned text before Phase 04 closes](./lessons/2026-11-16.run_error_checks_on_planned_text.md) — active
- [A verifier that re-reads the whole phase finds new detail on every run](./lessons/2026-11-16.full_phase_verifier_finds_new_detail.md) — active
- [The audit scorer fails on Windows without UTF-8 mode, and a fix changes the rubric hash](./lessons/2026-11-18.audit_scorer_needs_utf8_and_fix_changes_hash.md) — active
- [Audit runs on the same day sort by id, so a run named before "baseline" is taken as the earlier run](./lessons/2026-11-18.same_day_audit_runs_sort_by_id.md) — active

## Notes
