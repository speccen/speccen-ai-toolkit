---
type: Phase
phase: "01 — Feature Analysis"
status: COMPLETE
description: Pure rename of the five audit skills to audit-<role> (folder = frontmatter name), with every path, the script rubric paths, the command, ARCHITECTURE and README updated
---

<a id="phase-top"></a>
# rename audit skills — Feature Analysis

[Index](../index.md) · [State](../STATE.md) · [Log](../log.md)

---

<a id="extensions"></a>
## Extensions applied

| Extension | Why | Where it applies | Outcome |
|---|---|---|---|
| — | — | — | No extensions for this phase |

<a id="feature-description"></a>
## Request Description

### Request Summary

**Kind:** refactoring — settled. The brief is titled "Refactor" and asks for "a pure rename";
the session-start Work kind answer is "refactoring" (log 07:56, 07:58).

Rename the five skill folders under `skills/audit/` so that each folder name equals the
skill's frontmatter `name:` and carries the `audit-` prefix, with no numeric folder prefix —
the convention commit `1c41496` applied to `skills/sdd/`. Four stage skills only move their
folder (their `name:` is already the target). The governing audit skill moves from
`00-governing-audit/` to `audit-maturity/` and changes its `name:` from `app-maturity-audit`
to `audit-maturity`, with its `description` unchanged.

Every reference to the old folders or the old name outside `.speccen/` is updated: the
`skills/audit/0N-*` paths inside the five `SKILL.md` files, the two folder names that
`compare_scorecards.py` joins onto `SKILLS_ROOT` (runtime-critical), the `/speccen:audit`
command's target skill and path, `ARCHITECTURE.md`, and `README.md` — whose audit table the
`1c41496` rename pointed at `sdd-*` folders that do not exist, and whose install/upgrade note
must list the five old audit folders for removal.

The change must not alter rubric file names or contents (so the rubric hash stays
comparable), the audit run layout and ids, the `.speccen/` history, the `/speccen:audit`
command name, or any skill content beyond path and name references.

**Done when:** the brief's Verification 1 – 5 hold — no old name outside `.speccen/` and
`.git/` except the README upgrade note; every skill folder equals its frontmatter name; every
cited `skills/audit/...` path exists; the scripts run end to end with a `rubric_hash` equal to
the pre-rename hash on `main`; `git diff -M` shows the five folders as renames — and the change
is one commit on `refactor/audit-prefixed-skill-names` with the brief's commit message.

### Domain Context

The repository is the speccen plugin (Claude Code / Copilot CLI): skills grouped under
`skills/sdd/`, `skills/code/` and `skills/audit/`, plus commands and agents. A skill's
frontmatter `name:` is how a host lists and invokes it; the folder is how paths in other
skills, commands, scripts and docs reach it. When the two differ, or carry numeric ordering
prefixes, the names a user sees and the paths a maintainer edits drift apart — the
inconsistency `1c41496` removed for `skills/sdd/` and that now remains only in
`skills/audit/`.

The audit skills implement the Application Maturity Audit (`/speccen:audit`): recon,
dimension scoring against rubrics, a scorecard with a human review gate, and synthesis. Its
scripts stamp each run with a hash of the rubric files, so later runs can be compared
like-for-like; that hash is the one runtime behaviour the rename can break.

### Scope

**In scope** (brief, Required changes 1 – 8):
- `git mv` of the five folders, with their `references/` and `scripts/`;
- `name:` of the governing skill → `audit-maturity`;
- the `skills/audit/0N-*` paths in the five `SKILL.md` files;
- `compare_scorecards.py` — the two folder names joined onto `SKILLS_ROOT`;
- `commands/audit.md` — target skill name and path;
- `ARCHITECTURE.md` — the audit folder list and the governing skill path;
- `README.md` — the audit table, and the install/upgrade note (add the five old folders to the
  removal list, drop "Keep the audit folders (…)");
- any other reference to `app-maturity-audit` or an old audit folder outside `.speccen/`.

**Out of scope:**
- the stale counts and wording the same review found ("ten dimensions", "three signals", the
  legacy-cluster description, the "Weight column") — a separate change;
- any file under `audit-dimension-analysis/references/` and `build_scorecard.py` — not edited at
  all (rubric hash);
- `.speccen/` — the bundles and, per DD-1, the durable store entries, apart from this bundle
  and its Phase 06 graduation;
- renaming the `/speccen:audit` command;
- a manual version bump (CI does it);
- the separately installed standalone `app-maturity-audit` plugin (DD-4 basis: the brief names
  only repository paths).

**Unclear** — see [Open Questions](#open-items): where else the old names are restated (O-1,
Phase 02), and how historic records outside `.speccen/` are treated, if Phase 02 finds any
(O-2, Phase 03).

### Key Concepts & Terminology

| Term | As the brief uses it |
|---|---|
| audit skills | the five skills in `skills/audit/`: the governing audit skill and the four stage skills (recon, dimension analysis, scorecard review, synthesis) |
| `audit-<role>` | the target naming: folder name = frontmatter `name:` = `audit-` + role, no numeric prefix |
| governing skill | `00-governing-audit/` · `app-maturity-audit` → `audit-maturity/` · `audit-maturity` |
| stage skills | `audit-recon`, `audit-dimension-analysis`, `audit-scorecard-review`, `audit-synthesis` — name already right, folder moves |
| the `1c41496` convention | the rule commit `1c41496` applied to `skills/sdd/`; the model for scope and style |
| `SKILLS_ROOT` | the base path `compare_scorecards.py` joins skill folder names onto to find rubrics |
| rubric hash (`rubric_hash()`) | a hash over rubric file names and contents (not directories), stamped in a run's `run.json`; must stay equal across the rename |
| like-for-like | two audit runs whose rubric hashes match, so their scorecards compare |
| upgrade note | `README.md:117-136`, the list of old folders to remove before copying the plugin over an older install |
| records | `.speccen/bundles/**` history that keeps old paths on purpose |

<a id="hypotheses"></a>
## Working Hypotheses

| # | Hypothesis | Confirms / refutes | Settles in |
|---|---|---|---|
| H-1 | The brief's file and line citations (README :53-57, :117-136; ARCHITECTURE :278, :315; `commands/audit.md:9-10`; `compare_scorecards.py:33-34`; the `SKILL.md` lines) match HEAD `e824b5c`. | Phase 02 reads each cited place (P02-1). | Phase 02 |
| H-2 | `compare_scorecards.py` is the only script that builds paths from audit folder names; in particular `build_scorecard.py` holds no old folder name. If it does, the invariant "do not edit `build_scorecard.py`" conflicts with Required change 8. | Phase 02 searches every file under `skills/audit/**/scripts/` (P02-2). A conflict found is a hard stop (stop condition 2). | Phase 02 |
| H-3 | Old names are restated in places beyond those the brief lists — under Required change 8 these are in scope (lesson `2026-11-05.readme_restates_config_template`). From 01/5. | Phase 02 runs the brief's Verification 1 search before any change and lists every hit (P02-3). | Phase 02 (places); Phase 03 (O-2, if any hit is a historic record) |
| H-4 | The rubric hash does not depend on directory names, so moving the folders leaves it equal; the baseline is the hash computed on `main` at `e824b5c` before any move. From 01/6. | Phase 02 reads `rubric_hash()` and computes the baseline on a throwaway run (P02-4). | Phase 02 (fact and baseline); Phase 04 (the check) |

<a id="open-items"></a>
## Open Questions

| # | Open item | Settles in |
|---|---|---|
| O-1 | Facts in the code: P02-1 — the cited lines match HEAD (H-1); P02-2 — no other script holds an old audit folder name (H-2); P02-3 — every place the Verification 1 search hits before the change (H-3); P02-4 — how `rubric_hash()` is computed, and the baseline hash at `e824b5c` (H-4); P02-5 — whether any plugin manifest (`.claude-plugin/`) or marketplace file lists skill paths. | Phase 02 |
| O-2 | If Phase 02 finds old names in historic records outside `.speccen/` (for example a changelog entry), are they updated or kept as records? | Phase 03 |
| O-3 | The Test Plan: the brief's Verification 1 – 5 as checks, each run against the planned text in Phase 04 (lesson `2026-11-16.run_error_checks_on_planned_text`) and scoped to its place (lesson `2026-11-11.text_checks_read_their_place`). | Phase 04 |

None of these blocks Phase 02: the brief names the system (this repository's `skills/audit/`)
and every file to analyse.

<a id="interview"></a>
## Interview

Mode: `autonomous` (bundle config); `stops: proceed` (project config). The delegate answered
from the decision basis: the Architect's own words in `log.md` — the session-start answers
(07:56), the name (07:57) and the brief (07:58, recorded verbatim). The bundle has no ADR; no
standing decision in the durable store bears on a rename of skill folders. Prior art used: lesson
`2026-11-05.readme_restates_config_template` (01/5).

The brief states the five essentials clearly — kind ("Refactor"), problem (Context), outcome
(Goal, Target names), scope (Required changes, Invariants, Out of scope) and done when
(Verification, Delivery) — so they are not asked again. Round 1 holds what the brief leaves to
interpretation; no question depends on another, so there is one round.

**Round 1**

| # | Question | Depends on | Proposed | Answer |
|---|---|---|---|---|
| 01/1 | Store scope — leave the whole `.speccen/` unchanged (the durable store entries too, not only `bundles/**`), apart from this bundle and its Phase 06 graduation? | — | yes | delegate: yes — basis: brief Verification 1 excludes `.speccen/` entirely (`--exclude-dir=.speccen`); Invariant ".speccen/ history" (log 07:58) — [DD-1](../delegated-decisions.md#dd-1) |
| 01/2 | "One commit" — read it as one commit for the code change, with the bundle's phase-boundary commits (`chore: complete … PHASE [skip ci]`) as separate commits on the same branch? | — | yes | delegate: yes — basis: brief Delivery "one commit" with a code-change message (log 07:58); governing skill, Phase Transition Protocol step 6 — [DD-2](../delegated-decisions.md#dd-2) |
| 01/3 | Push and PR — after close-out, wait for the Architect's go before `git push` and opening the PR to `main`, since both are external side effects? | — | yes | delegate: yes — basis: governing skill, stop condition 7 (external side effects); brief Delivery names the PR but not when (log 07:58) — [DD-3](../delegated-decisions.md#dd-3) |
| 01/4 | Commit message — use the brief's message verbatim, with no attribution trailer? | — | yes | delegate: yes — basis: brief Delivery message (log 07:58); governing skill, Invariant 6 — [DD-4](../delegated-decisions.md#dd-4) |
| 01/5 | Reach — bring every place that restates an old audit name into line, beyond the places the brief lists? | — | yes, as a working hypothesis | hypothesis: as proposed (H-3) — basis: brief Required change 8; lesson `2026-11-05.readme_restates_config_template`; places → P02-3; historic records settle in Phase 03 (O-2) — [DD-5](../delegated-decisions.md#dd-5) |
| 01/6 | Hash baseline — take the `rubric_hash` computed on `main` at `e824b5c` before any move as the reference for Verification 4? | — | yes, as a working hypothesis | hypothesis: as proposed (H-4) — basis: brief Verification 4 "equals the hash computed on `main` before the rename" (log 07:58); computed in Phase 02 (P02-4), checked in Phase 04 (O-3) — [DD-6](../delegated-decisions.md#dd-6) |

No question was answered "later". Every delegated decision of this phase is `not material`.

<a id="outcome"></a>
## Outcome

The request is a pure rename of the five `skills/audit/` skills to `audit-<role>`, where the
folder equals the frontmatter name, following the `1c41496` model. The rename comes with path
updates in the skills, the `compare_scorecards.py` rubric paths, the command, `ARCHITECTURE.md`
and `README.md`. The rubric hash, the run layout and the `.speccen/` history do not change.
Phase 02 confirms the cited places, finds every other restatement and computes the baseline
rubric hash (O-1).
