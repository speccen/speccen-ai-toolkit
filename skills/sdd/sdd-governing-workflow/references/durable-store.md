# Durable Store — layout and navigation

**Applies when:** reading the durable store (Phases 02, 03, 07, 08) and before any write to it. Writers also read `durable-store-entries.md`.

> Part of the governing skill (`../SKILL.md`). A bold section name without a file — for
> example **Configuration** or **ADR Protocol** — refers to a section of `../SKILL.md`, or of
> this file where it appears here. This file is the single source of truth for its content.

## Location and layout

Repo-root, dot-prefixed (sorts to the top, beside `.github/`), committed with the code so Git
provides storage, history, branching, and distribution — but the store does not *depend* on
Git (see [durable-store-entries.md](durable-store-entries.md) → Timestamps).

```
.speccen/
├── speccen-config.yaml   # CONFIG · project defaults for every bundle — not a store entry
├── speccen-config.local.yaml # CONFIG · personal, never committed
├── .gitignore            # one line: speccen-config.local.yaml
├── extensions/           # EXTENSIONS · committed project rules, one folder per phase — not store entries
├── index.md              # DURABLE · regenerable root index, groups all kinds, links each entry
├── timeline.md           # DURABLE · regenerable oldest-first projection of the feature nodes
├── decisions/            # DURABLE · ADRs — deliberate forks (prescriptive: "do this")
│   └── <prefix>.<name_snake_case>.md
├── lessons/              # DURABLE · experiential knowledge (descriptive: "X bit us")
│   └── <prefix>.<name_snake_case>.md
├── notes/                # DURABLE · hiccup-resolutions + small informal decisions
│   └── <prefix>.<name_snake_case>.md
├── features/             # DURABLE · feature/refactoring nodes — the time axis (see durable-store-entries.md → Graph model)
│   └── <prefix>.<name_snake_case>/   # one folder per feature node
│       ├── node.md               # the feature node (spine + edges)
│       ├── specification.html    # the Phase 04 intent spec (assembled); graduated at close-out
│       ├── specification.md      # reduced projection of it
│       ├── reference.html        # the Phase 08 outcome reference, if one was produced
│       └── reference.md          # reduced projection of it
└── bundles/              # DISPOSABLE · one folder per workflow run; perishes after merge
    └── <id>/             # {{FOLDER_NAME}} — a bundle (STATE.md, log.md, speccen-config.yaml, phase-NN-.../, adrs/)
```

**Durable vs disposable under one root.** Everything above `bundles/` is the **durable store**
— permanent, committed, the project's memory. `bundles/` holds the **disposable** working
state — one folder per run, perishing after the work ships and its durable residue has
graduated. They share the root so all speccen output is in one predictable place, but they have
opposite lifespans: the store persists, bundles perish. A bundle's id matches the feature node
it graduates into, so `bundles/<id>/` traces to `features/<id>/`.

**Bundles are committed to git — and are deletable.** A bundle is committed while the work is
live, so it travels with the branch, survives machine loss, shows up in PRs, and merges with
the code. Once the work has shipped and its durable residue has graduated, a bundle may be
deleted — a plain `git rm` — because nobody needs the in-flight detail any more; git history
keeps it if anyone ever looks back. "Disposable" means *removable when no longer needed*, not
*kept out of version control*. Everything under `.speccen/` — the durable
store and the bundles alike — is committed.

`index.md` and `timeline.md` are both **regenerable projections** of the entry/feature nodes —
never hand-authored. The nodes are the source of truth; these two files are views of them. They
project the **durable** store only — never the `bundles/` working state.

A **feature is a folder**, not a single file, because it anchors attachments — above all the
Phase 08 **reference** (the feature's durable *outcome*). A decision/lesson/note is still one
file; only feature nodes get a folder.

**Bundle-like in conventions, NOT in lifecycle.** The store adopts the bundle's *conventions*
— YAML frontmatter, a regenerable `index.md`, navigation bars, explicit anchors,
bundle-relative links, one-file-per-entry, never-deleted. It does **not** adopt the bundle's
*lifecycle machinery* — there is **no `STATE.md`, no `log.md`, no bundle config, no phase folders, no
`phase.md`/`summary.md` split**. The store is a permanent *library*, not an in-flight
*process*; there is no workflow state to track. Do not add STATE/log/phase structure here to
"match" the bundle — the absence is deliberate.

## Navigation — single root index + extensive cross-linking

- **Root `index.md`** — the single, **complete** map of the store, regenerable. An index lists
  **everything in the store** — a reader opens it and finds every artifact and where it is,
  with nothing omitted. That means: the other top-level projection (`timeline.md`), the entry
  nodes grouped by kind (one line each: title, status, link), the code-documentation folders,
  and any reconciliation records. If an artifact exists at the store root, the index lists it.
  No per-kind index files.
- **Section order is fixed: Timeline → Features → Decisions → Lessons learned → Notes →
  Documentation → Reconciliation records.** The order follows how a developer digs into the
  history: first the overview of what happened when, then the features themselves, then the
  deliberate decisions behind them, then what was learned along the way, then the small
  informal residue, then the long-lived documentation of what was built, and last the store's
  own maintenance log. Each section goes one level deeper, so a reader stops as soon as they
  have what they need.
- **`timeline.md`** — a second regenerable projection: the feature nodes, oldest-first (see
  [durable-store-entries.md](durable-store-entries.md) → Graph model), listed in `index.md` like everything else.
- **Nav bar** — every entry carries `[Index]` under its H1.
- **Relationship links (typed edges) are the real navigation** — and the structure a future
  tool renders. From any node you can walk the whole graph: up to the rule a decision excepts
  (`Overrides` ↔ `Has exception`), back to the cause (`Triggered by` ↔ `Led to`), along the
  history (`Supersedes` ↔ `Superseded by`), from a feature to what it produced
  (`produced` ↔ `produced-by`) and the components it touched (`touches`), and laterally
  (`see`). All bundle-relative links between the `.md` files. See [durable-store-entries.md](durable-store-entries.md) → **Graph model** for the full
  typed edge vocabulary.

The store's `index.md` lists everything in the store:

```markdown
---
type: Index
---

# <Project> — Durable Store

## Timeline
- [Timeline](./timeline.md) — features & refactorings, oldest-first

## Features
- [<title>](./features/<id>/node.md) — <status>

## Decisions
- [<title>](./decisions/<id>.md) — <status>

## Lessons learned
- [<title>](./lessons/<id>.md) — <status>

## Notes
- [<title>](./notes/<id>.md) — <status>

## Documentation                 (only if any exist)
- [<title>](./documentation/<id>/<name>_documentation.html) — [md](./documentation/<id>/<name>_documentation.md)

## Reconciliation records        (only if any exist)
- [Reconciliation <UTC>](./reconciliation-<UTC>.md)
```

**The Documentation section** lists the output of `code-documentation`: one line per folder in
`.speccen/documentation/`, sorted by `<id>` (oldest first). The title is the H1 of the folder's
`*_documentation.md`. The line links the `.html` deliverable and its `.md` projection; a folder
still in planning has no `.html` yet, so its line links the `.md` only. Documentation is not a
graph node: it has no edges and is not on the timeline, like a reconciliation record. A folder
holding no `*_documentation.md` and no `*_documentation.html` is not listed — reconcile reports
it as structural drift. `code-documentation` upserts its own line in this section when it
writes or revises a document, and only that line; reconcile and Phase 06 close-out regenerate
the whole index, so they stay the safety net.

Omit a section that has no files yet (no Reconciliation section before the first reconcile
run, no Documentation section before the first `code-documentation` run). The index is
**complete**: whatever is at the store root appears here.

## Two tiers and graduation

- **Tier-1 — feature-local**, born in the bundle's `adrs/` (and Phase-05 deviations/learnings).
  Load-bearing inside the workflow; may die with the bundle.
- **Tier-2 — project-level**, the durable store. Permanent.

Knowledge reaches Tier-2 by two paths, **both resolved at Phase 06 close-out** (not
mid-workflow — by close-out every relevant fact is final: decisions, ADRs, what was
implemented, deviations, lessons):

- **Promotion (discretionary)** — a feature-local entry proven project-wide graduates. speccen
  *proposes* candidates on evidence; the Architect disposes. Default: stays local, dies with
  the bundle. Keeps Tier-2 clean and intentional.
- **Override (automatic)** — a bundle ADR that overrides a Tier-2 decision graduates *by
  necessity*, no discretion: a standing rule with an undocumented exception is a broken rule
  (the fence loses its sign). On graduation, both cross-links are written (`Overrides` on the
  new entry, `Has exception` on the Tier-2 rule). Neither is deleted.

A rejected-and-reverted bundle that never reaches close-out takes its overrides with it — and
that is correct: an override only matters if the code shipped, and code ships only through
close-out.

**Escalation (deliberate, later).** A scoped override that proves it should become the new
standard is a *supersession* — a separate, explicit Architect decision that globally replaces
the old Tier-2 rule. Distinct from a scoped override (local exception, parent survives).

**Direct capture.** Knowledge can also be written straight to the store without a bundle —
Architect-initiated, proportional (rule 3), for the between-features small decisions, lessons,
and notes that evaporate fastest. Set `origin: direct`. Direct capture obeys all six entry
rules; it is never the AI filing unprompted.
