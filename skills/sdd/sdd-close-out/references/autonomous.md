# Close-out Phase (06) — autonomous mode

**Applies when:** the effective mode of this phase is `autonomous`. Read it together with
`skills/sdd/sdd-governing-workflow/references/autonomous-execution.md`.

> Part of the `sdd-close-out` skill (`../SKILL.md`). Step numbers, the Quality Criteria and section
> names refer to that file. This file is the single source of truth for its content.

**`autonomous`** (Close-out runs under the bundle `mode`) — Steps 1–5 and 10 apply as written.
Steps 6 to 9 change:

- **Step 6.** Path 1 (overrides), the feature node, the graduated specification and the
  regenerated store index and timeline are mechanical and run as written. Path 2 (discretionary
  promotions) is the Architect's, so do not ask. Write the candidates with their evidence under
  `<a id="graduation-proposal"></a> ## Graduation Proposal` in `{{PHASE_FILE}}` and leave it
  pending. Write nothing discretionary to `.speccen/`.
- **Step 7.** Add to the summary: `**Delegated decisions:** [count] →
  [delegated-decisions.md](../delegated-decisions.md)` and `**Graduation proposal:** pending →
  [detail](./phase.md#graduation-proposal)`.
- **Step 8.** `Pending Architect Action` → `Review the delegated decisions and decide the
  graduation proposal`.
- **Step 9.** Replace the closing message with the end-of-run report described in
  **Autonomous Execution** (`skills/sdd/sdd-governing-workflow/references/autonomous-execution.md` → Transitions and the end of a run). Name the optional passes; do not
  start them. If any delegated decision or gate check exists, recommend the Retrospective.
- **Deciding the proposal later.** When the Architect resumes and decides, put the proposal
  through the review round (`sdd-interview` → The review round), write the approved entries in the entry format
  (`skills/sdd/sdd-governing-workflow/references/durable-store-entries.md` → Entry format), update the feature node's `produced` list and the inverse `produced-by`
  edges, regenerate the store index and timeline, and set `Pending Architect Action` to `none`
  once no review is outstanding.
