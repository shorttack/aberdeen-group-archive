#!/usr/bin/env python3
"""
audit_canonical_vs_repo_masters_v1.py

Read-only audit. Confirms ~/Desktop/Archive/aberdeen-group-archive/_master_*.csv
and ~/Desktop/Archive/aberdeen-group-archive/_master_*.csv are byte-identical.

Pre-requisite for retire_canonical_dir_v1.py.

Exits 0 if all 7 masters match byte-for-byte.
Exits 1 if any drift detected (prints diff summary).
Exits 2 if either directory is missing.

Usage:
    python3 scripts/audit_canonical_vs_repo_masters_v1.py
"""

from __future__ import annotations

import hashlib
import os
import sys
from pathlib import Path

CANONICAL = Path.home() / "Desktop" / "Archive" / "aberdeen-group-archive"
REPO = Path.home() / "Desktop" / "Archive" / "aberdeen-group-archive"

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


def file_stats(path: Path) -> tuple[int, int]:
    """Return (size_bytes, line_count)."""
    size = path.stat().st_size
    with path.open("rb") as f:
        lines = sum(1 for _ in f)
    return size, lines


def main() -> int:
    if not CANONICAL.exists():
        print(f"[FAIL] Canonical dir missing: {CANONICAL}")
        return 2
    if not REPO.exists():
        print(f"[FAIL] Repo dir missing: {REPO}")
        return 2

    print(f"Canonical: {CANONICAL}")
    print(f"Repo:      {REPO}")
    print()
    print(f"{'file':<30} {'canonical':<20} {'repo':<20} {'match':<6}")
    print("-" * 80)

    all_match = True
    for fname in MASTERS:
        c = CANONICAL / fname
        r = REPO / fname
        if not c.exists():
            print(f"{fname:<30} MISSING")
            all_match = False
            continue
        if not r.exists():
            print(f"{fname:<30} {'present':<20} MISSING")
            all_match = False
            continue
        c_size, c_lines = file_stats(c)
        r_size, r_lines = file_stats(r)
        c_hash = sha256_file(c)
        r_hash = sha256_file(r)
        match = c_hash == r_hash
        if not match:
            all_match = False
        c_desc = f"{c_size}b/{c_lines}L"
        r_desc = f"{r_size}b/{r_lines}L"
        marker = "OK" if match else "DRIFT"
        print(f"{fname:<30} {c_desc:<20} {r_desc:<20} {marker}")
        if not match:
            print(f"  canonical sha256: {c_hash}")
            print(f"  repo      sha256: {r_hash}")

    print()
    if all_match:
        print("[OK] All 7 masters byte-identical. Safe to retire canonical dir.")
        return 0
    print("[FAIL] Drift detected. Do NOT retire canonical until reconciled.")
    return 1


if __name__ == "__main__":
    sys.exit(main())
