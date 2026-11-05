| | |
|---|---|
| **Target** | speccen plugin `26.1104.2` — `skills/sdd/00-governing-workflow/SKILL.md`, `02-code-analysis`, `05-implementation`, config template |
| **Status** | Proposal — nothing changed |
| **Date** | 2026-11-05 |

## 1. Problem

Claude Code usage stats: *"90% — Give simple subagents a cheaper model."*

speccen already has model tiers (`phases.<phase>.model` → `models.<tier>`). The project maps
`code-analysis` to `economy` → `haiku`. But in the evidence bundle, **13 subagents ran, and all
13 ran on the session model**:

| What ran | Count | Model | Why |
|---|---|---|---|
| Gate-check verifier | 9 | session | Rule: the verifier always runs on the session model |
| Explore code searches (Phase 02) | 4 | session | Logged as *"Not speccen work-order units"* — no tier applies |
| Phase 02 evidence reading (the only `economy` unit) | 0 | — | Ran inline in the main session |

Two causes:

1. **Code searching is not a unit.** The Units table covers only the evolution-gap reading,
   prototypes, close-out documents, retrospective and reference. The heavy, read-only work —
   searching the codebase — has no unit, so no tier. The skill even says *"Nothing else runs in
   a subagent"*, yet the delegate ran four searches as subagents anyway, because the work needs
   it. The rule and the practice differ.
2. **The verifier runs too often.** Every gated phase needed a second verifier run:
   Phase 01 re-run; Phase 02 run 1 confirmed 11 of 19 rows; Phase 03 run 2 confirmed 5 of 15;
   Phase 04 run 1 found 12 defects, run 2 found 2. Each second run re-checks **every** row.
   Most failures were of a few known kinds: quotes not verbatim, wrong line numbers, records
   behind the latest Architect answer, `index.md` out of date.

## 2. Change A — make code searching a tiered unit

**Goal:** read-only code searches run on the cheap tier. The main session keeps every conclusion.

### A1. Governing skill → Subagent Execution → Units

Add one row, and change the sentence below the table.

```diff
 | Phase | Unit | Parallel | Stays in the main session |
 |---|---|---|---|
+| 02, 03, 04, 05 | a **code search**: find and quote code that answers one stated question (Code search below) | yes | every conclusion drawn from it; the re-check of key findings |
 | 02 | the evidence reading for the evolution-gap determination (Step 5) | — | the determination |
 ...
-Nothing else runs in a subagent. **Decision seats never do**: ...
+Nothing else runs in a subagent — a code search that is not launched as this unit runs inline.
+**Decision seats never do**: ...
```

### A2. Governing skill → Subagent Execution → new section "Code search"

```markdown
### Code search

A code search answers **one stated question** about the code, with evidence. It is read-only and
takes no decision.

- The work order states the question, the search breadth (`quick` · `medium` · `thorough`) and
  the place to start, if known.
- The worker returns **findings only**: each one a `path:line` and a short verbatim quote, plus
  what it did not find. No conclusions, no recommendations.
- The worker writes no files. Its report is the output. `Outputs:` in the work order is `none —
  report only`.
- The main session re-opens every finding it uses in the phase file before citing it. A search
  report is never cited as evidence on its own.
- Several searches with independent questions may run in parallel.

The tier is the phase's `model` (see Model). A search in Phase 05 uses `phases.implementation.model`.
```

> Why "findings only": a cheap model is good at finding and quoting, and weaker at judging. The
> main session already re-checks key findings (the bundle log says so), and the verifier checks
> the phase. So a weaker search costs little quality.

### A3. Governing skill → Configuration → Keys

```diff
-- `model`: `code-analysis`, `compliance-review`, `close-out`, `retrospective`, `reference` — the
-  phases with subagent units.
+- `model`: `code-analysis`, `compliance-review`, `specification`, `implementation`, `close-out`,
+  `retrospective`, `reference` — the phases with subagent units.
```

### A4. Config template (`.speccen/speccen-config.yaml`)

```diff
   specification:             # 04 — the plan and the intent freeze
     mode: inherit
     stops: inherit
+    model: economy           # code searches
     lock: false
   implementation:            # 05 — the code and the accept
     mode: inherit
     stops: inherit
+    model: economy           # code searches
     lock: false
```

`compliance-review` stays `balanced`: its main unit is the prototype, which writes code. Its code
searches use the same tier. If that is too costly, a later change can give searches their own
key — not proposed now, to keep the config simple.

Upgrading: the existing rule already adds a missing phase `model` as `inherit`. So old project
files keep today's behaviour until a person sets the tier. Bump the template `version` to `2` so
the session-start upgrade adds the two keys.

### A5. Phase skills — point to the unit

- `02-code-analysis` Step 2 and Step 3, add one line:
  *"Code questions may run as code-search units (governing skill → Subagent Execution → Code
  search). The analysis itself stays in the main session."*
- `05-implementation` Step 3, add the same line for questions that come up during a checklist item.
- `interview` (the lookup rule for Phases 03 and 04, "may look it up in the code"): add *"inline,
  or as a code-search unit"*.

### A6. Log line

No new format. The existing line already covers it:
`- **HH:MM — CODE ANALYSIS subagent** — code search: <question> · model: economy → haiku (project)`

## 3. Change B — fewer and smaller verifier runs

**Goal:** the verifier runs once in most phases, and a second run checks only what changed. The
verifier stays on the session model — that rule does not change.

### B1. Governing skill → Autonomous Execution → Gate test — a self-check before the verifier

Insert before the verifier bullet:

```markdown
- **Self-check before the verifier.** Before you launch the verifier, check every row yourself
  for the four common failures, and fix what you find:
  1. **Quotes** — every quote of the Architect matches `log.md` word for word.
  2. **References** — every `path:line` and anchor still points at what the row says; re-open
     the files you edited after you wrote the row.
  3. **Latest answer** — no record (phase file, DD, ADR, summary) is behind the newest Architect
     statement in `log.md`.
  4. **Index** — `index.md` lists every file this phase wrote.
  Record the self-check in one line above the gate table: `Self-check: done — N fixes`.
```

### B2. Gate test — the second run re-checks only what changed

```diff
-- If any item fails, fix it once and run the test again. If it still fails, stop.
+- If any item fails, fix it once and run the test again. The second verifier run re-checks
+  (a) every row that failed, and (b) every row whose evidence is in a file you changed during
+  the fix. Rows it does not re-check keep their `confirmed` value and say `confirmed (run 1)`.
+  If a re-checked row still fails, stop.
```

> Why (b): a fix can break a row that passed. Re-checking every row whose evidence file changed
> catches that, without paying for rows nothing touched.

## 4. What does not change

- The verifier and every decision seat stay on the session model.
- No global default subagent model in Claude Code. It would also move the verifier, without
  speccen knowing, and the log would name the wrong model.
- The one-writer rule: workers still never write `STATE.md`, `log.md` or `index.md`.

## 5. Risks

| Risk | Effect | Control |
|---|---|---|
| Haiku misses code a stronger model would find | A weaker analysis | Findings-only reports; the main session re-opens what it cites; the verifier on the session model checks the phase |
| Haiku quotes code wrongly | A wrong citation | The main session re-opens every finding before it cites it (A2) |
| The self-check takes main-session tokens | Less net saving | Four fixed checks, not a full re-run of the gate |
| B2 misses a row broken by the fix | A wrong `confirmed` | Rows with evidence in a changed file are always re-checked |

## 6. How to measure

Run the next bundle with this change, then compare with the evidence bundle:
- In `log.md`, count the subagent lines per model. Target: code searches on `economy`.
- Count the verifier runs per phase. Target: one run in most phases.
- Compare `/usage` for the two sessions.

## 7. Decisions for the Architect (yes / no)

| # | Proposal | Why this option | Answer |
|---|---|---|---|
| 7/1 | Code searches **share the phase's `model` tier**. No separate search key. | One key per phase keeps the config simple. A separate key can be added later if a phase needs it, without breaking existing files. | yes / no |
| 7/2 | Phase 03 code searches **run on the phase's tier, `balanced` (sonnet)**. `economy` is not forced for them. | Follows from 7/1. Prototypes need `balanced`, and Phase 03 runs few searches, so the extra cost is small. Sonnet is still cheaper than the session model. | yes / no |
| 7/3 | Bring the new keys to existing projects by **raising the template to `version: 2`**. Missing keys are added as `inherit`. | Uses the existing session-start upgrade. Old projects keep today's behaviour until someone sets a tier, so nothing changes without a choice. | yes / no |

