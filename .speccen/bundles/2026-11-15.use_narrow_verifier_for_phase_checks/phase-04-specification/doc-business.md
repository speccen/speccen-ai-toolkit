---
type: Doc
audience: business
expandable: true
status: COMPLETE
description: Intent — the delegate lists the code facts behind each phase in a fact list, and a checker run confirms only those facts
---

# use narrow verifier for phase checks — Business Process & Experience (intent, seed)

## Capability
- The delegate writes a short fact list: the code facts that each phase rests on. A checker run confirms only these facts.
- The delegate corrects a slip at once. A slip is a small error in a line number, a path or a count. A slip does not start a new checker run.

## Business Process (end to end, intended)
1. The delegate finishes the work of a phase.
2. The delegate writes the gate table. For each item that rests on the code, the delegate writes at most 3 facts in the fact list. One checker run has at most 15 facts.
3. The checker run starts. The delegate's own review takes place at the same time.
4. The checker run gives one result for each fact: confirmed, slip or wrong.
5. The delegate corrects each slip. A wrong fact starts a repair.
6. The next checker run reads only the wrong facts and the facts on changed files. It also reads the facts that come from a hint. A hint is a note from the last checker run about a problem outside the fact list. When a hint affects a conclusion, the delegate adds a wrong fact for the problem that the hint names.
7. When no fact is wrong, the phase closes.

## Where It Will Surface (UI/UX)
- No screen. The change is in the skill files of the workflow.
- The Architect sees the fact list and the results in each phase summary, under the gate table.

## What Will Change For The User
- Before: a checker run reads the full phase again. A slip often causes a repair.
- After: a checker run reads only the facts in the fact list. A slip causes no repair.

## Not Included
- No change to the repair limit, the stop rules or the items of the delegate's own review.
- No change to gated mode.
