#!/usr/bin/env python3
"""
diagnose_pdf_format_mismatch_v3.py

Diagnose the 437 `pdf_format_mismatch` rows in quote_only_rows_v1.csv.

A `pdf_format_mismatch` row means:
  - The CSV row has a non-empty `headline` and `kastner_quotation`
  - At least one PDF segment exists (PDF scan succeeded)
  - The headline detector ran but no detected article-head matched the CSV's
    headline. So the row drops to Pipeline 2 (quote-only / loose horizon).

The detector failure could be in the headline-detection step, the
headline-normalization step, or because the article genuinely isn't in the
PDF. This script categorizes which.

Methodology (substrate-only; no API):
  For each pdf_format_mismatch CSV row:
    1. Take the first ~80 chars of `kastner_quotation` as a search probe
    2. Search ALL PDF segments (claimed + unclaimed) for that probe
    3. If found, look at the segment(s) where it landed and at any
       adjacent segments to see what the detector saw vs. what the CSV
       expects
    4. Categorize the failure mode:

       F1 — quote found; detector grabbed mid-sentence as headline
            (segment's headline_attempted is clearly not a real title)
       F2 — quote found; headline appears to span two segments
            (probe lands in segment N but CSV headline is partial-match in
            segment N-1 tail; classic page-break/column-break split)
       F3 — quote found; detector saw the headline but with prefix/suffix
            junk that broke normalization (pub name, date, em-dash, ALL
            CAPS, byline)
       F4 — quote NOT found anywhere in PDF segments
            (article genuinely isn't in the PDF scan; no substrate fix
            will recover it)
       F5 — quote found; detector saw something reasonable but
            normalization rule needs tuning (CSV says "Apple Q3 Sales"
            vs detector saw "Apple's Q3 Sales Report")
       F0 — uncategorized (fallback bucket for diagnosis)

Outputs to stdout:
  - Total mismatch row count
  - Per-failure-mode count + percent
  - 3 sample rows per failure mode with:
    - CSV row_id, headline, first 100c of quote
    - segment_idx where probe landed (if any)
    - segment classification + headline_attempted

No file writes. Pete reads the report, picks the salvage target, then I
write a targeted salvage script.
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
CSV_PATH = QUOTATIONS_DIR / "kastner_quotes_clean.csv"

# PDF source — need access to the actual PDF text per segment.
# We use _pdf_segments_unclaimed for unclaimed segments AND we'll re-derive
# claimed-segment bodies from the corpus (which keeps the segment body_text
# embedded inside the article record).


def _norm(s: str) -> str:
    if s is None:
        return ""
    s = unicodedata.normalize("NFKD", s)
    s = re.sub(r"[\u2018\u2019\u201A\u201B]", "'", s)
    s = re.sub(r"[\u201C\u201D\u201E\u201F]", '"', s)
    s = re.sub(r"[\u2013\u2014\u2015]", "-", s)  # em/en dash
    s = re.sub(r"\s+", " ", s)
    return s.strip().lower()


def _probe_from_quote(quote: str, n: int = 80) -> str:
    """Build a search probe from the first n chars of the quote.

    Skip leading quotes/whitespace and a few common opening words so the
    probe is content-rich.
    """
    q = re.sub(r"\s+", " ", (quote or "").strip())
    # strip leading quote chars
    q = q.lstrip('"\u201C\u201D\'')
    # take first n chars but cut at last space to avoid mid-word
    if len(q) > n:
        q = q[:n].rsplit(" ", 1)[0]
    return q.strip()


def _headline_in_body(headline: str, body: str) -> int:
    """Return char position of headline in body if found (normalized), else -1."""
    h_norm = _norm(headline)
    if not h_norm or len(h_norm) < 8:
        return -1
    b_norm = _norm(body)
    return b_norm.find(h_norm)


def _looks_like_real_headline(s: str) -> bool:
    """Heuristic: does this look like an article title vs. a mid-sentence grab?

    Real titles tend to be:
      - <= 12 words
      - Not start with a quote mark
      - Not contain attribution verbs (said, told, etc.) before any verb
      - Title-case or short
    Mid-sentence grabs tend to:
      - Start with a quote, "But", "However", or be 15+ words
      - Contain "said", "told", "noted" before word 6
    """
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


def main():
    print(f"[diagnose_pdf_format_mismatch_v1] {datetime.now(timezone.utc).isoformat()}")
    print()

    # Load substrate
    with open(QUOTE_ONLY) as f:
        quote_only = list(csv.DictReader(f))
    corpus = json.loads(CORPUS.read_text())
    unclaimed = json.loads(UNCLAIMED.read_text())

    print(f"  quote_only_rows_v1.csv : {len(quote_only)} rows")
    print(f"  article_corpus_v1.json : {corpus['article_count']} articles")
    print(f"  unclaimed segments     : {unclaimed['unclaimed_segment_count']}")

    # Filter to pdf_format_mismatch. Column written by union_article_corpus_v1
    # is `pipeline_route_reason` (not `partition_reason`).
    REASON_COL = "pipeline_route_reason"
    if quote_only and REASON_COL not in quote_only[0]:
        # Sanity dump available reason-like columns
        sample_cols = [c for c in quote_only[0].keys() if "reason" in c.lower()]
        print(f"  !! reason column not found. reason-like cols: {sample_cols}")
        print(f"  all cols: {list(quote_only[0].keys())}")
        sys.exit(1)
    reason_counter = Counter(r.get(REASON_COL, "") for r in quote_only)
    print(f"  pipeline_route_reason distribution: {dict(reason_counter)}")
    mismatch_rows = [r for r in quote_only
                     if r.get(REASON_COL) == "pdf_format_mismatch"]
    print(f"  pdf_format_mismatch rows: {len(mismatch_rows)}")
    print()

    # Build a unified segment lookup: segment_idx → (body_text, classification, headline_attempted)
    # From unclaimed: directly available
    # From corpus articles: each article has a body_text spanning page_range
    #   We treat the article body as a synthetic "segment" indexed by its
    #   article_seq (negative idx to distinguish from real segment idxs)
    seg_lookup = {}
    for seg in unclaimed["segments"]:
        seg_lookup[seg["segment_idx"]] = {
            "kind": "unclaimed_segment",
            "body": seg.get("raw_preview", ""),
            "classification": seg.get("classification", ""),
            "headline_attempted": seg.get("headline_attempted", ""),
        }
    # Add corpus articles as searchable bodies
    article_bodies = []
    for a in corpus["articles"]:
        article_bodies.append({
            "article_seq": a.get("article_seq"),
            "headline": a.get("headline", ""),
            "body": a.get("body_text", ""),
            "page_range": a.get("page_range", []),
        })

    print(f"  unclaimed seg lookup    : {len(seg_lookup)} entries")
    print(f"  corpus article bodies   : {len(article_bodies)} articles")
    print()

    # Categorize each mismatch row
    failure_mode = Counter()
    samples = defaultdict(list)

    for row in mismatch_rows:
        headline = row.get("headline", "")
        quote = row.get("kastner_quotation", "")
        probe = _probe_from_quote(quote, n=80)
        probe_norm = _norm(probe)

        if len(probe_norm) < 20:
            # Probe too short to be reliable — bucket as F0
            failure_mode["F0_probe_too_short"] += 1
            if len(samples["F0_probe_too_short"]) < 3:
                samples["F0_probe_too_short"].append({
                    "row_id": row.get("row_id", ""),
                    "headline": headline[:100],
                    "quote_first_100": quote[:100],
                    "note": f"probe_norm len={len(probe_norm)}",
                })
            continue

        # Search unclaimed segments first (most likely failure surface)
        landed_in = None
        for seg_idx, seg in seg_lookup.items():
            if probe_norm in _norm(seg["body"]):
                landed_in = ("unclaimed", seg_idx, seg)
                break

        # If not in unclaimed, search corpus article bodies
        if not landed_in:
            for art in article_bodies:
                if probe_norm in _norm(art["body"]):
                    landed_in = ("corpus", art["article_seq"], art)
                    break

        if not landed_in:
            # F4: quote not in PDF at all
            failure_mode["F4_not_in_pdf"] += 1
            if len(samples["F4_not_in_pdf"]) < 3:
                samples["F4_not_in_pdf"].append({
                    "row_id": row.get("row_id", ""),
                    "headline": headline[:100],
                    "quote_first_100": quote[:100],
                    "probe": probe[:60],
                })
            continue

        location_kind, seg_id, seg_data = landed_in
        body = seg_data["body"]

        if location_kind == "corpus":
            # F5: quote IS in a corpus article body, but the join logic
            # didn't link the CSV row to that article. Almost certainly
            # a headline-normalization gap.
            failure_mode["F5_in_corpus_join_failed"] += 1
            if len(samples["F5_in_corpus_join_failed"]) < 3:
                samples["F5_in_corpus_join_failed"].append({
                    "row_id": row.get("row_id", ""),
                    "csv_headline": headline[:100],
                    "corpus_article_seq": seg_id,
                    "corpus_article_headline": seg_data["headline"][:100],
                    "quote_first_100": quote[:100],
                })
            continue

        # location_kind == "unclaimed"
        seg = seg_data
        hdl_attempted = seg.get("headline_attempted") or ""
        hdl_in_body_pos = _headline_in_body(headline, body)

        if hdl_in_body_pos >= 0:
            # The real CSV headline IS in the segment body — detector just
            # missed it. F3: normalization gap (detector saw something but
            # not the canonical headline).
            failure_mode["F3_headline_in_body_detector_missed"] += 1
            if len(samples["F3_headline_in_body_detector_missed"]) < 3:
                samples["F3_headline_in_body_detector_missed"].append({
                    "row_id": row.get("row_id", ""),
                    "csv_headline": headline[:100],
                    "headline_pos_in_body": hdl_in_body_pos,
                    "detector_saw": hdl_attempted[:100],
                    "seg_idx": seg_id,
                    "seg_class": seg.get("classification", ""),
                })
            continue

        # Headline not in this segment's body. Check adjacent segments for F2.
        adjacent_hit = False
        for adj_idx in (seg_id - 1, seg_id + 1):
            adj = seg_lookup.get(adj_idx)
            if adj and _headline_in_body(headline, adj["body"]) >= 0:
                adjacent_hit = True
                break

        if adjacent_hit:
            failure_mode["F2_headline_in_adjacent_segment"] += 1
            if len(samples["F2_headline_in_adjacent_segment"]) < 3:
                samples["F2_headline_in_adjacent_segment"].append({
                    "row_id": row.get("row_id", ""),
                    "csv_headline": headline[:100],
                    "quote_in_seg": seg_id,
                    "headline_in_adjacent_seg": True,
                    "detector_saw": hdl_attempted[:100],
                })
            continue

        # Quote found, headline not in this or adjacent segment.
        # Detector either grabbed mid-sentence (F1) or saw nothing usable.
        if hdl_attempted and not _looks_like_real_headline(hdl_attempted):
            failure_mode["F1_detector_grabbed_midsentence"] += 1
            if len(samples["F1_detector_grabbed_midsentence"]) < 3:
                samples["F1_detector_grabbed_midsentence"].append({
                    "row_id": row.get("row_id", ""),
                    "csv_headline": headline[:100],
                    "detector_grabbed": hdl_attempted[:100],
                    "seg_idx": seg_id,
                    "seg_class": seg.get("classification", ""),
                    "quote_first_100": quote[:100],
                })
            continue

        # Catch-all: quote in PDF, headline nowhere obvious, detector saw
        # something that LOOKS like a real headline but it doesn't match.
        # Could be: (a) CSV headline is paraphrased / shortened from real
        # PDF title; (b) PDF has a different title than what Pete logged.
        failure_mode["F6_detector_saw_different_title"] += 1
        if len(samples["F6_detector_saw_different_title"]) < 3:
            samples["F6_detector_saw_different_title"].append({
                "row_id": row.get("row_id", ""),
                "csv_headline": headline[:100],
                "detector_saw": hdl_attempted[:100],
                "seg_idx": seg_id,
                "seg_class": seg.get("classification", ""),
            })

    # Report
    total = len(mismatch_rows)
    if total == 0:
        print("!! No pdf_format_mismatch rows found. Nothing to diagnose.")
        return
    print(f"=== Failure mode distribution ({total} rows) ===")
    for mode, count in failure_mode.most_common():
        pct = 100.0 * count / total
        print(f"  {mode:<48} {count:>4}  ({pct:5.1f}%)")
    print()

    # Salvageability summary
    salvageable = {
        "F1_detector_grabbed_midsentence": "salvageable (rebuild headline detector on wider window)",
        "F2_headline_in_adjacent_segment": "salvageable (join adjacent segments before detection)",
        "F3_headline_in_body_detector_missed": "salvageable (fuzzy-match CSV headline against segment body)",
        "F5_in_corpus_join_failed": "salvageable (loosen headline normalization in union step)",
        "F6_detector_saw_different_title": "Pete-review (may be CSV paraphrase or wrong title)",
        "F4_not_in_pdf": "NOT salvageable (article not in PDF scan)",
        "F0_probe_too_short": "diagnose first (quote too short to probe reliably)",
    }
    print(f"=== Salvageability ===")
    sal_count = 0
    for mode in ["F1_detector_grabbed_midsentence",
                 "F2_headline_in_adjacent_segment",
                 "F3_headline_in_body_detector_missed",
                 "F5_in_corpus_join_failed"]:
        sal_count += failure_mode.get(mode, 0)
    print(f"  substrate-salvageable             : {sal_count} / {total} ({100.0*sal_count/total:.1f}%)")
    print(f"  Pete-review (different title)     : {failure_mode.get('F6_detector_saw_different_title', 0)}")
    print(f"  NOT salvageable (not in PDF)      : {failure_mode.get('F4_not_in_pdf', 0)}")
    print()

    for mode in failure_mode:
        print(f"=== Samples: {mode} ({failure_mode[mode]} total) — {salvageable.get(mode, '?')}")
        for s in samples[mode]:
            print(f"  {s}")
        print()


if __name__ == "__main__":
    main()
