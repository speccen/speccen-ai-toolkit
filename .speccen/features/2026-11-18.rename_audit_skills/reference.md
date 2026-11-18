---
type: Reference
phase: "08 — Reference"
status: COMPLETE
description: Reduced Markdown view of the audit-skill rename reference (commit fdbc357, PR #35); reference.html is authoritative
---

[Index](../../bundles/2026-11-18.rename_audit_skills/index.md) · [State](../../bundles/2026-11-18.rename_audit_skills/STATE.md) · [Log](../../bundles/2026-11-18.rename_audit_skills/log.md) · [HTML](./reference.html)

---

> This is the reduced view. [reference.html](./reference.html) is the full, authoritative reference, with all five diagrams.

# Audit Skill Rename — Technical Reference

The five maturity-audit skills get folder names that equal their skill names (`audit-maturity` … `audit-synthesis`). No rubric byte changes, so the rubric hash stays `212cd4db08e1`.

**Facts:**

- Code commit `fdbc357`
- 19 renames (13 `R100`) + 3 modified files · 41 insertions, 39 deletions
- PR #35 merged as `0f6c6b2`
- CI version `26.1118.1` (`a119ddf`, tag `v26.1118.1`)
- Rubric hash `212cd4db08e1` before and after
- 14 of 14 planned checks pass
- Decisions: DD-1 – DD-7 and DD-9 – DD-13 ADOPTED; DD-8 OVERRIDDEN
- 1 deviation (APPROVED, delegated)

**Scope.** This reference covers the changed files only: the five `skills/audit/` folders, `compare_scorecards.py`, `commands/audit.md`, `ARCHITECTURE.md` and `README.md`. It reads the code on `main` at `a119ddf`. The branch of this reference adds only bundle files. Read down to the layer you need. Each layer is a true picture at its own level.

## L1 — Context

The maturity audit is a second workflow in the plugin. A developer starts it with the command `/speccen:audit`. The command loads the governing skill. The governing skill loads four stage skills in turn. The stages write an audit run to `.speccen/audits/<run>/`.

Before the change, the folder names (`00-governing-audit` … `04-synthesis`) did not equal the skill names. The governing skill was named `app-maturity-audit`. After the change, every folder name equals its `name:` value.

> **Diagram** (drawn in `reference.html`): Context: the developer starts the audit command, which loads the governing skill audit-maturity, which loads four stage skills and manages the audit run folder. The command, the governing skill and the stage skills are changed.
>
> L1 — the command, the governing skill and the four stage skills. All six names or paths changed. The run data and the run layout did not change.

## L2 — The changed files

Commit `fdbc357` touches 22 paths. It renames 19 files with `git mv` and edits 3 files in place. Six of the 19 renamed files also change content. The other 13 are byte-identical (`R100`): 11 rubrics, `build_scorecard.py` and `bundle-conventions.md`.

> **Diagram** (drawn in `reference.html`): Containers: three documents (command, README, ARCHITECTURE) point at the five renamed audit skill folders. The sdd skills, code skills, agents and plugin manifest are unchanged.
>
> L2 — one zoom in from L1. Five folders change name. Three documents change text. Four other groups stay untouched.

### Rename map

| Old folder (`e824b5c`) | New folder | `name:` value | Files |
|---|---|---|---|
| `00-governing-audit/` | `audit-maturity/` | `app-maturity-audit` → `audit-maturity` | 2: `SKILL.md` (R094), `references/bundle-conventions.md` (R100) |
| `01-recon/` | `audit-recon/` | `audit-recon` (equal) | 1: `SKILL.md` (R088) |
| `02-dimension-analysis/` | `audit-dimension-analysis/` | `audit-dimension-analysis` (equal) | 12: `SKILL.md` (R087), 11 rubrics under `references/` (R100) |
| `03-scorecard-review/` | `audit-scorecard-review/` | `audit-scorecard-review` (equal) | 3: `SKILL.md` (R088), `scripts/compare_scorecards.py` (R098), `scripts/build_scorecard.py` (R100) |
| `04-synthesis/` | `audit-synthesis/` | `audit-synthesis` (equal) | 1: `SKILL.md` (R088) |

### Text edits by file

| File | Edit |
|---|---|
| `audit-maturity/SKILL.md` | `name:` becomes `audit-maturity`. Five paths use the new folders. The `description:` line does not change. |
| The four stage `SKILL.md` files | The `description:` names `audit-maturity` instead of `app-maturity-audit`. Each path to a sibling folder uses the new name (recon 3, dimension-analysis 2, scorecard-review 3, synthesis 1). |
| `compare_scorecards.py` | Lines 33 and 34 join `"audit-dimension-analysis"` and `"audit-scorecard-review"` onto `SKILLS_ROOT`. No other line changes. |
| `commands/audit.md` | The command loads `audit-maturity` from `skills/audit/audit-maturity/SKILL.md`. The command name stays `audit`. |
| `ARCHITECTURE.md` | Three lines change. Line 278 names `audit-maturity` … `audit-synthesis`. Line 307 names `skills/sdd/sdd-*/SKILL.md` (by ADR). Line 315 uses the new path. |
| `README.md` | The audit table names the five new folders (it named non-existent `sdd-*` folders). The upgrade note lists the five old audit folders for removal and no longer says "Keep the audit folders". |

## L3 — The rubric-hash path

One component holds the folder names at run time: `compare_scorecards.py`. Its function `rubric_hash()` (lines 29 – 41) hashes everything that decides a score. The script finds the rubrics through `SKILLS_ROOT` (line 23). `SKILLS_ROOT` is `parents[2]` of the script. The script keeps its depth, so `SKILLS_ROOT` and `PLUGIN_JSON` still resolve.

> **Diagram** (drawn in `reference.html`): Components of compare_scorecards.py: stamp and compare call rubric_hash, which uses SKILLS_ROOT and reads the rubrics, build_scorecard.py and an optional weights.json. The two folder names in rubric_hash are changed. The files it reads moved but have the same bytes.
>
> L3 — the components on the hash path. The two string literals at lines 33 and 34 are the only run-time code that names a folder.

```python
def rubric_hash(run):
    h = hashlib.sha256()
    files = sorted((SKILLS_ROOT / "audit-dimension-analysis" / "references").glob("*.md"))   # line 33
    files.append(SKILLS_ROOT / "audit-scorecard-review" / "scripts" / "build_scorecard.py")  # line 34
    if (run / "weights.json").exists():
        files.append(run / "weights.json")
    for f in files:
        h.update(f.name.encode())      # base name only
        h.update(f.read_bytes())       # bytes
    return h.hexdigest()[:12]
```

Line 243 recomputes the hash for the current run when a `compare` starts. Function `comparability()` (line 148) writes the warning "Not like-for-like" when two runs carry different hashes.

## Contracts

**Service Contracts.** This change has no business service contract. The plugin has no DI container, no controller and no external service boundary.

**Boundary the host sees.** A host loads a skill by its folder name and reads `name:` from the frontmatter. After the change, the two are equal for all 18 skills under `skills/*/*/` (check T-2). The command `/speccen:audit` keeps its name and its file.

**Component API.** The script `compare_scorecards.py` offers two commands and one function:

| Item | Behaviour | Changed? |
|---|---|---|
| `stamp <run_dir> [--app NAME]` | Writes `run.json` with id, date, app, commit, toolkit version and rubric hash. | No |
| `compare <run_dir>` | Writes `trend.md`, and regenerates `history.md` and `history.json`. | No |
| `rubric_hash(run) -> str` | Returns 12 hex digits. Input: base names and bytes of 11 rubrics, `build_scorecard.py` and an optional `weights.json`. | Two folder names inside. Same signature, same result. |

## Two argument-diagrams

### 1. The hash input is base names and bytes, not directories

A folder move changes the path of every hashed file. The hash still stays `212cd4db08e1`, because the hash never reads the folder part. This is the reason the folder move is safe.

> **Diagram** (drawn in `reference.html`): Two different paths, the old numbered folder and the new audit folder, give the same base name and bytes, so both give the hash 212cd4db08e1.
>
> Argument-diagram 1 — two different paths, one input to the hash. Shown for two of the 12 files; the other 10 follow the same rule (T-6 checks that all 12 keep their blob ids).

The same fact makes a stale folder name dangerous. A stale name at line 33 does not stop the script: the glob returns an empty list, the hash covers only the scorer, and the hash silently differs. A stale name at line 34 stops the script with `FileNotFoundError`. Checks T-4 and T-8 guard both.

### 2. Same-day run ids sort as text

The function `load_all()` orders runs by `(date, id)`. The T-4 fixture first used the id `2026-11-18.after` for the run after the rename. The id sorts before `2026-11-18.baseline`. The script then took the new run as the first run and compared nothing. It gave no warning. The first T-4 result looked clean for that reason.

> **Diagram** (drawn in `reference.html`): Two orderings of the same two runs. In the first, the id 2026-11-18.after sorts before 2026-11-18.baseline and nothing is compared. In the second, the id 2026-11-19.after sorts after the baseline and the two runs are compared.
>
> Argument-diagram 2 — one id decides whether the comparison runs. A mutation test (a changed hash that must warn) exposed the empty comparison.

## What changed, and why

The change is a pure rename. The brief set these limits: no content change beyond paths and names, no edit to a rubric or to `build_scorecard.py`, one commit with a fixed message, and no edit to `.speccen/` history. The rest of this section shows the decisions that shaped the result.

### Verdict on each part of the change

| Part | Verdict | Reason |
|---|---|---|
| Five folder renames with `git mv` | Required | Folder equals `name:`. Git records 19 renames, so history follows the files. |
| `name: audit-maturity` in the governing skill | Required | The folder name and the skill name must be equal. The `description:` line stays as it was (T-7). |
| Lines 33 – 34 of `compare_scorecards.py` | Required for correctness | A stale name at line 33 changes the hash silently. A stale name at line 34 stops the script. |
| `commands/audit.md` | Required | The command loads the governing skill by name and path. The command name stays `audit`. |
| Stage `description:` lines (DD-9) | Required by the acceptance search | The old name in those four lines would fail Verification 1. Only the name changes. |
| README audit table | Required for correctness | The table named `sdd-*` folders that do not exist. |
| README upgrade note (DD-10) | Placement choice | The note could keep its old opening. The Architect-approved text names the audit rename, as the model commit `1c41496` does. |
| `ARCHITECTURE.md` lines 278 and 315 | Required | Both lines restate a folder name or a path. |
| `ARCHITECTURE.md` line 307 | Placement choice, set by ADR | The fix could have waited as a follow-up (DD-8). The Architect decided to include it. See below. |

### Decisions, with status as recorded

The bundle ran in autonomous mode. The delegate took 13 decisions. The Architect reviewed all of them. This table shows each status as recorded in `delegated-decisions.md`. This reference does not set any status.

| Id | Decision | Status as recorded |
|---|---|---|
| DD-1 | The whole `.speccen/` stays unchanged, apart from this bundle and its graduation. | ADOPTED — the Architect, review round |
| DD-2 | "One commit" means one code commit. Bundle phase commits are separate. | ADOPTED — the Architect, review round |
| DD-3 | Push and PR wait for the Architect's go. | ADOPTED — the Architect, review round |
| DD-4 | The commit message is the brief's message, with no attribution trailer. | ADOPTED — the Architect, review round |
| DD-5 | Reach: every restatement of an old name, not only the places the brief lists. | ADOPTED — the Architect, review round |
| DD-6 | The hash baseline is the hash computed on `main` at `e824b5c`. | ADOPTED — the Architect, review round |
| DD-7 | Append `\b` to the `sdd-(…)` group of Verification 1. Recorded materiality: MATERIAL — unconfirmed. | ADOPTED — the Architect, review round |
| DD-8 | Leave `ARCHITECTURE.md:307` and report it as a follow-up. | OVERRIDDEN — the Architect, review round: "dd-8 update both readme and architecture md's". ADR: `2026-11-18.architecture_reading_guide_sdd_path` |
| DD-9 | The four stage `description:` lines change the name only. | ADOPTED — the Architect, review round |
| DD-10 | The README upgrade note also names the audit rename. | ADOPTED — the Architect, review round |
| DD-11 | T-4 runs on a synthetic run in the scratchpad. Nothing is committed. | ADOPTED — the Architect, review round |
| DD-12 | The checks live in `files/phase-05-text-checks.py`, outside the code commit. | ADOPTED — the Architect, review round |
| DD-13 | Deviation 1: run T-4 in Python UTF-8 mode. | ADOPTED — the Architect, review round |

### DD-7 — tighten the acceptance search

The brief's Verification 1 search must find the old names only in the README upgrade note. The brief's regex also matches `sdd-reconcile`: 9 false hits (Phase 02, group C). The delegate appended `\b` after the `sdd-(governing-audit|recon|dimension-analysis|scorecard-review|synthesis)` group. At the start the search gives 32 hits, none of them `sdd-reconcile`. After the change it gives 4 hits, all in the README note (lines 132, 133, 137, 138).

| Option | Taken? | Reason |
|---|---|---|
| `\b` after the group | Taken | It removes the 9 false hits. It keeps the rest of the search as the brief wrote it. |
| A trailing `/` after the group | Rejected | It misses a bare `sdd-recon` that has no slash. |
| `\| grep -v sdd-reconcile` | Rejected | It hides any line that holds both `sdd-reconcile` and a real old name. |

### DD-8 — the Architect overrides the delegate

The delegate chose to leave `ARCHITECTURE.md:307` (`skills/sdd/NN-*/SKILL.md`, a stale path from an earlier rename) because the brief says "keep this commit a pure rename". The Architect overrode that choice in the review round. The ADR records the decision and its scope.

| Option | Outcome | Reason |
|---|---|---|
| Leave line 307 and report a follow-up (DD-8) | OVERRIDDEN | The Architect asked to update both documents. |
| Fix line 307 in this change, folded into the one code commit with its message unchanged | Taken (ADR) | The Architect accepted: only `ARCHITECTURE.md:307`, fold into the code commit, keep the message (interview 06/18 – 06/20). |
| Change a README line too | Not needed | A search of `README.md` found no stale `sdd` skill path. The README does not change for this ADR. |

Effect: the fix was folded with a fixup rebase. The code commit changed from `6c6187c` to `fdbc357`. The diff grew from 40 to 41 insertions and from 38 to 39 deletions. Check T-14 was added. The ADR records no consequences (the Architect stated none).

### DD-13 and the other test-method decisions

| Decision | Option | Taken? | Reason |
|---|---|---|---|
| DD-13 — the scorer fails on this Windows host | Run T-4 with `-X utf8` | Taken | It changes how the check runs, not the code. The scorer stays byte-identical (T-6). |
| DD-13 — the scorer fails on this Windows host | Fix `build_scorecard.py` in this change | Rejected | It changes the rubric hash and breaks the brief's invariant. |
| DD-13 — the scorer fails on this Windows host | Stop and ask | Rejected | No scope change was needed. |
| DD-11 — where T-4 runs | A synthetic run in the session scratchpad | Taken | It commits nothing and leaves `.speccen/audits/` clean. |
| DD-11 — where T-4 runs | A run under `.speccen/audits/` of this repository | Rejected | It adds run data to the repository history. |
| DD-9 — stage descriptions | Replace the name only | Taken | It follows the brief's invariant on content. |
| DD-9 — stage descriptions | Leave the descriptions | Rejected | Verification 1 would then fail. |

No Phase 03 prototype ran (`prototypes: 0`): no material choice had competing approaches to build.

## Deviations

**Deviation 1 — T-4 needs Python UTF-8 mode on Windows.** Decision: APPROVED (delegated), [DD-13](../../bundles/2026-11-18.rename_audit_skills/delegated-decisions.md#dd-13). Purpose preserved: yes. Detail: [phase 05, Deviations](../../bundles/2026-11-18.rename_audit_skills/phase-05-implementation/phase.md#deviations).

**Planned.** Run `stamp`, `build_scorecard.py` and `compare` end to end.

**Actual.** `build_scorecard.py` stops with `UnicodeEncodeError: 'charmap' codec can't encode character` for the star symbol. The failing call is `(out_dir / "scorecard.md").write_text(...)` at line 391. The call has no `encoding` argument, so Python on Windows writes cp1252, and cp1252 has no star. With `-X utf8` all three scripts exit 0.

**Why not fix it.** The file is byte-identical to `e824b5c`, so the error predates the rename. The brief forbids any edit to the file. An edit would change the rubric hash and mark every later run "not like-for-like" against earlier runs.

**Resolution.** The durable store holds the lesson `2026-11-18.audit_scorer_needs_utf8_and_fix_changes_hash`. A fix needs its own decision on the hash break. Until then, run the audit scripts with `python -X utf8` on Windows.

A second finding came from the T-4 fixture, not from the code: the run-id sort order (argument-diagram 2). It is not a deviation. The durable store holds it as the lesson `2026-11-18.same_day_audit_runs_sort_by_id`. The fixture id changed from `2026-11-18.after` to `2026-11-19.after` with no change to the plan.

## Checks

The plan has 14 checks. The script `files/phase-05-text-checks.py` runs 13 of them (T-1 – T-3, T-5 – T-14). T-4 runs by hand because it needs a synthetic run. Every expected value comes from the plan and the brief, not from the code. The script reads texts from git objects. Result: 14 of 14 pass.

| Check | What it proves | Result |
|---|---|---|
| T-1 | Old names appear only in the README upgrade note (DD-7 search). | PASS — 4 hits (lines 132, 133, 137, 138) |
| T-2 | Folder equals `name:` for every `skills/*/*/SKILL.md`. | PASS — 18 skills, no mismatch |
| T-3 | Every cited `skills/audit/…` path exists. | PASS — 24 cited, 0 missing |
| T-4 | `stamp`, `build_scorecard.py` and `compare` run end to end at the new paths. The new hash equals the baseline. A changed hash warns. | PASS — by hand, see below |
| T-5 | 19 renames under `skills/audit/`, 13 `R100`. | PASS |
| T-6 | All 12 hash inputs keep their blob ids. | PASS — 12 inputs, same ids |
| T-7 | The governing `description:` line is equal to the old one. | PASS |
| T-8 | Nine text files equal the substitution map applied to the `e824b5c` text. | PASS — 9 files |
| T-9 | The README upgrade note equals the planned text. | PASS |
| T-10 | Change set: 19 renames plus `ARCHITECTURE.md`, `README.md`, `commands/audit.md`, and nothing else. | PASS |
| T-11 | One code commit, the brief's message, no attribution. | PASS |
| T-12 | `.speccen/` changes only in this bundle and its graduation. | PASS |
| T-13 | `skills/sdd`, `skills/code` and `agents` are unchanged. | PASS |
| T-14 | `ARCHITECTURE.md` has no `NN-*` path, and line 307 names `skills/sdd/sdd-*/SKILL.md` (added for the ADR). | PASS |

### The T-4 run

1. A synthetic run of 11 `dimensions/<dim>/result.json` files sits in the session scratchpad. Nothing is committed (DD-11).
1. The baseline run `2026-11-18.baseline` was stamped in Phase 02 with the skills as at `e824b5c`. Its `rubric_hash` is `212cd4db08e1`.
1. The new run `2026-11-19.after` runs on the renamed tree. `stamp` writes `rubric_hash` `212cd4db08e1`. `build_scorecard.py` and `compare` exit 0.
1. `trend.md` compares against `2026-11-18.baseline` and holds 0 "Not like-for-like" lines.
1. Mutation: the same run with a `weights.json` gives the warning "Not like-for-like: rubrics/scorer changed between these runs (rubric hash differs)". The check detects a change.
1. All commands ran with `python -I -B -X utf8` (Deviation 1).

**Move tests.** The mutations of T-1, T-8, T-9 and T-14 each change one expected text in memory. Each run then reports a failure for that check only. After the ADR fold, T-4 was not run again end to end: the fold changes only `ARCHITECTURE.md`, which is no input of the scripts or of the hash. The hash at `fdbc357` is still `212cd4db08e1`.

**Release.** PR #35 merged as `0f6c6b2`. CI then bumped the version to `26.1118.1` (`a119ddf`, tag `v26.1118.1`). The code commit does not touch the version (T-10).

## Known limitations and follow-ups

- **The scorer fails on Windows without UTF-8 mode.** `build_scorecard.py:391` writes `scorecard.md` with the platform encoding. A fix changes the rubric hash, so it needs its own decision. Follow-up: decide the hash break, then fix the file.
- **Same-day run ids sort as text.** A later run needs an id that sorts after its baseline. Otherwise `compare` compares nothing and does not warn. Test each "no warning" check with a mutation that must warn.
- **The hash reads bytes, so line endings count.** The value `212cd4db08e1` is the hash of the git blobs (LF) at `a119ddf`. A working tree with CRLF endings gives another value. The Phase 04 risk table names this risk. Observed while this reference was written: on the Windows checkout of the docs branch (`core.autocrlf=true`, working-tree files CRLF, index LF), `rubric_hash()` returns `6c10c0ec3ace`. The bundle does not record this value as a finding. Compare hashes only between runs made on the same line endings.
- **The README upgrade note keeps the old names on purpose.** It lists the five old audit folders for removal. Those 4 lines are the only hits of the DD-7 search.
- **Old paths remain in `.speccen/` history.** DD-1 leaves the durable store and earlier bundles unchanged.
- **Installed copies update after a release.** A host session that loaded the plugin before the release still lists the old audit skill names until the plugin cache updates.

## References

### Source map

| Item | Where |
|---|---|
| Code commit | `fdbc357` — `refactor: prefix the audit skills with audit- and drop the folder numbers` |
| Hash path | `skills/audit/audit-scorecard-review/scripts/compare_scorecards.py`, lines 23, 29 – 41, 148, 243 |
| Rename map and commit range | `git diff -M --name-status e824b5c fdbc357 -- skills/audit` · `git log --oneline e824b5c..a119ddf` |
| Scorer defect | `skills/audit/audit-scorecard-review/scripts/build_scorecard.py:391` |
| Checks | `files/phase-05-text-checks.py` (in the bundle) |

### Bundle basis

- Phase 01 — [feature analysis](../../bundles/2026-11-18.rename_audit_skills/phase-01-feature-analysis/summary.md): the brief, DD-1 – DD-6.
- Phase 02 — [code analysis](../../bundles/2026-11-18.rename_audit_skills/phase-02-code-analysis/summary.md): the hash path, the restatement inventory, the baseline `212cd4db08e1`.
- Phase 03 — [compliance and review](../../bundles/2026-11-18.rename_audit_skills/phase-03-compliance-review/summary.md): DD-7 – DD-9, the ADR iteration.
- Phase 04 — [specification](./specification.html) (intent) and its [implementation plan and test plan](../../bundles/2026-11-18.rename_audit_skills/phase-04-specification/phase.md#implementation-plan).
- Phase 05 — [implementation](../../bundles/2026-11-18.rename_audit_skills/phase-05-implementation/summary.md): [Deviation 1](../../bundles/2026-11-18.rename_audit_skills/phase-05-implementation/phase.md#deviations).
- Phase 06 — [technical close-out seed](../../bundles/2026-11-18.rename_audit_skills/phase-06-close-out/doc-technical.md), [business](../../bundles/2026-11-18.rename_audit_skills/phase-06-close-out/doc-business.md) and [executive](../../bundles/2026-11-18.rename_audit_skills/phase-06-close-out/doc-executive.md) seeds.
- Decisions — [delegated-decisions.md](../../bundles/2026-11-18.rename_audit_skills/delegated-decisions.md) (DD-1 – DD-13) and the ADR [2026-11-18.architecture_reading_guide_sdd_path](../../bundles/2026-11-18.rename_audit_skills/adrs/2026-11-18.architecture_reading_guide_sdd_path.md).
- Durable store — the feature node `2026-11-18.rename_audit_skills` and the two lessons named above.
