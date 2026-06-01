#!/usr/bin/env python3
"""
pre_filter_scoreable_obs_v1.py
================================
Pass C pre-filter — identify scoreable observations per study.

Generalizes the calibration filter from run_prescience_calibration_v3.py.
Reads each study's data/observations.csv and emits working/scoreable_obs_v1.csv
(the subset that will be sent to the 27B scorer) plus working/skipped_obs_v1.csv
(non-claim observations with skip reasons).

Filter rules (frozen from calibration):
  - empty/whitespace metric_value                 → skip "empty"
  - <40 chars after stripping markdown wrappers  → skip "too_short(Nchars)"
  - markdown header (^# / ^## / etc.)            → skip "markdown_header"
  - bare bold wrapper with no sentence period    → skip "bold_header_no_sentence"

Idempotent: re-running overwrites the working/ outputs atomically.

Usage:
  # single study
  python3 pre_filter_scoreable_obs_v1.py --study /Users/scott/Desktop/Archive/prepared/<study>

  # all studies under prepared/
  python3 pre_filter_scoreable_obs_v1.py --root /Users/scott/Desktop/Archive/prepared

  # dry-run (counts only, no writes)
  python3 pre_filter_scoreable_obs_v1.py --root /Users/scott/Desktop/Archive/prepared --dry-run

Outputs (per study):
  working/scoreable_obs_v1.csv  — full observation rows that will be scored
  working/skipped_obs_v1.csv    — obs_id, reason
  working/filter_summary_v1.json — counts + timestamp

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


def filter_study(study_dir: Path, dry_run: bool = False) -> dict:
    obs_csv = study_dir / "data" / "observations.csv"
    if not obs_csv.exists():
        return {"study": study_dir.name, "status": "skip_no_obs_csv",
                "total": 0, "scoreable": 0, "skipped": 0}

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
        "filtered_at": datetime.now(timezone.utc).isoformat(),
        "filter_version": "v1",
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


def main() -> int:
    ap = argparse.ArgumentParser()
    grp = ap.add_mutually_exclusive_group(required=True)
    grp.add_argument("--study", help="Single study directory")
    grp.add_argument("--root", help="Root containing prepared/<study>/ dirs")
    ap.add_argument("--dry-run", action="store_true",
                    help="Print counts, do not write filter outputs")
    args = ap.parse_args()

    if args.study:
        targets = [Path(args.study).resolve()]
    else:
        root = Path(args.root).resolve()
        if not root.is_dir():
            sys.exit(f"ERROR: not a directory: {root}")
        targets = sorted(p for p in root.iterdir()
                         if p.is_dir() and not p.name.startswith("."))

    print(f"Pre-filter v1 — {len(targets)} study dir(s) — dry_run={args.dry_run}")
    print(f"{'STATUS':10}  {'TOTAL':>6}  {'SCORE':>6}  {'SKIP':>6}  STUDY")
    print("-" * 80)

    grand_total = grand_score = grand_skip = 0
    no_obs = 0
    for t in targets:
        summary = filter_study(t, dry_run=args.dry_run)
        status = summary.get("status", "?")
        if status == "skip_no_obs_csv":
            no_obs += 1
            print(f"{'NO_OBS':10}  {'':>6}  {'':>6}  {'':>6}  {t.name}")
            continue
        grand_total += summary["total"]
        grand_score += summary["scoreable"]
        grand_skip += summary["skipped"]
        print(f"{status:10}  {summary['total']:>6}  "
              f"{summary['scoreable']:>6}  {summary['skipped']:>6}  {t.name}")

    print("-" * 80)
    print(f"{'TOTAL':10}  {grand_total:>6}  {grand_score:>6}  {grand_skip:>6}  "
          f"(studies with obs: {len(targets) - no_obs}, no_obs: {no_obs})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
