---
type: Doc
audience: executive
expandable: true
status: COMPLETE
description: The Architect now sets how many fix attempts the delegate makes on a failed gate test
---

# set allowed budget for autonomous phases — Business Outcome Brief (seed)

Intent: [Phase 04 executive seed](../phase-04-specification/doc-executive.md). Intended → delivered: the same. At the review, the Architect set the ceiling to 10; on 2026-11-12, the default to 5. The intent (specification) was amended to match.

## Capability Delivered
- The Architect sets a number of fix attempts for each autonomous phase: from 1 to 10.
- The delegate corrects its own bundle files within that number. Then it asks the Architect.
- The default is 5. A project that wants one fix attempt sets the number to 1.

## Risk Delta
- Risk closed: a stop for a small correction takes the Architect's time. This bundle had seven stops. The Architect replied "yes" or "ok, continue" to each stop. Three stops in Phases 01 and 02 came only from the limit of one fix attempt. A budget of 2 or more removes that type of stop.
- The other four stops came from the progress guard. The progress guard stays: the verifier found a problem again, or more rows failed.
- Risk closed: a loop of corrections with no limit. The number of fix attempts is never more than 10.
- Risk accepted: more verifier runs on the session model, at most 10 fix attempts at each gate. The progress guard halts a loop that does not converge.
- Risk accepted: the Architect does not see each correction before the gate. The log shows each fix attempt.
- Risk open: the new rule is in the skill text but not yet in use. This bundle ran on the old rule. The next autonomous bundle gives the first evidence.

## What It Unblocks
- Autonomous phases without a stop for small corrections.
- A clear meaning for each stop: the Architect must decide, or the delegate cannot complete the work within its fix attempts.

## Scope Note
- TCO / cost / budget: out of scope for this feature-level brief.
