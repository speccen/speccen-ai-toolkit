---
type: Specification
phase: "04 — Specification"
status: COMPLETE
description: Reduced Markdown projection of specification.html
---


# Audit skills with `audit-` names

[Index](../index.md) · [State](../STATE.md) · [Log](../log.md) · [HTML](./specification.html)

---

Intent specification. The five audit skills get folder names equal to their skill names, with the `audit-` prefix. Nothing else changes.

- Kind: refactoring
- Mode: autonomous
- Base: `e824b5c` (26.1116.3)
- Requirements: 8
- Checks: 14
- Baseline rubric hash: `212cd4db08e1`

- [What the change builds](#what)
- [Where the skills live (L1)](#context)
- [The files that change (L2)](#parts)
- [The one runtime path (L3)](#runtime)
- [Decisions](#decisions)
- [How it is built](#plan)
- [Requirements & acceptance scenarios](#requirements)
- [Checks](#checks)

<a id="what"></a>
## What the change builds

speccen groups its skills in three folders: `skills/sdd/`, `skills/code/` and `skills/audit/`. Commit `1c41496` gave every sdd skill a folder name equal to its skill name, with the `sdd-` prefix. The code skills follow the same rule. The audit skills do not.

The change moves the five audit folders to `audit-<role>` names. The governing audit skill changes its name from `app-maturity-audit` to `audit-maturity`. Every path to the old folders changes with them. The rubric hash, the audit run layout and the `.speccen/` history stay the same.

The change also repairs the README audit table. The sdd rename pointed that table at `sdd-*` folders that do not exist.

Source: the Architect's brief ([log](../log.md), 2026-11-18 07:58); [Phase 01](../phase-01-feature-analysis/phase.md#feature-description).

<a id="context"></a>
## Where the skills live (L1)

*Diagram:* Every box changes its folder name. Only `audit-maturity` also changes its skill name. Highlighted: changed.

The plugin manifest names the group `./skills/audit/`, not single folders. The manifest does not change ([Phase 02](../phase-02-code-analysis/phase.md#code-analysis)).

<a id="parts"></a>
## The files that change (L2)

| Folder (now → after) | Skill name | Files | Text change |
|---|---|---|---|
| `00-governing-audit/` → `audit-maturity/` | `app-maturity-audit` → `audit-maturity` | 2 | `name:`; 5 paths. `description:` unchanged |
| `01-recon/` → `audit-recon/` | `audit-recon` | 1 | description name; 3 paths |
| `02-dimension-analysis/` → `audit-dimension-analysis/` | `audit-dimension-analysis` | 12 | description name; 2 paths. 11 rubrics unchanged |
| `03-scorecard-review/` → `audit-scorecard-review/` | `audit-scorecard-review` | 3 | description name; 3 paths; 2 folder names in `compare_scorecards.py`. `build_scorecard.py` unchanged |
| `04-synthesis/` → `audit-synthesis/` | `audit-synthesis` | 1 | description name; 1 path |
| `commands/audit.md` | 1 | skill name and path. The command name stays `audit` |
| `ARCHITECTURE.md` | 1 | folder range (:278); path (:315); sdd path (:307, ADR) |
| `README.md` | 1 | audit table (:53 – :57); upgrade note (:130 – :136) |

**The substitution map**

Every text change, except the README upgrade note, is one of these replacements:

| Old | New |
|---|---|
| `00-governing-audit` | `audit-maturity` |
| `01-recon` | `audit-recon` |
| `02-dimension-analysis` | `audit-dimension-analysis` |
| `03-scorecard-review` | `audit-scorecard-review` |
| `04-synthesis` | `audit-synthesis` |
| `app-maturity-audit` | `audit-maturity` |
| `sdd-governing-audit/` … `sdd-synthesis/` (README table only) | `audit-maturity/` … `audit-synthesis/` |

**The new README upgrade note**

The note tells a user with a local copy which old folders to remove. The note now lists the five old audit folders and says that the audit folders have new names ([DD-10](../delegated-decisions.md#dd-10)). The full text is in the [plan](./phase.md#implementation-plan).

<a id="runtime"></a>
## The one runtime path (L3)

The audit scripts stamp each run with a hash of the rubrics and the scorer. Two runs compare like-for-like only when their hashes are equal. `compare_scorecards.py` finds the rubrics through two folder names. These names change. The file names and the bytes do not change, so the hash stays `212cd4db08e1`.

*Diagram:* Only the two folder names change. A wrong name at line 33 drops the rubrics with no error. A wrong name at line 34 stops the script with an error ([Phase 02](../phase-02-code-analysis/phase.md#code-analysis)).

<a id="decisions"></a>
## Decisions

The bundle has one ADR, from the review round. No standing decision in `.speccen/decisions/` governs skill names. The delegate took these decisions from the brief ([delegated decisions](../delegated-decisions.md)):

| Decision | Effect |
|---|---|
| [DD-1](../delegated-decisions.md#dd-1) | No file in `.speccen/` outside this bundle changes. |
| [DD-2](../delegated-decisions.md#dd-2), [DD-4](../delegated-decisions.md#dd-4) | One code commit with the brief's message and no trailer. Bundle commits are separate. |
| [DD-3](../delegated-decisions.md#dd-3) | Push and pull request wait for the Architect. |
| [DD-7](../delegated-decisions.md#dd-7) (material, unconfirmed) | The Verification 1 search gets `\b` after the `sdd-(…)` group, so `sdd-reconcile` does not match. |
| [DD-8](../delegated-decisions.md#dd-8) (overridden) → [ADR](../adrs/2026-11-18.architecture_reading_guide_sdd_path.md#decision) | The Architect overrode DD-8. `ARCHITECTURE.md:307` now names `skills/sdd/sdd-*/SKILL.md`. The fix is part of the one code commit. |
| [DD-9](../delegated-decisions.md#dd-9) | The four stage descriptions change only the governing skill name. |
| [DD-10](../delegated-decisions.md#dd-10) | The README note says that the audit folders have new names. |
| [DD-11](../delegated-decisions.md#dd-11), [DD-12](../delegated-decisions.md#dd-12) | The script check runs in the scratchpad. The checks live in `files/` of the bundle. |

<a id="plan"></a>
## How it is built

- **Move the five folders** with `git mv`. Git then records each file as a rename.

- **Rename the name and the paths** in the five skills and in `compare_scorecards.py`. The host loads and runs these files, so they come first.

- **Update the command and the docs**: `commands/audit.md`, `ARCHITECTURE.md`, `README.md`.

- **Verify and commit**: run the 14 checks, run the scripts end to end, make one commit.

Each step and its reason: [Implementation Plan](./phase.md#implementation-plan).

<a id="requirements"></a>
## Requirements & acceptance scenarios

### Requirement R-1: folder equals name

Each audit skill SHALL live in a folder whose name equals its frontmatter `name:`, with the `audit-` prefix and no number.

- WHEN the folder names under `skills/*/` are compared with their `name:` values
- THEN no skill shows a difference (T-2)

- WHEN the change is compared with `main`
- THEN git shows the five folders as renames, and the 13 files without edits as `R100` (T-5)

### Requirement R-2: governing skill name

The governing audit skill SHALL have the name `audit-maturity` and SHALL keep its `description:` unchanged.

- WHEN `audit-maturity/SKILL.md` is read
- THEN its `name:` is `audit-maturity` (T-2), and its `description:` line equals the line at `e824b5c` (T-7)

### Requirement R-3: no old name remains

No tracked file outside `.speccen/` SHALL name an old audit folder or `app-maturity-audit`, except the README upgrade note.

- WHEN the Verification 1 search with `\b` runs
- THEN every hit is a line of the README upgrade note (T-1)

- WHEN a file names `sdd-reconcile`
- THEN the search does not report the file (DD-7), and `skills/sdd/` is unchanged (T-13)

- WHEN a markdown file cites a `skills/audit/…` path
- THEN the path exists (T-3)

### Requirement R-4: the rubric hash stays comparable

The audit scripts SHALL find the rubrics and the scorer at the new folders, and SHALL compute the same rubric hash as before the change.

- WHEN `stamp` runs on a new run
- THEN `run.json` holds `"rubric_hash": "212cd4db08e1"` (T-4)

- WHEN `build_scorecard.py` and `compare` run after `stamp`
- THEN both exit with code 0, and `trend.md` has no "rubric hash differs" warning against a baseline stamped before the change (T-4)

- WHEN the rubrics and `build_scorecard.py` are compared with `e824b5c`
- THEN each file has the same blob id (T-6)

### Requirement R-5: the command

`/speccen:audit` SHALL keep its name and SHALL load `audit-maturity` from `skills/audit/audit-maturity/SKILL.md`.

- WHEN `commands/audit.md` is compared with `e824b5c`
- THEN the file has the same name, and its text differs only by the substitution map (T-8, T-10)

### Requirement R-6: the docs

`README.md` and `ARCHITECTURE.md` SHALL name the new folders. The README upgrade note SHALL list the five old audit folders for removal.

- WHEN the README upgrade note is read
- THEN the note equals the planned text and no longer says "Keep the audit folders" (T-9)

- WHEN the rest of the README and `ARCHITECTURE.md` are compared with `e824b5c`
- THEN they differ only by the substitution map, and in `ARCHITECTURE.md` by the one sdd path fix (T-8)

- WHEN the `ARCHITECTURE.md` reading guide names where a phase skill lives
- THEN it names `skills/sdd/sdd-*/SKILL.md` (T-14)

### Requirement R-7: a pure rename

The change SHALL alter only names and paths.

- WHEN each modified file is compared with the substitution map applied to its `e824b5c` text
- THEN the texts are equal (T-8)

- WHEN the change set is listed
- THEN the set holds 19 renames and 3 modified files, with nothing in `.claude-plugin/` and no `__pycache__` (T-10), and no file in `.speccen/` outside this bundle (T-12)

### Requirement R-8: delivery

The change SHALL be one commit on `refactor/audit-prefixed-skill-names` with the brief's message and no attribution line.

- WHEN the branch commits are listed
- THEN one commit touches paths outside `.speccen/`, and its message equals the brief's message (T-11)

<a id="checks"></a>
## Checks

The 14 checks T-1 – T-14 are in the [Test Plan](./phase.md#implementation-plan). T-1 – T-3 ran against the planned text in Phase 04 and passed. A broken plan failed T-2.
