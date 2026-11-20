# Compliance & Review Phase (03) — autonomous mode

**Applies when:** the effective mode of this phase is `autonomous`. Read it together with
`skills/sdd/sdd-governing-workflow/references/autonomous-execution.md`.

> Part of the `sdd-compliance-review` skill (`../SKILL.md`). Step numbers, the Quality Criteria and section
> names refer to that file. This file is the single source of truth for its content.

**`autonomous`** — the delegate takes the Architect's decisions in this phase:

- **Iteration.** Process every ADR in `adrs/` — those are the Architect's; you decide none. Run
  at most **two** iterations. If the Definition of Ready is still not met after the second, stop.
- **Prototypes.** If `phases.compliance-review.prototypes` is `n > 0` and a material choice has two
  or more viable approaches that the basis does not decide, build up to `n` prototypes (Step 5a),
  then stop with the comparison table — the choice is the Architect's. With `0`, the default,
  stop at the choice as before. Prototypes do not count against the two-iteration limit.
- **Definition of Ready.** Evaluate every criterion with cited evidence. The last criterion
  ("the Architect or its delegate has signalled readiness") is met by your recorded readiness
  decision and its basis. Also check that no `status: PENDING` placeholder ADR remains: a
  placeholder blocks the transition, exactly as Step 6 says.
- **Open questions and undecided ADRs.** Work through them with the interview (Step 6, Handling
  unresolved open questions): answer what the basis decides, and record each answer as a
  delegated decision linked to its question. Material ones the basis does not decide go to the
  Architect as one stop round. One still undecided after that — answered "later" — becomes the
  placeholder ADR described in Step 6 (`status: PENDING`, which blocks exactly as it does today). When the Architect
  answers, they either edit the placeholder to `DECIDED` or ask you to record it — and then only
  per **Scribing a stated decision** (`skills/sdd/sdd-governing-workflow/references/adr-scribing.md`). An answer that states no decision leaves the placeholder
  `PENDING` and the stop stands.
- **Conflicts.** An ADR that conflicts with another ADR or with the brief is a stop. So is an
  analysis that would require overriding a standing (Tier-2) ADR — that override is the
  Architect's ADR to write.
- **End.** Write `## Delegate gate check` into `{{SUMMARY_FILE}}`, then transition. Send no
  Step 9 message.
- **Verifier claims.** The code facts behind an ADR's rationale or a prototype's result
  (`skills/sdd/sdd-governing-workflow/references/autonomous-execution.md` → Gate test).
- Decision basis, stop conditions and records: **Autonomous Execution** (`skills/sdd/sdd-governing-workflow/references/autonomous-execution.md`).
