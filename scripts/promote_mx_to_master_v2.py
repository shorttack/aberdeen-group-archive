#!/usr/bin/env python3
"""
promote_mx_to_master_v2.py

Promote the -mx Pass C v7 scores into the prescience master (File 2).

Why v2 (not the existing promote_pass_c_to_master_v1.py):
  - v1 hardcodes FILE1 = ~/Desktop/Archive/prescience_scores_pass_c_cloud_v1.csv;
    our scores live in pass_c_v7_mx_tier.csv (the v7 --output).
  - v1's FILE2_COLS is 11 columns and OMITS `row_class`. The live master is now
    12 columns (row_class added later). Running v1 would silently DROP row_class
    from all 17,085 existing rows. v2 is 12-col-aware and preserves it.

Behavior:
  - Reads the 12-col master, preserves every existing row VERBATIM (incl. row_class).
  - Appends only obs_ids not already present (dedupe).
  - For each new -mx row, derives row_class from parse_ok:
        parse_ok == 'true'  -> 'scored'
        parse_ok == 'false' -> 'parse_fail'
    (matches the existing master convention.)
  - Backup before write; csv.QUOTE_ALL; read-back parity.
Dry-run by default; --commit to write.
"""
import csv
import datetime
import shutil
import sys
from pathlib import Path

ARCH = Path.home() / "Desktop" / "Archive"
REPO = ARCH / "aberdeen-group-archive"
SRC = ARCH / "pass_c_v7_mx_tier.csv"          # v7 batch output (11 cols)
MASTER = REPO / "_master_prescience_scores.csv"  # 12 cols incl row_class

MASTER_COLS = [
    "obs_id", "study_id", "model", "prescience_score", "confidence",
    "rationale", "scored_at", "scorer_version", "source_pass",
    "elapsed_sec", "parse_ok", "row_class",
]

commit = "--commit" in sys.argv


def row_class_for(parse_ok: str) -> str:
    return "scored" if str(parse_ok).strip().lower() == "true" else "parse_fail"


def main():
    if not SRC.exists():
        sys.exit(f"FATAL: missing {SRC}")
    if not MASTER.exists():
        sys.exit(f"FATAL: missing {MASTER}")

    # existing master (preserve verbatim)
    with open(MASTER, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        master_hdr = reader.fieldnames
        master_rows = list(reader)
    if master_hdr != MASTER_COLS:
        sys.exit(f"FATAL: master header mismatch.\n have: {master_hdr}\n want: {MASTER_COLS}")
    existing_ids = {r["obs_id"] for r in master_rows}

    # source -mx scores
    with open(SRC, newline="", encoding="utf-8") as f:
        src_rows = list(csv.DictReader(f))

    new_rows = []
    skipped = 0
    for r in src_rows:
        oid = r["obs_id"]
        if oid in existing_ids:
            skipped += 1
            continue
        new_rows.append({
            "obs_id": oid,
            "study_id": r["study_id"],
            "model": r["model"],
            "prescience_score": r["prescience_score"],
            "confidence": r["confidence"],
            "rationale": r["rationale"],
            "scored_at": r["scored_at"],
            "scorer_version": r["scorer_version"],   # 'v7'
            "source_pass": r["source_pass"],          # 'pass_c_sonar_v1'
            "elapsed_sec": r["elapsed_sec"],
            "parse_ok": r["parse_ok"],
            "row_class": row_class_for(r["parse_ok"]),
        })

    print(f"master rows existing : {len(master_rows)} ({len(master_hdr)} cols)")
    print(f"src -mx rows         : {len(src_rows)}")
    print(f"skip (dupe obs_id)   : {skipped}")
    print(f"append (new)         : {len(new_rows)}")
    print(f"master rows after    : {len(master_rows) + len(new_rows)}")
    from collections import Counter
    print(f"new row_class dist   : {dict(Counter(r['row_class'] for r in new_rows))}")
    print(f"mode                 : {'COMMIT' if commit else 'DRY-RUN'}")

    if not commit:
        print("\nDRY-RUN only — pass --commit to write.")
        return

    ts = datetime.datetime.utcnow().strftime("%Y%m%dT%H%M%SZ")
    bak = MASTER.with_suffix(f".csv.bak_promote_mx_{ts}")
    shutil.copy2(MASTER, bak)
    print(f"\nBackup: {bak}")

    out = master_rows + new_rows
    with open(MASTER, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=MASTER_COLS, quoting=csv.QUOTE_ALL)
        w.writeheader()
        w.writerows(out)

    # read-back parity
    with open(MASTER, newline="", encoding="utf-8") as f:
        back = list(csv.DictReader(f))
    assert len(back) == len(out), f"parity FAIL: wrote {len(out)}, read {len(back)}"
    mx_back = sum(1 for r in back if "-mx-OBS-" in r["obs_id"])
    print(f"Wrote {MASTER}: {len(out)} rows. Read-back parity PASS. (-mx rows present: {mx_back})")


if __name__ == "__main__":
    main()
