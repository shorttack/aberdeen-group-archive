#!/usr/bin/env python3
"""
build_format_mismatch_review_v1.py

Companion to diagnose_pdf_format_mismatch_v4.py.

After v4 partitioned the 437 `pdf_format_mismatch` rows into:

  F4_not_in_pdf                       = 278  (terminal — PDF doesn't contain article)
  F0b_headline_also_not_in_pdf        = 132  (terminal — PDF doesn't contain article)
  F0a_headline_in_unclaimed_norm_gap  =  17  (salvageable — fuzzy-match)
  F6_detector_saw_different_title     =   7  (Pete-review — two real headlines, one wins)
  F3_headline_in_body_detector_missed =   2  (salvageable — detector missed it)
  F1_detector_grabbed_midsentence     =   1  (salvageable — re-aim detector)

…this script emits a 27-row REVIEW CSV containing the F0a + F6 + F3 + F1
rows in the SAME schema as `_unindexed_kastner_candidates_v3.csv`:

  col  0     reject                       (blank = ADMIT to Pipeline 1;
                                           any non-whitespace = REJECT,
                                           keep in Pipeline 2)
  cols 1-18  canonical kastner_quotes_clean.csv columns
             (copied verbatim from the existing CSV row — these rows
             already exist in the master with row_id assigned)
  cols 19+   provenance from the v4 diagnostic:
             source_segment_idx          (segment idx or article_seq)
             classification              (bucket class or 'corpus')
             discovery_rule              (F0a / F1 / F3 / F6)
             discovery_confidence        (high for F1/F3 substrate hits,
                                          medium for F0a fuzzy, low for F6
                                          which is genuinely ambiguous)
             detector_headline_attempted (what the PDF detector saw —
                                          may be very different from the
                                          CSV's headline value)

Reject-column semantics (Pete-prescribed):

    is_rejected = bool(row.get("reject", "").strip())
    # blank, None, whitespace = ADMIT
    # any non-whitespace character = REJECT

These 27 rows ARE ALREADY in `kastner_quotes_clean.csv` (they have valid
`row_id` values). Pete's review decision is binary:

  ADMIT (blank reject):   row should be re-routed to Pipeline 1 (article-context)
  REJECT (non-blank):     row stays in Pipeline 2 (quote-only) — current state

How the downstream apply works (deferred to apply_format_mismatch_review_v1.py):
  - F0a admits: emit a substrate-correction record that lets the next union
    run find the right corpus article / unclaimed segment for these row_ids
  - F1/F3 admits: same — substrate-correction (detector missed the article)
  - F6 admits: Pete may also edit the `headline` column on the review row
    to pick the canonical title; the apply script will REPLACE-by-row_id
    on the headline column

Output: `kastner-author/quotations/_format_mismatch_review_v1.csv`
Dry-run by default; --commit writes the CSV.
"""
import csv, json, re, sys, unicodedata
from datetime import datetime, timezone
from pathlib import Path
from collections import Counter, defaultdict

ARCHIVE_REPO = Path("/Users/scott/Desktop/Archive/aberdeen-group-archive")
QUOTATIONS_DIR = ARCHIVE_REPO / "kastner-author/quotations"
QUOTE_ONLY = QUOTATIONS_DIR / "quote_only_rows_v1.csv"
CORPUS = QUOTATIONS_DIR / "article_corpus_v1.json"
UNCLAIMED = QUOTATIONS_DIR / "_pdf_segments_unclaimed_v1.json"
OUT_CSV = QUOTATIONS_DIR / "_format_mismatch_review_v1.csv"

# Canonical CSV header — verbatim from kastner_quotes_clean.csv.
# Apply scripts depend on this exact order.
CANONICAL_COLS = [
    "row_id", "article_seq", "date", "headline", "publication", "author",
    "content_type", "kastner_quotation", "immediate_context", "is_predictive",
    "prescience_score", "prescience_rationale", "forecast_horizon_years",
    "theme", "decade", "accuracy_outcome", "verdict_rationale",
    "verdict_sources",
]
PROVENANCE_COLS = [
    "source_segment_idx", "classification", "discovery_rule",
    "discovery_confidence", "detector_headline_attempted",
]
OUTPUT_COLS = ["reject"] + CANONICAL_COLS + PROVENANCE_COLS

REASON_COL = "pipeline_route_reason"


# ---------- normalization helpers (copied from diagnose_v4 for byte-identity)

def _norm(s: str) -> str:
    if s is None:
        return ""
    s = unicodedata.normalize("NFKD", s)
    s = re.sub(r"[\u2018\u2019\u201A\u201B]", "'", s)
    s = re.sub(r"[\u201C\u201D\u201E\u201F]", '"', s)
    s = re.sub(r"[\u2013\u2014\u2015]", "-", s)
    s = re.sub(r"\s+", " ", s)
    return s.strip().lower()


def _probe_from_quote(quote: str, n: int = 80) -> str:
    q = re.sub(r"\s+", " ", (quote or "").strip())
    q = q.lstrip('"\u201C\u201D\'')
    if len(q) > n:
        q = q[:n].rsplit(" ", 1)[0]
    return q.strip()


def _looks_like_real_headline(s: str) -> bool:
    if not s:
        return False
    s = s.strip()
    if s.startswith('"') or s.startswith("\u201C"):
        return False
    words = s.split()
    if len(words) > 14:
        return False
    if re.search(r"\b(said|told|noted|argued|predicted|expects?|believes?|"
                 r"forecasts?|observed|commented|added|explained|claimed|"
                 r"warned|cautioned)\b", " ".join(words[:6]), re.IGNORECASE):
        return False
    return True


# ---------- classifier (re-runs v4 logic but EMITS the row per-bucket)

def classify_row(row, seg_lookup, article_bodies):
    """Return (bucket_label, sid_for_provenance, sclass_for_provenance,
    detector_headline_attempted) for one CSV row, or None to skip
    (terminal buckets F4 / F0b / F0c)."""
    headline = row.get("headline", "")
    quote = row.get("kastner_quotation", "")
    probe = _probe_from_quote(quote, n=80)
    probe_norm = _norm(probe)

    # Short-probe path → headline fallback (F0a vs F0b/F0c)
    if len(probe_norm) < 20:
        h_norm = _norm(headline)
        if len(h_norm) < 12:
            return None  # F0c terminal
        headline_found_in = None
        for seg_idx, seg in seg_lookup.items():
            if h_norm in _norm(seg["body"]):
                headline_found_in = ("unclaimed", seg_idx, seg)
                break
        if not headline_found_in:
            for art in article_bodies:
                if h_norm in _norm(art["body"]):
                    headline_found_in = ("corpus", art["article_seq"], art)
                    break
        if headline_found_in:
            kind, sid, sdata = headline_found_in
            if kind == "corpus":
                return ("F0a", sid, "corpus", sdata.get("headline", "")[:200])
            return ("F0a", sid, sdata.get("classification", ""),
                    (sdata.get("headline_attempted") or "")[:200])
        return None  # F0b terminal

    # Long-probe path: search unclaimed first, then corpus
    landed_in = None
    for seg_idx, seg in seg_lookup.items():
        if probe_norm in _norm(seg["body"]):
            landed_in = ("unclaimed", seg_idx, seg)
            break
    if not landed_in:
        for art in article_bodies:
            if probe_norm in _norm(art["body"]):
                landed_in = ("corpus", art["article_seq"], art)
                break

    if not landed_in:
        return None  # F4 terminal

    kind, sid, sdata = landed_in
    if kind == "corpus":
        detector_saw = sdata.get("headline", "")
        seg_class = "corpus"
    else:
        detector_saw = sdata.get("headline_attempted") or ""
        seg_class = sdata.get("classification", "")

    csv_h_norm = _norm(headline)
    h_in_body = (csv_h_norm and len(csv_h_norm) >= 8
                 and csv_h_norm in _norm(
                     sdata.get("body", "") if kind == "corpus"
                     else sdata.get("body", "")))

    # F3: headline IS in PDF body but detector saw something else
    if h_in_body and detector_saw and _norm(detector_saw) != csv_h_norm:
        return ("F3", sid, seg_class, detector_saw[:200])

    # F1: detector grabbed mid-sentence (not a real headline)
    if detector_saw and not _looks_like_real_headline(detector_saw):
        return ("F1", sid, seg_class, detector_saw[:200])

    # F6: detector saw a different real-looking headline
    if detector_saw and _looks_like_real_headline(detector_saw) \
            and _norm(detector_saw) != csv_h_norm:
        return ("F6", sid, seg_class, detector_saw[:200])

    # Otherwise we shouldn't be here — fall through with an explicit label
    return ("F5", sid, seg_class, detector_saw[:200])


# Confidence mapping per bucket
CONFIDENCE = {
    "F0a": "medium",   # fuzzy headline match — Pete confirms it's the same article
    "F1":  "high",     # detector clearly misfired — substrate fix
    "F3":  "high",     # headline IS in body, detector missed it — substrate fix
    "F6":  "low",      # two real-looking headlines disagree — Pete picks one
}

# Salvageable buckets we emit to the review CSV
SALVAGE_BUCKETS = {"F0a", "F1", "F3", "F6"}


def main(commit: bool = False):
    print(f"[build_format_mismatch_review_v1] {datetime.now(timezone.utc).isoformat()}")
    print(f"Mode: {'COMMIT' if commit else 'DRY-RUN'}")
    print()

    # Load substrate
    with open(QUOTE_ONLY) as f:
        quote_only = list(csv.DictReader(f))
    corpus = json.loads(CORPUS.read_text())
    unclaimed = json.loads(UNCLAIMED.read_text())

    print(f"  quote_only_rows_v1.csv : {len(quote_only)} rows")
    print(f"  article_corpus_v1.json : {corpus['article_count']} articles")
    print(f"  unclaimed segments     : {unclaimed['unclaimed_segment_count']}")

    if REASON_COL not in quote_only[0]:
        print(f"  !! reason column '{REASON_COL}' not found")
        print(f"  cols: {list(quote_only[0].keys())}")
        sys.exit(1)

    mismatch_rows = [r for r in quote_only
                     if r.get(REASON_COL) == "pdf_format_mismatch"]
    print(f"  pdf_format_mismatch rows: {len(mismatch_rows)}")
    print()

    # Build segment + article body lookups
    seg_lookup = {}
    for seg in unclaimed["segments"]:
        seg_lookup[seg["segment_idx"]] = {
            "body": seg.get("raw_preview", ""),
            "classification": seg.get("classification", ""),
            "headline_attempted": seg.get("headline_attempted", ""),
        }
    article_bodies = []
    for a in corpus["articles"]:
        article_bodies.append({
            "article_seq": a.get("article_seq"),
            "headline": a.get("headline", ""),
            "body": a.get("body_text", ""),
        })

    # Classify and collect salvage rows
    bucket_counter = Counter()
    review_rows = []
    for row in mismatch_rows:
        result = classify_row(row, seg_lookup, article_bodies)
        if result is None:
            bucket_counter["terminal (F4/F0b/F0c)"] += 1
            continue
        bucket, sid, sclass, detector_saw = result
        bucket_counter[bucket] += 1
        if bucket not in SALVAGE_BUCKETS:
            continue  # F5 — should be rare, skip from review

        review = {"reject": ""}
        for col in CANONICAL_COLS:
            review[col] = row.get(col, "")
        review["source_segment_idx"] = sid if sid is not None else ""
        review["classification"] = sclass
        review["discovery_rule"] = bucket
        review["discovery_confidence"] = CONFIDENCE.get(bucket, "")
        review["detector_headline_attempted"] = detector_saw
        review_rows.append(review)

    print("=== Bucket counts (re-derived) ===")
    for bucket, cnt in sorted(bucket_counter.items()):
        print(f"  {bucket:35s} : {cnt:>4}")
    print()
    print(f"Salvage rows emitted to review CSV: {len(review_rows)}")
    bucket_breakdown = Counter(r["discovery_rule"] for r in review_rows)
    print(f"  by bucket: {dict(bucket_breakdown)}")
    print()

    # Schema audit
    bad = [i for i, r in enumerate(review_rows)
           if set(r.keys()) != set(OUTPUT_COLS)]
    if bad:
        print(f"  !! SCHEMA AUDIT FAIL: {len(bad)} rows have wrong keys "
              f"(first idx: {bad[0]})")
        sys.exit(1)
    print(f"  schema audit: OK ({len(OUTPUT_COLS)} cols per row)")
    print()

    # Sample rows
    print("=== Sample rows (one per salvage bucket) ===")
    seen = set()
    for r in review_rows:
        b = r["discovery_rule"]
        if b in seen:
            continue
        seen.add(b)
        print(f"  [{b}] row_id={r['row_id']!r} confidence={r['discovery_confidence']}")
        print(f"     csv_headline    : {r['headline'][:100]!r}")
        print(f"     detector_saw    : {r['detector_headline_attempted'][:100]!r}")
        print(f"     source_seg_idx  : {r['source_segment_idx']} "
              f"(class={r['classification']})")
        print(f"     quote first 100c: {r['kastner_quotation'][:100]!r}")
        print()

    if not commit:
        print("\u2192 DRY-RUN \u2014 no CSV written. Pass --commit to write.")
        print(f"   Would write {len(review_rows)} rows \u00d7 "
              f"{len(OUTPUT_COLS)} cols to {OUT_CSV}")
        return

    with open(OUT_CSV, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=OUTPUT_COLS, quoting=csv.QUOTE_ALL)
        w.writeheader()
        for r in review_rows:
            w.writerow(r)
    print(f"\u2192 WROTE: {OUT_CSV} ({OUT_CSV.stat().st_size:,} bytes, "
          f"{len(review_rows)} rows \u00d7 {len(OUTPUT_COLS)} cols)")


if __name__ == "__main__":
    main(commit=("--commit" in sys.argv))
