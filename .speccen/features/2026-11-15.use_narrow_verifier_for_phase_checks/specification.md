---
type: Specification
phase: "04 — Specification"
status: COMPLETE
description: Reduced projection of specification.html — the narrow gate-check verifier
---

# A narrow verifier for the gate test

[Index](../../bundles/2026-11-15.use_narrow_verifier_for_phase_checks/index.md) · [Specification (full)](./specification.html)

---

Intent specification. The gate-check verifier checks only a short list of claims about the code. The self-check keeps everything inside the bundle.

## Requirements and acceptance scenarios

### R-1 — The split of work

The Gate test SHALL state that the self-check owns everything inside the bundle. It SHALL state that the verifier owns only code and repository claims and never reads the bundle.

- **Scenario: The rule is stated** — WHEN a reader opens the Gate test, THEN the two owners and the "never reads the bundle" rule are stated.

Tested by T-1.

### R-2 — The claim list is built with the rows

The Gate test SHALL tell the delegate to record a row's load-bearing claims in the same step as the row. The list SHALL sit directly under the gate table, one claim per line, in the form `K-<n> (row <N>) · claim · how to check · expected`. A command SHALL be the preferred way to check.

- **Scenario: The list exists at the gate** — WHEN the delegate reaches the gate test, THEN the claim list is already written.
- **Scenario: A claim needs too many calls** — WHEN a claim cannot be settled in one or two tool calls, THEN the delegate splits the claim or drops it.
- **Scenario: Where the list goes** — WHEN the delegate records claims, THEN the list sits directly under the gate table, under Claims.
- **Scenario: Each claim has its form** — WHEN the delegate records a claim, THEN the claim is one line: `K-<n> (row <N>) · claim · how to check · expected`, about the content, not the line number.
- **Scenario: How to check** — WHEN the delegate writes how to check a claim, THEN it is preferably a command whose output settles the claim.
- **Scenario: Same step as the row** — WHEN the delegate writes a row that rests on code or repository evidence, THEN it records that row's claims in the same step.
- **Scenario: A line reference** — WHEN a claim cites a `path:line`, THEN the citation is allowed, and the claim still holds when only the line number moves.

Tested by T-2, T-3.

### R-3 — What goes on the list

The Gate test SHALL put exhaustive claims first and allow at most 3 claims for other rows. It SHALL list every count a conclusion depends on, and only binding convention quotes. It SHALL cap a run at 15 claims.

- **Scenario: A row says "nowhere"** — WHEN a row claims that something holds everywhere, or nowhere, THEN the row carries one whole-scope count or "none found" claim. Spot checks alone never confirm such a row.
- **Scenario: Too many claims qualify** — WHEN more than 15 claims qualify, THEN the 15 whose failure would change a conclusion stay, and the rest read not on list — low risk.
- **Scenario: Other rows** — WHEN a row is not exhaustive, THEN it carries at most 3 claims, the ones its conclusion rests on.
- **Scenario: Counts** — WHEN a conclusion depends on a count, THEN the count is on the list.
- **Scenario: Convention quotes** — WHEN a convention rule is quoted, THEN its quote is on the list only if the rule binds the change.
- **Scenario: A rule the change does not touch** — WHEN a convention rule comes from a technology outside the change, THEN the rule is cited by file. It is not on the list.

Tested by T-4, T-5.

### R-4 — Parallel launch

The Gate test SHALL launch the verifier as soon as the claim list is final, and run the self-check at the same time.

- **Scenario: Both run together** — WHEN the claim list is final, THEN the verifier starts, and the self-check runs beside it.

Tested by T-6.

### R-5 — Two kinds of failure

The Gate test SHALL define slip and wrong, and SHALL treat a slip as no failure.

- **Scenario: A line number is off** — WHEN the content is there but the line number is a little off, THEN the verifier reports slip with the correct value. The delegate corrects the citation. No fix attempt or re-run follows.
- **Scenario: The content is missing** — WHEN the content is not there, THEN the verifier reports wrong, the row fails, and the fix loop applies.
- **Scenario: The verifier is unsure** — WHEN the verifier cannot tell slip from wrong, THEN it reports wrong.
- **Scenario: Where the result goes** — WHEN the verifier returns a result for a claim, THEN the delegate appends the result to that claim line, after →.
- **Scenario: A path or a count is off** — WHEN a path or a count is a little off and the conclusion stands, THEN the verifier reports `slip` with the correct value.
- **Scenario: A value the conclusion depends on** — WHEN a value differs in a way the conclusion depends on, THEN the verifier reports `wrong`.

Tested by T-7.

### R-6 — Hints outside the list

The Gate test SHALL allow at most 2 noticed: lines per run, each answered in a gate-table row.

- **Scenario: A hint affects a conclusion** — WHEN a noticed: line affects a conclusion, THEN it becomes a wrong claim in the next run.
- **Scenario: The verifier stays inside its claims** — WHEN the verifier settles a claim, THEN it reads nothing beyond what settles that claim.
- **Scenario: At most two hints** — WHEN the verifier sees something adjacent that looks wrong, THEN it adds at most 2 `noticed:` lines.
- **Scenario: The answer to a hint** — WHEN the verifier adds a `noticed:` line, THEN the delegate answers it in a `noticed-<n>` row at the foot of the gate table. The answer is corrected, or not relevant, because ….

Tested by T-8.

### R-7 — The verified column

The Gate test SHALL fill the verified column from the claims, and SHALL launch no verifier when no row cites code or repository evidence.

- **Scenario: No code evidence** — WHEN no row cites code or repository evidence, THEN no verifier runs, and the column reads n/a — bundle-internal.
- **Scenario: No subagents** — WHEN the host cannot run subagents, THEN the column reads not run.
- **Scenario: A row with only slips** — WHEN every claim of a row is `confirmed` or `slip` with the citation corrected, THEN the row reads `confirmed (run N)`.
- **Scenario: A row without claims** — WHEN a row has no claim, THEN the row reads `n/a — bundle-internal` when it has no code evidence, or `not on list — low risk` when the cap cut its claims.

Tested by T-9.

### R-8 — Later runs and stops

A later verifier run SHALL re-check only the wrong claims, the claims whose file changed and promoted noticed: lines. After a stop, the Architect SHALL set which claims are re-checked.

- **Scenario: A fix changes one file** — WHEN a fix changes one file, THEN only the claims on that file, the wrong claims and promoted hints are re-checked; slips never.
- **Scenario: A row not re-checked** — WHEN a later run does not re-check a row, THEN the row keeps its last confirmed (run N).
- **Scenario: After a stop** — WHEN a run stops, THEN the Architect's answer sets which claims the next run re-checks. Without that answer, one run follows, and a `wrong` claim stops again.
- **Scenario: One run, every claim** — WHEN the verifier runs after a stop, THEN it reports on every listed claim in that one run.

Tested by T-9.

### R-9 — Unit, work order and worker

The skill SHALL register the verifier as a narrow unit. It SHALL give the verifier its own work order with Claims:, Stop: and a three-value return. It SHALL tell the worker not to read the bundle.

- **Scenario: The main session launches a verifier** — WHEN the main session launches the verifier, THEN it uses the narrow work order; the generic template stays for every other unit.
- **Scenario: The Units row** — WHEN a reader opens the Units table, THEN the verifier row names a narrow unit that settles the listed claims only. The gate decision stays with the main session.
- **Scenario: The work-order fields** — WHEN a reader opens the verifier work order, THEN it has `Unit: gate-check verifier (Phase NN, run N) — NARROW` and `Bundle: [{{FOLDER_NAME}}] — do not read bundle files`. It also has `Claims:`, `Stop:`, `Outputs: none — report only` and the return `confirmed` · `slip` · `wrong`, then at most 2 `noticed:` lines.
- **Scenario: Its place** — WHEN a reader opens Subagent Execution, THEN the verifier work order is a second block directly after the generic template.
- **Scenario: The worker** — WHEN the worker gets a verifier work order, THEN it settles only the listed claims, in one or two tool calls each. It does not read the bundle. It returns one line per claim: `confirmed`, `slip — <correct value>` or `wrong — <actual value>`. Then it adds at most 2 `noticed:` lines.

Tested by T-10, T-11, T-12.

### R-10 — Claim sources per phase

Each of Phases 01 – 05 SHALL name the source of its claims in its Mode behaviour.

- **Scenario: Phase 01** — WHEN Phase 01 reaches its gate, THEN no verifier runs, because the phase has no codebase access.
- **Scenario: Phase 02** — WHEN Phase 02 lists claims, THEN they are binding convention quotes, counts, "none found" claims and the code facts behind pattern or risk conclusions.
- **Scenario: Phase 03** — WHEN Phase 03 lists claims, THEN they are the code facts behind an ADR rationale or a prototype result.
- **Scenario: Phase 04** — WHEN Phase 04 lists claims, THEN they are the plan's anchors in existing code. Every file, symbol and integration point the plan changes or extends exists as described. There is at most one claim per plan step that touches existing code. The traceability rows stay with the self-check.
- **Scenario: Phase 05** — WHEN Phase 05 lists claims, THEN they are a single named test run, a symbol present or a pattern absent. They are never the full suite: the main session runs the full suite itself.
- **Scenario: The pointer** — WHEN a reader opens the Verifier claims bullet of Phases 01 – 05, THEN the bullet ends with (governing skill → Gate test).

Tested by T-13.

### R-11 — Nothing tells the verifier to check every row

No skill and no agent SHALL tell the verifier to check "every row" or "every quote"; the kept rules SHALL stay word for word.

- **Scenario: A search for the old rule** — WHEN a search runs for verifier lines with "every row", "every quote" or "re-open the evidence of every", THEN it finds none.
- **Scenario: The kept rules** — WHEN the six self-check items, the stop triggers, the session-model sentences and the generic template are compared with 92ee62f, THEN they are identical.
- **Scenario: The budget and the log format** — WHEN the fixes budget sentence and the log-line paragraph are compared with 92ee62f, THEN they are identical.
- **Scenario: Files outside the change** — WHEN the Phase 07 skill, `README.md` and `ARCHITECTURE.md` are compared with `92ee62f`, THEN they show no diff.

Tested by T-14, T-15, T-17, T-18.

### R-12 — The version

Both manifests SHALL carry the same new version, set by the CI rule.

- **Scenario: The bump** — WHEN Phase 05 runs on 2026-11-16, THEN plugin.json and marketplace.json read 26.1116.1.

Tested by T-16.

### R-13 — Wording

The inserted text SHALL use short sentences and one rule per bullet.

- **Scenario: A long sentence** — WHEN a sentence in the inserted text has more than 30 words (a code span counts as one word), THEN the check fails.
- **Scenario: A bullet with two rules** — WHEN the main session reads an inserted bullet in Phase 05, THEN it records "one rule" or splits the bullet, by hand.

Tested by T-19.

## Text checks

A script in the bundle's `files/` checks the edited text. The [Test Plan](../../bundles/2026-11-15.use_narrow_verifier_for_phase_checks/phase-04-specification/phase.md#test-plan) states what each check must prove.

- **T-1** — The Gate test states the split: the self-check owns the bundle, and the verifier owns only code and repository claims.
- **T-2** — Claims are recorded in the same step as their row.
- **T-3** — The claim list sits under the gate table, one claim per line, in the stated form.
- **T-4** — Exhaustive claims come first. Other rows carry at most 3 claims. Counts and binding quotes are on the list.
- **T-5** — A run has at most 15 claims. The rest read `not on list — low risk`.
- **T-6** — The verifier starts when the list is final, beside the self-check.
- **T-7** — `slip` and `wrong` are defined. A slip costs no fix attempt and no re-run.
- **T-8** — The verifier reads nothing beyond its claims and adds at most 2 `noticed:` lines.
- **T-9** — The `verified` values, the later-runs rule and the after-a-stop rule are stated.
- **T-10** — The Units row names the narrow verifier and keeps the gate decision in the main session.
- **T-11** — The verifier work order has its fields and sits directly after the generic template.
- **T-12** — The worker bullet states the narrow order, the return format and that the worker does not read the bundle.
- **T-13** — Each of Phases 01 – 05 has its Verifier claims bullet, with its claim source.
- **T-14** — No verifier line says "every row", "every quote" or "re-open the evidence of every".
- **T-15** — The kept passages are identical to `92ee62f`.
- **T-16** — Both manifests carry the same new version.
- **T-17** — The Gate test has one self-check instruction and one `fixes` budget sentence.
- **T-18** — Phase 07, README and ARCHITECTURE show no diff against `92ee62f`.
- **T-19** — No inserted sentence has more than 30 words. Each inserted bullet states one rule.

## Not included

- No change to the `fixes` budget, the stop conditions, the six self-check items or the log format.
- No change to gated mode, Phase 07, README or ARCHITECTURE.
- The verifier stays on the session model.
