---
type: Log
---

# Workflow History

## 2026-11-15

- **21:29 — FEATURE ANALYSIS → CODE ANALYSIS** — delegate gate check passed in verifier run 3 (fix attempts 2 of 5; failed rows per run 3 → 1 → 0) ([summary](./phase-01-feature-analysis/summary.md#delegate-gate-check)) · mode: autonomous (bundle config) · extensions: none
- **21:29 — FEATURE ANALYSIS** — verifier run 3: rows 1–8, 10, 11, 16, 17 confirmed; gate test passed
- **21:27 — FEATURE ANALYSIS subagent** — gate-check verifier (Phase 01, run 3) · model: session model → opus (Gate test: verifier runs on the session model)
- **21:26 — FEATURE ANALYSIS** — fix attempt 2 of 5: run 2 failed rows 7 — H-4 now quotes brief rule 2 word for word; every quote in phase.md, delegated-decisions.md and summary.md scanned against log.md (no other mismatch); Domain Context no longer says who measured the case (verifier note)
- **21:25 — FEATURE ANALYSIS** — verifier run 2: row 7 not confirmed (H-4 quote not word for word); rows 1–6, 8, 10–12, 15–17 confirmed
- **21:23 — FEATURE ANALYSIS subagent** — gate-check verifier (Phase 01, run 2) · model: session model → opus (Gate test: verifier runs on the session model)
- **21:22 — FEATURE ANALYSIS** — fix attempt 1 of 5: run 1 failed rows 4, 5, 16 — Out of scope bullets now cite their own source (row 4); `n/a — bundle-internal` definition follows rule 9 (row 5); DD-8 question asks when the request is done (row 16); also H-2 reworded as a statement about the request; self-check line filled
- **21:21 — FEATURE ANALYSIS** — verifier run 1: rows 4, 5, 16 not confirmed (attribution and wording); all other rows confirmed
- **21:18 — FEATURE ANALYSIS subagent** — gate-check verifier (Phase 01, run 1) · model: session model → opus (Gate test: verifier runs on the session model)
- **21:18 — FEATURE ANALYSIS** — gate test: self-check done — 1 correction (DD-6 basis quote now matches the brief word for word)
- **21:16 — FEATURE ANALYSIS** — delegate interview: round 1 01/1 – 01/7, round 2 01/8; answered under delegation (autonomous) from the decision basis — 01/1 refactoring, provisional (DD-1); 01/2 repository source at HEAD (DD-2); 01/3 measured case accepted as stated (DD-3); 01/4 – 01/8 working hypotheses H-5, H-2, H-3, H-4 and the done-when (DD-4 – DD-8)
- **21:14 — FEATURE ANALYSIS** — specification: 

  ```markdown
  # Task: make the speccen gate-check verifier narrow and fast

  ## Problem
  In `autonomous` mode, every phase ends with a gate test. A verifier subagent (`speccen-worker`) re-opens the evidence of every row of `## Delegate gate check`. Nothing limits what it re-reads, so it repeats most of the phase's research.

  Measured case (Phase 02): one run took about 13 minutes, 58 tool calls and about 177k tokens. It found only line-number slips, count slips and one misattributed quote. No conclusion changed. A narrow run of 7 listed claims took 2 min 48 s and 9 tool calls, and still caught a real count error.

  Most of the time goes to three things:
  1. **Breadth:** the verifier re-checks everything.
  2. **Order:** the verifier only starts after the self-check is done.
  3. **Re-runs:** a line-number slip fails a row, which costs a fix attempt and another verifier run.

  ## Goal
  Keep an independent check of claims about the code and the repository, because the delegate reviews its own work. Target: one run of at most about 5 minutes, and re-runs only when a conclusion was at stake.

  ## Rules (write them into the skill)

  ### 1. Who checks what
  - The existing self-check owns everything inside the bundle. The verifier owns only claims about the code and the repository, and never reads the bundle.

  ### 2. Build the claim list as you go
  - When the delegate writes a gate-table row that rests on code or repository evidence, it records that row's load-bearing claims in the same step.
  - At the gate the list already exists.

  ### 3. What a claim is
  - A claim is one line: `id · claim · how to check · expected`.
  - **How to check** is preferably a command whose output settles it.
  - A `path:line` is allowed, but the claim is about the **content**, not the line number.
  - Each claim must be settled in one or two tool calls. If it can't be, split it or drop it.

  ### 4. What goes on the list
  - **Exhaustive claims first.** A row that claims something holds everywhere, or nowhere, carries one claim that covers the whole scope: a count or a "none found" check. Example: `grep -rn 'new HttpClient(' src | wc -l` = 0. Spot checks never confirm such a row on their own.
  - **Other rows:** at most 3 claims, the ones the row's conclusion rests on.
  - Every count that a conclusion depends on.
  - Verbatim quotes only of convention rules that bind the change. A rule from a technology the change doesn't touch is cited by file and is not on the list.
  - **Hard cap: 15 claims per run.** If more qualify, keep the 15 whose failure would change a conclusion, and mark the rest `not on list — low risk`.

  ### 5. Claim sources per phase
  - **01:** none, because the phase has no codebase access. No verifier run.
  - **02:** convention quotes that bind the change, counts, "none found" claims and the code facts behind each pattern or risk conclusion.
  - **03:** code facts behind an ADR's rationale or a prototype's result.
  - **04:** the plan's anchors in the existing code. Every file, symbol and integration point the plan changes or extends exists as described. At most one claim per plan step that touches existing code. Traceability rows stay with the self-check.
  - **05:** the implementation does what the row says: a single named test run, a symbol present, a pattern absent. Never the full suite; the main session runs that itself.

  ### 6. Run in parallel
  - Launch the verifier as soon as the claim list is final, and run the self-check at the same time.
  - This is safe: the self-check edits only bundle files, and the verifier reads only code and the repository.

  ### 7. Two kinds of failure
  - **`slip`:** the content is there, but the line number, path or count is a little off, and the conclusion stands. The verifier gives the correct value. The delegate corrects the citation. It is **not** a failed row, uses no fix attempt and triggers no re-run.
  - **`wrong`:** the content isn't there, or the value differs in a way the conclusion depends on. The row has failed, and the normal fix loop applies.
  - If the verifier is unsure which kind it is, it reports `wrong`.

  ### 8. Hints outside the list
  - The verifier doesn't read beyond what settles its claims.
  - It may add at most 2 `noticed:` lines about something adjacent that looks wrong.
  - The delegate answers each one in the gate table: `corrected`, or `not relevant, because …`.
  - If a `noticed:` line affects a conclusion, it becomes a `wrong` claim in the next run.

  ### 9. When there is no verifier run
  - If no row cites code or repository evidence, no verifier is launched, and the `verified` column reads `n/a — bundle-internal`.
  - Without subagent support, the column reads `not run`, as it does today.

  ### 10. Later runs
  - Re-check only the `wrong` claims, the claims whose file changed during the fix, and any `noticed:` lines that were promoted to claims.
  - Slips are never re-checked.
  - Rows not re-checked keep their `confirmed (run N)`.

  ### 11. Filling the gate table
  - A row is `confirmed (run N)` when all of its claims are `confirmed` or `slip` (after the citation is corrected).
  - Rows without claims are `n/a — bundle-internal` or `not on list — low risk`.

  ### 12. Unchanged
  The verifier stays on the session model. The `fixes` budget, the stop conditions, the six self-check items and the log line format stay as they are.

  ## Work-order template (verifier unit)

  ```markdown
  **speccen work order**
  - Unit: gate-check verifier (Phase NN, run N) — NARROW
  - Bundle: [{{FOLDER_NAME}}] — do not read bundle files
  - Claims: [≤15, numbered — id · claim · how to check · expected]
  - Stop: once every listed claim is settled; one or two tool calls per claim; batch independent checks
  - Outputs: none — report only
  - Return: one line per claim — `confirmed` · `slip — <correct value>` · `wrong — <actual value>`; then at most 2 `noticed:` lines
  ```

  ## Files to change
  1. `skills/sdd/00-governing-workflow/SKILL.md`:
     - **Autonomous Execution → Gate test:** replace "re-open the evidence of every row" with rules 1–4 and 6–11, and rewrite the later-runs rule.
     - **Subagent Execution → Units:** the verifier row.
     - **Subagent Execution → The worker and the work order:** the template above.
  2. `agents/speccen-worker.md`: add one bullet saying a verifier work order is narrow, follows the return format and doesn't read the bundle.
  3. Phase skills `01`–`05`, **Mode behaviour** only: add that phase's line from rule 5, and refer to the governing skill for the rest.
  4. Bump the version in `.claude-plugin/plugin.json` and `marketplace.json`. The repo has no changelog.

  ## Acceptance
  - The governing skill states:
    - the split, the claim list with its cap, and exhaustive claims first;
    - the parallel launch, `slip` vs. `wrong`, and the handling of `noticed:` lines;
    - the `n/a` case and the later-runs rule.
  - Each phase skill 01–05 names its claim source.
  - The template has `Claims:`, `Stop:` and the three-value return.
  - No skill tells the verifier to check "every row" or "every quote".
  - Wording: short sentences, one rule per bullet.
  ```
- **21:12 — FEATURE ANALYSIS** — feature name: use narrow verifier for phase checks
- **21:10 — FEATURE ANALYSIS** — /speccen:start — session-start answers: Id prefix "2026-11-15 (Recommended)"; Name "I'll type it" (no name typed); Work kind "refactoring"; Mode "autonomous (Recommended)"
