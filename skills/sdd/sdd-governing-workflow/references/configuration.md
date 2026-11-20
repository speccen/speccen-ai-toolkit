# Configuration — key reference, templates, local files

**Applies when:** creating `.speccen/speccen-config.yaml` or a bundle's `speccen-config.yaml` (bundle creation); upgrading the project file (with `config-upgrade.md`); before creating or editing any config file at the Architect's request; when the Architect asks what a key does.

> Part of the governing skill (`../SKILL.md`). A bold section name without a file — for
> example **Configuration** or **ADR Protocol** — refers to a section of `../SKILL.md`, or of
> this file where it appears here. This file is the single source of truth for its content.
> The resolution order, locks, fail-safe and ownership rules stay in `../SKILL.md` →
> **Configuration**; nothing here relaxes them.

## Keys

| Key | Values | Meaning |
|---|---|---|
| `version` | a whole number | **Project file only.** The template version the file follows; the current version is `3`. A file without it predates versioning. See [`config-upgrade.md`](config-upgrade.md) |
| `mode` | `gated` · `autonomous` | The default mode at that level |
| `phases.<phase>.mode` | `inherit` · `gated` · `autonomous` | The mode for one phase. `inherit` means no value at this level |
| `stops` | `ask` · `proceed` | `autonomous` only; the default at that level. `ask`: a material decision the basis leaves open is a stop. `proceed`: the delegate takes its own proposed answer and records it for review (Autonomous Execution → Stop conditions) |
| `phases.<phase>.stops` | `inherit` · `ask` · `proceed` | `autonomous` only; the stop policy for one phase. `inherit` means no value at this level |
| `fixes` | `1` – `10` | `autonomous` only; the default at that level. How many fix attempts the delegate makes on a failing gate test before it stops (Autonomous Execution → Gate test). Independent of `stops` |
| `phases.<phase>.fixes` | `inherit` · `1` – `10` | `autonomous` only; the fix budget for one phase. `inherit` means no value at this level |
| `phases.<phase>.model` | `inherit` · `economy` · `balanced` · `premium` | The **tier** for that phase's subagent work (Subagent Execution). `inherit` means the session's model |
| `models.<tier>` | a model name for this host | Maps a tier to a model — the team default in the project file, a person's budget or host in their local file |
| `phases.compliance-review.prototypes` | `0` or more | `autonomous` only: how many prototypes the delegate may build for one material choice before it stops (Phase 03, Step 5a) |
| `lock` | `true` · `false` | **Committed files only.** `true`: no file below it can change anything |
| `phases.<phase>.lock` | `true` · `false` | **Committed files only.** `true`: no file below it can change this phase |

Which phases take which key:
- `mode`: `feature-analysis`, `code-analysis`, `compliance-review`, `specification`,
  `implementation`. A phase's `mode` governs every point inside that phase where the Architect
  decides, including the gate at its end (for `implementation`, the accept). Close-out has no
  exit gate and no `mode` key: it runs under the bundle's effective `mode`.
- `stops`: the same five phases as `mode`. It has no effect in a `gated` phase.
- `fixes`: the same five phases as `mode`. It has no effect in a `gated` phase.
- `model`: `code-analysis`, `compliance-review`, `specification`, `implementation`, `close-out`,
  `retrospective`, `reference` — the phases with subagent units.
- `lock`: any of these eight.

The modes:
- **`gated`** — the phase ends with a stop and the Architect's go signal is required. This is
  the default: the Gate Enforcement table applies unchanged.
- **`autonomous`** — the Architect's delegate takes the Architect's decisions in the phase and
  advances once the phase's gate test passes, stopping where the recorded intent does not decide.
  The protocol is **Autonomous Execution**.

**Tiers** say what the work needs; a person's mapping decides what it costs them. A tier is
mapped per tier: the personal project file first, then the project file, then the built-in
fallback `economy → haiku`, `balanced → sonnet`, `premium → opus` (Claude Code's names).

Later versions add keys under the same structure. Unknown keys are ignored.

## Templates

`.speccen/speccen-config.yaml` — written once, when a bundle is created and the project has none
(`mode` from the Mode answer; `gated` shown), and brought up to date at every session start (see
[`config-upgrade.md`](config-upgrade.md)):

```yaml
# speccen project configuration — committed. The defaults for every bundle in this repository.
# A bundle overrides them in its own speccen-config.yaml; a person in speccen-config.local.yaml.

version: 3                   # the template version — speccen adds new keys at session start

# How the workflow leaves a phase:
#   gated       stop at the end of the phase and wait for the Architect's go
#   autonomous  the Architect's delegate decides, and advances once the gate test passes
mode: gated
# What the delegate does with a material decision the recorded intent leaves open (autonomous only):
#   ask      stop and wait for the Architect (default)
#   proceed  take its own proposed answer, record it as unconfirmed, and put it to the review round
# Hard stops (new dependency, conflicting ADRs, irreversible action, failed gate or tests) always halt.
stops: ask
# How many times the delegate repairs a failing gate test before it stops (autonomous only, 1–10).
# It stops sooner when a repair makes no progress, or would change a conclusion, an ADR
# or what a delegated decision decides.
fixes: 5
lock: false                  # true: no bundle file and no local file can change anything

# Per phase. "inherit" means: use the mode above, or the session's model.
#   mode        inherit · gated · autonomous
#   stops       inherit · ask · proceed — autonomous only: see the top-level stops
#   fixes       inherit · 1 – 10 — autonomous only: see the top-level fixes
#   model       inherit · economy · balanced · premium — the tier for the phase's subagent work
#   prototypes  0 or more — autonomous only: prototypes the delegate may build (Phase 03)
#   lock        true: no bundle file and no local file can change this phase
# Tiers say what the work needs. Each person maps them to models in their local file.
# Decision seats and the gate-test verifier always run on the session's model.
phases:
  feature-analysis:          # 01 — discovery interview
    mode: inherit
    stops: inherit
    fixes: inherit
    lock: false
  code-analysis:             # 02 — evidence reading runs as a subagent
    mode: inherit
    stops: inherit
    fixes: inherit
    model: economy
    lock: false
  compliance-review:         # 03 — ADR interview; optional prototypes run as subagents
    mode: inherit
    stops: inherit
    fixes: inherit
    model: balanced
    prototypes: 0
    lock: false
  specification:             # 04 — the plan and the intent freeze
    mode: inherit
    stops: inherit
    fixes: inherit
    model: economy           # searches
    lock: false
  implementation:            # 05 — the code and the accept
    mode: inherit
    stops: inherit
    fixes: inherit
    model: economy           # searches
    lock: false
  close-out:                 # 06 — the audience documents run as subagents
    model: balanced
    lock: false
  retrospective:             # 07 — optional; the review runs as a subagent
    model: premium
    lock: false
  reference:                 # 08 — optional; gathering and authoring run as a subagent
    model: balanced
    lock: false

# Tier-to-model mapping — the team default, set for Claude Code.
# A person's local file overrides it, per tier, for their own budget or host.
models:
  economy: haiku
  balanced: sonnet
  premium: opus
```

`.speccen/speccen-config.local.yaml` — never created by default; written only when the Architect
asks:

```yaml
# speccen personal project settings — not committed. Set only what you change.

# Override the team's tier mapping for your budget or host — only the tiers you change:
# models:
#   premium: sonnet

# Your personal default for every bundle (optional):
# mode: autonomous
```

`.speccen/.gitignore` — one line, so every personal file is ignored at any depth below `.speccen/`:

```
speccen-config.local.yaml
```

`<bundle>/speccen-config.yaml` — written at bundle creation:

```yaml
# This bundle's overrides of .speccen/speccen-config.yaml — committed. Set only what differs.
mode: gated                  # chosen at session start

# For example:
# phases:
#   specification:
#     mode: gated
#     stops: proceed
#   compliance-review:
#     prototypes: 2
```

`<bundle>/speccen-config.local.yaml` — never created by default; written only when the Architect
asks, with just the setting requested:

```yaml
# Your personal override for this bundle only — not committed. Created only when you ask.
mode: autonomous
```

The bundle's own `.gitignore` holds the same single line, so the bundle stays safe if it is ever
copied out of `.speccen/`.

## Local files and git

`.speccen/.gitignore` and the bundle's own `.gitignore` each hold one line,
`speccen-config.local.yaml`. The auto-commit step never stages a local file and never force-adds
an ignored file. **Before creating a local file**, make sure a `.gitignore` covers it: add the
line if it is missing — the one write to a `.gitignore` allowed after creation. Then confirm with
`git check-ignore -q <path of the local file>` (it works before the file exists; exit code 0
means ignored). If it does not exit 0, do not create the file and tell the Architect why. If git
cannot answer because the folder is not a repository (exit code 128), there is nothing to
commit, so the `.gitignore` line alone is enough.
