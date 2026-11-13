# Issue #26 — Questions to the Architect: [number | text] subjects, never a bare label

Source: GitHub issue #26 (speccen/speccen-ai-toolkit), author petervyvey, copied verbatim on 2026-11-13.

---

## 1. Problem

Every time speccen puts something to the Architect, it uses the bundle's bookkeeping labels as if they were words: `DD-4`, `row 16`, `O-1`, `H-2`, `P02-3`, `01/8`. Stop rounds, the review round, the end-of-run report and the stop section in a phase summary all do this. The Architect has to open three files to learn what a question is about before answering it.

The skills ask for this format. The round template (`interview/SKILL.md:88-90`) starts each question with a reference (`01/7`) and a "short title". The review round (`:158-159`) asks "one question per delegated decision (`DD-<n>`)". The stop output (`00-governing-workflow/SKILL.md:1228-1232`) asks for "the exact question, the options, your lean and the evidence", without saying the question must make sense on its own. Nothing says *in plain words*. So the AI writes for the bundle, not for the reader.

**Evidence:** bundle `25.set_allowed_budget_for_autonomous_phases`, Phase 01 stop (2026-11-11). The stop round read: "Row 7 — Known facts cites log 11:05, 11:06 … Row 16 — Materiality of 01/4 reads three ways (DD-4 a value outside `not material` · `MATERIAL — unconfirmed`) … 01/9 — DD-3, DD-5, DD-6 and DD-7 rest on it." The Architect's answer: "do you really think a human knows what DD-*, P*, etc ... is?" And when the chat version was rewritten: "nonetheless, you … you are asking it to me this way" — because the record in `summary.md` still asked in labels. The Architect then set the format: "[INTERNAL-NUMBER | HUMAN UNDERSTANDABLE TEXT]", for example "[D-1 | What should be the button's color ?]".

The labels are useful: they make every question, decision and checklist item traceable. The problem is that they stand in for the words instead of travelling with them.

## 2. Change

One rule, stated once in the governing skill and pointed to from each place that puts something to the Architect:

> **Anything put to the Architect reads on its own.** Every question, decision, checklist row or open item it mentions has a subject in the form `[INTERNAL-NUMBER | HUMAN UNDERSTANDABLE TEXT]` — for example `[D-1 | What should be the button's color?]`. The internal number keeps it traceable; the text says what it is, so the Architect can answer without opening another file. A label never stands alone.

### 2.1 Governing skill → Structured questions (after `:367`)

```diff
+**Subjects: `[INTERNAL-NUMBER | HUMAN UNDERSTANDABLE TEXT]`.** Anything put to the Architect —
+an interview round, a stop, the review round, the end-of-run report — reads on its own. Give
+every question, decision, checklist row or open item it mentions a subject in this form, for
+example `[01/7 | Which queue carries the retry?]` or `[DD-4 | Does the fix budget also cover
+Phase 05's own fix rule?]`. The number (`DD-<n>`, `01/<n>`, `O-<n>`, `H-<n>`, `P02-<n>`, a
+gate-check row) keeps it traceable; the text says what it is, so the Architect can answer
+without opening another file. A label never stands alone.
```

### 2.2 Interview → The round (`interview/SKILL.md:86-96`)

```diff
-   **01/7 — [Short title]** — [The question: one decision, stated plainly, with one line on why
-   it matters. Name the options if there are any.]
+   **[01/7 | The decision, as a plain question]** — [One line on why it matters. Name the
+   options if there are any.]
    → Proposed: [the answer you propose]
 ...
    - **One decision per question**, phrased so that a plain "yes" takes the proposed answer.
+   - **Subject format** (governing skill → Structured questions): `[01/7 | …]`; any decision,
+     item or row the question mentions gets its own `[number | text]` subject.
```

### 2.3 Interview → The review round (`:158-161`)

```diff
-- **One question per delegated decision** (`DD-<n>`): `adopt`, `override` or `later`, with your
-  proposed answer. Put the `MATERIAL — unconfirmed` decisions first.
+- **One question per delegated decision**, with the subject `[DD-<n> | what was decided]`, then
+  why, and `adopt`, `override` or `later`, with your proposed answer. Put the
+  `MATERIAL — unconfirmed` decisions first.
```

### 2.4 Governing skill → Stop conditions → A stop produces (`:1228-1232`)

```diff
-- the phase's `summary.md`: an open item with the exact question, the options, your lean and the
-  evidence;
+- the phase's `summary.md`: an open item with the exact question, the options, your lean and the
+  evidence — every item with a `[number | text]` subject, readable without the rest of the bundle
+  (Structured questions);
```

### 2.5 Governing skill → Transitions and the end of a run (`:1305-1307`)

```diff
-never started. Then report to the Architect in one message: the phases run, the gate checks
-passed, the delegated decisions recorded, any stops and their answers, and the pending
-graduation proposal.
+never started. Then report to the Architect in one message, with `[number | text]` subjects (Structured
+questions): the phases run, the gate checks passed, the delegated decisions recorded, any stops
+and their answers, and the pending graduation proposal.
```

### 2.6 Governing skill → Gate test → Self-check (`:1158-1168`)

```diff
   5. **Interview structure** — every round holds only the frontier, and every question one
      decision.
+  6. **Subjects** — every question and item put to the Architect has a `[number | text]`
+     subject; no label stands alone.
```

## 3. Effect

- The Architect answers a stop or a review round from the message alone.
- Traceability is unchanged: every number stays, inside its subject.
- Bundle-internal tables (gate check, delegated decisions, interview tables) are unchanged: they are records, not questions.

## 4. Rejected alternatives

- **Drop the labels.** They are what makes a decision tree traceable across `log.md`, the delegated decisions and the review; the Retrospective relies on them.
- **A glossary of labels.** It still sends the Architect to another place before answering.
- **Plain words only, the number as a trailing pointer.** The Architect answers by number ("8 yes"); the number must lead, next to the text it names.
- **Fix it in chat only.** The stop record in `summary.md` is what the Architect answers from when they come back later; it must read on its own too.

## 5. Decisions for the plugin Architect

1. **[1 | Should the rule be stated once and pointed to, not repeated at each site?]** (2.1, referenced from 2.2 – 2.5) → Proposed: yes.
2. **[2 | Should the rule cover only what is put to the Architect, not the bundle's record tables?]** Questions, stops, the review round and the end-of-run report are covered; the gate check, delegated-decision and interview tables are not. → Proposed: yes.
3. **[3 | Should the self-check get a sixth item for subjects?]** (2.6) → Proposed: yes.

