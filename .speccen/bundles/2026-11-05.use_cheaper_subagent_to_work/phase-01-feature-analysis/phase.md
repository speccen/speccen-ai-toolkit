---
type: Phase
phase: "01 — Feature Analysis"
status: COMPLETE
description: Move read-only code searches onto the phase's cheap model tier, and cut the gate-check verifier to one run plus a delta re-check
---

<a id="phase-top"></a>
# Use cheaper subagent to work — Feature Analysis

[Index](../index.md) · [State](../STATE.md) · [Log](../log.md)

---

<a id="extensions"></a>
## Extensions applied

| Extension | Why | Where it applies | Outcome |
|---|---|---|---|
| — | — | — | No extensions for this phase |

`.speccen/extensions/feature-analysis/` does not exist in this repository.

<a id="feature-description"></a>
## Request Description

Source: GitHub issue #22, "Use cheaper subagent to work", stored verbatim in
[files/gh-22-use-cheaper-subagent.md](../files/gh-22-use-cheaper-subagent.md). The issue is a
proposal (its Status row reads "Proposal — nothing changed") with two changes (A, B), a "does not change"
list, risks, a measurement plan and three yes/no decisions (7/1 – 7/3).

### Request Summary

**Kind:** refactoring (provisional until Phase 03 — chosen at session start; see 01/1).

The request changes how speccen spends model budget on subagent work, in the speccen plugin's own
skill text and config template. It has two independent changes:

- **Change A — code searching becomes a tiered unit.** Read-only code searches ("find and quote
  code that answers one stated question") become a named subagent unit in the governing skill's
  Subagent Execution → Units table, for Phases 02, 03, 04 and 05. The unit runs on the phase's
  `model` tier. The worker returns findings only (`path:line` + short verbatim quote + what it did
  not find), writes no files, and draws no conclusions; the main session re-opens every finding
  before citing it. To make this possible in Phases 04 and 05, the `model` key is extended to
  `specification` and `implementation`, and the config template gains `model: economy` on those
  two phases with a template `version: 2` bump so the session-start upgrade adds the keys. Phase
  skills 02 (Steps 2, 3), 05 (Step 3) and `interview` (the code-lookup rule) point to the unit.
- **Change B — fewer and smaller verifier runs.** The gate test gains (B1) a fixed four-point
  **self-check** by the main session before the verifier is launched — quotes, references, latest
  answer, index — recorded as `Self-check: done — N fixes`; and (B2) a **delta re-check**: the
  second verifier run re-checks only rows that failed and rows whose evidence file changed during
  the fix; untouched rows keep `confirmed (run 1)`.

**Done when:** the governing skill, the phase skills 02 and 05, the `interview` skill and the
config template carry Changes A and B as proposed (with the §7 decisions settled), and no rule in
§4 "What does not change" is altered. Hypothesis — acceptance is settled in Phase 04 (01/4).

### Domain Context

speccen is a phase-gated, spec-driven development workflow delivered as a Claude Code (and
Copilot CLI) plugin of markdown skills. The domain here is **the workflow's own cost model**:
which work runs in a subagent, on which model tier, and how the autonomous-mode gate test is
verified.

The problem, as the brief states it: Claude Code usage stats report "90% — Give simple subagents
a cheaper model". In the evidence bundle, 13 subagents ran and all 13 ran on the session model —
9 gate-check verifier runs (by rule) and 4 Explore code searches in Phase 02 (no unit, so no
tier); the one `economy` unit ran inline. Two causes are named: code searching is not a unit
(rule and practice differ), and the verifier runs too often, with second runs re-checking every
row although most failures fall into four known kinds.

The capability served is lower token cost per bundle at unchanged decision quality: cheap models
do the finding and quoting, the session model keeps every judgement.

### Scope

**In scope**

- Governing skill (`skills/sdd/00-governing-workflow/SKILL.md`):
  - Subagent Execution → Units: the new code-search row; the changed "Nothing else runs in a
    subagent" sentence (A1).
  - Subagent Execution: a new "Code search" section (A2).
  - Configuration → Keys: `model` extended to `specification` and `implementation` (A3).
  - Configuration → Templates: `model: economy` on `specification` and `implementation`, and the
    template `version` raised to `2` (A4).
  - Autonomous Execution → Gate test: the self-check (B1) and the delta re-check (B2).
- `skills/sdd/02-code-analysis/SKILL.md` Steps 2 and 3 — pointer line (A5).
- `skills/sdd/05-implementation/SKILL.md` Step 3 — pointer line (A5).
- `skills/sdd/interview/SKILL.md` — the code-lookup rule, "inline, or as a code-search unit" (A5;
  see 01/3).
- The subagent log line format is reused unchanged (A6) — confirmed in scope as "no change".

**Out of scope** (from the brief's §4, and from this analysis)

- The verifier and every decision seat stay on the session model.
- No global default subagent model in Claude Code.
- The one-writer rule is unchanged: workers never write `STATE.md`, `log.md` or `index.md`.
- A separate config key for search tier (named in A4 as a possible later change).
- Running and reporting the §6 measurement — it needs a next bundle; a follow-up (01/4).

**Unclear — carried forward**

- The three §7 decisions (7/1 – 7/3) — Phase 03 (01/5).
- Which agent runs a code-search unit: `speccen-worker` or the host's built-in read-only search
  agent — Phase 03, with facts from Phase 02 (01/6).
- Facts about the current text (template `version` key, existing `stops: inherit` lines, the
  config-upgrade rule the brief relies on, other places that restate the Units table or the
  `model` key list) — Phase 02 (P02-2, P02-3).

### Key Concepts & Terminology

| Term | Meaning as the brief uses it |
|---|---|
| **subagent** | A separate session with fresh context, optionally on a cheaper model, that runs decision-free work. |
| **unit** | A named piece of decision-free work in the Subagent Execution → Units table that may run in a subagent. |
| **code search** | The proposed unit: find and quote code that answers **one stated question**. Read-only, no decision. |
| **search breadth** | `quick` · `medium` · `thorough` — stated in the code-search work order. |
| **findings only** | The worker's report: each finding a `path:line` and a short verbatim quote, plus what it did not find. No conclusions, no recommendations. |
| **tier** | `economy` · `balanced` · `premium` (or `inherit`) — what the work needs; mapped to a model by `models.<tier>`. |
| **`phases.<phase>.model`** | The config key that selects the tier for a phase's subagent units. |
| **session model** | The model of the main session; the verifier and decision seats always run on it. |
| **gate test** | The autonomous-mode end-of-phase check of the Quality Criteria, with cited evidence. |
| **verifier** | The `speccen-worker` run that re-opens the evidence of every gate-check row and fills the `verified` column. |
| **self-check** | The proposed four fixed checks (quotes, references, latest answer, index) the main session runs before launching the verifier. |
| **delta re-check** | The proposed second verifier run limited to failed rows and rows whose evidence file changed. |
| **`confirmed (run 1)`** | The `verified` value kept by rows the second run does not re-check. |
| **template `version`** | The version of the project config template that drives the session-start upgrade. |
| **evidence bundle** | The earlier bundle whose log produced the counts in §1 (not in this repository). |
| **work order** | The prompt that hands a unit to `speccen-worker`. For code search, `Outputs: none — report only`. |
| **decision seat** | A point where the Architect (or, in `autonomous` mode, the delegate) decides — gates, ADR handling, delegated decisions, stops, store promotions. Never run in a subagent. |
| **one-writer rule** | Only the main session writes `STATE.md`, `log.md` and `index.md`, and only the main session commits; workers never do. |

<a id="hypotheses"></a>
## Working Hypotheses

Hypotheses here are about the request only. Facts about the current repository text are listed
as "for Phase 02" items under Open Questions (P02-1 – P02-3).

| # | Hypothesis | Confirms / refutes | Checked in |
|---|---|---|---|
| H-4 | The §7 proposed answers (7/1 yes, 7/2 yes, 7/3 yes) are the intended direction. | Settled by ADRs in Phase 03. | Phase 03 |
| H-5 | Done when = the text changes land as proposed; the §6 measurement is a follow-up, not acceptance of this bundle. | Settled with the acceptance scenarios in Phase 04. | Phase 04 |
| H-6 | A code-search unit is run by `speccen-worker`, as A2 says "the worker". | Settled by an ADR in Phase 03, with the Phase 02 facts on how each agent takes a model. | Phase 03 |

### Known facts (from the brief)

- The request is a proposal; nothing has changed yet (brief Status row).
- The project maps `code-analysis` to `economy` → `haiku`; in the evidence bundle all 13
  subagents ran on the session model (brief §1 table; taken as stated — DD-4).
- The verifier stays on the session model; no global default subagent model; the one-writer rule
  stays (brief §4).

<a id="open-items"></a>
## Open Questions

| # | Question | Settles in |
|---|---|---|
| O-1 | 7/1 — Do code searches share the phase's `model` tier, with no separate search key? | Phase 03 |
| O-2 | 7/2 — Do Phase 03 code searches run on the phase's tier (`balanced`), not forced to `economy`? | Phase 03 |
| O-3 | 7/3 — Are the new keys brought to existing projects by raising the template to `version: 2`? | Phase 03 |
| O-4 | Which agent runs a code-search unit — `speccen-worker` (with the tier passed at launch) or the host's built-in read-only search agent? (H-6) | Phase 03 (facts from Phase 02) |
| O-5 | Facts P02-1 – P02-3 about the current repository text (below). | Phase 02 |
| O-6 | Acceptance scenarios and "done when" (H-5). | Phase 04 |

**For Phase 02** (facts in the code — not asked in the interview):

| # | Fact to establish |
|---|---|
| P02-1 | The repository's `skills/sdd/` files are the plugin's skills, and `.claude-plugin/plugin.json` carries version 26.1104.2 (the target named in DD-2). |
| P02-2 | The repository's config template carries `stops: inherit` per phase and a `version` key, and a session-start upgrade rule adds missing phase keys as `inherit` — the brief's A4 diff and "Upgrading" note assume this. |
| P02-3 | Where the Units table, the "Nothing else runs in a subagent" rule and the `model` key list are restated outside the governing skill (other skills, `ARCHITECTURE.md`, `README.md`, `agents/speccen-worker.md`). |

None of these blocks Phase 02: the area to analyse is named in the brief's Target row.

<a id="interview"></a>
## Interview

Mode: `autonomous` (bundle config). The delegate answered from the decision basis — the
Architect's own words in `log.md`, including the issue #22 brief and the session-start answers.

**Round 1**

| # | Question | Depends on | Proposed | Answer |
|---|---|---|---|---|
| 01/1 | Kind — is this a refactoring or a feature? It adds a unit and config keys, which is new behaviour of the workflow. | — | refactoring, provisional until Phase 03 | delegate: refactoring, provisional until Phase 03 — basis: session-start Work kind answer "refactoring" (log 17:03) — [DD-1](../delegated-decisions.md#dd-1) |
| 01/2 | Target — which text is changed: the plugin source in this repository, or the installed plugin? | — | the plugin source in this repository at HEAD (26.1104.2) | delegate: repository source at 26.1104.2 — basis: brief Target row "speccen plugin `26.1104.2`" — [DD-2](../delegated-decisions.md#dd-2); fact check → P02-1, Phase 02 |
| 01/3 | Scope — the brief's Target row reads "`skills/sdd/00-governing-workflow/SKILL.md`, `02-code-analysis`, `05-implementation`, config template"; A5 reads "`interview` (the lookup rule for Phases 03 and 04, "may look it up in the code"): add". Which holds — is `interview` in scope? | — | yes — A5 states it explicitly; the Target row is a summary | delegate: `interview` in scope — basis: brief §2 A5 — [DD-3](../delegated-decisions.md#dd-3) |
| 01/4 | Done when — does acceptance include the §6 measurement on a next bundle? | — | no — done when the text changes land; §6 is a follow-up | hypothesis: §6 is a follow-up, not acceptance — settles in Phase 04 (H-5) — [DD-5](../delegated-decisions.md#dd-5) |
| 01/5 | 7/1 — Do code searches share the phase's `model` tier, with no separate search key? | — | yes (the brief's proposal) — as a hypothesis for Phase 03 | later — open item for Phase 03 (O-1, H-4) — [DD-6](../delegated-decisions.md#dd-6) |
| 01/6 | Which agent runs a code-search unit — `speccen-worker` or the host's built-in read-only search agent (the evidence bundle used Explore)? | — | `speccen-worker`, as A2 says "the worker" | later — open item for Phase 03 (O-4, H-6); facts on how each agent takes a model → Phase 02 — [DD-7](../delegated-decisions.md#dd-7) |
| 01/7 | Evidence — the §1 counts come from an evidence bundle that is not in this repository. Take them as stated? | — | yes, as the stated problem | delegate: accepted as the Architect's stated evidence — basis: brief §1 — [DD-4](../delegated-decisions.md#dd-4) |
| 01/8 | 7/3 — Are the new keys brought to existing projects by raising the template to `version: 2`? | — | yes (the brief's proposal) — as a hypothesis for Phase 03 | later — open item for Phase 03 (O-3, H-4) — [DD-8](../delegated-decisions.md#dd-8) |

**Held back** (round 2 withdrawn — 01/10): 01/9 depends on 01/5, which was answered "later", so it was never on the frontier and is not asked.

| # | Question | Depends on | Proposed | Answer |
|---|---|---|---|---|
| 01/9 | 7/2 — Do Phase 03 code searches run on the phase's tier (`balanced`), not forced to `economy`? The brief says it "Follows from 7/1". | 01/5 | yes (the brief's proposal) — as a hypothesis for Phase 03 | held back — prerequisite 01/5 is "later" → open item for Phase 03 (O-2, H-4); [DD-9](../delegated-decisions.md#dd-9) withdrawn |

**Round 3 — stop round** (stop condition 5: the gate test failed on verifier run 2) — answered by the Architect

| # | Question | Depends on | Proposed | Answer |
|---|---|---|---|---|
| 01/10 | Row 15 — 01/9 (7/2) depends on 01/5, which was answered "later", so it was never on the frontier. Remove round 2, record 7/2 as held back with 01/5 under O-2, and mark DD-9 withdrawn (append-only note, not deleted)? | — | yes | Architect: "yes" (log 18:10) |
| 01/11 | Fix the four minor run-2 defects: add a "not applicable — autonomous" row for the interview closing-question criterion; quote both statements in 01/3 and DD-3; align DD-1 and phase.md on "provisional"; move the skill-rule line out of "Known facts (from the brief)"? | — | yes | Architect: "yes" (log 18:10) |
| 01/12 | After the fixes, how is the gate re-checked: a third verifier run on only the rows whose evidence changed (as the brief's B2 proposes), or on every row? | — | only the changed rows | Architect: "yes" (log 18:10) |
| 01/13 | This run follows the installed plugin skills (26.1103.1); the repository under change is 26.1104.2. Keep 26.1103.1 as the governing version for the rest of this bundle? | — | yes — reload only if you update the plugin | Architect: "yes" (log 18:10) |

**Round 4 — stop round 2** (stop condition 5: verifier run 3, row "one clear decision") — answered by the Architect

| # | Question | Depends on | Proposed | Answer |
|---|---|---|---|---|
| 01/14 | 01/11 bundled four fixes in one question. Accept this as a record defect — your "yes" took each proposed fix — and pass the gate? | — | yes | Architect: "yes" (log 19:03) |

<a id="outcome"></a>
## Outcome

The request is a two-part refactoring of speccen's own skill text and config template: make
read-only code searches a findings-only subagent unit on the phase's `model` tier (Phases 02–05),
and reduce gate-check verifier cost with a main-session self-check and a delta re-check. Scope,
terms and the "does not change" rules are fixed; the three §7 decisions and the choice of search
agent go to Phase 03, and the current-text facts go to Phase 02.
