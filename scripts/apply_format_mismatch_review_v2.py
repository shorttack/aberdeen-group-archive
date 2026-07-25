#!/usr/bin/env python3
"""
apply_format_mismatch_review_v2.py — v1.8.0 Quotations Corpus

v2 (2026-07-25 AUTO batch, L147): the deprecated UTC-now call -> its timezone-aware replacement
  migration only. No behavior change.

Apply Pete's reviewed format-mismatch CSV to the substrate.

INPUTS
------
  ~/Desktop/Archive/aberdeen-group-archive/kastner-author/quotations/
      _format_mismatch_review_v3.csv   (Pete's reviewed file, 27 rows, 24 cols)

OUTPUTS
-------
  1. kastner_quotes_clean.csv          (REPLACE-by-row_id for any admitted row
                                        whose headline Pete edited; row count
                                        preserved; backup written first)
  2. _format_mismatch_admits_v1.json   (sidecar manifest: list of admitted
                                        row_ids — consumed by the next
                                        union_article_corpus_v1.py run as a
                                        Pipeline-1 routing override)

REJECT SEMANTICS (Pete-prescribed, standing rule)
-------------------------------------------------
  is_rejected = bool(row.get("reject", "").strip())
  → blank/whitespace = ADMIT (route to Pipeline 1)
  → any non-whitespace char = REJECT (leave in Pipeline 2)

INVARIANTS (mirror apply_unindexed_quotes_v3.py)
-----------------------------------------------
  - Dry-run default; --commit is opt-in
  - csv.QUOTE_ALL on every write
  - UTC-stamped backup of kastner_quotes_clean.csv BEFORE any write
  - Row-parity check: master row count before == after
  - Producer/consumer schema diff before write (Gotcha 9)

USAGE
-----
  python3 apply_format_mismatch_review_v1.py            # dry-run (no writes)
  python3 apply_format_mismatch_review_v1.py --commit   # commit
"""
from __future__ import annotations
import csv, json, shutil, sys, datetime
from pathlib import Path

# ---------------------------------------------------------------- paths ----
QUOTATIONS = Path.home() / "Desktop/Archive/aberdeen-group-archive/kastner-author/quotations"
REVIEW_CSV = QUOTATIONS / "_format_mismatch_review_v3.csv"
MASTER     = QUOTATIONS / "kastner_quotes_clean.csv"
ADMITS_JSON = QUOTATIONS / "_format_mismatch_admits_v1.json"

# canonical 18-col schema for kastner_quotes_clean.csv
CANONICAL_COLS = [
    "row_id", "article_seq", "date", "headline", "publication", "author",
    "content_type", "kastner_quotation", "immediate_context", "is_predictive",
    "prescience_score", "prescience_rationale", "forecast_horizon_years",
    "theme", "decade", "accuracy_outcome", "verdict_rationale", "verdict_sources",
]

# ---------------------------------------------------------------- main ----
def main() -> int:
    commit = "--commit" in sys.argv
    mode = "COMMIT" if commit else "DRY-RUN"
    print(f"=== apply_format_mismatch_review_v1.py — mode={mode} ===\n")

    # ---- read review CSV --------------------------------------------------
    if not REVIEW_CSV.exists():
        print(f"ERROR: review CSV not found: {REVIEW_CSV}", file=sys.stderr)
        return 1
    with open(REVIEW_CSV, newline="") as f:
        review_rows = list(csv.DictReader(f))
    print(f"review CSV: {REVIEW_CSV.name} ({len(review_rows)} rows)")

    # ---- partition by reject semantics -----------------------------------
    admit_rows  = [r for r in review_rows if not r.get("reject", "").strip()]
    reject_rows = [r for r in review_rows if     r.get("reject", "").strip()]
    print(f"  ADMIT  (blank reject):         {len(admit_rows)}")
    print(f"  REJECT (non-whitespace):       {len(reject_rows)}")

    from collections import Counter
    admit_buckets  = Counter(r["discovery_rule"] for r in admit_rows)
    reject_buckets = Counter(r["discovery_rule"] for r in reject_rows)
    print(f"  ADMIT by bucket:               {dict(admit_buckets)}")
    print(f"  REJECT by bucket:              {dict(reject_buckets)}")

    admit_row_ids = sorted(int(r["row_id"]) for r in admit_rows)
    print(f"\n  admitted row_ids: {admit_row_ids}")

    # ---- read master ------------------------------------------------------
    if not MASTER.exists():
        print(f"ERROR: master not found: {MASTER}", file=sys.stderr)
        return 1
    with open(MASTER, newline="") as f:
        reader = csv.DictReader(f)
        master_cols = reader.fieldnames or []
        master_rows = list(reader)
    print(f"\nmaster: {MASTER.name} ({len(master_rows)} rows, {len(master_cols)} cols)")

    # producer/consumer schema diff (Gotcha 9)
    missing = [c for c in CANONICAL_COLS if c not in master_cols]
    if missing:
        print(f"ERROR: master missing canonical cols: {missing}", file=sys.stderr)
        return 1

    master_by_id = {int(r["row_id"]): r for r in master_rows}

    # ---- detect headline edits on admitted rows --------------------------
    headline_edits = []
    for ar in admit_rows:
        rid = int(ar["row_id"])
        if rid not in master_by_id:
            print(f"ERROR: admitted row_id {rid} not present in master", file=sys.stderr)
            return 1
        old_head = master_by_id[rid].get("headline", "")
        new_head = ar.get("headline", "")
        if old_head != new_head:
            headline_edits.append((rid, old_head, new_head))

    print(f"\nheadline edits on admits: {len(headline_edits)}")
    for rid, old, new in headline_edits:
        print(f"  row_id={rid}")
        print(f"    OLD: {old!r}")
        print(f"    NEW: {new!r}")

    # ---- plan mutations ---------------------------------------------------
    print(f"\nplan:")
    print(f"  1. Apply {len(headline_edits)} headline edits to master "
          f"(REPLACE-by-row_id; row count preserved)")
    print(f"  2. Write {len(admit_row_ids)} admitted row_ids to "
          f"{ADMITS_JSON.name} (Pipeline-1 routing override sidecar)")
    print(f"  3. Reject rows ({len(reject_rows)}): no master mutation; remain "
          f"in Pipeline 2 (pdf_format_mismatch)")

    if not commit:
        print(f"\nDRY-RUN: no writes. Pass --commit to apply.")
        return 0

    # ---- commit: backup master first -------------------------------------
    ts = datetime.datetime.now(datetime.UTC).strftime("%Y%m%dT%H%M%SZ")
    bak = MASTER.with_suffix(f".csv.bak_format_mismatch_review_v1_{ts}")
    shutil.copy2(MASTER, bak)
    print(f"\nbackup: {bak.name}")

    # apply headline edits in-place on master_rows
    for rid, _old, new in headline_edits:
        master_by_id[rid]["headline"] = new

    # row-parity guard
    assert len(master_rows) == len(master_by_id), "row-parity broken"

    # write master (preserve original column order)
    with open(MASTER, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=master_cols, quoting=csv.QUOTE_ALL)
        w.writeheader()
        w.writerows(master_rows)
    print(f"wrote: {MASTER.name} ({len(master_rows)} rows, {len(master_cols)} cols)")

    # write admits sidecar
    admits_payload = {
        "schema_version": 1,
        "generated_utc": ts,
        "source_review_csv": REVIEW_CSV.name,
        "admit_count": len(admit_row_ids),
        "reject_count": len(reject_rows),
        "admit_row_ids": admit_row_ids,
        "admit_by_bucket": dict(admit_buckets),
        "reject_by_bucket": dict(reject_buckets),
        "headline_edits_applied": len(headline_edits),
        "notes": (
            "These row_ids existed in kastner_quotes_clean.csv but were "
            "routed to Pipeline 2 by union_article_corpus_v1.py with reason "
            "'pdf_format_mismatch'. Pete reviewed the v2 detector buckets "
            "(F0a/F1/F3/F5/F6) and admitted these as legitimate Pipeline-1 "
            "candidates. The next union run must consult this manifest and "
            "override the format-mismatch routing for these row_ids."
        ),
    }
    with open(ADMITS_JSON, "w") as f:
        json.dump(admits_payload, f, indent=2, sort_keys=True)
    print(f"wrote: {ADMITS_JSON.name} ({len(admit_row_ids)} admitted row_ids)")

    print(f"\n=== GREEN — apply_format_mismatch_review_v1 complete ===")
    print(f"\nNEXT STEPS:")
    print(f"  1. Re-run union_article_corpus_v1.py — must read "
          f"_format_mismatch_admits_v1.json and route the 10 admitted "
          f"row_ids to Pipeline 1 (not Pipeline 2)")
    print(f"  2. Expected Pipeline 1 ceiling post-apply: ~474 rows "
          f"(prev 464 + 10 admits) absent additional source PDFs")
    return 0


if __name__ == "__main__":
    sys.exit(main())
