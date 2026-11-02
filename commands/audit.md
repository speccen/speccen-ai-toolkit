---
name: audit
description: Start (or resume) a speccen application maturity audit — shortcut to the governing audit skill.
argument-hint: "['<application-name>' — optional; derived from the repository when omitted]"
---

Start the application maturity audit.

Load the governing audit skill, `app-maturity-audit`
(`skills/audit/00-governing-audit/SKILL.md` in this plugin), and follow its **Session Start
Protocol** from Step 1 — resolve the run under `.speccen/audits/`, then proceed under the
governing skill's orchestration. The first run of a codebase is the baseline
(`YYYY-MM-DD.baseline`); later runs are compared against it and the previous run.

This command is only a shortcut: the governing skill is the single source of truth. Do not
duplicate or reinterpret its logic here. If `$ARGUMENTS` contains an application name, pass it
through.
