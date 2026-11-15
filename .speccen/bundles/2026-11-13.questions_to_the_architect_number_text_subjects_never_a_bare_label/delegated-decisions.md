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
| **Status** | ADOPTED — the Architect: "yes" (review round, log 2026-11-15 20:54) |

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
| **Status** | ADOPTED — the Architect: "yes" (review round, log 2026-11-15 20:54) |

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
| **Status** | ADOPTED — the Architect: "yes" (review round, log 2026-11-15 20:54) |

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
| **Status** | ADOPTED — the Architect: "yes" (review round, log 2026-11-15 20:54) |

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
| **Status** | ADOPTED — the Architect: "yes" (review round, log 2026-11-15 20:54) |

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
| **Status** | ADOPTED — the Architect: "yes" (review round, log 2026-11-15 20:54) |

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
| **Status** | ADOPTED — the Architect: "yes" (review round, log 2026-11-15 20:54) |

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
| **Status** | ADOPTED — the Architect: "yes" (review round, log 2026-11-15 20:54) |

<a id="dd-9"></a>
## DD-9 — Kind of request confirmed: feature

|     | Info |
| --- | --- |
| **Phase** | COMPLIANCE & REVIEW PHASE |
| **When** | 2026-11-13 06:13 UTC |
| **Question** | [03/1 \| Is the kind of request confirmed as a feature?] |
| **Interview question** | [`03/1`](./phase-03-compliance-review/phase.md#interview) |
| **Decision** | Decided under delegation (autonomous): yes — a feature. |
| **Basis** | Session-start Work kind "feature" ([log.md](./log.md), 06:28); nothing in Phases 01 – 02 contradicts it. |
| **Alternatives** | fix (the issue corrects behaviour the Architect objected to) |
| **Materiality** | not material |
| **Status** | ADOPTED — the Architect: "yes" (review round, log 2026-11-15 20:54) |

<a id="dd-10"></a>
## DD-10 — The rule is stated once and pointed to

|     | Info |
| --- | --- |
| **Phase** | COMPLIANCE & REVIEW PHASE |
| **When** | 2026-11-13 06:13 UTC |
| **Question** | [03/2 \| Is the rule stated once, in governing → Structured questions, and pointed to from each place, not repeated at each site?] |
| **Interview question** | [`03/2`](./phase-03-compliance-review/phase.md#interview) |
| **Decision** | Decided under delegation (autonomous): yes — the proposal of brief §5 decision 1 taken. |
| **Basis** | Brief §2 "One rule, stated once in the governing skill and pointed to from each place"; §5.1 "→ Proposed: yes"; Phase 02 convention "rule once, point from sites". §5 leaves the decision to the plugin Architect, so the basis does not decide it. |
| **Alternatives** | repeat the rule at each site |
| **Materiality** | MATERIAL — unconfirmed |
| **Status** | ADOPTED — the Architect: "yes" (review round, log 2026-11-15 20:54) |

<a id="dd-11"></a>
## DD-11 — Record tables stay outside the rule

|     | Info |
| --- | --- |
| **Phase** | COMPLIANCE & REVIEW PHASE |
| **When** | 2026-11-13 06:13 UTC |
| **Question** | [03/3 \| Does the rule cover only what is put to the Architect, leaving the record tables — gate check, delegated decisions, interview tables — unchanged?] |
| **Interview question** | [`03/3`](./phase-03-compliance-review/phase.md#interview) |
| **Decision** | Decided under delegation (autonomous): yes — the proposal of brief §5 decision 2 taken. |
| **Basis** | Brief §3 "Bundle-internal tables (gate check, delegated decisions, interview tables) are unchanged: they are records, not questions."; §5.2 "→ Proposed: yes". |
| **Alternatives** | subjects in the record tables too |
| **Materiality** | MATERIAL — unconfirmed |
| **Status** | ADOPTED — the Architect: "yes" (review round, log 2026-11-15 20:54) |

<a id="dd-12"></a>
## DD-12 — A sixth self-check item: Subjects

|     | Info |
| --- | --- |
| **Phase** | COMPLIANCE & REVIEW PHASE |
| **When** | 2026-11-13 06:13 UTC |
| **Question** | [03/4 \| Does the gate-test self-check get a sixth item, "Subjects"?] |
| **Interview question** | [`03/4`](./phase-03-compliance-review/phase.md#interview) |
| **Decision** | Decided under delegation (autonomous): yes — the proposal of brief §5 decision 3 taken; item 5 is kept as it is. |
| **Basis** | Brief §2.6 and §5.3 "→ Proposed: yes"; standing decision `2026-11-05.self_check_interview_structure`. |
| **Alternatives** | no self-check item; the rule alone |
| **Materiality** | MATERIAL — unconfirmed |
| **Status** | ADOPTED — the Architect: "yes" (review round, log 2026-11-15 20:54) |

<a id="dd-13"></a>
## DD-13 — The `stops: proceed` open item points to the rule

|     | Info |
| --- | --- |
| **Phase** | COMPLIANCE & REVIEW PHASE |
| **When** | 2026-11-13 06:13 UTC |
| **Question** | [03/5 \| Does the `stops: proceed` open item in `summary.md` point to the rule?] |
| **Interview question** | [`03/5`](./phase-03-compliance-review/phase.md#interview) |
| **Decision** | Decided under delegation (autonomous): yes — a pointer at the `stops: proceed` open item (Phase 02 inventory A-7). |
| **Basis** | Brief §2 rule "Anything put to the Architect reads on its own"; brief §1 "the record in `summary.md` still asked in labels"; Phase 02 inventory. |
| **Alternatives** | only the brief's five places; the rule's general wording alone for the rest |
| **Materiality** | MATERIAL — unconfirmed |
| **Repair** | 2026-11-13, Phase 03 iteration 2, under the narrowed stop condition 5 (03/16, Architect, log 07:32): the question held five places; split into one question per place with the same answer each — this entry keeps A-7; A-8, A-16, A-17, A-18 are DD-21 – DD-24. |
| **Status** | ADOPTED — the Architect: "yes" (review round, log 2026-11-15 20:54) |

<a id="dd-14"></a>
## DD-14 — The reconcile report's questions follow the rule

|     | Info |
| --- | --- |
| **Phase** | COMPLIANCE & REVIEW PHASE |
| **When** | 2026-11-13 06:13 UTC |
| **Question** | [03/6 \| Is the reconcile report's "Needs human resolution" list covered by the rule, as questions put to a human?] |
| **Interview question** | [`03/6`](./phase-03-compliance-review/phase.md#interview) |
| **Decision** | Decided under delegation (autonomous): yes — a pointer in `skills/sdd/reconcile/SKILL.md` at the "Needs human resolution" template. |
| **Basis** | Brief §2 rule "Anything put to the Architect"; the list ends in "Decide:" (`skills/sdd/reconcile/SKILL.md:159`). |
| **Alternatives** | leave reconcile out: it is not a phase and its ids are readable slugs |
| **Materiality** | MATERIAL — unconfirmed |
| **Status** | ADOPTED — the Architect: "yes" (review round, log 2026-11-15 20:54) |

<a id="dd-15"></a>
## DD-15 — Retrospective findings stay outside

|     | Info |
| --- | --- |
| **Phase** | COMPLIANCE & REVIEW PHASE |
| **When** | 2026-11-13 06:13 UTC |
| **Question** | [03/7 \| Do the Retrospective's delegation findings stay outside the rule, as a record?] |
| **Interview question** | [`03/7`](./phase-03-compliance-review/phase.md#interview) |
| **Decision** | Decided under delegation (autonomous): yes — a record (Phase 02 inventory A-15). |
| **Basis** | 03/3; brief §3 "they are records, not questions". |
| **Alternatives** | cover them: the Architect reads both |
| **Materiality** | MATERIAL — unconfirmed |
| **Repair** | 2026-11-13, Phase 03 iteration 2, under the narrowed stop condition 5 (03/16, Architect, log 07:32): the question held two records; split with the same answer each — the fix-attempt log line is DD-25. |
| **Status** | ADOPTED — the Architect: "yes" (review round, log 2026-11-15 20:54) |

<a id="dd-16"></a>
## DD-16 — `AskUserQuestion`: question text covered, header exempt

|     | Info |
| --- | --- |
| **Phase** | COMPLIANCE & REVIEW PHASE |
| **When** | 2026-11-13 06:13 UTC |
| **Question** | [03/8 \| In an `AskUserQuestion` call, does the rule cover the question text that names an item, with the 12-character header exempt?] |
| **Interview question** | [`03/8`](./phase-03-compliance-review/phase.md#interview) |
| **Decision** | Decided under delegation (autonomous): yes. |
| **Basis** | Brief §2 rule "Anything put to the Architect"; governing "**Headers ≤ 12 characters** (they are the tab labels)" (`skills/sdd/00-governing-workflow/SKILL.md:382`); no call names an item today (Phase 02, P02-4). |
| **Alternatives** | exempt the tool entirely |
| **Materiality** | MATERIAL — unconfirmed |
| **Repair** | 2026-11-13, Phase 03 iteration 2, under the narrowed stop condition 5 (03/16, Architect, log 07:32): moved to round 1 (it does not depend on 03/2); working hypothesis H-3 removed from the basis — a hypothesis is not a basis source. |
| **Status** | ADOPTED — the Architect: "yes" (review round, log 2026-11-15 20:54) |

<a id="dd-17"></a>
## DD-17 — Audit and code interviews inherit the rule

|     | Info |
| --- | --- |
| **Phase** | COMPLIANCE & REVIEW PHASE |
| **When** | 2026-11-13 06:13 UTC |
| **Question** | [03/9 \| Do the audit and code-documentation interviews follow the rule through the shared round template, with no pointer of their own?] |
| **Interview question** | [`03/9`](./phase-03-compliance-review/phase.md#interview) |
| **Decision** | Decided under delegation (autonomous): yes. |
| **Basis** | Interview skill, "Outside a bundle": "everything else (frontier, round format, answers that are not a choice, closing question) applies unchanged" (`skills/sdd/interview/SKILL.md:39-42`). |
| **Alternatives** | a pointer in each audit and code skill |
| **Materiality** | MATERIAL — unconfirmed |
| **Status** | ADOPTED — the Architect: "yes" (review round, log 2026-11-15 20:54) |

<a id="dd-18"></a>
## DD-18 — The rule goes at the end of Structured questions

|     | Info |
| --- | --- |
| **Phase** | COMPLIANCE & REVIEW PHASE |
| **When** | 2026-11-13 06:13 UTC |
| **Question** | [03/10 \| Does the rule go at the end of governing → Structured questions, after the paragraph "A series of decisions"?] |
| **Interview question** | [`03/10`](./phase-03-compliance-review/phase.md#interview) |
| **Decision** | Decided under delegation (autonomous): yes. |
| **Basis** | Brief §2.1 places it in Structured questions; the section's last paragraph introduces the interview (`skills/sdd/00-governing-workflow/SKILL.md:395-401`), and the rule governs both the tool and the interview. |
| **Alternatives** | after the tool's constraints (`:377-384`) |
| **Materiality** | not material |
| **Status** | ADOPTED — the Architect: "yes" (review round, log 2026-11-15 20:54) |

<a id="dd-19"></a>
## DD-19 — `README.md` mentions the subject form; `ARCHITECTURE.md` unchanged

|     | Info |
| --- | --- |
| **Phase** | COMPLIANCE & REVIEW PHASE |
| **When** | 2026-11-13 06:13 UTC |
| **Question** | [03/11 \| Does `README.md` mention the subject form in its autonomous-mode section, with `ARCHITECTURE.md` unchanged?] |
| **Interview question** | [`03/11`](./phase-03-compliance-review/phase.md#replaced-questions) (replaced; see 03/14, 03/15) |
| **Decision** | Decided under delegation (autonomous): yes. |
| **Basis** | `README.md:217-231` describes the stop round and the review round to the Architect; `ARCHITECTURE.md:76-81` describes the skill, not the message; lesson `2026-11-05.readme_restates_config_template`. |
| **Alternatives** | mention it in both; in neither |
| **Materiality** | MATERIAL — unconfirmed |
| **Repair** | 2026-11-13, Phase 03 iteration 2, under the narrowed stop condition 5 (03/16, Architect, log 07:32): the question held two decisions; replaced by DD-26 (`README.md`, raised to `MATERIAL — unconfirmed`) and DD-27 (`ARCHITECTURE.md`). The lesson cited in the basis is not a basis source; DD-26 and DD-27 do not rely on it. This entry stays as recorded. |
| **Repair** | 2026-11-15, Phase 03, after the second stop (03/22, Architect, log 20:08): materiality raised from `not material` to `MATERIAL — unconfirmed`, as for DD-26, which holds the same README decision. The answer is unchanged. |
| **Status** | ADOPTED — the Architect: "yes" (review round, log 2026-11-15 20:54) |

<a id="dd-20"></a>
## DD-20 — The label list adds `<skill>/<n>` and `Deviation [N]`

|     | Info |
| --- | --- |
| **Phase** | COMPLIANCE & REVIEW PHASE |
| **When** | 2026-11-13 06:13 UTC |
| **Question** | [03/12 \| Does the rule's list of label kinds add `<skill>/<n>` and `Deviation [N]` to the brief's list?] |
| **Interview question** | [`03/12`](./phase-03-compliance-review/phase.md#interview) |
| **Decision** | Decided under delegation (autonomous): yes. |
| **Basis** | `skills/sdd/interview/SKILL.md:45-46`, `skills/sdd/05-implementation/SKILL.md:225` (Phase 02, P02-3); brief §2.1's list exists to say which numbers keep an item traceable. |
| **Alternatives** | keep the brief's list as written |
| **Materiality** | not material |
| **Repair** | 2026-11-13, Phase 03 iteration 2, under the narrowed stop condition 5 (03/16, Architect, log 07:32): moved to round 1 (it does not depend on 03/2). |
| **Status** | ADOPTED — the Architect: "yes" (review round, log 2026-11-15 20:54) |

<a id="dd-21"></a>
## DD-21 — The resume summary points to the rule

|     | Info |
| --- | --- |
| **Phase** | COMPLIANCE & REVIEW PHASE |
| **When** | 2026-11-13 06:35 UTC |
| **Question** | [03/17 \| Does the resume summary point to the rule?] |
| **Interview question** | [`03/17`](./phase-03-compliance-review/phase.md#interview) |
| **Decision** | Decided under delegation (autonomous): yes — a pointer at the resume summary (Phase 02 inventory A-8). |
| **Basis** | Brief §2 rule "Anything put to the Architect reads on its own". |
| **Alternatives** | the rule's general wording alone |
| **Materiality** | MATERIAL — unconfirmed |
| **Repair** | 2026-11-13, Phase 03 iteration 2, under the narrowed stop condition 5 (03/16, Architect, log 07:32): split from DD-13 (03/5), same answer. |
| **Status** | ADOPTED — the Architect: "yes" (review round, log 2026-11-15 20:54) |

<a id="dd-22"></a>
## DD-22 — The interview's closing summary points to the rule

|     | Info |
| --- | --- |
| **Phase** | COMPLIANCE & REVIEW PHASE |
| **When** | 2026-11-13 06:35 UTC |
| **Question** | [03/18 \| Does the interview's closing summary point to the rule?] |
| **Interview question** | [`03/18`](./phase-03-compliance-review/phase.md#interview) |
| **Decision** | Decided under delegation (autonomous): yes — a pointer at the closing summary (Phase 02 inventory A-16). |
| **Basis** | Brief §2 rule "Anything put to the Architect reads on its own". |
| **Alternatives** | the rule's general wording alone |
| **Materiality** | MATERIAL — unconfirmed |
| **Repair** | 2026-11-13, Phase 03 iteration 2, under the narrowed stop condition 5 (03/16, Architect, log 07:32): split from DD-13 (03/5), same answer. |
| **Status** | ADOPTED — the Architect: "yes" (review round, log 2026-11-15 20:54) |

<a id="dd-23"></a>
## DD-23 — The Phase 05 completion notice points to the rule

|     | Info |
| --- | --- |
| **Phase** | COMPLIANCE & REVIEW PHASE |
| **When** | 2026-11-13 06:35 UTC |
| **Question** | [03/19 \| Does the Phase 05 completion notice point to the rule?] |
| **Interview question** | [`03/19`](./phase-03-compliance-review/phase.md#interview) |
| **Decision** | Decided under delegation (autonomous): yes — a pointer at the completion notice (Phase 02 inventory A-17). |
| **Basis** | Brief §2 rule "Anything put to the Architect reads on its own". |
| **Alternatives** | the rule's general wording alone |
| **Materiality** | MATERIAL — unconfirmed |
| **Repair** | 2026-11-13, Phase 03 iteration 2, under the narrowed stop condition 5 (03/16, Architect, log 07:32): split from DD-13 (03/5), same answer. |
| **Status** | ADOPTED — the Architect: "yes" (review round, log 2026-11-15 20:54) |

<a id="dd-24"></a>
## DD-24 — The `STATE.md` stop line points to the rule

|     | Info |
| --- | --- |
| **Phase** | COMPLIANCE & REVIEW PHASE |
| **When** | 2026-11-13 06:35 UTC |
| **Question** | [03/20 \| Does the `STATE.md` stop line point to the rule?] |
| **Interview question** | [`03/20`](./phase-03-compliance-review/phase.md#interview) |
| **Decision** | Decided under delegation (autonomous): yes — a pointer at the stop line (Phase 02 inventory A-18). |
| **Basis** | Brief §2 rule "Anything put to the Architect reads on its own". |
| **Alternatives** | the rule's general wording alone |
| **Materiality** | MATERIAL — unconfirmed |
| **Repair** | 2026-11-13, Phase 03 iteration 2, under the narrowed stop condition 5 (03/16, Architect, log 07:32): split from DD-13 (03/5), same answer. |
| **Status** | ADOPTED — the Architect: "yes" (review round, log 2026-11-15 20:54) |

<a id="dd-25"></a>
## DD-25 — The fix-attempt log line stays outside

|     | Info |
| --- | --- |
| **Phase** | COMPLIANCE & REVIEW PHASE |
| **When** | 2026-11-13 06:35 UTC |
| **Question** | [03/21 \| Does the fix-attempt log line stay outside the rule, as a record?] |
| **Interview question** | [`03/21`](./phase-03-compliance-review/phase.md#interview) |
| **Decision** | Decided under delegation (autonomous): yes — a record (Phase 02 inventory A-20). |
| **Basis** | 03/3; brief §3 "they are records, not questions". |
| **Alternatives** | cover it: the Architect reads the log |
| **Materiality** | MATERIAL — unconfirmed |
| **Repair** | 2026-11-13, Phase 03 iteration 2, under the narrowed stop condition 5 (03/16, Architect, log 07:32): split from DD-15 (03/7), same answer. |
| **Status** | ADOPTED — the Architect: "yes" (review round, log 2026-11-15 20:54) |

<a id="dd-26"></a>
## DD-26 — `README.md` mentions the subject form

|     | Info |
| --- | --- |
| **Phase** | COMPLIANCE & REVIEW PHASE |
| **When** | 2026-11-13 06:35 UTC |
| **Question** | [03/14 \| Should `README.md` mention the subject form in its autonomous-mode section, where it describes the stop round and the review round?] |
| **Interview question** | [`03/14`](./phase-03-compliance-review/phase.md#interview) |
| **Decision** | Decided under delegation (autonomous): yes. |
| **Basis** | Brief §2 rule "Anything put to the Architect reads on its own"; `README.md:217-231` describes the stop round and the review round to the Architect. The brief does not decide it. |
| **Alternatives** | leave `README.md` as it is |
| **Materiality** | MATERIAL — unconfirmed |
| **Repair** | 2026-11-13, Phase 03 iteration 2, under the narrowed stop condition 5 (03/16, Architect, log 07:32): replaces the README half of DD-19 (03/11); materiality raised from `not material`. |
| **Status** | ADOPTED — the Architect: "yes" (review round, log 2026-11-15 20:54) |

<a id="dd-27"></a>
## DD-27 — `ARCHITECTURE.md` stays unchanged

|     | Info |
| --- | --- |
| **Phase** | COMPLIANCE & REVIEW PHASE |
| **When** | 2026-11-13 06:35 UTC |
| **Question** | [03/15 \| Should `ARCHITECTURE.md` stay unchanged?] |
| **Interview question** | [`03/15`](./phase-03-compliance-review/phase.md#interview) |
| **Decision** | Decided under delegation (autonomous): yes. |
| **Basis** | `ARCHITECTURE.md:76-81` describes the interview skill, not the messages (Phase 02, P02-5). |
| **Alternatives** | mention the subject form there too |
| **Materiality** | not material |
| **Repair** | 2026-11-13, Phase 03 iteration 2, under the narrowed stop condition 5 (03/16, Architect, log 07:32): replaces the `ARCHITECTURE.md` half of DD-19 (03/11). |
| **Status** | ADOPTED — the Architect: "yes" (review round, log 2026-11-15 20:54) |

<a id="dd-28"></a>
## DD-28 — Skill-text changes stay uncommitted for the Architect

|     | Info |
| --- | --- |
| **Phase** | SPECIFICATION PHASE |
| **When** | 2026-11-15 19:20 UTC |
| **Question** | [04/1 \| Are the skill-text changes left uncommitted in the working tree for the Architect, with only the bundle files committed at each phase transition?] |
| **Interview question** | [`04/1`](./phase-04-specification/phase.md#interview) |
| **Decision** | Decided under delegation (autonomous): yes. |
| **Basis** | Phase Transition Protocol: a transition commits "the changed bundle files — only those"; precedent: bundle `2026-11-12.set_allowed_budget_for_autonomous_phases`, its question 04/1 (its DD-24). |
| **Alternatives** | commit the skill changes with the Phase 05 transition |
| **Materiality** | not material |
| **Status** | ADOPTED — the Architect: "yes" (review round, log 2026-11-15 20:54) |
