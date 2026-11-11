---
type: Doc
audience: business
expandable: true
status: COMPLETE
description: The delegate corrects a failed gate test up to the number of fix attempts that the Architect sets
---

# set allowed budget for autonomous phases — Business Process & Experience (intent, seed)

## Capability
- The Architect sets the number of fix attempts in the project settings file: 1, 2 or 3.
- The Architect can set a different number for each phase.
- The delegate corrects a failed gate test up to that number. Then the delegate halts.

## Business Process (end to end, intended)
1. At the end of an autonomous phase, the delegate writes the gate table.
2. The verifier examines each row of the gate table.
3. If a row fails, the delegate corrects the bundle file. This is one fix attempt.
4. The verifier examines the failed rows again, and the rows that cite a changed file.
5. The delegate halts when one of these conditions is true:
   - a correction would change a conclusion, a delegated decision or an ADR;
   - the delegate used all its fix attempts;
   - the verifier finds a problem again that it found in the previous run;
   - more rows fail than in the previous run.
6. In the Implementation phase, the delegate rejects the implementation for the last three conditions. For the first condition, the delegate halts.
7. After a stop, the Architect replies. The Architect sets the rows for the next verifier run.

## Where It Will Surface (UI/UX)
- No screen. The feature shows in three places:
  - the project settings file `.speccen/speccen-config.yaml`, key `fixes`;
  - a `log.md` line for each fix attempt;
  - the gate table in each phase summary.

## What Will Change For The User
- Before: the delegate made one fix attempt. Then the delegate halted and asked the Architect.
- After: the delegate makes up to the number of fix attempts that the Architect sets.
- Before: a stop could mean "may I correct a line number?".
- After: a stop means one of two things. The Architect must decide, or the delegate cannot complete the work within its fix attempts.

## Not Included
- The default number stays 1. Projects keep their current behaviour until the Architect changes the number.
- The number is never more than 3.
- Gated phases do not change. In a gated phase, the Architect approves each gate.
- Other limits of autonomous mode do not change, for example the limit of two rejected implementations.
