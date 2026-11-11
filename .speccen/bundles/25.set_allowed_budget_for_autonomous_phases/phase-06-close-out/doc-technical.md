---
type: Doc
audience: technical
expandable: true
status: COMPLETE
description: The fixes key, template version 3, the gate-test budget with three guards and the Phase 05 accept, in three files
---

# set allowed budget for autonomous phases — Technical Documentation (seed)

Plan: [Phase 04 Implementation Plan](../phase-04-specification/phase.md#implementation-plan). Record: [Phase 05](../phase-05-implementation/phase.md#implementation-summary).

## Files Created
| File | Description |
|---|---|
| — | No file created in the repository. The bundle holds the check scripts `files/phase-05-text-checks.py` and `files/phase-05-move-test.py`. |

## Files Modified
| File | Changes |
|---|---|
| `skills/sdd/00-governing-workflow/SKILL.md` | Keys table: version `3`; rows `fixes` and `phases.<phase>.fixes`; `fixes` in "Which phases take which key". Template: `version: 3`, `fixes: 1` with two comment lines, a legend line, `fixes: inherit` on five phases. Upgrade: absence values name `fixes: 1`; a version-3 sentence. Effective settings: `fixes` with default `1`. Fail-safe: a `fixes` value other than `1` – `3` counts as `1`. Gate test: the fix rule uses the phase's effective `fixes`; a stop bullet with three guards and a log line; the after-a-stop bullet; the self-check line is "N corrections". Stop condition 5 names the three causes. |
| `skills/sdd/05-implementation/SKILL.md` | Mode behaviour, Step 7 (accept): fix and test again up to the effective `fixes`, with the gate test's guards. A conclusion change is a stop. A used-up budget or no progress is a rejection (Phase 05b). |
| `README.md` | Absence values "(`inherit`, `ask`, `1`, `0`, `false`)"; the template block equals the governing template. |

All three stay uncommitted for the Architect (DD-24).

## Files Deleted
| File | Reason |
|---|---|
| — | No file deleted. |

## Deviations from Plan
- None → [Phase 05 deviations](../phase-05-implementation/phase.md#deviations).
- Two edits the plan did not name, with no wording change: the template edits stay inside the template block, so the version-1 upgrade example does not change; the three guards are a numbered sub-list with the plan's words.

## Learnings & Pitfalls (this feature)
- A text check must read only the place its Test Plan row names. An "unchanged" check must compare that place with the base commit. A check that searches the whole file passes when the text moves. This cause made most of the failures in the eight verifier runs and three stop rounds of the Phase 05 accept.
- Test each check before the verifier runs: move its expected text out of its place, in memory, and confirm the check fails (`files/phase-05-move-test.py`, 24 cases).
- Repair every case of a breach type, not only the cases the verifier names. Each repair of named cases only was followed by a run that found the next case.
- Write the decision records and the final edits first. Write the lists, the render and the summary last. Do not put decision ranges in lists; a new decision makes them stale (Phase 04, stop round 04/2).
- Read log times from `date`. Estimated times ran up to 20 minutes ahead of the clock and failed a gate row.
- A claim in a record about script behaviour needs the same test as the script. One sentence about failure modes failed two verifier runs.

## Results (if measured)
| Metric | Before | After | Improvement |
|---|---|---|---|
| Fix attempts allowed per gate | 1 | 1 – 3 (`fixes`, default 1) | set by the Architect |
| Stops for a one-fix limit in an autonomous bundle | this bundle: 3 (Phases 01, 02) | [pending developer measurement] — the next autonomous bundle with `fixes: 2` or `3` | [pending] |
| Verifier runs per gate | this bundle: up to 8 (Phase 05) | [pending developer measurement] | [pending] |

- This bundle ran on the old rule. The new rule is not yet released. The first measurement comes from the next bundle.
