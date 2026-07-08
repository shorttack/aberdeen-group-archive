#!/usr/bin/env python3
"""
union_article_corpus_v1.py

v1.8.0 substrate-builder. Runs the RTF extractor and PDF detector once,
dedupes their results, and emits three canonical files that v1.8.0 (and
all downstream versions) consume exclusively. After this script runs to
--commit, no future version should re-parse the source PDF/RTF unless
the source files themselves change.

Outputs (all under kastner-author/quotations/):

  1. article_corpus_v1.json
     The canonical Pipeline 1 substrate. Every entry is a structured
     article with headline + date + body + provenance (rtf or pdf).
     Dedup: (date, normalized-headline) — RTF wins ties (cleaner format).

  2. _pdf_segments_unclaimed_v1.json
     Every PDF form-feed segment that did NOT contribute to a successful
     article_corpus entry. Indexed by segment_index, with raw 600-char
     preview and the detector's classification + reason. THIS IS THE
     SALVAGE SUBSTRATE — any future detector improvement can read this
     file directly without re-parsing the source PDF.

  3. quote_only_rows_v1.csv
     The CSV row_ids routed to Pipeline 2 (quote+immediate_context
     scoring). Each row carries pipeline_route_reason in
     {not_in_pdf, pdf_format_mismatch, wrong_headline_detected,
     mis_classified_continuation, mis_classified_unknown}. Final per-row
     pipeline decision — should never be re-litigated.

Once we have these three files committed, "v1.8.0 scoring" reads from
them and never touches the source PDF.

Dry-run by default. --commit writes all three to the repo path.
"""
import csv, json, re, subprocess, sys, unicodedata, importlib.util
from datetime import datetime, timezone
from pathlib import Path
from collections import Counter

ARCHIVE_REPO = Path("/Users/scott/Desktop/Archive/aberdeen-group-archive")
QUOTATIONS_DIR = ARCHIVE_REPO / "kastner-author/quotations"
PDF_PATH = Path("/Users/scott/Desktop/Archive/Kastner_Consolidated_Quotes.pdf")
RTF_PATH = Path("/Users/scott/Desktop/Archive/Kastner_cleaned_quotes.rtf")
CSV_PATH = QUOTATIONS_DIR / "kastner_quotes_clean.csv"

CORPUS_OUT = QUOTATIONS_DIR / "article_corpus_v1.json"
UNCLAIMED_OUT = QUOTATIONS_DIR / "_pdf_segments_unclaimed_v1.json"
QUOTE_ONLY_OUT = QUOTATIONS_DIR / "quote_only_rows_v1.csv"

# Detector and extractor scripts (on Mac, scripts dir)
SCRIPTS_DIR = Path("/Users/scott/Desktop/Archive/scripts")
DETECTOR_PATH = SCRIPTS_DIR / "detect_article_boundaries_v2.py"
RTF_EXTRACTOR_PATH = SCRIPTS_DIR / "extract_rtf_articles_v1.py"


def normalize_text(s: str) -> str:
    s = unicodedata.normalize("NFKD", s)
    s = s.replace("\u2019", "'").replace("\u2018", "'")
    s = s.replace("\u201c", '"').replace("\u201d", '"')
    s = s.replace("\u2014", "-").replace("\u2013", "-")
    s = re.sub(r"\s+", " ", s)
    return s.strip().lower().strip("'\"").rstrip(";,.:").strip()


def load_module(path: Path, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def build_rtf_articles():
    """Run extract_rtf_articles_v1 against the RTF."""
    rtf_mod = load_module(RTF_EXTRACTOR_PATH, "rtf_extractor")
    text = rtf_mod.extract_plain_text(RTF_PATH)
    articles = rtf_mod.extract_articles(text)
    out = []
    for a in articles:
        if not a.get("headline") or not a.get("date"):
            continue
        out.append({
            "source": "rtf",
            "source_idx": a["article_idx"],
            "headline": a["headline"],
            "headline_norm": a["headline_norm"],
            "date": a["date"],
            "page_no": a["page_no"],
            "author_hint": a.get("author_hint"),
            "metadata_line": a.get("metadata_line"),
            "body": a.get("body", ""),
            "body_chars": a.get("body_chars", len(a.get("body", ""))),
        })
    return out


def build_pdf_articles_and_classifications():
    """Run detect_article_boundaries_v2 against the PDF and return:
       - the assembled articles (list of dicts with headline, body, segment_idx)
       - the per-segment classifications (for unclaimed-remainder computation)
    """
    det_mod = load_module(DETECTOR_PATH, "pdf_detector")
    text = det_mod.extract_pdf_text(PDF_PATH)
    segments = text.split("\f")
    classifications = []
    for i, seg in enumerate(segments):
        c = det_mod.classify_segment(seg, is_first=(i == 0))
        c["segment_idx"] = i
        c["raw_preview"] = seg[:600]
        c["raw_len"] = len(seg)
        classifications.append(c)

    # Assemble articles via the detector's existing pass-2 logic.
    # NOTE signature: assemble_articles(segments, classifications) — segments FIRST.
    # Returned dict keys: article_seq, headline, publication_hint, date_hint,
    #   page_range [start_seg+1, end_seg+1], body_text, is_multi_page,
    #   classification_confidence.
    # We reconstruct spans_segments from page_range so callers downstream get
    # the contiguous segment-index list.
    articles_raw = det_mod.assemble_articles(segments, classifications)
    for a in articles_raw:
        pr = a.get("page_range") or [None, None]
        if pr[0] is not None and pr[1] is not None:
            a["spans_segments"] = list(range(pr[0] - 1, pr[1]))
        else:
            a["spans_segments"] = []
        a["segment_idx"] = (pr[0] - 1) if pr[0] is not None else None
    return articles_raw, classifications, segments


def load_csv_articles():
    """Load CSV unique articles with full row dicts (we need row_ids for routing)."""
    rows = []
    with open(CSV_PATH) as f:
        for r in csv.DictReader(f):
            rows.append(r)
    return rows


def build_csv_unique_articles(rows):
    """Group CSV rows by (publication, date, normalized-headline). Return list of
    article dicts with their constituent row_ids."""
    by_key = {}
    for r in rows:
        h = r.get("headline", "").strip()
        if not h: continue
        pub = r.get("publication", "").strip()
        date = r.get("date", "").strip()
        nh = normalize_text(h)
        key = (pub, date, nh)
        if key not in by_key:
            by_key[key] = {
                "publication": pub,
                "date": date,
                "headline": h,
                "headline_norm": nh,
                "row_ids": [],
            }
        by_key[key]["row_ids"].append(r.get("row_id", ""))
    return list(by_key.values())


def main(commit: bool = False):
    print(f"[union_article_corpus_v1] {datetime.now(timezone.utc).isoformat()}")
    print(f"Mode: {'COMMIT' if commit else 'DRY-RUN'}")
    print()

    # ---------- Step 1: RTF articles ----------
    print("→ extracting RTF articles...")
    rtf_articles = build_rtf_articles()
    print(f"  RTF articles: {len(rtf_articles)}")

    # ---------- Step 2: PDF articles + classifications ----------
    print("→ detecting PDF articles...")
    pdf_articles_raw, pdf_classifications, pdf_segments = build_pdf_articles_and_classifications()
    print(f"  PDF segments: {len(pdf_segments)}")
    print(f"  PDF detected articles (raw): {len(pdf_articles_raw)}")

    # ---------- Step 3: Load CSV unique articles ----------
    rows = load_csv_articles()
    csv_articles = build_csv_unique_articles(rows)
    print(f"  CSV unique articles: {len(csv_articles)}")
    csv_norm_set = {a["headline_norm"] for a in csv_articles}

    # ---------- Step 4: Validate PDF articles against CSV (Pipeline 1 admission) ----------
    # Only PDF-detected articles whose normalized headline EXACTLY matches a CSV
    # unique article are admitted to the corpus. This avoids the wrong-headline-
    # detected garbage we saw in D6 (e.g. "Top of Form", mid-sentence Kastner quotes).
    pdf_admitted = []
    pdf_admitted_csv_norms = set()  # which CSV norms got served by PDF
    claimed_segment_ids = set()
    for a in pdf_articles_raw:
        nh = normalize_text(a.get("headline") or "")
        if not nh:
            continue
        if nh in csv_norm_set:
            body_text = a.get("body_text") or ""
            pdf_admitted.append({
                "source": "pdf",
                "source_idx": a.get("segment_idx"),
                "headline": a.get("headline"),
                "headline_norm": nh,
                "date": a.get("date_hint"),
                "page_no": None,
                "author_hint": a.get("publication_hint"),
                "metadata_line": None,
                "body": body_text,
                "body_chars": len(body_text),
                "spans_segments": a.get("spans_segments", []),
                "classification_confidence": a.get("classification_confidence"),
            })
            pdf_admitted_csv_norms.add(nh)
            for s in a.get("spans_segments", []):
                if s is not None:
                    claimed_segment_ids.add(s)
    print(f"  PDF articles admitted (headline matches CSV): {len(pdf_admitted)}")

    # ---------- Step 5: Build union corpus (dedup by headline_norm; RTF wins ties) ----------
    union = {}
    for a in rtf_articles:
        if a["headline_norm"] in csv_norm_set:
            union[a["headline_norm"]] = a
    rtf_admitted_count = len(union)
    for a in pdf_admitted:
        if a["headline_norm"] not in union:
            union[a["headline_norm"]] = a
    union_articles = list(union.values())
    print(f"  RTF admitted to corpus: {rtf_admitted_count}")
    print(f"  PDF admitted to corpus (new, not dup of RTF): {len(union_articles) - rtf_admitted_count}")
    print(f"  → TOTAL article_corpus_v1: {len(union_articles)}")

    # ---------- Step 6: Build unclaimed PDF segments ----------
    unclaimed_segments = [
        {
            "segment_idx": c["segment_idx"],
            "classification": c["classification"],
            "headline_attempted": c.get("headline"),
            "reason": c.get("reason"),
            "raw_len": c["raw_len"],
            "raw_preview": c["raw_preview"],
        }
        for c in pdf_classifications
        if c["segment_idx"] not in claimed_segment_ids
    ]
    print(f"  unclaimed PDF segments: {len(unclaimed_segments)} / {len(pdf_classifications)}")

    # ---------- Step 7: Build Pipeline 2 routing CSV ----------
    # For every CSV row: is its (pub, date, norm-headline) headline_norm in the
    # article_corpus union? If yes → Pipeline 1. If no → Pipeline 2, with a reason
    # derived from D6's bucket logic.
    served_norms = {a["headline_norm"] for a in union_articles}
    quote_only_rows = []
    pipeline1_rows = 0

    # Build helper: which CSV articles ARE in PDF but with wrong headline / cont / unk?
    # We need to re-run D6's probe logic here to assign reasons. Simpler: rely on
    # whether the headline's first-6-words appear in any PDF segment.
    seg_norms = [normalize_text(s) for s in pdf_segments]

    for r in rows:
        h = r.get("headline", "").strip()
        if not h:
            # No headline → quote-only by definition
            quote_only_rows.append({**r, "pipeline_route_reason": "no_headline"})
            continue
        nh = normalize_text(h)
        if nh in served_norms:
            pipeline1_rows += 1
            continue
        # Pipeline 2 — determine reason
        words = h.split()
        probe = " ".join(words[:6])
        pn = normalize_text(probe)
        if len(pn) < 15:
            reason = "headline_too_short_to_probe"
        elif not any(pn in s for s in seg_norms):
            reason = "not_in_pdf"
        else:
            reason = "pdf_format_mismatch"
        quote_only_rows.append({**r, "pipeline_route_reason": reason})

    print(f"  Pipeline 1 rows: {pipeline1_rows}")
    print(f"  Pipeline 2 rows: {len(quote_only_rows)}")
    route_counter = Counter(r["pipeline_route_reason"] for r in quote_only_rows)
    print(f"  Pipeline 2 reasons: {dict(route_counter)}")
    print()

    # ---------- Sanity ----------
    assert pipeline1_rows + len(quote_only_rows) == len(rows), \
        f"row partition lost rows: {pipeline1_rows} + {len(quote_only_rows)} != {len(rows)}"

    # ---------- Step 8: Write ----------
    if not commit:
        print("→ DRY-RUN — no files written. Pass --commit to write.")
        return

    if not QUOTATIONS_DIR.exists():
        sys.exit(f"FATAL: missing output dir {QUOTATIONS_DIR}")

    # 8a: article_corpus_v1.json
    corpus = {
        "schema_version": "v1",
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "source_pdf": str(PDF_PATH),
        "source_rtf": str(RTF_PATH),
        "source_csv": str(CSV_PATH),
        "article_count": len(union_articles),
        "rtf_admitted": rtf_admitted_count,
        "pdf_admitted_new": len(union_articles) - rtf_admitted_count,
        "articles": union_articles,
    }
    CORPUS_OUT.write_text(json.dumps(corpus, indent=2, default=str))
    print(f"→ WROTE: {CORPUS_OUT}  ({CORPUS_OUT.stat().st_size:,} bytes)")

    # 8b: _pdf_segments_unclaimed_v1.json
    unclaimed = {
        "schema_version": "v1",
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "source_pdf": str(PDF_PATH),
        "total_segments": len(pdf_classifications),
        "claimed_segment_count": len(claimed_segment_ids),
        "unclaimed_segment_count": len(unclaimed_segments),
        "segments": unclaimed_segments,
    }
    UNCLAIMED_OUT.write_text(json.dumps(unclaimed, indent=2, default=str))
    print(f"→ WROTE: {UNCLAIMED_OUT}  ({UNCLAIMED_OUT.stat().st_size:,} bytes)")

    # 8c: quote_only_rows_v1.csv
    if quote_only_rows:
        fieldnames = list(rows[0].keys()) + ["pipeline_route_reason"]
        with open(QUOTE_ONLY_OUT, "w", newline="") as f:
            w = csv.DictWriter(f, fieldnames=fieldnames, quoting=csv.QUOTE_ALL)
            w.writeheader()
            for r in quote_only_rows:
                w.writerow(r)
        print(f"→ WROTE: {QUOTE_ONLY_OUT}  ({QUOTE_ONLY_OUT.stat().st_size:,} bytes)")


if __name__ == "__main__":
    main(commit=("--commit" in sys.argv))
