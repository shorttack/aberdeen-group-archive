#!/usr/bin/env python3
"""
add_player_rebuttal_v1.py — Append a player-rebuttal row to
archive_masters/_master_player_rebuttals.csv.

Use when Pete writes a rebuttal note disagreeing with the Pass C scorer's
study-level prescience verdict. The scorer's verdict stays canonical in
_master_studies.csv; this CSV is the parallel record of Pete's signed
disagreements.

Schema (8 cols, csv.QUOTE_ALL):
  study_id, rebuttal_path, recorded_at, recorded_by,
  scorer_verdict, scorer_mean, scorer_n_obs, scorer_model

Usage:
  python3 add_player_rebuttal_v1.py \
    --study-id dectp-press-conference-... \
    --rebuttal-path kastner-author/notes/foo.md \
    --recorded-by "Peter S. Kastner" \
    --scorer-verdict low --scorer-mean 0.46 --scorer-n-obs 26 \
    --scorer-model sonar-reasoning-pro \
    [--dry-run | --apply]
"""

import argparse
import csv
import sys
from datetime import datetime, timezone
from pathlib import Path

ARCHIVE = Path.home() / "Desktop" / "Archive"
MASTERS = ARCHIVE / "archive_masters"
REBUTTALS = MASTERS / "_master_player_rebuttals.csv"

HEADER = ["study_id", "rebuttal_path", "recorded_at", "recorded_by",
          "scorer_verdict", "scorer_mean", "scorer_n_obs", "scorer_model"]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--study-id", required=True)
    ap.add_argument("--rebuttal-path", required=True)
    ap.add_argument("--recorded-by", required=True)
    ap.add_argument("--scorer-verdict", required=True,
                    choices=["high", "medium", "low", "not-applicable"])
    ap.add_argument("--scorer-mean", required=True)
    ap.add_argument("--scorer-n-obs", required=True)
    ap.add_argument("--scorer-model", required=True)
    g = ap.add_mutually_exclusive_group(required=True)
    g.add_argument("--dry-run", action="store_true")
    g.add_argument("--apply", action="store_true")
    args = ap.parse_args()

    row = {
        "study_id": args.study_id,
        "rebuttal_path": args.rebuttal_path,
        "recorded_at": datetime.now(timezone.utc).isoformat(timespec="seconds").replace("+00:00", "Z"),
        "recorded_by": args.recorded_by,
        "scorer_verdict": args.scorer_verdict,
        "scorer_mean": args.scorer_mean,
        "scorer_n_obs": args.scorer_n_obs,
        "scorer_model": args.scorer_model,
    }

    print(f"=== add_player_rebuttal_v1.py ({'APPLY' if args.apply else 'DRY-RUN'}) ===")
    print(f"target: {REBUTTALS}")
    for k, v in row.items():
        print(f"  {k}: {v}")

    if not REBUTTALS.exists():
        print(f"NOTE: {REBUTTALS} does not exist — will create with header.")

    if not args.apply:
        print("\nRe-run with --apply to append.")
        return 0

    write_header = not REBUTTALS.exists()
    with REBUTTALS.open("a", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=HEADER, quoting=csv.QUOTE_ALL)
        if write_header:
            w.writeheader()
        w.writerow(row)

    print(f"\nappended 1 row")
    return 0


if __name__ == "__main__":
    sys.exit(main() or 0)
