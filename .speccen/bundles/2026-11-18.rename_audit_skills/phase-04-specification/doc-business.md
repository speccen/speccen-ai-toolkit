---
type: Doc
audience: business
expandable: true
status: COMPLETE
description: The audit runs as before under /speccen:audit; only skill names and folders change
---

# rename audit skills — Business Process & Experience (intent, seed)

## Capability
- No new capability. The maturity audit works as before.
- The skill list shows `audit-maturity` instead of `app-maturity-audit` for the governing audit skill.

## Business Process (end to end, intended)
- The user types `/speccen:audit`.
- The command loads the `audit-maturity` skill.
- The audit runs its stages: recon, scoring, scorecard and review, synthesis.
- The scripts stamp and compare runs. Results from earlier runs stay comparable with new runs.

## Where It Will Surface (UI/UX)
- The skill list of the host (Claude Code or Copilot CLI): five audit skills with `audit-` names.
- The `README.md` table of audit skills and its upgrade note.
- No screen or API changes.

## What Will Change For The User
- Before: the governing audit skill is `app-maturity-audit` in folder `00-governing-audit/`.
- After: the skill and the folder are both `audit-maturity`.
- A user with a local copy removes the five old audit folders before they copy the new ones.

## Not Included
- No fix of the stale counts in the audit text ("ten dimensions", "three signals").
- No change to the `/speccen:audit` command name.
- No change to the rubrics or to how the audit scores.
