# Upgrading the project file

**Applies when:** Session Start Step 0, only when `.speccen/speccen-config.yaml` is not current (its `version` differs from the template's, or a template key is missing).

> Part of the governing skill (`../SKILL.md`). A bold section name without a file — for
> example **Configuration** or **ADR Protocol** — refers to a section of `../SKILL.md`, or of
> this file where it appears here. This file is the single source of truth for its content.

## Upgrading the project file

The project file is the one place a team sees every setting speccen offers, so it must keep up
with the template as speccen gains keys. At every session start (Step 0) the AI compares it with
the project-file template in [`configuration.md`](configuration.md) → Templates (read it now), key by key — every top-level key, every phase entry, every key a phase takes,
every tier under `models`. The file is current when its `version` matches the template's and no
key is missing. If it is not current:

- **Add every missing key**, at the position the template gives it, with the template's comment
  lines for that key — including its line in a shared comment block, such as the per-phase legend
  above `phases:`. Inserting such a line is adding, not changing a comment.
- **An added key keeps the effective setting unchanged**: it gets the value that means what its
  absence meant — `mode: gated`, `stops: ask`, `fixes: 5` and `lock: false` at the top; `inherit` for a
  phase's `mode`, `stops`, `fixes` and `model`; `0` for `prototypes`; `false` for a phase's `lock`; and the built-in
  fallback for a tier under `models`. So a phase's `model` is added as `inherit`, not as the
  template's tier — choosing a tier is the Architect's change to make.
- **Set `version`** to the template's version (add it if missing).
- **Never change anything already there**: not a value (even an invalid one — the fail-safe
  handles it), not a comment, not the order, not a key the template does not know.
- **A newer file is left alone.** A `version` higher than the template's was written by a later
  speccen: change nothing, and say once "the project config is from a newer speccen version".
- **A file that cannot be read** as the YAML subset is not upgraded: it already makes the bundle
  `gated` until it is fixed (see the fail-safe).
- **Only the project file.** The bundle file holds only what differs, and the local files only
  what a person set — neither is ever filled in.

**Example.** A project file written before `stops` and `version` existed — `mode: autonomous`, no
`stops` anywhere — gets these lines, marked `+`, and nothing else, when it is upgraded to version 1:

```yaml
# A bundle overrides them in its own speccen-config.yaml; a person in speccen-config.local.yaml.

+version: 1                   # the template version — speccen adds new keys at session start

# How the workflow leaves a phase:
#   ...
mode: autonomous                                           # kept as it was
+# What the delegate does with a material decision the recorded intent leaves open (autonomous only):
+#   ask      stop and wait for the Architect (default)
+#   proceed  take its own proposed answer, record it as unconfirmed, and put it to the review round
+# Hard stops (new dependency, conflicting ADRs, irreversible action, failed gate or tests) always halt.
+stops: ask
lock: false

# Per phase. "inherit" means: use the mode above, or the session's model.
#   mode        inherit · gated · autonomous
+#   stops       inherit · ask · proceed — autonomous only: see the top-level stops
#   model       ...
phases:
  feature-analysis:
    mode: inherit
+    stops: inherit
    lock: false
  # ... and `stops: inherit` after `mode` in code-analysis, compliance-review, specification
  # and implementation; close-out, retrospective, reference and models are unchanged
```

`stops: ask` is the value absence meant, so the delegate behaves exactly as before; switching to
`proceed` stays the Architect's edit. The Step 0 line reads: "project config upgraded to version 1:
added `version`, `stops`, `stops` on 5 phases".

An upgrade to version 2 also adds `model: inherit` to `specification` and `implementation`, and
sets `version: 2`.

An upgrade to version 3 adds `fixes: 5` at the top and `fixes: inherit` to the five phases that
take `stops`, and sets `version: 3`. An autonomous phase then makes up to five fix attempts; set
`fixes: 1` to keep one.

The upgrade is a change to a committed file: it is announced in one line (Step 0), recorded in the
bundle's `log.md` at the session's first entry, and committed with the next phase-transition
commit.

When the template gains a key, its `version` goes up by one, and the key, its comment and the
value that means its absence are added above.
