---
type: Doc
audience: technical
expandable: true
status: COMPLETE
description: The gate-check verifier settles a capped list of code and repository claims; the self-check owns the bundle; slips cost no fix attempt
---

# use narrow verifier for phase checks — Technical Documentation (seed)

## Files Created
| File | Description |
|---|---|
| `.speccen/bundles/2026-11-15.use_narrow_verifier_for_phase_checks/files/phase-05-text-checks.py` | Text checks T-1 – T-19 for the edited skill text. A bundle file. It does not ship with the plugin. |

## Files Modified
| File | Changes |
|---|---|
| `skills/sdd/00-governing-workflow/SKILL.md` | Gate test: new bullets "Who checks what", "Claims", "What goes on the list", "Self-check", "Verifier" and "The `verified` column". The later-runs rule and the after-a-stop bullet now speak of claims. Units: the verifier row is narrow. Subagent Execution: a verifier work order follows the generic template. |
| `agents/speccen-worker.md` | One bullet under **Do:** — how the worker runs a verifier work order and what it returns. |
| `skills/sdd/01-feature-analysis/SKILL.md` – `skills/sdd/05-implementation/SKILL.md` | One `**Verifier claims.**` bullet in each Mode behaviour. The bullet names the source of the phase's claims. |
| `.claude-plugin/plugin.json`, `.claude-plugin/marketplace.json` | Version `26.1115.1` → `26.1116.1`. |

## Files Deleted
| File | Reason |
|---|---|
| — | None. |

## Deviations from Plan
- [Deviation 1](../phase-05-implementation/phase.md#deviations) — two planned lines said "every row" beside "verifier". The planned search T-14 failed on them. The lines now say "All rows then read" and "the rows without a claim". The meaning is the same. APPROVED (delegated), DD-26.
- [Deviation 2](../phase-05-implementation/phase.md#deviation-2) — plan step 1.3 asked for a rendered view. The host has no Markdown renderer. The nesting was inspected in the raw text. APPROVED (delegated), DD-27.

## Learnings & Pitfalls (this feature)
- Run the planned error-case checks on the planned text before Phase 04 closes. The planned text failed its own search check (T-14) in Phase 05.
- A plan step that renders text needs a tool that exists on the host. Name the tool in the plan.
- A verifier that reads the full phase finds new detail on each run. Phase 04 used 9 verifier runs and Phase 05 used 4. Most failures were wording and records, not conclusions. This is the reason for the narrow rule.
- The new rule applies to later bundles. This bundle ran under plugin `26.1112.2`, with the full-phase verifier.

## Results (if measured)
| Metric | Before | After | Improvement |
|---|---|---|---|
| Verifier run time, full-phase rule (this bundle, Phase 04 runs 1 – 6) | 143 – 279 s per run | [pending developer measurement — first bundle on `26.1116.1`] | — |
| Verifier tokens, full-phase rule (Phase 04 runs 1 – 6) | 96 000 – 119 000 per run | [pending developer measurement] | — |
| Verifier runs to pass the Phase 04 gate | 9 | [pending developer measurement] | — |
