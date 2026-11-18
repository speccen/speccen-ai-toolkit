---
type: Phase
phase: "02 — Code Analysis"
status: COMPLETE
description: Every cited place matches HEAD; four more name references found; rubric hash is name-only (baseline 212cd4db08e1); Verification 1 regex also matches sdd-reconcile (9 hits)
---

<a id="phase-top"></a>
# rename audit skills — Code Analysis

[Index](../index.md) · [State](../STATE.md) · [Log](../log.md)

---

<a id="extensions"></a>
## Extensions applied

| Extension | Why | Where it applies | Outcome |
|---|---|---|---|
| — | — | — | No extensions for this phase |

<a id="code-analysis"></a>
## Code Analysis

All findings are at `e824b5c` (`main`). The branch head `787782d` differs from it only by the
bundle: `git diff --quiet e824b5c -- skills` exits 0.

### Architecture Overview

The plugin declares three skill groups in `.claude-plugin/plugin.json:22-26`
(`"./skills/sdd/"`, `"./skills/audit/"`, `"./skills/code/"`). The manifest names groups, not
skill folders, so a folder rename inside `skills/audit/` does not touch it (P02-5).
`.claude-plugin/marketplace.json` names no skill path.

`skills/audit/` today (19 files):

```
skills/audit/
├── 00-governing-audit/      name: app-maturity-audit   SKILL.md, references/bundle-conventions.md
├── 01-recon/                name: audit-recon          SKILL.md
├── 02-dimension-analysis/   name: audit-dimension-analysis
│                                                       SKILL.md, references/*.md (11 rubrics)
├── 03-scorecard-review/     name: audit-scorecard-review
│                                                       SKILL.md, scripts/build_scorecard.py,
│                                                                 scripts/compare_scorecards.py
└── 04-synthesis/            name: audit-synthesis      SKILL.md
```

Entry points and dependents:
- `commands/audit.md:9-10` — `/speccen:audit` loads the governing skill by name and path.
- The governing skill's stage → skill map (`00-governing-audit/SKILL.md:90-93`) and new-audit step
  (:129) load the stage skills by path.
- Each stage skill points at its sibling by path: recon :66 → dimension analysis; dimension
  analysis :68 → scorecard review; scorecard review :85 → synthesis. Recon :9, dimension analysis
  :9 and synthesis :12 read `00-governing-audit/references/bundle-conventions.md`.
- Recon :23 and scorecard review :14, :33 run the two scripts by repository-relative path.
- `compare_scorecards.py` reaches the rubrics and `build_scorecard.py` through `SKILLS_ROOT`
  (below).
- Docs: `ARCHITECTURE.md:278`, `:315`; `README.md:53-57`, `:130-136`.

### Behavioural Analysis

The rename moves text and folders only; the one runtime behaviour it can change is path
resolution in `compare_scorecards.py`.

`compare_scorecards.py:23` — `SKILLS_ROOT = pathlib.Path(__file__).resolve().parents[2]`. For
`skills/audit/03-scorecard-review/scripts/compare_scorecards.py`, `parents[2]` is `skills/audit`.
The script stays two levels below `skills/audit/` after the move
(`audit-scorecard-review/scripts/`), so `SKILLS_ROOT` and `PLUGIN_JSON`
(`SKILLS_ROOT.parent.parent / ".claude-plugin" / "plugin.json"`, :24) still resolve.

`rubric_hash()` (:29-41):

```
          ┌───────────────────────────┐
          │ rubric_hash(run)          │
          └─────────────┬─────────────┘
                        ▼
   ┌───────────────────────────────────────────────┐
   │ files = sorted(SKILLS_ROOT/"02-dimension-     │  :33  folder name hard-coded
   │   analysis"/"references").glob("*.md")        │       missing folder → [] (silent)
   └───────────────────────┬───────────────────────┘
                           ▼
   ┌───────────────────────────────────────────────┐
   │ files.append(SKILLS_ROOT/"03-scorecard-       │  :34  folder name hard-coded
   │   review"/"scripts"/"build_scorecard.py")     │
   └───────────────────────┬───────────────────────┘
                           ▼
                ┌─────────────────────┐
                │ run/weights.json    │
                │ exists?             │
                └───┬─────────────┬───┘
                 yes│             │no
                    ▼             │
        ┌──────────────────────┐  │
        │ append weights.json  │  │
        └──────────┬───────────┘  │
                   ▼              ▼
   ┌───────────────────────────────────────────────┐
   │ for f in files:                               │
   │   h.update(f.name)   ← base name only         │  :38-40
   │   h.update(f.read_bytes())                    │  missing build_scorecard.py →
   └───────────────────────┬───────────────────────┘  FileNotFoundError (not silent)
                           ▼
              ┌──────────────────────────┐
              │ return sha256[:12]       │
              └──────────────────────────┘
```

Consequences:
- The hash reads `f.name` (base name) and the bytes, never a directory, so moving the folders
  leaves it equal — H-4 holds.
- A stale `"02-dimension-analysis"` makes the glob return `[]`: the hash then covers only
  `build_scorecard.py` and silently differs. A stale `"03-scorecard-review"` raises
  `FileNotFoundError` on `read_bytes()` — loud, not silent. The brief's "silently hash no
  rubrics" holds for :33 only.
- **Baseline (P02-4):** `compare_scorecards.py stamp` on a throwaway run in the session scratchpad
  (`.../scratchpad/baseline-e824b5c/audits/2026-11-18.baseline/run.json`), with skills equal to
  `e824b5c`, wrote `"rubric_hash": "212cd4db08e1"`. The bytes are those of this Windows checkout;
  the Phase 05 check must run on the same checkout to be comparable.

`build_scorecard.py` takes `dimensions_dir`, `--out` and `--weights` (:373-375) and holds no
skill folder name: `grep -n "0[0-4]-" build_scorecard.py` finds nothing — H-2 holds, so the
invariant "do not edit `build_scorecard.py`" does not conflict with Required change 8.

### Data Model

The change touches names, not data. The relevant name data:

| Item | Count | Where |
|---|---|---|
| Skill folders to move | 5 | `skills/audit/0[0-4]-*` |
| Files that move with them | 19 | `find skills/audit -type f` |
| Rubric files (hash input, unchanged) | 11 | `02-dimension-analysis/references/*.md` |
| `name:` values to change | 1 | `00-governing-audit/SKILL.md:2` |
| Hits of the brief's Verification 1 search at HEAD | 41 | see Restatement inventory |

### Restatement inventory (P02-3)

The brief's Verification 1 search, run at HEAD, gives 41 hits. They split into four groups.

**A — places the brief lists (28 hits), all at the cited line (H-1 holds):**

| File | Lines | Text |
|---|---|---|
| `skills/audit/00-governing-audit/SKILL.md` | :2, :53, :90, :91, :92, :93, :129 | `name: app-maturity-audit`; rubric path; stage → skill map; new-audit step |
| `skills/audit/01-recon/SKILL.md` | :9, :23, :66 | conventions path; `stamp` command path; next-stage path |
| `skills/audit/02-dimension-analysis/SKILL.md` | :9, :68 | conventions path; next-stage path |
| `skills/audit/03-scorecard-review/SKILL.md` | :14, :33, :85 | `build_scorecard.py` path; `compare` path; next-stage path |
| `skills/audit/04-synthesis/SKILL.md` | :12 | conventions path |
| `skills/audit/03-scorecard-review/scripts/compare_scorecards.py` | :33, :34 | `SKILLS_ROOT / "02-dimension-analysis"`, `"03-scorecard-review"` |
| `commands/audit.md` | :9, :10 | `` `app-maturity-audit` ``; `skills/audit/00-governing-audit/SKILL.md` |
| `ARCHITECTURE.md` | :278, :315 | `` (`00-governing-audit` … `04-synthesis`, `` ; `skills/audit/00-governing-audit/SKILL.md` |
| `README.md` | :53, :54, :55, :56, :57, :136 | audit table `sdd-governing-audit/` … `sdd-synthesis/`, `` (`app-maturity-audit`) ``; upgrade note `` (`00-governing-audit/` … `04-synthesis/`). `` |

The brief cites the upgrade note as `README.md:117-136`; the install section starts at :117, and
the note itself is :130-136 (:129 is blank).

**B — old governing name in places the brief does not list (4 hits), in scope under Required
change 8 (H-3 holds):** the `description:` on line 3 of each stage skill —
`01-recon/SKILL.md:3`, `02-dimension-analysis/SKILL.md:3`, `03-scorecard-review/SKILL.md:3`,
`04-synthesis/SKILL.md:3` — reads "Loaded by the app-maturity-audit governing skill …".

**C — false positives of the search (9 hits):** the alternative
`sdd-(governing-audit|recon|…)` also matches the prefix of `sdd-reconcile`:
`ARCHITECTURE.md:314`, `README.md:40`, `README.md:751`, `skills/sdd/sdd-governing-workflow/SKILL.md:1164`, `:2272`,
`:2277`, `:2300`, `:2339`, `skills/sdd/sdd-reconcile/SKILL.md:2`. `sdd-reconcile` is a real skill
and must not change. So the search as written can never return "matches only in the README
upgrade note" (O-4).

**D — no hit:** `.claude-plugin/*` (P02-5), `.github/**`, `agents/`, `examples/`, `skills/code/`,
`skills/audit/00-governing-audit/references/bundle-conventions.md`. No changelog or release-notes
file is tracked (`git ls-files | grep -i -E "changelog|release"` is empty), so there are no
historic records outside `.speccen/` (O-2 closes: not applicable).

Adjacent, not an audit name: `ARCHITECTURE.md:307` reads
`` | A specific phase's behaviour | that phase's `skills/sdd/NN-*/SKILL.md` | `` — a numbered sdd
path left behind by `1c41496`. It is outside this brief's scope (O-5).

### Coding Patterns & Style

- **Naming:** `skills/sdd/` (11) and `skills/code/` (2) follow folder = `name:`; `skills/audit/`
  is the only group that does not. A one-line loop over `skills/*/*/SKILL.md` (the brief's
  Verification 2) reports the five audit skills only.
- **Path style in skills:** repository-relative paths in backticks
  (`` `skills/audit/01-recon/SKILL.md` ``), and commands as `python skills/audit/…/x.py`.
- **Model commit `1c41496`:** one commit; `git mv` renames; frontmatter `name:` and every path
  updated; README table and upgrade note; `.speccen/` records left as they were.
- **Test conventions:** no test framework and no test folder. Markdown skills are checked with
  string and shell checks (the brief's Verification 1 – 5; earlier bundles kept such checks in
  `files/phase-05-text-checks.py`). The two scripts have no tests; they run end to end by CLI.
- **Error handling in the script:** no guard on a missing rubrics folder (empty glob is accepted).

<a id="conventions"></a>
## Project Conventions Confirmation

`.claude/` does not exist. `.github/` holds `CODEOWNERS`, `SECURITY.md` and
`workflows/bump-version.yml`.

#### `.github/SECURITY.md`
**Read:** ✓  
**CRITICAL/MANDATORY Rules:** "Please do not report security vulnerabilities through public GitHub issues, discussions, or pull requests."  
**Architecture Boundaries:** N/A  
**Technology Constraints:** "This project uses calendar-based versions (`YY.MDD.N`)."  
**Naming Conventions:** N/A  
**Critical Workflows:** private vulnerability reporting through the Security tab  
**Hard Constraints:** in scope for security: "Instructions or commands that could cause an assistant to run unintended or destructive actions" — the rename changes command paths that an assistant runs (`python skills/audit/…`), so a wrong path is a defect of this kind, not a style issue.

#### `.github/CODEOWNERS` (not markdown; read for ownership)
**Read:** ✓  
**Hard Constraints:** `* @speccen/team-leads`; `/.github/` and `/.claude-plugin/` owned by `@speccen/team-leads`. The rename touches neither folder.

#### `.github/workflows/bump-version.yml` (not markdown; read for the release rule)
**Read:** ✓  
**Critical Workflows:** on push to `main`, unless only `.github/**`, `README.md`, `ARCHITECTURE.md` or `LICENSE` changed, CI bumps `.claude-plugin/plugin.json` and `marketplace.json` and tags `v<version>`. The rename changes `skills/` and `commands/`, so the merge triggers a bump.  
**Hard Constraints:** the version is CI-owned — matches the brief's "Do not bump the version by hand".

No project-specific convention files beyond these were found. The governing rules for this
change are the brief's Invariants and the model commit `1c41496`.

### Performance Characteristics

Not applicable to the change: `rubric_hash()` reads 12 – 13 small files per call (11 rubrics, the
scorer, an optional `weights.json`); the rename does not change that count.

### Relationship to Similar Components

`skills/sdd/` after `1c41496` is the direct model: folder = `name:` = `sdd-<role>`. `skills/code/`
(`code-documentation`, `code-review`) also matches. After this change all three groups follow the
same rule.

### Known Issues & Code Commentary

- `compare_scorecards.py` docstring: "The scorer (build_scorecard.py) is not touched; this script
  only reads its `summary.json` and the per-dimension `result.json` files."
- `compare_scorecards.py:30-31`: "Hash of everything that decides a score: the rubrics, the
  scorer, its default weights and the run's own weights.json override, if any."
- `TODO`, `FIXME` and `HACK` occur 3 times in `skills/audit/`, all in rubric text that names these markers as something to look for in an audited codebase (`02-dimension-analysis/references/code-quality.md:14`, `:33`; `references/performance-scalability.md:18`). None is a marker in the skills or scripts themselves, and the rubrics are not edited (hash invariant).

<a id="outcome"></a>
## Executive Summary

The rename is mechanical, and the brief maps it almost completely. All 28 cited hits match HEAD.
Four more name references exist (the stage skills' `description:` lines). No other script, manifest
or historic record needs a change. The rubric hash depends on base names only, so the move leaves
it at the baseline `212cd4db08e1`. The one finding that changes the plan is in the done-when: the
brief's Verification 1 search also matches `sdd-reconcile` (9 hits), so it needs a tighter pattern
before it can pass (O-4).

<a id="open-items"></a>
## Open Items

| # | Open item | Settles in |
|---|---|---|
| O-2 | Historic records outside `.speccen/` — closed: none exist (group D). | — |
| O-3 | Test Plan: Verification 1 – 5 as checks, run against the planned text and scoped to their place. Verification 4 needs a minimal `dimensions/` fixture for `build_scorecard.py` and compares with `212cd4db08e1`. | Phase 04 |
| O-4 | Verification 1 matches `sdd-reconcile` (group C, 9 hits): how is the search tightened so it can give the brief's expected result? Material — it changes an acceptance check. | Phase 03 |
| O-5 | `ARCHITECTURE.md:307` `skills/sdd/NN-*/SKILL.md` — a stale sdd path outside this brief: leave it, or fix it here? | Phase 03 |
| O-6 | The four stage `description:` lines (group B): replace `app-maturity-audit` with `audit-maturity`, wording otherwise unchanged? | Phase 03 |
