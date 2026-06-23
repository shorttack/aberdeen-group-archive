#!/usr/bin/env python3
"""
retire_canonical_dir_v1.py

Retire ~/Desktop/Archive/archive_masters/ as a standalone canonical dir.
After today's reconcile (2026-06-23), the repo working tree at
~/Desktop/Archive/aberdeen-group-archive/ is the single source of truth
for _master_*.csv files.

This script:
  1. Re-runs the audit (calls audit_canonical_vs_repo_masters_v1)
  2. If byte-identical, renames archive_masters/ -> _retired_archive_masters_<TS>/
  3. Writes a sidecar manifest documenting what moved and where
  4. Prints a sed/grep recipe to find any script still hardcoding the old path

Defaults to dry-run. Pass --commit to actually rename.

Usage:
    python3 scripts/retire_canonical_dir_v1.py            # dry-run
    python3 scripts/retire_canonical_dir_v1.py --commit   # rename
"""

from __future__ import annotations

import argparse
import datetime as dt
import hashlib
import json
import os
import subprocess
import sys
from pathlib import Path

CANONICAL = Path.home() / "Desktop" / "Archive" / "archive_masters"
REPO = Path.home() / "Desktop" / "Archive" / "aberdeen-group-archive"
ARCHIVE_PARENT = Path.home() / "Desktop" / "Archive"

MASTERS = [
    "_master_studies.csv",
    "_master_observations.csv",
    "_master_entities.csv",
    "_master_technologies.csv",
    "_master_codes.csv",
    "_master_entity_studies.csv",
    "_master_tech_studies.csv",
]


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def run_audit() -> bool:
    """Inline audit. Returns True if all 7 masters byte-identical."""
    if not CANONICAL.exists() or not REPO.exists():
        return False
    for fname in MASTERS:
        c = CANONICAL / fname
        r = REPO / fname
        if not c.exists() or not r.exists():
            return False
        if sha256_file(c) != sha256_file(r):
            return False
    return True


def inventory_canonical() -> list[dict]:
    """List every file in canonical, with size + sha256."""
    items = []
    for path in sorted(CANONICAL.rglob("*")):
        if path.is_file():
            rel = path.relative_to(CANONICAL)
            items.append(
                {
                    "rel_path": str(rel),
                    "size_bytes": path.stat().st_size,
                    "sha256": sha256_file(path),
                }
            )
    return items


def find_hardcoded_references() -> list[str]:
    """grep for hardcoded refs to archive_masters/ in repo scripts."""
    if not REPO.exists():
        return []
    try:
        result = subprocess.run(
            [
                "grep",
                "-rn",
                "--include=*.py",
                "--include=*.sh",
                "--include=*.md",
                "archive_masters",
                str(REPO / "scripts"),
            ],
            capture_output=True,
            text=True,
            timeout=30,
        )
        if result.returncode in (0, 1):
            return result.stdout.strip().split("\n") if result.stdout.strip() else []
    except (subprocess.TimeoutExpired, FileNotFoundError):
        pass
    return []


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--commit", action="store_true", help="Actually rename (default: dry-run)")
    args = parser.parse_args()

    ts = dt.datetime.now(dt.timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    retired_name = f"_retired_archive_masters_{ts}"
    retired_path = ARCHIVE_PARENT / retired_name

    print(f"Mode: {'COMMIT' if args.commit else 'DRY-RUN'}")
    print(f"Source:      {CANONICAL}")
    print(f"Destination: {retired_path}")
    print()

    # Pre-flight: audit
    print("[1/4] Pre-flight audit (canonical vs repo)...")
    if not run_audit():
        print("[FAIL] Audit failed. Canonical and repo masters are NOT byte-identical.")
        print("       Run scripts/audit_canonical_vs_repo_masters_v1.py for details.")
        print("       Do NOT proceed until reconciled.")
        return 1
    print("       OK - all 7 masters byte-identical")

    # Inventory
    print(f"[2/4] Inventorying {CANONICAL}...")
    items = inventory_canonical()
    total_size = sum(i["size_bytes"] for i in items)
    print(f"       {len(items)} files, {total_size:,} bytes total")

    # Hardcoded refs check
    print("[3/4] Scanning repo scripts for hardcoded archive_masters references...")
    refs = find_hardcoded_references()
    # Filter out lines that reference the retirement itself or the audit script
    refs_relevant = [
        r for r in refs
        if r and not any(s in r for s in [
            "_retired_archive_masters",
            "audit_canonical_vs_repo_masters",
            "retire_canonical_dir",
            "reconcile_masters_canonical_to_repo",
        ])
    ]
    if refs_relevant:
        print(f"       WARNING: {len(refs_relevant)} hardcoded references found:")
        for r in refs_relevant[:20]:
            print(f"         {r}")
        if len(refs_relevant) > 20:
            print(f"         ... and {len(refs_relevant) - 20} more")
        print()
        print("       After retirement, update these to point at the repo working tree.")
    else:
        print("       OK - no hardcoded references in scripts/")

    # Manifest
    manifest = {
        "retirement_timestamp_utc": ts,
        "source": str(CANONICAL),
        "destination": str(retired_path),
        "audit_passed": True,
        "file_count": len(items),
        "total_bytes": total_size,
        "files": items,
        "hardcoded_references_found": len(refs_relevant),
        "hardcoded_references": refs_relevant,
        "rationale": (
            "After 2026-06-23 masters reconcile (commit 2b6976cd), the repo "
            "working tree is the single source of truth. The standalone "
            "archive_masters/ directory is retired to prevent two-tree drift "
            "(9-day drift incident, see _decisions_log.md 2026-06-23)."
        ),
    }
    manifest_path = ARCHIVE_PARENT / f"_retire_canonical_manifest_{ts}.json"

    # Action
    print(f"[4/4] {'Renaming' if args.commit else 'Would rename'}: {CANONICAL.name} -> {retired_name}")
    if args.commit:
        if retired_path.exists():
            print(f"[FAIL] Destination already exists: {retired_path}")
            return 1
        os.rename(CANONICAL, retired_path)
        manifest_path.write_text(json.dumps(manifest, indent=2))
        print(f"       OK - renamed")
        print(f"       Manifest: {manifest_path}")
    else:
        print(f"       [DRY-RUN] would write manifest to {manifest_path}")
        print()
        print("To execute: rerun with --commit")

    print()
    print("Post-retirement reminders:")
    print(f"  - Recovery: mv {retired_path} {CANONICAL}")
    print("  - Update any --archive CLI flags pointing at the old path")
    print(f"  - Canonical is now: {REPO}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
