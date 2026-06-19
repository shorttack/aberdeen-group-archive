#!/usr/bin/env python3
"""
diagnose_detection_gap_v1.py  (D6)

Goal: explain the 326-article gap between detector v2's 432 detected HEADs and
the 106 matched-to-CSV. We need to know:

  (A) How many of the 432 detected HEADs have a headline that matches NO CSV
      article? (wrong-headline-on-real-article OR junk detection)

  (B) For each CSV article that's in the PDF (per D5 probe), what segment
      contains it AND was that segment classified as HEAD, CONTINUATION, or
      UNKNOWN by detector v2? This isolates:
        - "detected as HEAD but wrong headline extracted" (fixable: headline-
           extraction bug)
        - "detected as CONTINUATION" (fixable: classifier-bug — body looked
           like continuation but is actually a new article)
        - "detected as UNKNOWN" (fixable: extend classifier signals)
        - "no segment contains this article" (the D5 168 probe-miss bucket;
           unfixable from PDF)

Imports detector v2 directly to get the exact classification + extracted
headline for every segment.

Writes:
  - /tmp/d6_detection_gap.txt (human-readable diagnostic)
"""
import csv, re, sys, unicodedata, importlib.util
from pathlib import Path

# Import detector v2 from the scripts dir
DETECTOR = Path("/Users/scott/Desktop/Archive/scripts/detect_article_boundaries_v2.py")
spec = importlib.util.spec_from_file_location("detect_v2", DETECTOR)
detect_v2 = importlib.util.module_from_spec(spec)
spec.loader.exec_module(detect_v2)

PDF_PATH = Path("/Users/scott/Desktop/Archive/Kastner_Consolidated_Quotes.pdf")
CSV_PATH = Path("/Users/scott/Desktop/Archive/aberdeen-group-archive/kastner-author/quotations/kastner_quotes_clean.csv")


def main():
    # Run detector pipeline to get classified segments
    text = detect_v2.extract_pdf_text(PDF_PATH)
    raw_segments = text.split("\f")
    classified = []
    for i, seg in enumerate(raw_segments):
        c = detect_v2.classify_segment(seg, is_first=(i == 0))
        classified.append(c)

    n_head = sum(1 for c in classified if c["classification"] == "ARTICLE_HEAD")
    n_cont = sum(1 for c in classified if c["classification"] == "ARTICLE_CONTINUATION")
    n_unk = sum(1 for c in classified if c["classification"] == "UNKNOWN")
    n_empty = sum(1 for c in classified if c["classification"] == "EMPTY")
    print(f"classified: HEAD={n_head} CONT={n_cont} UNK={n_unk} EMPTY={n_empty}")

    # Load CSV unique articles
    csv_articles = []
    seen = set()
    with open(CSV_PATH) as f:
        r = csv.DictReader(f)
        for row in r:
            h = row.get("headline", "").strip()
            pub = row.get("publication", "").strip()
            date = row.get("date", "").strip()
            key = (pub, date, h)
            if h and key not in seen:
                seen.add(key)
                csv_articles.append((pub, date, h))

    print(f"unique csv articles: {len(csv_articles)}")

    # For each CSV article, find which segment(s) contain it (probe by first-6-words),
    # and report what the classifier said about that segment.
    seg_norms = [detect_v2.normalize_text(s) for s in raw_segments]

    bucket_counts = {"HEAD_correct": 0, "HEAD_wrong_headline": 0,
                     "CONTINUATION": 0, "UNKNOWN": 0, "EMPTY": 0,
                     "NOT_IN_PDF": 0}
    wrong_headline_samples = []
    cont_samples = []
    unk_samples = []
    notinpdf_samples = []

    for pub, date, headline in csv_articles:
        words = headline.split()
        probe = " ".join(words[:6]).lower()
        probe_norm = detect_v2.normalize_text(probe)
        if len(probe_norm) < 15:
            continue
        hits = [i for i, s in enumerate(seg_norms) if probe_norm in s]
        if not hits:
            bucket_counts["NOT_IN_PDF"] += 1
            if len(notinpdf_samples) < 5:
                notinpdf_samples.append((pub, date, headline))
            continue
        seg_idx = hits[0]
        cls = classified[seg_idx]["classification"]
        detected_headline = classified[seg_idx].get("headline") or ""
        csv_norm = detect_v2.normalize_text(headline)
        det_norm = detect_v2.normalize_text(detected_headline)
        if cls == "ARTICLE_HEAD":
            if csv_norm == det_norm or csv_norm[:50] == det_norm[:50]:
                bucket_counts["HEAD_correct"] += 1
            else:
                bucket_counts["HEAD_wrong_headline"] += 1
                if len(wrong_headline_samples) < 10:
                    wrong_headline_samples.append({
                        "seg": seg_idx,
                        "csv": headline,
                        "detected": detected_headline,
                        "pub": pub, "date": date,
                    })
        elif cls == "ARTICLE_CONTINUATION":
            bucket_counts["CONTINUATION"] += 1
            if len(cont_samples) < 10:
                cont_samples.append({
                    "seg": seg_idx,
                    "csv": headline,
                    "reason": classified[seg_idx].get("reason", ""),
                    "first200": raw_segments[seg_idx][:300],
                    "pub": pub, "date": date,
                })
        elif cls == "UNKNOWN":
            bucket_counts["UNKNOWN"] += 1
            if len(unk_samples) < 10:
                unk_samples.append({
                    "seg": seg_idx,
                    "csv": headline,
                    "first200": raw_segments[seg_idx][:300],
                    "pub": pub, "date": date,
                })
        elif cls == "EMPTY":
            bucket_counts["EMPTY"] += 1

    print(f"\n=== Bucket counts (CSV article fate) ===")
    for k, v in bucket_counts.items():
        print(f"  {k:25s}: {v}")
    total = sum(bucket_counts.values())
    print(f"  {'TOTAL':25s}: {total}")

    if wrong_headline_samples:
        print(f"\n=== HEAD-detected but WRONG-HEADLINE-extracted (10 samples) ===")
        for s in wrong_headline_samples:
            print(f"  seg {s['seg']}  [{s['pub']}] {s['date']}")
            print(f"    csv:      {s['csv'][:100]!r}")
            print(f"    detected: {s['detected'][:100]!r}")

    if cont_samples:
        print(f"\n=== CSV article classified as CONTINUATION (10 samples) ===")
        for s in cont_samples:
            print(f"  seg {s['seg']}  [{s['pub']}] {s['date']}  csv={s['csv'][:60]!r}")
            print(f"    reason: {s['reason']}")
            print(f"    first200: {s['first200'][:250]!r}")

    if unk_samples:
        print(f"\n=== CSV article classified as UNKNOWN (10 samples) ===")
        for s in unk_samples:
            print(f"  seg {s['seg']}  [{s['pub']}] {s['date']}  csv={s['csv'][:60]!r}")
            print(f"    first200: {s['first200'][:250]!r}")

    if notinpdf_samples:
        print(f"\n=== Truly missing from PDF (5 samples) ===")
        for pub, date, h in notinpdf_samples:
            print(f"  [{pub}] {date}  {h[:80]!r}")


if __name__ == "__main__":
    main()
