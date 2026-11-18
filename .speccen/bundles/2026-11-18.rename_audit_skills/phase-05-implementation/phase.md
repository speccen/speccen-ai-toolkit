---
type: Phase
phase: "05 — Implementation"
status: COMPLETE
description: Rename implemented in one commit (6c6187c); T-1 – T-13 pass; one deviation (T-4 runs Python in UTF-8 mode on this Windows host)
---

<a id="phase-top"></a>
# rename audit skills — Implementation

[Index](../index.md) · [State](../STATE.md) · [Log](../log.md)

---

<a id="extensions"></a>
## Extensions applied

| Extension | Why | Where it applies | Outcome |
|---|---|---|---|
| — | — | — | No extensions for this phase |

### Project Conventions Re-Confirmation (Phase 05)

`.claude/` does not exist. `.github/` was re-read; nothing changed since Phase 02
(`git diff --quiet e824b5c HEAD -- .github` exits 0).

#### `.github/SECURITY.md`
**Re-Read:** ✓  
**CRITICAL/MANDATORY Rules Impacting This Implementation:**
- In scope for security: "Instructions or commands that could cause an assistant to run unintended or destructive actions" — the change edits the command paths an assistant runs (`python skills/audit/…`); T-3 and T-4 prove they resolve and run.

**Other Rules Impacting This Implementation:**
- "This project uses calendar-based versions (`YY.MDD.N`)." — the version is not touched (T-10).

#### `.github/CODEOWNERS`, `.github/workflows/bump-version.yml`
**Re-Read:** ✓  
**Other Rules Impacting This Implementation:**
- `/.claude-plugin/` is owned by team leads and bumped by CI on merge: no file there changes (T-10).

**Plan confirmed by the delegate** — 2026-11-18, before the first change (autonomous mode).

<a id="implementation-summary"></a>
## Implementation Summary

| Plan phase | Done | Evidence |
|---|---|---|
| 1 — Move the five folders | ✅ | `git mv` ×5; 19 files; no `0[0-4]-*` folder; no `__pycache__` |
| 2 — Name and paths in skills and script | ✅ | 6 files through the substitution map; T-2, T-6, T-7, T-8 pass |
| 3 — Command and docs | ✅ | `commands/audit.md`, `ARCHITECTURE.md`, `README.md` (map + note block :130 – :136 replaced, now :130 – :138); T-1, T-3, T-8, T-9 pass |
| 4 — Verify and commit | ✅ | T-4 by hand (below); commit `6c6187c`; `files/phase-05-text-checks.py`: ALL PASS |

All 27 checklist items are ticked in the [Implementation Plan](../phase-04-specification/phase.md#implementation-plan).
Each file kept its line endings (all nine are LF in this checkout).

**Code commit:** `6c6187c` — `refactor: prefix the audit skills with audit- and drop the folder numbers`,
the brief's message byte for byte, no trailer; 22 paths (19 renames, 3 modified files).

### Planned tests

`files/phase-05-text-checks.py` (T-1 – T-3, T-5 – T-13) — every expected value is copied from the
Phase 04 Test Plan and the brief (the map, the planned note, the commit message, `e824b5c`), and
texts are read from git objects. Full run `python -I -B files/phase-05-text-checks.py` after the
commit:

| Check | Result |
|---|---|
| T-1 | PASS — 4 hits, all in the README note (:132, :133, :137, :138) |
| T-2 | PASS — 18 skills, no mismatch (the brief's own loop: no output) |
| T-3 | PASS — 24 citations, 0 missing |
| T-5 | PASS — 19 renames under `skills/audit/`, 13 `R100` |
| T-6 | PASS — 12 hash inputs, same blob ids |
| T-7 | PASS — governing `description:` equal |
| T-8 | PASS — 9 files equal the map applied to `e824b5c` |
| T-9 | PASS — the note equals the planned text |
| T-10 | PASS — 19 renames + `ARCHITECTURE.md`, `README.md`, `commands/audit.md`; nothing else |
| T-11 | PASS — 1 code commit; message equal; no attribution |
| T-12 | PASS — `.speccen/` changes only in this bundle |
| T-13 | PASS — `skills/sdd`, `skills/code`, `agents` unchanged |

**Move tests:** `MUTATE=T-1`, `MUTATE=T-8`, `MUTATE=T-9` each change one expected text in memory;
each run reports `FAILED: <that check>` and no other.

**T-4 (by hand, scratchpad, nothing committed — DD-11):** a synthetic run of 11
`dimensions/<dim>/result.json` files.
- Baseline run `2026-11-18.baseline`, stamped at `787782d` (skills = `e824b5c`) in Phase 02:
  `rubric_hash` `212cd4db08e1`; `build_scorecard.py` → exit 0.
- New run `2026-11-19.after` on the renamed tree: `stamp` exit 0, `rubric_hash` `212cd4db08e1`;
  `build_scorecard.py` exit 0 (`summary.json`, `scorecard.md`); `compare` exit 0 (`trend.md`,
  `history.md`, `history.json`). `trend.md` compares against `2026-11-18.baseline` ("The previous
  run is the baseline") with 0 "Not like-for-like" lines.
- Mutation: the same with a `weights.json` in the new run → `trend.md` holds
  "⚠ Not like-for-like: rubrics/scorer changed between these runs (rubric hash differs)". The
  check detects a hash change.
- Fixture correction (no plan change): the first new run was named `2026-11-18.after`. It sorts
  before `2026-11-18.baseline`, so `compare` took it as the first run and compared nothing; the
  mutation test exposed it. Renamed to `2026-11-19.after` and re-run as above.
- All runs used `python -I -B -X utf8` — Deviation 1.

<a id="deviations"></a>
## Deviations

### Deviation 1 — 2026-11-18

|     | Info |
| --- | --- |
| **Planned** | T-4: run `stamp`, `build_scorecard.py` and `compare` end to end (Phase 04 plan 4.2). |
| **Actual** | `build_scorecard.py` stops with `UnicodeEncodeError: 'charmap' codec can't encode character '★'` at `(out_dir / "scorecard.md").write_text(...)` (build_scorecard.py:391). The T-4 runs use Python's UTF-8 mode (`-X utf8`); then all three scripts exit 0. |
| **Reason** | `write_text()` has no `encoding`, so on this Windows host Python writes cp1252, which has no `★`. The file is byte-identical to `e824b5c` (T-6), so the error predates the rename. The brief forbids any edit to `build_scorecard.py` (rubric hash), so it is not fixed here. |
| **Impact** | None on the plan or the code. T-4 records the `-X utf8` flag. The encoding defect is a follow-up outside this change: a fix to `build_scorecard.py` changes the rubric hash, so it needs its own decision. |
| **Purpose preserved?** | Yes — plan phase 4 still proves the scripts run end to end at the new paths with an unchanged hash. |
| **Decision** | APPROVED (delegated) — a flag on how the check runs, no change to code, scope or a scenario — [DD-13](../delegated-decisions.md#dd-13) |

graduation-candidate: `build_scorecard.py` writes `scorecard.md` with the platform encoding and fails on Windows; the fix changes the rubric hash, so it is a fence — a lesson for the store.

### Learnings

- graduation-candidate: audit run ids sort as text, so a test run must sort after its baseline; a
  comparison check passed with nothing compared until a mutation test (a changed hash that must
  warn) exposed it. Run a mutation for every "no warning" check.

<a id="open-items"></a>
## Open Items

| # | Item | Settles in |
|---|---|---|
| O-7 | `[DD-7 \| Tighten Verification 1 with \b after the sdd- group?]` — `MATERIAL — unconfirmed` | review round |
| O-8 | `[DD-8 \| ARCHITECTURE.md:304 stale skills/sdd/NN-* path]` — follow-up | end-of-run report |
| O-9 | `[DD-3 \| Push and PR wait for the Architect]` | end of run |
| O-10 | `[Deviation 1 \| build_scorecard.py fails on Windows without UTF-8 mode]` — follow-up; graduation candidate | Phase 06 |

<a id="outcome"></a>
## Outcome

The five audit skills are `audit-maturity`, `audit-recon`, `audit-dimension-analysis`,
`audit-scorecard-review` and `audit-synthesis`, with every path, the script, the command and the
docs updated in commit `6c6187c`. The rubric hash stays `212cd4db08e1`, and a run after the rename
compares like-for-like with a run before it.
