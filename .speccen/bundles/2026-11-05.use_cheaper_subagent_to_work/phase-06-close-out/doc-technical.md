---
type: Doc
audience: technical
expandable: true
status: COMPLETE
description: Seven files changed — template version 2, model on 04 and 05, the search unit, the gate-test self-check and delta re-check, pointers and restated copies
---

# Use cheaper subagent to work — Technical Documentation (seed)

## Files Created
| File | Description |
|---|---|
| — | None. |

## Files Modified
| File | Changes |
|---|---|
| `skills/sdd/00-governing-workflow/SKILL.md` | Keys: the current version is `2`. `model` is a key on 7 phases, including `specification` and `implementation`. The fail-safe ignores `model` only on `feature-analysis`. Template: `version: 2`; `model: economy  # searches` on `specification` and `implementation`. The v1 upgrade example is marked as v1; one sentence states the v2 upgrade. Units table: a new search row; a search that is not launched as a unit runs inline. New `### Search` section. Gate test: a five-point self-check before the verifier; the second verifier run re-checks only the failed rows and the rows whose evidence is in a changed file. |
| `skills/sdd/02-code-analysis/SKILL.md` | Two pointer lines to the search unit (end of Step 2; after the Step 3 intro). |
| `skills/sdd/05-implementation/SKILL.md` | One pointer line to the search unit in Step 3. |
| `skills/sdd/interview/SKILL.md` | The bundle, store and code lookups point to the search unit. |
| `README.md` | The template copy matches the governing template. "Model tiers" names searches and their phases. |
| `ARCHITECTURE.md` | The Subagents bullet names searches. The verifier runs on the session model, not on a tier. |
| `agents/speccen-worker.md` | The `description` names a search among the unit kinds. |

## Files Deleted
| File | Reason |
|---|---|
| — | None. |

## Deviations from Plan
- None. → [Deviations](../phase-05-implementation/phase.md#deviations)

## Learnings & Pitfalls (this feature)
- The README holds a full copy of the config template. Change both in the same commit. Check: string equality of the two blocks (T-11).
- The `model` phase list appears twice: the Keys section and the fail-safe. Change both together (T-2, T-3).
- Text checks that match wrapped prose break when a line is re-wrapped. Match with whitespace tolerance (T-2).
- The verifier found new STE defects on each re-check of the Phase 04 seeds: six runs for one row. A fixed term list for the seeds, set before writing, avoids most of these runs.
- Interview rounds failed the gate three times on in-round dependencies and bundled questions (Phases 01 and 03). The new fifth self-check targets this failure.

## Results (if measured)
| Metric | Before | After | Improvement |
|---|---|---|---|
| Search work on `economy` (count of subagent lines per model in `log.md`) | 0 (evidence bundle) | [pending developer measurement] | — |
| Verifier runs per phase | [pending developer measurement] | [pending developer measurement] | — |

- Measure on the next bundle (brief §6; open item O-10).
