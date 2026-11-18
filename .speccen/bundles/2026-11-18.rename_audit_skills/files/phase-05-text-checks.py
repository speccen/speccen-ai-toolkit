#!/usr/bin/env python3
"""Phase 05 checks for the bundle 2026-11-18.rename_audit_skills (Test Plan T-1 – T-13, T-4 apart).

Every expected value comes from the Phase 04 Test Plan and the brief, never from the new code:
the substitution map, the planned README upgrade note, the brief's commit message and the base
commit e824b5c. Texts are read from git objects (`git show REV:path`), so line endings do not
matter. Run from the repository root:  python -I -B <bundle>/files/phase-05-text-checks.py
Move test: set MUTATE=T-1, T-8 or T-9 to change one expected text in memory; that check must fail.
"""
import os, re, subprocess, sys

BASE, HEAD = "e824b5c", "HEAD"
BUNDLE = ".speccen/bundles/2026-11-18.rename_audit_skills/"
MUTATE = os.environ.get("MUTATE", "")
MAP = [("00-governing-audit", "audit-maturity"), ("01-recon", "audit-recon"),
       ("02-dimension-analysis", "audit-dimension-analysis"),
       ("03-scorecard-review", "audit-scorecard-review"), ("04-synthesis", "audit-synthesis"),
       ("app-maturity-audit", "audit-maturity")]
README_TABLE = [("sdd-governing-audit/", "audit-maturity/"), ("sdd-recon/", "audit-recon/"),
                ("sdd-dimension-analysis/", "audit-dimension-analysis/"),
                ("sdd-scorecard-review/", "audit-scorecard-review/"),
                ("sdd-synthesis/", "audit-synthesis/")]
PLANNED_NOTE = """> Upgrading a local copy from before the `sdd-` and `audit-` prefixes: the workflow skill folders
> were renamed (`00-governing-workflow/` → `sdd-governing-workflow/`, … `interview/` →
> `sdd-interview/`), and so were the audit skill folders (`00-governing-audit/` →
> `audit-maturity/`, … `04-synthesis/` → `audit-synthesis/`). Remove the old folders from your
> skills directory before you copy the new ones, or both sets load: `00-governing-workflow/`,
> `01-feature-analysis/`, `02-code-analysis/`, `03-compliance-review/`, `04-specification/`,
> `05-implementation/`, `06-close-out/`, `07-retrospective/`, `08-reference/`, `interview/`,
> `reconcile/`, `00-governing-audit/`, `01-recon/`, `02-dimension-analysis/`,
> `03-scorecard-review/` and `04-synthesis/`."""
BRIEF_MESSAGE = """refactor: prefix the audit skills with audit- and drop the folder numbers

Rename the five skills in skills/audit/ so the folder and the frontmatter
name are the same and carry the audit- prefix (00-governing-audit ->
audit-maturity, 01-recon -> audit-recon, ... 04-synthesis ->
audit-synthesis). The governing skill's name changes from
app-maturity-audit to audit-maturity. Update every skill path, the
compare_scorecards.py rubric paths, the /speccen:audit command and the
README audit table (which the sdd rename had pointed at non-existent
sdd-* folders). Rubric contents, the rubric hash, audit run layout and
the .speccen/ history are unchanged."""
SEARCH = re.compile(r"0[0-4]-(governing-audit|recon|dimension-analysis|scorecard-review|synthesis)"
                    r"|app-maturity-audit|sdd-(governing-audit|recon|dimension-analysis|scorecard-review|synthesis)\b")
RUBRICS = ["adaptability", "architecture", "cicd-deployment", "code-quality", "dependency-health",
           "documentation", "observability", "performance-scalability", "reliability", "security",
           "testing"]
# old path at BASE -> new path at HEAD
MOVES = {f"skills/audit/02-dimension-analysis/references/{r}.md":
         f"skills/audit/audit-dimension-analysis/references/{r}.md" for r in RUBRICS}
MOVES["skills/audit/03-scorecard-review/scripts/build_scorecard.py"] = \
    "skills/audit/audit-scorecard-review/scripts/build_scorecard.py"
UNCHANGED = dict(MOVES)  # T-5: the 13 R100 files
UNCHANGED["skills/audit/00-governing-audit/references/bundle-conventions.md"] = \
    "skills/audit/audit-maturity/references/bundle-conventions.md"
EDITED = {  # T-8: old path -> new path, compared through the map
    "skills/audit/00-governing-audit/SKILL.md": "skills/audit/audit-maturity/SKILL.md",
    "skills/audit/01-recon/SKILL.md": "skills/audit/audit-recon/SKILL.md",
    "skills/audit/02-dimension-analysis/SKILL.md": "skills/audit/audit-dimension-analysis/SKILL.md",
    "skills/audit/03-scorecard-review/SKILL.md": "skills/audit/audit-scorecard-review/SKILL.md",
    "skills/audit/04-synthesis/SKILL.md": "skills/audit/audit-synthesis/SKILL.md",
    "skills/audit/03-scorecard-review/scripts/compare_scorecards.py":
        "skills/audit/audit-scorecard-review/scripts/compare_scorecards.py",
    "commands/audit.md": "commands/audit.md",
    "ARCHITECTURE.md": "ARCHITECTURE.md",
}


def git(*a, ok=False):
    r = subprocess.run(["git", *a], capture_output=True, text=True, encoding="utf-8")
    if ok:
        return r.returncode
    if r.returncode:
        raise SystemExit(f"git {' '.join(a)} failed: {r.stderr}")
    return r.stdout


def show(rev, path):
    return git("show", f"{rev}:{path}")


def apply(text, pairs):
    for a, b in pairs:
        text = text.replace(a, b)
    return text


def note_block(text):
    """The README upgrade note: the '>' lines that start with '> Upgrading a local copy'."""
    lines = text.split("\n")
    start = next(i for i, l in enumerate(lines) if l.startswith("> Upgrading a local copy"))
    end = start
    while end < len(lines) and lines[end].startswith(">"):
        end += 1
    return start, end, "\n".join(lines[start:end])


results = []


def check(tid, ok, detail):
    results.append((tid, ok))
    print(f"{tid}: {'PASS' if ok else 'FAIL'} — {detail}")


tracked = [p for p in git("ls-tree", "-r", "--name-only", HEAD).split("\n")
           if p and not p.startswith(".speccen/")]
texts = {}
for p in tracked:
    try:
        texts[p] = show(HEAD, p)
    except (SystemExit, UnicodeDecodeError):
        pass
readme = texts["README.md"]
ns, ne, note = note_block(readme)

# T-1 — every hit of the DD-7 search is a line of the README upgrade note; 4 hits
note_lines = set(range(ns, ne))
if MUTATE == "T-1":
    note_lines = set(range(ns, ne - 1))
hits = [(p, i) for p, t in texts.items() for i, l in enumerate(t.split("\n")) if SEARCH.search(l)]
outside = [(p, i + 1) for p, i in hits if not (p == "README.md" and i in note_lines)]
check("T-1", not outside and len(hits) == 4, f"{len(hits)} hits, outside the note: {outside}")

# T-2 — folder = name: over skills/*/*/SKILL.md
skills = [p for p in tracked if re.fullmatch(r"skills/[^/]+/[^/]+/SKILL\.md", p)]
mism = []
for p in skills:
    n = re.search(r"^name: (.*)$", texts[p], re.M).group(1).strip()
    if n != p.split("/")[2]:
        mism.append((p, n))
check("T-2", not mism and len(skills) == 18, f"{len(skills)} skills, mismatches: {mism}")

# T-3 — every skills/audit/... path cited in a tracked .md outside .speccen/ exists
existing = set(tracked) | {"/".join(p.split("/")[:k]) + "/" for p in tracked for k in range(1, p.count("/") + 1)}
cited, missing = 0, []
for p, t in texts.items():
    if p.endswith(".md"):
        for m in re.finditer(r"skills/audit/[A-Za-z0-9_./-]*", t):
            c = m.group(0).rstrip(".")
            cited += 1
            if c not in existing and c + "/" not in existing:
                missing.append((p, c))
check("T-3", cited > 0 and not missing, f"{cited} citations, missing: {missing}")

# T-5 — 19 renames under skills/audit; the 13 unchanged files are R100
ns5 = [l.split("\t") for l in git("diff", "-M", "--name-status", BASE, HEAD, "--", "skills/audit").strip().split("\n") if l]
renames = [r for r in ns5 if r[0].startswith("R")]
r100 = {(r[1], r[2]) for r in renames if r[0] == "R100"}
check("T-5", len(ns5) == 19 and len(renames) == 19 and r100 == set(UNCHANGED.items()),
      f"{len(ns5)} entries, {len(renames)} renames, {len(r100)} R100")

# T-6 — the hash inputs keep their blob ids
diff6 = [o for o, n in MOVES.items() if git("rev-parse", f"{BASE}:{o}") != git("rev-parse", f"{HEAD}:{n}")]
check("T-6", not diff6, f"{len(MOVES)} hash inputs, changed: {diff6}")

# T-7 — the governing description line is unchanged
d_old = re.search(r"^description:.*$", show(BASE, "skills/audit/00-governing-audit/SKILL.md"), re.M).group(0)
d_new = re.search(r"^description:.*$", texts["skills/audit/audit-maturity/SKILL.md"], re.M).group(0)
check("T-7", d_old == d_new, "description line equal" if d_old == d_new else "description changed")

# T-8 — pure rename: new = map(old)
bad8 = []
for o, n in EDITED.items():
    exp = apply(show(BASE, o), MAP)
    if MUTATE == "T-8" and o == "commands/audit.md":
        exp = exp.replace("audit-maturity", "audit-maturity-x", 1)
    if exp != texts[n]:
        bad8.append(n)
old_readme = show(BASE, "README.md")
os_, oe, _ = note_block(old_readme)
ol, nl = old_readme.split("\n"), readme.split("\n")
exp_rest = apply("\n".join(ol[:os_] + ol[oe:]), MAP + README_TABLE)
if exp_rest != "\n".join(nl[:ns] + nl[ne:]):
    bad8.append("README.md (outside the note)")
check("T-8", not bad8, f"{len(EDITED) + 1} files, differing: {bad8}")

# T-9 — the note equals the planned text
planned = PLANNED_NOTE if MUTATE != "T-9" else PLANNED_NOTE.replace("audit-synthesis/`).", "audit-synthesis/`)!")
check("T-9", note == planned and "Keep the audit folders" not in readme, "note equals the planned text" if note == planned else "note differs")

# T-10 — the change set outside .speccen/
ns10 = [l.split("\t") for l in git("diff", "-M", "--name-status", BASE, HEAD).strip().split("\n") if l]
ns10 = [r for r in ns10 if not r[-1].startswith(".speccen/")]
mods = sorted(r[1] for r in ns10 if r[0] == "M")
rn = [r for r in ns10 if r[0].startswith("R") and r[2].startswith("skills/audit/")]
other = [r for r in ns10 if r not in rn and r[0] != "M"]
pyc = [p for p in tracked if "__pycache__" in p]
ok10 = len(rn) == 19 and mods == ["ARCHITECTURE.md", "README.md", "commands/audit.md"] and not other and not pyc
check("T-10", ok10, f"{len(rn)} renames, modified {mods}, other {other}, pycache {pyc}")

# T-11 — one code commit, the brief's message, no attribution
code = [c for c in git("log", "--format=%H", f"{BASE}..{HEAD}", "--", ".", ":(exclude).speccen").split() if c]
msg = git("log", "-1", "--format=%B", code[0]).strip() if len(code) == 1 else ""
attrib = re.search(r"Co-Authored-By|Generated with", msg, re.I)
check("T-11", len(code) == 1 and msg == BRIEF_MESSAGE and not attrib, f"{len(code)} code commit(s); message {'equal' if msg == BRIEF_MESSAGE else 'differs'}")

# T-12 — .speccen/ changes only inside this bundle
sp = [p for p in git("diff", "--name-only", BASE, HEAD, "--", ".speccen").split("\n") if p and not p.startswith(BUNDLE)]
check("T-12", not sp, f"outside the bundle: {sp}")

# T-13 — other skill groups and agents unchanged
rc = git("diff", "--quiet", BASE, HEAD, "--", "skills/sdd", "skills/code", "agents", ok=True)
check("T-13", rc == 0, "skills/sdd, skills/code, agents unchanged" if rc == 0 else "changed")

failed = [t for t, ok in results if not ok]
print("ALL PASS" if not failed else f"FAILED: {', '.join(failed)}")
sys.exit(1 if failed else 0)
