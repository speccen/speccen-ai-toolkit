---
type: Phase
phase: "02 — Code Analysis"
status: COMPLETE
description: The subagent and gate-test rules live in one governing section each, but six restated sites (README, ARCHITECTURE, worker description, fail-safe, version row) sit beyond the brief's edit list
---

<a id="phase-top"></a>
# Use cheaper subagent to work — Code Analysis

[Index](../index.md) · [State](../STATE.md) · [Log](../log.md)

---

<a id="extensions"></a>
## Extensions applied

| Extension | Why | Where it applies | Outcome |
|---|---|---|---|
| — | — | — | No extensions for this phase |

`.speccen/extensions/code-analysis/` does not exist in this repository.

<a id="code-analysis"></a>
## Code Analysis

The "code" under analysis is speccen's own instruction text: markdown skills read by the host
agent, one agent definition, and a YAML template embedded in the governing skill. There is no
executable code, no build and no test suite. All line numbers below are at commit `b59e7ab`
(branch `feature/use-cheaper-subagent`).

### Orientation and durable store

- **P02-1 — confirmed.** `.claude-plugin/plugin.json` declares `"version": "26.1104.2"` and
  `"skills": ["./skills/sdd/", "./skills/audit/", "./skills/code/"]`. The repository is the plugin
  source; the brief's Target is this tree.
- **Installed vs source.** The session runs the installed plugin 26.1103.1 (01/13). A diff of
  `skills/` shows only three files differ: `00-governing-workflow`, `06-close-out`, `reconcile`.
  In the governing skill the difference is Step 0 (config upgrade, `SKILL.md:409–419`), the
  `version` key, the template intro (`:728–729`), `stops: inherit` per phase in the template, the
  section **Upgrading the project file** (`:844–911`), its ownership notes (`:956`, `:959`),
  Invariant 1 (`:2109–2111`), and the store-index section order. `agents/speccen-worker.md` is identical.
- **Durable store.** `.speccen/` holds only this bundle and the project config created at
  session start; there are no decisions, lessons, notes or features to read. No prior art, no
  fences.
- **Side effect of 01/13, recorded for later phases.** The project config this bundle created
  (`.speccen/speccen-config.yaml`) follows the 26.1103.1 template: no `version`, no
  `stops: inherit` per phase. A session on 26.1104.2 would upgrade it at Step 0.

### Architecture Overview

The behaviour the request changes sits in three sections of
`skills/sdd/00-governing-workflow/SKILL.md` (2165 lines) and is restated in nine other files (README, ARCHITECTURE, `agents/speccen-worker.md`, `interview`, and the phase skills 02, 03, 06, 07, 08).

| Concern | Source of truth (governing skill) | Restated in |
|---|---|---|
| Config keys; which phases take `model` | Configuration → Keys `:687–723`; the list at `:702–710` (`model` at `:708–709`) | fail-safe `:940–941` (repeats the phases that do **not** take `model`); README "Model tiers" `:305–329` (no phase list) |
| Config template | Configuration → Templates `:725–796` (`version: 1` at `:735`, `model: economy` at `:764`) | **README `:238–303` — a full copy of the template** |
| Upgrade rule | Upgrading the project file `:844–911`; Step 0 `:409–419` | ARCHITECTURE `:140–144` |
| Gate test (verifier) | Autonomous Execution → Gate test `:1143–1163` | template comment `:755`, README `:262`, `:326` |
| Units table; "Nothing else runs in a subagent" | Subagent Execution → Units `:1298–1310` | **ARCHITECTURE `:156–158`** (lists the units; `:153–155` is the tiers bullet — S-3 covers both); phase pointers 02 `:259`, 03 `:192`, 06 `:88`, 07 `:30`, 08 `:165` |
| Worker, work order, one writer, log line | `:1312–1337` | `agents/speccen-worker.md` (description lists unit kinds) |
| Model resolution | Subagent Execution → Model `:1339–1345` | README `:307–329` |
| Code lookups in interviews | — (no unit) | **interview `:62–67`** |

Dependencies: every phase skill points into Subagent Execution by name; `agents/speccen-worker.md`
is launched by name from `:1314`; the template is read by Step 0 and by bundle creation (New
Session Protocol step 3). Dependents of the Units table: phases 02, 03, 06, 07, 08 and every
autonomous gate test.

### Behavioural Analysis

**Path 1 — launching a subagent unit (today).** The skill text at `:1298–1356` defines the
sequence below. The only branch on "is this work a unit" is the closed Units table plus the
sentence "Nothing else runs in a subagent." (`:1309`).

```
          ┌───────────────────────────────┐
          │ phase step reaches some work  │
          └───────────────┬───────────────┘
                          ▼
              ┌───────────────────────┐
              │ listed in Units table?│  (:1298–1307)
              └────┬─────────────┬────┘
                 no│             │yes
                   ▼             ▼
       ┌──────────────────┐  ┌───────────────────────┐
       │ run inline in the│  │ is the unit the gate- │
       │ main session     │  │ check verifier?       │
       │ ("Nothing else   │  └────┬─────────────┬────┘
       │  runs in a       │    yes│             │no
       │  subagent" :1309)│       ▼             ▼
       └──────────────────┘  ┌────────────┐  ┌──────────────────────────┐
                             │ session    │  │ tier = phases.<p>.model  │
                             │ model      │  │ (inherit → session)      │
                             │ (:1344)    │  │ model = models.<tier>    │
                             └─────┬──────┘  │ local → project → builtin│
                                   │         └────────────┬─────────────┘
                                   └──────────┬───────────┘
                                              ▼
                               ┌──────────────────────────────┐
                               │ host cannot launch speccen-  │
                               │ worker, or the launch fails? │ (:1354)
                               └──────┬────────────────┬──────┘
                                   yes│                │no
                                      ▼                ▼
                         ┌─────────────────────┐ ┌──────────────────────────┐
                         │ run inline, session │ │ launch worker with work  │
                         │ model; say so once  │ │ order + requested model; │
                         │ per session (:1354– │ │ log line (:1336); if the │
                         │ 1355)               │ │ host did not confirm the │
                         └─────────────────────┘ │ model, say so (:1355–56) │
                                                 └────────────┬─────────────┘
                                                              ▼
                                               ┌──────────────────────────────┐
                                               │ check outputs exist/complete │
                                               │ missing → inline once; still │
                                               │ failing (autonomous) → gate  │
                                               │ failure (:1330–1332)         │
                                               └──────────────────────────────┘
```

Decision seats never enter this flow: they are not units and "never" run in a subagent
(`:1309–1310`).

Observed gap (the brief's cause 1): a code search reaches the "no" branch and must run inline on
the session model. The interview skill already sends one more kind of work down the "yes" branch
without a table row: "look it up — inline, or as a read-only `speccen-worker` unit" for bundle and
store facts (interview `:63–65`). So the rule-vs-practice gap exists in the text itself, not only
in the evidence bundle.

**Path 2 — the gate test (today), `:1143–1163`.**

```
     ┌──────────────────────────────────────┐
     │ end of an autonomous phase           │
     └──────────────────┬───────────────────┘
                        ▼
     ┌──────────────────────────────────────┐
     │ evaluate Quality Criteria item by    │
     │ item with cited evidence; Mode-      │
     │ behaviour checks; write table        │
     │ item | result | evidence | verified  │
     └──────────────────┬───────────────────┘
                        ▼
              ┌──────────────────────┐
              │ host runs subagents? │
              └────┬────────────┬────┘
                 no│            │yes
                   ▼            ▼
      ┌──────────────────┐  ┌──────────────────────────────┐
      │ verified =       │  │ verifier (speccen-worker,    │
      │ "not run"        │  │ session model) re-opens the  │
      └────────┬─────────┘  │ evidence of EVERY row        │
               │            └──────────────┬───────────────┘
               └───────────────┬───────────┘
                               ▼
                     ┌───────────────────┐
                     │ any item failed?  │
                     └───┬───────────┬───┘
                       no│           │yes
                         ▼           ▼
              ┌──────────────┐  ┌─────────────────────────────┐
              │ transition   │  │ fix once; run the test      │
              └──────────────┘  │ again — again EVERY row     │
                                └──────────────┬──────────────┘
                                               ▼
                                     ┌───────────────────┐
                                     │ still failing?    │
                                     └───┬───────────┬───┘
                                       no│           │yes
                                         ▼           ▼
                                 ┌────────────┐ ┌──────────┐
                                 │ transition │ │  STOP    │
                                 └────────────┘ └──────────┘
```

There is no self-check before the verifier, and "run the test again" (`:1160`) does not limit the
second run. Both of the brief's B-changes attach to this one bullet list.

**Inputs / outputs / side effects.** Inputs are config values and the phase's artifacts. Outputs
are the `verified` column, the `log.md` subagent line, and — on failure — a stop. Side effects:
model spend per worker launch; no file writes by workers beyond their listed outputs.

### Data Model

| Structure | Where | Fields relevant here | Cardinality |
|---|---|---|---|
| Project config | template `:731–796` | `version` (1), `mode`, `stops`, `lock`, `phases.<8 keys>.{mode,stops,model,prototypes,lock}`, `models.{economy,balanced,premium}` | 1 per repo; `model` present on 5 of 8 phases today |
| Phase → keys list | `:702–710` | `model` allowed on `code-analysis`, `compliance-review`, `close-out`, `retrospective`, `reference` | a `model` on any other phase is ignored and mentioned once — fail-safe `:939–941`: "So is a key on a phase that does not take it — … a `model` on `feature-analysis`, `specification` or `implementation`" |
| Units table | `:1300–1307` | Phase · Unit · Parallel · Stays in the main session | 6 rows |
| Work order | `:1317–1325` | Unit, Bundle, Follow, Inputs, Outputs, Return | 1 per launch |
| Gate-check table | `:1151–1152` | `item | result | evidence | verified` | one row per Quality Criterion (≈15–20 per phase) |
| Subagent log line | `:1336–1337` | time, phase, unit, tier → model, source | 1 per launch |

Consequence for A3/A4: putting `model: economy` on `specification` or `implementation` in the
template without changing the phase→keys list (`:708–709`) **and** the fail-safe list
(`:940–941`) would make the fail-safe ignore it. A3, A4 and the fail-safe line must land together.

Consequence for 7/3: the upgrade rule (`:856–859`) adds a missing phase `model` as `inherit`,
"not as the template's tier". So with `version: 2`, an existing project gets
`model: inherit` on 04 and 05 — today's behaviour — exactly as the brief's "Upgrading" note
assumes. **P02-2 — confirmed**: the template has `version: 1` (`:735`) and `stops: inherit` on the
five phases that take it (`:759`, `:763`, `:768`, `:774`, `:778`), and the upgrade rule exists.

### Coding Patterns & Style

- **Single source of truth with pointers.** Rules live once in the governing skill; phase skills
  carry one italic pointer line, e.g. 02 `:259` "*The evidence reading for this step may run as a
  subagent unit (governing skill → Subagent Execution). The determination itself stays in the main
  session.*" The brief's A5 lines follow exactly this pattern.
- **Restated copies do exist** despite that pattern: the README carries the full config template;
  ARCHITECTURE enumerates the units. Past changes kept them in sync in the same commit — e.g.
  `47ce36a` (config upgrade) touched `ARCHITECTURE.md`, `README.md` and the governing skill;
  `999c03e` (stops) touched `README.md`, governing and `interview`.
- **Template versioning.** "When the template gains a key, its `version` goes up by one, and the
  key, its comment and the value that means its absence are added above." (`:909–910`). The
  version appears at `:691` (Keys row: "the current version is `1`"), `:735` (template),
  README `:242`, and in three places of the v1 upgrade example (`:418`, `:876`, `:902`). The first
  three state the current version; the three example lines describe the v1 upgrade.
- **Prose register.** Skill text is short-sentence, imperative, STE-leaning; tables for rules;
  `**bold**` lead-ins; explicit "never/only" lists.
- **Commit style.** Conventional commits, `feat:` for skill behaviour changes, `docs:` for README /
  ARCHITECTURE only; version bump is automated on merge to `main` (bump-version workflow).
- **Test conventions.** There is no test framework or runner. The skills are prose; verification
  today is review and running a bundle. The Phase 04 Test Plan therefore has to establish the
  approach — realistically: text checks (every restated copy matches the source; grep for stale
  `version: 1`, the old Units sentence, the old `model` phase list) plus, optionally, the brief's §6
  measurement as a follow-up.

### Performance Characteristics

The "performance" here is model spend.

- **Verifier cost per phase** = rows × evidence re-opened × runs. Rows ≈ 15–20 (Phase 01 of this
  bundle: 15, then 19 rows; run 3 re-checked 9). Runs: 1 if clean, 2 after one fix (`:1160`), each re-checking every
  row. This bundle's Phase 01 needed three runs (the third only because the Architect chose a
  changed-rows re-check at a stop, 01/12): run 1 confirmed 12 of 15, run 2 18 of 19, run 3 8 of 9.
- **What failed in practice** (this bundle, runs 1–3): a term count, a non-verbatim quote, facts
  filed as hypotheses, a missing criterion row, an in-round dependency, a bundled question. These
  overlap the brief's four kinds (quotes, references, latest answer, index) only partly:
  **interview-structure** defects (frontier, one decision per question) are not among B1's four
  checks. Evidence for Phase 03, not a conclusion.
- **Code searches.** Today every Phase 02 search is inline (session model) or an unlisted
  subagent. This phase ran its searches inline. The brief's §1 counts (4 searches on the session
  model) are taken as stated (DD-4).

### Relationship to Similar Components

| Component | Model | Writes files | Decides | Relevance |
|---|---|---|---|---|
| 02 evidence reading (unit) | phase tier (`economy`) | no (input to determination) | no | closest peer to code search; the brief's §1 says it ran inline |
| 03 prototypes (unit) | phase tier (`balanced`) | yes, in worktrees | no | why 7/2 keeps `balanced` for 03 |
| 06/07/08 units | phase tier | yes | no | — |
| gate-check verifier (unit) | always session | no (report only) | no | the only existing **report-only** unit — the precedent for code search's `Outputs: none — report only` |
| interview bundle/store lookup | unspecified ("read-only `speccen-worker` unit") | no | no | an existing unlisted unit; A1's new sentence would make it run inline unless it is also listed |
| host built-in read-only search agent (e.g. Claude Code's Explore) | host-defined; the repo states nothing | no | no | what the evidence bundle used (brief §1); not referenced anywhere in the repo |

For O-4 (which agent runs a code search): `agents/speccen-worker.md` has `model: inherit` and the
governing skill passes the resolved model at launch (`:1314–1315`), so a tier is honoured through
the launch parameter. The worker's "Never" list already forbids decisions and writes outside its
outputs, which fits "findings only". Its description (`speccen-worker.md:3`) enumerates unit kinds and does not
include a search. Nothing in the repo states how a host's built-in search agent takes a model;
that is a host fact, and Host support (`:1347–1356`) already warns that hosts may ignore a
requested model.

### Known Issues & Code Commentary

No `TODO`, `FIXME` or `HACK` markers in `skills/sdd`, `agents`, `commands`, `README.md` or
`ARCHITECTURE.md`. Relevant verbatim commentary:

- Template comment, governing `:755` and README `:262`: "# Decision seats and the gate-test
  verifier always run on the session's model."
- Template comment, governing `:761`: "code-analysis:             # 02 — evidence reading
  runs as a subagent" — a comment that names the unit; A4 adds "# code searches" comments in the
  same style.
- Governing `:1309`: "Nothing else runs in a subagent."
- Interview `:67`: "Phases 03 and 04 may look it up in the code."

<a id="conventions"></a>
## Project Conventions Confirmation

No `.claude/` folder exists. `.github/` holds one markdown file (`SECURITY.md`), `CODEOWNERS` and one workflow; all three were read.

#### `.github/CODEOWNERS`
**Read:** ✓
**CRITICAL/MANDATORY Rules:** N/A
**Architecture Boundaries:** N/A
**Technology Constraints:** N/A
**Naming Conventions:** N/A
**Critical Workflows:** `/.github/` and `/.claude-plugin/` owned by `@speccen/team-leads` — "Workflows and release automation can change what runs with write access"; "Plugin manifests carry the published version and marketplace metadata".
**Hard Constraints:** Default owner for everything: `* @speccen/team-leads`. This change touches neither `/.github/` nor `/.claude-plugin/`.

#### `.github/SECURITY.md`
**Read:** ✓
**CRITICAL/MANDATORY Rules:** "Please do not report security vulnerabilities through public GitHub issues, discussions, or pull requests."
**Architecture Boundaries:** N/A
**Technology Constraints:** Calendar versions `YY.MDD.N`; fixes to the latest release only.
**Naming Conventions:** N/A
**Critical Workflows:** Private vulnerability reporting via the Security tab, fallback email.
**Hard Constraints:** In-scope issues include "Instructions or commands that could cause an assistant to run unintended or destructive actions" and "Prompt-injection weaknesses in the skills and workflows" — relevant: a code-search worker reads repository content, which the store rules already treat as data, not instructions.

#### `.github/workflows/bump-version.yml` (not markdown; read for workflow)
**Read:** ✓
**Critical Workflows:** On push to `main`, except `paths-ignore` `.github/**`, `README.md`, `ARCHITECTURE.md`, `LICENSE`, bumps `.claude-plugin/plugin.json` to `YY.MDD.N`. A skill change triggers a bump on merge; a README/ARCHITECTURE-only change does not.
**Hard Constraints:** None stated. Inferred, not stated: the version in `plugin.json` is set by this workflow, so a change does not edit it by hand.

Conventions observed in history (not in files): conventional commits (`feat:`, `docs:`,
`refactor:`); one feature per PR from a `feature/*` branch; restated copies updated in the same
commit as the source.

<a id="outcome"></a>
## Executive Summary

**Dominant finding.** The request slots cleanly into the current structure: every rule it changes
has one source section in the governing skill (Keys, Templates, Gate test, Subagent Execution),
and the phase skills already use the one-line pointer pattern A5 proposes. But the brief's edit
list is incomplete — the README carries a full copy of the config template, ARCHITECTURE
enumerates the subagent units, the fail-safe repeats the `model` phase list, and the current
`version` is stated in three places — so the change is six restated sites larger than its Target
row ([S-1 – S-6](#restated-sites)).

**Root cause of the brief's cause 1, confirmed in text.** The Units table is closed ("Nothing else
runs in a subagent", `:1309`), yet the interview skill already names an unlisted read-only
`speccen-worker` lookup (`:63–65`). Rule and practice differ inside the skills, not only in the
evidence bundle. Change A's new sentence ("a code search that is not launched as this unit runs
inline") would also govern that interview lookup.

**Key insight for Phase 03.** A3 and A4 are coupled through the fail-safe (a `model` on a phase
not in the Keys list is ignored), and the upgrade rule already adds a missing `model` as `inherit`
— so 7/3's "nothing changes without a choice" holds by existing text. For Change B, the Phase 01
evidence of this bundle shows interview-structure defects that B1's four checks do not cover.

<a id="open-items"></a>
## Open Items

| # | Item | Settles in |
|---|---|---|
| O-1 – O-3 | §7 decisions 7/1, 7/2, 7/3 (carried from Phase 01; facts above) | Phase 03 |
| O-4 | Search agent: `speccen-worker` vs host built-in. Facts: worker takes the tier via the launch model; the repo says nothing about built-in agents' models | Phase 03 |
| O-6 | Acceptance and "done when" | Phase 04 |
| O-7 | Does the interview's existing bundle/store lookup unit (`interview:63–65`) become a Units row too, or fold into code search? It is affected by A1's new sentence | Phase 03 |
| O-8 | Do B1's four self-check kinds get a fifth for interview structure (frontier, one decision per question)? Evidence: this bundle's Phase 01 runs | Phase 03 |
| O-9 | Scope additions S-1 – S-6 ([restated sites](#restated-sites)); whether the v1 upgrade example lines change | Phase 04 (plan), confirm in Phase 03 |

**Settled in this phase:** P02-1 (Orientation), P02-2 (Data Model), P02-3 (Architecture Overview
and the site list below) — so Phase 01's O-5 is closed. None of the open items blocks Phase 03.

<a id="restated-sites"></a>
**Restated sites outside the brief's edit list (P02-3, O-9)** — six:

| # | Site | Why it must change |
|---|---|---|
| S-1 | README `:238–303` — full copy of the template | A4 (`model: economy` on 04/05) and `version: 2` (7/3) |
| S-2 | README "Model tiers" `:305–329` | says "Phases with subagent work name a tier" (`:307`) and what runs on the session model (`:326`); 04 and 05 gain subagent work |
| S-3 | ARCHITECTURE `:153–158` | lists the units; also says the verifier runs "on their tier's model", which contradicts governing `:1344` today |
| S-4 | `agents/speccen-worker.md:3` description | enumerates unit kinds; a search is not among them |
| S-5 | governing fail-safe `:940–941` | lists `specification` and `implementation` as phases that do not take `model` (A3) |
| S-6 | governing Keys row `:691` — "the current version is `1`" | 7/3 raises the version |

The template line `:735` and the interview lookup rule are in the brief already (A4, A5). The v1
upgrade example (`:418`, `:876`, `:902`) describes the v1 upgrade and may stay; Phase 04 decides.
