---
type: Summary
phase: "04 — Specification"
status: COMPLETE
phase_file: ./phase.md
description: Four-phase plan plus an iteration-2 addendum (ADR: fix ARCHITECTURE.md:307), 8 requirements, 13 checks (T-1 – T-3 run against the planned text); plan and Test Plan approved under delegation
---

# Phase 04 Summary — Specification

[Index](../index.md) · [State](../STATE.md) · [Log](../log.md)

---

**Work completed:** an Implementation Plan in four phases (move; skills and script; command and
docs; verify and commit), with the substitution map, the planned README note, a target-state flow
and a Test Plan of 13 checks. One interview round (04/1 – 04/3). The checks T-1 – T-3 ran against
the planned text in an in-memory simulation and passed; a broken plan failed.

**Outcome:** `git mv` of the five folders plus the substitution map on nine files, one code
commit → [full detail](./phase.md#implementation-plan)

**Specification (the complete, assembled spec — intent + requirements/scenarios):**
- [specification.html](./specification.html) — full, authoritative (reduced view: [specification.md](./specification.md))

**Stakeholder seeds (intent — expansion seeds, not for verbatim external sharing):**
- Executive → [doc-executive.md](./doc-executive.md)
- Business → [doc-business.md](./doc-business.md)

**Open items carried forward:** → [detail](./phase.md#open-items)
- `[DD-7 | Tighten Verification 1 with \b after the sdd- group?]` — `MATERIAL — unconfirmed`, review round
- `[DD-8 | ARCHITECTURE.md:307 stale skills/sdd/NN-* path]` — follow-up, end-of-run report
- `[DD-3 | Push and PR wait for the Architect]` — end of run

**Delegated decisions:** 3 in this phase (`DD-10` – `DD-12`, all `not material`), 12 in total → [delegated-decisions.md](../delegated-decisions.md)

**Extensions applied:** none

<a id="delegate-gate-check"></a>
## Delegate gate check

Self-check: done — 0 corrections. Verifier run 1: 6 confirmed, 1 slip (K-7, citation corrected); no fix attempt used.

The delegate approves the Implementation Plan and the Test Plan (decided under delegation
(autonomous); basis: the brief, DD-1 – DD-12, the Phase 02 inventory). No test is waived.

| # | Item | Result | Evidence | Verified |
|---|---|---|---|---|
| 1 | Extensions table complete | pass | `.speccen/extensions/` does not exist; [phase.md#extensions](./phase.md#extensions) | n/a — bundle-internal |
| 2 | Proposed changes list every file with its change type | pass | Proposed Changes Summary: 5 renamed folders (19 files), 9 modified files, unchanged list | confirmed (run 1) |
| 3 | Target-state flow as ASCII, linked to Phase 02 | pass | Target-State Execution Flow; link to `../phase-02-code-analysis/phase.md#code-analysis` | confirmed (run 1) |
| 4 | Strategy evaluation where needed | pass | one approach, prescribed by the brief | n/a — bundle-internal |
| 5 | Phases numbered and sequenced | pass | Phases 1 – 4 | n/a — bundle-internal |
| 6 | Checklist items specific and traceable | pass | each item names the file, lines and map; lines from Phase 02 group A, B | confirmed (run 1) |
| 7 | Each phase ends with Build and Validate | pass | 1.2, 2.4, 3.4, 4.4 | n/a — bundle-internal |
| 8 | Each phase states a Why with a source | pass | Phases 1 – 4 Why lines cite the brief, Phase 02 anchors, DD-2/4/10/11/12 | n/a — bundle-internal |
| 9 | Risk table populated | pass | 7 risks | n/a — bundle-internal |
| 10 | Test Plan present with scope, behaviours, coverage | pass | T-1 – T-13; "Not tested" row; behaviours by kind; run on the planned text | n/a — bundle-internal |
| 11 | Intent seeds written, `expandable: true` | pass | [doc-executive.md](./doc-executive.md), [doc-business.md](./doc-business.md) | n/a — bundle-internal |
| 12 | Seeds in STE style | pass | short active sentences; same terms as the brief ("audit skills", "folder", "name") | n/a — bundle-internal |
| 13 | Executive seed keeps TCO out | pass | Scope Note | n/a — bundle-internal |
| 14 | Deviations protocol stated | pass | Deviations Protocol | n/a — bundle-internal |
| 15 | `specification.html` assembled with `specification.md` | pass | both files; frontmatter block; nav bar | n/a — bundle-internal |
| 16 | Requirements & acceptance scenarios with error and edge cases | pass | R-1 – R-8; edges: `sdd-reconcile` (R-3), a wrong script folder (R-4) | n/a — bundle-internal |
| 17 | Diagrams verified to render | pass | both inline SVGs parse with `xml.etree.ElementTree`; no external asset | n/a — bundle-internal |
| 18 | Summary links plan, spec and seeds | pass | this file | n/a — bundle-internal |
| 19 | `index.md` lists every file this phase wrote | pass | [index.md](../index.md) Phase 04 | n/a — bundle-internal |
| 20 | Interview structure | pass | [phase.md#interview](./phase.md#interview) 04/1 – 04/3; DD-10 – DD-12 | n/a — bundle-internal |
| 21 | No question parked "later" | pass | none | n/a — bundle-internal |
| noticed-1 | the upgrade note runs from line 130 to 136; line 135 ends mid-sentence and 136 continues it | corrected: the citations now read 130 – 136; T-8 and T-9 find the note by its first line, not by line number | `files/` check script `note_block()` (Phase 05) | — |

### Traceability

| Source | Scenario(s) | Check(s) |
|---|---|---|
| Brief Goal: folder = `name:` = `audit-<role>` | R-1 | T-2, T-5 |
| Brief Required change 1: `git mv`, keep history | R-1 (renames) | T-5 |
| Brief Required change 2: `name: audit-maturity`, `description` unchanged | R-2 | T-2, T-7 |
| Brief Required change 3: skill paths | R-3 | T-1, T-3, T-8 |
| Brief Required change 4: script folder names | R-4 | T-4, T-8 |
| Brief Required change 5: command | R-5 | T-8, T-10 |
| Brief Required change 6: ARCHITECTURE | R-6 | T-1, T-8 |
| Brief Required change 7: README table and note | R-6 | T-1, T-8, T-9 |
| Brief Required change 8: any other reference (DD-5, DD-9) | R-3 | T-1 |
| Invariant: rubric hash comparability | R-4 | T-4, T-6 |
| Invariant: run layout and ids | R-7 (no other content change) | T-8, T-10 |
| Invariant: `.speccen/` history (DD-1) | R-7 | T-12 |
| Invariant: `/speccen:audit` name and behaviour | R-5 | T-8, T-10 |
| Invariant: no content change beyond names | R-7 | T-8 |
| Out of scope: stale counts | R-7 | T-8 |
| Verification 1 (DD-7) | R-3 | T-1, T-13 |
| Verification 2 – 5 | R-1, R-3, R-4 | T-2, T-3, T-4, T-5 |
| Delivery: one commit, message, no version bump (DD-2, DD-4) | R-8, R-7 | T-11, T-10 |
| DD-10 README note clause | R-6 | T-9 |

No ADR exists. Every requirement has a scenario, every scenario a check, and every specification
item a source in the table above. Each plan phase's Why cites a source (row 8).

Claims
- K-1 (row 2) · the five folders hold 2, 1, 12, 3, 1 files · `for d in skills/audit/0*/; do echo "$d $(find $d -type f | wc -l)"; done` · `00-governing-audit/ 2`, `01-recon/ 1`, `02-dimension-analysis/ 12`, `03-scorecard-review/ 3`, `04-synthesis/ 1` → run 1: confirmed
- K-2 (rows 2, 6) · in the governing skill the old names are exactly on lines 2, 53, 90, 91, 92, 93, 129 · `grep -nE "0[0-4]-(governing-audit|recon|dimension-analysis|scorecard-review|synthesis)|app-maturity-audit" skills/audit/00-governing-audit/SKILL.md | cut -d: -f1 | tr '\n' ' '` · `2 53 90 91 92 93 129` → run 1: confirmed
- K-3 (rows 2, 6) · in the stage skills the old names are exactly on recon 3, 9, 23, 66; dimension analysis 3, 9, 68; scorecard review 3, 14, 33, 85; synthesis 3, 12 · the same pattern over `skills/audit/0[1-4]-*/SKILL.md`, `cut -d: -f1,2` · those 13 file:line pairs → run 1: confirmed
- K-4 (rows 3, 6) · in `compare_scorecards.py` the old names are only on lines 33 and 34 · the same pattern over `skills/audit/03-scorecard-review/scripts/*.py` · 2 lines, both in `compare_scorecards.py`, lines 33 and 34 → run 1: confirmed
- K-5 (row 6) · in `commands/audit.md` the old names are only on lines 9 and 10 · the same pattern over `commands/` · `commands/audit.md:9`, `:10` → run 1: confirmed
- K-6 (row 6) · in `ARCHITECTURE.md` the old audit names are only on lines 278 and 315 · the pattern with `\b` after the `sdd-(…)` group over `ARCHITECTURE.md` · lines 278 and 315 → run 1: confirmed
- K-7 (row 6) · `README.md` holds the old names on 53 – 57 and 136 only, and the upgrade note is lines 130 – 136 · the `\b` pattern over `README.md`; `sed -n '130p;136p' README.md` · lines 53, 54, 55, 56, 57, 136; line 130 starts `> Upgrading a local copy from before the`, line 136 is `` > (`00-governing-audit/` … `04-synthesis/`). `` → run 1: slip — the note starts on line 130 (line 129 is blank); citations corrected in Phase 02 and Phase 04 files and the specification

<a id="delegate-gate-check-iteration-2"></a>
### Delegate gate check — iteration 2 (addendum)

Self-check: done — 1 correction (a scratch copy of the specification still cited `:304`; fixed and re-assembled)

| # | Item | Result | Evidence | Verified |
|---|---|---|---|---|
| 1 | The ADR is reflected in the plan | pass | [phase.md#addendum-iteration-2](./phase.md#addendum-iteration-2) Phase 5 (5.1 – 5.3) | confirmed (run 1) |
| 2 | The phase states a Why with a source | pass | Phase 5 Why cites the ADR and the brief's Delivery; 5.2 Why cites 06/19 | n/a — bundle-internal |
| 3 | Checks adjusted and traced | pass | Check changes: T-8, T-12, T-14 (new); R-6 scenario added; the ADR is the source | n/a — bundle-internal |
| 4 | Specification re-assembled | pass | `specification.html` (2 SVGs parse), `specification.md`; DD-8 row shows the override; Checks: 14 | n/a — bundle-internal |
| 5 | No invented scope | pass | the only new change is the ADR's; `README.md` unchanged per 06/18 | n/a — bundle-internal |

Claims (iteration 2)
- K-8 (row 1) · `6c6187c` is the only commit since `e824b5c` that touches paths outside `.speccen/`, so a fixup rebase replays only bundle commits after it · `git log --format=%h e824b5c..HEAD -- . ':(exclude).speccen'` · exactly `6c6187c` → run 1: confirmed
- K-9 (row 1) · the plan's anchor line exists as described · `sed -n 307p ARCHITECTURE.md` · `` | A specific phase's behaviour | that phase's `skills/sdd/NN-*/SKILL.md` | `` → run 1: confirmed

Error-case run against the current code before the fix (09:19): T-8 and T-14 FAIL, T-12 PASS — the adjusted checks detect the missing fix.
