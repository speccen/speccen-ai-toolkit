# Scribing a stated decision

**Applies when:** the Architect asks you to record a decision they stated into a `status: PENDING` placeholder ADR — including a "yes" to the interview's closing question "Record these decisions into their ADRs?".

> Part of the governing skill (`../SKILL.md`). A bold section name without a file — for
> example **Configuration** or **ADR Protocol** — refers to a section of `../SKILL.md`, or of
> this file where it appears here. This file is the single source of truth for its content.


A `status: PENDING` placeholder ADR (Phase 03) holds a question. The Architect closes it by
editing the file, or by asking the AI to record the decision they have stated. The AI may
transcribe it when **all** of these hold:

1. The Architect has **explicitly asked**, in this conversation ("record it", "write that into
   the ADR", or "yes" to the interview's closing question "Record these decisions into their
   ADRs?"). Answering a stop is not a request.
2. The decision is in `log.md` — in the Architect's own words, or as a proposed answer the
   Architect accepted in the interview (their "yes" is logged next to it). The transcription
   copies from there.
3. It states a decision: a choice between options, or a rule. "I don't know" or "you pick" is not
   one; then the placeholder stays `PENDING` and the stop stands. If the statement is ambiguous
   between options, ask — do not pick.
4. The file is a `status: PENDING` placeholder. A `DECIDED` ADR is never edited.

Then:

- Write the Architect's words into the `Decision` row, verbatim and quoted — or, for an accepted
  proposal, the proposal quoted and marked "accepted by the Architect in interview question N".
  Add no wording of your own.
- Set `status: DECIDED` in the frontmatter and `DECIDED` in the `Status` row. Leave
  `description`, `Subject` and `Context` as they are.
- Fill `Consequences` only with what the Architect stated; otherwise write `not stated by the
  Architect`.
- Carry on as for any new ADR: **ADR Protocol** steps 4–8 (state, compliance response, index).

The ADR is the Architect's decision, and the file carries no AI attribution (Invariant 6). The AI
did not decide: it wrote down what the Architect said.
