#!/usr/bin/env python3
"""
audit_schema_and_overlap_v1.py
==============================

READ-ONLY follow-up to audit_mac_vs_repo_v1.py. Answers two questions for
the three drifted masters where repo > Mac in row count:

  Q1: What COLUMN does the repo's _master_entities.csv (9c) have that the
      Mac's (8c) doesn't? Same for _master_technologies.csv.

  Q2: For each of _master_entities.csv, _master_technologies.csv, and
      _master_codes.csv: is the Mac's set of ID values a strict SUBSET
      of the repo's? Or is there mutual divergence?

Output: prints a structured report to stdout AND writes
  /Users/scott/Desktop/Archive/_audit_schema_overlap_<UTCstamp>.json

No archive files are modified. Read-only against both sides.

Usage:
    python3 audit_schema_and_overlap_v1.py

Requires `gh` CLI authenticated for shorttack/aberdeen-group-archive.
"""

from __future__ import annotations

import base64
import csv
import datetime as dt
import io
import json
import shutil
import subprocess
import sys
from pathlib import Path

MAC_ROOT = Path.home() / "Desktop/Archive/aberdeen-group-archive"
REPO = "shorttack/aberdeen-group-archive"
REPO_BRANCH = "main"

# (filename, primary_key_column_on_mac, primary_key_column_on_repo_if_different)
# We'll auto-detect the key column from header rather than hardcoding so it's
# robust to renames. For _master_codes.csv, the key is methodology_code (or
# whatever appears in column 0 of its header).
TARGETS = [
    "_master_entities.csv",
    "_master_technologies.csv",
    "_master_codes.csv",
]


def gh_check() -> None:
    if shutil.which("gh") is None:
        print("FATAL: gh CLI not on PATH", file=sys.stderr)
        sys.exit(2)


def gh_get_file_meta(filename: str) -> dict:
    cmd = ["gh", "api", f"/repos/{REPO}/contents/{filename}?ref={REPO_BRANCH}"]
    p = subprocess.run(cmd, capture_output=True, text=True)
    if p.returncode != 0:
        raise RuntimeError(
            f"gh api /contents/{filename} failed: {p.stderr.strip()[:300]}"
        )
    return json.loads(p.stdout)


def gh_get_blob(blob_sha: str) -> bytes:
    cmd = ["gh", "api", f"/repos/{REPO}/git/blobs/{blob_sha}"]
    p = subprocess.run(cmd, capture_output=True, text=True)
    if p.returncode != 0:
        raise RuntimeError(f"gh api blob failed: {p.stderr.strip()[:300]}")
    payload = json.loads(p.stdout)
    return base64.b64decode(payload["content"])


def parse_csv_from_path(path: Path) -> tuple[list[str], list[list[str]]]:
    with open(path, "r", newline="", encoding="utf-8") as f:
        reader = csv.reader(f)
        header = next(reader)
        rows = list(reader)
    return header, rows


def parse_csv_from_bytes(data: bytes) -> tuple[list[str], list[list[str]]]:
    f = io.StringIO(data.decode("utf-8"))
    reader = csv.reader(f)
    header = next(reader)
    rows = list(reader)
    return header, rows


def first_col_value(row: list[str], colcount: int) -> str:
    """Returns the value in column 0, safely handling short rows."""
    if not row:
        return ""
    return row[0]


def value_at(row: list[str], idx: int) -> str:
    if 0 <= idx < len(row):
        return row[idx]
    return ""


def audit_one_target(filename: str) -> dict:
    report: dict = {
        "file": filename,
        "mac": {},
        "repo": {},
        "schema_diff": {},
        "overlap": {},
    }

    # --- Mac side ---
    mac_path = MAC_ROOT / filename
    if not mac_path.is_file():
        report["mac"]["error"] = "MISSING"
        return report
    mac_header, mac_rows = parse_csv_from_path(mac_path)
    report["mac"]["header"] = mac_header
    report["mac"]["rows"] = len(mac_rows)
    report["mac"]["cols"] = len(mac_header)

    # --- Repo side ---
    try:
        meta = gh_get_file_meta(filename)
    except RuntimeError as e:
        report["repo"]["error"] = str(e)
        return report
    blob = gh_get_blob(meta["sha"])
    repo_header, repo_rows = parse_csv_from_bytes(blob)
    report["repo"]["header"] = repo_header
    report["repo"]["rows"] = len(repo_rows)
    report["repo"]["cols"] = len(repo_header)
    report["repo"]["blob_sha"] = meta["sha"]

    # --- Schema diff ---
    mac_set = set(mac_header)
    repo_set = set(repo_header)
    report["schema_diff"]["only_in_repo"] = sorted(repo_set - mac_set)
    report["schema_diff"]["only_in_mac"] = sorted(mac_set - repo_set)
    report["schema_diff"]["common"] = sorted(mac_set & repo_set)

    # --- Overlap on primary key (column 0 by convention) ---
    if not mac_header or not repo_header:
        report["overlap"]["error"] = "empty header"
        return report

    mac_key_col = mac_header[0]
    repo_key_col = repo_header[0]
    report["overlap"]["mac_key_col"] = mac_key_col
    report["overlap"]["repo_key_col"] = repo_key_col

    mac_keys = {value_at(r, 0) for r in mac_rows if r}
    repo_keys = {value_at(r, 0) for r in repo_rows if r}

    both = mac_keys & repo_keys
    mac_only = mac_keys - repo_keys
    repo_only = repo_keys - mac_keys

    report["overlap"]["mac_unique_keys"] = len(mac_keys)
    report["overlap"]["repo_unique_keys"] = len(repo_keys)
    report["overlap"]["in_both"] = len(both)
    report["overlap"]["mac_only"] = len(mac_only)
    report["overlap"]["repo_only"] = len(repo_only)

    report["overlap"]["mac_subset_of_repo"] = len(mac_only) == 0
    report["overlap"]["repo_subset_of_mac"] = len(repo_only) == 0
    report["overlap"]["disjoint_count"] = len(mac_only) + len(repo_only)

    # Sample 5 from each side for eyeballing
    report["overlap"]["sample_mac_only"] = sorted(mac_only)[:5]
    report["overlap"]["sample_repo_only"] = sorted(repo_only)[:5]
    report["overlap"]["sample_in_both"] = sorted(both)[:5]

    # If a Mac key is in the repo, are the row values different too? Sample 3.
    samples = []
    repo_by_key = {value_at(r, 0): r for r in repo_rows if r}
    mac_by_key = {value_at(r, 0): r for r in mac_rows if r}
    for k in sorted(both)[:3]:
        samples.append(
            {
                "key": k,
                "mac_row": mac_by_key[k],
                "repo_row": repo_by_key[k],
            }
        )
    report["overlap"]["sample_shared_rows"] = samples

    return report


def main() -> int:
    if not MAC_ROOT.is_dir():
        print(f"FATAL: {MAC_ROOT} not found", file=sys.stderr)
        return 2
    gh_check()

    ts = dt.datetime.now(dt.timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    out_path = MAC_ROOT.parent / f"_audit_schema_overlap_{ts}.json"

    print(f"Schema + overlap audit @ {dt.datetime.now().isoformat(timespec='seconds')}")
    print(f"Mac : {MAC_ROOT}")
    print(f"Repo: {REPO}  branch={REPO_BRANCH}")
    print()

    all_reports = []
    for fn in TARGETS:
        print(f"--- {fn} ---")
        rep = audit_one_target(fn)
        all_reports.append(rep)

        if rep.get("repo", {}).get("error") or rep.get("mac", {}).get("error"):
            print(f"  ERROR: {rep.get('repo', {}).get('error') or rep.get('mac', {}).get('error')}")
            print()
            continue

        m = rep["mac"]
        r = rep["repo"]
        s = rep["schema_diff"]
        o = rep["overlap"]
        print(f"  Mac : {m['rows']:>6} rows x {m['cols']} cols")
        print(f"  Repo: {r['rows']:>6} rows x {r['cols']} cols  ({r['blob_sha'][:10]})")
        print(f"  Schema columns only in REPO : {s['only_in_repo']}")
        print(f"  Schema columns only in MAC  : {s['only_in_mac']}")
        print(f"  Key column: mac={o['mac_key_col']!r}  repo={o['repo_key_col']!r}")
        print(f"  Unique keys: mac={o['mac_unique_keys']}  repo={o['repo_unique_keys']}")
        print(f"  In both    : {o['in_both']}")
        print(f"  Mac-only   : {o['mac_only']}      (Mac has these, repo doesn't)")
        print(f"  Repo-only  : {o['repo_only']}     (repo has these, Mac doesn't)")
        print(f"  Mac is subset of repo? {o['mac_subset_of_repo']}")
        print(f"  Repo is subset of Mac? {o['repo_subset_of_mac']}")
        if o["sample_mac_only"]:
            print(f"  Sample Mac-only keys : {o['sample_mac_only']}")
        if o["sample_repo_only"]:
            print(f"  Sample repo-only keys: {o['sample_repo_only']}")
        if o["sample_shared_rows"]:
            print(f"  Sample shared rows (first 3 keys present on both sides):")
            for s_ in o["sample_shared_rows"]:
                print(f"    key={s_['key']}")
                print(f"      mac : {s_['mac_row']}")
                print(f"      repo: {s_['repo_row']}")
        print()

    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(all_reports, f, indent=2)

    print(f"Wrote: {out_path}")
    print("Audit complete. (Read-only — no archive files modified.)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
