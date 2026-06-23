#!/usr/bin/env python3
"""
reconcile_masters_canonical_to_repo_v1.py

Reconcile the archive REPO masters working tree with the CANONICAL Desktop-level
archive_masters/ directory. The repo masters have been drifting since Jun 13–14,
2026; canonical has been the actual operating layer (Phase 1+2 reads from it).

DIRECTION: canonical (~/Desktop/Archive/archive_masters/) -> repo
                       (~/Desktop/Archive/aberdeen-group-archive/)

SCOPE: 7 master CSVs at repo root (canonical filenames identical):
  - _master_studies.csv
  - _master_entities.csv
  - _master_technologies.csv
  - _master_observations.csv      (schema shrink expected: 31 cols -> 17 cols)
  - _master_codes.csv
  - _master_entity_studies.csv
  - _master_tech_studies.csv

OUT OF SCOPE (already in sync or unchanged, verified 2026-06-23 09:35 EDT):
  - _master_prescience_scores.csv      (byte-identical size)
  - _master_quotations_prescience.csv  (byte-identical size)
  - _master_entity_field_conflicts.csv (byte-identical size; both stale May 24)

SAFETY:
  - Dry-run by default; --commit required to actually write
  - Backs up ALL 7 repo masters to archive_masters_pre_reconcile_canonical_<UTC>/
    before any write
  - REFUSES to run if canonical row count < repo row count on any file
  - REFUSES to run if any non-observations file has col-count mismatch
  - For _master_observations.csv, the expected schema shrink is 31->17 cols and
    the script will only allow that specific direction (NOT a grow)
  - Sidecar audit CSV emitted: _reconcile_canonical_to_repo_audit_<UTC>.csv

USAGE (on Mac):
  cd ~/Desktop/Archive/aberdeen-group-archive
  python3 scripts/reconcile_masters_canonical_to_repo_v1.py            # dry-run
  python3 scripts/reconcile_masters_canonical_to_repo_v1.py --commit   # write

Author: Pete + agent, 2026-06-23. v1.
"""

from __future__ import annotations

import argparse
import csv
import shutil
import sys
from datetime import datetime, timezone
from pathlib import Path

# Hard-coded paths intentional. These are Pete's Mac layout.
REPO_DIR = Path.home() / "Desktop" / "Archive" / "aberdeen-group-archive"
CANON_DIR = Path.home() / "Desktop" / "Archive" / "archive_masters"

MASTERS = [
    "_master_studies.csv",
    "_master_entities.csv",
    "_master_technologies.csv",
    "_master_observations.csv",
    "_master_codes.csv",
    "_master_entity_studies.csv",
    "_master_tech_studies.csv",
]

# For each file: (expected_repo_cols, expected_canon_cols)
# Any deviation aborts the run unless --force is passed.
EXPECTED_SCHEMA = {
    "_master_studies.csv":         (16, 16),
    "_master_entities.csv":        ( 8,  8),
    "_master_technologies.csv":    ( 8,  8),
    "_master_observations.csv":    (31, 17),  # schema shrink expected
    "_master_codes.csv":           ( 4,  4),
    "_master_entity_studies.csv":  ( 2,  2),
    "_master_tech_studies.csv":    ( 2,  2),
}


def utc_stamp() -> str:
    return datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")


def line_count(path: Path) -> int:
    """Count lines in a file (header + data)."""
    n = 0
    with path.open("rb") as f:
        for _ in f:
            n += 1
    return n


def col_count(path: Path) -> int:
    """Parse the header with csv.reader to count columns honoring quoted commas."""
    with path.open("r", newline="", encoding="utf-8") as f:
        reader = csv.reader(f)
        header = next(reader)
    return len(header)


def measure(path: Path) -> dict:
    if not path.exists():
        return {"exists": False, "lines": 0, "cols": 0, "bytes": 0}
    return {
        "exists": True,
        "lines": line_count(path),
        "cols": col_count(path),
        "bytes": path.stat().st_size,
    }


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--commit", action="store_true",
                    help="Actually write. Default is dry-run.")
    ap.add_argument("--force", action="store_true",
                    help="Bypass schema/row-count safety checks. Use with care.")
    args = ap.parse_args()

    print("=" * 78)
    print("reconcile_masters_canonical_to_repo_v1.py")
    print(f"mode: {'COMMIT' if args.commit else 'dry-run'}")
    print(f"repo : {REPO_DIR}")
    print(f"canon: {CANON_DIR}")
    print("=" * 78)

    # 0. Pre-flight: both dirs exist
    if not REPO_DIR.is_dir():
        print(f"FATAL: repo dir does not exist: {REPO_DIR}", file=sys.stderr)
        return 2
    if not CANON_DIR.is_dir():
        print(f"FATAL: canonical dir does not exist: {CANON_DIR}", file=sys.stderr)
        return 2

    # 1. Measure both sides for every master
    plan = []
    abort_reasons = []
    for name in MASTERS:
        repo_path = REPO_DIR / name
        canon_path = CANON_DIR / name
        repo_m = measure(repo_path)
        canon_m = measure(canon_path)

        if not canon_m["exists"]:
            abort_reasons.append(f"{name}: canonical missing at {canon_path}")
            continue
        if not repo_m["exists"]:
            abort_reasons.append(f"{name}: repo target missing at {repo_path}")
            continue

        # Row-count safety: canonical must be >= repo (a reconcile that drops
        # rows is suspicious; halt unless --force)
        if canon_m["lines"] < repo_m["lines"]:
            abort_reasons.append(
                f"{name}: canonical lines ({canon_m['lines']}) < "
                f"repo lines ({repo_m['lines']}); refusing to drop rows"
            )

        # Schema check: must match EXPECTED_SCHEMA exactly
        exp_repo, exp_canon = EXPECTED_SCHEMA[name]
        if repo_m["cols"] != exp_repo:
            abort_reasons.append(
                f"{name}: repo cols ({repo_m['cols']}) != expected ({exp_repo})"
            )
        if canon_m["cols"] != exp_canon:
            abort_reasons.append(
                f"{name}: canon cols ({canon_m['cols']}) != expected ({exp_canon})"
            )

        plan.append({
            "name": name,
            "repo": repo_m,
            "canon": canon_m,
            "delta_lines": canon_m["lines"] - repo_m["lines"],
            "delta_cols": canon_m["cols"] - repo_m["cols"],
            "delta_bytes": canon_m["bytes"] - repo_m["bytes"],
        })

    # 2. Print plan
    print()
    print(f"{'file':<32} {'repo':>10} {'canon':>10} {'Δlines':>8} {'Δcols':>7}")
    print("-" * 78)
    for p in plan:
        repo_desc = f"{p['repo']['lines']}/{p['repo']['cols']}c"
        canon_desc = f"{p['canon']['lines']}/{p['canon']['cols']}c"
        print(f"{p['name']:<32} {repo_desc:>10} {canon_desc:>10} "
              f"{p['delta_lines']:>+8} {p['delta_cols']:>+7}")
    print()

    # 3. Abort if any safety issue
    if abort_reasons and not args.force:
        print("ABORT — safety checks failed:")
        for r in abort_reasons:
            print(f"  - {r}")
        print()
        print("Re-run with --force only if you have manually verified each issue.")
        return 1
    if abort_reasons and args.force:
        print("WARNING — proceeding past safety checks with --force:")
        for r in abort_reasons:
            print(f"  - {r}")
        print()

    if not args.commit:
        print("DRY-RUN complete. Re-run with --commit to execute.")
        return 0

    # 4. Backup repo masters
    stamp = utc_stamp()
    backup_dir = REPO_DIR / f"archive_masters_pre_reconcile_canonical_{stamp}"
    backup_dir.mkdir(exist_ok=False)
    print(f"Backing up repo masters to: {backup_dir}")
    for p in plan:
        src = REPO_DIR / p["name"]
        dst = backup_dir / p["name"]
        shutil.copy2(src, dst)
        print(f"  backed up: {p['name']}")
    print()

    # 5. Copy canonical -> repo
    print("Copying canonical -> repo:")
    for p in plan:
        src = CANON_DIR / p["name"]
        dst = REPO_DIR / p["name"]
        shutil.copy2(src, dst)
        print(f"  wrote: {p['name']} "
              f"({p['repo']['lines']}->{p['canon']['lines']} lines, "
              f"{p['repo']['cols']}->{p['canon']['cols']} cols)")
    print()

    # 6. Sidecar audit CSV
    audit_path = REPO_DIR / f"_reconcile_canonical_to_repo_audit_{stamp}.csv"
    with audit_path.open("w", newline="", encoding="utf-8") as f:
        w = csv.writer(f, quoting=csv.QUOTE_ALL)
        w.writerow([
            "file",
            "lines_before", "lines_after", "delta_lines",
            "cols_before", "cols_after", "delta_cols",
            "bytes_before", "bytes_after", "delta_bytes",
        ])
        for p in plan:
            w.writerow([
                p["name"],
                p["repo"]["lines"], p["canon"]["lines"], p["delta_lines"],
                p["repo"]["cols"], p["canon"]["cols"], p["delta_cols"],
                p["repo"]["bytes"], p["canon"]["bytes"], p["delta_bytes"],
            ])
    print(f"Audit: {audit_path}")
    print()

    # 7. Verify final state
    print("Post-write verification:")
    ok = True
    for p in plan:
        after = measure(REPO_DIR / p["name"])
        match = (after["lines"] == p["canon"]["lines"]
                 and after["cols"] == p["canon"]["cols"]
                 and after["bytes"] == p["canon"]["bytes"])
        status = "OK" if match else "MISMATCH"
        if not match:
            ok = False
        print(f"  {p['name']}: {after['lines']} lines / "
              f"{after['cols']} cols / {after['bytes']} bytes  [{status}]")

    print()
    if ok:
        print("RECONCILE COMPLETE. All 7 masters now match canonical.")
        print()
        print("Next steps (Mac):")
        print(f"  1. cd {REPO_DIR}")
        print("  2. cd ~/Repos/kastner-aberdeen-wiki")
        print("  3. Re-run Phase 1+2 against the reconciled repo masters:")
        print("     python3 ~/Desktop/Archive/aberdeen-group-archive/scripts/build/01_load_csvs_v3.py \\")
        print(f"       --archive {REPO_DIR} --wiki ~/Repos/kastner-aberdeen-wiki")
        print("     (then 02_build_data_layer_v4.py with same args)")
        print("  4. Verify shape: 1455 studies / 23990 obs / 3291 ent / 4370 tech")
        print("  5. EOD commit on archive repo (masters reconcile, standalone)")
        print("  6. EOD commit on wiki repo (Phase 1-6 outputs, sibling)")
        return 0
    else:
        print("FATAL: post-write verification failed. Backup at:", backup_dir)
        print("Restore with: cp", backup_dir / "*", REPO_DIR / "")
        return 3


if __name__ == "__main__":
    sys.exit(main())
