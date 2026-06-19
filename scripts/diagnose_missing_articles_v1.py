#!/usr/bin/env python3
"""
diagnose_missing_articles_v1.py

Quick D5 diagnostic: take the unmatched CSV headlines from detector v2 and find
where they actually appear in the raw PDF text — so we can see what page header
/ metadata format we're missing in the classifier.

Reads:
  - /Users/scott/Desktop/Archive/Kastner_Consolidated_Quotes.pdf
  - /Users/scott/Desktop/Archive/aberdeen-group-archive/kastner-author/quotations/kastner_quotes_clean.csv

Writes nothing. Dumps diagnostics to stdout.
"""
import csv, re, subprocess, sys, unicodedata
from pathlib import Path
from collections import Counter

PDF_PATH = Path("/Users/scott/Desktop/Archive/Kastner_Consolidated_Quotes.pdf")
CSV_PATH = Path("/Users/scott/Desktop/Archive/aberdeen-group-archive/kastner-author/quotations/kastner_quotes_clean.csv")


def normalize_text(s: str) -> str:
    s = unicodedata.normalize("NFKD", s)
    s = s.replace("\u2019", "'").replace("\u2018", "'")
    s = s.replace("\u201c", '"').replace("\u201d", '"')
    s = s.replace("\u2014", "-").replace("\u2013", "-")
    s = re.sub(r"\s+", " ", s)
    s = s.strip().lower().strip("'\"").rstrip(";,.:")
    return s.strip()


def extract():
    r = subprocess.run(
        ["pdftotext", "-layout", str(PDF_PATH), "-"],
        capture_output=True, text=True, check=True,
    )
    return r.stdout


def main():
    text = extract()
    segments = text.split("\f")
    print(f"segments: {len(segments)}")

    # Load all unique CSV headlines
    csv_heads = []
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
                csv_heads.append((pub, date, h))
    print(f"unique csv articles: {len(csv_heads)}")

    # For each csv headline, find which segment(s) contain it (normalized substring)
    seg_norms = [normalize_text(s) for s in segments]
    seg_first200 = [s[:400] for s in segments]

    found_in_seg = 0
    not_in_pdf = 0
    publication_format_samples = Counter()  # what does the "metadata line" look like for unmatched articles?
    sample_dump = []  # full segment header for first N missing

    for pub, date, headline in csv_heads:
        # Try a partial-prefix search to be tolerant
        # Take first 6 words of headline for the probe
        words = headline.split()
        probe = " ".join(words[:6]).lower()
        probe_norm = normalize_text(probe)
        if len(probe_norm) < 15:  # too short to be reliable
            continue
        hits = [i for i, s in enumerate(seg_norms) if probe_norm in s]
        if hits:
            found_in_seg += 1
            # For samples NOT among the detector's 432 HEADs, dump the segment's first 400 chars
            # so we see the publication's page-header format
            if len(sample_dump) < 25:
                seg_idx = hits[0]
                # Find the line containing the probe
                seg_text = segments[seg_idx]
                lines = seg_text.split("\n")
                # First 12 lines = page header area
                head_block = "\n".join(lines[:12])
                sample_dump.append({
                    "pub": pub,
                    "date": date,
                    "headline": headline[:80],
                    "seg_idx": seg_idx,
                    "head_block": head_block,
                })
        else:
            not_in_pdf += 1

    print(f"\nfound in PDF (by probe): {found_in_seg}")
    print(f"NOT in PDF (probe-miss): {not_in_pdf}")
    print(f"\n=== Sample segment-headers for CSV articles (first 25) ===\n")
    for s in sample_dump:
        print(f"--- [{s['pub']}] {s['date']}  {s['headline']!r}  (seg {s['seg_idx']}) ---")
        print(s["head_block"])
        print()


if __name__ == "__main__":
    main()
