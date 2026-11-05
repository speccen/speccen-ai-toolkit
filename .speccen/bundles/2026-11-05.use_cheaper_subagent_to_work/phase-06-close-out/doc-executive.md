---
type: Doc
audience: executive
expandable: true
status: COMPLETE
description: The main session now sends simple search questions to a worker on a cheaper model tier
---

# Use cheaper subagent to work — Business Outcome Brief (seed)

Intent: [Phase 04 executive seed](../phase-04-specification/doc-executive.md). Intended → delivered: the same. No deviation.

## Capability Delivered
- The main session sends simple search questions to a worker on a cheaper model tier.
- The main session keeps all decisions.
- The verifier needs fewer runs on the session model to check each phase gate.

## Risk Delta
- Risk this closes: the model cost per feature is higher than necessary.
- Risk accepted: a worker on a cheaper model tier can miss or misquote code. The main session opens each file location again before it uses the evidence.
- Risk accepted: the second verifier run checks fewer rows. The second run checks only the failed rows and the rows that cite a changed file.
- Risk open: nobody has measured the saving yet. The next bundle supplies the measurement.

## What It Unblocks
- A measured comparison of the cost per feature, before and after this feature.
- More autonomous phases, because each autonomous phase needs fewer verifier runs on the session model.

## Scope Note
- TCO / cost / budget: out of scope for this feature-level brief.
