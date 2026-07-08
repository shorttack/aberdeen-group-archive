#!/usr/bin/env python3
"""
pre_filter_scoreable_obs_v5.py
================================
Pass C v2 pre-filter: produce per-study `scoreable_obs_v5.csv` listing only
observation rows that warrant prescience scoring, filtered to Bucket A and
Bucket B studies (per 2026-05-25 decision memo, narrowed v2 scope).

v5 changes (§11q, 2026-06-02):
  - scorer_version_target string now built from _llm_helper_v3.LOCAL_MODEL
    (single source of truth for the local model name). New value:
    "qwen3.6:27b-mlx_passC_v2" instead of v4's "qwen3.5:27b-mlx_passC_v2".
    No downstream consumer reads this exact string (verified via GH code
    search 2026-06-02); it's human-readable provenance written into each
    study's filter_summary_v5.json.
  - Output filenames bumped: scoreable_obs_v5.csv, skipped_obs_v5.csv,
    filter_summary_v5.json, _bucket_audit_v5.csv. v4 outputs preserved
    forever (per forever-archive principle); v5 runs alongside, do not
    overwrite.
  - ETA print updated to reference current model name dynamically.
  - Requires _llm_helper_v2.py to be importable (sys.path or copied into
    same dir). Falls back to hardcoded 3.6 string if import fails, with
    a printed warning.

Rebased for v1.5 archive shape:
  - 1,434 studies in _master_studies.csv (most NOT in prepared/)
  - 23,605 obs in _master_observations.csv (17 cols, v20 canonical obs_ids)
  - Source of truth for bucket: prepared/<study>/manifest.json::assigned_bucket
  - Studies without a manifest are flagged for review, NOT silently dropped

Schema differences from v2 (May 25 abandoned run):
  - Reads v1.5 canonical obs_ids (STANDARD or STANDARD_LETTER_SUFFIX)
  - Emits scoreable_obs_v5.csv (§11q bump to track Qwen 3.6 model swap)
  - Emits skipped_obs_v5.csv and filter_summary_v5.json (same)
  - Root audit CSV: _bucket_audit_v5.csv (filename bumped)

Scoreable criteria (unchanged from v1):
  An observation is scoreable if its `observation_type` is one of:
    - viability-prediction        (the predictive claim itself)
    - market-data                 (quantitative market claim)
    - strategy-classification     (strategic positioning claim)
    - benchmark-result            (measured performance claim)
    - expert-opinion              (analyst judgment)
    - topic-insight               (synthesized topic claim)
  AND its `metric_value` is non-empty and not '[DEFERRED]' / '[REVIEW]'.

Idempotent: re-running overwrites the per-study v4 outputs in-place.

Usage:
  # dry-run across all studies in prepared/, default bucket filter A,B
  python3 pre_filter_scoreable_obs_v4.py --root /Users/scott/Desktop/Archive/prepared --dry-run

  # commit
  python3 pre_filter_scoreable_obs_v4.py --root /Users/scott/Desktop/Archive/prepared

  # override bucket filter (e.g., add Bucket D)
  python3 pre_filter_scoreable_obs_v4.py --root ... --bucket-filter A,B,D
"""

import argparse
import csv
import json
import os
import sys
from pathlib import Path
from typing import Set

# §11q (2026-06-02): single source of truth for the local model.
# Try to import from build/_llm_helper_v2.py; fall back with a warning if the
# helper isn't on sys.path (e.g., script copied somewhere weird). Hardcoded
# fallback MUST match _llm_helper_v2.LOCAL_MODEL exactly.
try:
    # When running from ~/Desktop/Archive/scripts/, the build dir is a sibling.
    _here = Path(__file__).resolve().parent
    if (_here / "build" / "_llm_helper_v3.py").exists():
        sys.path.insert(0, str(_here / "build"))
    from _llm_helper_v3 import LOCAL_MODEL, scorer_version_target
    SCORER_VERSION_TARGET = scorer_version_target("passC_v2")
except ImportError as _e:
    print(f"[pre_filter v5] WARNING: could not import _llm_helper_v2 ({_e}); "
          "using hardcoded fallback. Update LOCAL_MODEL in helper to change.",
          file=sys.stderr)
    LOCAL_MODEL = "qwen3.6:27b-mlx"
    SCORER_VERSION_TARGET = f"{LOCAL_MODEL}_passC_v2"

SCOREABLE_OBS_TYPES = {
    # v3 original (v1.5 ingest skill §6 catalog)
    "viability-prediction",
    "market-data",
    "strategy-classification",
    "benchmark-result",
    "expert-opinion",
    "topic-insight",
    # v4 additions (2026-05-29) — discovered in live A+B audit
    # These are the actual types used in RA- / bm- / ra- Aberdeen studies.
    # Moderate scope: forward-looking judgments only, not raw data points.
    "market-forecast",         # explicit predictions about future market state
    "market-assessment",       # often forward-looking market judgment
    "competitive-assessment",  # who-will-win analyses
    "analytical-claim",        # mixed; model will return low confidence on non-predictive rows
    # NOT included (moderate scope cutoff):
    #   market-metric, financial-metric: historical data points, no prediction to score
    #   study-summary: meta about the study itself
    #   framework: taxonomic; rarely predictive
    #   market-condition: usually current-state, not forward-looking
}
NON_SCOREABLE_VALUES = {"", "[DEFERRED]", "[REVIEW]", "n/a", "tbd", "unknown"}


def load_manifest_bucket(study_dir: Path) -> tuple[str, bool]:
    """Returns (bucket, has_manifest). Bucket is UNKNOWN if no manifest."""
    manifest = study_dir / "manifest.json"
    if not manifest.exists():
        return ("UNKNOWN", False)
    try:
        with open(manifest) as f:
            m = json.load(f)
        # assigned_bucket is operator-set source of truth
        b = m.get("assigned_bucket") or m.get("bucket") or "UNKNOWN"
        return (str(b).strip().upper(), True)
    except Exception as e:
        print(f"  [WARN] {study_dir.name}: manifest.json unreadable ({e})", file=sys.stderr)
        return ("UNKNOWN", False)


def filter_study(study_dir: Path, dry_run: bool) -> dict:
    """Returns a stats dict for the audit CSV."""
    obs_csv = study_dir / "data" / "observations.csv"
    if not obs_csv.exists():
        return {
            "study_id": study_dir.name, "bucket": "UNKNOWN", "predicted_bucket": "",
            "kept": False, "total_obs": 0, "scoreable": 0, "skipped": 0,
            "no_manifest": True, "no_observations": True,
        }

    with open(obs_csv, newline="") as f:
        reader = csv.DictReader(f)
        rows = list(reader)
    total = len(rows)

    scoreable_rows = []
    skipped_rows = []
    for row in rows:
        otype = (row.get("observation_type") or "").strip()
        mvalue = (row.get("metric_value") or "").strip()
        is_scoreable = (otype in SCOREABLE_OBS_TYPES and
                        mvalue.lower() not in NON_SCOREABLE_VALUES and
                        mvalue not in NON_SCOREABLE_VALUES)
        if is_scoreable:
            scoreable_rows.append(row)
        else:
            skipped_rows.append({
                **{k: row.get(k, "") for k in ("obs_id", "study_id", "observation_type", "metric_value")},
                "skip_reason": ("not-scoreable-type" if otype not in SCOREABLE_OBS_TYPES else "empty-or-deferred-value"),
            })

    if not dry_run:
        working = study_dir / "working"
        working.mkdir(exist_ok=True)

        # scoreable_obs_v4.csv
        out_scoreable = working / "scoreable_obs_v4.csv"
        if scoreable_rows:
            fieldnames = list(scoreable_rows[0].keys())
            with open(out_scoreable, "w", newline="") as f:
                w = csv.DictWriter(f, fieldnames=fieldnames, quoting=csv.QUOTE_ALL)
                w.writeheader()
                w.writerows(scoreable_rows)
        else:
            # Empty file with header from observations.csv if no rows
            with open(out_scoreable, "w", newline="") as f:
                w = csv.writer(f, quoting=csv.QUOTE_ALL)
                if rows:
                    w.writerow(list(rows[0].keys()))

        # skipped_obs_v4.csv
        out_skipped = working / "skipped_obs_v4.csv"
        with open(out_skipped, "w", newline="") as f:
            w = csv.DictWriter(
                f,
                fieldnames=["obs_id", "study_id", "observation_type", "metric_value", "skip_reason"],
                quoting=csv.QUOTE_ALL,
            )
            w.writeheader()
            w.writerows(skipped_rows)

        # filter_summary_v4.json
        with open(working / "filter_summary_v4.json", "w") as f:
            json.dump({
                "study_id": study_dir.name,
                "total_obs": total,
                "scoreable": len(scoreable_rows),
                "skipped": len(skipped_rows),
                "scorer_version_target": SCORER_VERSION_TARGET,
                "filter_version": "v5",
            }, f, indent=2)

    return {
        "study_id": study_dir.name,
        "bucket": "",  # filled by caller
        "predicted_bucket": "",  # filled by caller
        "kept": False,  # filled by caller
        "total_obs": total,
        "scoreable": len(scoreable_rows),
        "skipped": len(skipped_rows),
        "no_manifest": False,
        "no_observations": False,
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", required=True, type=Path,
                    help="Path to prepared/ directory")
    ap.add_argument("--bucket-filter", default="A,B",
                    help="Comma-separated bucket codes to keep (default: A,B)")
    ap.add_argument("--dry-run", action="store_true",
                    help="Report only; do not write any files")
    args = ap.parse_args()

    if not args.root.is_dir():
        sys.exit(f"--root not a directory: {args.root}")

    keep_buckets: Set[str] = {b.strip().upper() for b in args.bucket_filter.split(",") if b.strip()}
    print(f"Pass C v2 pre-filter (script v4)")
    print(f"Root: {args.root}")
    print(f"Bucket filter: {sorted(keep_buckets)}")
    print(f"Mode: {'DRY-RUN' if args.dry_run else 'COMMIT'}")
    print()

    study_dirs = sorted([d for d in args.root.iterdir() if d.is_dir() and not d.name.startswith("_")])
    print(f"Found {len(study_dirs)} study dirs in prepared/")
    print()

    audit_rows = []
    totals = {"total_obs": 0, "scoreable_kept": 0, "skipped_kept": 0,
              "studies_kept": 0, "studies_excluded_bucket": 0,
              "studies_no_manifest": 0, "studies_no_obs": 0}
    bucket_counts = {}

    for d in study_dirs:
        bucket, has_manifest = load_manifest_bucket(d)
        bucket_counts[bucket] = bucket_counts.get(bucket, 0) + 1
        kept = (bucket in keep_buckets)

        if not has_manifest:
            totals["studies_no_manifest"] += 1
            audit_rows.append({
                "study_id": d.name, "bucket": "UNKNOWN", "predicted_bucket": "",
                "kept": False, "total_obs": "", "scoreable": "", "skipped": "",
                "no_manifest": True, "no_observations": "",
            })
            continue

        if not kept:
            totals["studies_excluded_bucket"] += 1
            audit_rows.append({
                "study_id": d.name, "bucket": bucket, "predicted_bucket": "",
                "kept": False, "total_obs": "", "scoreable": "", "skipped": "",
                "no_manifest": False, "no_observations": "",
            })
            continue

        # Bucket A or B with manifest: run filter
        stats = filter_study(d, args.dry_run)
        stats["bucket"] = bucket
        stats["kept"] = not stats["no_observations"]
        if stats["no_observations"]:
            totals["studies_no_obs"] += 1
        else:
            totals["studies_kept"] += 1
            totals["total_obs"] += stats["total_obs"]
            totals["scoreable_kept"] += stats["scoreable"]
            totals["skipped_kept"] += stats["skipped"]
        audit_rows.append(stats)

    # Emit root audit CSV
    audit_path = args.root / "_bucket_audit_v4.csv"
    if not args.dry_run:
        with open(audit_path, "w", newline="") as f:
            w = csv.DictWriter(
                f,
                fieldnames=["study_id", "bucket", "predicted_bucket", "kept",
                            "total_obs", "scoreable", "skipped",
                            "no_manifest", "no_observations"],
                quoting=csv.QUOTE_ALL,
            )
            w.writeheader()
            w.writerows(audit_rows)

    # Report
    print("Bucket distribution (all 493 prepared/ study dirs):")
    for b, c in sorted(bucket_counts.items()):
        marker = " <- KEEP" if b in keep_buckets else ""
        print(f"  {b}: {c}{marker}")
    print()
    print("Totals for kept studies:")
    print(f"  Studies kept (Bucket A+B with manifest, has observations): {totals['studies_kept']}")
    print(f"  Studies excluded by bucket filter: {totals['studies_excluded_bucket']}")
    print(f"  Studies with no manifest (flagged): {totals['studies_no_manifest']}")
    print(f"  Studies with no observations (flagged): {totals['studies_no_obs']}")
    print(f"  Total observations across kept studies: {totals['total_obs']}")
    print(f"  Scoreable observations across kept studies: {totals['scoreable_kept']}")
    print(f"  Skipped observations across kept studies: {totals['skipped_kept']}")
    print()
    if not args.dry_run:
        print(f"Wrote audit: {audit_path}")
        print(f"Wrote scoreable_obs_v4.csv + skipped_obs_v4.csv + filter_summary_v4.json into {totals['studies_kept']} working/ dirs")
    else:
        print("[DRY-RUN] No files written. Re-run without --dry-run to commit.")

    # ETA hint
    if totals["scoreable_kept"] > 0:
        eta_hours = totals["scoreable_kept"] * 16 / 3600  # 16s/obs effective
        print(f"\nETA at 16 s/obs ({LOCAL_MODEL}): {eta_hours:.1f} hours wall clock")


if __name__ == "__main__":
    main()
