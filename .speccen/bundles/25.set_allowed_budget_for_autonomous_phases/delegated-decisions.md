---
type: DelegatedDecisions
description: Decisions taken under delegation in autonomous mode — review, adopt or override
---

# set allowed budget for autonomous phases — Delegated Decisions

[Index](./index.md) · [State](./STATE.md) · [Log](./log.md)

---

<a id="dd-1"></a>
## DD-1 — Kind of request: fix (provisional)

|     | Info |
| --- | --- |
| **Phase** | FEATURE ANALYSIS PHASE |
| **When** | 2026-11-11 10:08 UTC |
| **Question** | Is this a fix, provisional until Phase 03? It adds a config key, which is new behaviour of the workflow, so it could also be read as a feature. |
| **Interview question** | [`01/1`](./phase-01-feature-analysis/phase.md#interview) |
| **Decision** | Decided under delegation (autonomous): fix, provisional until Phase 03 (H-1). |
| **Basis** | Session-start Work kind answer "fix" ([log.md](./log.md), 11:05). |
| **Alternatives** | feature |
| **Materiality** | not material |
| **Status** | DELEGATED |

<a id="dd-2"></a>
## DD-2 — Target: the plugin source in this repository at 26.1108.1

|     | Info |
| --- | --- |
| **Phase** | FEATURE ANALYSIS PHASE |
| **When** | 2026-11-11 10:08 UTC |
| **Question** | Is the text to change the plugin source in this repository at HEAD (26.1108.1), not the installed plugin? |
| **Interview question** | [`01/2`](./phase-01-feature-analysis/phase.md#interview) |
| **Decision** | Decided under delegation (autonomous): the plugin source in this repository at HEAD 26.1108.1; fact check P02-1 in Phase 02. |
| **Basis** | Architect: "in the speccen repo, .speccen folder + bundle of course!" ([log.md](./log.md), 11:05); brief §1 cites 26.1108.1. |
| **Alternatives** | the installed plugin cache |
| **Materiality** | not material |
| **Status** | DELEGATED |

<a id="dd-3"></a>
## DD-3 — Scope: only the `fixes` budget

|     | Info |
| --- | --- |
| **Phase** | FEATURE ANALYSIS PHASE |
| **When** | 2026-11-11 10:08 UTC |
| **Question** | The bundle name says "allowed budget for autonomous phases"; is the scope only `fixes`, with the other autonomous limits (Phase 05 retries, Phase 03 loop, `prototypes`) left out? |
| **Interview question** | [`01/3`](./phase-01-feature-analysis/phase.md#interview) |
| **Decision** | Decided under delegation (autonomous): only `fixes`, as the brief's §2 defines it; the other limits are out of scope. |
| **Basis** | Brief §2 "A new config key `fixes`" and §2.1 – §2.6, which change no other limit ([files/gh-25-gate-test-fix-budget.md](./files/gh-25-gate-test-fix-budget.md)). |
| **Alternatives** | all autonomous limits become configurable budgets |
| **Materiality** | not material |
| **Status** | DELEGATED |

<a id="dd-4"></a>
## DD-4 — Reach of `fixes`: working hypothesis for Phase 03

|     | Info |
| --- | --- |
| **Phase** | FEATURE ANALYSIS PHASE |
| **When** | 2026-11-11 10:08 UTC (re-recorded 10:20 UTC in the gate-check fix attempt) |
| **Question** | Does `fixes` govern every repair rule at an `autonomous` gate, including one a phase skill sets at its own gate, as a working hypothesis for Phase 03? |
| **Interview question** | [`01/4`](./phase-01-feature-analysis/phase.md#interview) |
| **Decision** | Decided under delegation (autonomous): recorded as working hypothesis H-2 — every repair rule at an `autonomous` gate; settles in Phase 03 (O-1), with facts from Phase 02 (P02-2). Nothing is decided in Phase 01. |
| **Basis** | Brief §2 "It applies to **every `autonomous` phase**"; its diffs change only the governing skill. Phase 01 Mode behaviour: a question a later phase can settle becomes a working hypothesis. |
| **Alternatives** | governing gate test only |
| **Materiality** | not material |
| **Status** | DELEGATED |

<a id="dd-5"></a>
## DD-5 — §5 decisions: §2's values as working hypothesis

|     | Info |
| --- | --- |
| **Phase** | FEATURE ANALYSIS PHASE |
| **When** | 2026-11-11 10:08 UTC |
| **Question** | §5 is empty — take §2's values as the proposal for Phase 03 to decide? |
| **Interview question** | [`01/5`](./phase-01-feature-analysis/phase.md#interview) |
| **Decision** | Decided under delegation (autonomous): working hypothesis H-3: default `1`, values `1` – `3`, ceiling `3`, progress as fewer failed rows than the run before, the conclusions guard, template `version: 3`; settles in Phase 03 (O-2). |
| **Basis** | Brief §2, §2.3 – §2.6; §5 empty. |
| **Alternatives** | ask the Architect to fill §5 now |
| **Materiality** | not material |
| **Status** | DELEGATED |

<a id="dd-6"></a>
## DD-6 — Evidence: client-project table accepted as stated

|     | Info |
| --- | --- |
| **Phase** | FEATURE ANALYSIS PHASE |
| **When** | 2026-11-11 10:08 UTC |
| **Question** | The client-project table in §1 comes from a bundle that is not in this repository. Take it as stated? |
| **Interview question** | [`01/6`](./phase-01-feature-analysis/phase.md#interview) |
| **Decision** | Decided under delegation (autonomous): accepted as the Architect's stated evidence. |
| **Basis** | Brief §1 (the Architect is the issue author). |
| **Alternatives** | ask for the client bundle |
| **Materiality** | not material |
| **Status** | DELEGATED |

<a id="dd-7"></a>
## DD-7 — Done when: working hypothesis

|     | Info |
| --- | --- |
| **Phase** | FEATURE ANALYSIS PHASE |
| **When** | 2026-11-11 10:20 UTC |
| **Question** | Done when — the §2 text changes land in the governing skill and `README.md`, every other place that restates the changed rules agrees, and default behaviour is unchanged? |
| **Interview question** | [`01/7`](./phase-01-feature-analysis/phase.md#interview) (round 2; depends on 01/3, 01/4) |
| **Decision** | Decided under delegation (autonomous): working hypothesis H-4, as proposed; settles in Phase 04 (O-4). |
| **Basis** | Brief §2.1 – §2.6 and §3 "Unchanged by default". |
| **Alternatives** | acceptance includes a measured run with `fixes: 3` |
| **Materiality** | not material |
| **Status** | DELEGATED |

<a id="dd-8"></a>
## DD-8 — Phase 02 gate repair: correct the log time cited in row 20, re-check without a stop

|     | Info |
| --- | --- |
| **Phase** | CODE ANALYSIS PHASE |
| **When** | 2026-11-11 14:45 UTC |
| **Question** | Check run 5 failed row 20 on one citation: the Architect's 15:43 words were cited as "log 15:44". Repair and re-check, or stop? |
| **Interview question** | — (gate repair, no interview question) |
| **Decision** | Decided under delegation (autonomous): repair the citation (15:44 → 15:43, two places) and re-check row 20, without a stop round. Row 20 failed in run 4 and run 5 (one row each, so no drop in count), but each time on a different, mechanical defect; the fix changes no conclusion, decision or ADR. |
| **Basis** | Architect: "don't you understand that [ autonomous + stops:proceed] means that you are on your won to decide?" ([log.md](./log.md), 15:43), and "I don't know how to express in simple English that have to loop until issues are fixed" ([log.md](./log.md), 15:45). |
| **Alternatives** | stop round to the Architect (current skill text, condition 5 after a stop) |
| **Materiality** | not material |
| **Status** | DELEGATED |


<a id="dd-9"></a>
## DD-9 — Kind of request: fix (confirmed)

|     | Info |
| --- | --- |
| **Phase** | COMPLIANCE & REVIEW PHASE |
| **When** | 2026-11-11 14:50 UTC |
| **Question** | Is the kind of request confirmed as a fix? |
| **Interview question** | [`03/1`](./phase-03-compliance-review/phase.md#interview) |
| **Decision** | Decided under delegation (autonomous): fix. Phase 01 hypothesis H-1 holds. |
| **Basis** | Session-start Work kind answer "fix" ([log.md](./log.md), 11:05); brief §1: the stop "costs the Architect's attention and does not add a decision". |
| **Alternatives** | feature |
| **Materiality** | not material |
| **Status** | DELEGATED |

<a id="dd-10"></a>
## DD-10 — Reach: the budget also governs the Phase 05 accept check

|     | Info |
| --- | --- |
| **Phase** | COMPLIANCE & REVIEW PHASE |
| **When** | 2026-11-11 14:50 UTC |
| **Question** | Does the fix budget also govern the Phase 05 accept check, so a spent or stalled budget there still leads to rejection and revert, not to a stop? |
| **Interview question** | [`03/2`](./phase-03-compliance-review/phase.md#interview) |
| **Decision** | Decided under delegation (autonomous): yes. Phase 05 Step 7 (`05-implementation/SKILL.md:324`) fixes up to the phase's effective `fixes`, with the same guards; when the budget is spent or stalls, the delegate rejects and runs 05b as today. Phase 01 hypothesis H-2 holds. |
| **Basis** | Brief §2: "It applies to **every `autonomous` phase**"; §2.3: `fixes` takes the same five phases as `mode`, `implementation` included — without this, `phases.implementation.fixes` would have no effect. |
| **Alternatives** | governing gate test only; Phase 05 keeps "fix once" |
| **Materiality** | not material |
| **Status** | DELEGATED |

<a id="dd-11"></a>
## DD-11 — Values `1`, `2`, `3`

|     | Info |
| --- | --- |
| **Phase** | COMPLIANCE & REVIEW PHASE |
| **When** | 2026-11-11 14:50 UTC |
| **Question** | Are the key's values `1`, `2` or `3`? |
| **Interview question** | [`03/10`](./phase-03-compliance-review/phase.md#interview) |
| **Decision** | Decided under delegation (autonomous): yes. |
| **Basis** | Brief §2.3; bounded by the ceiling of 3 ([DD-12](#dd-12)) and the default `1` ([DD-17](#dd-17)). |
| **Alternatives** | another range |
| **Materiality** | not material |
| **Status** | DELEGATED |

<a id="dd-12"></a>
## DD-12 — Ceiling: keep 3 fix attempts, not a loop with no ceiling

|     | Info |
| --- | --- |
| **Phase** | COMPLIANCE & REVIEW PHASE |
| **When** | 2026-11-11 14:50 UTC |
| **Question** | Does the ceiling of 3 fix attempts stay, rather than looping with no ceiling until the check passes? |
| **Interview question** | [`03/3`](./phase-03-compliance-review/phase.md#interview) |
| **Decision** | Decided under delegation (autonomous): keep the ceiling of 3. The Architect's 15:45 words govern how this bundle runs under today's one-fix rule; with `fixes: 3` and the progress guard, a converging run loops on its own up to the ceiling. |
| **Basis** | Brief §2 guard 3 ("At most `3` fix attempts") and §4 ("Unbounded retries" rejected); the Architect: "I don't know how to express in simple English that have to loop until issues are fixed" ([log.md](./log.md), 15:45). |
| **Alternatives** | no ceiling — loop while the progress guard holds |
| **Materiality** | MATERIAL — unconfirmed |
| **Status** | DELEGATED |

<a id="dd-13"></a>
## DD-13 — Conclusions guard: stop at once

|     | Info |
| --- | --- |
| **Phase** | COMPLIANCE & REVIEW PHASE |
| **When** | 2026-11-11 14:50 UTC |
| **Question** | Does the delegate stop at once when the next fix would change a phase conclusion, a delegated decision or an ADR? |
| **Interview question** | [`03/4`](./phase-03-compliance-review/phase.md#interview) |
| **Decision** | Decided under delegation (autonomous): yes. |
| **Basis** | Brief §2, guard 2. |
| **Alternatives** | let the budget cover such fixes |
| **Materiality** | not material |
| **Status** | DELEGATED |

<a id="dd-14"></a>
## DD-14 — Progress measured by breaches, not by the count of failed rows

|     | Info |
| --- | --- |
| **Phase** | COMPLIANCE & REVIEW PHASE |
| **When** | 2026-11-11 14:50 UTC |
| **Question** | Is "no progress" measured by breaches, not by the count of failed rows: stop when a breach the run before named is still there, or when more rows fail than in the run before? |
| **Interview question** | [`03/5`](./phase-03-compliance-review/phase.md#interview) |
| **Decision** | Decided under delegation (autonomous): yes. This replaces the brief's "fails as many rows or more than the run before". It does not depend on which rows a run re-checks (Phase 02 O-5). |
| **Basis** | Brief §2 guard 1, intent "the delegate is going round in circles, not converging"; this bundle's Phase 02 check runs 4 and 5 each failed row 20 on a different defect and run 6 passed ([log.md](./log.md), 15:42 – 15:46) — the brief's count would have stopped a converging run; the Architect: "loop until issues are fixed" ([log.md](./log.md), 15:45). |
| **Alternatives** | the brief's row count ("as many rows or more") |
| **Materiality** | MATERIAL — unconfirmed |
| **Status** | DELEGATED |

<a id="dd-15"></a>
## DD-15 — Restated site: the version row says version 3

|     | Info |
| --- | --- |
| **Phase** | COMPLIANCE & REVIEW PHASE |
| **When** | 2026-11-11 14:50 UTC |
| **Question** | Does the version row (`SKILL.md:691`) change from "the current version is `2`" to `3`? |
| **Interview question** | [`03/11`](./phase-03-compliance-review/phase.md#interview) |
| **Decision** | Decided under delegation (autonomous): yes. |
| **Basis** | Done-when hypothesis H-4 ([DD-7](#dd-7)): "every other place that restates the changed rules agrees"; version 3 ([DD-18](#dd-18)); Phase 02 site S-10. |
| **Alternatives** | leave the row unchanged |
| **Materiality** | not material |
| **Status** | DELEGATED |

<a id="dd-16"></a>
## DD-16 — Self-check line: "N corrections" instead of "N fixes"

|     | Info |
| --- | --- |
| **Phase** | COMPLIANCE & REVIEW PHASE |
| **When** | 2026-11-11 14:50 UTC |
| **Question** | Is the self-check record line renamed from "N fixes" to "N corrections", so "fix" means only a gate-test fix attempt? |
| **Interview question** | [`03/6`](./phase-03-compliance-review/phase.md#interview) |
| **Decision** | Decided under delegation (autonomous): yes, at `SKILL.md:1168`. Records in earlier bundles stay as written. |
| **Basis** | Governing skill, STE rule 4 "One meaning per word"; the brief's new log line "fix attempt <n> of <fixes>". |
| **Alternatives** | keep "N fixes" |
| **Materiality** | not material |
| **Status** | DELEGATED |

<a id="dd-17"></a>
## DD-17 — Default `1`

|     | Info |
| --- | --- |
| **Phase** | COMPLIANCE & REVIEW PHASE |
| **When** | 2026-11-11 14:55 UTC |
| **Question** | Is the default `1`, so absence and the upgrade keep today's behaviour? |
| **Interview question** | [`03/7`](./phase-03-compliance-review/phase.md#interview) |
| **Decision** | Decided under delegation (autonomous): yes. |
| **Basis** | Brief §2.1 ("default `1`"), §2.5 and §3 "Unchanged by default". |
| **Alternatives** | another default |
| **Materiality** | not material |
| **Status** | DELEGATED |

<a id="dd-18"></a>
## DD-18 — Template version 3

|     | Info |
| --- | --- |
| **Phase** | COMPLIANCE & REVIEW PHASE |
| **When** | 2026-11-11 14:55 UTC |
| **Question** | Does the template go to version 3? |
| **Interview question** | [`03/8`](./phase-03-compliance-review/phase.md#interview) |
| **Decision** | Decided under delegation (autonomous): yes. |
| **Basis** | Brief §2.4, §2.5; "When the template gains a key, its `version` goes up by one" (`SKILL.md:914-915`). |
| **Alternatives** | no version bump |
| **Materiality** | not material |
| **Status** | DELEGATED |

<a id="dd-19"></a>
## DD-19 — Restated site: the README absence values gain `1`

|     | Info |
| --- | --- |
| **Phase** | COMPLIANCE & REVIEW PHASE |
| **When** | 2026-11-11 14:55 UTC |
| **Question** | Do the README absence values (`README.md:193`) gain `1`? |
| **Interview question** | [`03/12`](./phase-03-compliance-review/phase.md#interview) |
| **Decision** | Decided under delegation (autonomous): yes. |
| **Basis** | Done-when hypothesis H-4 ([DD-7](#dd-7)); default `1` ([DD-17](#dd-17)); Phase 02 site S-11. |
| **Alternatives** | leave the list unchanged |
| **Materiality** | not material |
| **Status** | DELEGATED |

<a id="dd-20"></a>
## DD-20 — Restated site: the fail-safe example stays

|     | Info |
| --- | --- |
| **Phase** | COMPLIANCE & REVIEW PHASE |
| **When** | 2026-11-11 14:55 UTC |
| **Question** | Does the fail-safe example (`SKILL.md:944-946`) stay unchanged? |
| **Interview question** | [`03/9`](./phase-03-compliance-review/phase.md#interview) |
| **Decision** | Decided under delegation (autonomous): yes. |
| **Basis** | The rule covers `fixes` on a phase that does not take it without naming it, so it stays true; Phase 02 site S-14. |
| **Alternatives** | add `fixes` to the example |
| **Materiality** | not material |
| **Status** | DELEGATED |

<a id="dd-21"></a>
## DD-21 — Phase 03 gate fix: repair the five failed rows and re-check every row

|     | Info |
| --- | --- |
| **Phase** | COMPLIANCE & REVIEW PHASE |
| **When** | 2026-11-11 14:55 UTC |
| **Question** | Check run 1 did not confirm rows 2, 3, 13, 14 and 15 (an empty `adrs/` folder called absent; questions holding more than one decision; an unlogged quote; one decision question that differs from its interview question). The gate test allows one fix and a re-run (`SKILL.md:1176-1179`): does the re-run re-check every row? |
| **Interview question** | — (gate repair, no interview question) |
| **Decision** | Decided under delegation (autonomous): yes — the repair changed every file the rows cite, so every row is re-checked. Splitting the questions changes the record's structure, not an answer: every earlier answer stands. This is the one fix the current text allows; it does not depart from it. |
| **Basis** | Gate test: the re-run re-checks "every row that failed" and "every row whose evidence is in a file you changed during the fix" (`SKILL.md:1176-1179`). |
| **Alternatives** | re-check only the failed rows |
| **Materiality** | not material |
| **Status** | DELEGATED |

<a id="dd-22"></a>
## DD-22 — Phase 03 gate repair after the fix: repair the two failed rows and re-check, without a stop

|     | Info |
| --- | --- |
| **Phase** | COMPLIANCE & REVIEW PHASE |
| **When** | 2026-11-11 14:58 UTC |
| **Question** | Check run 2 did not confirm rows 3 and 15 (question numbers that do not run on across rounds; a default cited to a brief section that does not state it), after the one allowed fix. Repair and re-check, or stop? |
| **Interview question** | — (gate repair, no interview question) |
| **Decision** | Decided under delegation (autonomous): repair and re-check every row that cites a changed file. Progress: 5 failed rows in run 1, 2 in run 2, and no breach of run 1 came back. Renumbering changes no answer. |
| **Basis** | Architect: "don't you understand that [ autonomous + stops:proceed] means that you are on your won to decide?" ([log.md](./log.md), 15:43), and "I don't know how to express in simple English that have to loop until issues are fixed" ([log.md](./log.md), 15:45). |
| **Alternatives** | stop round to the Architect (current skill text, condition 5: the gate test still fails after one fix attempt) |
| **Materiality** | not material |
| **Status** | DELEGATED |

<a id="dd-23"></a>
## DD-23 — Phase 03 gate repair: correct the brief-section list in row 15, re-check without a stop

|     | Info |
| --- | --- |
| **Phase** | COMPLIANCE & REVIEW PHASE |
| **When** | 2026-11-11 15:01 UTC |
| **Question** | Check run 3 did not confirm row 15: its list of cited brief sections left out §2.1 and named §2.6, which no file in its scope cites. Repair and re-check, or stop? |
| **Interview question** | — (gate repair, no interview question) |
| **Decision** | Decided under delegation (autonomous): correct the list to "§1, §2, §2.1, §2.3 – §2.5, §3, §4" and re-check rows 9, 12, 14 and 15 (the rows citing `summary.md` or `delegated-decisions.md`). Progress: 2 failed rows in run 2, 1 in run 3, and no breach of run 2 came back. The fix changes no answer. |
| **Basis** | Architect: "don't you understand that [ autonomous + stops:proceed] means that you are on your won to decide?" ([log.md](./log.md), 15:43), and "I don't know how to express in simple English that have to loop until issues are fixed" ([log.md](./log.md), 15:45). |
| **Alternatives** | stop round to the Architect (current skill text, condition 5: the gate test still fails after one fix attempt) |
| **Materiality** | not material |
| **Status** | DELEGATED |

<a id="dd-24"></a>
## DD-24 — Skill-text changes stay uncommitted for the Architect

|     | Info |
| --- | --- |
| **Phase** | SPECIFICATION PHASE |
| **When** | 2026-11-11 15:06 UTC |
| **Question** | Are the skill-text changes left uncommitted in the working tree for the Architect, with only the bundle files committed at each phase transition? |
| **Interview question** | [`04/1`](./phase-04-specification/phase.md#interview) |
| **Decision** | Decided under delegation (autonomous): yes. |
| **Basis** | Phase Transition Protocol, which commits "the changed bundle files — only those"; precedent: bundle `2026-11-05.use_cheaper_subagent_to_work`, its Phase 04 question 04/2; the Architect: "feature branch, no push on main is allowed" ([log.md](./log.md), 11:05). |
| **Alternatives** | commit the skill changes with the Phase 05 transition |
| **Materiality** | not material |
| **Status** | DELEGATED |

<a id="dd-25"></a>
## DD-25 — Phase 04 gate fix: repair the five failed rows and re-check every row

|     | Info |
| --- | --- |
| **Phase** | SPECIFICATION PHASE |
| **When** | 2026-11-11 15:17 UTC |
| **Question** | Check run 1 did not confirm rows 5, 8, 12, 15 and 22 (two phase Whys without their place in the order; subtask Whys inside checklist items; words used as noun and verb in the seeds and the specification; the specification diagram sent a changed conclusion to rejection in Phase 05; traceability rows out of line with the requirements and the Test Plan, and two Architect prompts missing). The gate test allows one fix and a re-run (`SKILL.md:1176-1179`): does the re-run re-check every row? |
| **Interview question** | — (gate fix, no interview question) |
| **Decision** | Decided under delegation (autonomous): yes — the fix changed phase.md, summary.md, both seeds, specification.html and specification.md, which the rows cite, so every row is re-checked. The fix changes no requirement, no decision and no answer. This is the one fix the current text allows. |
| **Basis** | Gate test: the re-run re-checks "every row that failed" and "every row whose evidence is in a file you changed during the fix" (`SKILL.md:1176-1179`). |
| **Alternatives** | re-check only the failed rows |
| **Materiality** | not material |
| **Status** | DELEGATED |

<a id="dd-26"></a>
## DD-26 — Phase 04 gate repair after the fix: repair rows 15, 17 and 22, re-check without a stop

|     | Info |
| --- | --- |
| **Phase** | SPECIFICATION PHASE |
| **When** | 2026-11-11 19:22 UTC |
| **Question** | Check run 2 did not confirm rows 15 (more words used as noun and verb; two passives; two long sentences; three names for the project file; the guard order differed between the plan's flow and the specification; R-8 worded "the number of further fix attempts"), 17 (the render cited predates the rebuild) and 22 (the 15:43 traceability row in the wrong columns), after the one allowed fix. Repair and re-check, or stop? |
| **Interview question** | — (gate repair, no interview question) |
| **Decision** | Decided under delegation (autonomous): repair and re-check every row (the repair changed phase.md, summary.md, specification.html and specification.md). Progress: 5 failed rows in run 1, 3 in run 2, and no breach of run 1 came back. The guard order follows the specification and the plan text (conclusions first, then budget and progress), which is the more cautious reading; it changes no requirement, decision or answer. |
| **Basis** | Architect: "don't you understand that [ autonomous + stops:proceed] means that you are on your won to decide?" ([log.md](./log.md), 15:43), and "I don't know how to express in simple English that have to loop until issues are fixed" ([log.md](./log.md), 15:45). |
| **Alternatives** | stop round to the Architect (current skill text, condition 5: the gate test still fails after one fix attempt) |
| **Materiality** | not material |
| **Status** | DELEGATED |

<a id="dd-27"></a>
## DD-27 — Phase 04 gate repair: STE word use in the specification, re-check without a stop

|     | Info |
| --- | --- |
| **Phase** | SPECIFICATION PHASE |
| **When** | 2026-11-11 19:29 UTC |
| **Question** | Check run 3 did not confirm row 15 only: "fix", "pass", "upgrade" and "edit" each had two meanings or parts of speech in the specification; R-4 had 29 words; R-13 had no verb for its object; specification.md kept the old heading, two long sentences and an incomplete list of decisions. Repair and re-check, or stop? |
| **Interview question** | — (gate repair, no interview question) |
| **Decision** | Decided under delegation (autonomous): repair and re-check rows 15 – 19 and 21 – 23 (the rows citing the specification, the summary, `delegated-decisions.md` or `index.md`). Progress: 3 failed rows in run 2, 1 in run 3, and no breach of run 2 came back. The repair changes wording only, no requirement, decision or answer. |
| **Basis** | Architect: "don't you understand that [ autonomous + stops:proceed] means that you are on your won to decide?" ([log.md](./log.md), 15:43), and "I don't know how to express in simple English that have to loop until issues are fixed" ([log.md](./log.md), 15:45). |
| **Alternatives** | stop round to the Architect (current skill text, condition 5: the gate test still fails after one fix attempt) |
| **Materiality** | not material |
| **Status** | DELEGATED |

<a id="dd-28"></a>
## DD-28 — Phase 04 gate repair after the stop round: repair rows 15, 22 and 23, re-check without a stop

|     | Info |
| --- | --- |
| **Phase** | SPECIFICATION PHASE |
| **When** | 2026-11-11 19:54 UTC |
| **Question** | Check run 5 (after the stop round 04/2) did not confirm rows 15 (STE: "count" and "read" in two senses, "accept" as verb and noun, three unclear pronouns, "opening" without its noun), 22 (the 20:48 answer not in the traceability table; 15:37 called a stop-round answer) and 23 (the evidence leaves out the stop round). Repair and re-check, or stop? |
| **Interview question** | — (gate repair, no interview question) |
| **Decision** | Decided under delegation (autonomous): repair and re-check rows 15 – 19 and 21 – 23 (row 15 and the rows that cite a changed file). Progress: 3 failed rows in run 4 and 3 in run 5 (not more), and no breach that run 4 named is still there. The specification and the traceability table no longer name decision ranges, so a new decision does not make them stale. The repair changes wording only. |
| **Basis** | Architect: "don't you understand that [ autonomous + stops:proceed] means that you are on your won to decide?" ([log.md](./log.md), 15:43), and "I don't know how to express in simple English that have to loop until issues are fixed" ([log.md](./log.md), 15:45); the progress guard of [DD-14](#dd-14). |
| **Alternatives** | a second stop round to the Architect |
| **Materiality** | not material |
| **Status** | DELEGATED |

<a id="dd-29"></a>
## DD-29 — Phase 04 gate repair after check run 6: name two start prompts in the traceability table

|     | Info |
| --- | --- |
| **Phase** | SPECIFICATION PHASE |
| **When** | 2026-11-11 19:58 UTC |
| **Question** | Check run 6 did not confirm row 22: the traceability table does not name two 11:05 prompts ("/speccen:start" and "analyse the gh issue on speccen-ai-tools"). Repair and re-check, or stop? |
| **Interview question** | — (gate repair, no interview question) |
| **Decision** | Decided under delegation (autonomous): name both prompts in the row for other prompts and re-check row 22 and the rows that cite a changed file (18, 19, 21, 23). Progress: 3 failed rows in run 5, 1 in run 6, and no breach that run 5 named is still there. The repair adds a list entry only. |
| **Basis** | Architect: "don't you understand that [ autonomous + stops:proceed] means that you are on your won to decide?" ([log.md](./log.md), 15:43), and "I don't know how to express in simple English that have to loop until issues are fixed" ([log.md](./log.md), 15:45); the progress guard of [DD-14](#dd-14). |
| **Alternatives** | a stop round to the Architect |
| **Materiality** | not material |
| **Status** | DELEGATED |
