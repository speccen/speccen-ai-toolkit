---
type: Phase
phase: "05 — Implementation"
status: COMPLETE
description: The fixes budget written into the governing skill, the Phase 05 skill and the README; text checks T-1 – T-19
---

<a id="phase-top"></a>
# set allowed budget for autonomous phases — Implementation

[Index](../index.md) · [State](../STATE.md) · [Log](../log.md)

---

<a id="extensions"></a>
## Extensions applied

| Extension | Why | Where it applies | Outcome |
|---|---|---|---|
| — | — | — | No extensions for this phase |

`.speccen/extensions/` does not exist in this repository.

<a id="conventions"></a>
### Project Conventions Re-Confirmation (Phase 05)

`.claude/` does not exist in this repository. `.github/` holds one `.md` file.

#### `.github/SECURITY.md`
**Re-Read:** ✓  
**CRITICAL/MANDATORY Rules Impacting This Implementation:**
- In scope as a security issue: "Instructions or commands that could cause an assistant to run unintended or destructive actions" and "Prompt-injection weaknesses in the skills and workflows". The change edits skill instructions; it adds no command and lets the delegate do nothing it could not do before — it only repeats the existing fix step up to a bounded number of times (ceiling 3).

**Other Rules Impacting This Implementation:**
- "This project uses calendar-based versions (`YY.MDD.N`)." — the plugin version is bumped by `bump-version.yml` on push to `main`; this change does not edit any version file.

#### `.github/CODEOWNERS` (context, not Markdown)
**Re-Read:** ✓  
- `*` → `@speccen/team-leads`: all three changed files are owned by the team leads; the change stays uncommitted for the Architect (DD-24).

#### Durable store — prior art
- Lesson `2026-11-05.readme_restates_config_template`: the README template block must equal the governing block character for character (T-16).
- The Architect: "feature branch, no push on main is allowed" (log 11:05) — work stays on `feature/set-allowed-budget-for-autonomous-phases`.

**Plan confirmed by the delegate** — 2026-11-11. The skill files are unchanged since `a7c8206` (`git diff a7c8206 HEAD -- skills README.md` is empty), so the plan's line references hold at the start.

<a id="implementation-summary"></a>
## Implementation Summary

All five plan phases ran in order without a stop; every checklist item in the
[Implementation Plan](../phase-04-specification/phase.md#implementation-plan) is ticked.

| Plan phase | Files | What changed |
|---|---|---|
| 1 Configuration | `skills/sdd/00-governing-workflow/SKILL.md` | Keys: version row says `3`; rows `fixes` and `phases.<phase>.fixes` after `phases.<phase>.stops`; `fixes` bullet under "Which phases take which key". Template: `version: 3`, the two comment lines and `fixes: 1` after `stops: ask`, the legend line, `fixes: inherit` after `stops: inherit` on the five phases. Upgrade: absence values name `fixes: 1` and `fixes`; the version-3 sentence after the version-2 sentence. Effective settings name `fixes` with default `1`; fail-safe line for `fixes`. |
| 2 Gate test | same file | The fix rule uses the phase's effective `fixes`; the stop bullet with the three guards and the log line; the after-a-stop bullet; self-check line "N corrections"; stop condition 5. |
| 3 Phase 05 accept | `skills/sdd/05-implementation/SKILL.md` | Step 7 uses the budget and the guards; a conclusion change stops; a used-up budget or no progress rejects (05b). |
| 4 Restated copies | `README.md` | Absence values "(`inherit`, `ask`, `1`, `0`, `false`)"; the template block copied from the governing skill. The old README block was identical to the old governing block: the copy's diff shows only the new lines. |
| 5 Verification | `files/phase-05-text-checks.py` | T-1 – T-19, see below. |

Edits the plan did not name, checked: the template edits were made only inside the template
block, because the version-1 upgrade example (`Upgrading the project file` → **Example**) also
holds the `stops` legend line and `stops: inherit`, and stays unchanged. The stop bullet's three
guards are written as a numbered sub-list with the plan's exact words. No other text in
`skills/`, `agents/`, `commands/`, `README.md` or `ARCHITECTURE.md` describes the one-fix rule
(search for "fix once", "one fix", "second verifier run", "N fixes": no hit).

<a id="test-results"></a>
## Text check results

`python3 -I .speccen/bundles/25.set_allowed_budget_for_autonomous_phases/files/phase-05-text-checks.py`
from the repository root, against base `a7c8206` — first run 2026-11-11 21:01; last run 21:24, after the repairs of 21:05, 21:08, 21:14 (stop round 05/1), 21:20 (stop round 05/2) and 21:24 (DD-31) — see the [summary](./summary.md#delegate-gate-check):

| Check | Result | Check | Result |
|---|---|---|---|
| T-1 | pass | T-11 | pass |
| T-2 | pass | T-12 | pass |
| T-3 | pass | T-13 | pass |
| T-4 | pass | T-14 | pass |
| T-5 | pass | T-15 | pass |
| T-6 | pass | T-16 | pass |
| T-7 | pass | T-17 | pass |
| T-8 | pass | T-18 | pass |
| T-9 | pass | T-19 | pass |
| T-10 | pass | | |

`files/phase-05-move-test.py` (run the same way) moves each check's expected text out of the place its Test Plan row names, in memory, and confirms that every case fails (24 cases over the 19 checks); it also asserts that all 19 pass on the unmoved text.

The checks compare text with whitespace normalised (line wraps do not count), and take their
expected strings from the plan's checklist and the requirements, not from the edited files.
`git diff --stat -- . ':(exclude).speccen'`: `README.md`, `skills/sdd/00-governing-workflow/SKILL.md`,
`skills/sdd/05-implementation/SKILL.md` — 3 files. The skill changes stay uncommitted (DD-24).

<a id="deviations"></a>
## Deviations

None.

<a id="outcome"></a>
## Outcome

Accepted by the delegate on 2026-11-11 (21:54) after the gate test passed in verifier run 8 — [summary](./summary.md#delegate-gate-check). The skill text was confirmed correct in every run; all failures lay in the check script and the bundle records. The three changed files stay uncommitted for the Architect (DD-24).

<a id="open-items"></a>
## Open Items

The two `MATERIAL — unconfirmed` decisions (DD-12, DD-14) go to the end-of-run review.
