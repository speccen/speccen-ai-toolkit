---
id: 2026-11-18.rename_audit_skills
kind: feature
work-kind: refactoring
status: active
evidence: confirmed
created: 2026-11-18T07:24:00Z
updated: 2026-11-18T07:24:00Z
date: 2026-11-18T07:24:00Z
touches: [maturity-audit, readme]
produced: []
specification: ./specification.html
---

# Rename audit skills

[Index](../../index.md)

---

|     | Info |
| --- | --- |
| **What** | The five audit skills get folder names equal to their frontmatter names, with the `audit-` prefix and no numbers (`00-governing-audit` → `audit-maturity`, … `04-synthesis` → `audit-synthesis`); the governing skill's name changes from `app-maturity-audit` to `audit-maturity` |
| **Outcome** | One code commit (`6c6187c`): 19 renames; paths, the `compare_scorecards.py` rubric folders, `/speccen:audit`, ARCHITECTURE and the README table and upgrade note updated; rubric hash unchanged (`212cd4db08e1`) |
| **Touches** | maturity-audit, readme |
| **Origin bundle** | bundles/2026-11-18.rename_audit_skills (disposable; this node is the durable residue) |

| Related | |
| --- | --- |
| **Specification** | [specification.html](./specification.html) — intent |
