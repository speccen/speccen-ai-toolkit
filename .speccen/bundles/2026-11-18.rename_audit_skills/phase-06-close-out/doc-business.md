---
type: Doc
audience: business
expandable: true
status: COMPLETE
description: The audit runs as before under /speccen:audit; the five audit skills now have audit- names
---

# rename audit skills — Business Process & Experience (seed)

## Capability
- No new capability. The maturity audit works as before. This matches the intent ([Phase 04 seed](../phase-04-specification/doc-business.md)).
- The five audit skills have names that match their folders: `audit-maturity`, `audit-recon`, `audit-dimension-analysis`, `audit-scorecard-review`, `audit-synthesis`.

## Business Process (end to end)
- The user types `/speccen:audit`.
- The command loads the `audit-maturity` skill.
- The audit runs its stages: recon, scoring, scorecard and review, synthesis.
- The scripts stamp and compare runs. A run after the change compares like-for-like with a run before it. The test showed the same rubric hash, `212cd4db08e1`.

## Where It Surfaces (UI/UX)
- The skill list of the host shows the five `audit-` names after the next plugin release.
- `README.md` shows the new folders in the audit table and in the upgrade note.
- No screen or API changes.

## What Changes for the User
- Before: the governing audit skill was `app-maturity-audit` in folder `00-governing-audit/`.
- After: the skill and the folder are both `audit-maturity`.
- A user with a local copy removes the five old audit folders before they copy the new ones. The README upgrade note lists them.

## Not Included
- No fix of the stale counts in the audit text ("ten dimensions", "three signals").
- No change to the `/speccen:audit` command name.
- No change to the rubrics or to how the audit scores.
- No fix of the stale sdd path in `ARCHITECTURE.md:307`. This is a follow-up.
