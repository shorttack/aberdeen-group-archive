#!/usr/bin/env python3
"""promote_quotations_to_master_v3.py

Promote v1.8.0 quotations corpus verdicts to a new sidecar master:
    ~/Desktop/Archive/aberdeen-group-archive/_master_quotations_prescience.csv

Sidecar pattern — does NOT modify kastner_quotes_clean.csv. Mirrors the
_master_prescience_scores.csv precedent: append-only, keyed on row_id,
preserves all corpus columns plus audit metadata.

Per session disposition 2026-06-19:
  - Q1: sidecar master (option β)
  - Q2: low_signal_flag TRUE for short pure-attribution quotes regardless of name
  - Q3: study-level rollup DEFERRED to a later script
  - Q4: all 27 corpus columns carry through

Schema (31 cols total):
  1-27.  Corpus columns verbatim from quotations_corpus_v1.csv
  28.    blog_scrape_contamination_flag  bool   computed per v3 predicate
  29.    scorer_version     str    "quotations_corpus_v1"
  30.    source_pass        str    "quotations_corpus"
  31.    promoted_at        str    UTC ISO timestamp at promote time

blog_scrape_contamination_flag rule (v3 — 2026-06-19 §11x semantic correction):
  flag = TRUE if quote contains ANY known blog-scrape platform artifact (case-insensitive).

  Patterns detect Blogger / oncomputerstips boilerplate scraped from RSS into
  the source corpus — the actual degenerate shape in this dataset. v1's
  "short attribution" hypothesis was empirically wrong: the real degenerates
  are LONG (40-80 words) blog footers + share-button text, while genuine
  short quotes ("No other vendor has anything close to this.") got false-
  positive flagged.

  Confirmed targets from manual inspection of session-context-flagged rids:
    rid 1180: 'Peter S Kastner Blogging at oncomputerstips.blogspot.com...'
    rid 1186: '-- Peter S. Kastner Posted by Anonymous... Email ThisBlogThis!Share...'
    rid 1200: '...Peter S. Kastner Posted by Anonymous at 12:12?AM No comments:...'

  IMPORTANT: This flag is an AUDIT signal about quote-TEXT quality. It does NOT
  imply the prescience verdict is wrong. Many flagged rows (e.g. rid 1188 and
  rid 1193, both dual-core processor predictions scored high) contain genuinely
  prescient content adjacent to Blogger platform boilerplate. Downstream
  consumers should treat the flag as 'this quote text may need cleaning' — not
  as 'this row is low signal'.

  Renamed from v2's `low_signal_flag` because the v2 semantics conflated
  text-quality (was this scraped cleanly?) with verdict-quality (is the
  prescience score sound?). These are independent dimensions.

  rid 1132 ('Peter Kastner, a personal computer analyst with the Aberdeen Group, said...')
  is intentionally NOT flagged: it's a legit news article quote with bracketed
  analyst attribution, correctly assigned 'low' by the scorer. Different category.

Standing invariants (per kastner-archive-pipeline + kastner-github skills):
  - Dry-run default; --commit opt-in
  - csv.QUOTE_ALL on every write
  - Backup before write: _master_quotations_prescience.csv.bak_promote_<utc>
    (only created on overwrite — new file on first run)
  - Row count preserved + reported (in == out)
  - UTC timestamps via datetime.timezone.utc (NOT datetime.utcnow())
  - Versioned _v1 from creation

CLI:
  --commit       write to disk (default: dry-run)
  --corpus PATH  override corpus CSV path
  --master PATH  override master CSV path
  --append       append to existing master instead of overwriting
                 (use when re-promoting incremental v1.8.x corpus deltas)
  --row-id ID    promote a single row only (for incremental testing)

Examples:
  python3 promote_quotations_to_master_v1.py                    # dry-run all 334
  python3 promote_quotations_to_master_v1.py --commit            # write all 334
  python3 promote_quotations_to_master_v1.py --row-id 731        # single row dry-run
  python3 promote_quotations_to_master_v1.py --append --commit   # incremental promote
"""

from __future__ import annotations

import argparse
import csv
import datetime as dt
import re
import shutil
import sys
from pathlib import Path

# ------------------------------------------------------------------------------
# Paths
# ------------------------------------------------------------------------------

DEFAULT_CORPUS = Path.home() / "Desktop/Archive/aberdeen-group-archive/kastner-author/quotations/quotations_corpus_v1.csv"
DEFAULT_MASTER = Path.home() / "Desktop/Archive/aberdeen-group-archive/_master_quotations_prescience.csv"

SCORER_VERSION = "quotations_corpus_v1"
SOURCE_PASS    = "quotations_corpus"

# Corpus column order (must match score_quotations_corpus_v1.py output)
CORPUS_COLS = [
    "row_id", "article_id", "horizon_label", "horizon_int",
    "analyst", "headline", "publication", "date", "quote",
    "p2_score", "p2_confidence", "p2_bucket", "p2_rationale",
    "p2_elapsed_sec", "p2_parse_ok",
    "tiebreaker_invoked",
    "p1_score", "p1_confidence", "p1_bucket", "p1_rationale",
    "p1_elapsed_sec", "p1_parse_ok",
    "final_score", "final_confidence", "final_bucket",
    "final_pipeline", "final_rationale",
]

# Sidecar adds 4 metadata cols
MASTER_COLS = CORPUS_COLS + [
    "blog_scrape_contamination_flag",
    "scorer_version",
    "source_pass",
    "promoted_at",
]

# ------------------------------------------------------------------------------
# blog_scrape_contamination_flag predicate (v3)
# ------------------------------------------------------------------------------

# Blog-scrape platform artifact patterns (all checked case-insensitive).
# These are unique sentinel strings from Blogger / oncomputerstips RSS
# scrapes that contaminate the source corpus.
BLOG_ARTIFACT_PATTERNS = (
    "posted by anonymous",
    "email thisblogthis",
    "share to twitter",
    "share to facebook",
    "share to pinterest",
    "blogging at",
    "oncomputerstips",
    "blog at oncomputers",
    "no comments:",
)


def compute_blog_scrape_contamination_flag(quote: str) -> bool:
    """Return True if quote contains Blogger/oncomputerstips platform boilerplate.

    Rule (v3, 2026-06-19 §11x):
      flag = TRUE if quote (case-insensitive) contains any pattern in
      BLOG_ARTIFACT_PATTERNS.

    Audit signal about quote-text contamination, not verdict-quality. Renamed
    from `compute_low_signal_flag` (v2). Many contaminated rows contain
    substantive prescient content adjacent to scrape artifacts; the flag
    only tells downstream queries the source text needs cleaning, not that
    the prescience verdict is unreliable.
    """
    if not isinstance(quote, str) or not quote.strip():
        return False
    lower = quote.lower()
    return any(p in lower for p in BLOG_ARTIFACT_PATTERNS)


# ------------------------------------------------------------------------------
# Main
# ------------------------------------------------------------------------------

def main() -> int:
    ap = argparse.ArgumentParser(description="Promote quotations corpus verdicts to sidecar master.")
    ap.add_argument("--commit", action="store_true", help="Write to disk (default: dry-run).")
    ap.add_argument("--corpus", type=Path, default=DEFAULT_CORPUS, help="Corpus CSV path.")
    ap.add_argument("--master", type=Path, default=DEFAULT_MASTER, help="Master sidecar CSV path.")
    ap.add_argument("--append", action="store_true",
                    help="Append to existing master (dedupe on row_id). Default: overwrite.")
    ap.add_argument("--row-id", type=str, default=None,
                    help="Promote only this row_id (for testing).")
    args = ap.parse_args()

    corpus_path: Path = args.corpus
    master_path: Path = args.master

    # ---- Verify corpus exists ----
    if not corpus_path.is_file():
        print(f"ERROR: corpus not found at {corpus_path}", file=sys.stderr)
        return 2

    # ---- Read corpus ----
    with open(corpus_path, newline="") as f:
        reader = csv.DictReader(f)
        if reader.fieldnames != CORPUS_COLS:
            print("ERROR: corpus schema mismatch", file=sys.stderr)
            print(f"  Expected: {CORPUS_COLS}", file=sys.stderr)
            print(f"  Got:      {reader.fieldnames}", file=sys.stderr)
            return 3
        corpus_rows = list(reader)

    print(f"Corpus: {corpus_path}")
    print(f"  rows: {len(corpus_rows)}")
    print(f"  cols: {len(CORPUS_COLS)}")

    # ---- Filter by --row-id if set ----
    if args.row_id is not None:
        corpus_rows = [r for r in corpus_rows if r["row_id"] == args.row_id]
        if not corpus_rows:
            print(f"ERROR: row_id={args.row_id} not found in corpus", file=sys.stderr)
            return 4
        print(f"  filtered to row_id={args.row_id}: {len(corpus_rows)} row(s)")

    # ---- Build promote rows ----
    promoted_at = dt.datetime.now(dt.timezone.utc).isoformat()
    out_rows = []
    flag_counter = {"flagged": 0, "unflagged": 0}
    bucket_counter = {"high": 0, "medium": 0, "low": 0, "parse_fail": 0, "human_review": 0}

    for r in corpus_rows:
        flag = compute_blog_scrape_contamination_flag(r.get("quote", ""))
        flag_counter["flagged" if flag else "unflagged"] += 1
        bucket = r.get("final_bucket", "")
        bucket_counter[bucket] = bucket_counter.get(bucket, 0) + 1
        out = dict(r)  # copy all 27 corpus cols
        out["blog_scrape_contamination_flag"] = "true" if flag else "false"
        out["scorer_version"] = SCORER_VERSION
        out["source_pass"] = SOURCE_PASS
        out["promoted_at"] = promoted_at
        out_rows.append(out)

    # ---- Append-mode dedupe ----
    final_rows = out_rows
    if args.append and master_path.exists():
        with open(master_path, newline="") as f:
            existing = list(csv.DictReader(f))
        existing_ids = {r["row_id"] for r in existing}
        new_only = [r for r in out_rows if r["row_id"] not in existing_ids]
        final_rows = existing + new_only
        print(f"Append mode: existing {len(existing)}, new {len(new_only)}, total {len(final_rows)}")

    # ---- Report ----
    print()
    print(f"Mode: {'COMMIT' if args.commit else 'DRY-RUN'}")
    print(f"Master: {master_path}")
    print(f"  rows to write: {len(final_rows)}")
    print(f"  cols: {len(MASTER_COLS)} ({len(CORPUS_COLS)} corpus + 4 metadata)")
    print()
    print("blog_scrape_contamination_flag distribution (this promote batch):")
    print(f"  contaminated:    {flag_counter['flagged']:>3}")
    print(f"  clean:           {flag_counter['unflagged']:>3}")
    print("  (NOTE: contamination = quote-text quality, not verdict quality.")
    print("   Many contaminated rows have substantive prescient content + scrape footer.)")
    print()
    print("final_bucket distribution (this promote batch):")
    for b in ("high", "medium", "low", "parse_fail", "human_review"):
        n = bucket_counter.get(b, 0)
        if n > 0:
            print(f"  {b:<13} {n:>3}")
    print()
    print(f"scorer_version: {SCORER_VERSION}")
    print(f"source_pass:    {SOURCE_PASS}")
    print(f"promoted_at:    {promoted_at}")

    # ---- Show flagged rows (always — small list, high signal) ----
    if flag_counter["flagged"] > 0:
        flagged_rids = [r["row_id"] for r in out_rows if r["blog_scrape_contamination_flag"] == "true"]
        print()
        print(f"Contaminated row_ids ({len(flagged_rids)}):")
        for rid in flagged_rids:
            row = next(r for r in out_rows if r["row_id"] == rid)
            preview = row["quote"][:60] + ("..." if len(row["quote"]) > 60 else "")
            print(f"  rid={rid:>5}  bucket={row['final_bucket']:<8} {preview!r}")

    if not args.commit:
        print()
        print("DRY-RUN only — pass --commit to write.")
        return 0

    # ---- Backup before overwrite ----
    if master_path.exists() and not args.append:
        ts = dt.datetime.now(dt.timezone.utc).strftime("%Y%m%dT%H%M%SZ")
        bak = master_path.with_suffix(f".csv.bak_promote_{ts}")
        shutil.copy2(master_path, bak)
        print(f"\nBackup: {bak}")
    elif master_path.exists() and args.append:
        ts = dt.datetime.now(dt.timezone.utc).strftime("%Y%m%dT%H%M%SZ")
        bak = master_path.with_suffix(f".csv.bak_append_{ts}")
        shutil.copy2(master_path, bak)
        print(f"\nBackup (append): {bak}")

    # ---- Write ----
    master_path.parent.mkdir(parents=True, exist_ok=True)
    with open(master_path, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=MASTER_COLS, quoting=csv.QUOTE_ALL)
        w.writeheader()
        w.writerows(final_rows)

    # ---- Verify ----
    with open(master_path, newline="") as f:
        verify = list(csv.DictReader(f))
    if len(verify) != len(final_rows):
        print(f"ERROR: row count mismatch after write: wrote {len(final_rows)}, read {len(verify)}", file=sys.stderr)
        return 5
    print(f"\nWrote: {master_path}")
    print(f"  verified: {len(verify)} rows × {len(MASTER_COLS)} cols")

    return 0


if __name__ == "__main__":
    sys.exit(main())
