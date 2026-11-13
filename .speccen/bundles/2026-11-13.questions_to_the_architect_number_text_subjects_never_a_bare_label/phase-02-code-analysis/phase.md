---
type: Phase
phase: "02 — Code Analysis"
status: COMPLETE
description: The skills give items labels but nowhere ask that the item's text travel with the label; the brief's edits fit, and several Architect-facing places the brief does not list also name items by label
---

<a id="phase-top"></a>
# Questions to the Architect: [number | text] subjects, never a bare label — Code Analysis

[Index](../index.md) · [State](../STATE.md) · [Log](../log.md)

---

<a id="extensions"></a>
## Extensions applied

| Extension | Why | Where it applies | Outcome |
|---|---|---|---|
| — | — | — | No extensions for this phase (`.speccen/extensions/` does not exist) |

<a id="code-analysis"></a>
## Code Analysis

The "code" of speccen is the text of its skills. Every reference below is `path:line` at commit
`6ffc99e` (branch `feature/questions-to-the-architect-subjects`; the skills are unchanged since
`d2636cb` on `main`).
Earlier bundles are cited by their working-tree path: the bundle
`.speccen/bundles/2026-11-12.set_allowed_budget_for_autonomous_phases/` is named
`25.set_allowed_budget_for_autonomous_phases` at `6ffc99e`; it was renamed outside this session
(`log.md`, 06:30).

### Architecture Overview

- **Position.** speccen is a Claude Code plugin. Its behaviour is the text the AI loads:
  `skills/sdd/00-governing-workflow/SKILL.md` (2262 lines) governs the workflow and holds every
  cross-phase rule; eight phase skills (`skills/sdd/01-…` to `08-…`); two shared skills,
  `skills/sdd/interview/SKILL.md` (214 lines) and `skills/sdd/reconcile/SKILL.md`; the audit skills
  (`skills/audit/…`) and the code skills (`skills/code/…`); one agent,
  `agents/speccen-worker.md`; two commands, `commands/start.md` and `commands/audit.md`.
  `README.md` and `ARCHITECTURE.md` describe the behaviour for people.
- **Hierarchy.** The governing skill is the single source of truth. Phase skills refer back to
  it ("follow the **Bundle & File Naming Conventions** defined in
  `skills/sdd/00-governing-workflow/SKILL.md`", e.g. `skills/sdd/01-feature-analysis/SKILL.md:9-10`).
  The interview skill defines the round format and is used by Phases 01, 03, 04, stops, the
  review round, Phase 06's graduation decision (`skills/sdd/00-governing-workflow/SKILL.md:395-401`)
  and, `gated` only, by the audit and code skills (`skills/sdd/interview/SKILL.md:37-52`).
- **Where the change lives.** The brief's rule belongs in governing → **Structured questions**
  (`skills/sdd/00-governing-workflow/SKILL.md:367-401`), the section that already governs how
  anything is asked of the Architect. Each other site points to it.

### Behavioural Analysis

How an item reaches the Architect today. Every path ends in a message or record the Architect
reads; the skills say what goes in it, but never that each item named in it carries its text.

**Scope of this flow (02/2, Architect, `log.md` 07:03):** only the paths by which an item — a
question, a decision, a row, an open item — reaches the Architect. Branches of the workflow
that never put an item to the Architect are left out.

Citations: `gov` = `skills/sdd/00-governing-workflow/SKILL.md`, `int` =
`skills/sdd/interview/SKILL.md`, `p05` = `skills/sdd/05-implementation/SKILL.md`. `(S)` is the
stop and `(R)` the review round; each is drawn once and entered from several branches.

**Paths, in outline.**

- `gated` interview: rounds repeat while an open decision remains. Each answer is a choice, "you
  decide", "later" (the question and its dependants become open items), "don't know yet" (Phase
  01: a working hypothesis and an open item) or "stop" (the remaining frontier becomes open
  items and the interview ends). When no open decision remains: the closing summary and
  question; "not yet" runs another round, "yes" hands back to the phase, which writes its output
  — open items included — and ends with its notice.
- `autonomous` decision: the delegate decides it (a DD when it could have gone another way and
  affects the work product, and always for an interview answer; pure style is not recorded); or,
  material and open under `stops: proceed`, it becomes a DD "MATERIAL — unconfirmed" and an open
  item in `summary.md`; or it is a stop (a hard stop, or material and open under `stops: ask`).
  Every DD reaches the Architect in the review round.
- Gate test: every row passes → transition; rows fail and a fix is allowed → fix, a log line
  naming the failed rows, and the test again; rows fail with no fix allowed, or the host cannot
  run a check → stop.
- Stop: `STATE.md` line, open item in `summary.md`, log entry, stop round. The answer "yes" or
  "no, use X" becomes basis; after a gate stop it may set the rows to re-check and the fixes
  allowed — without that, one run, and a failing row stops again. "Later" parks a question that
  does not block (Phase 01: a working hypothesis); a blocking one stays a stop.
- End of a run: the end-of-run report, then the review round. A resumed session: the resume
  summary. `gated` Phase 05: the completion notice, after all plan phases and the planned tests.

**1 — the `gated` interview**

```
           ┌────────────────────────────────────────────────┐
 ┌────────▶│ round: the frontier as a numbered list          │
 │         │ "01/7 — [Short title]"  int :82-98              │
 │         └────────────────────────┬───────────────────────┘
 │                                  ▼
 │         ┌────────────────────────────────────────────────┐
 │         │ the Architect answers, by number  int :97-101   │
 │         └────────────────────────┬───────────────────────┘
 │                                  ▼
 │                      ┌────────────────────────┐
 │                      │ kind of answer?         │ int :123-133
 │                      └────────────┬───────────┘
 │        ┌──────────────┬───────────┴───┬──────────────────┐
 │  choice or            │ "later"       │ "don't know yet"  │ "stop"
 │  "you decide"         ▼               ▼ (Phase 01)        ▼
 │        │   ┌──────────────────┐ ┌──────────────────┐ ┌──────────────────────┐
 │        │   │ the question and │ │ working          │ │ remaining frontier   │
 │        │   │ its dependants   │ │ hypothesis + an  │ │ becomes open items;  │
 │        │   │ become open items│ │ open item        │ │ the interview ends   │
 │        │   │ int :125-126     │ │ int :127-129     │ │ int :130             │
 │        │   └────────┬─────────┘ └────────┬─────────┘ └──────────┬───────────┘
 │        ▼            ▼                    ▼                      ▼
 │  ┌────────────────────────────────────────────┐   ┌──────────────────────────┐
 │  │ recorded: log.md + Interview table         │   │ open items in phase.md   │
 │  │ int :107-118                               │   │ and summary.md, read by  │
 │  └─────────────────────┬──────────────────────┘   │ the Architect            │
 │                        ▼                          └──────────────────────────┘
 │            ┌──────────────────────────┐
 │            │ open decision remains?    │ int :171-172
 │            └──────┬──────────────┬────┘
 │               yes │              │ no
 ├───────────────────┘              ▼
 │         ┌────────────────────────────────────────────────┐
 │         │ closing summary of the decisions  int :174      │
 │         │ + closing question  int :175-180                │
 │         └────────────────────────┬───────────────────────┘
 │                      ┌───────────┴────────────┐
 │                      │ answer?                 │ int :181-182
 │                      └─────┬────────────┬─────┘
 │                    not yet │            │ yes
 └────────────────────────────┘            ▼
                     ┌────────────────────────────────────────────────┐
                     │ the phase writes its output, open items        │
                     │ included, and ends with its notice             │
                     └────────────────────────────────────────────────┘
```

**2 — a decision in an `autonomous` phase**

```
 ┌──────────────────────────────────────────────────┐
 │ a decision arises in an autonomous phase          │
 └─────────────────────────┬────────────────────────┘
                           ▼
              ┌───────────────────────────┐
              │ how is it settled?         │
              └──┬───────────┬─────────┬──┘
   basis decides │           │         │ hard stop: conditions 2, 3, 4, 6, 7
   it, or not    │           │         │ gov :1238-1242, :1245-1250; or material
   material      │           │         │ and open under `stops: ask` gov :1236-1237
   gov :1157-1169│           │         ▼
                 │           │   ┌───────────┐
                 │           │   │ (S) stop   │
                 │           │   └───────────┘
                 │           │ material and open under `stops: proceed`  gov :1279-1282
                 │           ▼
                 │   ┌──────────────────────────────────────┐
                 │   │ DD "MATERIAL — unconfirmed" + an open │
                 │   │ item in summary.md  gov :1279-1280    │──────────┐
                 │   └──────────────────────────────────────┘          │
                 ▼                                                       │
       ┌──────────────────────────┐                                     │
       │ recorded as a DD?         │ gov :1220-1222, int :117-118        │
       └─────┬──────────────┬─────┘                                     │
   could have │              │ pure style within                        │
   gone another way          │ the conventions                          │
   and affects the work      ▼                                          │
   product, or an     ┌──────────────┐                                  │
   interview answer   │ not recorded │                                  │
             ▼        └──────────────┘                                  │
   ┌──────────────────────────────────┐                                 │
   │ DD-<n> in delegated-decisions.md │                                 │
   │ gov :1290                        │                                 │
   └─────────────────┬────────────────┘                                 │
                     ▼                                                  ▼
   ┌────────────────────────────────────────────────────────────────────────────┐
   │ (R) review round after the run: one question per delegated decision        │
   │ "(`DD-<n>`)"  int :153-161                                                  │
   └────────────────────────────────────────────────────────────────────────────┘
```

**3 — the gate test, the stop, the end of a run and a resumed session**

```
 ┌──────────────────────────────────────────────────┐
 │ gate test at the end of an autonomous phase:      │◀──────────────────────┐
 │ rows `item | result | evidence | verified`        │                       │
 │ gov :1180                                         │                       │
 └─────────────────────────┬────────────────────────┘                       │
                           ▼                                                 │
              ┌───────────────────────────┐                                  │
              │ result?                    │ gov :1199-1207, :1251           │
              └──┬───────────┬─────────┬──┘                                  │
  every row      │ rows fail;│         │ rows fail and the budget is used    │
  passes         │ a fix is  │         │ up, no progress, or the fix changes │
                 │ allowed   │         │ a conclusion, DD or ADR (cond. 5);  │
                 │           │         │ or the host cannot run a check (8)  │
                 │           ▼         ▼                                     │
                 │  ┌────────────────────────┐ ┌───────────┐                 │
                 │  │ fix; log "fix attempt   │ │ (S) stop   │                 │
                 │  │ <n> of <fixes>: run <N> │ └───────────┘                 │
                 │  │ failed rows <list>"     │                               │
                 │  │ gov :1209               │──────────────────────────────┤
                 │  └────────────────────────┘                               │
                 ▼                                                            │
       ┌──────────────────────────┐                                          │
       │ Phase 06 complete?        │                                          │
       └─────┬──────────────┬─────┘                                          │
          no │              │ yes                                            │
             ▼              ▼                                                │
 ┌──────────────────┐ ┌───────────────────────────────────────────┐         │
 │ transition to    │ │ end-of-run report  gov :1337-1340, then    │         │
 │ the next phase   │ │ (R) review round  gov :1341-1343           │         │
 └──────────────────┘ └───────────────────────────────────────────┘         │
                                                                             │
 ┌──────────────────────────────────────────────────┐                       │
 │ (S) stop: STATE.md "Stopped (autonomous) —        │                       │
 │ <one-line reason>" gov :1258-1259; open item in   │                       │
 │ summary.md gov :1260-1261; log entry gov :1262;   │                       │
 │ stop round gov :1263-1264                         │                       │
 └─────────────────────────┬────────────────────────┘                       │
                           ▼                                                 │
              ┌───────────────────────────┐                                  │
              │ the Architect's answer?    │ int :143-146                    │
              └──┬───────────────────┬────┘                                  │
  "yes" or       │                   │ "later"                               │
  "no, use X"    ▼                   ▼                                       │
 ┌───────────────────────────┐  ┌───────────────────────────┐               │
 │ logged verbatim; becomes  │  │ does the question block    │               │
 │ basis  gov :1267-1268     │  │ the phase?  int :144-146   │               │
 └─────────────┬─────────────┘  └──┬──────────────────────┬─┘               │
               ▼                yes │                      │ no              │
 ┌───────────────────────────┐     ▼                      ▼                 │
 │ did the stop come from    │ ┌───────────┐  ┌──────────────────────────┐  │
 │ the gate test?            │ │ (S) stays  │  │ parked: the run carries  │  │
 └──┬──────────────────┬─────┘ │ a stop     │  │ on; the phase's gate     │  │
  no │              yes │       └───────────┘  │ cannot pass while it is  │  │
     ▼                  ▼                      │ open; Phase 01: a working│  │
 ┌──────────────┐ ┌──────────────────────────┐ │ hypothesis               │  │
 │ the run      │ │ the answer sets the rows  │ └──────────────────────────┘  │
 │ resumes at   │ │ to re-check and the fixes │                               │
 │ the stopped  │ │ allowed; without that,    │                               │
 │ work         │ │ one run, and a failing    │                               │
 └──────────────┘ │ row stops again           │                               │
                  │ gov :1210-1212            │───────────────────────────────┘
                  └──────────────────────────┘

 ┌──────────────────────────┐      ┌────────────────────────────────────────────┐
 │ a session resumes         │─────▶│ resume summary: delegated decisions not yet │
 └──────────────────────────┘      │ reviewed, any stop, any graduation proposal │
                                   │ gov :533-540                                │
                                   └────────────────────────────────────────────┘

 ┌──────────────────────────┐      ┌────────────────────────────────────────────┐
 │ gated Phase 05: all plan  │─────▶│ completion notice "the planned tests pass   │
 │ phases done, planned      │      │ [or: with the following waived: …]"         │
 │ tests pass or are waived  │      │ p05 :286-292                                │
 └──────────────────────────┘      └────────────────────────────────────────────┘
```

**Known limits of the diagrams** (accepted by the Architect, 02/3, `log.md` 07:11). The diagrams
do not draw: the answer "a question back" (`skills/sdd/interview/SKILL.md:133`); the
`autonomous` Phase 01 working hypothesis (`skills/sdd/00-governing-workflow/SKILL.md:1253-1254`);
the review round on request (`skills/sdd/interview/SKILL.md:155`); the `gated` Phase 05
deviation notice (A-11); the end of a `gated` phase without an interview (A-12); and the record
step after a `gated` "stop" answer. The diagram-2 label "not material" is supported by
`skills/sdd/00-governing-workflow/SKILL.md:1220` and `:1228-1230`, not by `:1157-1169`. Records the
Architect reads and skills outside the speccen workflow stay out of the diagrams (02/4). The
inventory below is the complete list of paths.

<a id="architect-facing-places"></a>
#### Inventory — places that put something to the Architect (P02-1)

| # | Place | Text today | Names items? | In the brief |
|---|---|---|---|---|
| A-1 | Interview round template | `skills/sdd/interview/SKILL.md:86-93` — "**01/7 — [Short title]** — [The question: one decision, stated plainly, …]" | yes — the question's own reference; other questions, DDs, ADRs it mentions | §2.2 |
| A-2 | Interview — review round | `skills/sdd/interview/SKILL.md:158-161` — "**One question per delegated decision** (`DD-<n>`): `adopt`, `override` or `later`" | yes — `DD-<n>`, graduation candidates | §2.3 |
| A-3 | Stop record in `summary.md` | `skills/sdd/00-governing-workflow/SKILL.md:1260-1261` — "an open item with the exact question, the options, your lean and the evidence" | yes — gate rows, DDs, questions | §2.4 |
| A-4 | Stop round | `skills/sdd/00-governing-workflow/SKILL.md:1263-1264` — "the stopped questions as one numbered interview round" | yes — via the round template (A-1) | covered by §2.2 |
| A-5 | End-of-run report | `skills/sdd/00-governing-workflow/SKILL.md:1337-1340` — "the phases run, the gate checks passed, the delegated decisions recorded, any stops and their answers, and the pending graduation proposal" | yes — DDs, gate checks, stops, candidates | §2.5 |
| A-6 | Gate-test self-check | `skills/sdd/00-governing-workflow/SKILL.md:1181-1191` — five items; 5: "**Interview structure**" | — (a check, not a message) | §2.6 |
| A-7 | `stops: proceed` open item | `skills/sdd/00-governing-workflow/SKILL.md:1279-1280` — "Record it as a delegated decision with `Materiality` → `MATERIAL — unconfirmed`, so it is visible in the review round, and in the phase `summary.md` under its open items." | yes — `DD-<n>` in `summary.md` | **not listed** |
| A-8 | Resume summary | `skills/sdd/00-governing-workflow/SKILL.md:539-540` — "how many delegated decisions are not yet reviewed, any stop awaiting the Architect, and any pending graduation proposal" | can — a stop or candidate named by label | **not listed** |
| A-9 | Phase 06 graduation interview | `skills/sdd/06-close-out/SKILL.md:250-252` — "one numbered question per candidate, `promote` or `keep local`" | yes — candidate ids; via the round template (A-1) | covered by §2.2 |
| A-10 | Phase 03 ADR interview | `skills/sdd/03-compliance-review/SKILL.md:281-283` — "**One numbered question per undecided ADR** — its question, one line of context from the placeholder, the options, and a proposed decision"; also `skills/sdd/interview/SKILL.md:30` | yes — ADR ids; via A-1 | covered by §2.2 |
| A-11 | Phase 05 deviation notice (`gated`) | `skills/sdd/05-implementation/SKILL.md:237-240` — "documented it under the Deviations section … Please review and signal how to proceed." | points to a file; names no item | not listed — no label |
| A-12 | Phase-end notices 01 – 04, 06, 07, 08 | e.g. `skills/sdd/02-code-analysis/SKILL.md:416`, `skills/sdd/07-retrospective/SKILL.md:293-296` ("[N] findings") | no — counts and file paths only | not listed — no label |
| A-13 | Audit scorecard review interview | `skills/audit/03-scorecard-review/SKILL.md:59-65` — "Put them as one `interview` round"; the gate after it is an `AskUserQuestion` call (`:77-79`) | via A-1 (interview outside a bundle) | covered by §2.2 |
| A-14 | Code-documentation interview | `skills/code/code-documentation/SKILL.md:126-127` — "**2b — The open decisions: one `interview` round**", reference `code-documentation/<n>`; `skills/code/code-review/SKILL.md` uses only `AskUserQuestion` (`:39,100,107,178`) | via A-1 for code-documentation | covered by §2.2 |
| A-15 | Phase 07 delegation findings | `skills/sdd/07-retrospective/SKILL.md:140` — "cite the `DD-n` or the gate-check row" | yes — inside the Retrospective Report (a record) | not listed — a record |
| A-16 | Interview closing summary (`gated`) | `skills/sdd/interview/SKILL.md:174` — "Give a short closing summary of the decisions — in the Architect's words where possible." | can — decisions by reference | not listed |
| A-17 | Phase 05 completion notice | `skills/sdd/05-implementation/SKILL.md:292` — "the planned tests pass [or: with the following waived: …]" | can — waived tests by id | not listed |
| A-18 | `STATE.md` stop line | `skills/sdd/00-governing-workflow/SKILL.md:1258-1259` — "`Pending Architect Action` → `Stopped (autonomous) — <one-line reason>`" | can — a one-line reason may name a row or DD | not listed |
| A-19 | Reconcile report and notice | `skills/sdd/reconcile/SKILL.md:153-159` — "## Needs human resolution … [id-A] and [id-B] … Decide: which wins (supersession), or scoped override?"; the notice lists the items, `:172-176` | yes — store ids (readable slugs) | not listed — borderline |
| A-20 | Fix-attempt log line | `skills/sdd/00-governing-workflow/SKILL.md:1209` — "`fix attempt <n> of <fixes>: run <N> failed rows <list>`" | yes — bare row numbers; a record the Architect reads (bare row numbers are what the stop round quoted in brief §1 used: "Row 7 … Row 16") | not listed — a record |

Places that name, or can name, items and are not in the brief: **A-7** (the `stops: proceed`
open item in `summary.md` — the same file and reader as A-3), **A-8** (the resume summary),
**A-16** (the interview's closing summary), **A-17** (the Phase 05 completion notice), **A-18**
(the `STATE.md` stop line); and, as records the Architect reads, **A-15** (Retrospective
delegation findings), **A-19** (reconcile report, store-id slugs) and **A-20** (the fix-attempt
log line). A-4, A-9, A-10, A-13 and A-14 inherit the change through the interview round
template.

#### Line references in the brief (P02-2)

The issue was opened on 2026-11-11 10:40:40 UTC (`gh issue view 26 --json createdAt`). The newest
commit then was `8ecb30a`; the governing skill's text there is the same as at `6a0f83c` (`git diff`
is empty). Three later commits changed the governing skill: `77fb4f4` (+40 / −15, net +25),
`2e4634f` (+7 / −6, net +1) and `7cfcb66` (+8 / −2, net +6) — 2230 → 2262 lines. Text below line
1228 moved by the full +32; text at line 1158 moved by +23, because only part of `77fb4f4`'s
change lies above it. Three governing references have drifted; the interview references and
§2.1's heading hold.

| Brief | Cited | Now | Holds? |
|---|---|---|---|
| §2.1 "after `:367`" | Structured questions | section starts at `skills/sdd/00-governing-workflow/SKILL.md:367` (the heading, then as now), ends at `:401` | yes; "after :367" names the section, not a line in it — the insertion point is open (O-6) |
| §2.2 | `interview/SKILL.md:86-96` | `skills/sdd/interview/SKILL.md:86-96` | yes |
| §2.3 | `:158-161` | `skills/sdd/interview/SKILL.md:158-161` | yes |
| §2.4 | `:1228-1232` | `skills/sdd/00-governing-workflow/SKILL.md:1260-1261` (`:1228-1232` is now "Decisions you take" / materiality) | drifted +32 |
| §2.5 | `:1305-1307` | `skills/sdd/00-governing-workflow/SKILL.md:1337-1340` (`:1305-1307` is now the DD template) | drifted +32 |
| §2.6 | `:1158-1168` | `skills/sdd/00-governing-workflow/SKILL.md:1181-1191` (`:1158-1168` is now "Decision basis") | drifted +23 |

The quoted "before" text of every diff matches the current text word for word, so each diff
still applies by content. §1's evidence reference `:1228-1232` drifted the same +32.

#### Where labels are defined (P02-3)

- `DD-<n>` — defined: "Entries are numbered `DD-1`, `DD-2`, …"
  (`skills/sdd/00-governing-workflow/SKILL.md:1290`).
- `<phase>/<n>` — defined: "Refer to a question with its phase: `01/7`, `03/2`"
  (`skills/sdd/interview/SKILL.md:73-76`).
- `<skill>/<n>` — defined for interviews outside a bundle: "**Numbering** uses the calling skill
  instead of a phase: `code-documentation/3`, `audit-gate/2`" (`skills/sdd/interview/SKILL.md:45-46`).
- `Deviation [N]` — the Phase 05 deviation heading "### Deviation [N] — YYYY-MM-DD"
  (`skills/sdd/05-implementation/SKILL.md:225`).
- ADR ids and store ids — `<prefix>.<name_snake_case>`, readable slugs
  (`skills/sdd/00-governing-workflow/SKILL.md`, Bundle location and id format).
- `O-<n>`, `H-<n>`, `P02-<n>` — **not defined anywhere** in `skills/`, `agents/`, `commands/`,
  `README.md` or `ARCHITECTURE.md`. A search for `O-[0-9]`, `H-[0-9]` and `P02-` finds only
  `ISO-8601` (`skills/sdd/00-governing-workflow/SKILL.md:1799`, `:1845`), which is not a label.
  They are a habit of earlier bundles.
- Gate-check rows — the template is "one row per item — `item | result | evidence | verified`"
  (`skills/sdd/00-governing-workflow/SKILL.md:1180`): no number column. "Row 7" is an ordinal
  that bundles add.

So the rule must work for labels the skills define and for numbers a bundle invents. §2.1's
list names `DD-<n>`, `01/<n>`, `O-<n>`, `H-<n>`, `P02-<n>` and gate rows; it does not name
`<skill>/<n>` or `Deviation [N]`.

#### `AskUserQuestion` (P02-4)

- Governing: "**Headers ≤ 12 characters** (they are the tab labels)"
  (`skills/sdd/00-governing-workflow/SKILL.md:382`); the session-start call
  (`:428-462`) asks for prefix, name, kind, mode — no bundle item.
- The interview never uses the tool: "This list is the interview's own format. It does not use
  the `AskUserQuestion` tool." (`skills/sdd/interview/SKILL.md:98`).
- Other calls: `skills/audit/00-governing-audit/SKILL.md:119,124,142`,
  `skills/audit/01-recon/SKILL.md:34`, `skills/audit/03-scorecard-review/SKILL.md:77`,
  `skills/code/code-review/SKILL.md:39,100,107,178`,
  `skills/code/code-documentation/SKILL.md:47,119,201,290`. Each asks a fixed choice (run,
  baseline, gate, scope, approve) — none names a bundle item.

No `AskUserQuestion` call in the skills names a bundle item today. H-3 holds in substance: if a
future call does, the question text carries the subject; headers cannot.

#### Restated copies (P02-5)

- `README.md:217-231` describes stops ("one numbered round with its proposed answers"), `DD-n`
  entries and the review round ("each delegated decision (adopt, override or later)").
- `ARCHITECTURE.md:76-81` describes the interview ("a numbered list, each question with a
  proposed answer").
- Neither restates a template or the self-check list, so neither contradicts the change. Both
  describe what the Architect reads; whether they mention subjects is open (O-7).

### Data Model

- **Subject** (new): `[<label> | <text>]`. `<label>` is one of the defined labels (`DD-<n>`,
  `<phase>/<n>`, `<skill>/<n>`, `Deviation [N]`, an ADR or store id) or a bundle-local number (`O-<n>`, `H-<n>`, `P02-<n>`, a gate-check row); `<text>` is a plain
  question or statement. Inside a markdown table the pipe must be escaped (`\|`) — this bundle
  does so in `phase-01-feature-analysis/phase.md` and `delegated-decisions.md`.
- **Cardinalities.** One interview round: Phase 01 of this bundle had 6, then 2. One run: tens
  of DDs — `.speccen/bundles/2026-11-12.set_allowed_budget_for_autonomous_phases/delegated-decisions.md`
  runs to `DD-32`.

### Coding Patterns & Style

- **Rule once, point from sites.** The governing skill states a rule once; other places cite it
  by section in parentheses, e.g. "(see **Structured questions** in the conventions)"
  (`skills/sdd/00-governing-workflow/SKILL.md:429`). The brief's §2.4 and §2.5 follow this
  ("(Structured questions)").
- **Templates in fenced blocks**, with bracketed placeholders (`[Short title]`).
- **Numbered self-check items**, bold lead word, em dash, one or two lines of rule
  (`skills/sdd/00-governing-workflow/SKILL.md:1183-1190`).
- **Prose register.** Skill text is plain, short-sentence English with bold key terms; not STE
  (STE applies to reader documents only, `skills/sdd/00-governing-workflow/SKILL.md:360-363`).

**Test conventions.** There is no test framework. Earlier bundles verified skill-text changes
with throwaway Python text checks kept in the bundle's `files/` (e.g.
`.speccen/bundles/2026-11-12.set_allowed_budget_for_autonomous_phases/files/phase-05-text-checks.py`),
and lesson `2026-11-11.text_checks_read_their_place` says such checks must read the passage in
its place, not grep the whole file. The Phase 04 Test Plan follows that convention.

### Performance Characteristics

Not applicable to runtime: the "cost" is reading length. Adding a subject lengthens each item by
one short phrase. The rule's purpose is to remove the Architect's lookups in other files (brief
§1: "has to open three files"). No complexity concern.

### Relationship to Similar Components

- The governing skill already has one "reads on its own" style rule for a reader: the navigation
  bar is kept off `doc-*.md` so links to internal state do not ride along
  (`skills/sdd/00-governing-workflow/SKILL.md:182`). The new rule is the same idea applied
  to labels.
- The standing decision `2026-11-05.self_check_interview_structure` added self-check item 5;
  §2.6 adds item 6 in the same form.

### Known Issues & Code Commentary

- The round template invites the gap: "**01/7 — [Short title]**"
  (`skills/sdd/interview/SKILL.md:88`) — a title, not the question, sits next to the label.
- The review round: "**One question per delegated decision** (`DD-<n>`)"
  (`skills/sdd/interview/SKILL.md:158`) — the label only.
- No TODO, FIXME or HACK comment in the passages concerned.

<a id="conventions"></a>
## Project Conventions Confirmation

No `.claude/` folder and no `CLAUDE.md` exist.

#### `.github/SECURITY.md`
**Read:** ✓  
**CRITICAL/MANDATORY Rules:** "Please do not report security vulnerabilities through public GitHub issues, discussions, or pull requests."  
**Architecture Boundaries:** N/A  
**Technology Constraints:** "This project uses calendar-based versions (`YY.MDD.N`)."  
**Naming Conventions:** N/A  
**Critical Workflows:** Private vulnerability reporting via the Security tab, or speccen@cucurbit.be.  
**Hard Constraints:** In scope includes "Instructions or commands that could cause an assistant to run unintended or destructive actions" and "Prompt-injection weaknesses in the skills and workflows" — relevant: the change adds instructions only, no command.

#### `.github/CODEOWNERS` (not `.md`; read for ownership)
**Read:** ✓  
**Hard Constraints:** `*`, `/.github/` and `/.claude-plugin/` owned by `@speccen/team-leads`. Comments: "Workflows and release automation can change what runs with write access" (`/.github/`); "Plugin manifests carry the published version and marketplace metadata" (`/.claude-plugin/`).

#### `.github/workflows/bump-version.yml` (not `.md`; read for release flow)
**Read:** ✓  
**Critical Workflows:** on push to `main`, bumps the version unless only `.github/**`, `README.md`, `ARCHITECTURE.md` or `LICENSE` changed. A change to `skills/` therefore produces a version bump on merge.

<a id="outcome"></a>
## Executive Summary

**Dominant finding:** the skills give each item a label (`DD-<n>`, `01/7`) but nowhere ask that
the item's text travel with it; the round template puts a "short title" next to the label, and
the review round names the label alone. The brief's six edits address this at the right places;
its diffs still apply by content although three governing line references (§2.4 – §2.6) have
drifted by 23 – 32 lines.

**Root cause:** the format is defined for the bundle's traceability (`interview` → Numbering), not
for the reader.

**Key insight:** the change is one rule in **Structured questions** plus pointers. Places the brief
does not list also put labelled items to the Architect — the `stops: proceed` open item (A-7), the
resume summary (A-8), the interview's closing summary (A-16), the Phase 05 completion notice
(A-17) and the `STATE.md` stop line (A-18) — and records the Architect reads carry bare labels too
(A-15, A-19, A-20). Bundle-local labels (`O-`, `H-`, `P02-`, gate rows) are not defined in any
skill, so the rule must cover numbers a bundle invents.

<a id="open-items"></a>
## Open Items

| # | Open item | Settles in |
|---|---|---|
| O-1 | [O-1 \| Does the rule reach places the brief does not list — the `stops: proceed` open item, the resume summary, the interview's closing summary, the Phase 05 completion notice, the `STATE.md` stop line, and the records the Architect reads?] Now concrete: A-7, A-8, A-16, A-17, A-18 (messages and records put to the Architect), and the records A-15, A-19, A-20 — see the [inventory](#architect-facing-places). | Phase 03 |
| O-2 | [O-2 \| The three decisions in brief §5: state the rule once and point to it; cover only what is put to the Architect, not the record tables; add a sixth self-check item for subjects.] Unchanged from Phase 01. | Phase 03 |
| O-3 | [O-3 \| Does the rule cover the questions asked with the `AskUserQuestion` tool, and if so which parts?] Fact: no call names a bundle item today (P02-4). | Phase 03 |
| O-4 | [O-4 \| What are the acceptance scenarios — when is this done?] | Phase 04 |
| O-6 | [O-6 \| Where in Structured questions does the rule go — after the tool's constraints, or after "A series of decisions"?] The brief's "after `:367`" names the section, not a place in it. | Phase 03 |
| O-7 | [O-7 \| Should `README.md` and `ARCHITECTURE.md` mention the subject form where they describe stops and the review round?] | Phase 03 |

O-5 (the Phase 02 facts) is closed by this phase: P02-1 → the inventory above; P02-2 → the line
references table; P02-3 → where labels are defined; P02-4 → `AskUserQuestion`; P02-5 → restated
copies. No open item blocks Phase 03.
