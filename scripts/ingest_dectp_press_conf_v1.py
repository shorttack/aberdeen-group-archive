#!/usr/bin/env python3
"""
ingest_dectp_press_conf_v1.py
Ingest the DECtp Press Conference 1988 study into the Kastner Aberdeen archive.

Dry-run by default. Pass --commit to write.

Actions:
  1. Verify _master_studies.csv schema is 16 columns
  2. Check for duplicate study_id
  3. Backup _master_studies.csv
  4. Append new master row (csv.QUOTE_ALL)
  5. Copy source markdown + 4 images to archive destination

Usage:
  python3 ~/Desktop/Archive/scripts/ingest_dectp_press_conf_v1.py
  python3 ~/Desktop/Archive/scripts/ingest_dectp_press_conf_v1.py --commit
"""

import csv, sys, shutil, datetime, hashlib, os
from pathlib import Path

# ── Paths ────────────────────────────────────────────────────────────────────
ARCHIVE_MASTERS = Path.home() / "Desktop/Archive/archive_masters"
MASTER_CSV      = ARCHIVE_MASTERS / "_master_studies.csv"

# Source files — adjust if you placed the extracted zip elsewhere
SRC_DIR = Path.home() / "Desktop/Archive/_ingest_queue/DECtp-press-conference-with-images"
SRC_MD  = SRC_DIR / "DECtp-NYC-1988-07-cleaned.md"
SRC_IMAGES = [
    SRC_DIR / "DECtp 1988 tps rdbms.png",
    SRC_DIR / "DECtp-flatfiles-tps-1988-08.19.41.png",
    SRC_DIR / "DECtp 1988 tps flat files.png",
    SRC_DIR / "DECtp 1988 price-performance.png",
    SRC_DIR / "DECtp 1988 avg system cost.png",
]

# Destination in the archive repo working tree
DEST_DIR    = Path.home() / "Desktop/Archive/aberdeen-group-archive" \
              / "kastner-author/1988-dectp-press-conference-nyc"
DEST_MEDIA  = DEST_DIR / "media"
DEST_SOURCE = DEST_DIR / "source"

# Study markdown (pre-authored with observations)
# Pete: copy this file to the same _ingest_queue dir before running, or adjust path
STUDY_MD = Path.home() / "Desktop/Archive/_ingest_queue" \
           / "dectp-press-conf-1988-study.md"

# ── New master row (16 columns, matching _master_studies.csv header order) ───
STUDY_ID = "dectp-press-conference-transcript-and-benchmark-charts-plaza-5e5836"

NEW_ROW = {
    "study_id":              STUDY_ID,
    "title":                 "DECtp Press Conference Transcript and Benchmark Charts, Plaza Hotel NYC, July 1988",
    "author":                "Digital Equipment Corporation (Kirk, Dallas; Olsen, Kenneth H.; Glorioso, Robert; Hughes, Bob)",
    "date":                  "1988-07-19",
    "type":                  "primary-source",
    "subject_domain":        "transaction-processing-benchmarks",
    "methodology":           "press-conference-transcript; debit-credit-benchmark; comparative-performance",
    "source_file":           "DECtp-NYC-1988-07-cleaned.md",
    "abstract":              (
        "Cleaned transcript of DEC's DECtp product launch press conference, "
        "Plaza Hotel, New York City, July 19, 1988. Presenters include Ken Olsen "
        "(President, DEC), Bob Glorioso (VP Engineering), and Bob Hughes (VP Marketing). "
        "Glorioso presents Debit-Credit benchmark results for VAX systems vs. IBM and "
        "Tandem in two configurations (RDBMS and flat-file). Hughes presents "
        "price/performance charts showing DEC at half IBM's cost per TPS. Includes "
        "four high-resolution benchmark chart images. Source: Computer History Museum "
        "catalogue #102717571, accession X2675.2004, Gift of Hewlett-Packard. "
        "Kastner was present as a Debit-Credit subject matter expert; traveled by "
        "helicopter with Olsen and Glorioso to the DEC private jet."
    ),
    "license":               "CC-BY-NC-SA-4.0",
    "importance":            "",
    "importance_rationale":  "",
    "relevance":             "",
    "relevance_rationale":   "",
    "prescience":            "[DEFERRED]",
    "prescience_rationale":  "",
}

EXPECTED_COLS = 16

# ── Helpers ──────────────────────────────────────────────────────────────────
def utc_stamp():
    return datetime.datetime.utcnow().strftime("%Y%m%dT%H%M%SZ")

def verify_schema(path):
    with open(path, newline="") as f:
        reader = csv.reader(f)
        header = next(reader)
    if len(header) != EXPECTED_COLS:
        print(f"ABORT: expected {EXPECTED_COLS} columns, found {len(header)}: {header}")
        sys.exit(1)
    print(f"Schema OK: {len(header)} columns")
    return header

def check_duplicate(path, study_id):
    with open(path, newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            if row.get("study_id") == study_id:
                return True
    return False

def read_rows(path):
    with open(path, newline="") as f:
        reader = csv.reader(f)
        header = next(reader)
        rows = list(reader)
    return header, rows

def write_csv(path, header, rows):
    with open(path, "w", newline="") as f:
        w = csv.writer(f, quoting=csv.QUOTE_ALL)
        w.writerow(header)
        w.writerows(rows)

# ── Main ─────────────────────────────────────────────────────────────────────
def main():
    commit = "--commit" in sys.argv
    print(f"Mode: {'COMMIT' if commit else 'DRY-RUN'}")
    print()

    # 1. Verify schema
    header = verify_schema(MASTER_CSV)

    # 2. Check duplicate
    if check_duplicate(MASTER_CSV, STUDY_ID):
        print(f"ABORT: study_id '{STUDY_ID}' already exists in master CSV.")
        sys.exit(1)
    print(f"Duplicate check OK: '{STUDY_ID}' not in archive")

    # 3. Verify source files exist
    missing = []
    for f in [SRC_MD] + SRC_IMAGES:
        if not f.exists():
            missing.append(str(f))
    if missing:
        print("MISSING source files:")
        for m in missing:
            print(f"  {m}")
        print()
        print("Copy the extracted zip contents to:")
        print(f"  {SRC_DIR}/")
        if not commit:
            print("(DRY-RUN: continuing anyway to show what would happen)")
        else:
            sys.exit(1)
    else:
        print(f"Source files OK: {len(SRC_IMAGES)+1} files found")

    # 4. Show proposed master row
    print()
    print("=== Proposed master row ===")
    for k, v in NEW_ROW.items():
        display = v[:80] + "..." if len(v) > 80 else v
        print(f"  {k:25s}: {display}")
    print()

    # 5. Show destination paths
    print("=== File destinations ===")
    print(f"  Study markdown  : {DEST_DIR}/dectp-press-conf-1988.md")
    print(f"  Source MD       : {DEST_SOURCE}/DECtp-NYC-1988-07-cleaned.md")
    for img in SRC_IMAGES:
        print(f"  Image           : {DEST_MEDIA}/{img.name}")
    print()

    if not commit:
        print("DRY-RUN complete. Pass --commit to write.")
        return

    # ── COMMIT ──────────────────────────────────────────────────────────────
    # Backup
    ts = utc_stamp()
    bak = MASTER_CSV.with_suffix(f".csv.bak_dectp_press_conf_{ts}")
    shutil.copy2(MASTER_CSV, bak)
    print(f"Backup: {bak}")

    # Read, append, write
    header, rows = read_rows(MASTER_CSV)
    before = len(rows)
    new_row_values = [NEW_ROW[col] for col in header]
    rows.append(new_row_values)
    write_csv(MASTER_CSV, header, rows)
    after_header, after_rows = read_rows(MASTER_CSV)
    print(f"Master CSV: {before} rows → {len(after_rows)} rows (delta +1)")

    # Row-parity check
    if len(after_rows) != before + 1:
        print(f"ERROR: row parity failed! Expected {before+1}, got {len(after_rows)}")
        sys.exit(1)
    print("Row parity OK")

    # Create destination directories
    DEST_DIR.mkdir(parents=True, exist_ok=True)
    DEST_MEDIA.mkdir(parents=True, exist_ok=True)
    DEST_SOURCE.mkdir(parents=True, exist_ok=True)

    # Copy study markdown
    shutil.copy2(STUDY_MD, DEST_DIR / "dectp-press-conf-1988.md")
    print(f"Copied: dectp-press-conf-1988.md → {DEST_DIR}/")

    # Copy source transcript
    shutil.copy2(SRC_MD, DEST_SOURCE / "DECtp-NYC-1988-07-cleaned.md")
    print(f"Copied: DECtp-NYC-1988-07-cleaned.md → {DEST_SOURCE}/")

    # Copy images
    for img in SRC_IMAGES:
        if img.exists():
            shutil.copy2(img, DEST_MEDIA / img.name)
            print(f"Copied: {img.name} → {DEST_MEDIA}/")
        else:
            print(f"SKIP (not found): {img.name}")

    print()
    print("=== Ingest complete ===")
    print(f"study_id : {STUDY_ID}")
    print(f"Dest     : {DEST_DIR}")
    print()
    print("Next steps:")
    print("  1. git pull in ~/Desktop/Archive/aberdeen-group-archive")
    print("  2. Run Phase 1+2 to rebuild DuckDB:")
    print("     python3 ~/Desktop/Archive/scripts/build/01_load_csvs_v2.py \\")
    print("       --archive ~/Desktop/Archive/archive_masters \\")
    print("       --wiki ~/Repos/kastner-aberdeen-wiki")
    print("     python3 ~/Desktop/Archive/scripts/build/02_build_data_layer_v4.py \\")
    print("       --wiki ~/Repos/kastner-aberdeen-wiki")
    print("  3. Run Phases 3-5 if kw ask should find this study.")
    print("  4. EOD batch commit via kastner-github skill.")

if __name__ == "__main__":
    main()
