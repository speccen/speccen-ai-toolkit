# GitHub issue #25 — Gate test: a fix budget for autonomous phases

Source: https://github.com/speccen/speccen-ai-toolkit/issues/25 · state: OPEN · created 2026-11-10T12:35:47Z ·
no comments at capture (2026-11-11). The issue body is HTML; it is transcribed here to Markdown
with its text unchanged. Section 5 is empty in the issue: the body ends at its heading.

---

## 1. Problem

In an `autonomous` phase, the delegate runs the gate test, and a verifier re-checks every row. Today the delegate may fix a failing gate **once**. If a re-checked row still fails, the run stops (stop condition 5, `SKILL.md:1212`; gate test, `:1176-1179`).

In practice, most second-run failures are **precision faults**, not wrong conclusions: a line number one off, a count that differs between two files, "lesson" instead of "note", a quote not word for word. The Architect's answer to such a stop is almost always "yes, go ahead". The stop costs the Architect's attention and does not add a decision.

**Evidence** — a refactoring bundle in a client project (`autonomous`, `stops: ask`):

| Phase | Run 1 | Run 2 | Run 3 | Run 4 | Architect's answer to the stop |
| -- | -- | -- | -- | -- | -- |
| 01 Feature Analysis | 4 rows failed | 2 failed → stop | 2 failed | 0 ✓ | "yes" to both questions |
| 02 Code Analysis | 7 rows failed | 5 failed → stop | failed → stop |   | "yes, go ahead" |

Phase 02, run 2: the 5 failing rows were a subset of run 1's 7; the run was converging. The failures (the exact wording of a tool's error handling, a line number one off, a count of 3 in one file and 4 in another, a store "note" called a "lesson") changed no Phase 02 conclusion.

**Related finding** — the speccen retrospective of `2026-11-05.use_cheaper_subagent_to_work` (`phase-07-retrospective/retrospective.md`, "B2 governs only the second verifier run; runs after a stop are unruled and unbounded"): Phase 04 row 12 failed on runs 1–5 through four stop rounds, each one the same question. 26.1108.1 added the post-stop re-check scope, but still sets **no bound and no progress rule**.

Two separate wishes are mixed today:

- `stops` answers: *may the delegate decide a material question for the Architect?*
- The fix budget answers: *how often may the delegate repair its own work before it asks for help?*

The second is not a decision for the Architect. It should not depend on `stops`.

## 2. Change

A new config key `fixes`: the number of fix attempts the delegate may make on a failing gate test. It applies to **every `autonomous` phase**, with `stops: ask` and with `stops: proceed`. It has no effect in a `gated` phase (the Architect is the gate there).

Three guards keep the budget safe:

1. **Progress.** Each re-check must fail **fewer rows** than the run before. If not, stop now — the delegate is going round in circles, not converging.
2. **Conclusions.** If a fix would change a phase conclusion, a delegated decision or an ADR, stop now. The budget is for repairing the record, not for changing what it concludes.
3. **Ceiling.** At most `3` fix attempts. Each verifier run is on the session model; more runs cost more than one stop round.

### 2.1 Governing skill → Autonomous Execution → Gate test (`:1176-1182`)

```diff
-- If any item fails, fix it once and run the test again. The second verifier run re-checks
-  (a) every row that failed, and (b) every row whose evidence is in a file you changed during
-  the fix. Rows it does not re-check keep their `confirmed` value and say `confirmed (run 1)`.
-  If a re-checked row still fails, stop.
-- After a stop, the Architect's answer sets which rows the next verifier run re-checks; rows it
-  does not re-check keep their last `confirmed (run N)`. A verifier that fails a row lists every
-  rule breach it finds in that row at once.
+- If any item fails, fix it and run the test again — up to the phase's effective `fixes`
+  attempts (Configuration; default `1`). Each later verifier run re-checks (a) every row that
+  failed in the run before, and (b) every row whose evidence is in a file you changed during
+  the fix. Rows it does not re-check keep their last `confirmed (run N)`.
+- Stop (stop condition 5) when a re-checked row still fails and:
+  1. the budget is used up; or
+  2. the run fails **as many rows or more** than the run before — no progress; or
+  3. the fix you would make next changes a phase conclusion, a delegated decision or an ADR.
+  Log each attempt as `fix attempt <n> of <fixes>: run <N> failed rows <list>`.
+- After a stop, the Architect's answer sets which rows the next verifier run re-checks, and
+  whether further fix attempts are allowed; without that, one run, and a failing row stops
+  again. Rows it does not re-check keep their last `confirmed (run N)`. A verifier that fails a
+  row lists every rule breach it finds in that row at once.
```

### 2.2 Governing skill → Stop conditions (`:1212`)

```diff
-5. a gate test still fails after one fix attempt;
+5. a gate test still fails after the fix budget, makes no progress, or needs a fix that changes
+   a conclusion, a delegated decision or an ADR (Gate test);
```

### 2.3 Governing skill → Configuration → Keys (`:694-698`)

```diff
 | `phases.<phase>.stops` | `inherit` · `ask` · `proceed` | `autonomous` only; the stop policy for one phase. `inherit` means no value at this level |
+| `fixes` | `1` · `2` · `3` | `autonomous` only; the default at that level. How many fix attempts the delegate makes on a failing gate test before it stops (Autonomous Execution → Gate test). Independent of `stops` |
+| `phases.<phase>.fixes` | `inherit` · `1` · `2` · `3` | `autonomous` only; the fix budget for one phase. `inherit` means no value at this level |
```

"Which phases take which key" — add:

```diff
 - `stops`: the same five phases as `mode`. It has no effect in a `gated` phase.
+- `fixes`: the same five phases as `mode`. It has no effect in a `gated` phase.
```

### 2.4 Template (`SKILL.md:741-790` and `README.md:245-290`)

```diff
-version: 2                   # the template version — speccen adds new keys at session start
+version: 3                   # the template version — speccen adds new keys at session start
 ...
 # Hard stops (new dependency, conflicting ADRs, irreversible action, failed gate or tests) always halt.
 stops: ask
+# How many times the delegate repairs a failing gate test before it stops (autonomous only, 1–3).
+# It stops sooner when a repair makes no progress or would change a conclusion.
+fixes: 1
 lock: false
 ...
 #   stops       inherit · ask · proceed — autonomous only: see the top-level stops
+#   fixes       inherit · 1 · 2 · 3 — autonomous only: see the top-level fixes
 ...
   feature-analysis:
     mode: inherit
     stops: inherit
+    fixes: inherit
     lock: false
   # ... and `fixes: inherit` after `stops` in code-analysis, compliance-review, specification
   # and implementation
```

### 2.5 Upgrading the project file (`:857-861`, `:902-905`)

```diff
-  absence meant — `mode: gated`, `stops: ask` and `lock: false` at the top; `inherit` for a phase's
-  `mode`, `stops` and `model`; `0` for `prototypes`; ...
+  absence meant — `mode: gated`, `stops: ask`, `fixes: 1` and `lock: false` at the top; `inherit`
+  for a phase's `mode`, `stops`, `fixes` and `model`; `0` for `prototypes`; ...
 ...
 An upgrade to version 2 also adds `model: inherit` to `specification` and `implementation`, and
 sets `version: 2`.
+
+An upgrade to version 3 adds `fixes: 1` at the top and `fixes: inherit` to the five phases that
+take `stops`, and sets `version: 3`. Behaviour is unchanged until the Architect raises `fixes`.
```

### 2.6 Effective settings and fail-safe (`:925-941`)

```diff
-`inherit` counts as no value. The other per-phase keys (`stops`, `model`, `prototypes`) resolve the same
-way at phase level, then fall back to their defaults (`ask`, `inherit`, `0`).
+`inherit` counts as no value. The other per-phase keys (`stops`, `fixes`, `model`, `prototypes`) resolve
+the same way at phase level, then fall back to their defaults (`ask`, `1`, `inherit`, `0`).
 ...
 - A `prototypes` value that is not a whole number of `0` or more counts as `0`.
+- A `fixes` value that is not `1`, `2` or `3` counts as `1`.
```

A project `lock` stops a bundle or local file from raising `fixes`, as for every other key.

## 3. Effect

- **Unchanged by default.** Absence and the upgrade both mean `fixes: 1`: today's behaviour.
- **With `fixes: 3`**, the Phase 02 run above would have gone on after run 2 (5 < 7, precision faults only) instead of stopping. A run that does not converge still stops at once (guard 1).
- A stop now means one of three things: a decision is the Architect's (conditions 1–4, 6–8), the delegate could not repair its own work within the budget, or a repair would change a conclusion. It never means "please confirm I may fix a line number".
- Cost: at most `fixes + 1` verifier runs per gate on the session model. Each later run re-checks only failed rows and rows citing a changed file.

## 4. Rejected alternatives

- **Tie the budget to `stops: proceed`.** `proceed` removes only stop condition 1; conditions 2–8 "mean the basis is broken, or the action is not yours to take" (`:1249`). Mixing the two keys would punish an Architect who wants `ask` for decisions with stops for typos.
- **Unbounded retries.** The 2026-11-05 bundle shows one row failing five runs in a row; without a ceiling and a progress rule this becomes a costly loop.
- **Let the verifier ignore precision faults.** That weakens the gate; evidence that does not show what the row claims has not passed (`:1183-1184`).

## 5. Decisions for the plugin Architect

*(empty in the issue)*
