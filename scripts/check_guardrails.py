#!/usr/bin/env python3
"""Guardrail and wiring check for the speccen governing skill.

Two checks, standard library only:

1. Guardrail inventory. Every sentence in the governing skill and its references that
   carries a guardrail word (never, only, must, always, CRITICAL, cannot, absolute) is
   recorded in scripts/guardrails.lock with its tier: CORE (SKILL.md, always loaded) or
   REF (a reference file, loaded at a trigger). The check fails when a locked sentence
   disappears, or when a CORE sentence is found only in a reference file — a rule may
   never move out of the always-loaded skill without a deliberate lock update.

2. Reference wiring. Every file in references/ has an "**Applies when:**" line in its
   first lines and is linked from SKILL.md; every relative link in SKILL.md resolves.

Usage:
    python scripts/check_guardrails.py            # check (exit 1 on failure)
    python scripts/check_guardrails.py --update   # rewrite the lock after a deliberate change
"""

import argparse
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
SKILL_DIR = ROOT / "skills" / "sdd" / "sdd-governing-workflow"
CORE = SKILL_DIR / "SKILL.md"
LOCK = ROOT / "scripts" / "guardrails.lock"
WORDS = re.compile(r"\b(never|only|must|always|CRITICAL|cannot|absolute)\b", re.I)


def normalise(text):
    text = re.sub(r"\*\*|__", "", text)
    text = re.sub(r"^\s*(?:[-*]|\d+\.)\s+", "", text)
    return re.sub(r"\s+", " ", text).strip()


def sentences(path):
    text = path.read_text(encoding="utf-8")
    text = re.sub(r"```.*?```", " ", text, flags=re.S)  # templates are not rules
    out = []
    for block in re.split(r"\n\s*\n|\n(?=\s*(?:[-*]|\d+\.)\s)", text):
        for s in re.split(r"(?<=[.!?:])\s+(?=[A-Z*`\"(])", block):
            s = normalise(s)
            if len(s) > 25 and WORDS.search(s):
                out.append(s)
    return out


def inventory():
    inv = {}
    for s in sentences(CORE):
        inv[s] = "CORE"
    for ref in sorted((SKILL_DIR / "references").glob("*.md")):
        for s in sentences(ref):
            inv.setdefault(s, "REF")
    return inv


def check_wiring():
    errors = []
    core_text = CORE.read_text(encoding="utf-8")
    for ref in sorted((SKILL_DIR / "references").glob("*.md")):
        head = "\n".join(ref.read_text(encoding="utf-8").splitlines()[:6])
        if "**Applies when:**" not in head:
            errors.append(f"{ref.name}: no '**Applies when:**' line at the top")
        if f"references/{ref.name}" not in core_text:
            errors.append(f"{ref.name}: not linked from SKILL.md")
    prose = re.sub(r"```.*?```", " ", core_text, flags=re.S)  # template links are examples
    for target in re.findall(r"\]\(([^)#]+)(?:#[^)]*)?\)", prose):
        if "://" in target:
            continue
        if not (CORE.parent / target).exists():
            errors.append(f"SKILL.md: broken link {target}")
    return errors


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--update", action="store_true")
    args = ap.parse_args()
    inv = inventory()
    if args.update:
        LOCK.write_text("".join(f"{t}\t{s}\n" for s, t in sorted(inv.items(), key=lambda x: (x[1], x[0]))),
                        encoding="utf-8")
        print(f"wrote {LOCK.relative_to(ROOT)}: {len(inv)} guardrail sentences")
        return 0
    errors = check_wiring()
    if not LOCK.exists():
        errors.append("scripts/guardrails.lock missing — run with --update once")
    else:
        for line in LOCK.read_text(encoding="utf-8").splitlines():
            tier, s = line.split("\t", 1)
            now = inv.get(s)
            if now is None:
                errors.append(f"removed {tier} guardrail: {s[:110]}")
            elif tier == "CORE" and now != "CORE":
                errors.append(f"CORE guardrail moved to a reference: {s[:110]}")
    for e in errors:
        print("FAIL", e)
    print("ok" if not errors else f"{len(errors)} problem(s)")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
