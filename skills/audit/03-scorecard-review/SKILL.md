---
name: audit-scorecard-review
description: AGGREGATE & REVIEW stage of the Application Maturity Audit. Loaded by the app-maturity-audit governing skill to compute the scorecard from the scored dimensions, regenerate the index, and enforce the human review gate before any audience document is written. Not a standalone entry point.
---

# Audit — AGGREGATE & REVIEW Stage

Turn the scored dimensions into the three headline signals, then hold the gate.

## Step 1 — Compute the scorecard (machine-owned)

Run the scorer:
```bash
python skills/audit/03-scorecard-review/scripts/build_scorecard.py {{AUDIT_FOLDER}}/dimensions --out {{AUDIT_FOLDER}}
```
Custom weights are not a prompt: they exist only if the Architect put a `weights.json` in
`{{AUDIT_FOLDER}}` — then add `--weights {{AUDIT_FOLDER}}/weights.json`. The trend script hashes
that file, so a run scored with custom weights is flagged "not like-for-like" against the others.
It reads every `dimensions/*/result.json` and writes:
- `scorecard.md` (`type: Scorecard`) — the table plus the three signals
- `summary.json` — machine-readable aggregate

The three signals: **weighted average** (overall maturity), **production-readiness gate**
(minimum level among security / testing / reliability), and **modernization pressure** (from
the legacy cluster — architecture / performance / dependency-health / code-quality). A repo
can pass the gate yet carry High pressure — safe to run today, but a growing brake. Use the
script's numbers verbatim; never hand-edit `scorecard.md`.

## Step 1b — Compare with earlier runs

Run the trend script:
```bash
python skills/audit/03-scorecard-review/scripts/compare_scorecards.py compare {{AUDIT_FOLDER}}
```
It writes `trend.md` (movement vs the previous run and vs the baseline; for the baseline run
itself, a "baseline established" note) and regenerates `.speccen/audits/history.md` and
`history.json`. Both are machine-owned; never hand-edit them. Heed any "not like-for-like" warning
(the rubrics changed between runs).

Then read the earlier runs' `detail.md` files and write `{{AUDIT_FOLDER}}/trend-notes.md`
(`type: TrendNotes`): for every dimension whose level moved, cite the changed evidence (a file,
a commit) that explains it — a move with no changed evidence is flagged as possible scoring
noise and re-checked — and list new, resolved and persisting findings per dimension. Skip this
for the baseline run.

## Step 2 — Regenerate the index

Rebuild `index.md` from frontmatter, grouped by type (Bundle Control · Scorecard · Dimensions
lowest-level-first · Audience Documents · ADRs), per bundle-conventions.

## Step 3 — Open the review gate

Set `STATE.md` Stage to `AWAITING ARCHITECT REVIEW`, `Awaiting: architect review of scores`.
Present the scorecard, the trend (`trend.md`, `trend-notes.md`) and the dimension summaries to the
Architect. **Stop here.**

## Step 4 — Review the scores (interview, then the gate question)

**4a — The review interview.** Interview the Architect only on the dimensions that need a
decision — never on all eleven:
- `confidence: low`, or
- flagged in `trend.md` as a level change without changed evidence in `trend-notes.md`, or
- a critical dimension (security, testing, reliability) that sets the readiness gate.

Put them as one `interview` round (`skills/sdd/interview/SKILL.md`, "Outside a bundle"; reference
`audit-gate/<n>`), one question per dimension, with the proposed answer `keep <level>` — or
`change to <level>` where the trend flagged it as noise. The Architect's answers are their own
words: log them verbatim in `log.md` and record the `## Interview` table in `trend-notes.md`.
Dimensions with nothing to decide are not asked.

**4b — Apply corrections (loop).** If the Architect corrects a level, treat it as authoritative:
1. Update that dimension's `result.json` and `detail.md` to reflect the corrected level and
   the reason.
2. Re-run the scorer and the trend script (Steps 1 and 1b) and regenerate `index.md` (Step 2).
3. Log the correction verbatim in `log.md`.

**4c — The gate question.** When the interview is done, ask with one `AskUserQuestion` call,
header `Gate`: `Proceed to synthesis`, `Apply more corrections`. Stay at the gate until the
Architect answers `Proceed to synthesis` (or says it in words).

## Step 5 — Release

On an explicit go-signal (`Proceed to synthesis`, or "generate the documents" / "proceed to synthesis"), set Stage to
`SYNTHESIS`, log the signal, and return control to the governing skill, which loads
`skills/audit/04-synthesis/SKILL.md`. Never advance without the signal.
