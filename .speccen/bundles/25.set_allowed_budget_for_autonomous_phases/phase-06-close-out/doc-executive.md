---
type: Doc
audience: executive
expandable: true
status: COMPLETE
description: The Architect now sets how many fix attempts the delegate makes on a failed gate test
---

# set allowed budget for autonomous phases — Business Outcome Brief (seed)

Intent: [Phase 04 executive seed](../phase-04-specification/doc-executive.md). Intended → delivered: the same. No deviation.

## Capability Delivered
- The Architect sets a number of fix attempts for each autonomous phase: 1, 2 or 3.
- The delegate corrects its own bundle files within that number. Then it asks the Architect.
- The default is 1. Each project keeps its current behaviour until the Architect sets a higher number.

## Risk Delta
- Risk closed: a stop for a small correction takes the Architect's time. This bundle had seven stops. The Architect replied "yes" or "ok, continue" to each stop. Three stops in Phases 01 and 02 came only from the limit of one fix attempt. A budget of 2 or 3 removes that type of stop.
- The other four stops came from the progress guard. The progress guard stays: the verifier found a problem again, or more rows failed.
- Risk closed: a loop of corrections with no limit. The number of fix attempts is never more than 3.
- Risk accepted: more verifier runs on the session model, at most 3 fix attempts at each gate.
- Risk accepted: the Architect does not see each correction before the gate. The log shows each fix attempt.
- Risk open: the new rule is in the skill text but not yet in use. This bundle ran on the old rule. The next autonomous bundle gives the first evidence.

## What It Unblocks
- Autonomous phases without a stop for small corrections.
- A clear meaning for each stop: the Architect must decide, or the delegate cannot complete the work within its fix attempts.

## Scope Note
- TCO / cost / budget: out of scope for this feature-level brief.
