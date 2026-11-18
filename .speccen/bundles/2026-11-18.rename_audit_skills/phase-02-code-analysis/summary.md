---
type: Summary
phase: "02 — Code Analysis"
status: COMPLETE
phase_file: ./phase.md
description: Cited places confirmed, 4 extra name references, rubric hash name-only (baseline 212cd4db08e1), Verification 1 regex needs tightening
---

# Phase 02 Summary — Code Analysis

[Index](../index.md) · [State](../STATE.md) · [Log](../log.md)

---

**Work completed:** analysed the audit skill tree, its entry points, the `rubric_hash()` path
resolution (with a flow diagram), and every hit of the brief's Verification 1 search. Read the
conventions in `.github/` (no `.claude/`). Computed the baseline rubric hash at `e824b5c`.

**Outcome:** the rename is mechanical. All 28 cited hits match HEAD, and there are 4 more name
references (the stage `description:` lines). The rubric hash depends on base names only (baseline
`212cd4db08e1`). The brief's Verification 1 search also matches `sdd-reconcile`, so it needs
tightening → [full detail](./phase.md#outcome)

**Open items carried forward:** → [detail](./phase.md#open-items)
- `[O-3 | Test Plan: Verification 1 – 5 as scoped checks, with a dimensions fixture and the baseline hash 212cd4db08e1]` — Phase 04
- `[O-4 | How is the Verification 1 search tightened so sdd-reconcile no longer matches?]` — Phase 03 (material)
- `[O-5 | Leave or fix the stale ARCHITECTURE.md:307 skills/sdd/NN-* path?]` — Phase 03
- `[O-6 | Replace app-maturity-audit in the four stage description lines?]` — Phase 03

**Evolution-gap doc:** not generated — no structural evolution-blocker found; the rename slots into
the current structure (no boundary conflict, stub, contract limitation, scaling wall or
entanglement: `SKILLS_ROOT` is depth-relative and the hash is name-only).

**Delegated decisions:** none in this phase (6 in total) → [delegated-decisions.md](../delegated-decisions.md)

**Extensions applied:** none

<a id="delegate-gate-check"></a>
## Delegate gate check

Fix attempt 1 of 5: run 1 failed rows 11 (K-7 wrong — 3 hits, not 0); corrected in phase.md Known Issues; run 2 confirmed.

Self-check: done — 3 corrections (group A count 29 → 28; group C count 8 → 9, adding `ARCHITECTURE.md:314`; row 18 claim re-pointed and row 19 added for H-2)

| # | Item | Result | Evidence | Verified |
|---|---|---|---|---|
| 1 | Extensions table complete | pass | `.speccen/extensions/` does not exist; [phase.md#extensions](./phase.md#extensions) | n/a — bundle-internal |
| 2 | Architecture overview with position in the system | pass | [phase.md](./phase.md#code-analysis) Architecture Overview; `.claude-plugin/plugin.json:22-26` | confirmed (run 1) |
| 3 | Behavioural analysis with all execution paths | pass | Behavioural Analysis: `SKILLS_ROOT` (:23), `rubric_hash()` (:29-41), both failure modes | confirmed (run 1) |
| 4 | Execution flow as ASCII diagram matching real branches | pass | `rubric_hash()` diagram: the one conditional (`weights.json` exists) | confirmed (run 1) |
| 5 | Data model with types and counts | pass | Data Model table: 5 folders, 19 files, 11 rubrics, 1 `name:`, 41 hits | confirmed (run 1) |
| 6 | `.claude/` and `.github/` scanned, all `.md` read | pass | `.claude/` absent; `.github/SECURITY.md` read; CODEOWNERS and workflow read | confirmed (run 1) |
| 7 | Project Conventions Confirmation table | pass | [phase.md#conventions](./phase.md#conventions) | n/a — bundle-internal |
| 8 | Coding patterns and practices identified | pass | Coding Patterns & Style; test conventions: none, string checks | n/a — bundle-internal |
| 9 | Performance characteristics | pass | Performance: not applicable, 12 – 13 file reads | n/a — bundle-internal |
| 10 | Comparison with similar components | pass | Relationship: `skills/sdd/`, `skills/code/` | n/a — bundle-internal |
| 11 | Known issues and commentary verbatim | pass | Known Issues: two docstring quotes; 3 TODO/FIXME/HACK hits, all rubric text naming the markers | confirmed (run 2) |
| 12 | Executive Summary under `outcome` | pass | [phase.md#outcome](./phase.md#outcome) | n/a — bundle-internal |
| 13 | Evolution-gap determination recorded | pass | this summary: not generated, with reason | n/a — bundle-internal |
| 14 | Summary written and links back | pass | this file | n/a — bundle-internal |
| 15 | `index.md` lists every file this phase wrote | pass | [index.md](../index.md) Phase 02 | n/a — bundle-internal |
| 16 | No blocking open question | pass | O-4 – O-6 are Phase 03 decisions; none blocks Phase 03 | n/a — bundle-internal |
| 17 | Restatement inventory (P02-3) complete and exhaustive | pass | Restatement inventory groups A – C = 28 + 4 + 9 = 41 | confirmed (run 1) |
| 18 | Baseline rubric hash recorded (P02-4) | pass | `212cd4db08e1`, run in scratchpad at skills = `e824b5c` | confirmed (run 1) |
| 19 | No other script holds an audit folder name (H-2) | pass | Behavioural Analysis, `build_scorecard.py` paragraph | confirmed (run 1) |
| noticed-1 | `index.md` and `log.md` of this bundle are modified in the working tree | not relevant, because these are the main session's own uncommitted Phase 02 writes; they are committed at the transition | `git status --short` | — |
| noticed-2 | `performance-scalability.md:18` and `code-quality.md:33` name only TODO/FIXME, not HACK | not relevant, because the conclusion (no real marker; rubrics untouched) holds for each line | the three lines | — |

Claims
- K-1 (row 2) · plugin manifest lists skill groups only · `grep -n "skills/" .claude-plugin/plugin.json .claude-plugin/marketplace.json` · exactly 3 lines, all in plugin.json: `./skills/sdd/`, `./skills/audit/`, `./skills/code/` → run 1: confirmed
- K-2 (row 3) · `SKILLS_ROOT` is `parents[2]` of the script · `sed -n 23,24p skills/audit/03-scorecard-review/scripts/compare_scorecards.py` · `SKILLS_ROOT = pathlib.Path(__file__).resolve().parents[2]` and `PLUGIN_JSON = SKILLS_ROOT.parent.parent / ".claude-plugin" / "plugin.json"` → run 1: confirmed
- K-3 (rows 3, 4) · hash uses base name and bytes; hard-coded folder names at :33-34; one conditional · `sed -n 29,41p` of the same file · `"02-dimension-analysis"` at :33, `"03-scorecard-review"` at :34, `if (run / "weights.json").exists()`, `h.update(f.name.encode())`, `h.update(f.read_bytes())` → run 1: confirmed
- K-4 (rows 5, 17) · the Verification 1 search has 41 hits at HEAD · the brief's `grep -rnE … --exclude-dir=.git --exclude-dir=.speccen . | wc -l` · 41 → run 1: confirmed
- K-5 (row 5) · 19 files under `skills/audit/`, 11 rubrics · `find skills/audit -type f | wc -l; ls skills/audit/02-dimension-analysis/references/*.md | wc -l` · 19 and 11 → run 1: confirmed
- K-6 (row 6) · `.claude/` absent; `.github/` md files · `ls -a .claude; find .github -name "*.md"` · `.claude` missing; only `.github/SECURITY.md` → run 1: confirmed
- K-7 (row 11) · TODO/FIXME/HACK in `skills/audit/` occur only as rubric text naming the markers · `grep -rnE "TODO|FIXME|HACK" skills/audit` · 3 lines: `references/code-quality.md:14`, `:33`, `references/performance-scalability.md:18` → run 1: wrong — 3 (the claim said 0); run 2: confirmed
- K-8 (row 17) · group C: 9 hits are `sdd-reconcile` · the brief's search piped to `grep -c "sdd-reconcile"` · 9 → run 1: confirmed
- K-9 (row 17) · group B: the four stage descriptions name `app-maturity-audit` · `grep -n "^description:.*app-maturity-audit" skills/audit/0[1-4]-*/SKILL.md | wc -l` · 4 → run 1: confirmed
- K-10 (row 18) · `build_scorecard.py` holds no skill folder name (H-2) · `grep -c "0[0-4]-" skills/audit/03-scorecard-review/scripts/build_scorecard.py` · 0 → run 1: confirmed
- K-11 (row 18) · the rubric hash at skills = `e824b5c` is `212cd4db08e1` · `python -B -c "import sys,pathlib;sys.path.insert(0,'skills/audit/03-scorecard-review/scripts');import compare_scorecards as c;print(c.rubric_hash(pathlib.Path('.')))"` (repository root has no `weights.json`; `-B` writes no `__pycache__`) · `212cd4db08e1` → run 1: confirmed
