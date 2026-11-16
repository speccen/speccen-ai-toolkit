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

<a id="dd-9"></a>
## DD-9 — Kind of request: refactoring (confirmed)

|     | Info |
| --- | --- |
| **Phase** | COMPLIANCE & REVIEW PHASE |
| **When** | 2026-11-15 20:35 UTC |
| **Question** | Confirm the kind as refactoring (H-1)? |
| **Interview question** | [`03/1`](./phase-03-compliance-review/phase.md#interview) |
| **Decision** | Decided under delegation (autonomous): refactoring, confirmed. |
| **Basis** | Session-start Work kind "refactoring" ([log.md](./log.md), 21:10); the brief's "Files to change" lists only existing files and no config key. |
| **Alternatives** | feature |
| **Materiality** | not material |
| **Status** | DELEGATED |

<a id="dd-10"></a>
## DD-10 — Version bump by hand, as the brief says

|     | Info |
| --- | --- |
| **Phase** | COMPLIANCE & REVIEW PHASE |
| **When** | 2026-11-15 20:35 UTC |
| **Question** | Follow the brief's item 4 and bump `plugin.json` and `marketplace.json` by hand, although CI bumps on every push to `main`? |
| **Interview question** | [`03/2`](./phase-03-compliance-review/phase.md#interview) |
| **Decision** | Decided under delegation (autonomous): bump by hand to the next `YY.MDD.N`; the CI double bump is put to the Architect in the review round. |
| **Basis** | Brief: "Bump the version in `.claude-plugin/plugin.json` and `marketplace.json`." ([log.md](./log.md), 21:14) — ranks above the convention observed in Phase 02 (`.github/workflows/bump-version.yml`). |
| **Alternatives** | leave the bump to CI |
| **Materiality** | not material |
| **Status** | DELEGATED |

<a id="dd-11"></a>
## DD-11 — After-a-stop paragraph restated in claims

|     | Info |
| --- | --- |
| **Phase** | COMPLIANCE & REVIEW PHASE |
| **When** | 2026-11-15 20:35 UTC |
| **Question** | Restate the after-a-stop paragraph (governing 1235 – 1238) in claims? |
| **Interview question** | [`03/3`](./phase-03-compliance-review/phase.md#interview) |
| **Decision** | Decided under delegation (autonomous): restate it: the Architect's answer sets which claims the next run re-checks; the verifier reports on every listed claim. |
| **Basis** | Brief rule 10 and Acceptance "the `n/a` case and the later-runs rule" ([log.md](./log.md), 21:14); Phase 02 C-2. |
| **Alternatives** | leave it in rows |
| **Materiality** | not material |
| **Status** | DELEGATED |

<a id="dd-12"></a>
## DD-12 — Phase 07 spot-check unchanged

|     | Info |
| --- | --- |
| **Phase** | COMPLIANCE & REVIEW PHASE |
| **When** | 2026-11-15 20:35 UTC |
| **Question** | Leave Phase 07's gate-row spot-check unchanged? |
| **Interview question** | [`03/4`](./phase-03-compliance-review/phase.md#interview) |
| **Decision** | Decided under delegation (autonomous): unchanged. |
| **Basis** | Brief "Files to change" lists no Phase 07 edit ([log.md](./log.md), 21:14); 07: 134 – 136 does not describe the verifier (Phase 02 C-2). |
| **Alternatives** | add the new `verified` values to Phase 07 |
| **Materiality** | not material |
| **Status** | DELEGATED |

<a id="dd-13"></a>
## DD-13 — README and ARCHITECTURE unchanged

|     | Info |
| --- | --- |
| **Phase** | COMPLIANCE & REVIEW PHASE |
| **When** | 2026-11-15 20:35 UTC |
| **Question** | Leave README and ARCHITECTURE unchanged? |
| **Interview question** | [`03/5`](./phase-03-compliance-review/phase.md#interview) |
| **Decision** | Decided under delegation (autonomous): unchanged. |
| **Basis** | Brief rule 12 (the verifier stays on the session model) ([log.md](./log.md), 21:14); Phase 02 architecture table (README 269, 343; ARCHITECTURE 158). |
| **Alternatives** | describe the narrow verifier in README |
| **Materiality** | not material |
| **Status** | DELEGATED |

<a id="dd-14"></a>
## DD-14 — Claim list in the phase summary, under the gate table

|     | Info |
| --- | --- |
| **Phase** | COMPLIANCE & REVIEW PHASE |
| **When** | 2026-11-15 20:35 UTC |
| **Question** | Record the claims in `summary.md` under `## Delegate gate check`, as a `Claims` list directly under the gate table? |
| **Interview question** | [`03/6`](./phase-03-compliance-review/phase.md#interview) |
| **Decision** | Decided under delegation (autonomous): as proposed. Split by fix attempt 1: the claim-line form moved to 03/12 (DD-20); by fix attempt 2 the result moved to 03/13 (DD-21). The answer on the place is unchanged. |
| **Basis** | Brief rule 2 ([log.md](./log.md), 21:14); the gate table lives in `summary.md` (governing skill, Gate test). |
| **Alternatives** | `phase.md`; a separate bundle file; claims inside the gate-table evidence cell |
| **Materiality** | MATERIAL — unconfirmed |
| **Status** | DELEGATED |

<a id="dd-15"></a>
## DD-15 — Self-check items unchanged; rule 1 as an ownership split

|     | Info |
| --- | --- |
| **Phase** | COMPLIANCE & REVIEW PHASE |
| **When** | 2026-11-15 20:35 UTC |
| **Question** | Keep the six self-check items unchanged and state rule 1 as an ownership split, not a new item? |
| **Interview question** | [`03/7`](./phase-03-compliance-review/phase.md#interview) |
| **Decision** | Decided under delegation (autonomous): as proposed. |
| **Basis** | Brief rules 1 and 12 ([log.md](./log.md), 21:14); standing decision `2026-11-05.self_check_interview_structure`. |
| **Alternatives** | a new self-check item covering bundle-internal rows |
| **Materiality** | not material |
| **Status** | DELEGATED |

<a id="dd-16"></a>
## DD-16 — Stop trigger 3 kept as written

|     | Info |
| --- | --- |
| **Phase** | COMPLIANCE & REVIEW PHASE |
| **When** | 2026-11-15 20:35 UTC |
| **Question** | Keep stop trigger 3 as written, with a failed row meaning a row with a `wrong` claim? |
| **Interview question** | [`03/8`](./phase-03-compliance-review/phase.md#interview) |
| **Decision** | Decided under delegation (autonomous): as proposed. |
| **Basis** | Brief rules 7, 11 and 12 ([log.md](./log.md), 21:14); standing decision `2026-11-11.fix_progress_by_breaches`. |
| **Alternatives** | restate the trigger in claims |
| **Materiality** | not material |
| **Status** | DELEGATED |

<a id="dd-17"></a>
## DD-17 — Verifier template beside the generic one

|     | Info |
| --- | --- |
| **Phase** | COMPLIANCE & REVIEW PHASE |
| **When** | 2026-11-15 20:35 UTC |
| **Question** | Keep the generic work-order template and add the verifier template as a second block directly after it? |
| **Interview question** | [`03/9`](./phase-03-compliance-review/phase.md#interview) |
| **Decision** | Decided under delegation (autonomous): as proposed. |
| **Basis** | Brief, "Files to change" item 1, which puts "the template above" under Subagent Execution → The worker and the work order ([log.md](./log.md), 21:14); precedent: the Search unit's own fields. |
| **Alternatives** | replace the generic template; put the template in Gate test |
| **Materiality** | not material |
| **Status** | DELEGATED |

<a id="dd-18"></a>
## DD-18 — `noticed:` answers as extra gate-table rows

|     | Info |
| --- | --- |
| **Phase** | COMPLIANCE & REVIEW PHASE |
| **When** | 2026-11-15 20:35 UTC |
| **Question** | Answer each `noticed:` line as one extra row at the foot of the gate table? |
| **Interview question** | [`03/10`](./phase-03-compliance-review/phase.md#interview) |
| **Decision** | Decided under delegation (autonomous): as proposed: `noticed-<n> \| <the line> \| corrected / not relevant, because … \| <evidence> \| —`. |
| **Basis** | Brief rule 8 "The delegate answers each one in the gate table" ([log.md](./log.md), 21:14). |
| **Alternatives** | a separate list under the table |
| **Materiality** | not material |
| **Status** | DELEGATED |

<a id="dd-19"></a>
## DD-19 — Done when: Acceptance plus the Phase 03 decisions

|     | Info |
| --- | --- |
| **Phase** | COMPLIANCE & REVIEW PHASE |
| **When** | 2026-11-15 20:35 UTC |
| **Question** | Is the request done when the brief's Acceptance holds plus 03/2, 03/3, 03/6, 03/9, 03/10, 03/12 and 03/13? |
| **Interview question** | [`03/11`](./phase-03-compliance-review/phase.md#interview) |
| **Decision** | Decided under delegation (autonomous): as proposed; Phase 04 turns it into scenarios. Fix attempt 2 named 03/12 and 03/13, which 03/6 covered before the split; the scope is unchanged (a recording repair). |
| **Basis** | Brief, Acceptance ([log.md](./log.md), 21:14); 03/2, 03/3, 03/6, 03/9, 03/10, 03/12, 03/13. |
| **Alternatives** | the brief's Acceptance alone |
| **Materiality** | not material |
| **Status** | DELEGATED |

<a id="dd-20"></a>
## DD-20 — Claim-line form: brief form with `K-<n> (row <N>)` ids

|     | Info |
| --- | --- |
| **Phase** | COMPLIANCE & REVIEW PHASE |
| **When** | 2026-11-15 20:39 UTC |
| **Question** | Write each claim as `id · claim · how to check · expected`, with the id `K-<n> (row <N>)`? |
| **Interview question** | [`03/12`](./phase-03-compliance-review/phase.md#interview) |
| **Decision** | Decided under delegation (autonomous): as proposed. Split out of 03/6 by fix attempt 1 (a recording repair: one question per decision); fix attempt 2 moved the result placement to 03/13 (DD-21). |
| **Basis** | Brief rules 3 and 11 ([log.md](./log.md), 21:14). |
| **Alternatives** | `C-<n>` ids (taken by Phase 02 open items); a row column in a claims table |
| **Materiality** | MATERIAL — unconfirmed |
| **Status** | DELEGATED |

<a id="dd-21"></a>
## DD-21 — Claim result appended to its line

|     | Info |
| --- | --- |
| **Phase** | COMPLIANCE & REVIEW PHASE |
| **When** | 2026-11-16 05:12 UTC |
| **Question** | Append each claim's run result to its own line, after `→` (`confirmed (run N)`, `slip — <correct value>`, `wrong — <actual value>`)? |
| **Interview question** | [`03/13`](./phase-03-compliance-review/phase.md#interview) |
| **Decision** | Decided under delegation (autonomous): as proposed. Split out of 03/12 by fix attempt 2 (a recording repair: one question per decision). |
| **Basis** | Brief rules 7 and 11 ([log.md](./log.md), 21:14). |
| **Alternatives** | a result column in a claims table; results only in the gate table's `verified` cell |
| **Materiality** | MATERIAL — unconfirmed |
| **Status** | DELEGATED |

<a id="dd-22"></a>
## DD-22 — Test approach: a text-check script in `files/`

|     | Info |
| --- | --- |
| **Phase** | SPECIFICATION PHASE |
| **When** | 2026-11-16 05:22 UTC |
| **Question** | Verify the change with a throwaway text-check script in the bundle's `files/`, run by the main session? |
| **Interview question** | [`04/1`](./phase-04-specification/phase.md#interview) |
| **Decision** | Decided under delegation (autonomous): as proposed: `files/phase-05-text-checks.py`, checks T-1 – T-19 (T-19 added in fix attempt 1; its one-rule half by hand, 04/6). |
| **Basis** | Phase 02 conventions, "Tests of skill text" ([phase-02 #conventions](./phase-02-code-analysis/phase.md#conventions)); lesson `2026-11-11.text_checks_read_their_place`. |
| **Alternatives** | manual review only |
| **Materiality** | not material |
| **Status** | DELEGATED |

<a id="dd-23"></a>
## DD-23 — Version value by the CI rule

|     | Info |
| --- | --- |
| **Phase** | SPECIFICATION PHASE |
| **When** | 2026-11-16 05:22 UTC |
| **Question** | Set the next version by the CI's own rule, on the day Phase 05 runs? |
| **Interview question** | [`04/2`](./phase-04-specification/phase.md#interview) |
| **Decision** | Decided under delegation (autonomous): as proposed: `YY.MDD.N` — on 2026-11-16, `26.1116.1`. |
| **Basis** | Brief "Files to change" item 4 ([log.md](./log.md), 2026-11-15 21:14); `.github/workflows/bump-version.yml`; DD-10. |
| **Alternatives** | `26.1115.2` (the next number on the current date) |
| **Materiality** | not material |
| **Status** | DELEGATED |

<a id="dd-24"></a>
## DD-24 — Claim-source line as a `**Verifier claims.**` bullet

|     | Info |
| --- | --- |
| **Phase** | SPECIFICATION PHASE |
| **When** | 2026-11-16 05:22 UTC |
| **Question** | Add the claim source to each phase's Mode behaviour as one `**Verifier claims.**` bullet, directly before the line that points to the governing skill? |
| **Interview question** | [`04/3`](./phase-04-specification/phase.md#interview) |
| **Decision** | Decided under delegation (autonomous): as proposed. |
| **Basis** | Brief "Files to change" item 3: "add that phase's line from rule 5, and refer to the governing skill for the rest" ([log.md](./log.md), 2026-11-15 21:14). |
| **Alternatives** | a sentence inside the Quality Criteria bullet |
| **Materiality** | not material |
| **Status** | DELEGATED |

<a id="dd-25"></a>
## DD-25 — Plan structure: four phases

|     | Info |
| --- | --- |
| **Phase** | SPECIFICATION PHASE |
| **When** | 2026-11-16 05:22 UTC |
| **Question** | Structure the plan as four implementation phases, one per group in the brief's "Files to change"? |
| **Interview question** | [`04/4`](./phase-04-specification/phase.md#interview) |
| **Decision** | Decided under delegation (autonomous): as proposed: Gate test; Subagent Execution and the worker; phase skills; version and checks. |
| **Basis** | Brief "Files to change" items 1 – 4 ([log.md](./log.md), 2026-11-15 21:14). |
| **Alternatives** | one phase per file |
| **Materiality** | not material |
| **Status** | DELEGATED |
