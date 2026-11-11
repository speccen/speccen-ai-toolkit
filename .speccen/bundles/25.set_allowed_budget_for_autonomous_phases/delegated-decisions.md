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
