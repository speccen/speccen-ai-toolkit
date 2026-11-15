---
type: Doc
audience: business
expandable: true
status: COMPLETE
description: The Architect reads every question, stop and review item with its subject in plain words
---

# Questions to the Architect: [number | text] subjects, never a bare label — Business Process & Experience (seed)

Intent: [Phase 04 business seed](../phase-04-specification/doc-business.md). Intended → delivered: the same. No deviation.

## Capability
- Each item that speccen puts to the Architect has a subject: `[number | text]`. The number keeps the item traceable. The text says what the item is about.
- An autonomous run continues when a correction only changes how a decision is recorded.

## Business Process (end to end)
- speccen finds a question for the Architect.
- speccen writes the question with its subject, for example `[03/22 | May the delegate repair the failed rows?]`.
- Each other item that the question names also gets a subject.
- The Architect reads the question and answers by number.
- speccen records the answer. The records keep their numbers.
- At the end of an autonomous run, speccen puts each delegated decision to the Architect as `[DD-<n> | what was decided]`.

## Where It Surfaces (UI/UX)
- No screen. The subjects appear in chat messages: interview rounds, stops, the review round, the end-of-run report, the resume summary.
- The subjects also appear in bundle files that the Architect reads: the stop record in `summary.md`, the `STATE.md` stop line, the reconcile report.

## What Changes for the User
- Before: "01/9 — DD-3, DD-5, DD-6 and DD-7 rest on it." The Architect opens other files to understand the question.
- After: each label has its text. The Architect understands the question from the message.
- Before: a record correction stops an autonomous run. After: the run continues, and the review round shows the correction.

## Not Included
- The labels stay.
- The record tables do not change.
- `ARCHITECTURE.md` does not change.
