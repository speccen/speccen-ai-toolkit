# Bundle creation — New Session Protocol

**Applies when:** Session Start Step 2 finds no `{{FOLDER_NAME}}/STATE.md` — a new bundle.

> Part of the governing skill (`../SKILL.md`). A bold section name without a file — for
> example **Configuration** or **ADR Protocol** — refers to a section of `../SKILL.md`, or of
> this file where it appears here. This file is the single source of truth for its content.

## New Session Protocol

1. Take the Architect's **description of the request** as given — including any specifics (a
   class name, a pattern, a business capability, a service contract, a domain name). Do not
   ask for more here: in `gated` mode, Phase 01's interview clears up what the description
   leaves open (Phase 01, Step 2a).
2. Only if no description was given at all, ask for one — in a single plain question.
3. Create the bundle skeleton in `{{FOLDER_NAME}}`:
   - `STATE.md` and `log.md` from the templates below; `index.md` follows in step 4
   - `speccen-config.yaml` — the bundle's overrides, from its template in
     [`configuration.md`](configuration.md) → Templates, with `mode` from the Mode answer — and
     `.gitignore` (the single line `speccen-config.local.yaml`); never a local config file
   - if the project has no `.speccen/speccen-config.yaml` yet: that file from its template in
     [`configuration.md`](configuration.md) → Templates, with `mode` from the Mode answer, and
     `.speccen/.gitignore` (the single line `speccen-config.local.yaml`, added if that file
     exists without it)
   - `phase-01-feature-analysis/` with `phase.md` and `summary.md` stubs (frontmatter and
     navigation bar per **Bundle & File Naming Conventions**)
   - `adrs/` (empty)
   - `files/` with an empty `.gitkeep`, so the folder is committed and pushed even while it
     holds nothing else
4. Set `STATE.md` to register `FEATURE ANALYSIS PHASE` / `IN PROGRESS`. Then generate `index.md`
   from the skeleton (see **`index.md`**): it lists the Bundle Control files and the Phase 01 stubs.
5. Read the **Feature Analysis skill**: `skills/sdd/sdd-feature-analysis/SKILL.md`
6. Execute Phase 01 under the governance of that skill.

## STATE.md template

```markdown
---
type: State
---

# Workflow State

| Field | Value |
|---|---|
| Current Phase | FEATURE ANALYSIS PHASE |
| Current Phase Folder | phase-01-feature-analysis |
| Phase Status | IN PROGRESS |
| Last Updated | YYYY-MM-DD |
| Pending Architect Action | none |
```

## log.md template

```markdown
---
type: Log
---

# Workflow History
```
