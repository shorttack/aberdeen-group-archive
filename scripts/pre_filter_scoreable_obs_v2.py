#!/usr/bin/env python3
"""
pre_filter_scoreable_obs_v2.py
================================
Pass C pre-filter — identify scoreable observations per study.

v2 delta vs v1: adds --bucket-filter A,B[,...] which reads each study's
manifest.json["bucket"] and skips studies whose assigned bucket is not in the
allowed set. Studies without a manifest.json or without a "bucket" field are
classified as bucket UNKNOWN and skipped when --bucket-filter is supplied
(and reported in the summary).

Rationale (Pete, 2026-05-25): Pass C is restricted to Bucket A (benchmark
reports, 20-30pp) and Bucket B (executive summaries, 2-6pp) — the
observation-dense report formats. Buckets C/D/E (press releases, TOCs,
research agendas) are excluded from prescience scoring.

Filter rules (frozen from calibration, unchanged from v1):
  - empty/whitespace metric_value                 → skip "empty"
  - <40 chars after stripping markdown wrappers  → skip "too_short(Nchars)"
  - markdown header (^# / ^## / etc.)            → skip "markdown_header"
  - bare bold wrapper with no sentence period    → skip "bold_header_no_sentence"

New artifact in --root mode:
  <root>/_bucket_audit_v2.csv  — study_id, bucket, predicted_bucket, kept,
                                 total_obs, scoreable, skipped, no_manifest

Idempotent: re-running overwrites the working/ outputs atomically.

Usage:
  # Bucket A+B only, all prepared studies (production scope for Pass C)
  python3 pre_filter_scoreable_obs_v2.py \\
      --root /Users/scott/Desktop/Archive/prepared \\
      --bucket-filter A,B

  # dry-run audit (counts only, no writes)
  python3 pre_filter_scoreable_obs_v2.py \\
      --root /Users/scott/Desktop/Archive/prepared \\
      --bucket-filter A,B --dry-run

  # no bucket filter (legacy v1 behavior, all buckets)
  python3 pre_filter_scoreable_obs_v2.py --root /Users/scott/Desktop/Archive/prepared

  # single study (bucket filter not enforced for explicit single-study mode)
  python3 pre_filter_scoreable_obs_v2.py --study /Users/scott/Desktop/Archive/prepared/<study>

Outputs (per kept study):
  working/scoreable_obs_v1.csv  — full observation rows that will be scored
  working/skipped_obs_v1.csv    — obs_id, reason
  working/filter_summary_v1.json — counts + timestamp + bucket

Forever-archive: §16.5 QUOTE_ALL on all CSV writes. Atomic .tmp + os.replace.
"""
from __future__ import annotations
import argparse
import csv
import json
import os
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

QUOTE_ALL = csv.QUOTE_ALL

HEADER_RE = re.compile(r"^\s*#{1,6}\s+")
BOLD_HEADER_RE = re.compile(r"^\s*\*\*.{1,80}\*\*\s*$")


def is_non_claim(metric_value: str) -> tuple[bool, str]:
    if not metric_value or not metric_value.strip():
        return True, "empty"
    v = metric_value.strip()
    stripped = re.sub(r"[*_#`]+", "", v).strip()
    if len(stripped) < 40:
        return True, f"too_short({len(stripped)}chars)"
    if HEADER_RE.match(v):
        return True, "markdown_header"
    if BOLD_HEADER_RE.match(v) and "." not in v:
        return True, "bold_header_no_sentence"
    return False, ""


def atomic_write_csv(path: Path, rows: list[dict], header: list[str]) -> None:
    tmp = path.with_suffix(path.suffix + ".tmp")
    with open(tmp, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=header, quoting=QUOTE_ALL,
                           extrasaction="ignore")
        w.writeheader()
        for r in rows:
            w.writerow(r)
    os.replace(tmp, path)


def atomic_write_json(path: Path, obj: dict) -> None:
    tmp = path.with_suffix(path.suffix + ".tmp")
    with open(tmp, "w", encoding="utf-8") as f:
        json.dump(obj, f, indent=2, sort_keys=True)
    os.replace(tmp, path)


def read_manifest_bucket(study_dir: Path) -> tuple[str, str, bool]:
    """Return (assigned_bucket, predicted_bucket, has_manifest).

    Bucket values are uppercase single letters when known, or "UNKNOWN".
    Looks at manifest.json (preferred) then manifest_v20.json as fallback.
    """
    for name in ("manifest.json", "manifest_v20.json"):
        mf = study_dir / name
        if mf.exists():
            try:
                with open(mf, encoding="utf-8") as f:
                    m = json.load(f)
                b = (m.get("bucket") or "").strip().upper() or "UNKNOWN"
                pb = (m.get("predicted_bucket") or "").strip().upper() or ""
                return b, pb, True
            except Exception:
                return "UNKNOWN", "", True
    return "UNKNOWN", "", False


def filter_study(study_dir: Path, dry_run: bool = False,
                 bucket: str = "", predicted_bucket: str = "") -> dict:
    obs_csv = study_dir / "data" / "observations.csv"
    if not obs_csv.exists():
        return {"study": study_dir.name, "status": "skip_no_obs_csv",
                "total": 0, "scoreable": 0, "skipped": 0,
                "bucket": bucket, "predicted_bucket": predicted_bucket}

    working_dir = study_dir / "working"
    working_dir.mkdir(exist_ok=True)

    with open(obs_csv, encoding="utf-8") as f:
        reader = csv.DictReader(f)
        all_obs = list(reader)
        fieldnames = reader.fieldnames or []

    scoreable: list[dict] = []
    skipped: list[dict] = []
    for row in all_obs:
        skip, reason = is_non_claim(row.get("metric_value", ""))
        if skip:
            skipped.append({"obs_id": row.get("obs_id", ""), "reason": reason})
        else:
            scoreable.append(row)

    summary = {
        "study": study_dir.name,
        "total": len(all_obs),
        "scoreable": len(scoreable),
        "skipped": len(skipped),
        "bucket": bucket,
        "predicted_bucket": predicted_bucket,
        "filtered_at": datetime.now(timezone.utc).isoformat(),
        "filter_version": "v2",
    }

    if not dry_run:
        atomic_write_csv(
            working_dir / "scoreable_obs_v1.csv",
            scoreable,
            fieldnames,
        )
        atomic_write_csv(
            working_dir / "skipped_obs_v1.csv",
            skipped,
            ["obs_id", "reason"],
        )
        atomic_write_json(working_dir / "filter_summary_v1.json", summary)

    summary["status"] = "ok"
    return summary


def parse_bucket_filter(raw: str) -> set[str]:
    return {b.strip().upper() for b in raw.split(",") if b.strip()}


def main() -> int:
    ap = argparse.ArgumentParser()
    grp = ap.add_mutually_exclusive_group(required=True)
    grp.add_argument("--study", help="Single study directory")
    grp.add_argument("--root", help="Root containing prepared/<study>/ dirs")
    ap.add_argument("--dry-run", action="store_true",
                    help="Print counts, do not write filter outputs")
    ap.add_argument("--bucket-filter", default="",
                    help="Comma-separated bucket letters to keep "
                         "(e.g. 'A,B'). Empty = no bucket filter.")
    args = ap.parse_args()

    allowed = parse_bucket_filter(args.bucket_filter) if args.bucket_filter else set()
    if allowed:
        print(f"Bucket filter ACTIVE — keeping: {sorted(allowed)}")
    else:
        print("Bucket filter OFF — processing all studies regardless of bucket")

    if args.study:
        targets = [Path(args.study).resolve()]
        # explicit single-study mode bypasses bucket filter
        force_keep_single = True
    else:
        root = Path(args.root).resolve()
        if not root.is_dir():
            sys.exit(f"ERROR: not a directory: {root}")
        targets = sorted(p for p in root.iterdir()
                         if p.is_dir() and not p.name.startswith("."))
        force_keep_single = False

    print(f"Pre-filter v2 — {len(targets)} study dir(s) — dry_run={args.dry_run}")
    print(f"{'STATUS':10}  {'BKT':>3}  {'TOTAL':>6}  {'SCORE':>6}  {'SKIP':>6}  STUDY")
    print("-" * 90)

    grand_total = grand_score = grand_skip = 0
    no_obs = 0
    filtered_out = 0
    no_manifest = 0
    audit_rows: list[dict] = []

    for t in targets:
        bucket, predicted_bucket, has_manifest = read_manifest_bucket(t)
        if not has_manifest:
            no_manifest += 1

        # Apply bucket filter (skip --study explicit mode)
        keep = True
        if allowed and not force_keep_single:
            keep = bucket in allowed

        if not keep:
            filtered_out += 1
            print(f"{'FILT_OUT':10}  {bucket:>3}  {'':>6}  {'':>6}  {'':>6}  {t.name}")
            audit_rows.append({
                "study_id": t.name, "bucket": bucket,
                "predicted_bucket": predicted_bucket,
                "kept": "no", "total_obs": "",
                "scoreable": "", "skipped": "",
                "no_manifest": "yes" if not has_manifest else "no",
            })
            continue

        summary = filter_study(t, dry_run=args.dry_run,
                               bucket=bucket, predicted_bucket=predicted_bucket)
        status = summary.get("status", "?")
        if status == "skip_no_obs_csv":
            no_obs += 1
            print(f"{'NO_OBS':10}  {bucket:>3}  {'':>6}  {'':>6}  {'':>6}  {t.name}")
            audit_rows.append({
                "study_id": t.name, "bucket": bucket,
                "predicted_bucket": predicted_bucket,
                "kept": "no_obs", "total_obs": 0,
                "scoreable": 0, "skipped": 0,
                "no_manifest": "yes" if not has_manifest else "no",
            })
            continue

        grand_total += summary["total"]
        grand_score += summary["scoreable"]
        grand_skip += summary["skipped"]
        print(f"{status:10}  {bucket:>3}  {summary['total']:>6}  "
              f"{summary['scoreable']:>6}  {summary['skipped']:>6}  {t.name}")
        audit_rows.append({
            "study_id": t.name, "bucket": bucket,
            "predicted_bucket": predicted_bucket,
            "kept": "yes", "total_obs": summary["total"],
            "scoreable": summary["scoreable"], "skipped": summary["skipped"],
            "no_manifest": "yes" if not has_manifest else "no",
        })

    print("-" * 90)
    kept = len(targets) - filtered_out - no_obs
    print(f"{'TOTAL':10}  {'':>3}  {grand_total:>6}  {grand_score:>6}  {grand_skip:>6}  "
          f"(kept: {kept}, filtered_out: {filtered_out}, "
          f"no_obs: {no_obs}, no_manifest: {no_manifest})")

    # Write audit CSV in --root mode (even on --dry-run, so Pete can review)
    if not args.study:
        root = Path(args.root).resolve()
        audit_path = root / "_bucket_audit_v2.csv"
        atomic_write_csv(
            audit_path, audit_rows,
            ["study_id", "bucket", "predicted_bucket", "kept",
             "total_obs", "scoreable", "skipped", "no_manifest"],
        )
        print(f"Audit written → {audit_path}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
