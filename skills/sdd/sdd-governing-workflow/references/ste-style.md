# STE-style writing

**Applies when:** before writing any document speccen produces for people to read — the audience seeds (`doc-*.md` in Phases 02, 04 and 06) and the Phase 08 `reference.html` / `reference.md`.

> Part of the governing skill (`../SKILL.md`). This file is the single source of truth for its content.

Every document speccen **produces for people to read** is written in the **style of Simplified
Technical English (ASD-STE100)** — a controlled, unambiguous, translation-friendly register.
This covers the audience documents (`doc-*.md`, in `phase-04-specification/` and
`phase-06-close-out/`) and the Phase 08 technical reference (`reference.html` and its reduced
`reference.md`). This is *STE-styled*, not certified: follow the writing rules below, but no
approved-dictionary check is required.

Rules to apply:

1. **Short sentences.** One instruction or one idea per sentence. Aim for ≤ 20 words in
   procedural text, ≤ 25 in descriptive text.
2. **Active voice.** "The service sends a confirmation mail" — not "a confirmation mail is
   sent."
3. **Imperative for instructions.** Start an instruction with the verb: "Select a plan",
   "Record the status".
4. **One meaning per word.** Use each word in a single, common sense. Do not use a word as
   both noun and verb across the document (prefer "Start the subscription" over reusing
   "start" as a noun).
5. **No noun clusters over three words.** Break up long strings of stacked nouns.
6. **Simple tenses.** Prefer present and simple past/future. Avoid perfect and continuous
   tenses and stacked modals ("would have been able to").
7. **One topic per paragraph**, and keep paragraphs short.
8. **Consistent terminology.** Use the same word for the same thing every time — never vary
   for style. Reuse the feature's own domain terms.
9. **Plain vocabulary.** Prefer common words over elaborate ones ("use" not "utilise",
   "start" not "commence").
10. **No ambiguous pronouns.** Repeat the noun rather than a "this"/"it" whose referent is
    unclear.

This register applies to the documents speccen produces for readers — the `doc-*.md` seeds and
the Phase 08 `reference.html` / `reference.md`. It does **not** apply to the workflow's
internal analytical and control files — `phase.md`, ADRs, `summary.md`, `STATE.md`, `log.md`:
analytical writing needs the nuance and hedging STE removes, and the log is recorded verbatim.
