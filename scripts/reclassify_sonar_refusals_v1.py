#!/usr/bin/env python3
"""
reclassify_sonar_refusals_v1.py — Split the SH sweep's `-1` sentinel population
into two distinct populations:

  -1   parse_fail:malformed       (driver could not parse JSON at all)
  -99  content_unrecoverable      (Sonar correctly refused — content missing
                                   from the observation row, archive hygiene
                                   candidate)

The driver v8 writes `-1` for both cases. This script audits the
`raw_response_sh` column of each `-1` row, and reclassifies rows where:

  1. raw_response_sh parses as valid JSON, AND
  2. The JSON contains prescience_3y == -1 AND prescience_5y == -1, AND
  3. The rationale starts with a Sonar structured-refusal phrase
     ("Cannot score", "Insufficient information", "Unable to evaluate",
     "No information", etc.)

Rows matching all three criteria get:
  - prescience_3y -> -99
  - prescience_5y -> -99
  - rationale_3y prefixed with "[content_unrecoverable] " (preserving original)
  - rationale_5y prefixed with "[content_unrecoverable] " (preserving original)
  - confidence_3y / confidence_5y left at 1
  - All other columns unchanged

A manifest CSV is emitted listing the reclassified obs_ids for use by a
future archive-hygiene pass.

Usage (dry-run, default):
  python3 scripts/reclassify_sonar_refusals_v1.py \\
    --input Perplexity_Only/sh_sweep_le_2015_results.csv

Usage (real write — requires explicit --apply):
  python3 scripts/reclassify_sonar_refusals_v1.py \\
    --input Perplexity_Only/sh_sweep_le_2015_results.csv \\
    --backup Perplexity_Only/sh_sweep_le_2015_results.csv.bak_pre_refusal_reclass_$(date +%Y%m%dT%H%M%SZ) \\
    --manifest Perplexity_Only/sh_sweep_le_2015_refusal_manifest_v1.csv \\
    --apply
"""
from __future__ import annotations

import argparse
import csv
import hashlib
import json
import os
import re
import shutil
import sys
import tempfile
from pathlib import Path

REFUSAL_PHRASES = (
    "cannot score",
    "insufficient information",
    "unable to evaluate",
    "unable to score",
    "no information",
    "not provided",
    "content is unavailable",
    "without the actual",
    "without the text",
    "no observation provided",
)

SENTINEL_REFUSAL = "-99"
SENTINEL_PARSE_FAIL = "-1"
RATIONALE_PREFIX = "[content_unrecoverable] "


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(8192), b""):
            h.update(chunk)
    return h.hexdigest()


def looks_like_sonar_refusal(raw_response: str) -> tuple[bool, str]:
    """Return (is_refusal, reason). Heuristic — see module docstring."""
    if not raw_response or not raw_response.strip():
        return False, "empty_raw_response"

    # Must parse as JSON
    try:
        obj = json.loads(raw_response)
    except (json.JSONDecodeError, ValueError):
        return False, "raw_response_not_valid_json"

    if not isinstance(obj, dict):
        return False, "raw_response_not_object"

    # Must declare prescience -1 on both windows
    p3 = obj.get("prescience_3y")
    p5 = obj.get("prescience_5y")
    if p3 != -1 or p5 != -1:
        return False, f"prescience values not both -1 (3y={p3}, 5y={p5})"

    # Rationale must start with a refusal phrase
    r3 = (obj.get("rationale_3y") or "").strip().lower()
    r5 = (obj.get("rationale_5y") or "").strip().lower()
    matches_3 = any(r3.startswith(p) for p in REFUSAL_PHRASES)
    matches_5 = any(r5.startswith(p) for p in REFUSAL_PHRASES)
    if not (matches_3 and matches_5):
        return False, f"rationale does not start with refusal phrase (3y_match={matches_3}, 5y_match={matches_5})"

    return True, "ok_refusal"


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--input", required=True, help="Path to sh_sweep_le_2015_results.csv")
    ap.add_argument("--backup", default=None,
                    help="Path for backup of original CSV. Required when --apply.")
    ap.add_argument("--manifest", default=None,
                    help="Path for refusal-manifest CSV. Required when --apply.")
    ap.add_argument("--apply", action="store_true",
                    help="Actually write changes. Default is dry-run.")
    args = ap.parse_args()

    src = Path(args.input).resolve()
    if not src.exists():
        print(f"[err] input not found: {src}", file=sys.stderr)
        return 2

    pre_sha = sha256_file(src)
    pre_size = src.stat().st_size
    print(f"[pre] {src}")
    print(f"[pre] sha256: {pre_sha}")
    print(f"[pre] size:   {pre_size} bytes")

    # Load all rows, identify candidates
    with open(src, newline="") as f:
        reader = csv.DictReader(f)
        fieldnames = list(reader.fieldnames or [])
        rows = list(reader)
    print(f"[load] {len(rows)} rows, {len(fieldnames)} cols")

    # Idempotency check — refuse if -99 already present
    already = sum(1 for r in rows if r.get("prescience_3y") == SENTINEL_REFUSAL
                  or r.get("prescience_5y") == SENTINEL_REFUSAL)
    if already > 0:
        print(f"[err] file already contains {already} rows with prescience == -99 — "
              f"reclassification is idempotent and refuses to re-run", file=sys.stderr)
        return 3

    # Walk -1 rows and classify
    candidates = [r for r in rows
                  if r.get("prescience_3y") == SENTINEL_PARSE_FAIL
                  and r.get("prescience_5y") == SENTINEL_PARSE_FAIL]
    print(f"[scan] {len(candidates)} rows with both windows == -1 (parse_fail population)")

    reclassify = []
    keep_as_parse_fail = []
    for r in candidates:
        raw = r.get("raw_response_sh") or ""
        is_refusal, reason = looks_like_sonar_refusal(raw)
        if is_refusal:
            reclassify.append(r)
        else:
            keep_as_parse_fail.append((r, reason))

    print(f"[classify] -> reclassify as -99 (content_unrecoverable): {len(reclassify)}")
    print(f"[classify] -> keep as -1     (parse_fail:malformed):     {len(keep_as_parse_fail)}")
    print()

    # Show every reclassified row's obs_id + raw snippet
    print("[reclassify] obs_ids and raw_response preview:")
    for r in reclassify:
        oid = r.get("obs_id", "")
        anc = r.get("anchor_year", "")
        raw = (r.get("raw_response_sh") or "")[:120].replace("\n", " ")
        print(f"  {oid:60s}  anchor={anc}  raw={raw!r}")

    if keep_as_parse_fail:
        print()
        print("[keep] true parse_fail rows (will remain -1):")
        for r, reason in keep_as_parse_fail:
            oid = r.get("obs_id", "")
            anc = r.get("anchor_year", "")
            print(f"  {oid:60s}  anchor={anc}  reason={reason}")

    if not args.apply:
        print()
        print("[dry-run] no changes written. Re-run with --apply --backup PATH --manifest PATH to write.")
        return 0

    # Apply mode requires backup + manifest paths
    if not args.backup:
        print("[err] --apply requires --backup PATH", file=sys.stderr)
        return 2
    if not args.manifest:
        print("[err] --apply requires --manifest PATH", file=sys.stderr)
        return 2

    backup_path = Path(args.backup).resolve()
    manifest_path = Path(args.manifest).resolve()
    backup_path.parent.mkdir(parents=True, exist_ok=True)
    manifest_path.parent.mkdir(parents=True, exist_ok=True)

    # Backup first
    shutil.copy2(src, backup_path)
    bak_sha = sha256_file(backup_path)
    print(f"[backup] {backup_path}  sha={bak_sha}")
    if bak_sha != pre_sha:
        print("[err] backup SHA does not match input SHA — aborting", file=sys.stderr)
        return 4

    # Build reclassify lookup
    reclassify_ids = {r.get("obs_id") for r in reclassify}

    # Mutate in memory
    for r in rows:
        if r.get("obs_id") in reclassify_ids:
            r["prescience_3y"] = SENTINEL_REFUSAL
            r["prescience_5y"] = SENTINEL_REFUSAL
            # Prefix rationales — preserve Sonar's original explanation
            r3 = r.get("rationale_3y") or ""
            r5 = r.get("rationale_5y") or ""
            if not r3.startswith(RATIONALE_PREFIX):
                r["rationale_3y"] = RATIONALE_PREFIX + r3
            if not r5.startswith(RATIONALE_PREFIX):
                r["rationale_5y"] = RATIONALE_PREFIX + r5

    # Atomic write — tempfile + os.replace
    tmp_fd, tmp_path = tempfile.mkstemp(suffix=".csv", dir=str(src.parent))
    os.close(tmp_fd)
    try:
        with open(tmp_path, "w", newline="") as f:
            w = csv.DictWriter(f, fieldnames=fieldnames, quoting=csv.QUOTE_ALL)
            w.writeheader()
            for r in rows:
                w.writerow(r)
        os.replace(tmp_path, src)
    except Exception:
        if Path(tmp_path).exists():
            os.unlink(tmp_path)
        raise

    post_sha = sha256_file(src)
    post_size = src.stat().st_size
    print(f"[post] sha256: {post_sha}")
    print(f"[post] size:   {post_size} bytes (Δ {post_size - pre_size:+d})")

    # Invariant check — row + col count unchanged, only -1 -> -99 deltas
    with open(src, newline="") as f:
        post_rows = list(csv.DictReader(f))
    assert len(post_rows) == len(rows), f"row count drift: {len(rows)} -> {len(post_rows)}"
    n99 = sum(1 for r in post_rows if r.get("prescience_3y") == SENTINEL_REFUSAL)
    n_neg1_3y = sum(1 for r in post_rows if r.get("prescience_3y") == SENTINEL_PARSE_FAIL)
    print(f"[verify] rows with -99 (3y): {n99}  expected: {len(reclassify)}")
    print(f"[verify] rows with -1  (3y): {n_neg1_3y}  expected: {len(keep_as_parse_fail)}")
    assert n99 == len(reclassify), "reclassification count mismatch"
    assert n_neg1_3y == len(keep_as_parse_fail), "parse_fail residual count mismatch"

    # Write manifest
    manifest_cols = ["obs_id", "study_id", "anchor_year", "anchor_source",
                     "original_rationale_3y", "original_rationale_5y", "raw_response_sh"]
    with open(manifest_path, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=manifest_cols, quoting=csv.QUOTE_ALL)
        w.writeheader()
        for r in reclassify:
            # Strip the prefix we just added back out, for clean manifest content
            r3 = r.get("rationale_3y", "")
            r5 = r.get("rationale_5y", "")
            if r3.startswith(RATIONALE_PREFIX):
                r3 = r3[len(RATIONALE_PREFIX):]
            if r5.startswith(RATIONALE_PREFIX):
                r5 = r5[len(RATIONALE_PREFIX):]
            w.writerow({
                "obs_id": r.get("obs_id", ""),
                "study_id": r.get("study_id", ""),
                "anchor_year": r.get("anchor_year", ""),
                "anchor_source": r.get("anchor_source", ""),
                "original_rationale_3y": r3,
                "original_rationale_5y": r5,
                "raw_response_sh": r.get("raw_response_sh", ""),
            })
    print(f"[manifest] {manifest_path}  rows={len(reclassify)}")
    print()
    print(f"[done] reclassified {len(reclassify)} rows -> -99 (content_unrecoverable)")
    print(f"[done] retained {len(keep_as_parse_fail)} rows as -1 (parse_fail:malformed)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
