#!/usr/bin/env python3
"""
scan_media_quotations_first_10_v1.py

Read 'Peter S Kastner Media Quotations.md', extract the first 10 press
articles, and check each against:
  - kastner_quotes_clean.csv      (1208 rows, dedupe on date + headline_norm)
  - article_corpus_v1.json        (179 articles, headline_norm match)

Heuristics for article boundary detection in this .md:
  - Articles separated by blank-line stretches
  - Headlines appear as either:
      (a) ALL-CAPS lines >= 8 chars
      (b) **Bold** markdown lines with title-case text
  - Source/date line follows headline, e.g. "NewsFactor Network, 4 December 2002"
  - First 10 = first 10 candidate headlines walking top-to-bottom

This script does NOT modify any file. It prints a table:
  # | headline | inferred_date | match_in_csv | match_in_corpus | net_new?
"""
from __future__ import annotations
import csv, json, re, sys, unicodedata
from pathlib import Path
from datetime import datetime

QUOTATIONS = Path.home() / "Desktop/Archive/aberdeen-group-archive/kastner-author/quotations"
MD_PATH    = QUOTATIONS / "Peter S Kastner Media Quotations.md"
CSV_PATH   = QUOTATIONS / "kastner_quotes_clean.csv"
CORPUS_JSON = QUOTATIONS / "article_corpus_v1.json"

N_ARTICLES = 10

# ---------------------------------------------------- normalize_text ----
# Must match union_article_corpus_v1.py normalization
def normalize_text(s: str) -> str:
    if not s:
        return ""
    s = unicodedata.normalize("NFKD", s)
    s = "".join(c for c in s if not unicodedata.combining(c))
    s = s.lower()
    s = re.sub(r"[^a-z0-9 ]+", " ", s)
    s = re.sub(r"\s+", " ", s).strip()
    return s

# ---------------------------------------------------- date parsing ------
MONTHS = {m.lower(): i for i, m in enumerate(
    ["January","February","March","April","May","June","July","August",
     "September","October","November","December"], start=1)}
MONTHS_ABBR = {m.lower(): i for i, m in enumerate(
    ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"], start=1)}
MONTHS.update(MONTHS_ABBR)

def parse_date_loose(line: str) -> str | None:
    """Try to find a date inside `line`. Returns ISO YYYY-MM-DD or None."""
    if not line:
        return None
    # Pattern 1: '4 December 2002', '12 February 2004'
    m = re.search(r"\b(\d{1,2})\s+([A-Za-z]+)\s+(\d{4})\b", line)
    if m:
        d, mon, y = int(m.group(1)), m.group(2).lower(), int(m.group(3))
        if mon in MONTHS:
            return f"{y:04d}-{MONTHS[mon]:02d}-{d:02d}"
    # Pattern 2: 'February 12, 2004', 'June 14, 2004'
    m = re.search(r"\b([A-Za-z]+)\s+(\d{1,2}),\s+(\d{4})\b", line)
    if m:
        mon, d, y = m.group(1).lower(), int(m.group(2)), int(m.group(3))
        if mon in MONTHS:
            return f"{y:04d}-{MONTHS[mon]:02d}-{d:02d}"
    # Pattern 3: 'Tue, Jun 16, 2009'
    m = re.search(r"\b([A-Za-z]{3,9}),?\s+([A-Za-z]{3})\s+(\d{1,2}),\s+(\d{4})\b", line)
    if m:
        mon, d, y = m.group(2).lower(), int(m.group(3)), int(m.group(4))
        if mon in MONTHS:
            return f"{y:04d}-{MONTHS[mon]:02d}-{d:02d}"
    return None

# ---------------------------------------------------- headline detection
def looks_like_headline(line: str) -> str | None:
    """Return the headline text if `line` looks like one, else None."""
    s = line.strip()
    if not s:
        return None
    if len(s) < 8 or len(s) > 250:
        return None

    # ALL-CAPS heuristic: at least 3 words, mostly uppercase letters
    letters = [c for c in s if c.isalpha()]
    if letters:
        upper_ratio = sum(1 for c in letters if c.isupper()) / len(letters)
        if upper_ratio >= 0.85 and len(s.split()) >= 3:
            return s

    # Bold markdown: **headline** (entire line is bold)
    m = re.match(r"^\*\*(.+?)\*\*$", s)
    if m:
        candidate = m.group(1).strip()
        # Must look like a title (has letters, has spaces, no markdown chars)
        if len(candidate.split()) >= 3 and not candidate.startswith(("From:", "Date:", "By ")):
            return candidate

    return None

# ---------------------------------------------------- main --------------
def main() -> int:
    if not MD_PATH.exists():
        print(f"ERROR: not found: {MD_PATH}", file=sys.stderr); return 1
    text = MD_PATH.read_text(encoding="utf-8", errors="replace")
    lines = text.split("\n")
    print(f"read: {MD_PATH.name} ({len(text):,} chars, {len(lines):,} lines)\n")

    # Walk lines top-to-bottom, collect first N headline candidates.
    # For each, look at next 5 non-blank lines for a date.
    articles = []
    i = 0
    while i < len(lines) and len(articles) < N_ARTICLES:
        h = looks_like_headline(lines[i])
        if h:
            # Look ahead for date in next 8 lines
            date_iso = None
            for j in range(i+1, min(i+8, len(lines))):
                d = parse_date_loose(lines[j])
                if d:
                    date_iso = d
                    break
            articles.append({
                "line_no": i + 1,
                "headline_raw": h,
                "headline_norm": normalize_text(h),
                "date": date_iso,
            })
        i += 1

    print(f"detected {len(articles)} headline candidates in first walk\n")

    # ---- load CSV master ----
    csv_by_norm = {}  # headline_norm -> list of (row_id, date, headline)
    with open(CSV_PATH, newline="") as f:
        for r in csv.DictReader(f):
            hn = normalize_text(r.get("headline",""))
            if hn:
                csv_by_norm.setdefault(hn, []).append(
                    (r.get("row_id",""), r.get("date",""), r.get("headline",""))
                )
    print(f"csv: {sum(len(v) for v in csv_by_norm.values())} rows, "
          f"{len(csv_by_norm)} distinct headline_norms\n")

    # ---- load corpus ----
    with open(CORPUS_JSON) as f:
        corpus = json.load(f)
    corpus_norms = {a.get("headline_norm","") for a in corpus.get("articles", [])}
    print(f"corpus: {len(corpus.get('articles', []))} articles, "
          f"{len(corpus_norms)} distinct headline_norms\n")

    # ---- compare ----
    print("=" * 110)
    print(f"{'#':>2} | {'date':<10} | {'in_csv':<6} | {'in_corpus':<9} | NET-NEW? | headline")
    print("-" * 110)
    for idx, a in enumerate(articles, 1):
        in_csv = a["headline_norm"] in csv_by_norm
        in_corpus = a["headline_norm"] in corpus_norms
        net_new = not (in_csv or in_corpus)
        flag = "YES *NEW*" if net_new else "no"
        date = a["date"] or "(no date)"
        print(f"{idx:>2} | {date:<10} | {str(in_csv):<6} | {str(in_corpus):<9} | "
              f"{flag:<8} | {a['headline_raw'][:75]}")

    print("=" * 110)
    print()

    # ---- detail for any CSV match ----
    for idx, a in enumerate(articles, 1):
        if a["headline_norm"] in csv_by_norm:
            print(f"# {idx} matches in CSV ({len(csv_by_norm[a['headline_norm']])} row(s)):")
            for row_id, d, h in csv_by_norm[a["headline_norm"]][:3]:
                print(f"    row_id={row_id}  date={d!r}  headline={h!r}")
            print()

    # ---- summary ----
    net_new_count = sum(
        1 for a in articles
        if a["headline_norm"] not in csv_by_norm and a["headline_norm"] not in corpus_norms
    )
    print(f"SUMMARY: {len(articles)} articles checked; "
          f"{net_new_count} net-new to corpus+csv")

    return 0

if __name__ == "__main__":
    sys.exit(main())
