#!/usr/bin/env python3
"""Stamp an audit run and compare it with earlier runs of the same codebase.

One `.speccen/` belongs to one codebase, so every run under `.speccen/audits/` is one point
in a single time series. The scorer (build_scorecard.py) is not touched; this script only
reads its `summary.json` and the per-dimension `result.json` files.

  stamp   <run_dir>   write <run_dir>/run.json (id, date, app, commit, toolkit version, rubric hash)
  compare <run_dir>   write <run_dir>/trend.md (vs previous run and vs baseline) and
                      regenerate <audits_root>/history.md + history.json

Both outputs are machine-owned: never hand-edit them. Finding-level movement (new / resolved /
persisting) needs judgment and lives in the hand-written <run_dir>/trend-notes.md.
"""
import argparse
import datetime
import hashlib
import json
import pathlib
import subprocess
import sys

SKILLS_ROOT = pathlib.Path(__file__).resolve().parents[2]
PLUGIN_JSON = SKILLS_ROOT.parent.parent / ".claude-plugin" / "plugin.json"
# Higher is better for these; the ordinal labels are lower-is-better burdens.
BURDEN = {"Low": 0, "Medium": 1, "Moderate": 1, "High": 2}


def rubric_hash(run: pathlib.Path) -> str:
    """Hash of everything that decides a score: the rubrics, the scorer, its default weights and
    the run's own weights.json override, if any."""
    h = hashlib.sha256()
    files = sorted((SKILLS_ROOT / "02-dimension-analysis" / "references").glob("*.md"))
    files.append(SKILLS_ROOT / "03-scorecard-review" / "scripts" / "build_scorecard.py")
    if (run / "weights.json").exists():
        files.append(run / "weights.json")
    for f in files:
        h.update(f.name.encode())
        h.update(f.read_bytes())
    return h.hexdigest()[:12]


def git(*args) -> str:
    try:
        return subprocess.run(["git", *args], capture_output=True, text=True,
                              check=True).stdout.strip()
    except (OSError, subprocess.CalledProcessError):
        return ""


def stamp(run: pathlib.Path, app: str):
    version = ""
    if PLUGIN_JSON.exists():
        version = json.loads(PLUGIN_JSON.read_text()).get("version", "")
    data = {
        "id": run.name,
        "date": datetime.date.today().isoformat(),
        "app": app or git("rev-parse", "--show-toplevel").rsplit("/", 1)[-1],
        "commit": git("rev-parse", "HEAD"),
        "toolkit_version": version,
        "rubric_hash": rubric_hash(run),
    }
    (run / "run.json").write_text(json.dumps(data, indent=2) + "\n")
    print(f"Wrote {run / 'run.json'}")


def load_run(run: pathlib.Path):
    sj, rj = run / "summary.json", run / "run.json"
    if not (sj.exists() and rj.exists()):
        return None
    meta, summary = json.loads(rj.read_text()), json.loads(sj.read_text())
    levels = {d["dimension"]: d for d in summary.get("dimensions", [])}
    return {"id": run.name, "meta": meta, "summary": summary, "levels": levels}


def load_all(root: pathlib.Path):
    runs = []
    for d in sorted(p for p in root.iterdir() if p.is_dir()):
        r = load_run(d)
        if r:
            runs.append(r)
        else:
            print(f"note: skipping {d.name} (needs run.json and summary.json)", file=sys.stderr)
    runs.sort(key=lambda r: (r["meta"].get("date", ""), r["id"]))
    return runs


def arrow(delta, higher_is_better=True):
    if delta is None:
        return "—"
    if delta == 0:
        return "="
    good = (delta > 0) == higher_is_better
    return ("▲ " if good else "▼ ") + f"{delta:+g}"


def fmt(v):
    return "—" if v is None else str(v)


def diff(a, b):
    return None if a is None or b is None else round(b - a, 2)


def burden_delta(a, b):
    if a not in BURDEN or b not in BURDEN:
        return None
    return BURDEN[b] - BURDEN[a]


def signal_rows(ref, cur):
    """(label, ref value, current value, change). Burdens: a rise is bad."""
    rs, cs = ref["summary"], cur["summary"]
    rows = []
    for label, key in (("Weighted average", "weighted_average"),
                       ("Readiness gate (min of critical)", "gating_level")):
        rows.append((label, fmt(rs.get(key)), fmt(cs.get(key)),
                     arrow(diff(rs.get(key), cs.get(key)))))
    for label, key in (("Modernization pressure", "modernization_pressure"),
                       ("TCO signature (relative)", "tco_burden")):
        bd = burden_delta(rs.get(key), cs.get(key))
        rows.append((label, fmt(rs.get(key)), fmt(cs.get(key)), arrow(bd, False)))
    return rows


def dim_rows(ref, cur):
    rows = []
    for dim in sorted(set(ref["levels"]) | set(cur["levels"])):
        a, b = ref["levels"].get(dim), cur["levels"].get(dim)
        la, lb = (a or {}).get("level"), (b or {}).get("level")
        note = ""
        if a is None:
            note = "newly scored"
        elif b is None:
            note = "no longer scored (N/A)"
        elif a.get("confidence") != b.get("confidence"):
            note = f"confidence {a.get('confidence')} → {b.get('confidence')}"
        rows.append((dim, fmt(la), fmt(lb), arrow(diff(la, lb)), note))
    return rows


def table(head, rows):
    out = ["| " + " | ".join(head) + " |", "|" + "|".join("---" for _ in head) + "|"]
    out += ["| " + " | ".join(r) + " |" for r in rows]
    return "\n".join(out)


def comparability(ref, cur):
    warn = []
    if ref["meta"].get("rubric_hash") != cur["meta"].get("rubric_hash"):
        warn.append("rubrics/scorer changed between these runs (rubric hash differs) — "
                    "deltas may reflect the rubric, not the code")
    return warn


def section(title, ref, cur):
    ra, ca = ref["meta"], cur["meta"]
    lines = [f"## {title}", "",
             f"Reference: `{ref['id']}` ({ra.get('date')}, commit `{ra.get('commit', '')[:9]}`) → "
             f"current: `{cur['id']}` ({ca.get('date')}, commit `{ca.get('commit', '')[:9]}`)", ""]
    for w in comparability(ref, cur):
        lines += [f"> ⚠ Not like-for-like: {w}.", ""]
    lines += ["### Signals", "", table(["Signal", "Reference", "Current", "Change"],
                                        signal_rows(ref, cur)), "",
              "### Dimensions", "", table(["Dimension", "Reference", "Current", "Change", "Note"],
                                          dim_rows(ref, cur)), ""]
    return lines


def write_trend(run, runs):
    cur = next(r for r in runs if r["id"] == run.name)
    idx = runs.index(cur)
    previous = runs[idx - 1] if idx > 0 else None
    baseline = next((r for r in runs if r["id"].endswith(".baseline")), None)

    lines = ["---", "type: Trend", f"run: {cur['id']}",
             "description: Maturity movement against the previous run and the baseline", "---", "",
             "# Maturity trend", "",
             "> Machine-generated by `compare_scorecards.py` — never hand-edit. Finding-level "
             "movement and the explanation of each level change go in `trend-notes.md`.", ""]
    if previous is None:
        lines += ["**Baseline established** — this is the first run; there is nothing to "
                  "compare against yet.", ""]
    else:
        lines += section("Since the previous run", previous, cur)
        if baseline and baseline["id"] not in (cur["id"], previous["id"]):
            lines += section("Since the baseline", baseline, cur)
        elif baseline and baseline["id"] == previous["id"]:
            lines += ["_The previous run is the baseline; see above._", ""]
        elif baseline is None:
            lines += ["> ⚠ No `*.baseline` run found in `.speccen/audits/`.", ""]
        moved = [r for r in dim_rows(previous, cur) if r[3] not in ("=", "—")]
        if moved:
            lines += ["### Level changes that need cited evidence", "",
                      "Each change below must be justified in `trend-notes.md` by changed "
                      "evidence (a file, a commit), otherwise treat it as scoring noise.", ""]
            lines += [f"- {d}: {a} → {b}" for d, a, b, _, _ in moved] + [""]
    (run / "trend.md").write_text("\n".join(lines))
    print(f"Wrote {run / 'trend.md'}")


def write_history(root, runs):
    dims = sorted({d for r in runs for d in r["levels"]})
    head = ["Run", "Date", "Commit", "Avg", "Gate", "Pressure", "TCO"] + dims
    rows = []
    for r in runs:
        s, m = r["summary"], r["meta"]
        rows.append([f"`{r['id']}`", m.get("date", ""), f"`{m.get('commit', '')[:9]}`",
                     fmt(s.get("weighted_average")), fmt(s.get("gating_level")),
                     fmt(s.get("modernization_pressure")), fmt(s.get("tco_burden"))]
                    + [fmt((r["levels"].get(d) or {}).get("level")) for d in dims])
    md = ["---", "type: History", "description: Maturity scores of every audit run, oldest first",
          "---", "", "# Maturity history", "",
          "> Machine-generated by `compare_scorecards.py` — never hand-edit.", "",
          table(head, rows), ""]
    (root / "history.md").write_text("\n".join(md))
    (root / "history.json").write_text(json.dumps(
        [{"id": r["id"], **r["meta"], "signals": {k: v for k, v in r["summary"].items()
                                                   if k != "dimensions"},
          "levels": {d: v.get("level") for d, v in r["levels"].items()}} for r in runs],
        indent=2) + "\n")
    print(f"Wrote {root / 'history.md'} and history.json")


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("command", choices=["stamp", "compare"])
    ap.add_argument("run_dir", help=".speccen/audits/<id>")
    ap.add_argument("--app", default="", help="application name (stamp only)")
    args = ap.parse_args()
    run = pathlib.Path(args.run_dir).resolve()
    if not run.is_dir():
        sys.exit(f"Not a directory: {run}")
    if args.command == "stamp":
        stamp(run, args.app)
        return
    runs = load_all(run.parent)
    if not any(r["id"] == run.name for r in runs):
        sys.exit(f"{run.name} needs run.json (stamp) and summary.json (build_scorecard.py) first")
    # the weights override may have been added after the stamp: refresh this run's hash
    cur = next(r for r in runs if r["id"] == run.name)
    cur["meta"]["rubric_hash"] = rubric_hash(run)
    (run / "run.json").write_text(json.dumps(cur["meta"], indent=2) + "\n")
    write_trend(run, runs)
    write_history(run.parent, runs)


if __name__ == "__main__":
    main()
