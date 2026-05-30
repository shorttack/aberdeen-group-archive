#!/usr/bin/env python3
"""
roll_up_prescience_v3.py — Roll per-observation Pass C scores up to
study-level prescience (high / medium / low / not-applicable) and write
back to _master_studies.csv for the [DEFERRED] cohort only.

Canonical reference: readme_prescience.md (root of aberdeen-group-archive).

Rule A (mean threshold over non-prefilter obs):
    obs_used = scores where prescience_score != -1
    if len(obs_used) == 0:
        verdict = "not-applicable"
        rationale = "Pass C found no scorable forward-looking observations
                     after prefilter."
    else:
        mean = sum(scores) / len(obs_used)
        if mean >= 3.5:   verdict = "high"
        elif mean >= 2.0: verdict = "medium"
        else:             verdict = "low"
        rationale = templated 1-2 sentence summary including mean,
                    obs count, and a short distribution note.

Only [DEFERRED] studies in _master_studies.csv are touched. Existing
high / medium / low / not-applicable ratings are left untouched, even
when today's Pass C scored their observations.

Standard invariants (per kastner-archive-pipeline skill):
  - Default mode is DRY-RUN. --commit required to write.
  - Timestamped backup of _master_studies.csv before any write.
  - csv.QUOTE_ALL on every CSV write.
  - Row-count parity (before/after).
  - Audit trail CSV emitted alongside the master rewrite.

Usage:
    python3 roll_up_prescience_v3.py            # dry-run, prints planned changes
    python3 roll_up_prescience_v3.py --commit   # apply
"""

import csv
import datetime
import shutil
import sys
from collections import Counter
from pathlib import Path

ARCHIVE = Path.home() / "Desktop/Archive/archive_masters"
STUDIES = ARCHIVE / "_master_studies.csv"
SCORES  = ARCHIVE / "_master_prescience_scores.csv"

# Threshold rule A (canonical, this script):
THRESH_HIGH   = 3.5
THRESH_MEDIUM = 2.0

# Audit columns we write to _master_studies.csv
PRESCIENCE_COL = "prescience"
RATIONALE_COL  = "prescience_rationale"

# Marker we will REPLACE.
DEFERRED = "[DEFERRED]"

commit_mode = "--commit" in sys.argv


def load_scores(path: Path) -> dict[str, list[tuple[int, int]]]:
    """Return {study_id: [(score, confidence), ...]} as ints."""
    by_study: dict[str, list[tuple[int, int]]] = {}
    with open(path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            sid = row["study_id"]
            try:
                score = int(row["prescience_score"])
            except (TypeError, ValueError):
                continue
            try:
                conf = int(row["confidence"])
            except (TypeError, ValueError):
                conf = 0
            by_study.setdefault(sid, []).append((score, conf))
    return by_study


def classify(scores: list[tuple[int, int]]) -> tuple[str, str, dict]:
    """
    Apply Rule A. Return (verdict, rationale, stats_dict).
    stats_dict is for the audit CSV.
    """
    used = [s for s, _ in scores if s != -1]
    n_total = len(scores)
    n_prefilter = n_total - len(used)
    n_used = len(used)

    if n_used == 0:
        return (
            "not-applicable",
            (
                f"Pass C found no scorable forward-looking observations "
                f"after prefilter ({n_prefilter} of {n_total} obs marked "
                f"non-forward-looking; 0 sent to scorer)."
            ),
            {
                "n_total_obs": n_total,
                "n_prefilter": n_prefilter,
                "n_used": 0,
                "mean": "",
                "distribution": "",
            },
        )

    mean = sum(used) / n_used
    if mean >= THRESH_HIGH:
        verdict = "high"
    elif mean >= THRESH_MEDIUM:
        verdict = "medium"
    else:
        verdict = "low"

    # short distribution note: counts of 0-5
    bucket_counts = Counter(used)
    dist_parts = [f"{bucket_counts.get(i, 0)}x{i}" for i in range(6) if bucket_counts.get(i, 0)]
    distribution = ", ".join(dist_parts)

    rationale = (
        f"Pass C cloud rollup (rule A, mean={mean:.2f} over {n_used} obs; "
        f"distribution: {distribution}). "
        f"{n_prefilter} additional obs were prefiltered as non-forward-looking."
    )

    return (
        verdict,
        rationale,
        {
            "n_total_obs": n_total,
            "n_prefilter": n_prefilter,
            "n_used": n_used,
            "mean": f"{mean:.4f}",
            "distribution": distribution,
        },
    )


def main() -> int:
    if not STUDIES.exists():
        sys.exit(f"Missing: {STUDIES}")
    if not SCORES.exists():
        sys.exit(f"Missing: {SCORES}")

    # 1. Load scores keyed by study_id.
    scores_by_study = load_scores(SCORES)
    print(f"[load] _master_prescience_scores.csv: "
          f"{sum(len(v) for v in scores_by_study.values())} rows, "
          f"{len(scores_by_study)} distinct studies")

    # 2. Load studies master.
    with open(STUDIES, newline="", encoding="utf-8") as f:
        reader = csv.reader(f)
        header = next(reader)
        rows = list(reader)
    if PRESCIENCE_COL not in header or RATIONALE_COL not in header:
        sys.exit(f"_master_studies.csv missing required columns: "
                 f"{PRESCIENCE_COL!r} / {RATIONALE_COL!r}")
    pres_idx = header.index(PRESCIENCE_COL)
    rat_idx  = header.index(RATIONALE_COL)
    sid_idx  = header.index("study_id")
    n_rows_before = len(rows)
    print(f"[load] _master_studies.csv: {n_rows_before} rows, {len(header)} cols")

    # 3. Plan changes — only [DEFERRED] rows that have scores.
    plan: list[dict] = []
    skipped_no_scores = 0
    skipped_not_deferred = 0
    for r in rows:
        sid = r[sid_idx]
        cur = (r[pres_idx] or "").strip()
        if cur != DEFERRED:
            skipped_not_deferred += 1
            continue
        if sid not in scores_by_study:
            skipped_no_scores += 1
            continue
        verdict, rationale, stats = classify(scores_by_study[sid])
        plan.append({
            "study_id": sid,
            "old_prescience": cur,
            "new_prescience": verdict,
            "new_rationale": rationale,
            **stats,
        })

    # 4. Report.
    bucket_dist = Counter(p["new_prescience"] for p in plan)
    print()
    print(f"=== Plan ===")
    print(f"  [DEFERRED] studies in master that have Pass C scores: {len(plan)}")
    print(f"  [DEFERRED] studies in master WITHOUT scores (left as-is): "
          f"{skipped_no_scores}")
    print(f"  Non-[DEFERRED] studies (left as-is): {skipped_not_deferred}")
    print(f"  New bucket distribution:")
    for k in ("high", "medium", "low", "not-applicable"):
        print(f"    {k:>16}: {bucket_dist.get(k, 0)}")

    # 5. Always write the audit CSV (dry-run gets one too).
    ts = datetime.datetime.utcnow().strftime("%Y%m%dT%H%M%SZ")
    audit_path = ARCHIVE / f"_rollup_v3_audit_{ts}.csv"
    audit_cols = [
        "study_id", "old_prescience", "new_prescience",
        "n_total_obs", "n_prefilter", "n_used", "mean", "distribution",
        "new_rationale",
    ]
    with open(audit_path, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f, quoting=csv.QUOTE_ALL)
        w.writerow(audit_cols)
        for p in plan:
            w.writerow([p[c] for c in audit_cols])
    print(f"\n[audit] wrote {audit_path} ({len(plan)} rows)")

    # 6. Commit if requested.
    if not commit_mode:
        print("\nDRY-RUN — pass --commit to write _master_studies.csv")
        return 0

    # backup
    bak = STUDIES.with_suffix(f".csv.bak_rollup_v3_{ts}")
    shutil.copy2(STUDIES, bak)
    print(f"\n[backup] {bak}")

    # apply
    plan_by_sid = {p["study_id"]: p for p in plan}
    for r in rows:
        sid = r[sid_idx]
        if sid in plan_by_sid:
            r[pres_idx] = plan_by_sid[sid]["new_prescience"]
            r[rat_idx]  = plan_by_sid[sid]["new_rationale"]

    # row-count parity
    assert len(rows) == n_rows_before, \
        f"Row-count drift: {len(rows)} != {n_rows_before}"

    with open(STUDIES, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f, quoting=csv.QUOTE_ALL)
        w.writerow(header)
        w.writerows(rows)
    print(f"[write] {STUDIES} — {len(rows)} rows, {len(header)} cols (unchanged)")
    print(f"[done] applied {len(plan)} prescience updates.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
