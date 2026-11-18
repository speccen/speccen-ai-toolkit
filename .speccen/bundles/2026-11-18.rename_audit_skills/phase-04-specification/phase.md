---
type: Phase
phase: "04 — Specification"
status: COMPLETE
description: Four-phase plan — move the five folders, rename the paths and the name, update command and docs, verify with 13 checks and make one commit
---

<a id="phase-top"></a>
# rename audit skills — Specification

[Index](../index.md) · [State](../STATE.md) · [Log](../log.md)

---

<a id="extensions"></a>
## Extensions applied

| Extension | Why | Where it applies | Outcome |
|---|---|---|---|
| — | — | — | No extensions for this phase |

<a id="interview"></a>
## Interview

Mode: `autonomous` (bundle config); `stops: proceed` (project config). No Implementation Plan
existed (Step 2). Steps 3 checks: the scope is settled (Phase 01, DD-1 – DD-9), no ADR is in scope,
no open question remains, and Phase 02 lists every place to change. The material choice of the
acceptance search was settled in Phase 03 (DD-7). Three choices of form remain; they are
independent: one round.

**Round 1**

| # | Question | Depends on | Proposed | Answer |
|---|---|---|---|---|
| 04/1 | README upgrade note — besides the two edits the brief names (add the five old audit folders to the removal list; drop "Keep the audit folders (…)"), also say in its first sentence that the audit folders were renamed, as `1c41496` did for the sdd folders? | — | yes | delegate: yes — basis: brief Goal "Use `1c41496` as the model for scope and style" (log 07:58); `1c41496` README note names the renamed folders; without the clause a reader who upgraded after the sdd rename would read the note as not for them — [DD-10](../delegated-decisions.md#dd-10) |
| 04/2 | Verification 4 fixture — run the scripts on a synthetic run (11 `dimensions/<dim>/result.json` files) in the session scratchpad, beside a baseline run stamped at `e824b5c`, and commit nothing? | — | yes | delegate: yes — basis: brief Verification 4 "on a throwaway run (in a temp dir, not committed)" (log 07:58); Phase 02 baseline `212cd4db08e1` — [DD-11](../delegated-decisions.md#dd-11) |
| 04/3 | Check script — keep the planned checks T-1 – T-13 as `files/phase-05-text-checks.py` in this bundle, committed with the bundle, never in the code commit? | — | yes | delegate: yes — basis: DD-2 (bundle commits separate from the one code commit); earlier bundles kept the checks in `files/` — [DD-12](../delegated-decisions.md#dd-12) |

No question was answered "later". All three are `not material`.

<a id="implementation-plan"></a>
## Implementation Plan

### Proposed Changes Summary

**Renamed (`git mv`), 5 folders, 19 files:**

| From | To |
|---|---|
| `skills/audit/00-governing-audit/` (2 files) | `skills/audit/audit-maturity/` |
| `skills/audit/01-recon/` (1) | `skills/audit/audit-recon/` |
| `skills/audit/02-dimension-analysis/` (12) | `skills/audit/audit-dimension-analysis/` |
| `skills/audit/03-scorecard-review/` (3) | `skills/audit/audit-scorecard-review/` |
| `skills/audit/04-synthesis/` (1) | `skills/audit/audit-synthesis/` |

**Modified after the move** (name and path text only — the substitution map below):

| File | Lines (at `e824b5c`) | Change |
|---|---|---|
| `skills/audit/audit-maturity/SKILL.md` | :2, :53, :90 – :93, :129 | `name: audit-maturity`; 5 paths |
| `skills/audit/audit-recon/SKILL.md` | :3, :9, :23, :66 | description name (DD-9); 3 paths |
| `skills/audit/audit-dimension-analysis/SKILL.md` | :3, :9, :68 | description name; 2 paths |
| `skills/audit/audit-scorecard-review/SKILL.md` | :3, :14, :33, :85 | description name; 3 paths |
| `skills/audit/audit-synthesis/SKILL.md` | :3, :12 | description name; 1 path |
| `skills/audit/audit-scorecard-review/scripts/compare_scorecards.py` | :33, :34 | two folder names |
| `commands/audit.md` | :9, :10 | skill name; path |
| `ARCHITECTURE.md` | :278, :315 | folder range; path |
| `README.md` | :53 – :57, :130 – :136 | audit table; upgrade note |

**Unchanged (must stay byte-identical):** the 11 rubrics in `references/`, `build_scorecard.py`,
`bundle-conventions.md`, the governing skill's `description:`, everything in `skills/sdd/`,
`skills/code/`, `agents/`, `.claude-plugin/`, `.github/`, and `.speccen/` outside this bundle
(DD-1). No file is created or deleted in the code commit.

**Substitution map** (applied to the modified files; it covers every planned text change except
the README upgrade note, which is replaced as a block):

| Old | New |
|---|---|
| `00-governing-audit` | `audit-maturity` |
| `01-recon` | `audit-recon` |
| `02-dimension-analysis` | `audit-dimension-analysis` |
| `03-scorecard-review` | `audit-scorecard-review` |
| `04-synthesis` | `audit-synthesis` |
| `app-maturity-audit` | `audit-maturity` |
| `sdd-governing-audit/`, `sdd-recon/`, `sdd-dimension-analysis/`, `sdd-scorecard-review/`, `sdd-synthesis/` (README table only) | `audit-maturity/`, `audit-recon/`, `audit-dimension-analysis/`, `audit-scorecard-review/`, `audit-synthesis/` |

The README audit table's governing row then reads
`` | `audit-maturity/` | Governing Audit (`audit-maturity`) | All stages — orchestrator | ``.

**Planned README upgrade note** (replaces `README.md:130-136` as one block — DD-10):

```markdown
> Upgrading a local copy from before the `sdd-` and `audit-` prefixes: the workflow skill folders
> were renamed (`00-governing-workflow/` → `sdd-governing-workflow/`, … `interview/` →
> `sdd-interview/`), and so were the audit skill folders (`00-governing-audit/` →
> `audit-maturity/`, … `04-synthesis/` → `audit-synthesis/`). Remove the old folders from your
> skills directory before you copy the new ones, or both sets load: `00-governing-workflow/`,
> `01-feature-analysis/`, `02-code-analysis/`, `03-compliance-review/`, `04-specification/`,
> `05-implementation/`, `06-close-out/`, `07-retrospective/`, `08-reference/`, `interview/`,
> `reconcile/`, `00-governing-audit/`, `01-recon/`, `02-dimension-analysis/`,
> `03-scorecard-review/` and `04-synthesis/`.
```

**New patterns introduced:** none. **Patterns eliminated:** numeric folder prefixes and the
`app-maturity-audit` name in `skills/audit/`.

### Target-State Execution Flow

The one runtime path that the rename touches — `rubric_hash()` — after the change. Compare with
the [current-state flow](../phase-02-code-analysis/phase.md#code-analysis).

```
          ┌───────────────────────────┐
          │ rubric_hash(run)          │
          └─────────────┬─────────────┘
                        ▼
   ┌───────────────────────────────────────────────┐
   │ files = sorted(SKILLS_ROOT/"audit-dimension-  │  :33  new folder name
   │   analysis"/"references").glob("*.md")        │       → 11 rubrics
   └───────────────────────┬───────────────────────┘
                           ▼
   ┌───────────────────────────────────────────────┐
   │ files.append(SKILLS_ROOT/"audit-scorecard-    │  :34  new folder name
   │   review"/"scripts"/"build_scorecard.py")     │
   └───────────────────────┬───────────────────────┘
                           ▼
                ┌─────────────────────┐
                │ run/weights.json    │
                │ exists?             │
                └───┬─────────────┬───┘
                 yes│             │no
                    ▼             │
        ┌──────────────────────┐  │
        │ append weights.json  │  │
        └──────────┬───────────┘  │
                   ▼              ▼
   ┌───────────────────────────────────────────────┐
   │ for f in files:                               │
   │   h.update(f.name)  (same 12 base names)      │
   │   h.update(f.read_bytes())  (same bytes)      │
   └───────────────────────┬───────────────────────┘
                           ▼
              ┌──────────────────────────┐
              │ return sha256[:12]       │
              │ = 212cd4db08e1 (no       │
              │   weights.json)          │
              └──────────────────────────┘
```

What changed: only the two folder names at :33 – :34. `SKILLS_ROOT` (`parents[2]`) still resolves
to `skills/audit`, the base names and bytes are the same, so the hash is unchanged.

### Strategy Evaluation

One approach: the brief prescribes `git mv` plus text substitution, modelled on `1c41496`. No
alternative is in contention; the choices of form are 04/1 – 04/3, the acceptance search is DD-7.

### Implementation Phases

#### Phase 1: Move the five folders ✅

**Why:** The folders move first with `git mv`, so git records each file as a rename and keeps its
history; the text edits then apply to the files at their new paths. — source: brief Required
change 1 (log 07:58); [Phase 02 Architecture Overview](../phase-02-code-analysis/phase.md#code-analysis)

##### 1.1 Move
- [x] `git mv skills/audit/00-governing-audit skills/audit/audit-maturity`
- [x] `git mv skills/audit/01-recon skills/audit/audit-recon`
- [x] `git mv skills/audit/02-dimension-analysis skills/audit/audit-dimension-analysis`
- [x] `git mv skills/audit/03-scorecard-review skills/audit/audit-scorecard-review`
- [x] `git mv skills/audit/04-synthesis skills/audit/audit-synthesis`

##### 1.2 Build and Validate
- [x] `find skills/audit -type f | wc -l` = 19; no `0[0-4]-*` folder remains under `skills/audit/`
- [x] no `__pycache__` under `skills/audit/` (run Python with `-B` throughout)

#### Phase 2: Rename the name and the paths in the skills and the script ✅

**Why:** The skills and the script are what a host loads and runs; after Phase 1 their paths
point at folders that no longer exist, so they are fixed before the docs. — source: brief
Required changes 2 – 4 and 8 (log 07:58); [Phase 02 restatement inventory](../phase-02-code-analysis/phase.md#code-analysis) groups A, B

##### 2.1 Governing skill
**Why:** the `description:` stays byte-identical — it carries the trigger phrases. — source: brief Required change 2
- [x] `audit-maturity/SKILL.md:2` → `name: audit-maturity`
- [x] `audit-maturity/SKILL.md` :53, :90 – :93, :129 — apply the substitution map

##### 2.2 Stage skills
- [x] `audit-recon/SKILL.md` :3, :9, :23, :66 — apply the map
- [x] `audit-dimension-analysis/SKILL.md` :3, :9, :68 — apply the map
- [x] `audit-scorecard-review/SKILL.md` :3, :14, :33, :85 — apply the map
- [x] `audit-synthesis/SKILL.md` :3, :12 — apply the map

##### 2.3 Script
**Why:** a missed name at :33 silently drops the rubrics from the hash. — source: [Phase 02 Behavioural Analysis](../phase-02-code-analysis/phase.md#code-analysis)
- [x] `compare_scorecards.py:33` → `"audit-dimension-analysis"`; `:34` → `"audit-scorecard-review"`; no other line

##### 2.4 Build and Validate
- [x] T-2, T-6, T-7 pass; T-8 passes for the six files of this phase

#### Phase 3: Update the command and the docs ✅

**Why:** The command is the user's entry to the audit, and the docs tell a reader where the
skills are and what to remove on upgrade; they follow once the skills are final. — source: brief
Required changes 5 – 7 (log 07:58); DD-10

##### 3.1 Command
- [x] `commands/audit.md` :9 – :10 — apply the map (`` `audit-maturity` ``,
      `skills/audit/audit-maturity/SKILL.md`); the file keeps its name and every other line

##### 3.2 ARCHITECTURE
- [x] `ARCHITECTURE.md` :278, :315 — apply the map; `:307` stays as it is (DD-8)

##### 3.3 README
- [x] `README.md:53-57` — apply the map and the README-table map
- [x] `README.md:130-136` — replace with the planned upgrade note, as one block

##### 3.4 Build and Validate
- [x] T-1, T-3, T-8, T-9 pass

#### Phase 4: Verify and commit ✅

**Why:** The brief defines done as Verification 1 – 5 and one commit with its message; the
scripts must be run end to end because a text search cannot see a wrong script path. — source:
brief Verification and Delivery (log 07:58); DD-2, DD-4, DD-11, DD-12

##### 4.1 Check script
- [x] Write `files/phase-05-text-checks.py` (T-1 – T-3, T-5 – T-13; T-4 runs by hand per its row)
- [x] Move test: for T-1, T-8, T-9, mutate one expected text in memory and confirm the check fails

##### 4.2 Scripts end to end (T-4)
- [x] In the scratchpad: write the 11-dimension fixture; `build_scorecard.py` it into the
      baseline run stamped at `e824b5c`; then a second run: `stamp`, `build_scorecard.py`, `compare`

##### 4.3 Commit
**Why:** stage only code paths, so the bundle never enters the code commit. — source: DD-2
- [x] `git add -A skills/audit commands/audit.md ARCHITECTURE.md README.md`
- [x] `git commit` with the brief's message verbatim (DD-4) — no trailer
- [x] T-5, T-10, T-11, T-12, T-13 pass on the commit

##### 4.4 Build and Validate
- [x] full run of `files/phase-05-text-checks.py`: all checks pass

### Risk Mitigation

| Risk | Impact | Mitigation |
|---|---|---|
| A stale folder name in `compare_scorecards.py` makes the hash silently differ | High | T-4 compares the new hash with `212cd4db08e1` and checks the trend has no hash warning; T-8 checks :33 – :34 |
| An edit touches a rubric or `build_scorecard.py` and changes the hash | High | T-6 compares blob ids with `e824b5c`; the substitution map is never applied under `references/` or to `build_scorecard.py` |
| The search over-matches `sdd-reconcile` and hides the real result | Medium | DD-7 `\b`; T-13 checks `skills/sdd/` unchanged |
| An edit beyond names (pure-rename breach) | Medium | T-8: every modified file equals the map applied to its `e824b5c` text |
| Python writes `__pycache__` into `skills/audit/` | Low | `-B` on every run; check in 1.2 and T-10 |
| The host CLI adds an attribution trailer to the code commit | Medium | T-11 reads the commit message back and compares it with the brief |
| Line endings: CRLF on this checkout changes the bytes the hash reads | Low | T-4 runs on the same checkout as the baseline (Phase 02) |

### Test Plan

Markdown skills and two small scripts, no test framework (Phase 02 Test conventions): the checks
are string, git and CLI checks in `files/phase-05-text-checks.py`, each scoped to its place
(lesson `2026-11-11.text_checks_read_their_place`). The error-case and "none found" checks T-1 –
T-3 were run against the planned text in this phase (below; lesson
`2026-11-16.run_error_checks_on_planned_text`).

| # | Target | Type | What must be true |
|---|---|---|---|
| T-1 | old names (Verification 1, DD-7 search) | none-found | every hit is a line of the README upgrade note block; 4 hits |
| T-2 | folder = `name:` (Verification 2) | integration | no mismatch over `skills/*/*/SKILL.md` (18 skills) |
| T-3 | cited `skills/audit/…` paths (Verification 3) | none-found | every path cited in a tracked `.md` outside `.speccen/` exists; 0 missing |
| T-4 | scripts end to end (Verification 4) | integration | `stamp` writes `rubric_hash` = `212cd4db08e1`; `build_scorecard.py` exits 0 and writes `summary.json`, `scorecard.md`; `compare` exits 0 and writes `trend.md`, `history.md`; `trend.md` has no "rubric hash differs" warning against the baseline stamped at `e824b5c` |
| T-5 | renames (Verification 5) | git | `git diff -M --name-status main HEAD -- skills/audit` = 19 `R` lines; 13 are `R100` (11 rubrics, `build_scorecard.py`, `bundle-conventions.md`) |
| T-6 | hash inputs unchanged | git | blob id of each rubric and of `build_scorecard.py` at `e824b5c` (old path) = at `HEAD` (new path) |
| T-7 | governing `description:` unchanged | string | the `description:` line of `audit-maturity/SKILL.md` = that of `00-governing-audit/SKILL.md` at `e824b5c` |
| T-8 | pure rename | string | for the 5 `SKILL.md`, `compare_scorecards.py`, `commands/audit.md`, `ARCHITECTURE.md`, and `README.md` outside the note block: HEAD text = substitution map applied to the `e824b5c` text |
| T-9 | README upgrade note | string | the note block = the planned text, byte for byte (line endings normalised) |
| T-10 | change set | git | outside `.speccen/`: 19 `R` + `M` `README.md`, `ARCHITECTURE.md`, `commands/audit.md`, and nothing else (no `.claude-plugin/`, no `__pycache__`) |
| T-11 | the code commit | git | exactly one commit on the branch touches paths outside `.speccen/`; its message = the brief's message; no `Co-Authored-By` or "Generated with" line |
| T-12 | `.speccen/` history | git | `git diff --name-only main HEAD -- .speccen` lists only this bundle's files |
| T-13 | other skill groups | git | `git diff --quiet main HEAD -- skills/sdd skills/code agents` |

Not tested: the skills' runtime behaviour in a host session (none, because the change edits
paths and names only; T-2, T-3 and T-8 prove the text, and a host loads skills by folder).

**Behaviours to cover, by kind:** error and failure — a stale script folder (T-4 hash, T-8),
an edited hash input (T-6), a stray edit (T-8, T-10); side effects — `__pycache__` (T-10),
version bump (T-10), attribution (T-11); edges — `sdd-reconcile` (DD-7, T-13), the note listing
old names on purpose (T-1, T-9).

**Coverage intent:** every requirement of the specification has at least one check
(Traceability in the summary).

**Run against the planned text (Phase 04):** an in-memory simulation applied the substitution
map and the planned note to the `e824b5c` text (no file written) and ran T-1 – T-3: T-1 4 hits,
0 outside the note; T-2 no mismatch; T-3 19 cited, 0 missing — PASS. A mutated plan (one folder
left out of the map) failed T-2 — the check detects the error. The first simulation run cut the
old note at :135 instead of :136; that was a defect of the simulation, corrected before the
recorded run.

### Deviations Protocol

> "Any deviation from this Implementation Plan during Phase 05 must be:
> 1. Stopped immediately
> 2. Documented in `phase-05-implementation/phase.md` under the `deviations` anchor
> 3. Reviewed by the Architect before implementation continues"

In `autonomous` mode, a deviation within implementation detail is decided and recorded by the
delegate; one that changes an acceptance scenario, the scope or a phase's Why is a stop
(governing skill, stop condition 4).

<a id="outcome"></a>
## Outcome

Selected approach: `git mv` of the five folders, then the substitution map on nine files and the
README note as one block, verified by T-1 – T-13 and committed once with the brief's message.

<a id="open-items"></a>
## Open Items

| # | Item | Settles in |
|---|---|---|
| O-7 | `[DD-7 \| Tighten Verification 1 with \b after the sdd- group?]` — `MATERIAL — unconfirmed` | review round |
| O-8 | `[DD-8 \| ARCHITECTURE.md:307 stale skills/sdd/NN-* path]` — a follow-up outside this change | end-of-run report |
| O-9 | Push and PR wait for the Architect (DD-3) | end of run |
