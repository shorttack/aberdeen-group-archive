#!/usr/bin/env python3
"""
audit_mac_vs_repo_v1.py
=======================

READ-ONLY diagnostic. Compares master and known CSVs between:
  - Mac canonical:  /Users/scott/Desktop/Archive/aberdeen-group-archive/
  - Repo HEAD:      shorttack/aberdeen-group-archive  origin/main  (flat at root)

Writes ONE output file:
  /Users/scott/Desktop/Archive/_audit_mac_vs_repo_<YYYYMMDDTHHMMSSZ>.csv

That is the ONLY file this script writes. No backups. No edits to any master.
No staged commits. No network writes. Read-only against both sides.

Usage:
    python3 audit_mac_vs_repo_v1.py

Requires `gh` CLI authenticated for shorttack/aberdeen-group-archive (read access).
If gh is unavailable or unauthenticated, repo-side columns are filled with
'REPO_UNREACHABLE' and the script still completes — you get the Mac-side
inventory plus a clear "could not reach repo" signal.

Columns in output:
  file_name         filename relative to archive_masters/ (Mac) / repo root
  mac_exists        bool
  mac_rows          int   (data rows, excludes header; csv.reader-based)
  mac_cols          int   (header column count)
  mac_size_bytes    int
  mac_sha256        str   (full file content)
  mac_mtime_utc     str   ISO 8601, e.g. '2026-05-25T21:37:20Z'
  mac_mtime_local   str   ISO 8601 local, e.g. '2026-05-25T17:37:20-04:00'
  repo_exists       bool  (False or REPO_UNREACHABLE)
  repo_rows         int
  repo_cols         int
  repo_size_bytes   int   (Git Data API reports decoded size)
  repo_blob_sha     str   (git blob sha; not content sha256)
  repo_sha256       str   (sha256 of decoded blob content; comparable to mac_sha256)
  status            enum  see below
  notes             str

status enum:
  IN_SYNC               sha256 matches; safe — no action needed
  ROW_DELTA             same column count, different row count
  COL_DELTA             same row count, different column count
  BOTH_DELTA            row and column count both differ
  CONTENT_DELTA         row and col counts match but sha256 differs (content drift)
  MISSING_REPO          Mac has it, repo confirmed does NOT have it (gh api returned 404)
  MISSING_MAC           repo has it, Mac does not
  REPO_UNREACHABLE      gh api failed for transient reasons (auth, network, rate limit)
  MISSING_BOTH          neither side has it (sanity)

Files surveyed (extend FILES list below to add more):
  - All _master_*.csv plus _known_*.csv plus _master_entity_field_conflicts.csv
"""

from __future__ import annotations

import csv
import datetime as dt
import hashlib
import json
import os
import shutil
import subprocess
import sys
from pathlib import Path
from typing import Optional

# ---------- Configuration ----------

MAC_ROOT = Path.home() / "Desktop/Archive/aberdeen-group-archive"
REPO = "shorttack/aberdeen-group-archive"
REPO_BRANCH = "main"

# Files to audit. Each lives at archive_masters/<name> on the Mac and at /<name>
# at the repo root (the repo is flat — no archive_masters/ subdir per
# kastner-archive-pipeline skill).
FILES = [
    "_master_studies.csv",
    "_master_observations.csv",
    "_master_entities.csv",
    "_master_technologies.csv",
    "_master_codes.csv",
    "_master_entity_field_conflicts.csv",
    "_known_entities.csv",
    "_known_technologies.csv",
]

# ---------- Helpers ----------


def utc_now_compact() -> str:
    return dt.datetime.now(dt.timezone.utc).strftime("%Y%m%dT%H%M%SZ")


def iso_utc(epoch_seconds: float) -> str:
    return (
        dt.datetime.fromtimestamp(epoch_seconds, dt.timezone.utc)
        .strftime("%Y-%m-%dT%H:%M:%SZ")
    )


def iso_local(epoch_seconds: float) -> str:
    # Local time WITH offset, so it's unambiguous in the output.
    local = dt.datetime.fromtimestamp(epoch_seconds).astimezone()
    return local.strftime("%Y-%m-%dT%H:%M:%S%z")


def sha256_of_file(path: Path) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def sha256_of_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def count_csv_rows_and_cols(path: Path) -> tuple[int, int]:
    """
    Returns (data_row_count, header_col_count).

    Uses csv.reader so embedded newlines in QUOTE_ALL fields are handled
    correctly (wc -l would over-count). Reads the whole file once.
    """
    with open(path, "r", newline="", encoding="utf-8") as f:
        reader = csv.reader(f)
        try:
            header = next(reader)
        except StopIteration:
            return (0, 0)
        cols = len(header)
        rows = sum(1 for _ in reader)
    return (rows, cols)


def count_csv_rows_and_cols_from_bytes(data: bytes) -> tuple[int, int]:
    """Same as count_csv_rows_and_cols but for in-memory bytes (decoded blob)."""
    import io

    f = io.StringIO(data.decode("utf-8"))
    reader = csv.reader(f)
    try:
        header = next(reader)
    except StopIteration:
        return (0, 0)
    cols = len(header)
    rows = sum(1 for _ in reader)
    return (rows, cols)


def gh_available() -> bool:
    return shutil.which("gh") is not None


def gh_get_file_metadata(filename: str) -> Optional[dict]:
    """
    Returns the file metadata dict from /contents/<filename> (small files only,
    but we use it just for the blob SHA + size, NOT for content fetch).
    Returns None on 404, raises on transient errors so the caller can mark
    REPO_UNREACHABLE.
    """
    cmd = ["gh", "api", f"/repos/{REPO}/contents/{filename}?ref={REPO_BRANCH}"]
    proc = subprocess.run(cmd, capture_output=True, text=True)
    if proc.returncode != 0:
        stderr = (proc.stderr or "").lower()
        if "404" in stderr or "not found" in stderr:
            return None  # genuine absence
        raise RuntimeError(
            f"gh api failed for /contents/{filename}: rc={proc.returncode} "
            f"stderr={proc.stderr.strip()[:300]}"
        )
    return json.loads(proc.stdout)


def gh_get_blob_bytes(blob_sha: str) -> bytes:
    """
    Fetches the raw decoded bytes of a blob via the Git Data API.
    Works for files of any size (the contents API caps at ~1 MB; the blobs
    API does not).
    """
    cmd = ["gh", "api", f"/repos/{REPO}/git/blobs/{blob_sha}"]
    proc = subprocess.run(cmd, capture_output=True, text=True)
    if proc.returncode != 0:
        raise RuntimeError(
            f"gh api failed for /git/blobs/{blob_sha}: rc={proc.returncode} "
            f"stderr={proc.stderr.strip()[:300]}"
        )
    payload = json.loads(proc.stdout)
    encoding = payload.get("encoding", "")
    content = payload.get("content", "")
    if encoding != "base64":
        raise RuntimeError(
            f"Unexpected blob encoding for {blob_sha}: {encoding!r}"
        )
    import base64

    return base64.b64decode(content)


# ---------- Per-file audit ----------


def audit_one(filename: str, gh_ok: bool) -> dict:
    rec: dict = {
        "file_name": filename,
        "mac_exists": False,
        "mac_rows": "",
        "mac_cols": "",
        "mac_size_bytes": "",
        "mac_sha256": "",
        "mac_mtime_utc": "",
        "mac_mtime_local": "",
        "repo_exists": "",
        "repo_rows": "",
        "repo_cols": "",
        "repo_size_bytes": "",
        "repo_blob_sha": "",
        "repo_sha256": "",
        "status": "",
        "notes": "",
    }

    # --- Mac side ---
    mac_path = MAC_ROOT / filename
    if mac_path.is_file():
        try:
            st = mac_path.stat()
            rec["mac_exists"] = True
            rec["mac_size_bytes"] = st.st_size
            rec["mac_mtime_utc"] = iso_utc(st.st_mtime)
            rec["mac_mtime_local"] = iso_local(st.st_mtime)
            mrows, mcols = count_csv_rows_and_cols(mac_path)
            rec["mac_rows"] = mrows
            rec["mac_cols"] = mcols
            rec["mac_sha256"] = sha256_of_file(mac_path)
        except Exception as e:
            rec["notes"] = f"mac-side error: {type(e).__name__}: {e}"
            # Don't bail — still try the repo side so the audit is complete.
    else:
        rec["mac_exists"] = False

    # --- Repo side ---
    if not gh_ok:
        rec["repo_exists"] = "REPO_UNREACHABLE"
        rec["status"] = "REPO_UNREACHABLE"
        prior = rec["notes"]
        rec["notes"] = (
            (prior + "; " if prior else "")
            + "gh CLI unavailable — skipped repo lookup"
        )
        return rec

    try:
        meta = gh_get_file_metadata(filename)
    except RuntimeError as e:
        rec["repo_exists"] = "REPO_UNREACHABLE"
        rec["status"] = "REPO_UNREACHABLE"
        prior = rec["notes"]
        rec["notes"] = (prior + "; " if prior else "") + str(e)
        return rec

    if meta is None:
        # gh confirmed 404
        rec["repo_exists"] = False
        if rec["mac_exists"]:
            rec["status"] = "MISSING_REPO"
        else:
            rec["status"] = "MISSING_BOTH"
        return rec

    rec["repo_exists"] = True
    rec["repo_blob_sha"] = meta.get("sha", "")
    rec["repo_size_bytes"] = meta.get("size", "")

    # Fetch blob bytes via Git Data API (works for any file size).
    try:
        blob_bytes = gh_get_blob_bytes(rec["repo_blob_sha"])
    except RuntimeError as e:
        # We know the file exists in the repo (we have its sha) — but we
        # couldn't fetch the body. Mark as unreachable for content compare.
        prior_status = rec["status"]
        rec["status"] = "REPO_UNREACHABLE"
        prior_notes = rec["notes"]
        rec["notes"] = (
            (prior_notes + "; " if prior_notes else "")
            + f"blob fetch failed: {e}"
        )
        _ = prior_status  # suppress unused
        return rec

    try:
        rrows, rcols = count_csv_rows_and_cols_from_bytes(blob_bytes)
        rec["repo_rows"] = rrows
        rec["repo_cols"] = rcols
        rec["repo_sha256"] = sha256_of_bytes(blob_bytes)
    except Exception as e:
        prior_notes = rec["notes"]
        rec["notes"] = (
            (prior_notes + "; " if prior_notes else "")
            + f"repo-side parse error: {type(e).__name__}: {e}"
        )
        rec["status"] = "REPO_UNREACHABLE"
        return rec

    # --- Status decision ---
    if not rec["mac_exists"]:
        rec["status"] = "MISSING_MAC"
        return rec

    if rec["mac_sha256"] and rec["repo_sha256"] and rec["mac_sha256"] == rec["repo_sha256"]:
        rec["status"] = "IN_SYNC"
        return rec

    row_match = rec["mac_rows"] == rec["repo_rows"]
    col_match = rec["mac_cols"] == rec["repo_cols"]

    if row_match and col_match:
        rec["status"] = "CONTENT_DELTA"
    elif row_match and not col_match:
        rec["status"] = "COL_DELTA"
    elif col_match and not row_match:
        rec["status"] = "ROW_DELTA"
    else:
        rec["status"] = "BOTH_DELTA"

    return rec


# ---------- Main ----------


def main() -> int:
    if not MAC_ROOT.is_dir():
        print(
            f"FATAL: Mac archive_masters/ not found at {MAC_ROOT}",
            file=sys.stderr,
        )
        return 2

    gh_ok = gh_available()
    if not gh_ok:
        print(
            "WARNING: `gh` CLI not on PATH — repo side will be REPO_UNREACHABLE.",
            file=sys.stderr,
        )

    ts = utc_now_compact()
    out_path = MAC_ROOT.parent / f"_audit_mac_vs_repo_{ts}.csv"

    print(f"Audit start: {dt.datetime.now().isoformat(timespec='seconds')}")
    print(f"Mac root   : {MAC_ROOT}")
    print(f"Repo       : {REPO}  branch={REPO_BRANCH}")
    print(f"Files      : {len(FILES)}")
    print(f"Output     : {out_path}")
    print()

    rows: list[dict] = []
    for fn in FILES:
        print(f"  auditing {fn} ...", end=" ", flush=True)
        rec = audit_one(fn, gh_ok)
        rows.append(rec)
        print(rec["status"])

    # Write CSV with QUOTE_ALL per archive convention.
    fieldnames = [
        "file_name",
        "mac_exists",
        "mac_rows",
        "mac_cols",
        "mac_size_bytes",
        "mac_sha256",
        "mac_mtime_utc",
        "mac_mtime_local",
        "repo_exists",
        "repo_rows",
        "repo_cols",
        "repo_size_bytes",
        "repo_blob_sha",
        "repo_sha256",
        "status",
        "notes",
    ]
    with open(out_path, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fieldnames, quoting=csv.QUOTE_ALL)
        w.writeheader()
        for r in rows:
            w.writerow(r)

    # Summary to stdout
    print()
    print("=" * 72)
    print(f"{'FILE':<42} {'MAC':>14} {'REPO':>14}  STATUS")
    print("-" * 72)
    for r in rows:
        mac_desc = (
            f"{r['mac_rows']}r x {r['mac_cols']}c"
            if r["mac_exists"]
            else "(absent)"
        )
        if r["repo_exists"] is True:
            repo_desc = f"{r['repo_rows']}r x {r['repo_cols']}c"
        elif r["repo_exists"] is False:
            repo_desc = "(absent)"
        else:
            repo_desc = "(unreachable)"
        print(f"{r['file_name']:<42} {mac_desc:>14} {repo_desc:>14}  {r['status']}")
    print("-" * 72)

    # Status histogram
    hist: dict[str, int] = {}
    for r in rows:
        hist[r["status"]] = hist.get(r["status"], 0) + 1
    print("Status counts:", ", ".join(f"{k}={v}" for k, v in sorted(hist.items())))
    print()
    print(f"Wrote: {out_path}")
    print("Audit complete. (Read-only — no archive files modified.)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
