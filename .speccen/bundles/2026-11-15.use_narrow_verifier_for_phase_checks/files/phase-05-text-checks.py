"""Text checks T-1 – T-19 for the narrow gate-check verifier (Phase 04 Test Plan, DD-22).

Run from the repository root:  python3 -I <bundle>/files/phase-05-text-checks.py [T-1 T-2 ...]
Each check reads its place in the file, not the whole file. Assertions come from the plan: the
Test Plan, the specification's scenarios and the appendix text (phase-04-specification/phase.md),
as amended by the approved Deviation 1 (phase-05-implementation/phase.md, DD-26) — never from the
edited files.
"""
import json
import re
import subprocess
import sys

BASE = "92ee62f"
GOV = "skills/sdd/00-governing-workflow/SKILL.md"
WORKER = "agents/speccen-worker.md"
PHASES = {
    "01": "skills/sdd/01-feature-analysis/SKILL.md",
    "02": "skills/sdd/02-code-analysis/SKILL.md",
    "03": "skills/sdd/03-compliance-review/SKILL.md",
    "04": "skills/sdd/04-specification/SKILL.md",
    "05": "skills/sdd/05-implementation/SKILL.md",
}


def read(path):
    with open(path, encoding="utf-8") as f:
        return f.read()


def old(path):
    return subprocess.run(["git", "show", f"{BASE}:{path}"], capture_output=True, text=True,
                          check=True).stdout


def between(text, start, end):
    i = text.index(start)
    j = text.index(end, i + len(start))
    return text[i:j]


def flat(text):
    return " ".join(text.split())


def gate(text=None):
    return between(text if text is not None else read(GOV), "### Gate test", "### Decisions you take")


def subagent(text=None):
    return between(text if text is not None else read(GOV), "## Subagent Execution", "\n## Prompt Log")


def mode(path):
    t = read(path)
    i = t.index("## Mode behaviour")
    j = t.find("\n## ", i + 1)
    return t[i:j if j > 0 else len(t)]


def has(place, *needles):
    f = flat(place)
    missing = [n for n in needles if flat(n) not in f]
    assert not missing, f"missing: {missing}"


def generic_template(text):
    i = text.index("**speccen work order**\n- Unit: [phase and unit")
    start = text.rindex("```markdown\n", 0, i)
    end = text.index("```\n", i) + 4
    return text[start:end]


def t1():
    has(gate(), "The self-check owns everything inside the bundle.",
        "The verifier owns only claims about the code and the repository.",
        "The verifier never reads the bundle.")


def t2():
    has(gate(), "record that row's load-bearing claims in the same step", "At the gate the list already exists.")


def t3():
    has(gate(), "directly under the gate table, under `Claims`",
        "`K-<n> (row <N>) · claim · how to check · expected`",
        "preferably a command whose output settles the claim",
        "A `path:line` is allowed.", "about the content, not the line number",
        "one or two tool calls", "split it or drop it")


def t4():
    has(gate(), "Exhaustive claims first.", "holds everywhere, or nowhere",
        "a count or a \"none found\" check", "Spot checks never confirm such a row",
        "at most 3 claims", "Every count that a conclusion depends on.",
        "convention rules that bind the change", "is cited by file and is not on the list")


def t5():
    has(gate(), "Hard cap: 15 claims per run.", "keep the 15 whose failure would change a conclusion",
        "`not on list — low risk`")


def t6():
    has(gate(), "Launch it as soon as the claim list is final.",
        "Run it at the same time as the verifier",
        "the self-check edits only bundle files, and the verifier reads only code and the repository")


def t7():
    has(gate(), "**`slip`**", "the line number, path or count is a little off, and the conclusion stands",
        "the verifier gives the correct value, and you correct the citation",
        "**`wrong`**", "the content is not there, or the value differs in a way the conclusion depends on",
        "A `wrong` claim fails its row, and the fix loop below applies.",
        "it uses no fix attempt and triggers no re-run",
        "If the verifier is unsure which kind it is, it reports `wrong`.",
        "Append each result to its claim line, after `→`.")


def t8():
    has(gate(), "reads nothing beyond what settles them", "at most 2 `noticed:` lines",
        "about something adjacent that looks wrong", "in a row at the foot of the gate table",
        "`noticed-<n> |", "corrected, or not relevant, because", "becomes a `wrong` claim in the next run")


def t9():
    has(gate(), "A row is `confirmed (run N)` when every claim it has is `confirmed`, or `slip` with the citation corrected.",
        "A row without claims reads `n/a — bundle-internal`.",
        "reads `not on list — low risk`", "If no row cites code or repository evidence, launch no verifier.",
        "All rows then read `n/a — bundle-internal`.",
        "write `not run` in that column",
        "re-checks only (a) the `wrong` claims, (b) the claims whose file changed during the fix, and (c) any `noticed:` line promoted to a claim.",
        "Slips are never re-checked.", "Rows it does not re-check keep their last `confirmed (run N)`.",
        "the Architect's answer sets which claims the next verifier run re-checks",
        "Without that, one run follows, and a `wrong` claim stops again.",
        "The verifier reports on every listed claim in one run.")


def t10():
    rows = [l for l in subagent().splitlines() if l.startswith("|") and "gate-check verifier" in l]
    assert len(rows) == 1, rows
    has(rows[0], "narrow", "settles the listed claims only", "never reads the bundle", "the gate decision")


def t11():
    s = subagent()
    new_block = "The gate-check verifier has its own, narrow work order:"
    has(gate(), "with the verifier work order")
    has(s, "- Unit: gate-check verifier (Phase NN, run N) — NARROW",
        "- Bundle: [{{FOLDER_NAME}}] — do not read bundle files", "- Claims: [≤15",
        "- Stop: once every listed claim is settled", "- Outputs: none — report only",
        "`confirmed` · `slip — <correct value>` · `wrong — <actual value>`; then at most 2 `noticed:` lines")
    generic = generic_template(read(GOV))
    assert generic == generic_template(old(GOV)), "generic template changed"
    after = read(GOV).split(generic, 1)[1]
    assert after.lstrip("\n").startswith(new_block), "verifier template not directly after the generic one"


def t12():
    do = between(read(WORKER), "**Do:**", "**Do not:**") if "**Do not:**" in read(WORKER) else between(read(WORKER), "**Do:**", "**Return**")
    bullets = [b for b in re.split(r"\n(?=- )", do) if "gate-check verifier" in b]
    assert len(bullets) == 1, bullets
    has(bullets[0], "narrow", "settle only the listed claims", "one or two tool calls each",
        "do not read the bundle", "one line per claim", "`confirmed`", "`slip — <correct value>`",
        "`wrong — <actual value>`", "at most 2 `noticed:` lines")


def t13():
    want = {
        "01": ["no verifier runs", "no codebase access"],
        "02": ["Convention quotes that bind the change", "counts", "\"none found\" claims",
               "pattern or risk conclusion"],
        "03": ["ADR's rationale", "prototype's result"],
        "04": ["every file, symbol and integration point the plan changes or extends",
               "At most one claim per plan step that touches existing code",
               "The traceability rows stay with the self-check"],
        "05": ["a single named test run", "a symbol present, a pattern absent", "Never the full suite", "the main session runs that itself"],
    }
    for n, path in PHASES.items():
        bullets = [b for b in re.split(r"\n(?=- )", mode(path)) if b.startswith("- **Verifier claims.**")]
        assert len(bullets) == 1, (n, bullets)
        assert flat(bullets[0]).endswith("(governing skill → Gate test)."), (n, "pointer")
        has(bullets[0], *want[n])


def t14():
    files = subprocess.run(["git", "ls-files", "skills", "agents"], capture_output=True, text=True,
                           check=True).stdout.split()
    bad = []
    for path in files:
        if not path.endswith(".md"):
            continue
        for no, line in enumerate(read(path).splitlines(), 1):
            low = line.lower()
            if "verifier" in low and ("every row" in low or "every quote" in low
                                      or "re-open the evidence of every" in low):
                bad.append(f"{path}:{no}")
    assert not bad, bad


def t15():
    new, prev = read(GOV), old(GOV)
    ng, og = gate(new), gate(prev)
    passages = [
        between(og, "  1. **Quotes**", "  Record the self-check"),
        between(og, "- Stop (stop condition 5) when:", "\n\n  A fix that only"),
        "up to the phase's effective `fixes`\n  attempts (Configuration; default `5`).",
        between(og, "  A fix that only repairs", "\n\n  Log each attempt"),
        between(og, "  Log each attempt", "\n- After a stop"),
        between(og, "- No question of this phase that was parked", "- If any item fails"),
        "  Record the self-check in one line above the gate table: `Self-check: done — N corrections`.",
    ]
    for p in passages:
        assert p in ng, f"changed: {p[:60]!r}"
    lines = prev.splitlines()
    for no in (778, 1453, 1454):
        assert lines[no - 1] in new, f"session-model line {no} changed"
    assert generic_template(new) == generic_template(prev), "generic template changed"


def t16():
    p = json.load(open(".claude-plugin/plugin.json"))["version"]
    m = json.load(open(".claude-plugin/marketplace.json"))
    vs = {p, m["metadata"]["version"], m["plugins"][0]["version"]}
    assert len(vs) == 1, vs
    v = vs.pop()
    assert re.fullmatch(r"\d{2}\.\d{3,4}\.\d+", v), v
    key = lambda s: (int(s.split(".")[0]), int(s.split(".")[1]), int(s.split(".")[2]))
    assert key(v) > key("26.1115.1"), v
    assert v == "26.1116.1", v


def t17():
    g = gate()
    assert g.count("`Self-check: done — N corrections`") == 1
    assert flat(g).count("up to the phase's effective `fixes` attempts") == 1


def t18():
    r = subprocess.run(["git", "diff", "--quiet", BASE, "--", "skills/sdd/07-retrospective",
                        "README.md", "ARCHITECTURE.md"])
    assert r.returncode == 0, "diff found"


def sentences(text):
    text = re.sub(r"`[^`]*`", "CODE", text)
    out = []
    for part in re.split(r"\s*\|\s*", text):
        part = re.sub(r"^\s*(?:[-*]|\d+\.)\s+", "", part)
        part = re.sub(r"\*\*([^*]*?\.)\*\*", r"\1\n", part)
        for s in re.split(r"(?<=[.!?])\s+|\n", part):
            if s.strip():
                out.append(s.strip())
    return out


def t19():
    diff = subprocess.run(["git", "diff", "-U0", BASE, "--", "skills", "agents"], capture_output=True,
                          text=True, check=True).stdout
    added, bullets, cur = [], [], []
    for line in diff.splitlines():
        if line.startswith("+") and not line.startswith("+++"):
            body = line[1:]
            if re.match(r"^\s*(?:[-*]|\d+\.)\s|^\|", body) or not body.strip():
                if cur:
                    bullets.append(" ".join(cur))
                cur = [body] if body.strip() else []
            else:
                cur.append(body.strip())
        else:
            if cur:
                bullets.append(" ".join(cur))
            cur = []
    if cur:
        bullets.append(" ".join(cur))
    long = []
    for b in bullets:
        for s in sentences(b):
            n = len([w for w in s.split() if re.search(r"\w", w)])
            if n > 30:
                long.append((n, s[:90]))
    assert not long, long


CHECKS = {f"T-{i}": f for i, f in enumerate(
    [t1, t2, t3, t4, t5, t6, t7, t8, t9, t10, t11, t12, t13, t14, t15, t16, t17, t18, t19], 1)}

if __name__ == "__main__":
    wanted = sys.argv[1:] or list(CHECKS)
    failed = 0
    for name in wanted:
        try:
            CHECKS[name]()
            print(f"{name}: pass")
        except Exception as e:
            failed += 1
            print(f"{name}: FAIL — {e}")
    sys.exit(1 if failed else 0)
