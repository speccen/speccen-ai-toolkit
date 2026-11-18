---
type: Doc
audience: executive
expandable: true
status: COMPLETE
description: All speccen skill groups now use one naming rule; audit results stay comparable
---

# rename audit skills — Business Outcome Brief (seed)

## Capability Delivered
- The five audit skills have `audit-` names that match their folders. All three skill groups of speccen now follow one naming rule. This matches the intent ([Phase 04 seed](../phase-04-specification/doc-executive.md)).

## Risk Delta
- Risk closed: the README pointed to audit folders that did not exist. It now points to the real folders.
- Risk closed: the architecture guide named numbered sdd folders that no longer exist. It now names the real folders.
- Risk closed: one skill had two names (`app-maturity-audit`, `00-governing-audit`). It now has one name.
- Risk accepted: users with a local copy must remove the old folders. The README tells them how.
- Risk found, not closed: the audit scorer fails on Windows unless Python runs in UTF-8 mode. A fix needs its own decision, because a fix changes the rubric hash.

## What It Unblocks
- Later audit changes start from correct paths and names.
- The stale counts in the audit text can be fixed in a separate, small change.

## Scope Note
- TCO / cost / budget: out of scope for this feature-level brief.
