---
type: DelegatedDecisions
description: Decisions taken under delegation in autonomous mode — review, adopt or override
---

# Questions to the Architect: [number | text] subjects, never a bare label — Delegated Decisions

[Index](./index.md) · [State](./STATE.md) · [Log](./log.md)

---

<a id="dd-1"></a>
## DD-1 — Issue #26 counts as the Architect's own words

|     | Info |
| --- | --- |
| **Phase** | FEATURE ANALYSIS PHASE |
| **When** | 2026-11-13 05:31 UTC |
| **Question** | [01/1 \| Does issue #26, which the Architect wrote, count as the Architect's own words for this bundle?] |
| **Interview question** | [`01/1`](./phase-01-feature-analysis/phase.md#interview) |
| **Decision** | Decided under delegation (autonomous): yes. The brief is stored in [files/gh-26-questions-subjects.md](./files/gh-26-questions-subjects.md) and referenced from `log.md` (06:30). |
| **Basis** | The Architect's "yes" to the same question for issue #25 (bundle `2026-11-12.set_allowed_budget_for_autonomous_phases`, `log.md` 2026-11-11 11:52, its 01/9); session-start Name "Use issue #26 title" ([log.md](./log.md), 06:28). |
| **Alternatives** | Treat only the chat prompts as the Architect's words, and the issue as background. |
| **Materiality** | not material |
| **Status** | DELEGATED |

<a id="dd-2"></a>
## DD-2 — Target: the plugin source in this repository

|     | Info |
| --- | --- |
| **Phase** | FEATURE ANALYSIS PHASE |
| **When** | 2026-11-13 05:31 UTC |
| **Question** | [01/2 \| Is the text to change the plugin source in this repository, not the installed plugin copy?] |
| **Interview question** | [`01/2`](./phase-01-feature-analysis/phase.md#interview) |
| **Decision** | Decided under delegation (autonomous): the plugin source in this repository. |
| **Basis** | Brief §1 and §2 cite repository paths and line numbers; the session runs in this repository. |
| **Alternatives** | The installed plugin cache. |
| **Materiality** | not material |
| **Status** | DELEGATED |

<a id="dd-3"></a>
## DD-3 — The rule's reach: every place, as a working hypothesis

|     | Info |
| --- | --- |
| **Phase** | FEATURE ANALYSIS PHASE |
| **When** | 2026-11-13 05:31 UTC |
| **Question** | [01/3 \| Is the working hypothesis that the rule reaches every place that puts something to the Architect, not only the five places §2 changes?] |
| **Interview question** | [`01/3`](./phase-01-feature-analysis/phase.md#interview) |
| **Decision** | Decided under delegation (autonomous): recorded as working hypothesis H-1 — every place; not decided in Phase 01. Phase 02 makes the inventory (P02-1); Phase 03 decides (O-1). |
| **Basis** | Brief §2: the rule text says "Anything put to the Architect reads on its own"; Phase 01 skill, Mode behaviour: an open question that Phase 02 can investigate becomes a working hypothesis. |
| **Alternatives** | Only the five places the brief's diffs change. |
| **Materiality** | not material (the material choice is left to Phase 03) |
| **Status** | DELEGATED |

<a id="dd-4"></a>
## DD-4 — The §5 proposals are the starting proposal for Phase 03

|     | Info |
| --- | --- |
| **Phase** | FEATURE ANALYSIS PHASE |
| **When** | 2026-11-13 05:31 UTC |
| **Question** | [01/4 \| Are the three §5 proposals the starting proposal for Phase 03?] |
| **Interview question** | [`01/4`](./phase-01-feature-analysis/phase.md#interview) |
| **Decision** | Decided under delegation (autonomous): recorded as working hypothesis H-2; Phase 03 decides each (O-2). |
| **Basis** | Brief §5 "Decisions for the plugin Architect", each "→ Proposed: yes". |
| **Alternatives** | Decide them in Phase 01. |
| **Materiality** | not material (the decisions are left to Phase 03) |
| **Status** | DELEGATED |

<a id="dd-5"></a>
## DD-5 — Earlier bundles and the durable store are not rewritten

|     | Info |
| --- | --- |
| **Phase** | FEATURE ANALYSIS PHASE |
| **When** | 2026-11-13 05:31 UTC |
| **Question** | [01/5 \| Are earlier bundles and durable-store entries left as they are, without rewriting their labels?] |
| **Interview question** | [`01/5`](./phase-01-feature-analysis/phase.md#interview) |
| **Decision** | Decided under delegation (autonomous): yes — out of scope. |
| **Basis** | Brief §2 changes only skill text; brief §3 "Traceability is unchanged: every number stays, inside its subject." |
| **Alternatives** | Rewrite the subjects in earlier bundles and store entries. |
| **Materiality** | not material |
| **Status** | DELEGATED |

<a id="dd-6"></a>
## DD-6 — This bundle already uses the subject form

|     | Info |
| --- | --- |
| **Phase** | FEATURE ANALYSIS PHASE |
| **When** | 2026-11-13 05:31 UTC |
| **Question** | [01/6 \| Should this bundle already write what it puts to the Architect in the `[number \| text]` form?] |
| **Interview question** | [`01/6`](./phase-01-feature-analysis/phase.md#interview) |
| **Decision** | Decided under delegation (autonomous): yes. |
| **Basis** | Brief §1: the Architect set the format "[INTERNAL-NUMBER \| HUMAN UNDERSTANDABLE TEXT]". Presentation only. |
| **Alternatives** | Keep the current skill format until the change is implemented. |
| **Materiality** | not material |
| **Status** | DELEGATED |

<a id="dd-7"></a>
## DD-7 — `AskUserQuestion`: question text covered, headers exempt, as a working hypothesis

|     | Info |
| --- | --- |
| **Phase** | FEATURE ANALYSIS PHASE |
| **When** | 2026-11-13 05:31 UTC |
| **Question** | [01/7 \| Is the working hypothesis that, in an `AskUserQuestion` call, the rule covers the question text that names an item and exempts the header?] |
| **Interview question** | [`01/7`](./phase-01-feature-analysis/phase.md#interview) |
| **Decision** | Decided under delegation (autonomous): recorded as working hypothesis H-3 — the question text that names an item is covered; the header (12 characters at most) is exempt. Phase 02 checks how the skills use the tool (P02-4); Phase 03 decides (O-3). |
| **Basis** | Brief §2 rule "Anything put to the Architect"; governing skill → Structured questions: "Headers ≤ 12 characters". |
| **Alternatives** | Exempt `AskUserQuestion` entirely; require the subject in the header. |
| **Materiality** | not material (the decision is left to Phase 03) |
| **Status** | DELEGATED |

<a id="dd-8"></a>
## DD-8 — Done when, as a working hypothesis

|     | Info |
| --- | --- |
| **Phase** | FEATURE ANALYSIS PHASE |
| **When** | 2026-11-13 05:31 UTC |
| **Question** | [01/8 \| Is this done when the §2 changes are in the skills, every place Phase 02 finds follows or points to the rule, and record tables are unchanged?] |
| **Interview question** | [`01/8`](./phase-01-feature-analysis/phase.md#interview) |
| **Decision** | Decided under delegation (autonomous): recorded as working hypothesis H-4; Phase 04 settles the acceptance (O-4). |
| **Basis** | Brief §2 (the six changes) and §3 (Effect). |
| **Alternatives** | Done when only the six §2 changes are in. |
| **Materiality** | not material (acceptance is left to Phase 04) |
| **Status** | DELEGATED |
