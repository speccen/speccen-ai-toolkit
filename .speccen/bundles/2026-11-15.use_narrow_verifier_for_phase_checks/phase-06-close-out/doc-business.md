---
type: Doc
audience: business
expandable: true
status: COMPLETE
description: The delegate lists the code facts behind each phase, and a checker run confirms only those facts
---

# use narrow verifier for phase checks — Business Process & Experience (seed)

Intent: [Phase 04 business seed](../phase-04-specification/doc-business.md). Outcome: delivered as intended. Two small wording changes (see the technical seed) do not change the process.

## Capability
- The delegate writes a short fact list: the code facts that each phase rests on. A checker run confirms only these facts.
- The delegate corrects a slip at once. A slip is a small error in a line number, a path or a count. A slip does not start a new checker run.

## Business Process (end to end)
1. The delegate finishes the work of a phase.
2. The delegate writes the gate table. For each item that rests on the code, the delegate writes at most 3 facts in the fact list. One checker run has at most 15 facts.
3. The checker run starts. The delegate's own review takes place at the same time.
4. The checker run gives one result for each fact: confirmed, slip or wrong.
5. The delegate corrects each slip. A wrong fact starts a repair.
6. The next checker run reads only the wrong facts and the facts on changed files. It also reads the facts that come from a hint.
7. When no fact is wrong, the phase closes.
- When a phase has no code facts, no checker run takes place.

## Where It Surfaces (UI/UX)
- No screen. The change is in the skill files of the workflow.
- The Architect sees the fact list and the results in each phase summary, under the gate table.

## What Changes for the User
- Before: a checker run reads the full phase again. A slip often causes a repair.
- After: a checker run reads only the facts in the fact list. A slip causes no repair.
- The change starts with the next bundle. This bundle used the old checker run.

## Not Included
- No change to the repair limit, the stop rules or the items of the delegate's own review.
- No change to gated mode.
