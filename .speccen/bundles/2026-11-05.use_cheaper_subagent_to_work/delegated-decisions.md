---
type: DelegatedDecisions
description: Decisions taken under delegation in autonomous mode — review, adopt or override
---

# Use cheaper subagent to work — Delegated Decisions

[Index](./index.md) · [State](./STATE.md) · [Log](./log.md)

---

<a id="dd-1"></a>
## DD-1 — Kind of request: refactoring (provisional)

|     | Info |
| --- | --- |
| **Phase** | FEATURE ANALYSIS PHASE |
| **When** | 2026-11-05 17:06 UTC |
| **Question** | Is the request a refactoring or a feature? It adds a subagent unit and config keys. |
| **Interview question** | `01/1` |
| **Decision** | Decided under delegation (autonomous): refactoring, provisional until Phase 03. |
| **Basis** | Session-start Work kind answer "refactoring" ([log.md](./log.md), 17:03). |
| **Alternatives** | feature |
| **Materiality** | not material |
| **Status** | DELEGATED |

<a id="dd-2"></a>
## DD-2 — Target: the plugin source in this repository at 26.1104.2

|     | Info |
| --- | --- |
| **Phase** | FEATURE ANALYSIS PHASE |
| **When** | 2026-11-05 17:06 UTC |
| **Question** | Which text is changed — the plugin source in this repository, or the installed plugin? |
| **Interview question** | `01/2` |
| **Decision** | Decided under delegation (autonomous): the plugin source in this repository at HEAD (26.1104.2). The fact is checked in Phase 02 (P02-1). |
| **Basis** | Brief Target row: "speccen plugin `26.1104.2`" ([files/gh-22-use-cheaper-subagent.md](./files/gh-22-use-cheaper-subagent.md)). |
| **Alternatives** | the installed plugin cache (26.1103.1) |
| **Materiality** | not material |
| **Status** | DELEGATED |

<a id="dd-3"></a>
## DD-3 — The `interview` skill is in scope

|     | Info |
| --- | --- |
| **Phase** | FEATURE ANALYSIS PHASE |
| **When** | 2026-11-05 17:06 UTC |
| **Question** | The brief's Target row reads "`skills/sdd/00-governing-workflow/SKILL.md`, `02-code-analysis`, `05-implementation`, config template"; A5 reads "`interview` (the lookup rule for Phases 03 and 04, "may look it up in the code"): add". Which holds — is `interview` in scope? |
| **Interview question** | `01/3` |
| **Decision** | Decided under delegation (autonomous): yes — the A5 pointer line in `interview` is in scope. |
| **Basis** | Brief §2 A5, third bullet ([files/gh-22-use-cheaper-subagent.md](./files/gh-22-use-cheaper-subagent.md)). |
| **Alternatives** | leave `interview` unchanged |
| **Materiality** | not material |
| **Status** | DELEGATED |

<a id="dd-4"></a>
## DD-4 — The §1 evidence counts are taken as stated

|     | Info |
| --- | --- |
| **Phase** | FEATURE ANALYSIS PHASE |
| **When** | 2026-11-05 17:06 UTC |
| **Question** | The §1 counts come from an evidence bundle that is not in this repository. Take them as stated? |
| **Interview question** | `01/7` |
| **Decision** | Decided under delegation (autonomous): yes — they are the Architect's stated problem evidence and are not re-verified. |
| **Basis** | Brief §1 ([files/gh-22-use-cheaper-subagent.md](./files/gh-22-use-cheaper-subagent.md)). |
| **Alternatives** | ask the Architect for the evidence bundle |
| **Materiality** | not material |
| **Status** | DELEGATED |

<a id="dd-5"></a>
## DD-5 — Done when: the §6 measurement is a follow-up (hypothesis)

|     | Info |
| --- | --- |
| **Phase** | FEATURE ANALYSIS PHASE |
| **When** | 2026-11-05 17:12 UTC |
| **Question** | Does acceptance include the §6 measurement on a next bundle? |
| **Interview question** | `01/4` |
| **Decision** | Decided under delegation (autonomous): record as hypothesis H-5 — the §6 measurement is a follow-up, not acceptance; Phase 04 settles acceptance. |
| **Basis** | Brief §6 "Run the next bundle with this change" — brief ([files/gh-22-use-cheaper-subagent.md](./files/gh-22-use-cheaper-subagent.md)); Phase 01 Step 2a: acceptance settles in Phase 04. |
| **Alternatives** | include the §6 measurement in acceptance |
| **Materiality** | not material |
| **Status** | DELEGATED |

<a id="dd-6"></a>
## DD-6 — 7/1 deferred to Phase 03

|     | Info |
| --- | --- |
| **Phase** | FEATURE ANALYSIS PHASE |
| **When** | 2026-11-05 17:12 UTC |
| **Question** | 7/1 — Do code searches share the phase's `model` tier, with no separate search key? |
| **Interview question** | `01/5` |
| **Decision** | Decided under delegation (autonomous): defer to Phase 03 as open item O-1; the brief's proposal "yes" is hypothesis H-4. |
| **Basis** | Brief §7 lists 7/1 as a decision "for the Architect" — brief ([files/gh-22-use-cheaper-subagent.md](./files/gh-22-use-cheaper-subagent.md)); ADR decisions belong to Phase 03. |
| **Alternatives** | answer 7/1 now |
| **Materiality** | not material |
| **Status** | DELEGATED |

<a id="dd-7"></a>
## DD-7 — Search-agent choice deferred to Phase 03

|     | Info |
| --- | --- |
| **Phase** | FEATURE ANALYSIS PHASE |
| **When** | 2026-11-05 17:12 UTC |
| **Question** | Which agent runs a code-search unit — `speccen-worker` or the host's built-in read-only search agent? |
| **Interview question** | `01/6` |
| **Decision** | Decided under delegation (autonomous): defer to Phase 03 as open item O-4; `speccen-worker` is hypothesis H-6; Phase 02 records how each agent takes a model. |
| **Basis** | Brief §2 A2 "The worker returns **findings only**" and the §1 table row "Explore code searches (Phase 02)" (count 4) — brief ([files/gh-22-use-cheaper-subagent.md](./files/gh-22-use-cheaper-subagent.md)). |
| **Alternatives** | decide `speccen-worker` now |
| **Materiality** | not material |
| **Status** | DELEGATED |

<a id="dd-8"></a>
## DD-8 — 7/3 deferred to Phase 03

|     | Info |
| --- | --- |
| **Phase** | FEATURE ANALYSIS PHASE |
| **When** | 2026-11-05 17:12 UTC |
| **Question** | 7/3 — Are the new keys brought to existing projects by raising the template to `version: 2`? |
| **Interview question** | `01/8` |
| **Decision** | Decided under delegation (autonomous): defer to Phase 03 as open item O-3; the brief's proposal "yes" is hypothesis H-4. |
| **Basis** | Brief §7 lists 7/3 as a decision "for the Architect" — brief ([files/gh-22-use-cheaper-subagent.md](./files/gh-22-use-cheaper-subagent.md)); the `version` facts are P02-2. |
| **Alternatives** | answer 7/3 now |
| **Materiality** | not material |
| **Status** | DELEGATED |

<a id="dd-9"></a>
## DD-9 — 7/2 deferred to Phase 03

|     | Info |
| --- | --- |
| **Phase** | FEATURE ANALYSIS PHASE |
| **When** | 2026-11-05 17:12 UTC |
| **Question** | 7/2 — Do Phase 03 code searches run on the phase's tier (`balanced`), not forced to `economy`? |
| **Interview question** | `01/9` |
| **Decision** | Decided under delegation (autonomous): defer to Phase 03 as open item O-2; the brief's proposal "yes" is hypothesis H-4. |
| **Basis** | Brief §7 7/2 "Follows from 7/1" — brief ([files/gh-22-use-cheaper-subagent.md](./files/gh-22-use-cheaper-subagent.md)). |
| **Alternatives** | answer 7/2 now |
| **Materiality** | not material |
| **Status** | DELEGATED |

---

**2026-11-05 18:12 UTC — DD-9 withdrawn.** Stop-round answer 01/10, Architect: "yes" (log 18:10).
01/9 was asked while its prerequisite 01/5 was "later"; it is held back and recorded as open item
O-2 for Phase 03, not decided. DD-9 stays in this file for the record.

<a id="dd-10"></a>
## DD-10 — Kind confirmed: refactoring

|     | Info |
| --- | --- |
| **Phase** | COMPLIANCE & REVIEW PHASE |
| **When** | 2026-11-05 19:15 UTC |
| **Question** | Confirm the kind of request (provisional since 01/1). |
| **Interview question** | `03/1` |
| **Decision** | Decided under delegation (autonomous): refactoring, confirmed. The change restructures how existing work is assigned to models and verified; no capability is added for the end user of the plugin. |
| **Basis** | Session-start Work kind answer "refactoring" (log.md, 17:03); DD-1. |
| **Alternatives** | feature |
| **Materiality** | not material |
| **Status** | DELEGATED |

<a id="dd-11"></a>
## DD-11 — Brief §2–§3 (Changes A and B) is the design basis

|     | Info |
| --- | --- |
| **Phase** | COMPLIANCE & REVIEW PHASE |
| **When** | 2026-11-05 19:15 UTC |
| **Question** | Are the brief's Changes A and B the intended design, with only the §7 questions open? |
| **Interview question** | `03/2` |
| **Decision** | Decided under delegation (autonomous): yes — A1–A6 and B1–B2 are the Architect's stated design; §7 and the questions found in Phase 02 are the open decisions. |
| **Basis** | Brief §2–§4, written by the Architect ([files/gh-22-use-cheaper-subagent.md](./files/gh-22-use-cheaper-subagent.md)); §7 names only three decisions "for the Architect". |
| **Alternatives** | treat A and B as options to decide one by one |
| **Materiality** | not material |
| **Status** | DELEGATED |

<a id="dd-12"></a>
## DD-12 — Restated sites S-1 – S-6 are in scope

|     | Info |
| --- | --- |
| **Phase** | COMPLIANCE & REVIEW PHASE |
| **When** | 2026-11-05 19:15 UTC |
| **Question** | Are the six restated sites found in Phase 02 in scope? |
| **Interview question** | `03/3` |
| **Decision** | Decided under delegation (autonomous): yes — S-1 – S-6 change in the same commit as their source; the v1 upgrade example lines are left to Phase 04. |
| **Basis** | Project convention confirmed in Phase 02 ([Coding Patterns & Style](./phase-02-code-analysis/phase.md#code-analysis): restated copies updated in the same commit, e.g. `47ce36a`, `999c03e`); [restated sites](./phase-02-code-analysis/phase.md#restated-sites). |
| **Alternatives** | keep the brief's Target list only |
| **Materiality** | not material |
| **Status** | DELEGATED |

<a id="dd-13"></a>
## DD-13 — 7/2: Phase 03 code searches run on Phase 03's tier

|     | Info |
| --- | --- |
| **Phase** | COMPLIANCE & REVIEW PHASE |
| **When** | 2026-11-05 19:18 UTC |
| **Question** | 7/2 — Do Phase 03 code searches run on the phase's tier (`balanced`), not forced to `economy`? |
| **Interview question** | `03/9` |
| **Decision** | Decided under delegation (autonomous): yes — with one shared tier per phase, Phase 03 searches take Phase 03's `model` (`balanced` in the template). |
| **Basis** | ADR [2026-11-05.code_search_tier](./adrs/2026-11-05.code_search_tier.md#decision) (03/4); brief §7 7/2 "Follows from 7/1" ([files/gh-22-use-cheaper-subagent.md](./files/gh-22-use-cheaper-subagent.md)). |
| **Alternatives** | force `economy` for Phase 03 searches (would need a separate key, which 03/4 rules out) |
| **Materiality** | not material |
| **Status** | DELEGATED |
