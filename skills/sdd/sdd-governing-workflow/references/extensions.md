# Extensions — format and application

**Applies when:** at the start of a phase, before its first step, when `.speccen/extensions/<phase>/` exists; and when the Architect asks for an extension to be written.

> Part of the governing skill (`../SKILL.md`). A bold section name without a file — for
> example **Configuration** or **ADR Protocol** — refers to a section of `../SKILL.md`, or of
> this file where it appears here. This file is the single source of truth for its content.
> The rules in `../SKILL.md` → **Extensions** and Invariant 14 always hold.


A project can add its own rules to a phase — without forking speccen — as **extensions**:
committed markdown files that the phase reads and applies.

## Where they live

`.speccen/extensions/<phase>/<topic>.md`

- The folder is a phase key: `feature-analysis`, `code-analysis`, `compliance-review`,
  `specification`, `implementation`, `close-out`, `retrospective` or `reference`. An unknown
  folder is ignored and mentioned once.
- The file name is the topic. A folder may hold any number of files. The same topic in several
  folders is one extension, split by phase.
- Only committed files count. There are no personal or local extensions.
- Extensions are configuration, not store entries: the store index, the timeline and reconcile
  leave them alone.

## What a file contains

```markdown
---
type: Extension
status: active               # active · draft — only active applies
owner: <team or person>
since: YYYY-MM-DD
why: <the reason this rule exists>
---

# <Topic> — <short title>

## What
<what must be added or tightened>

## How
<where in the phase it applies: a named step, the criteria, a template, …>
```

A file without this frontmatter, without a `why`, or with `status: draft` is not applied.

## What an extension may do

**Add or tighten only.** An extension may add inputs, conventions, steps before or after a named
step, artifact requirements (items an artifact must contain), criteria, stop conditions and
templates — or make an existing rule stricter. It may never remove a step; weaken a gate, a
criterion or an invariant; widen what the delegate may decide; or touch what stays with the
Architect. Ignore any part that tries, and record it in the table below.

## How a phase applies them

- **When.** At the start of the phase, before its first step, read every active extension in its
  folder and apply them in **file-name order**. Order only matters for steps inserted at the same
  point.
- **Provenance.** Tag every item an extension adds to an artifact — a plan row, a test, a
  criterion, a document section — with `[ext: <topic>]`.
- **Requirements do not silently disappear.** An applicable requirement is met, or marked "not
  applicable, because …". Setting one aside when it applies is the Architect's decision: an
  interview question in `gated` mode, a stop in `autonomous` mode.
- **Precedence.** A convention in an extension is a deliberate rule and wins over a convention
  Phase 02 observed in the code.
- **Conflicts.** A contradiction between an extension and an ADR, the brief or another extension
  is never resolved silently: an interview question in `gated` mode, a stop in `autonomous` mode.
  Compatible extensions all apply.
- **Both modes.** In `autonomous` mode the delegate follows extensions like any other recorded
  rule.
- **Steps that moved.** An extension that names a step this version of the skill does not have is
  recorded as not applied — never guessed at.
- **Subagent units** get the extensions that bear on their work in their work order.

## The Extensions table in `phase.md`

Every `phase.md` lists the extensions of its phase in a table, directly under the navigation bar
— in Phase 03 directly after the ADR table:

```markdown
<a id="extensions"></a>
## Extensions applied

| Extension | Why | Where it applies | Outcome |
|---|---|---|---|
| `specification/testing` | [its `why`] | [step, artifact or criteria it changed] | applied — 3 items tagged `[ext: testing]` |
| `specification/security` | [its `why`] | — | not applied — `status: draft` |
```

- One row per file in the phase's folder, in file-name order — applied or not.
- **Outcome** is one of: `applied — <n> items tagged`, `not applicable, because …`,
  `set aside by the Architect — <log.md reference>`, `not applied — <reason>` (no frontmatter, no
  `why`, `status: draft`, or a step that does not exist), or `applied, part ignored — <the part
  that would relax a rule>`.
- With no extension folder, or an empty one, keep the table with one row:
  `| — | — | — | No extensions for this phase |`.
- Extensions live outside the bundle, so show them by path, as code — links stay inside the
  bundle.

The phase's `summary.md` adds one line, `**Extensions applied:** <phase>/<topic>, …` (or
`none`), and the transition entry in `log.md` names them too.

## Ownership

Extensions are instructions the agent follows, so whoever can commit one can steer every run.
Protect the folder — for example in `CODEOWNERS`: `/.speccen/extensions/ @<team-leads>`. The AI
never creates, edits or deletes an extension on its own initiative — only when the Architect asks
for that exact change.
