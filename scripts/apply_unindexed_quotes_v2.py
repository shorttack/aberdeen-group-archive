#!/usr/bin/env python3
"""
apply_unindexed_quotes_v2.py

Apply Pete-reviewed silent-loss candidates into the canonical
`kastner_quotes_clean.csv`.

Input:  kastner-author/quotations/_unindexed_kastner_candidates_v2.csv
        (Pete-reviewed; rows with any non-whitespace in `reject` are dropped)
Output: kastner-author/quotations/kastner_quotes_clean.csv (appended in place,
        backed up first)

Reject logic (Pete-prescribed 2026-06-19):
    is_rejected = bool(row["reject"].strip())
    # blank, None, spaces, tabs → ADMIT
    # any non-whitespace character → REJECT

Pipeline per surviving row:
  1. Drop the `reject` column
  2. Drop the 5 provenance columns (source_segment_idx, classification,
     discovery_rule, discovery_confidence, detector_headline_attempted)
  3. Generate a fresh `row_id` by continuing from max(existing row_id) in
     kastner_quotes_clean.csv
  4. Re-order the surviving 18 columns to match the canonical CSV schema
  5. Append with csv.QUOTE_ALL

Backup before write:
    kastner_quotes_clean.csv.bak_apply_unindexed_v2_<utc-stamp>

Dry-run by default; --commit writes.

After this script commits, RE-RUN union_article_corpus_v1.py with --commit to
rebuild article_corpus_v1.json, _pdf_segments_unclaimed_v1.json, and
quote_only_rows_v1.csv. The new admissions need to land in the substrate
or downstream pipelines will not see them.
"""
import csv, shutil, sys
from datetime import datetime, timezone
from pathlib import Path
from collections import Counter

ARCHIVE_REPO = Path("/Users/scott/Desktop/Archive/aberdeen-group-archive")
QUOTATIONS_DIR = ARCHIVE_REPO / "kastner-author/quotations"
CANDIDATES_CSV = QUOTATIONS_DIR / "_unindexed_kastner_candidates_v2.csv"
MASTER_CSV = QUOTATIONS_DIR / "kastner_quotes_clean.csv"

# Canonical schema (must match the live kastner_quotes_clean.csv header
# verified from /tmp/quotes.csv).
CANONICAL_COLS = [
    "row_id", "article_seq", "date", "headline", "publication", "author",
    "content_type", "kastner_quotation", "immediate_context", "is_predictive",
    "prescience_score", "prescience_rationale", "forecast_horizon_years",
    "theme", "decade", "accuracy_outcome", "verdict_rationale",
    "verdict_sources",
]
# Columns we drop from the candidates CSV before appending
DROP_COLS = {
    "reject", "source_segment_idx", "classification", "discovery_rule",
    "discovery_confidence", "detector_headline_attempted",
}


def next_row_id(existing_rows):
    """Compute next row_id by scanning existing master CSV.

    Handles both integer and string row_ids; if existing IDs are integers,
    returns int + 1. Otherwise falls back to count-based.
    """
    ids = [r.get("row_id", "").strip() for r in existing_rows]
    ids = [i for i in ids if i]
    int_ids = []
    for i in ids:
        try:
            int_ids.append(int(i))
        except ValueError:
            pass
    if int_ids and len(int_ids) == len(ids):
        # All IDs are pure integers
        return max(int_ids) + 1, "int"
    # Fallback: use len(existing) as start; format same as first non-int ID
    return len(existing_rows) + 1, "fallback"


def main(commit: bool = False):
    print(f"[apply_unindexed_quotes_v2] {datetime.now(timezone.utc).isoformat()}")
    print(f"Mode: {'COMMIT' if commit else 'DRY-RUN'}")
    print()

    # 1. Read reviewed candidates
    with open(CANDIDATES_CSV) as f:
        cand_rows = list(csv.DictReader(f))
    print(f"  candidates CSV        : {CANDIDATES_CSV.name}")
    print(f"  candidates rows read  : {len(cand_rows)}")

    # 2. Read existing master
    with open(MASTER_CSV) as f:
        reader = csv.DictReader(f)
        master_header = reader.fieldnames
        master_rows = list(reader)
    print(f"  master CSV            : {MASTER_CSV.name}")
    print(f"  master rows read      : {len(master_rows)}")
    print(f"  master cols           : {len(master_header)}")

    # 2a. Verify master header matches canonical schema
    if master_header != CANONICAL_COLS:
        extra = set(master_header) - set(CANONICAL_COLS)
        missing = set(CANONICAL_COLS) - set(master_header)
        print(f"  !! MASTER HEADER MISMATCH")
        print(f"     extra in master  : {extra or 'none'}")
        print(f"     missing in master: {missing or 'none'}")
        sys.exit(1)
    print(f"  master schema audit   : OK ({len(master_header)} cols)")

    # 3. Partition candidates: admit vs reject
    admit = []
    reject = []
    for r in cand_rows:
        reject_raw = r.get("reject") or ""
        is_rejected = bool(reject_raw.strip())
        if is_rejected:
            reject.append(r)
        else:
            admit.append(r)

    print()
    print(f"=== Reject column partition ===")
    print(f"  rejected (non-whitespace in reject): {len(reject)}")
    print(f"  admitted (blank/whitespace in reject): {len(admit)}")

    # Diagnostics: distribution by discovery_rule
    admit_by_rule = Counter(r.get("discovery_rule", "") for r in admit)
    reject_by_rule = Counter(r.get("discovery_rule", "") for r in reject)
    print(f"  admitted by discovery_rule : {dict(admit_by_rule)}")
    print(f"  rejected by discovery_rule : {dict(reject_by_rule)}")

    if not admit:
        print("\n→ No admissions. Nothing to apply. Exiting.")
        return

    # 4. Generate fresh row_ids
    next_id, id_mode = next_row_id(master_rows)
    print()
    print(f"  next row_id           : {next_id} ({id_mode}-mode)")

    # 5. Build appended rows in canonical column order
    new_rows = []
    for i, cand in enumerate(admit):
        new_row = {}
        for col in CANONICAL_COLS:
            if col == "row_id":
                new_row[col] = str(next_id + i)
            else:
                new_row[col] = cand.get(col, "") or ""
        new_rows.append(new_row)

    # Quick audit: every new row has exactly CANONICAL_COLS keys
    bad = [i for i, r in enumerate(new_rows) if set(r.keys()) != set(CANONICAL_COLS)]
    if bad:
        print(f"  !! NEW-ROW SCHEMA FAIL: {len(bad)} rows have wrong keys (first: {bad[0]})")
        sys.exit(1)
    print(f"  new-row schema audit  : OK ({len(CANONICAL_COLS)} cols per new row)")

    print()
    print(f"=== Sample (first 2 new rows) ===")
    for r in new_rows[:2]:
        print(f"  row_id={r['row_id']!r}  headline={r['headline'][:80]!r}")
        print(f"     pub={r['publication']!r}  date={r['date']!r}")
        print(f"     quote (first 200c): {r['kastner_quotation'][:200]!r}")
        print()

    print(f"=== Append plan ===")
    print(f"  master rows before    : {len(master_rows)}")
    print(f"  + admitted            : {len(new_rows)}")
    print(f"  master rows after     : {len(master_rows) + len(new_rows)}")
    print()

    if not commit:
        print("→ DRY-RUN — no write. Pass --commit to apply.")
        print()
        print("After --commit succeeds, RE-RUN to refresh the substrate:")
        print("  python3 ~/Desktop/Archive/scripts/union_article_corpus_v1.py --commit")
        return

    # 6. Backup
    ts = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    bak = MASTER_CSV.with_suffix(f".csv.bak_apply_unindexed_v2_{ts}")
    shutil.copy2(MASTER_CSV, bak)
    print(f"  backup written        : {bak.name}")

    # 7. Append (re-write entire master + new rows for atomicity + QUOTE_ALL guarantee)
    with open(MASTER_CSV, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=CANONICAL_COLS, quoting=csv.QUOTE_ALL)
        w.writeheader()
        for r in master_rows:
            w.writerow(r)
        for r in new_rows:
            w.writerow(r)

    # 8. Verify post-write count
    with open(MASTER_CSV) as f:
        post_rows = list(csv.DictReader(f))
    print(f"  master rows after     : {len(post_rows)}")
    assert len(post_rows) == len(master_rows) + len(new_rows), \
        f"row count mismatch: expected {len(master_rows) + len(new_rows)}, got {len(post_rows)}"

    print()
    print(f"→ WROTE: {MASTER_CSV} ({MASTER_CSV.stat().st_size:,} bytes)")
    print()
    print("NEXT: refresh the substrate so the new admissions land in")
    print("article_corpus_v1.json + quote_only_rows_v1.csv + _pdf_segments_unclaimed_v1.json:")
    print()
    print("  python3 ~/Desktop/Archive/scripts/union_article_corpus_v1.py --commit")


if __name__ == "__main__":
    main(commit=("--commit" in sys.argv))
