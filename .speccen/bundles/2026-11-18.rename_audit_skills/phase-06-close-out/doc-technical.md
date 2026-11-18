---
type: Doc
audience: technical
expandable: true
status: COMPLETE
description: Five audit skill folders renamed to audit-<role> with git mv; nine files updated by a fixed substitution map; rubric hash unchanged
---

# rename audit skills — Technical Documentation (seed)

## Files Created
| File | Description |
|---|---|
| `skills/audit/audit-maturity/` (2 files) | Rename of `skills/audit/00-governing-audit/` (`git mv`). |
| `skills/audit/audit-recon/` (1 file) | Rename of `skills/audit/01-recon/`. |
| `skills/audit/audit-dimension-analysis/` (12 files) | Rename of `skills/audit/02-dimension-analysis/`. The 11 rubrics move byte-identical (`R100`). |
| `skills/audit/audit-scorecard-review/` (3 files) | Rename of `skills/audit/03-scorecard-review/`. `build_scorecard.py` moves byte-identical. |
| `skills/audit/audit-synthesis/` (1 file) | Rename of `skills/audit/04-synthesis/`. |

## Files Modified
| File | Changes |
|---|---|
| `skills/audit/audit-maturity/SKILL.md` | `name:` is `audit-maturity`. Five paths use the new folders. `description:` is unchanged. |
| `skills/audit/audit-recon/SKILL.md` | The `description:` names `audit-maturity`. Three paths use the new folders. |
| `skills/audit/audit-dimension-analysis/SKILL.md` | The `description:` names `audit-maturity`. Two paths use the new folders. |
| `skills/audit/audit-scorecard-review/SKILL.md` | The `description:` names `audit-maturity`. Three paths use the new folders. |
| `skills/audit/audit-synthesis/SKILL.md` | The `description:` names `audit-maturity`. One path uses the new folder. |
| `skills/audit/audit-scorecard-review/scripts/compare_scorecards.py` | Lines 33 – 34 join `"audit-dimension-analysis"` and `"audit-scorecard-review"` onto `SKILLS_ROOT`. |
| `commands/audit.md` | Loads `audit-maturity` from `skills/audit/audit-maturity/SKILL.md`. The command name stays `audit`. |
| `ARCHITECTURE.md` | Line 278 names `audit-maturity` … `audit-synthesis`. Line 315 uses the new path. Line 307 is not changed (DD-8). |
| `README.md` | The audit table names the new folders. The upgrade note lists the five old audit folders for removal and says that the audit folders have new names. |

## Files Deleted
| File | Reason |
|---|---|
| `skills/audit/00-governing-audit/`, `01-recon/`, `02-dimension-analysis/`, `03-scorecard-review/`, `04-synthesis/` | Old folders of the renames above. Git records each file as a rename. |

- One code commit: `fdbc357` (19 renames, 3 modified files). The message is the brief's message. No trailer.
- No version change. CI bumps the version on merge.

## Deviations from Plan
- [Deviation 1](../phase-05-implementation/phase.md#deviations) — T-4 runs Python in UTF-8 mode (`-X utf8`). `build_scorecard.py:391` writes `scorecard.md` with the platform encoding and fails with cp1252 on Windows. The scorer is not changed (rubric hash invariant). APPROVED (delegated), [DD-13](../delegated-decisions.md#dd-13).

## Learnings & Pitfalls (this feature)
- `build_scorecard.py` fails on Windows without UTF-8 mode. A fix changes the rubric hash, so a fix needs its own decision.
- Audit run ids sort as text. A test run must sort after its baseline, or `compare` compares nothing. A mutation test (a changed hash must warn) found this.
- The brief's Verification 1 search also matches `sdd-reconcile`. A `\b` after the `sdd-(…)` group removes the 9 false hits (DD-7).
- The README upgrade note starts on line 130. Line 129 is blank. Find the note by its first line, not by a line number.

## Results (if measured)
| Metric | Before | After | Improvement |
|---|---|---|---|
| Skill folders whose name differs from `name:` | 5 (all of `skills/audit/`) | 0 | −5 |
| Hits of the old names outside `.speccen/` (DD-7 search) | 32 | 4 (the README upgrade note, on purpose) | −28 |
| Rubric hash | `212cd4db08e1` | `212cd4db08e1` | unchanged |
| Planned checks | — | 13 of 13 pass | — |
