---
type: Doc
audience: executive
expandable: true
status: COMPLETE
description: The Architect sets how many fix attempts the delegate makes on a failed gate test
---

# set allowed budget for autonomous phases — Business Outcome Brief (intent, seed)

## Capability To Be Delivered
- The Architect sets a number of fix attempts for each autonomous phase: 1, 2 or 3.
- The delegate corrects its own bundle files within that number. Then it asks the Architect.

## Risk Delta (expected)
- Risk this closes: a stop for a small correction takes the Architect's time. In issue #25, the Architect almost always approved these corrections.
- Risk this closes: a loop of corrections with no limit. Today, the number of verifier runs after a stop has no limit.
- Risk accepted: more verifier runs on the session model. The maximum is 3 fix attempts at each gate.
- Risk accepted: the Architect does not see each correction before the gate. The log shows each fix attempt.

## What It Will Unblock
- Autonomous phases without a stop for small corrections.
- A clear meaning for each stop: the Architect must decide, or the delegate cannot complete the work within its fix attempts.

## Scope Note
- TCO / cost / budget: out of scope for this feature-level brief.
