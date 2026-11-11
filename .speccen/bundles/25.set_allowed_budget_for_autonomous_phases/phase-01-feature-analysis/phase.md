---
type: Phase
phase: "01 — Feature Analysis"
status: COMPLETE
description: Add a `fixes` config key that sets how many times the delegate may repair a failing gate test, with progress, conclusions and ceiling guards
---

<a id="phase-top"></a>
# set allowed budget for autonomous phases — Feature Analysis

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

Source: GitHub issue #25, "Gate test: a fix budget for autonomous phases", stored as
[files/gh-25-gate-test-fix-budget.md](../files/gh-25-gate-test-fix-budget.md). The issue has a
problem statement with evidence (§1), a proposed change with seven text diffs in six subsections (§2.1 – §2.6; §2.3 holds two), the
effect (§3), rejected alternatives (§4), and an empty §5 "Decisions for the plugin Architect".
The Architect named the bundle "set allowed budget for autonomous phases".

### Request Summary

**Kind:** fix (provisional until Phase 03 — chosen at session start; see 01/1).

In an `autonomous` phase the delegate ends the phase with a gate test, and a verifier re-checks
every row. Today the delegate may repair a failing gate test only once; a row that still fails
on the next verifier run is a stop (stop condition 5). The request adds a **fix budget**: a new
config key `fixes` (values `1` · `2` · `3`, default `1`) at the top level and per phase, which
sets how many fix attempts the delegate makes before it stops. The key works independently of
`stops`, applies in every `autonomous` phase, and has no effect in a `gated` phase.

Three guards bound the budget:

- **Progress** — each later verifier run must fail fewer rows than the run before, or the run
  stops at once.
- **Conclusions** — a fix that would change a phase conclusion, a delegated decision or an ADR
  stops the run at once.
- **Ceiling** — at most `3` fix attempts.

The request also says what happens after a stop (the Architect's answer may allow more fix
attempts; without that, one run), adds a log line per attempt, changes the wording of stop
condition 5, adds the key to the Keys table, the template (raised to `version: 3`), the upgrade
rule, effective-settings resolution and the fail-safe, and repeats the template change in
`README.md`.

**Done when:** the §2 text changes land in the governing skill and `README.md`, every other place that restates the changed rules agrees, and default behaviour is unchanged.
Hypothesis — acceptance is settled in Phase 04 (01/7, H-4).

### Domain Context

speccen is a phase-gated, spec-driven development workflow shipped as a Claude Code (and Copilot
CLI) plugin of Markdown skills. The domain here is the **autonomous-mode gate test**: how the
delegate proves a phase is complete before it advances without the Architect, and when it must
hand control back.

The problem, as the brief states it: most stops on a second verifier run are **precision
faults** — a line number one off, a count that differs between two files, a wrong term, a quote
not word for word — not wrong conclusions. The Architect almost always answers "yes, go ahead";
the stop costs attention and adds no decision. The brief's evidence: a client-project bundle
(Phase 02: 7 → 5 failed rows, converging, stopped anyway) and the retrospective of this
repository's own bundle `2026-11-05.use_cheaper_subagent_to_work`, where one row failed on five
runs through four stop rounds. The brief also notes that 26.1108.1 bounded which rows a run after
a stop re-checks, but set no limit and no progress rule.

The capability served is fewer stops that carry no decision, while a run that does not converge,
or a repair that would change a conclusion, still returns to the Architect. The brief separates
two questions that are mixed today: `stops` — may the delegate decide a material question for
the Architect? — and the fix budget — how often may the delegate repair its own work before it
asks for help?

### Scope

**In scope** (from the brief's §2)

- Governing skill (`skills/sdd/00-governing-workflow/SKILL.md`):
  - Autonomous Execution → Gate test: budgeted fix attempts, the three stop triggers, the
    per-attempt log line, the after-stop rule (§2.1).
  - Autonomous Execution → Stop conditions: condition 5 reworded (§2.2).
  - Configuration → Keys: `fixes` and `phases.<phase>.fixes`; "Which phases take which key"
    (§2.3).
  - Configuration → Templates: `version: 3`, top-level `fixes: 1` with its comments, the legend
    line, `fixes: inherit` on the five phases that take `stops` (§2.4).
  - Configuration → Upgrading the project file: absence value of `fixes`, the version-3 upgrade
    sentence (§2.5).
  - Configuration → Effective settings: `fixes` resolution and default; fail-safe line (§2.6).
- `README.md` — the template copy (§2.4).

**Out of scope**

- Other autonomous budgets: the Phase 05 reject-and-retry limit ("at most twice"), the Phase 03
  loop limit ("at most two"), and `prototypes` (01/3).
- Relaxing the verifier: rejected in the brief §4 ("Let the verifier ignore precision faults").
- Tying the budget to `stops: proceed`: rejected in the brief §4.
- `gated` phases: `fixes` has no effect there (brief §2).

**Unclear — carried forward**

- Whether `fixes` also governs a phase skill's own repair rule at its gate, or only the
  governing gate test — Phase 03 (01/4, O-1), with facts from Phase 02 (P02-2).
- The decisions the empty §5 should hold — Phase 03 (01/5, O-2).
- Facts about the current text — Phase 02 (P02-1 – P02-3).
- Acceptance scenarios — Phase 04 (01/7, O-4).

<a id="terminology"></a>
### Key Concepts & Terminology

| Term | Meaning in this request (the brief's terms, and the speccen terms it relies on) |
|---|---|
| **delegate** | The Architect's delegate: the AI acting in the Architect's seat for decisions in an `autonomous` phase, on the recorded decision basis only. It runs the gate test and makes the fix attempts. |
| **gate test** | The delegate's end-of-phase check in an `autonomous` phase: the Quality Criteria item by item with cited evidence, written as `## Delegate gate check`. |
| **verifier** / **verifier run** | The `speccen-worker` run, on the session model, that re-opens each row's evidence and confirms it. Runs are numbered `run 1`, `run 2`, …. |
| **row** | One line of the gate check table: `item \| result \| evidence \| verified`. A row the verifier does not confirm has failed. |
| **re-check** | A later verifier run over failed rows and rows whose evidence is in a changed file; other rows keep `confirmed (run N)`. |
| **fix attempt** | One repair by the delegate of the failing rows, followed by a verifier run. |
| **fix budget** / **`fixes`** | The proposed key: how many fix attempts the delegate makes before it stops. Values `1` · `2` · `3`; default `1`; per phase `inherit` · `1` · `2` · `3`. |
| **precision fault** | A failure that changes no conclusion: a wrong line number, a count mismatch, a wrong term, a quote not word for word. |
| **progress (guard)** | Each re-check must fail fewer rows than the run before; otherwise stop at once. |
| **conclusions (guard)** | A fix that changes a phase conclusion, a delegated decision or an ADR stops the run at once. |
| **ceiling (guard)** | At most 3 fix attempts. |
| **stop** / **stop condition 5** | The delegate halts and waits for the Architect. Condition 5 today: "a gate test still fails after one fix attempt". |
| **`stops`** | The existing key: `ask` (a material open decision is a stop) or `proceed` (the delegate takes its proposal and records it for review). |
| **template `version`** | The version of the project config template that drives the session-start upgrade; the brief raises it to `3`. |
| **plugin Architect** | The Architect of the speccen plugin itself (§5 heading), as distinct from an Architect running a bundle in a client project. |

<a id="known-facts"></a>
### Known facts

- The brief is GitHub issue #25 in `speccen/speccen-ai-toolkit`, open, no comments (stored in
  `files/`).
- The brief's §5 "Decisions for the plugin Architect" is empty.
- The session-start answers: Work kind `fix`, Mode `autonomous` (log 11:05).
- The project config sets `stops: proceed` (`.speccen/speccen-config.yaml:14`).
- The bundle runs on branch `feature/set-allowed-budget-for-autonomous-phases`; the Architect
  stated "no push on main is allowed" (log 11:05).

<a id="hypotheses"></a>
## Working Hypotheses

| # | Hypothesis | Confirms / refutes | Settles in |
|---|---|---|---|
| H-1 | The kind is **fix**: the request corrects a stop rule that stops without adding a decision, rather than adding a new capability. | Phase 03 records the kind with the decisions; a reading that the `fixes` key is a new capability makes it a feature. | Phase 03 |
| H-2 | `fixes` governs every repair-and-re-check rule at an `autonomous` gate, so no phase keeps its own "fix once". | Refuted if a phase-specific gate rule must stay at one repair for a reason the basis gives. | Phase 03 (facts from Phase 02, P02-2) |
| H-3 | The decisions §5 leaves empty are the values §2 proposes: default `1`, values `1` – `3`, ceiling `3`, progress as fewer failed rows than the run before (brief §2: "fewer rows"; stop at "as many rows or more"), the conclusions guard, template `version: 3`. | Phase 03 puts each as a question; an Architect answer that differs refutes it. | Phase 03 |
| H-4 | Done when: the §2 text changes land in the governing skill and `README.md`, every other place that restates the changed rules agrees, and default behaviour is unchanged. | Phase 04 acceptance scenarios. | Phase 04 |

<a id="open-items"></a>
## Open Questions

| # | Question | Settles in |
|---|---|---|
| O-1 | Does `fixes` also govern a phase skill's own repair rule at its gate (H-2)? | Phase 03 (facts from Phase 02) |
| O-2 | The decisions §5 leaves empty (H-3). | Phase 03 |
| O-3 | Facts P02-1 – P02-3 about the current repository text (below). | Phase 02 |
| O-4 | Acceptance scenarios and "done when" (H-4). | Phase 04 |

**For Phase 02** (facts in the code — not asked in the interview):

| # | Fact to establish |
|---|---|
| P02-1 | The line references in the brief (`:1176-1182`, `:1212`, `:694-698`, `:741-790`, `:857-861`, `:902-905`, `:925-941`, `:1183-1184`, `:1249`, `README.md:245-290`) point at the text the brief quotes, at repository HEAD 26.1108.1. |
| P02-2 | Every place outside the brief's diffs that restates the one-fix rule, stop condition 5, the Keys table, the template `version`, the upgrade rule or the per-phase key list — other phase skills, `ARCHITECTURE.md`, `README.md`, `agents/speccen-worker.md`. |
| P02-3 | How the existing upgrade rule handles a project file at `version: 2` when the template is at `3`, and whether the version-1 example and the version-2 sentence need a counterpart. |

None of these blocks Phase 02: the brief names the files to analyse.

<a id="interview"></a>
## Interview

Mode: `autonomous` (bundle config); `stops: proceed` (project config). The delegate answered from
the decision basis: the Architect's own words in `log.md` (the session-start answers and the
prompts of 11:05), and the issue #25 brief, which the Architect authored. The brief is stored in
`files/` and referenced from `log.md` (11:07), not copied into it; the Architect confirmed that it
counts as their own words (01/9, log 11:52). No ADR and no standing decision bears on these
questions.

**Round 1**

| # | Question | Depends on | Proposed | Answer |
|---|---|---|---|---|
| 01/1 | Kind — is this a fix, provisional until Phase 03? It adds a config key, which is new behaviour of the workflow, so it could also be read as a feature. | — | yes — fix, provisional until Phase 03 | delegate: fix, provisional until Phase 03 — basis: session-start Work kind answer "fix" (log 11:05) — [DD-1](../delegated-decisions.md#dd-1); H-1 |
| 01/2 | Target — is the text to change the plugin source in this repository at HEAD (26.1108.1), not the installed plugin? | — | yes — the plugin source in this repository at HEAD (26.1108.1) | delegate: repository source at 26.1108.1 — basis: "in the speccen repo, .speccen folder + bundle of course!" (log 11:05); the brief cites 26.1108.1 (§1) — [DD-2](../delegated-decisions.md#dd-2); fact check → P02-1 |
| 01/3 | Scope — the bundle name says "allowed budget for autonomous phases"; the brief defines one budget, `fixes`, for the gate test. Is the scope only `fixes`, with the other autonomous limits (Phase 05 retries, Phase 03 loop, `prototypes`) left out? | — | yes — only `fixes`, as the brief's §2 defines it | delegate: only `fixes` — basis: brief §2 "A new config key `fixes`" and §2.1 – §2.6, which change no other limit — [DD-3](../delegated-decisions.md#dd-3) |
| 01/4 | Reach — does `fixes` govern every repair rule at an `autonomous` gate, including one a phase skill sets at its own gate, as a working hypothesis for Phase 03? The brief says "It applies to **every `autonomous` phase**" (§2), and its diffs change only the governing skill. | — | yes, as a working hypothesis | hypothesis: every repair rule at an `autonomous` gate — settles in Phase 03 (H-2, O-1); facts → Phase 02 (P02-2) — [DD-4](../delegated-decisions.md#dd-4) |
| 01/5 | §5 is empty — take §2's values (default `1`, `1` – `3`, ceiling `3`, progress as fewer failed rows than the run before, the conclusions guard, `version: 3`) as the proposal for Phase 03 to decide? | — | yes, as a working hypothesis | hypothesis: §2's values are the proposal — settles in Phase 03 (H-3, O-2) — [DD-5](../delegated-decisions.md#dd-5) |
| 01/6 | Evidence — the client-project table in §1 comes from a bundle that is not in this repository. Take it as stated? | — | yes, as the stated problem | delegate: accepted as the Architect's stated evidence — basis: brief §1 — [DD-6](../delegated-decisions.md#dd-6) |

**Round 2** — the frontier after round 1: 01/7 depends on the scope (01/3) and the reach (01/4).

| # | Question | Depends on | Proposed | Answer |
|---|---|---|---|---|
| 01/7 | Done when — the §2 text changes land in the governing skill and `README.md`, every other place that restates the changed rules agrees, and default behaviour is unchanged? | 01/3, 01/4 | yes, as a working hypothesis | hypothesis: as proposed (H-4) — settles in Phase 04 (O-4) — [DD-7](../delegated-decisions.md#dd-7) |

No question was answered "later". Every delegated decision of this phase is `not material`:
the reach of `fixes` (01/4) would be material if decided, so Phase 01 does not decide it — it is
recorded as working hypothesis H-2 and decided in Phase 03.

**Round 3 — stop round** (stop condition 5: the gate test still failed after one fix attempt) —
answered by the Architect

| # | Question | Depends on | Proposed | Answer |
|---|---|---|---|---|
| 01/8 | [01/8 \| May the delegate fix the two remaining problems and run the checker once more?] The re-check covers the two failing items and every item that cites a file the fix changes. | — | yes | Architect: "yes" (log 11:52) |
| 01/9 | [01/9 \| Does issue #25, which the Architect wrote, count as the Architect's own words?] The rules accept only chat messages in the log; the issue is in `files/`, referenced from log 11:07. | — | yes | Architect: "yes" (log 11:52) |
| 01/10 | [01/10 \| Should the log be corrected by adding an entry, not by editing the old one?] | — | yes | Architect: "yes" (log 11:52) |

<a id="outcome"></a>
## Outcome

The request is a provisional **fix** to the autonomous gate test: a `fixes` key (default `1`,
ceiling `3`) lets the delegate repair a failing gate test more than once, bounded by progress and
conclusions guards, independent of `stops`, with the default unchanged. Phase 02 establishes
where the current text states the rules the brief changes (P02-1 – P02-3); Phase 03 settles the
reach of `fixes` (O-1) and the decisions §5 leaves empty (O-2).
