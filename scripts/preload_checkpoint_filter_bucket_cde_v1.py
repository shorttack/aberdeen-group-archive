#!/usr/bin/env python3
"""
preload_checkpoint_filter_bucket_cde_v1.py
==========================================
Pre-load the Pass C checkpoint with all Bucket C/D/E + UNKNOWN study IDs marked
as "completed", so `run_prescience_pass_c_v1.py` will skip them and process
only the Bucket A+B subset.

Reads `_bucket_audit_v2.csv` (written by pre_filter_scoreable_obs_v2.py) and
identifies every study with kept != "yes". Writes (or merges into) the
checkpoint file at <root>/pass_c_checkpoint_v1.json.

Idempotent: re-running merges with any existing checkpoint, never removes
already-completed study IDs.

Already-completed Bucket A+B studies (e.g. the smoke test's 5 studies) are
preserved. The 5 smoke-test studies remain "completed" so they won't be
re-scored.

Forever-archive: atomic write via .tmp + os.replace.

Usage:
  python3 preload_checkpoint_filter_bucket_cde_v1.py \\
      --root /Users/scott/Desktop/Archive/prepared

  # dry-run (show counts, no write)
  python3 preload_checkpoint_filter_bucket_cde_v1.py \\
      --root /Users/scott/Desktop/Archive/prepared --dry-run
"""
from __future__ import annotations
import argparse
import csv
import json
import os
import sys
from datetime import datetime, timezone
from pathlib import Path


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", required=True,
                    help="Root containing prepared/<study>/ dirs")
    ap.add_argument("--dry-run", action="store_true",
                    help="Show counts, do not write")
    args = ap.parse_args()

    root = Path(args.root).resolve()
    audit_csv = root / "_bucket_audit_v2.csv"
    ckpt_path = root / "pass_c_checkpoint_v1.json"

    if not audit_csv.exists():
        sys.exit(f"ERROR: missing audit CSV. Run pre_filter_scoreable_obs_v2.py "
                 f"first. Expected: {audit_csv}")

    # Load existing checkpoint (preserves smoke-test results)
    existing_completed: list[str] = []
    if ckpt_path.exists():
        with open(ckpt_path, encoding="utf-8") as f:
            ckpt = json.load(f)
        existing_completed = ckpt.get("completed_studies", [])
        print(f"Existing checkpoint: {len(existing_completed)} completed studies")
    else:
        ckpt = {"completed_studies": [], "in_progress": None}
        print("No existing checkpoint — creating fresh")

    existing_set = set(existing_completed)

    # Read audit; collect study_ids where kept != "yes"
    skip_ids: list[tuple[str, str]] = []  # (study_id, bucket)
    keep_ids: list[tuple[str, str]] = []
    no_obs_ids: list[tuple[str, str]] = []
    with open(audit_csv, encoding="utf-8") as f:
        for row in csv.DictReader(f):
            sid = row["study_id"]
            bkt = row["bucket"]
            kept = row["kept"]
            if kept == "yes":
                keep_ids.append((sid, bkt))
            elif kept == "no_obs":
                no_obs_ids.append((sid, bkt))
                # Mark no_obs studies as completed too — driver would skip
                # them anyway, but this keeps the count exact.
                skip_ids.append((sid, bkt))
            else:  # "no" = filtered out by bucket
                skip_ids.append((sid, bkt))

    # New IDs to add to completed
    new_skips = [sid for sid, _ in skip_ids if sid not in existing_set]
    print(f"\nFrom audit CSV:")
    print(f"  Bucket A+B (kept):     {len(keep_ids):>4}")
    print(f"  Filtered out (C/D/E):  {len([s for s,_ in skip_ids if s not in [x for x,_ in no_obs_ids]]):>4}")
    print(f"  No observations:       {len(no_obs_ids):>4}")
    print(f"  Total to mark skip:    {len(skip_ids):>4}")
    print(f"  New IDs (not in checkpoint): {len(new_skips)}")

    # Bucket breakdown of new skips
    bucket_counts: dict[str, int] = {}
    for sid, bkt in skip_ids:
        if sid not in existing_set:
            bucket_counts[bkt] = bucket_counts.get(bkt, 0) + 1
    print(f"\nNew skips by bucket:")
    for b in sorted(bucket_counts):
        print(f"  {b}: {bucket_counts[b]}")

    if args.dry_run:
        print("\n(dry-run) No write performed.")
        return 0

    # Merge: existing + new skips
    merged_set = set(existing_completed) | {sid for sid, _ in skip_ids}
    merged_list = sorted(merged_set)
    ckpt["completed_studies"] = merged_list
    ckpt["last_preload_at"] = datetime.now(timezone.utc).isoformat()
    ckpt["preload_source"] = "preload_checkpoint_filter_bucket_cde_v1.py"
    ckpt["preload_audit"] = str(audit_csv.name)

    tmp = ckpt_path.with_suffix(".json.tmp")
    with open(tmp, "w", encoding="utf-8") as f:
        json.dump(ckpt, f, indent=2, sort_keys=True)
    os.replace(tmp, ckpt_path)

    print(f"\n✓ Wrote {ckpt_path}")
    print(f"  Total completed_studies: {len(merged_list)}")
    print(f"  Expected pending in next driver run: {len(keep_ids) - (len(merged_set) - len(skip_ids))}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
