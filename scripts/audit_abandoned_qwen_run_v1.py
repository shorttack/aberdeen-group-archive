#!/usr/bin/env python3
"""
audit_abandoned_qwen_run_v1.py
================================
Audit the 309 abandoned Qwen working dirs at
~/Desktop/Archive/_pass_c_abandoned_runs/20260526/prepared/<study>/working/

Goal: decide whether the May 26 Qwen 3.5 27B MLX scores are salvageable as
a Qwen calibration set, avoiding the need to rerun Pass C from scratch.

Context: Pete fired the agent and downgraded to Max on May 26. The agent
quality was bad, but the *model* output was Qwen 27B MLX with the canonical
prescience_score_prompt_v2.md prompt — that should still be sound.

Outputs (written next to this script on Mac):
  - audit_abandoned_qwen_summary_v1.md       human-readable report
  - audit_abandoned_qwen_rows_v1.csv         all raw rows concatenated
  - audit_abandoned_qwen_per_study_v1.csv    one row per study with stats
  - audit_abandoned_qwen_skipped_v1.csv      studies missing the scores csv

Read-only with respect to the archive. Writes only to this script's directory.

Run on Mac:
  cd ~/Desktop/Archive/aberdeen-group-archive
  python3 scripts/audit_abandoned_qwen_run_v1.py
"""
from __future__ import annotations
import csv
import json
import os
import sys
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path

# ---------- paths ----------
ABANDONED_ROOT = Path.home() / "Desktop/Archive/_pass_c_abandoned_runs/20260526/prepared"
MASTER_SCORES  = Path.home() / "Desktop/Archive/aberdeen-group-archive/_master_prescience_scores.csv"
MASTER_OBS     = Path.home() / "Desktop/Archive/aberdeen-group-archive/_master_observations.csv"
OUT_DIR        = Path(__file__).resolve().parent

SCORES_GLOB    = "prescience_scores_*.csv"  # tolerate v1, v2, 27b, 35b, etc.
SKIPPED_FNAME  = "skipped_obs_v1.csv"
FILTER_FNAME   = "filter_summary_v1.json"
SCOREABLE_FNAME = "scoreable_obs_v1.csv"
LOG_FNAME      = "pass_c_log_v1.jsonl"


def short(p: Path) -> str:
    """Compact path for the report."""
    try:
        return str(p.relative_to(Path.home()))
    except ValueError:
        return str(p)


def read_csv_rows(path: Path) -> list[dict]:
    if not path.exists():
        return []
    with path.open(newline="", encoding="utf-8") as fh:
        return list(csv.DictReader(fh))


def main() -> int:
    if not ABANDONED_ROOT.exists():
        print(f"ERROR: {ABANDONED_ROOT} does not exist", file=sys.stderr)
        return 1

    study_dirs = sorted(p for p in ABANDONED_ROOT.iterdir() if p.is_dir())
    print(f"[audit] found {len(study_dirs)} study dirs under {short(ABANDONED_ROOT)}")

    # ---------- gather ----------
    all_rows: list[dict] = []
    per_study: list[dict] = []
    missing_scores: list[dict] = []

    for sdir in study_dirs:
        wdir = sdir / "working"
        score_files = sorted(wdir.glob(SCORES_GLOB)) if wdir.exists() else []

        if not score_files:
            missing_scores.append({
                "study_id": sdir.name,
                "working_dir_exists": wdir.exists(),
                "has_scoreable": (wdir / SCOREABLE_FNAME).exists() if wdir.exists() else False,
                "has_skipped":   (wdir / SKIPPED_FNAME).exists()   if wdir.exists() else False,
                "has_filter":    (wdir / FILTER_FNAME).exists()    if wdir.exists() else False,
                "has_log":       (wdir / LOG_FNAME).exists()       if wdir.exists() else False,
            })
            continue

        study_rows: list[dict] = []
        for sf in score_files:
            for r in read_csv_rows(sf):
                r["_source_file"] = short(sf)
                study_rows.append(r)
        all_rows.extend(study_rows)

        scores = [r.get("prescience_score", "") for r in study_rows]
        confs  = [r.get("confidence", "") for r in study_rows]
        parses = [r.get("parse_ok", "") for r in study_rows]
        models = [r.get("model", "") for r in study_rows]

        per_study.append({
            "study_id":       sdir.name,
            "score_files":    len(score_files),
            "rows":           len(study_rows),
            "parse_ok_true":  sum(1 for p in parses if p == "true"),
            "parse_ok_false": sum(1 for p in parses if p == "false"),
            "score_-1":       scores.count("-1"),
            "score_0":        scores.count("0"),
            "score_1":        scores.count("1"),
            "score_2":        scores.count("2"),
            "score_3":        scores.count("3"),
            "score_4":        scores.count("4"),
            "score_5":        scores.count("5"),
            "conf_1":         confs.count("1"),
            "conf_2":         confs.count("2"),
            "conf_3":         confs.count("3"),
            "model_unique":   "|".join(sorted(set(m for m in models if m))) or "",
        })

    # ---------- global stats ----------
    total_rows = len(all_rows)
    models_c   = Counter(r.get("model", "") for r in all_rows)
    versions_c = Counter(r.get("scorer_version", "") for r in all_rows)
    scores_c   = Counter(r.get("prescience_score", "") for r in all_rows)
    confs_c    = Counter(r.get("confidence", "") for r in all_rows)
    parse_c    = Counter(r.get("parse_ok", "") for r in all_rows)
    src_pass_c = Counter(r.get("source_pass", "") for r in all_rows)

    # ---------- cross-reference master ----------
    master_obs_ids: set[str] = set()
    if MASTER_SCORES.exists():
        for r in read_csv_rows(MASTER_SCORES):
            oid = r.get("obs_id", "")
            if oid:
                master_obs_ids.add(oid)
    abandoned_obs_ids = {r.get("obs_id", "") for r in all_rows if r.get("obs_id")}
    overlap = abandoned_obs_ids & master_obs_ids
    only_in_abandoned = abandoned_obs_ids - master_obs_ids
    only_in_master    = master_obs_ids - abandoned_obs_ids

    # ---------- emit raw rows ----------
    rows_csv = OUT_DIR / "audit_abandoned_qwen_rows_v1.csv"
    if all_rows:
        # union of keys, stable order: schema cols first, then anything extra
        canon = ["obs_id","study_id","model","prescience_score","confidence",
                 "rationale","scored_at","scorer_version","source_pass",
                 "elapsed_sec","parse_ok"]
        extras = sorted({k for r in all_rows for k in r.keys()} - set(canon))
        fields = canon + extras
        with rows_csv.open("w", newline="", encoding="utf-8") as fh:
            w = csv.DictWriter(fh, fieldnames=fields, extrasaction="ignore")
            w.writeheader()
            for r in all_rows:
                w.writerow(r)
        print(f"[audit] wrote {short(rows_csv)} ({total_rows} rows)")

    # ---------- emit per-study ----------
    per_csv = OUT_DIR / "audit_abandoned_qwen_per_study_v1.csv"
    if per_study:
        with per_csv.open("w", newline="", encoding="utf-8") as fh:
            w = csv.DictWriter(fh, fieldnames=list(per_study[0].keys()))
            w.writeheader()
            for r in per_study:
                w.writerow(r)
        print(f"[audit] wrote {short(per_csv)} ({len(per_study)} studies)")

    # ---------- emit skipped ----------
    skip_csv = OUT_DIR / "audit_abandoned_qwen_skipped_v1.csv"
    if missing_scores:
        with skip_csv.open("w", newline="", encoding="utf-8") as fh:
            w = csv.DictWriter(fh, fieldnames=list(missing_scores[0].keys()))
            w.writeheader()
            for r in missing_scores:
                w.writerow(r)
        print(f"[audit] wrote {short(skip_csv)} ({len(missing_scores)} studies w/o scores)")

    # ---------- markdown summary ----------
    summary = OUT_DIR / "audit_abandoned_qwen_summary_v1.md"
    parse_true  = parse_c.get("true", 0)
    parse_false = parse_c.get("false", 0)
    parse_total = parse_true + parse_false
    parse_pct   = (100.0 * parse_true / parse_total) if parse_total else 0.0

    # salvage verdict
    verdict_lines: list[str] = []
    if total_rows == 0:
        verdict = "EMPTY"
        verdict_lines.append("No score rows found in abandoned working dirs. Nothing to salvage.")
    else:
        ok = []
        warn = []
        if parse_pct >= 90:
            ok.append(f"parse_ok rate {parse_pct:.1f}% (≥ 90% target)")
        else:
            warn.append(f"parse_ok rate {parse_pct:.1f}% (below 90% target)")

        scored_real = sum(scores_c.get(s, 0) for s in ("1","2","3","4","5"))
        scored_zero = scores_c.get("0", 0)
        scored_pre  = scores_c.get("-1", 0)
        scored_real_pct = (100.0 * scored_real / total_rows) if total_rows else 0.0
        if scored_real_pct >= 30:
            ok.append(f"{scored_real} rows ({scored_real_pct:.1f}%) scored on 1-5 scale (≥ 30% target)")
        else:
            warn.append(f"only {scored_real} rows ({scored_real_pct:.1f}%) on 1-5 scale")

        if len(models_c) == 1:
            ok.append(f"single model used: {list(models_c.keys())[0]}")
        elif len(models_c) <= 3:
            warn.append(f"{len(models_c)} models mixed: {dict(models_c)}")
        else:
            warn.append(f"{len(models_c)} models mixed — too heterogeneous")

        if len(overlap) >= 100:
            ok.append(f"{len(overlap)} obs overlap with master — direct kappa possible")
        else:
            warn.append(f"only {len(overlap)} obs overlap with master")

        if not warn:
            verdict = "SALVAGE — LOOKS CLEAN"
        elif not ok:
            verdict = "DO NOT SALVAGE"
        else:
            verdict = "MIXED — INSPECT BEFORE DECIDING"
        verdict_lines = [f"- [OK] {x}" for x in ok] + [f"- [WARN] {x}" for x in warn]

    def block(counter: Counter, limit: int = 20) -> str:
        items = counter.most_common(limit)
        if not items:
            return "  (empty)"
        return "\n".join(f"  {n:>6}  {k!r}" for k, n in items)

    summary.write_text(
        f"""# Abandoned May 26 Qwen Run — Salvage Audit

**Audit run**: {datetime.now(timezone.utc).isoformat()}
**Root**: `{short(ABANDONED_ROOT)}`
**Cause of abandonment**: agent quality (Pete fired agent, downgraded Pro→Max). Model output itself not implicated.

## Verdict

**{verdict}**

{chr(10).join(verdict_lines)}

## Topline

| Metric | Value |
|---|---|
| Study dirs found | {len(study_dirs)} |
| Studies with score CSVs | {len(per_study)} |
| Studies missing score CSVs | {len(missing_scores)} |
| Total score rows | {total_rows} |
| parse_ok = true | {parse_true} ({parse_pct:.1f}%) |
| parse_ok = false | {parse_false} |

## Models seen
{block(models_c)}

## Scorer versions seen
{block(versions_c)}

## Score distribution
{block(scores_c)}

## Confidence distribution
{block(confs_c)}

## Source pass values
{block(src_pass_c)}

## Cross-reference with `_master_prescience_scores.csv`

| Set | Count |
|---|---|
| Obs scored in abandoned run | {len(abandoned_obs_ids)} |
| Obs in master scores | {len(master_obs_ids)} |
| Overlap (same obs in both) | {len(overlap)} |
| Only in abandoned | {len(only_in_abandoned)} |
| Only in master | {len(only_in_master)} |

The overlap set is what we can directly compute kappa on — Qwen (from abandoned run) vs Sonar/Claude (from master) on the same obs_id.

## Files written

- `{short(rows_csv)}` — all raw rows concatenated
- `{short(per_csv)}` — one row per study with score histogram
- `{short(skip_csv)}` — studies whose working/ dir has no scores CSV

## Next moves by verdict

- **SALVAGE — LOOKS CLEAN**: build a Qwen calibration manifest by inner-joining `audit_abandoned_qwen_rows_v1.csv` with master scores on `obs_id`, then compute weighted-kappa Qwen-vs-Sonar and Qwen-vs-Claude over the overlap set. No rerun needed.
- **MIXED — INSPECT BEFORE DECIDING**: review the WARN bullets above. Likely need to subset to one model + one scorer_version before kappa.
- **DO NOT SALVAGE / EMPTY**: proceed with v8 driver against `prescience_score_prompt_v2.md`.
""",
        encoding="utf-8",
    )
    print(f"[audit] wrote {short(summary)}")

    # ---------- stdout summary ----------
    print()
    print("=" * 60)
    print(f"VERDICT: {verdict}")
    print("=" * 60)
    print(f"Total rows:     {total_rows}")
    print(f"parse_ok=true:  {parse_true} ({parse_pct:.1f}%)")
    print(f"Studies w/ scores:    {len(per_study)}")
    print(f"Studies w/o scores:   {len(missing_scores)}")
    print(f"Models:         {dict(models_c)}")
    print(f"Versions:       {dict(versions_c)}")
    print(f"Scores:         {dict(scores_c)}")
    print(f"Master overlap: {len(overlap)} obs")
    print()
    print("See:")
    print(f"  {short(summary)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
