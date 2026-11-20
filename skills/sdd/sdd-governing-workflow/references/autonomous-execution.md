# Autonomous Execution

**Applies when:** a phase whose effective mode is `autonomous`, the end-of-run review, and any pass that audits delegated decisions (Phase 07).

> Part of the governing skill (`../SKILL.md`). A bold section name without a file — for
> example **Configuration** or **ADR Protocol** — refers to a section of `../SKILL.md`, or of
> this file where it appears here. This file is the single source of truth for its content.

## The delegate

In `autonomous` mode you act as **the Architect's delegate**. You take the Architect's seat for
decisions: where a skill says the Architect decides, signals, confirms, approves, accepts or
rejects, you do it, on the basis below. You do **not** take the Architect's identity or the
Architect's authority records. The Architect chose this mode in advance, and that choice is the
authority you act under.

Skills write **"the Architect or its delegate"** at every touchpoint you may take. It means the
Architect when the phase's effective mode is `gated` and the delegate when it is `autonomous` —
never either at will. Where a skill says **"the Architect"** alone, that item stays with the
Architect even in `autonomous` mode (next section).

Provenance is always honest. Every record you write says "decided under delegation
(autonomous)" — never "the Architect decided" and never "I decided" (Invariant 6 still holds:
you are not an author).

## What stays with the Architect

Even in `autonomous` mode, only the Architect:

1. authors ADRs — the one exception is the `status: PENDING` placeholder ADR that Phase 03
   creates for an unresolved open question. A placeholder records the question and holds no
   decision. Only the Architect decides it: by replacing it with a decision, by deleting it, or by
   asking you to transcribe their stated decision verbatim (**Scribing a stated decision**,
   [`adr-scribing.md`](adr-scribing.md)) (Invariants 4 and 6);
2. decides discretionary promotions to the durable store (Phase 06, Step 6, path 2);
3. changes the mode or the config files (Configuration);
4. starts the optional passes (Phases 07 and 08) — and the delegate never starts `sdd-reconcile`
   either, a repo-level step run on main by whoever owns it, or by a CI step;
5. waives a planned test (Invariant 10);
6. skips a core phase — the skip warning asks the Architect to take responsibility, and you
   cannot;
7. sets aside an extension requirement that applies (see Extensions).

Everything else the Architect decides in `gated` mode is yours to decide in `autonomous` mode.

## Decision basis

You may decide only on these sources, in this order:

1. **ADRs** — the bundle's `adrs/` and the standing decisions in the durable store (a
   `status: PENDING` placeholder holds no decision and is not a basis);
2. **the Architect's own words** — the prompts recorded verbatim in `log.md`, including every
   answer to a stop;
3. **the project conventions** confirmed in the phases;
4. **frozen earlier artifacts** — the Phase 04 specification is frozen when Phase 04 closes.

Nothing else is a basis. When these sources do not determine the answer, you do not choose what
seems best: you stop (see **Stop conditions**).

## Gate test

At the end of every `autonomous` phase, before the transition, run the **gate test**:

- Evaluate the phase's own Quality Criteria checklist **item by item with cited evidence** — a
  file, anchor, scenario id or test name. A criterion that asks for the Architect's signal or
  approval is met by your recorded decision and its basis.
- Run the phase-specific checks in the phase skill's `references/autonomous.md` (its **Mode behaviour**).
- Write the result into the phase's `summary.md` under the fixed heading
  `## Delegate gate check`: one row per item — `item | result | evidence | verified`.
- **Who checks what.** The self-check owns everything inside the bundle. The verifier owns only
  claims about the code and the repository. The verifier never reads the bundle.
- **Claims.** When you write a gate row that rests on code or repository evidence, record that
  row's load-bearing claims in the same step. At the gate the list already exists.
  - Record the claims directly under the gate table, under `Claims`, one line each:
    `K-<n> (row <N>) · claim · how to check · expected`.
  - **How to check** is preferably a command whose output settles the claim.
  - A `path:line` is allowed. The claim is about the content, not the line number.
  - Each claim is settled in one or two tool calls. If it cannot be, split it or drop it.
- **What goes on the list.**
  - **Exhaustive claims first.** A row that claims something holds everywhere, or nowhere,
    carries one claim that covers the whole scope: a count or a "none found" check. For
    example: `grep -rn 'new HttpClient(' src | wc -l` = 0. Spot checks never confirm such a row
    on their own.
  - Other rows: at most 3 claims, the ones the row's conclusion rests on.
  - Every count that a conclusion depends on.
  - Verbatim quotes only of convention rules that bind the change. A rule from a technology the
    change does not touch is cited by file and is not on the list.
  - **Hard cap: 15 claims per run.** If more qualify, keep the 15 whose failure would change a
    conclusion, and mark the rest `not on list — low risk`.
  - Each phase's `references/autonomous.md` names the source of its claims.
- **Self-check.** Check every row yourself for the six common failures, and fix what you find.
  Run it at the same time as the verifier (next bullet):
  1. **Quotes** — every quote of the Architect matches `log.md` word for word.
  2. **References** — every `path:line` and anchor still points at what the row says; re-open
     the files you edited after you wrote the row.
  3. **Latest answer** — no record (phase file, DD, ADR, summary) is behind the newest Architect
     statement in `log.md`.
  4. **Index** — `index.md` lists every file this phase wrote.
  5. **Interview structure** — every round holds only the frontier, and every question one
     decision.
  6. **Subjects** — every question and item put to the Architect has a `[number | text]`
     subject; no label stands alone.
  Record the self-check in one line above the gate table: `Self-check: done — N corrections`.
- **Verifier.** Where the host can run subagents, launch the **verifier** (`speccen-worker`, on
  the session model — see Subagent Execution) with the verifier work order. Launch it as soon as
  the claim list is final. This is safe beside the self-check: the self-check edits only bundle
  files, and the verifier reads only code and the repository.
  - The verifier settles the listed claims and reads nothing beyond what settles them.
  - It returns one result per claim. Append each result to its claim line, after `→`.
  - **`slip`** — the content is there, but the line number, path or count is a little off, and
    the conclusion stands.
  - For a slip, the verifier gives the correct value, and you correct the citation.
  - A slip is not a failed row: it uses no fix attempt and triggers no re-run.
  - **`wrong`** — the content is not there, or the value differs in a way the conclusion depends
    on.
  - A `wrong` claim fails its row, and the fix loop below applies.
  - If the verifier is unsure which kind it is, it reports `wrong`.
  - It may add at most 2 `noticed:` lines about something adjacent that looks wrong.
  - Answer each `noticed:` line in a row at the foot of the gate table:
    `noticed-<n> | <the line> | corrected, or not relevant, because … | <evidence> | —`.
  - A `noticed:` line that affects a conclusion becomes a `wrong` claim in the next run.
- **The `verified` column.**
  - A row is `confirmed (run N)` when every claim it has is `confirmed`, or `slip` with the
    citation corrected.
  - A row without claims reads `n/a — bundle-internal`.
  - A row whose claims the cap left off the list reads `not on list — low risk`.
  - If no row cites code or repository evidence, launch no verifier. All rows then read
    `n/a — bundle-internal`.
  - Without subagent support, write `not run` in that column.
- No question of this phase that was parked with "later" is still unanswered.
- Every active extension of this phase was applied: each applicable requirement is met or marked
  "not applicable, because …", and the Extensions table in `phase.md` is complete.
- If any item fails, fix it and run the test again — up to the phase's effective `fixes`
  attempts (Configuration; default `5`). A later verifier run re-checks only (a) the `wrong`
  claims, (b) the claims whose file changed during the fix, and (c) any `noticed:` line promoted
  to a claim. Slips are never re-checked. Rows it does not re-check keep their last
  `confirmed (run N)`.
- Stop (stop condition 5) when:
  1. the fix you would make next changes a phase conclusion, an ADR, or what a delegated
     decision decides; or
  2. a re-checked row still fails and the budget is used up; or
  3. a run makes no progress: a rule breach the run before named is still there, or more rows
     fail than in the run before.

  A fix that only repairs how a decision is recorded is not such a change: splitting a question
  into one per decision with the same answer each, moving a question to the round its
  dependencies allow, correcting a citation, or raising a decision's materiality to
  `MATERIAL — unconfirmed`. Each new or changed entry keeps the decision's answer and states
  the repair; the review round still puts every one of them to the Architect.

  Log each attempt as `fix attempt <n> of <fixes>: run <N> failed rows <list>`.
- After a stop, the Architect's answer sets which claims the next verifier run re-checks, and
  whether further fix attempts are allowed. Without that, one run follows, and a `wrong` claim
  stops again. Claims it does not re-check keep their last result. The verifier reports on every
  listed claim in one run.

You review your own work, so the evidence is the point: an item without cited evidence has not
passed.

## Decisions you take

When a decision arises that the basis leaves open and that is **not material**, decide it. If the
answer could reasonably have gone another way and it affects the work product, record it in
`delegated-decisions.md`. Pure style within the conventions is not recorded.

In an interview (Phases 01, 03 and 04) you work through the same numbered questions the Architect
would get (`sdd-interview`). Every question you answer there is a delegated decision, linked
to its question reference — for example `01/7` — so a reviewer can follow your decision tree.

A decision is **material** as defined in **Gate Enforcement** → Material decisions. A material
decision that the basis does not determine is a stop.

## Stop conditions

Stop — do not continue, do not guess — when:

1. the basis leaves more than one reasonable answer to a **material** decision — unless the
   phase's effective `stops` is `proceed` (see **Proceeding on a proposal**);
2. the basis conflicts with itself: ADR against ADR, or an ADR against the brief;
3. a new dependency is needed;
4. a deviation goes beyond implementation detail — it would change an acceptance scenario, a
   contract, the scope or the **Why** of its plan phase (smaller deviations you decide and
   record);
5. a gate test still fails after the fix budget, makes no progress, or needs a fix that changes
   a conclusion, an ADR or what a delegated decision decides (Gate test);
6. a planned test still fails after the retry budget: a rejected implementation is reverted and
   retried **at most twice**, and the Phase 03 loop runs **at most two** iterations;
7. an action is irreversible or outside the skills — a force-push, a deploy, deleting data, any
   external side effect, or a revert that cannot be limited to the files this iteration changed
   (creating prototype worktrees and branches as Phase 03 Step 5a defines is not such an action;
   pushing, merging or deleting them is);
8. this host cannot run a check the gate test requires, for example the planned tests.

In Phase 01, an open question that Phase 02 can investigate is a working hypothesis, not a stop
— see `skills/sdd/sdd-feature-analysis/references/autonomous.md`.

A stop produces:

- `STATE.md`: `Phase Status` → `AWAITING ARCHITECT REVIEW`; `Pending Architect Action` →
  `Stopped (autonomous) — <one-line reason>`, where an item the reason names has its
  `[number | text]` subject;
- the phase's `summary.md`: an open item with the exact question, the options, your lean and the
  evidence — every item with a `[number | text]` subject, readable without the rest of the bundle
  (Structured questions);
- a `log.md` entry recording the stop;
- the **stop round**: the stopped questions as one numbered interview round, each with your
  proposed answer (`sdd-interview` → Stop rounds).

Collect before you stop: carry on only with work that does not depend on the open questions, and
put them to the Architect together. Then wait. The Architect's answers are logged verbatim
(Invariant 5) and become part of the basis. "Later" parks a question that does not block the rest
of the phase — the run carries on, but that phase's gate test cannot pass while it is open. The
mode stays `autonomous` — a stop does not change it. Never continue on an assumed answer.

## Proceeding on a proposal

`stops` (see Configuration) decides what condition 1 does. With `ask` — the default — it is a
stop. With `proceed`, you do not halt on a material decision the basis leaves open:

- Take your own **proposed answer** (the one you would have put in the stop round) and carry on.
  Choose the answer the basis supports best; where it supports none, the most reversible one.
- Record it as a delegated decision with `Materiality` → `MATERIAL — unconfirmed`, so it is
  visible in the review round, and in the phase `summary.md` under its open items, with a
  `[number | text]` subject (Structured questions).
- Condition 1 is the **only** stop `proceed` removes. Conditions 2 to 8 stay hard stops: they
  mean the basis is broken, or the action is not yours to take.
- The Architect's answers in the review round are logged verbatim and become basis for later
  phases. An `OVERRIDDEN` decision re-enters Phase 03 through the ADR Protocol, as for any
  delegated decision.

## Delegated decisions record

`delegated-decisions.md` is an append-only bundle file, created at the first recorded decision (a
bundle that never runs `autonomous` has none). Entries are numbered `DD-1`, `DD-2`, …:

```markdown
---
type: DelegatedDecisions
description: Decisions taken under delegation in autonomous mode — review, adopt or override
---

# [FEATURE_NAME] — Delegated Decisions

[Index](./index.md) · [State](./STATE.md) · [Log](./log.md)

---

## DD-1 — [short title]

|     | Info |
| --- | --- |
| **Phase** | [phase name] |
| **When** | YYYY-MM-DD HH:MM UTC |
| **Question** | [what had to be decided] |
| **Interview question** | [its reference, for example `01/7` — when the decision came from an interview] |
| **Decision** | [what was decided under delegation (autonomous)] |
| **Basis** | [ADR ids, log.md entries, convention names, frozen-artifact anchors] |
| **Alternatives** | [the options not taken] |
| **Materiality** | [`not material` · `MATERIAL — unconfirmed` (taken under `stops: proceed`)] |
| **Status** | DELEGATED |
```

- The status is `DELEGATED`. Only the Architect decides `ADOPTED` (optionally pointing to an ADR
  the Architect writes) or `OVERRIDDEN` (the Architect writes an ADR — it can be scribed on
  request — and the ADR Protocol re-enters Phase 03). You record the status the Architect states
  in the review round (`sdd-interview` → The review round), and never choose one.
- A delegated decision reaches the durable store only if the Architect adopts it as an ADR and
  promotes it in Phase 06, Step 6.
- Review surface: each phase `summary.md` shows the number of delegated decisions with a link;
  the resume summary shows how many are unreviewed; the Phase 06 summary lists them.

## Transitions and the end of a run

An `autonomous` transition runs the Phase Transition Protocol as written, with the passed gate
test as its trigger. The phase-boundary commits are the Architect's revert points.

The run continues from phase to phase until a stop, or until Phase 06 completes. When Phase 06
completes under `autonomous`: `STATE.md` shows `CLOSE-OUT PHASE` / `COMPLETE` with `Pending
Architect Action` → `Review the delegated decisions and decide the graduation proposal`; the
discretionary graduation proposal is prepared and left pending; the optional passes are named, never
started. Then report to the Architect in one message, with `[number | text]` subjects (Structured
questions): the phases run, the gate checks passed, the delegated decisions recorded, any stops and
their answers, and the pending graduation proposal. When any delegated decision or gate check
exists, the report also recommends the Retrospective (Phase 07), which audits them against the code;
only the Architect starts it. It also lists any prototype branches left for the Architect to delete.
Then offer the **review round** (`sdd-interview` → The review round): every delegated decision and every
pending graduation candidate, as one numbered interview.
