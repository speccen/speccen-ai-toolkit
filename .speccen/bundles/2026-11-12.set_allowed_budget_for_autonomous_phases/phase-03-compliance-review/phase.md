---
type: Phase
phase: "03 — Compliance & Review"
status: COMPLETE
description: No bundle ADRs; four standing decisions, all compliant; twelve open questions settled by the delegate (two MATERIAL — unconfirmed); Definition of Ready met
---

<a id="phase-top"></a>
# set allowed budget for autonomous phases — Compliance & Review

[Index](../index.md) · [State](../STATE.md) · [Log](../log.md)

---

<a id="adrs"></a>
## ADRs in scope

| ADR | Tier | Status | Decision | Compliance |
|---|---|---|---|---|
| `.speccen/decisions/2026-11-05.bundle_store_lookup_unit.md` | standing | DECIDED | One search unit for code, bundle and store | compliant |
| `.speccen/decisions/2026-11-05.code_search_agent.md` | standing | DECIDED | Searches run on `speccen-worker`, not on a host's built-in search agent | compliant |
| `.speccen/decisions/2026-11-05.code_search_tier.md` | standing | DECIDED | Searches share the phase's `model` tier — no separate search key | compliant |
| `.speccen/decisions/2026-11-05.self_check_interview_structure.md` | standing | DECIDED | The gate-test self-check has a fifth check: interview structure | compliant |

No bundle ADR exists (`adrs/` holds no file). The standing decisions carry no `description` key, so the
Decision column gives each one's H1 title.

<a id="extensions"></a>
## Extensions applied

| Extension | Why | Where it applies | Outcome |
|---|---|---|---|
| — | — | — | No extensions for this phase |

`.speccen/extensions/` does not exist in this repository.

<a id="compliance"></a>
## Compliance Iterations

**Iteration 1 (2026-11-11)** — no bundle ADR to process; the standing decisions checked against
the analysis and the change:

| Standing decision | What it governs | Does the change touch it? |
|---|---|---|
| One search unit for code, bundle and store | the search unit (Subagent Execution → Units) | no — `fixes` adds no unit; the verifier is already a listed unit |
| Searches run on `speccen-worker` | the agent a search runs on | no |
| Searches share the phase's `model` tier | no separate search key | no — `fixes` is a budget, not a model key; the verifier stays on the session model |
| The self-check has a fifth check | the five self-check items (`SKILL.md:1160-1167`) | no — the five items stay; 03/6 renames only the count in the record line (`:1168`) |

No analysis file changed for compliance. The interview below settles the open items of Phases 01
and 02.

<a id="interview"></a>
## Interview

Mode: `autonomous` (bundle config); `stops: proceed` (project config). The delegate answered from
the decision basis: the issue #25 brief (`files/gh-25-gate-test-fix-budget.md`, authored by the
Architect), the Architect's prompts in `log.md`, and the Phase 02 facts. With `stops: proceed`, a
material question the basis does not fully decide gets the delegate's answer, recorded
`MATERIAL — unconfirmed` and put first in the end-of-run review. Round 1 holds the questions that
depend on no other; round 2 the three that depend on a round-1 answer.

**Round 1**

| # | Question | Depends on | Proposed | Answer |
|---|---|---|---|---|
| 03/1 | [03/1 \| Is the kind of request confirmed as a fix?] Phase 01 recorded it as provisional (H-1). | — | yes — fix | delegate: fix — basis: the session-start Work kind answer "fix" (log 11:05); the brief corrects a stop rule that "costs the Architect's attention and does not add a decision" (§1) — [DD-9](../delegated-decisions.md#dd-9) |
| 03/2 | [03/2 \| Does the fix budget also govern the Phase 05 accept check, so a spent or stalled budget there still leads to rejection and revert, not to a stop?] Phase 05 Step 7 says "fix once and test again" (`05-implementation/SKILL.md:324`); Phase 01 hypothesis H-2. | — | yes | delegate: yes — basis: the brief, "It applies to **every `autonomous` phase**" (§2), and the five phases that take `fixes` include `implementation` (§2.3); without this, `phases.implementation.fixes` would have no effect. The Phase 05 outcome (reject, then 05b; stop after two rejections) stays — [DD-10](../delegated-decisions.md#dd-10) |
| 03/3 | [03/3 \| Does the ceiling of 3 fix attempts stay, rather than looping with no ceiling until the check passes?] The brief caps at 3 (§2, guard 3) and rejects "Unbounded retries" (§4). During Phase 02 the Architect said "I don't know how to express in simple English that have to loop until issues are fixed" (log 15:45). | — | yes — keep the ceiling of 3 | delegate: yes, keep 3 — basis: brief §2 guard 3 and §4. The 15:45 words govern how this bundle runs under today's one-fix rule; with `fixes: 3` and the progress guard, a run that converges loops on its own up to the ceiling. **MATERIAL — unconfirmed**: two statements of the Architect point different ways — [DD-12](../delegated-decisions.md#dd-12) |
| 03/4 | [03/4 \| Does the delegate stop at once when the next fix would change a phase conclusion, a delegated decision or an ADR?] | — | yes | delegate: yes — basis: brief §2, guard 2 — [DD-13](../delegated-decisions.md#dd-13) |
| 03/5 | [03/5 \| Is "no progress" measured by breaches, not by the count of failed rows: stop when a breach the run before named is still there, or when more rows fail than in the run before?] The brief measures fewer failed rows (§2 guard 1), but a later run re-checks a different set of rows (Phase 02 O-5). In this bundle, check runs 4 and 5 each failed row 20 on a different defect, and run 6 passed (log 15:42 – 15:46). | — | yes | delegate: yes — basis: brief §2 guard 1 names the intent, "the delegate is going round in circles, not converging"; the Architect's "loop until issues are fixed" (log 15:45). The brief's row count would have stopped at run 5 of this bundle, which was converging. **MATERIAL — unconfirmed**: it departs from the brief's wording — [DD-14](../delegated-decisions.md#dd-14) |
| 03/6 | [03/6 \| Is the self-check record line renamed from "N fixes" to "N corrections", so "fix" means only a gate-test fix attempt?] `SKILL.md:1168` uses "fixes" for the self-check's own count. | — | yes | delegate: yes — basis: the governing skill's rule "One meaning per word" (STE rule 4); the brief's new log line "fix attempt <n> of <fixes>" would sit next to "N fixes" with another meaning. Records in earlier bundles stay as written — [DD-16](../delegated-decisions.md#dd-16) |
| 03/7 | [03/7 \| Is the default `1`, so absence and the upgrade keep today's behaviour?] | — | yes | delegate: yes — basis: brief §2.1 ("default `1`"), §2.5 and §3 "Unchanged by default" — [DD-17](../delegated-decisions.md#dd-17) |
| 03/8 | [03/8 \| Does the template go to version 3?] | — | yes | delegate: yes — basis: brief §2.4, §2.5; the rule "When the template gains a key, its `version` goes up by one" (`SKILL.md:914-915`) — [DD-18](../delegated-decisions.md#dd-18) |
| 03/9 | [03/9 \| Does the fail-safe example (`SKILL.md:944-946`) stay unchanged?] It names only `mode` and `model`. | — | yes | delegate: yes — basis: the rule covers `fixes` on a phase that does not take it without naming it, so it stays true (Phase 02 site S-14) — [DD-20](../delegated-decisions.md#dd-20) |

**Round 2**

| # | Question | Depends on | Proposed | Answer |
|---|---|---|---|---|
| 03/10 | [03/10 \| Are the key's values `1`, `2` or `3`?] | 03/3, 03/7 | yes | delegate: yes — basis: brief §2.3; the ceiling of 3 (03/3) and the default `1` (03/7) bound it — [DD-11](../delegated-decisions.md#dd-11) |
| 03/11 | [03/11 \| Does the version row (`SKILL.md:691`) change from "the current version is `2`" to `3`?] | 03/8 | yes | delegate: yes — basis: done-when hypothesis H-4, "every other place that restates the changed rules agrees" (DD-7); with version 3 the row becomes false (Phase 02 site S-10) — [DD-15](../delegated-decisions.md#dd-15) |
| 03/12 | [03/12 \| Do the README absence values (`README.md:193`) gain `1`?] They list "(`inherit`, `ask`, `0`, `false`)". | 03/7 | yes | delegate: yes — basis: done-when hypothesis H-4 (DD-7); with default `1` the list becomes incomplete (Phase 02 site S-11) — [DD-19](../delegated-decisions.md#dd-19) |

<a id="outcome"></a>
## Outcome

The analysis complies with the four standing decisions; no bundle ADR exists. Every open item
Phases 01 and 02 sent to Phase 03 is settled:

- **Kind** — a fix (03/1).
- **Reach** — the budget governs the governing gate test and the Phase 05 accept check; Phase 05
  keeps its own outcome when the budget runs out (03/2). Phase 01 hypothesis H-2 holds.
- **Values** — `1`, `2`, `3` (03/10); default `1` (03/7); template version 3 (03/8); ceiling 3 (03/3);
  conclusions guard (03/4). Phase 01 hypothesis H-3 holds, except the progress measure.
- **Progress** — measured by breaches: stop when a breach the run before named is still there,
  or when more rows fail than in the run before (03/5). This replaces the brief's "fewer rows".
- **Restated sites** — the version row and the README absence values change; the fail-safe
  example stays (03/9, 03/11, 03/12). The Phase 05 site follows from 03/2.
- **Self-check wording** — "N corrections" (03/6).

Two answers are `MATERIAL — unconfirmed` (03/3, 03/5). They go first in the end-of-run review.

<a id="open-items"></a>
## Open Items

| # | Item | Settles in |
|---|---|---|
| O-6 | Acceptance scenarios and "done when" (Phase 01 hypothesis H-4) | Phase 04 |

No placeholder ADR: no question was answered "later".

<a id="definition-of-ready"></a>
## Definition of Ready

| Criterion | Met | Evidence |
|---|---|---|
| Every ADR file has a compliance response appended within it | yes | No bundle ADR file exists; the standing decisions are checked under [Compliance Iterations](#compliance) |
| All open questions from Phase 01 and Phase 02 are resolved or explicitly escalated | yes | Phase 02 O-1 → 03/2; O-2 → 03/3 – 03/5, 03/7, 03/8, 03/10; O-3 → 03/9, 03/11, 03/12; O-4 → 03/6; O-5 → 03/5; O-6 carried to Phase 04 ([Open Items](#open-items)) |
| Project Conventions Confirmation exists and is complete (from Phase 02) | yes | [Phase 02 conventions](../phase-02-code-analysis/phase.md#conventions) |
| The domain understanding is sufficient to write a detailed, phase-structured Implementation Plan without further analysis | yes | Phase 02 lists every site with line numbers ([restated sites](../phase-02-code-analysis/phase.md#restated-sites)); [Outcome](#outcome) fixes the values and the reach |
| No unresolved ambiguities remain that could cause the Implementation Plan to be based on incorrect assumptions | yes | The brief's off line references are corrected in Phase 02 ([restated sites](../phase-02-code-analysis/phase.md#restated-sites)); the two `MATERIAL — unconfirmed` answers are decided, only unconfirmed |
| The open items Phase 01 assigned to Phases 02 and 03 are resolved, and the kind of request is confirmed — or each is explicitly carried to Phase 04 | yes | Phase 01 O-1 → 03/2; O-2 → 03/3 – 03/5, 03/7, 03/8, 03/10; O-3 → answered in Phase 02 (line references checked against 26.1108.1, [gate row 19](../phase-02-code-analysis/summary.md#delegate-gate-check)); O-4 → Phase 04; kind → 03/1 |
| If prototypes were run: the choice is recorded as an ADR, and every prototype record has its outcome | n/a | No prototypes: no material choice had two viable approaches that a spike would decide better than reasoning; `prototypes: 0` (`.speccen/speccen-config.yaml:39`) |
| The Architect or its delegate has signalled readiness to proceed to Specification Phase | yes | The delegate's readiness decision, below; no `status: PENDING` placeholder ADR exists |

Definition of Ready satisfied. All criteria met. Ready for Phase 04 upon approval by the Architect
or its delegate.

**Readiness decision (delegate):** proceed to Phase 04 — every criterion above is met, one
iteration was enough, and no stop condition applies.
