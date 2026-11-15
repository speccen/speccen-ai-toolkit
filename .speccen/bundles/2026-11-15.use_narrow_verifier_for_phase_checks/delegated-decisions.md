---
type: DelegatedDecisions
description: Decisions taken under delegation in autonomous mode — review, adopt or override
---

# use narrow verifier for phase checks — Delegated Decisions

[Index](./index.md) · [State](./STATE.md) · [Log](./log.md)

---

<a id="dd-1"></a>
## DD-1 — Kind of request: refactoring (provisional)

|     | Info |
| --- | --- |
| **Phase** | FEATURE ANALYSIS PHASE |
| **When** | 2026-11-15 20:15 UTC |
| **Question** | Record this as a refactoring, provisional until Phase 03? It changes how an existing check behaves, so it could also be read as a feature. |
| **Interview question** | [`01/1`](./phase-01-feature-analysis/phase.md#interview) |
| **Decision** | Decided under delegation (autonomous): refactoring, provisional until Phase 03 (H-1). |
| **Basis** | Session-start Work kind answer "refactoring" ([log.md](./log.md), 21:10). |
| **Alternatives** | feature |
| **Materiality** | not material |
| **Status** | DELEGATED |

<a id="dd-2"></a>
## DD-2 — Target: the plugin source in this repository at HEAD

|     | Info |
| --- | --- |
| **Phase** | FEATURE ANALYSIS PHASE |
| **When** | 2026-11-15 20:15 UTC |
| **Question** | Change the plugin source in this repository at HEAD, not the installed plugin cache? |
| **Interview question** | [`01/2`](./phase-01-feature-analysis/phase.md#interview) |
| **Decision** | Decided under delegation (autonomous): the repository source at HEAD; fact check P02-1 in Phase 02. |
| **Basis** | Brief, "Files to change", names repository paths (`skills/sdd/…`, `agents/speccen-worker.md`, `.claude-plugin/plugin.json`) ([log.md](./log.md), 21:14). |
| **Alternatives** | the installed plugin cache |
| **Materiality** | not material |
| **Status** | DELEGATED |

<a id="dd-3"></a>
## DD-3 — Evidence: the measured case is taken as stated

|     | Info |
| --- | --- |
| **Phase** | FEATURE ANALYSIS PHASE |
| **When** | 2026-11-15 20:15 UTC |
| **Question** | Take the measured case in the brief's Problem section as stated? |
| **Interview question** | [`01/3`](./phase-01-feature-analysis/phase.md#interview) |
| **Decision** | Decided under delegation (autonomous): accepted as the Architect's stated evidence. |
| **Basis** | Brief, Problem ([log.md](./log.md), 21:14). |
| **Alternatives** | ask for the source bundle of the measurement |
| **Materiality** | not material |
| **Status** | DELEGATED |

<a id="dd-4"></a>
## DD-4 — Self-check remit: items unchanged (working hypothesis)

|     | Info |
| --- | --- |
| **Phase** | FEATURE ANALYSIS PHASE |
| **When** | 2026-11-15 20:15 UTC |
| **Question** | Keep the self-check items unchanged (rule 12), so a bundle-internal row is covered by the self-check and the delegate's own evidence, with no new item for rule 1? |
| **Interview question** | [`01/4`](./phase-01-feature-analysis/phase.md#interview) |
| **Decision** | Decided under delegation (autonomous): recorded as working hypothesis H-5; settles in Phase 03 (O-2). Item count checked in Phase 02 (P02-2). |
| **Basis** | Brief rules 1, 11 and 12 ([log.md](./log.md), 21:14); decision `2026-11-05.self_check_interview_structure` (prior art). |
| **Alternatives** | a new self-check item covering the bundle-internal rows |
| **Materiality** | not material |
| **Status** | DELEGATED |

<a id="dd-5"></a>
## DD-5 — Later phases: only 01 – 05 need a claim source (working hypothesis)

|     | Info |
| --- | --- |
| **Phase** | FEATURE ANALYSIS PHASE |
| **When** | 2026-11-15 20:15 UTC |
| **Question** | Assume only Phases 01 – 05 need a claim source, as rule 5 lists? |
| **Interview question** | [`01/5`](./phase-01-feature-analysis/phase.md#interview) |
| **Decision** | Decided under delegation (autonomous): recorded as working hypothesis H-2; checked in Phase 02 (P02-3). |
| **Basis** | Brief rule 5 lists 01 – 05 ([log.md](./log.md), 21:14). |
| **Alternatives** | claim sources for 06 – 08 now |
| **Materiality** | not material |
| **Status** | DELEGATED |

<a id="dd-6"></a>
## DD-6 — Reach: every place that restates the verifier rule (working hypothesis)

|     | Info |
| --- | --- |
| **Phase** | FEATURE ANALYSIS PHASE |
| **When** | 2026-11-15 20:15 UTC |
| **Question** | Also bring into line every other place that restates the verifier rule, beyond the four listed files? |
| **Interview question** | [`01/6`](./phase-01-feature-analysis/phase.md#interview) |
| **Decision** | Decided under delegation (autonomous): recorded as working hypothesis H-3; places listed in Phase 02 (P02-4); scope settles in Phase 03 (O-2). |
| **Basis** | Brief, Acceptance: "No skill tells the verifier to check "every row" or "every quote"." ([log.md](./log.md), 21:14); lesson `2026-11-05.readme_restates_config_template`. |
| **Alternatives** | only the four listed files |
| **Materiality** | not material |
| **Status** | DELEGATED |

<a id="dd-7"></a>
## DD-7 — Claim-list place: the phase summary (working hypothesis)

|     | Info |
| --- | --- |
| **Phase** | FEATURE ANALYSIS PHASE |
| **When** | 2026-11-15 20:15 UTC |
| **Question** | Record the claim list in the phase `summary.md`, under `## Delegate gate check`, beside the gate table? |
| **Interview question** | [`01/7`](./phase-01-feature-analysis/phase.md#interview) |
| **Decision** | Decided under delegation (autonomous): recorded as working hypothesis H-4; settles in Phase 03 (O-2). |
| **Basis** | Brief rule 2 "At the gate the list already exists" ([log.md](./log.md), 21:14); the gate table lives in `summary.md` (governing skill, Gate test). |
| **Alternatives** | `phase.md`; a separate bundle file |
| **Materiality** | not material |
| **Status** | DELEGATED |

<a id="dd-8"></a>
## DD-8 — Done when: Acceptance plus the H-3 places (working hypothesis)

|     | Info |
| --- | --- |
| **Phase** | FEATURE ANALYSIS PHASE |
| **When** | 2026-11-15 20:15 UTC |
| **Question** | Is the request done when the brief's Acceptance list holds, extended to every place H-3 brings in? |
| **Interview question** | [`01/8`](./phase-01-feature-analysis/phase.md#interview) |
| **Decision** | Decided under delegation (autonomous): recorded as a working hypothesis; settles in Phase 04 (O-4). |
| **Basis** | Brief, Acceptance ([log.md](./log.md), 21:14); depends on 01/5 and 01/6. |
| **Alternatives** | the brief's Acceptance list alone |
| **Materiality** | not material |
| **Status** | DELEGATED |
