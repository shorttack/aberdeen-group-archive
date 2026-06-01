#!/usr/bin/env python3
"""
pre_filter_scoreable_obs_v3.py
================================
Pass C v2 pre-filter: produce per-study `scoreable_obs_v3.csv` listing only
observation rows that warrant prescience scoring, filtered to Bucket A and
Bucket B studies (per 2026-05-25 decision memo, narrowed v2 scope).

Rebased for v1.5 archive shape:
  - 1,434 studies in _master_studies.csv (most NOT in prepared/)
  - 23,605 obs in _master_observations.csv (17 cols, v20 canonical obs_ids)
  - Source of truth for bucket: prepared/<study>/manifest.json::assigned_bucket
  - Studies without a manifest are flagged for review, NOT silently dropped

Schema differences from v2 (May 25 abandoned run):
  - Reads v1.5 canonical obs_ids (STANDARD or STANDARD_LETTER_SUFFIX)
  - Emits scoreable_obs_v3.csv (filename bumped to avoid confusion with v1 abandoned outputs)
  - Emits skipped_obs_v3.csv and filter_summary_v3.json (same)
  - Root audit CSV: _bucket_audit_v3.csv (filename bumped)

Scoreable criteria (unchanged from v1):
  An observation is scoreable if its `observation_type` is one of:
    - viability-prediction        (the predictive claim itself)
    - market-data                 (quantitative market claim)
    - strategy-classification     (strategic positioning claim)
    - benchmark-result            (measured performance claim)
    - expert-opinion              (analyst judgment)
    - topic-insight               (synthesized topic claim)
  AND its `metric_value` is non-empty and not '[DEFERRED]' / '[REVIEW]'.

Idempotent: re-running overwrites the per-study v3 outputs in-place.

Usage:
  # dry-run across all studies in prepared/, default bucket filter A,B
  python3 pre_filter_scoreable_obs_v3.py --root /Users/scott/Desktop/Archive/prepared --dry-run

  # commit
  python3 pre_filter_scoreable_obs_v3.py --root /Users/scott/Desktop/Archive/prepared

  # override bucket filter (e.g., add Bucket D)
  python3 pre_filter_scoreable_obs_v3.py --root ... --bucket-filter A,B,D
"""

import argparse
import csv
import json
import os
import sys
from pathlib import Path
from typing import Set

SCOREABLE_OBS_TYPES = {
    "viability-prediction",
    "market-data",
    "strategy-classification",
    "benchmark-result",
    "expert-opinion",
    "topic-insight",
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

        # scoreable_obs_v3.csv
        out_scoreable = working / "scoreable_obs_v3.csv"
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

        # skipped_obs_v3.csv
        out_skipped = working / "skipped_obs_v3.csv"
        with open(out_skipped, "w", newline="") as f:
            w = csv.DictWriter(
                f,
                fieldnames=["obs_id", "study_id", "observation_type", "metric_value", "skip_reason"],
                quoting=csv.QUOTE_ALL,
            )
            w.writeheader()
            w.writerows(skipped_rows)

        # filter_summary_v3.json
        with open(working / "filter_summary_v3.json", "w") as f:
            json.dump({
                "study_id": study_dir.name,
                "total_obs": total,
                "scoreable": len(scoreable_rows),
                "skipped": len(skipped_rows),
                "scorer_version_target": "qwen3.5:27b-mlx_passC_v2",
                "filter_version": "v3",
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
    print(f"Pass C v2 pre-filter (script v3)")
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
    audit_path = args.root / "_bucket_audit_v3.csv"
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
        print(f"Wrote scoreable_obs_v3.csv + skipped_obs_v3.csv + filter_summary_v3.json into {totals['studies_kept']} working/ dirs")
    else:
        print("[DRY-RUN] No files written. Re-run without --dry-run to commit.")

    # ETA hint
    if totals["scoreable_kept"] > 0:
        eta_hours = totals["scoreable_kept"] * 16 / 3600  # 16s/obs effective
        print(f"\nETA at 16 s/obs (qwen3.5:27b-mlx): {eta_hours:.1f} hours wall clock")


if __name__ == "__main__":
    main()
