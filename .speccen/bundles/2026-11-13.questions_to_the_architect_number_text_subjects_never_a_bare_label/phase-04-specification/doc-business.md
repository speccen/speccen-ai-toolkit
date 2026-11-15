---
type: Doc
audience: business
expandable: true
status: COMPLETE
description: The Architect reads every question, stop and review item with its subject in plain words
---

# Questions to the Architect: [number | text] subjects, never a bare label — Business Process & Experience (intent, seed)

## Capability
- Each item that speccen puts to the Architect has a subject: `[number | text]`. The number keeps the item traceable. The text says what the item is about.
- An autonomous run continues when a correction only changes how a decision is recorded.

## Business Process (end to end, intended)
- speccen works on a phase and finds a question for the Architect.
- speccen writes the question with its subject, for example `[03/22 | May the delegate repair the failed rows?]`.
- Each other item that the question names also gets a subject.
- The Architect reads the question and answers by number, for example "22 yes".
- speccen records the answer. The records keep their numbers, so the decision stays traceable.
- At the end of an autonomous run, speccen puts each delegated decision to the Architect as `[DD-<n> | what was decided]`.

## Where It Will Surface (UI/UX)
- No screen. The subjects appear in the chat messages: interview rounds, stops, the review round, the end-of-run report and the resume summary.
- The subjects also appear in the bundle files that the Architect reads: the stop record in `summary.md`, the `STATE.md` stop line and the reconcile report.

## What Will Change For The User
- Before: "01/9 — DD-3, DD-5, DD-6 and DD-7 rest on it." The Architect opens three files to understand the question.
- After: each label has its text, for example "[DD-3 | …]". The Architect understands the question from the message.
- Before: a record correction stops an autonomous run. After: the run continues, and the review round shows the correction.

## Not Included
- The labels stay. speccen does not remove them.
- The record tables (gate check, delegated decisions, interview tables) do not change.
- `ARCHITECTURE.md` does not change.
