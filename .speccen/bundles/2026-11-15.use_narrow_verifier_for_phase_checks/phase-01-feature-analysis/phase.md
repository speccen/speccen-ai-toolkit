---
type: Phase
phase: "01 — Feature Analysis"
status: COMPLETE
description: Narrow the gate-check verifier to a capped list of code and repository claims, run it beside the self-check, and stop line-number slips from failing rows
---

<a id="phase-top"></a>
# use narrow verifier for phase checks — Feature Analysis

[Index](../index.md) · [State](../STATE.md) · [Log](../log.md)

---

<a id="extensions"></a>
## Extensions applied

| Extension | Why | Where it applies | Outcome |
|---|---|---|---|
| — | — | — | No extensions for this phase |

<a id="feature-description"></a>
## Request Description

### Request Summary

**Kind:** refactoring (provisional until Phase 03 — see 01/1).

In `autonomous` mode every core phase ends with a gate test. Today a verifier subagent
(`speccen-worker`) re-opens the evidence of every row of `## Delegate gate check`, without a
limit on what it re-reads. The request narrows that verifier:

- **Split of ownership.** The existing self-check owns everything inside the bundle. The
  verifier owns only claims about the code and the repository, and never reads the bundle.
- **A claim list, built as the rows are written.** Each claim is one line —
  `id · claim · how to check · expected` — settled in one or two tool calls, about content, not
  line numbers. Exhaustive ("everywhere" / "nowhere") rows carry one whole-scope claim; other
  rows at most 3; every load-bearing count is listed; only binding convention quotes are listed.
  A hard cap of 15 claims per run, ranked by whether a failure would change a conclusion; the
  rest are `not on list — low risk`.
- **A claim source per phase** (01 none — no verifier run; 02 – 05 as the brief's rule 5 lists).
- **Parallel launch.** The verifier starts once the claim list is final, while the self-check
  runs.
- **Two failure kinds.** `slip` (content there, citation a little off, conclusion stands) is
  corrected by the delegate and costs no fix attempt and no re-run. `wrong` fails the row and
  enters the normal fix loop. When unsure, the verifier reports `wrong`.
- **`noticed:` hints.** At most 2 per run; each answered in the gate table; one that affects a
  conclusion becomes a `wrong` claim in the next run.
- **No-run cases.** No code or repository row → no verifier, `n/a — bundle-internal`. No
  subagent support → `not run`.
- **Later runs** re-check only `wrong` claims, claims whose file changed in the fix, and
  promoted `noticed:` lines. Slips are never re-checked.
- **Unchanged:** the session model for the verifier, the `fixes` budget, the stop conditions,
  the self-check items and the log line format.

The change lands as text in the governing skill (Gate test; Subagent Execution → Units and the
work order), the `speccen-worker` agent (one bullet), the **Mode behaviour** section of Phases
01 – 05, and a version bump in `plugin.json` and `marketplace.json`.

**Done when:** the brief's Acceptance list holds — the governing skill states the split, the
claim list with its cap and exhaustive-first rule, the parallel launch, `slip` vs. `wrong`, the
`noticed:` handling, the `n/a` case and the later-runs rule; each phase skill 01 – 05 names its
claim source; the work-order template has `Claims:`, `Stop:` and the three-value return; no
skill tells the verifier to check "every row" or "every quote"; short sentences, one rule per
bullet. Whether places outside the skills that restate the verifier rule must also agree is
H-3 (settles in Phase 03); the final acceptance list is Phase 04's (O-4).

### Domain Context

speccen is a phase-gated, Architect-governed workflow shipped as a Claude Code / Copilot CLI
plugin. In `autonomous` mode the AI acts as the Architect's delegate and reviews its own work at
each gate; the verifier is the independent part of that review. The request serves the cost and
latency of autonomous runs: the brief's "Measured case (Phase 02)" puts one verifier run at about 13 minutes,
58 tool calls and about 177k tokens, finding only citation slips and one misattributed quote,
while a narrow run of 7 listed claims took 2 min 48 s and 9 tool calls and still caught a real
count error. Target: one run of at most about 5 minutes, and re-runs only when a conclusion was
at stake — while keeping an independent check of claims about the code and the repository.

### Scope

**In scope**
- The verifier's remit, its claim list (format, selection, cap), its launch timing, its failure
  kinds, its `noticed:` hints, its no-run cases, and the later-runs rule — in the governing
  skill's Gate test.
- The verifier row of Subagent Execution → Units, and the verifier work-order template.
- One bullet in `agents/speccen-worker.md`.
- One claim-source line in the **Mode behaviour** of each of Phases 01 – 05, with a pointer to
  the governing skill.
- The plugin version bump (`.claude-plugin/plugin.json`, `marketplace.json`).

**Out of scope**
- The verifier's model (stays on the session model) — brief, rule 12.
- The `fixes` budget, the stop conditions, the self-check items, the log line format — brief,
  rule 12.
- A changelog — brief, "Files to change" item 4: "The repo has no changelog."
- `gated` mode — delegate's reading, not the brief: the brief describes only the gate test of
  `autonomous` mode (Problem: "In `autonomous` mode, every phase ends with a gate test").

**Unclear — carried forward**
- Whether Phase 06 (or the optional passes) runs a gate test that would need a claim source —
  H-2, P02-3.
- Whether places outside the skills that restate the verifier rule are in scope — H-3, P02-4.
- Where the claim list is recorded in the bundle — H-4.

<a id="terminology"></a>
### Key Concepts & Terminology

| Term | As the Architect uses it |
|---|---|
| gate test | The end-of-phase check in `autonomous` mode: Quality Criteria item by item with cited evidence, written under `## Delegate gate check` |
| delegate | The AI acting in the Architect's decision seat in `autonomous` mode |
| verifier | The `speccen-worker` subagent that independently re-checks gate-table evidence; after this change, only claims about code and repository |
| self-check | The delegate's own pass over the gate rows for the common failures, before (today) or beside (after) the verifier; owns everything inside the bundle |
| narrow | Limited to a listed, capped set of claims, each settled in one or two tool calls |
| claim | One line `id · claim · how to check · expected`, about content, not line number |
| claim list | The claims for one verifier run, recorded as the gate rows are written, at most 15 |
| load-bearing claim | A claim the row's conclusion rests on |
| exhaustive claim | One whole-scope count or "none found" check for a row that says something holds everywhere or nowhere |
| claim source | What a phase's claims are drawn from (rule 5) |
| `slip` | Content there, citation (line, path or count) a little off, conclusion stands — corrected, not a failure |
| `wrong` | Content not there, or a value differing in a way the conclusion depends on — a failed row |
| `noticed:` line | A verifier hint about something adjacent that looks wrong; at most 2 per run |
| `not on list — low risk` | A qualifying claim dropped by the cap |
| `n/a — bundle-internal` | The `verified` value of a row with no code or repository evidence; when no row cites such evidence, no verifier is launched (rule 9). Without subagent support the value is `not run` instead |
| fix attempt / `fixes` | One repair of a failing gate test; the budget of such repairs (unchanged) |
| run N | The Nth verifier run of a phase's gate test |

<a id="known-facts"></a>
## Known Facts

From the Architect's brief (log 21:14) and the session-start answers (log 21:10); none is a fact
about the code.

- The bundle runs `autonomous`; the brief describes the gate test of `autonomous` mode only.
- The Architect lists four files or file groups to change, the template text, and an acceptance
  list.
- The Architect states the measured case (13 min / 58 calls / ~177k tokens versus 2 min 48 s /
  9 calls).
- Rule 12 names "the six self-check items" as unchanged.

<a id="for-phase-02"></a>
### For Phase 02 (facts in the code — not asked)

Each settles in Phase 02 (carried by O-3).

- **P02-1** — The source to change is this repository at HEAD (plugin version per
  `.claude-plugin/plugin.json`), not the installed plugin cache; confirm the version and the
  path of `marketplace.json`, and the next version string.
- **P02-2** — How many self-check items the repository's governing skill lists (the brief says
  six; check whether the text at HEAD agrees).
- **P02-3** — Whether Phase 06, 07 or 08 runs a delegate gate test or launches the verifier.
- **P02-4** — Every place that restates the verifier rule ("every row", "re-open the evidence",
  "every quote", the Units row, the work order): skills, agent, README, ARCHITECTURE.md,
  examples, commands.
- **P02-5** — The current text of Gate test, Units, the work-order template and each phase's
  Mode behaviour, as the base for the diffs.

<a id="hypotheses"></a>
## Working Hypotheses

| # | Hypothesis | Confirms / refutes | Settles in |
|---|---|---|---|
| H-1 | The kind is refactoring: the change restructures how an existing check runs, without new user-facing capability | Phase 03 finds a new config key or new artifact type → feature | Phase 03 |
| H-2 | The request needs a claim source only for the phases rule 5 lists (01 – 05); Phases 06 – 08 need none | P02-3 finds that Phase 06, 07 or 08 runs the verifier | Phase 02, then Phase 03 if refuted |
| H-3 | Every place that restates the verifier rule is brought into line, not only the four listed files — so no text anywhere still says the verifier checks every row | P02-4 lists the places; Phase 03 decides their scope | Phase 03 |
| H-4 | The claim list is recorded in the phase's `summary.md`, under `## Delegate gate check`, beside the gate table — so that "At the gate the list already exists." (brief, rule 2) and the gate table can map rows to claims | Phase 03 / 04 choose the place and format | Phase 03 |
| H-5 | Rule 1 does not widen the self-check items (rule 12 keeps them): a bundle-internal row rests on the delegate's cited evidence and the self-check, and gets `n/a — bundle-internal` | Phase 03 finds the brief needs a further self-check item | Phase 03 |

<a id="open-items"></a>
## Open Questions

| # | Open item | Settles in |
|---|---|---|
| O-1 | The kind (H-1) | Phase 03 |
| O-2 | Reach outside the four listed files (H-3), claim-list placement (H-4), the self-check's remit (H-5), Phase 06 – 08 (H-2 if refuted), and how the later-runs rule fits the standing decision that "no progress" is measured by breaches (`2026-11-11.fix_progress_by_breaches`) | Phase 03 |
| O-3 | Facts P02-1 – P02-5 | Phase 02 |
| O-4 | The final acceptance list, from the brief's Acceptance plus the outcome of O-2 | Phase 04 |

None of these blocks Phase 02: the brief names the files to analyse.

<a id="interview"></a>
## Interview

Mode: `autonomous` (bundle config); `stops: proceed` (project config). The delegate answered
from the decision basis: the Architect's own words in `log.md` — the session-start answers
(21:10), the feature name (21:12) and the brief (21:14, pasted in chat, so recorded verbatim). The
bundle has no ADR. The durable store holds prior art that bears on the questions without deciding
them:
- decision `2026-11-05.self_check_interview_structure` — the fifth self-check item (interview
  structure), added because Phase 01 verifier runs failed on it; relevant to 01/4;
- decision `2026-11-11.fix_progress_by_breaches` — "no progress" is measured by breaches, not by
  failed-row counts; a later verifier run re-checks a different set of rows; relevant to the
  later-runs rule (carried to Phase 03 under O-2);
- lesson `2026-11-05.readme_restates_config_template` — `README.md`, `ARCHITECTURE.md` and the
  worker description restate the subagent units, and an edit list missed them; basis for 01/6.

**Round 1**

| # | Question | Depends on | Proposed | Answer |
|---|---|---|---|---|
| 01/1 | Kind — record this as a refactoring, provisional until Phase 03? It changes how an existing check behaves, so it could also be read as a feature. | — | yes — refactoring, provisional | delegate: refactoring, provisional until Phase 03 — basis: session-start Work kind "refactoring" (log 21:10) — [DD-1](../delegated-decisions.md#dd-1); H-1 |
| 01/2 | Target — change the plugin source in this repository at HEAD, not the installed plugin cache? | — | yes — the repository source | delegate: the repository source — basis: brief "Files to change" names repository paths (`skills/sdd/…`, `agents/…`, `.claude-plugin/plugin.json`) (log 21:14) — [DD-2](../delegated-decisions.md#dd-2); fact check → P02-1 |
| 01/3 | Evidence — take the measured case in the brief's Problem section as stated? | — | yes — as the stated problem | delegate: accepted as the Architect's stated evidence — basis: brief, Problem (log 21:14) — [DD-3](../delegated-decisions.md#dd-3) |
| 01/4 | Self-check remit — keep the self-check items unchanged (rule 12), so a bundle-internal row is covered by the self-check and the delegate's own evidence, with no new item for rule 1? | — | yes, as a working hypothesis | hypothesis: as proposed (H-5) — settles in Phase 03 (O-2); item count → P02-2 — [DD-4](../delegated-decisions.md#dd-4) |
| 01/5 | Later phases — assume only Phases 01 – 05 need a claim source, as rule 5 lists? | — | yes, as a working hypothesis | hypothesis: as proposed (H-2) — settles in Phase 02 (P02-3) — [DD-5](../delegated-decisions.md#dd-5) |
| 01/6 | Reach — also bring into line every other place that restates the verifier rule, beyond the four listed files? | — | yes, as a working hypothesis | hypothesis: as proposed (H-3) — basis: lesson `2026-11-05.readme_restates_config_template`; places → P02-4; scope settles in Phase 03 (O-2) — [DD-6](../delegated-decisions.md#dd-6) |
| 01/7 | Claim-list place — record the claim list in the phase `summary.md`, under `## Delegate gate check`, beside the gate table? | — | yes, as a working hypothesis | hypothesis: as proposed (H-4) — settles in Phase 03 (O-2) — [DD-7](../delegated-decisions.md#dd-7) |

**Round 2** — the frontier after round 1: 01/8 depends on the reach (01/6) and the later phases
(01/5).

| # | Question | Depends on | Proposed | Answer |
|---|---|---|---|---|
| 01/8 | Done when — the brief's Acceptance list holds, extended to every place H-3 brings in? | 01/5, 01/6 | yes, as a working hypothesis | hypothesis: as proposed — settles in Phase 04 (O-4) — [DD-8](../delegated-decisions.md#dd-8) |

No question was answered "later". Every delegated decision of this phase is `not material`: the
questions that would be material if decided (01/4 – 01/8) are recorded as working hypotheses and
decided in Phase 03 or 04.

<a id="outcome"></a>
## Outcome

A provisional refactoring: the gate-check verifier becomes narrow — a capped list of at most 15
code and repository claims, built as the gate rows are written, run beside the self-check, with
`slip` versus `wrong` so citation slips cost no fix attempt and no re-run. The brief fixes the
rules, the template and the files; Phase 02 confirms the current text and every place that
restates it (P02-1 – P02-5), and Phase 03 settles the reach, the claim-list place and the
self-check remit (H-2 – H-5).
