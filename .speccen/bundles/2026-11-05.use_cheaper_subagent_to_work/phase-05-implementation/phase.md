---
type: Phase
phase: "05 — Implementation"
status: COMPLETE
description: Plan executed in seven files — template v2 and model on 04/05, the search unit, the gate-test self-check and delta re-check, pointers, restated copies; T-1 – T-19 pass
---

<a id="phase-top"></a>
# Use cheaper subagent to work — Implementation

[Index](../index.md) · [State](../STATE.md) · [Log](../log.md)

---

<a id="extensions"></a>
## Extensions applied

| Extension | Why | Where it applies | Outcome |
|---|---|---|---|
| — | — | — | No extensions for this phase: `.speccen/extensions/implementation/` does not exist |

## Project Conventions Re-Confirmation (Phase 05)

No `.claude/` folder and no `CLAUDE.md` exist. `.github/` holds `SECURITY.md` (markdown),
`CODEOWNERS` and `workflows/bump-version.yml`; all were re-read on 2026-11-05.

#### `.github/SECURITY.md`
**Re-Read:** ✓
**CRITICAL/MANDATORY Rules Impacting This Implementation:** none for the edited text. Relevant
scope line, verbatim: "Prompt-injection weaknesses in the skills and workflows" — the new Search
section keeps the worker read-only and decision-free, and the main session re-opens every
finding, so repository text a worker reads never becomes an instruction.

**Other Rules Impacting This Implementation:**
- Calendar versions `YY.MDD.N` are set by the release workflow — `.claude-plugin/plugin.json` is not edited by hand.

#### `.github/CODEOWNERS`
**Re-Read:** ✓
**Other Rules Impacting This Implementation:** default owner `* @speccen/team-leads`; this change
touches neither `/.github/` nor `/.claude-plugin/`.

#### `.github/workflows/bump-version.yml` (not markdown; read for workflow)
**Re-Read:** ✓
**Other Rules Impacting This Implementation:** a skill change bumps the version on merge to
`main`; README/ARCHITECTURE-only changes do not. No edit needed here.

Conventions from history ([Phase 02](../phase-02-code-analysis/phase.md#conventions)): restated
copies change in the same commit as their source (DD-12); one-line italic pointers into the
governing skill; lines wrapped at about 100 characters.

## Plan confirmation

Plan confirmed by the delegate — 2026-11-05 (autonomous mode). Executed from
[the Implementation Plan](../phase-04-specification/phase.md#implementation-plan). Phase 04 is
closed, so the ticked checklist is recorded here.

<a id="implementation-summary"></a>
## Implementation Summary

### Phase 1: Configuration — keys, fail-safe and template version 2 ✅
- [x] 1.1 Keys `version` row → "the current version is `2`"
- [x] 1.1 `model` bullet lists `code-analysis`, `compliance-review`, `specification`, `implementation`, `close-out`, `retrospective`, `reference`
- [x] 1.1 Fail-safe → "or a `model` on `feature-analysis`."
- [x] 1.2 Template `version: 2`
- [x] 1.2 `specification:` gains `model: economy           # searches`
- [x] 1.2 `implementation:` gains `model: economy           # searches`
- [x] 1.3 v1 example intro → "…and nothing else, when it is upgraded to version 1:"
- [x] 1.3 After the example's closing paragraph: "An upgrade to version 2 also adds `model: inherit` to `specification` and `implementation`, and sets `version: 2`."
- [x] 1.4 Validate: T-1, T-2, T-3, T-14, T-18, T-19 pass; the template block parses as YAML (`version` 2; `specification` and `implementation` each `model: economy`)

### Phase 2: Subagent Execution — the search unit ✅
- [x] 2.1 Units table: search row added as the first row
- [x] 2.1 "Nothing else runs in a subagent — a search that is not launched as this unit runs inline." (the paragraph after it re-wrapped, wording unchanged)
- [x] 2.2 `### Search` section between **The worker and the work order** and **Model**: one question; read-only, no decision; work order with breadth and `Outputs: none — report only`; findings only; no files; re-open before citing; never cited alone; parallel; tier rule incl. Phase 01 and Phase 05; `speccen-worker`, not a built-in search agent; existing log line
- [x] 2.3 Validate: T-4, T-5, T-6, T-15, T-16 pass

### Phase 3: Gate test — self-check and delta re-check ✅
- [x] 3.1 **Self-check before the verifier** bullet with five checks and `Self-check: done — N fixes`
- [x] 3.2 Delta re-check text replaces "If any item fails, fix it once and run the test again. If it still fails, stop."
- [x] 3.3 Validate: T-7, T-8, T-9 pass

### Phase 4: Phase skills — pointer lines ✅
- [x] 4.1 `02-code-analysis`: pointer at the end of Step 2 and after the Step 3 intro paragraph
- [x] 4.1 `05-implementation` Step 3: pointer after the per-item list
- [x] 4.1 `interview`: bundle/store lookup → "inline, or as a search unit (governing skill → Subagent Execution → Search)"; code lookup → "Phases 03 and 04 may look it up in the code — inline, or as a search unit."
- [x] 4.2 Validate: T-10 passes

### Phase 5: Restated copies ✅
- [x] 5.1 README template block replaced with the governing block (character for character)
- [x] 5.1 README "Model tiers": searches sentence added
- [x] 5.1 ARCHITECTURE Subagents bullet: searches added; the verifier now "runs in one on the session's model"
- [x] 5.1 `agents/speccen-worker.md` description: "a search" added
- [x] 5.2 Validate: T-11, T-12, T-13, T-17 pass

### Phase 6: Verification and hand-over ✅
- [x] 6.1 T-1 – T-19 run and recorded below
- [x] 6.1 `git diff --stat -- . ':(exclude).speccen'` → 7 files: `ARCHITECTURE.md`, `README.md`, `agents/speccen-worker.md`, `skills/sdd/00-governing-workflow/SKILL.md`, `skills/sdd/02-code-analysis/SKILL.md`, `skills/sdd/05-implementation/SKILL.md`, `skills/sdd/interview/SKILL.md` — the seven of the Proposed Changes Summary
- [x] 6.1 Skill changes left uncommitted for the Architect (DD-15)
- [x] 6.2 All checks pass

<a id="tests"></a>
## Test results

One Python script (scratchpad, not committed — the Test Plan says no test location exists) reads
the edited files and `git show HEAD:<file>` for the before-state, and asserts each check as
written in the [Test Plan](../phase-04-specification/phase.md#implementation-plan). Assertions
come from the Test Plan and requirements text, not from the edited files.

| Id | Requirement | What the script asserts | Result |
|---|---|---|---|
| T-1 | R-7 | template block has `version: 2 `; `model: economy` inside both the `specification:` and `implementation:` entries; Keys says "the current version is `2`"; "current version is `1`" occurs nowhere | PASS |
| T-2 | R-6 | the `model` bullet's backticked names are exactly the seven phases, in order | PASS (after check fix, see below) |
| T-3 | R-6 | fail-safe reads "or a `model` on `feature-analysis`."; the old three-phase text is gone | PASS |
| T-4 | R-1, R-5 | search row present; inline sentence present; "Nothing else runs in a subagent. " gone | PASS |
| T-5 | R-1 – R-4 | `### Search` sits after "The worker and the work order" and before "Model"; contains the 14 required phrases (one stated question, `Outputs: none — report only`, `path:line`, verbatim quote, what was not found, no conclusions, re-opens every finding, never cited alone, read-only, takes no decision, `speccen-worker`, no `model` key case, `inherit`, Phase 05 uses `phases.implementation.model`) | PASS |
| T-6 | R-12 | Model section's verifier sentence identical before and after; template comment "Decision seats and the gate-test verifier always run on the session's model." present; gate verifier bullet still "on the session model" | PASS |
| T-7 | R-10 | gate test has the self-check bullet, checks 1–5 and `Self-check: done — N fixes` | PASS |
| T-8 | R-11 | gate test has (a) failed rows, (b) rows whose evidence is in a changed file, `confirmed (run 1)`; old text gone | PASS |
| T-9 | R-11 | "If a re-checked row still fails, stop." present | PASS |
| T-10 | R-1, R-9 | 02 has the pointer twice; 05 once; interview has both lookup lines | PASS |
| T-11 | R-13 | README template block equals the governing block (string equality) | PASS |
| T-12 | R-12, R-13 | ARCHITECTURE Subagents bullet names searches and puts the verifier on the session's model; the old "verifier) run … on their tier's model" pattern is gone | PASS |
| T-13 | R-13 | worker frontmatter description contains "a search, an evidence reading" | PASS |
| T-14 | R-8 | upgrade rule bullets identical before and after; "a phase's `model` is added as `inherit`" present | PASS |
| T-15 | R-14 | "Log each launched unit" text identical before and after; Search gives the line in the same format | PASS |
| T-16 | R-15 | Search states `quick` · `medium` · `thorough` and that independent searches may run in parallel | PASS |
| T-17 | R-13 | README "Model tiers" has the searches sentence with Phases 02 to 05 and any phase | PASS |
| T-18 | R-16 | Keys table key list identical before and after; Model section identical; template `models:` identical | PASS |
| T-19 | R-8 | v1 intro says "when it is upgraded to version 1"; the v2 sentence directly follows the closing paragraph | PASS |

**Check fix (T-2).** The first run failed T-2. The skill text was correct — the bullet lists the
seven phases — but the check's pattern required a line break before "phases with subagent units",
and the re-wrapped bullet breaks the line elsewhere. The pattern was made whitespace-tolerant;
the assertion (exactly these seven phases, in order) did not change. No skill text changed for it.

Behaviours to cover (Test Plan): R-2 by T-5 (writes no files; no decision); R-5 by T-4; R-6
error path by T-3 (a `model` on 01 still ignored); R-8 by T-14 and T-19; R-11 error path by T-9;
R-12 by T-6 and T-12. Every requirement R-1 – R-16 has at least one passing check.

<a id="deviations"></a>
## Deviations

None. Every checklist item was done as written. Two notes, neither a deviation:
- The paragraph after the changed "Nothing else runs…" sentence was re-wrapped; its words did not change.
- The plan's line numbers were at `b59e7ab`; edits were placed by the text each item names.
- Item 6.1 asks to record each command: the checks ran as one Python script, so each row above records the assertion the script makes rather than a shell line.

<a id="outcome"></a>
## Outcome

The plan is implemented in the seven planned files and all nineteen planned checks pass. The
skill changes are uncommitted in the working tree for the Architect (DD-15).

<a id="open-items"></a>
## Open Items

| # | Item | Status |
|---|---|---|
| O-10 | The brief's §6 cost measurement on the next bundle | follow-up, carried |
