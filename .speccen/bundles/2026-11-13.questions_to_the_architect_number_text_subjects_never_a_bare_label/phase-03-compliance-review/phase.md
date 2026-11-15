---
type: Phase
phase: "03 — Compliance & Review"
status: COMPLETE
description: The rule's reach, form and place decided under delegation, with fourteen material answers left unconfirmed for the review round; the Architect added the narrowing of stop condition 5 to the scope
---

<a id="phase-top"></a>
# Questions to the Architect: [number | text] subjects, never a bare label — Compliance & Review

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
| `.speccen/decisions/2026-11-11.fix_budget_ceiling_10.md` | standing | DECIDED | The fix budget is at most 10 fix attempts; an invalid value counts as 1 | compliant |
| `.speccen/decisions/2026-11-11.fix_progress_by_breaches.md` | standing | DECIDED | A gate test makes no progress when a breach comes back or more rows fail — not when fewer rows fail | compliant |
| `.speccen/decisions/2026-11-12.fix_budget_default_5.md` | standing | DECIDED | The fix budget defaults to 5 fix attempts; absence and the upgrade both mean 5 | compliant |

The bundle's `adrs/` folder holds no ADR file. The standing decisions carry no `description`
key, so the Decision column gives each one's H1 title.

<a id="extensions"></a>
## Extensions applied

| Extension | Why | Where it applies | Outcome |
|---|---|---|---|
| — | — | — | No extensions for this phase (`.speccen/extensions/` does not exist) |

<a id="compliance"></a>
## Compliance Iterations

### Iteration 1 — 2026-11-13

**Bundle ADRs.** None. No compliance response is due.

**Standing (Tier-2) decisions.** Each was read and checked against the request and the Phase 02
analysis:

| Standing decision | Bears on this feature? | Finding |
|---|---|---|
| `2026-11-05.self_check_interview_structure` | yes — brief §2.6 adds a sixth self-check item next to its fifth | The change keeps item 5 as it is and adds item 6 after it (03/4). No contradiction, no override. |
| `2026-11-11.fix_progress_by_breaches` | yes — the narrowed stop condition 5 (03/16) sits in the same list of gate-test stop triggers | The narrowing changes trigger 1 ("changes … a delegated decision") only; the no-progress trigger this decision governs is untouched. No contradiction. |
| `2026-11-05.bundle_store_lookup_unit`, `2026-11-05.code_search_agent`, `2026-11-05.code_search_tier`, `2026-11-11.fix_budget_ceiling_10`, `2026-11-12.fix_budget_default_5` | no | They govern searches and the fix budget's size; the change touches neither. |

No divergence from a standing decision, so no scoped override is needed.

**Open items from Phases 01 and 02.** Each is settled in the [interview](#interview) below:

| Open item | Settled by |
|---|---|
| [O-1 \| Does the rule reach places the brief does not list — every message, record or report that puts an item to the Architect?] — now concrete: the `stops: proceed` open item, the resume summary, the interview's closing summary, the Phase 05 completion notice, the `STATE.md` stop line, and the records the Architect reads | 03/5, 03/6, 03/7, 03/9, 03/17 – 03/21 |
| [O-2 \| The three decisions in brief §5: state the rule once and point to it; cover only what is put to the Architect, not the record tables; add a sixth self-check item for subjects.] | 03/2, 03/3, 03/4 |
| [O-3 \| Does the rule cover the questions asked with the `AskUserQuestion` tool, and if so which parts?] | 03/8 |
| [O-6 \| Where in Structured questions does the rule go — after the tool's constraints, or after "A series of decisions"?] | 03/10 |
| [O-7 \| Should `README.md` and `ARCHITECTURE.md` mention the subject form where they describe stops and the review round?] | 03/14, 03/15 |
| Kind of request (Phase 01, provisional until Phase 03) | 03/1 |
| [O-4 \| What are the acceptance scenarios — when is this done?] | carried to Phase 04, as Phase 01 set |

### Iteration 2 — 2026-11-13 (the Architect's answer to the stop)

The gate test of iteration 1 failed on the interview's structure and on one decision's
materiality; the repair would change delegated decisions, so the delegate stopped
([summary.md#stop](./summary.md#stop)). The Architect answered: "include and apply this
immediately in this refactoring" (`log.md` 07:32).

<a id="scope-addition"></a>
**Scope addition — stop condition 5 narrowed (03/16).** In reply to the Architect's question "What
needs to be changed so you would not stop here in a [autonomous + proceed] mode?" (`log.md` 07:29),
the delegate proposed this change to `skills/sdd/00-governing-workflow/SKILL.md`; the Architect's
answer adds it to this bundle (03/16) and applies it to this run from now on (03/24). The
Architect's next message, "also refactor the SKILLS to have this change included in this flow"
(`log.md` 07:33), confirms that the skill text itself changes, in Phase 05 with the rest:

```diff
 - Stop (stop condition 5) when:
-  1. the fix you would make next changes a phase conclusion, a delegated decision or an ADR; or
+  1. the fix you would make next changes a phase conclusion, an ADR, or what a delegated
+     decision decides; or
 ...
+  A fix that only repairs how a decision is recorded is not such a change: splitting a question
+  into one per decision with the same answer each, moving a question to the round its
+  dependencies allow, correcting a citation, or raising a decision's materiality to
+  `MATERIAL — unconfirmed`. Each new or changed entry keeps the decision's answer and states
+  the repair; the review round still puts every one of them to the Architect.
```

and in stop condition 5 (`gov :1243-1244`): "…needs a fix that changes a conclusion, an ADR or
what a delegated decision decides".

Facts for Phase 04 (read in the current text): the trigger is
`skills/sdd/00-governing-workflow/SKILL.md:1203-1204` ("1. the fix you would make next changes a
phase conclusion, a delegated decision or an ADR; or") and repeated in stop condition 5 at
`:1243-1244` ("needs a fix that changes a conclusion, a delegated decision or an ADR (Gate
test)"). It is restated in three more places, which change with it: `skills/sdd/05-implementation/SKILL.md:326`
("If the next fix would change a phase conclusion, a delegated decision or an ADR, stop."), and
the config comment "It stops sooner when a repair makes no progress or would change a
conclusion." at `skills/sdd/00-governing-workflow/SKILL.md:750`, copied in `README.md:254`.
`ARCHITECTURE.md` does not restate it. The standing decision
`2026-11-11.fix_progress_by_breaches` governs trigger 3 and is not touched.

**Applied to this run.** Under the narrowed rule, the iteration-1 repair is a record repair, not
a change to what a decision decides: 03/5 and 03/7 are split into one question per place with
the same answer each (new 03/17 – 03/21), 03/8 and 03/12 move to round 1, and 03/11 is replaced
by 03/14 and 03/15 (its README half raised to `MATERIAL — unconfirmed`). Every changed or new DD
states its repair.

<a id="analysis-updates"></a>
### What the decisions settle

With the answers below, the change is (answers under delegation unless marked; the material ones
wait for the Architect's review — see [open items](#open-items)):

1. **The rule** — stated once, at the end of governing → Structured questions (03/2, 03/10),
   with the brief's wording, examples and label list, plus `<skill>/<n>` and `Deviation [N]`
   (03/12). It covers what is put to the Architect, not the record tables (03/3).
2. **Pointers and template changes** — the brief's places (§2.2 – §2.5; §2.6 is the self-check),
   plus the `stops: proceed` open item (03/5), the resume summary (03/17), the interview's
   closing summary (03/18), the Phase 05 completion notice (03/19), the `STATE.md` stop line
   (03/20) and the reconcile report's "Needs human resolution" list (03/6).
3. **Inherited without a pointer** — the audit and code-documentation interviews, through the
   round template (03/9); `AskUserQuestion` question text that names an item, headers exempt
   (03/8). The stop round, the Phase 03 ADR interview and Phase 06's graduation interview use
   the round template too (Phase 02, A-4, A-9, A-10), so §2.2 reaches them as a fact.
4. **Outside the rule** — record tables (03/3), the Retrospective's delegation findings (03/7)
   and the fix-attempt log line (03/21).
5. **The self-check** gets a sixth item, **Subjects** (03/4).
6. **`README.md`** mentions the subject form in its autonomous-mode section (03/14);
   `ARCHITECTURE.md` is unchanged (03/15).
7. **Stop condition 5** is narrowed as in the [scope addition](#scope-addition) (03/16, the
   Architect).

### Domain understanding

One consequence for Phase 04: inside a markdown table the subject's `|` must be escaped as `\|`
(Phase 02 Data Model); the rule's text should say so, since every phase's records are tables.

<a id="interview"></a>
## Interview

Mode: `autonomous` (bundle config); `stops: proceed` (project config). Basis: the brief (issue
#26, the Architect's own words — 01/1), the Architect's answers in `log.md` (02/1 – 02/4 at 07:03
and 07:11; 07:32), the Phase 02 analysis and conventions, and the standing decisions above. The
brief's §5 leaves three decisions "for the plugin Architect" with proposals, so the basis does
not decide them. They, the rule's reach and the README mention change what counts as done, so
they are material: under `stops: proceed` the delegate takes its proposed answer and marks it
`MATERIAL — unconfirmed` for the review round.

Re-recorded in iteration 2 under the narrowed stop condition 5 (03/16): every answer is as it was
in iteration 1; only the rounds and the split of questions changed. Repaired again after the
second stop (03/22): questions that were replaced are no longer rows of a round; they are listed
under [Replaced questions](#replaced-questions).

**Round 1** — no dependencies.

| # | Question | Depends on | Proposed | Answer |
|---|---|---|---|---|
| 03/1 | [03/1 \| Is the kind of request confirmed as a feature?] | — | yes | delegate: yes — basis: session-start Work kind "feature" (log 06:28); nothing in Phases 01 – 02 contradicts it — [DD-9](../delegated-decisions.md#dd-9) |
| 03/2 | [03/2 \| Is the rule stated once, in governing → Structured questions, and pointed to from each place, not repeated at each site?] Brief §5 decision 1. | — | yes | delegate: yes — proposal taken, `MATERIAL — unconfirmed` — basis: brief §2 "One rule, stated once in the governing skill and pointed to from each place", §5.1 "Proposed: yes" — [DD-10](../delegated-decisions.md#dd-10) |
| 03/3 | [03/3 \| Does the rule cover only what is put to the Architect, leaving the record tables — gate check, delegated decisions, interview tables — unchanged?] Brief §5 decision 2. | — | yes | delegate: yes — proposal taken, `MATERIAL — unconfirmed` — basis: brief §3 "Bundle-internal tables (gate check, delegated decisions, interview tables) are unchanged: they are records, not questions.", §5.2 "Proposed: yes" — [DD-11](../delegated-decisions.md#dd-11) |
| 03/4 | [03/4 \| Does the gate-test self-check get a sixth item, "Subjects"?] Brief §5 decision 3. | — | yes | delegate: yes — proposal taken, `MATERIAL — unconfirmed` — basis: brief §2.6, §5.3 "Proposed: yes"; standing decision `2026-11-05.self_check_interview_structure` keeps item 5 — [DD-12](../delegated-decisions.md#dd-12) |
| 03/8 | [03/8 \| In an `AskUserQuestion` call, does the rule cover the question text that names an item, with the 12-character header exempt?] No call names an item today (Phase 02, P02-4). *Moved from round 2 (iteration 2).* | — | yes | delegate: yes — proposal taken, `MATERIAL — unconfirmed` — basis: brief §2 rule "Anything put to the Architect reads on its own"; governing "**Headers ≤ 12 characters** (they are the tab labels)" (`gov :382`) — [DD-16](../delegated-decisions.md#dd-16) |
| 03/12 | [03/12 \| Does the rule's list of label kinds add `<skill>/<n>` and `Deviation [N]` to the brief's list?] Both are defined in the skills (Phase 02, P02-3). *Moved from round 2 (iteration 2).* | — | yes | delegate: yes — basis: `int :45-46`, `p05 :225`; brief §2.1 lists the label kinds that keep an item traceable — [DD-20](../delegated-decisions.md#dd-20) |
| 03/14 | [03/14 \| Should `README.md` mention the subject form in its autonomous-mode section, where it describes the stop round and the review round?] *Replaces the README half of 03/11; first put in the stop round.* | — | yes | delegate: yes — proposal taken, `MATERIAL — unconfirmed` — basis: brief §2 rule "Anything put to the Architect reads on its own"; `README.md:217-231` describes the stop round and the review round to the Architect; the brief does not decide it — [DD-26](../delegated-decisions.md#dd-26) |
| 03/15 | [03/15 \| Should `ARCHITECTURE.md` stay unchanged?] *Replaces the other half of 03/11; first put in the stop round.* | — | yes | delegate: yes — basis: `ARCHITECTURE.md:76-81` describes the interview skill, not the messages; Phase 02, P02-5 — [DD-27](../delegated-decisions.md#dd-27) |

**Round 2** — the frontier after round 1: each question below depends on where the rule lives
(03/2) or on what it leaves out (03/3).

| # | Question | Depends on | Proposed | Answer |
|---|---|---|---|---|
| 03/5 | [03/5 \| Does the `stops: proceed` open item in `summary.md` point to the rule?] (A-7) *Split in iteration 2: it held five places; the other four are 03/17 – 03/20.* | 03/2, 03/3 | yes | delegate: yes — proposal taken, `MATERIAL — unconfirmed` — basis: brief §2 rule "Anything put to the Architect reads on its own"; brief §1 "the record in `summary.md` still asked in labels" — [DD-13](../delegated-decisions.md#dd-13) |
| 03/6 | [03/6 \| Is the reconcile report's "Needs human resolution" list covered by the rule, as questions put to a human?] Its items are written "[id-A] and [id-B] … Decide: …" (A-19). | 03/2, 03/3 | yes | delegate: yes — proposal taken, `MATERIAL — unconfirmed` — basis: brief §2 rule "Anything put to the Architect"; the list ends in "Decide:", a question (`skills/sdd/reconcile/SKILL.md:159`) — [DD-14](../delegated-decisions.md#dd-14) |
| 03/7 | [03/7 \| Do the Retrospective's delegation findings stay outside the rule, as a record?] (A-15) *Split in iteration 2: the fix-attempt log line is 03/21.* | 03/3 | yes | delegate: yes — proposal taken, `MATERIAL — unconfirmed` — basis: 03/3; brief §3 "they are records, not questions" — [DD-15](../delegated-decisions.md#dd-15) |
| 03/9 | [03/9 \| Do the audit and code-documentation interviews follow the rule through the shared round template, with no pointer of their own?] (A-13, A-14) | 03/2 | yes | delegate: yes — proposal taken, `MATERIAL — unconfirmed` — basis: the interview skill's "Outside a bundle" section — "everything else (frontier, round format, answers that are not a choice, closing question) applies unchanged" (`int :39-42`) — [DD-17](../delegated-decisions.md#dd-17) |
| 03/10 | [03/10 \| Does the rule go at the end of governing → Structured questions, after the paragraph "A series of decisions"?] It governs both the tool and the interview, so it follows both. | 03/2 | yes | delegate: yes — basis: brief §2.1 places it in Structured questions; the section's last paragraph introduces the interview (`gov :395-401`) — [DD-18](../delegated-decisions.md#dd-18) |
| 03/17 | [03/17 \| Does the resume summary point to the rule?] (A-8) *Split from 03/5 in iteration 2.* | 03/2, 03/3 | yes | delegate: yes — proposal taken, `MATERIAL — unconfirmed` — basis: brief §2 rule "Anything put to the Architect reads on its own" — [DD-21](../delegated-decisions.md#dd-21) |
| 03/18 | [03/18 \| Does the interview's closing summary point to the rule?] (A-16) *Split from 03/5 in iteration 2.* | 03/2, 03/3 | yes | delegate: yes — proposal taken, `MATERIAL — unconfirmed` — basis: brief §2 rule "Anything put to the Architect reads on its own" — [DD-22](../delegated-decisions.md#dd-22) |
| 03/19 | [03/19 \| Does the Phase 05 completion notice point to the rule?] (A-17) *Split from 03/5 in iteration 2.* | 03/2, 03/3 | yes | delegate: yes — proposal taken, `MATERIAL — unconfirmed` — basis: brief §2 rule "Anything put to the Architect reads on its own" — [DD-23](../delegated-decisions.md#dd-23) |
| 03/20 | [03/20 \| Does the `STATE.md` stop line point to the rule?] (A-18) *Split from 03/5 in iteration 2.* | 03/2, 03/3 | yes | delegate: yes — proposal taken, `MATERIAL — unconfirmed` — basis: brief §2 rule "Anything put to the Architect reads on its own" — [DD-24](../delegated-decisions.md#dd-24) |
| 03/21 | [03/21 \| Does the fix-attempt log line stay outside the rule, as a record?] (A-20) *Split from 03/7 in iteration 2.* | 03/3 | yes | delegate: yes — proposal taken, `MATERIAL — unconfirmed` — basis: 03/3; brief §3 "they are records, not questions" — [DD-25](../delegated-decisions.md#dd-25) |

**Round 3 — first stop round** (stop condition 5: the repair would change delegated decisions) —
answered by the Architect. The stop put 03/13 (with 03/14 and 03/15, since answered in round 1);
the Architect then asked the question that became 03/16 (log 07:29). One answer (log 07:32) settles
rounds 3 – 5, recorded here by frontier: 03/24 depends on 03/16, and 03/13 on 03/24.

| # | Question | Depends on | Proposed | Answer |
|---|---|---|---|---|
| 03/16 | [03/16 \| Does the narrowing of stop condition 5 join this bundle's scope?] The narrowing: a fix that only repairs how a decision is recorded is not a stop. Asked by the Architect (log 07:29); the delegate's proposal is the [scope addition](#scope-addition). *Split after the second stop (03/22): it held two decisions; the other is 03/24.* | — | yes | Architect: "include and apply this immediately in this refactoring" (log 07:32) |

**Round 4** — the frontier after round 3.

| # | Question | Depends on | Proposed | Answer |
|---|---|---|---|---|
| 03/24 | [03/24 \| Does the narrowed stop condition 5 apply to this run from now on, before the skill text changes in Phase 05?] *Split from 03/16 after the second stop (03/22); in its own round after the third checker run.* | 03/16 | yes | Architect: "include and apply this immediately in this refactoring" (log 07:32) |

**Round 5** — the frontier after round 4.

| # | Question | Depends on | Proposed | Answer |
|---|---|---|---|---|
| 03/13 | [03/13 \| May the delegate re-record the Phase 03 interview — 03/8 and 03/12 moved into round 1, and 03/5 and 03/7 split into one question per place — keeping every answer as it stands?] *Dependency on 03/24 stated after the third checker run.* | 03/24 | yes | Architect: "include and apply this immediately in this refactoring" (log 07:32) — read as yes, under the narrowed rule (03/16, 03/24) |

**Round 6 — second stop round** (stop condition 5: no progress, and no further fix attempts set
after the first stop — `gov :1206-1207`, `:1210-1212`) — answered by the Architect

| # | Question | Depends on | Proposed | Answer |
|---|---|---|---|---|
| 03/22 | [03/22 \| May the delegate repair rows 7, 16 and 17 with record-only fixes, within the phase's fix budget, stopping only on a fix that changes what a decision decides?] *Dependency on 03/24 stated after the fourth checker run.* | 03/24 | yes | Architect: "continue?" (log 2026-11-15 20:08) — read as yes |
| 03/23 | [03/23 \| For the rest of this run, does an answered stop allow the phase's full fix budget again, unless the answer says otherwise?] This run only; making it part of speccen would be a scope question of its own. | — | yes | Architect: "continue?" (log 2026-11-15 20:08) — read as yes |

No question was answered "later".

<a id="replaced-questions"></a>
**Replaced questions** — kept for traceability; not part of any round.

- [03/11 \| Does `README.md` mention the subject form in its autonomous-mode section, with
  `ARCHITECTURE.md` unchanged?] — held two decisions; replaced in iteration 2 by 03/14 and 03/15
  (round 1), whose answers are the same. Its record is [DD-19](../delegated-decisions.md#dd-19).
- 03/14 and 03/15 were also put to the Architect in the first stop round; under `stops: proceed`
  they were answered under delegation, in round 1.

<a id="open-items"></a>
## Open Items

| # | Open item | Settles in |
|---|---|---|
| O-4 | [O-4 \| What are the acceptance scenarios — when is this done?] Now including the narrowed stop condition 5. | Phase 04 |
| O-8 | [O-8 \| Fourteen material answers taken under `stops: proceed` wait for the Architect] — [03/2 \| rule stated once], [03/3 \| record tables outside], [03/4 \| sixth self-check item], [03/5 \| `stops: proceed` open item], [03/6 \| reconcile report covered], [03/7 \| Retrospective findings outside], [03/8 \| `AskUserQuestion` question text covered], [03/9 \| audit and code interviews through the template], [03/14 \| `README.md` mention], [03/17 \| resume summary], [03/18 \| closing summary], [03/19 \| Phase 05 completion notice], [03/20 \| `STATE.md` stop line], [03/21 \| fix-attempt log line outside] | the review round after the run |

Iteration 1 had eight material answers; splitting 03/5 and 03/7 added five (03/17 – 03/21), and
replacing 03/11 added one (03/14, raised to `MATERIAL — unconfirmed`). DD-19, the record of the replaced 03/11, is `MATERIAL — unconfirmed` too; its
README decision is the one 03/14 puts to the review round, so it adds no fifteenth answer.

<a id="outcome"></a>
## Definition of Ready

| Criterion | Met? | Evidence |
|---|---|---|
| Every ADR file has a compliance response appended within it | yes — no bundle ADR exists | the bundle's `adrs/` holds no ADR file; standing decisions checked in [Compliance Iterations](#compliance) |
| All open questions from Phase 01 and Phase 02 are resolved or explicitly escalated | yes | O-1, O-2, O-3, O-6, O-7 and the kind settled by the interview; O-4 carried to Phase 04; O-5 closed in Phase 02 |
| Project Conventions Confirmation exists and is complete (from Phase 02) | yes | `phase-02-code-analysis/phase.md#conventions` |
| The domain understanding is sufficient to write a detailed, phase-structured Implementation Plan | yes | [What the decisions settle](#analysis-updates) and the [scope addition](#scope-addition): every file and passage to change is named |
| No unresolved ambiguities remain that could cause the plan to rest on incorrect assumptions | yes | the material answers are recorded decisions, open only to the Architect's review (O-8) |
| The open items Phase 01 assigned to Phases 02 and 03 are resolved, and the kind of request is confirmed | yes | 03/1 (feature); O-1 – O-3, O-5 – O-7 resolved; O-4 carried to Phase 04 |
| If prototypes were run: the choice is an ADR, every record has its outcome | n/a | no prototype run (`prototypes: 0`) |
| The Architect or its delegate has signalled readiness to proceed to Specification | yes | delegate readiness decision, basis: the criteria above — see the gate check in [summary.md](./summary.md#delegate-gate-check) |

Definition of Ready satisfied. All criteria met. Ready for Phase 04 upon approval by the Architect
or its delegate.
