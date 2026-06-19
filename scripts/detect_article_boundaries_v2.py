#!/usr/bin/env python3
"""
detect_article_boundaries_v2.py
================================
v1.8.0 quotations corpus — article boundary detector for Kastner_Consolidated_Quotes.pdf.

PURPOSE
-------
The PDF is a Microsoft Word export (1.94 MB extracted, 546 pages, 544 non-empty form-feed
segments). Pete's hint: "most press article stories end with a page break". D1 diagnosis
confirmed: form-feed delimits PAGES, not articles. Articles START at a page boundary and
may span multiple pages. Need to detect article-start vs continuation-page segments.

GOAL
----
Map every form-feed-delimited segment to either:
  (a) ARTICLE_HEAD — first page of an article (headline + byline + page+date pattern at top)
  (b) ARTICLE_CONTINUATION — continuation page of the article that started earlier
  (c) UNKNOWN — couldn't classify (flagged for manual review)

OUTPUT
------
DRY-RUN (default) prints diagnostics:
  - Total segments classified per category
  - Sample of 5 ARTICLE_HEAD segments (headline + first 80 chars body)
  - Sample of 5 ARTICLE_CONTINUATION segments (first 80 chars)
  - Sample of 5 UNKNOWN segments (full text, ≤200 chars)
  - Histogram of headline lengths
  - Detected article count vs CSV unique-article count (567) — closer = better detector

--commit writes JSON index:
  ~/Desktop/Archive/aberdeen-group-archive/kastner-author/quotations/_article_index.json
  Schema: {"articles": [{"article_seq": int, "headline": str, "publication_hint": str,
                          "date_hint": str, "page_range": [int,int],
                          "char_offset_start": int, "char_offset_end": int,
                          "body_text": str, "is_multi_page": bool}, ...]}

PATTERNS (from D1 segment heads)
--------------------------------
Segment [0]: "Kastner Aberdeen Quotes Consolidated / / Unix draws a crowd; / SOFTWARE & SERVICES;
              Analysis Savage, J.A. Page: 33 03/19/90 / Suddenly, Unix-based fault-tolerant..."

Segment [1]: "All of the fault-tolerant vendors have had to toy with the Unix kernel..."
              (no headline; mid-sentence body — clearly a continuation)

Segment [2]: "Mini vendors adapt in order to survive / SOFTWARE & SERVICES; Analysis Daly,
              James Page: 27 03/13/89 / [separator rule] / One of the o..."

PATTERN OBSERVATIONS:
  1. Article-head segments contain a "Page: NN MM/DD/YY" metadata line near the top.
     This is the strongest signal for ARTICLE_HEAD classification.
  2. The headline is the line immediately preceding the section/byline/page+date metadata.
     Often ends with semicolon or no punctuation. 20-120 chars typical.
  3. The first segment has a banner "Kastner Aberdeen Quotes Consolidated" prefix —
     a one-off, not a per-article pattern. Strip before detection.
  4. Section markers like "SOFTWARE & SERVICES; Analysis" appear after the headline.
     Multiple subjects: SOFTWARE, HARDWARE, NETWORKING, INDUSTRY TRENDS, etc.
  5. Some articles use separator rules ("──────────...") between metadata and body.
  6. Page break form-feeds (\\x0c) come BETWEEN segments. Within a segment, line breaks
     are \\n. Multi-page articles have their pages as separate segments concatenated
     by the form-feed split.

DETECTOR ALGORITHM (v1)
-----------------------
For each segment:
  1. Strip leading banner if present (segment 0 only)
  2. Look in the first ~600 chars for the "Page: NN MM/DD/YY" pattern
     Regex: r'Page:\\s*\\d+\\s+\\d{1,2}/\\d{1,2}/\\d{2,4}'
  3. If found → ARTICLE_HEAD
     - Headline = first non-empty line above the "Page:" line that isn't a section marker
       (section markers: "SOFTWARE & SERVICES", "HARDWARE", "NETWORKING",
                         "INDUSTRY TRENDS", "Analysis", etc.)
     - Extract date and page_number from the "Page:" line
  4. If not found → check for headline-like-line-followed-by-body pattern
     - First non-empty line is 20-150 chars, doesn't start with lowercase, doesn't end
       with period
     - Followed within 5 lines by sustained prose
     - This handles articles without the Aberdeen "Page: NN ..." metadata (e.g., blog posts)
  5. If neither pattern → ARTICLE_CONTINUATION (presumed continuation of prior segment)
     - Mid-sentence start (first line begins with lowercase letter)
     - No headline-like structure in top 5 lines
  6. If still ambiguous → UNKNOWN

PASSES
------
Pass 1: Classify every segment HEAD vs CONTINUATION vs UNKNOWN
Pass 2: Walk classified segments in order, merging continuations into their parent HEAD
Pass 3: Match resulting articles against CSV's unique (headline, publication, date) triples
         to compute match rate. Target: ≥85% match rate validates the detector.

USAGE
-----
Mac:
  cd ~/Desktop/Archive
  python3 ~/Desktop/Archive/scripts/detect_article_boundaries_v2.py
  # → DRY-RUN diagnostics printed to stdout
  python3 ~/Desktop/Archive/scripts/detect_article_boundaries_v2.py --commit
  # → writes _article_index.json

VERSIONING
----------
v1.0 — first draft, written blind from D1 segment-head sample.
        Will need iteration based on Pete's first dry-run diagnostic output.
"""

from __future__ import annotations

import csv
import json
import re
import subprocess
import sys
import unicodedata
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path

# ---------- paths ----------

HOME = Path.home()
PDF_PATH = HOME / "Desktop/Archive/Kastner_Consolidated_Quotes.pdf"
ARCHIVE_REPO = HOME / "Desktop/Archive/aberdeen-group-archive"
CSV_PATH = ARCHIVE_REPO / "kastner-author/quotations/kastner_quotes_clean.csv"
OUTPUT_PATH = ARCHIVE_REPO / "kastner-author/quotations/_article_index.json"
DIAG_PATH = ARCHIVE_REPO / "kastner-author/quotations/_article_index_diagnostics_v1.txt"

# ---------- constants ----------

BANNER_PREFIX_PATTERN = re.compile(
    r"^\s*Kastner Aberdeen Quotes Consolidated\s*\n?", re.IGNORECASE | re.MULTILINE
)

# "Page: 33 03/19/90" — must match the Aberdeen citation metadata line.
# Allow 1-3 digit page numbers, MM/DD/YY or MM/DD/YYYY dates.
PAGE_DATE_PATTERN = re.compile(
    r"Page:\s*(\d{1,4})\s+(\d{1,2}/\d{1,2}/\d{2,4})"
)

# Section markers seen on Computerworld articles (D1 sample). Will need expansion
# after the first dry-run reveals more publication-specific patterns.
SECTION_MARKERS = {
    "SOFTWARE & SERVICES",
    "HARDWARE",
    "NETWORKING",
    "INDUSTRY TRENDS",
    "ANALYSIS",
    "NEWS",
    "FEATURES",
    "OPINION",
    "VIEWPOINT",
    "REVIEWS",
    "MANAGEMENT",
    "STORAGE",
    "SECURITY",
    "MOBILE",
    "WEB",
    "WIRELESS",
    "ENTERPRISE",
    "COMPUTERS",
    "COMMUNICATIONS",
    "PCS & WORKSTATIONS",
}

# Heuristic: continuation-page first lines often start mid-sentence (lowercase),
# or with conjunctions/prepositions.
CONTINUATION_LOWERCASE_START = re.compile(r"^\s*[a-z]")
CONTINUATION_CONJ_START = re.compile(
    r"^\s*(and|but|or|yet|so|because|although|though|while|whereas|however|moreover|therefore|thus|hence|nevertheless|nonetheless|meanwhile|furthermore|additionally|consequently|in addition|on the other hand)\b",
    re.IGNORECASE,
)

# ---------- text normalization ----------


def normalize_text(s: str) -> str:
    """Match the normalization Pete and I used in D3 — Unicode + smart-quote folding +
    whitespace collapse + lowercase. Used for CSV-headline-to-PDF-article matching only;
    not used on the body text we keep for scoring.

    v2 (2026-06-19): also strip outer quote chars and trailing punctuation, since the PDF
    headline extraction routinely preserves trailing `;` `,` `.` `:` that the CSV does not.
    """
    s = unicodedata.normalize("NFKD", s)
    s = s.replace("\u2019", "'").replace("\u2018", "'")
    s = s.replace("\u201c", '"').replace("\u201d", '"')
    s = s.replace("\u2014", "-").replace("\u2013", "-")
    s = re.sub(r"\s+", " ", s)
    s = s.strip().lower()
    # Strip outer quote chars (CSV is inconsistent — some headlines wrapped in '...' or "...")
    s = s.strip("'\"")
    # Strip trailing punctuation that the PDF preserves and the CSV drops
    s = s.rstrip(";,.:")
    return s.strip()


def subtitle_prefix(s: str) -> str:
    """Return the headline portion before a subtitle separator.

    Many CSV headlines carry a section/subtitle suffix joined by `;` or ` - ` (e.g.
    `Can DEC find an opening on the desktop? PRODUCT SPOTLIGHT; The DEC market`).
    PDF-extracted headlines often only capture the main clause. This helper returns
    the pre-subtitle prefix so the matcher can fall back to it.
    """
    s = normalize_text(s)
    for sep in ["; ", " - "]:
        if sep in s:
            return s.split(sep, 1)[0].strip().rstrip(";,.:").strip()
    return s


# ---------- core logic ----------


def extract_pdf_text(pdf_path: Path) -> str:
    """Shell out to pdftotext -layout. Returns the full extracted text."""
    if not pdf_path.exists():
        sys.exit(f"FATAL: PDF not found at {pdf_path}")
    result = subprocess.run(
        ["pdftotext", "-layout", str(pdf_path), "-"],
        capture_output=True,
        check=True,
    )
    return result.stdout.decode("utf-8", errors="replace")


def split_into_page_segments(pdf_text: str) -> list[str]:
    """Split on form-feed (page boundary). Returns list of segments (including empty ones
    at original index, so segment[i] corresponds to PDF page i+1 minus any leading banner)."""
    return pdf_text.split("\f")


def classify_segment(segment: str, is_first: bool = False) -> dict:
    """Classify a single page segment.

    Returns dict:
      {
        'classification': 'ARTICLE_HEAD' | 'ARTICLE_CONTINUATION' | 'UNKNOWN',
        'headline': str or None,
        'publication_hint': str or None,
        'page_number': int or None,
        'date_string': str or None,
        'confidence': 'high' | 'medium' | 'low',
        'reason': str,  # human-readable classification reason
        'first_line': str,
        'top_chars': str,  # first 600 chars for diagnostic
      }
    """
    body = segment

    # Strip banner from segment 0 only
    if is_first:
        body = BANNER_PREFIX_PATTERN.sub("", body, count=1)

    body_stripped = body.strip()
    if not body_stripped:
        return {
            "classification": "EMPTY",
            "headline": None,
            "publication_hint": None,
            "page_number": None,
            "date_string": None,
            "confidence": "high",
            "reason": "empty segment",
            "first_line": "",
            "top_chars": "",
        }

    lines = [l for l in body_stripped.split("\n")]
    first_nonblank = next((l for l in lines if l.strip()), "")
    top_chars = body_stripped[:600]

    # --- Test 1: explicit Page+Date metadata anywhere in top 1500 chars ---
    pd_match = PAGE_DATE_PATTERN.search(body_stripped[:1500])
    if pd_match:
        page_no = int(pd_match.group(1))
        date_str = pd_match.group(2)
        # Headline detection: find the headline line BEFORE the Page+Date line
        # The metadata line typically reads: "<SECTION_MARKER> [byline] Page: N MM/DD/YY"
        # The headline is on a line before that.
        metadata_line_start = body_stripped.rfind("\n", 0, pd_match.start()) + 1
        metadata_line = body_stripped[metadata_line_start : pd_match.end()].strip()

        # Find the metadata line's index in `lines`
        metadata_line_idx = None
        for li, ln in enumerate(lines):
            if PAGE_DATE_PATTERN.search(ln):
                metadata_line_idx = li
                break

        # Headline = walk FORWARD from line 0 to find the first non-empty, non-section-marker
        # line that comes BEFORE the metadata line. Articles consistently put the headline
        # at the top, with metadata below (per D1 segment heads).
        headline = None
        if metadata_line_idx is not None:
            for li in range(metadata_line_idx):
                cand = lines[li].strip()
                if not cand:
                    continue
                if cand.upper() in SECTION_MARKERS:
                    continue
                if PAGE_DATE_PATTERN.search(cand):
                    continue
                if 10 <= len(cand) <= 250 and not cand[0].islower():
                    headline = cand
                    break

        # Fallback: headline is the first non-blank, non-section-marker line above metadata
        if not headline:
            for line in lines:
                cand = line.strip()
                if not cand:
                    continue
                if PAGE_DATE_PATTERN.search(cand):
                    break  # reached metadata, stop
                if cand.upper() in SECTION_MARKERS:
                    continue
                if 10 <= len(cand) <= 250 and not cand[0].islower():
                    headline = cand
                    break

        return {
            "classification": "ARTICLE_HEAD",
            "headline": headline,
            "publication_hint": metadata_line[: metadata_line.find("Page:")].strip()
            if "Page:" in metadata_line
            else None,
            "page_number": page_no,
            "date_string": date_str,
            "confidence": "high",
            "reason": f"matched Page+Date pattern: {metadata_line[:80]}",
            "first_line": first_nonblank[:150],
            "top_chars": top_chars,
        }

    # --- Test 2: headline-like first line + sustained prose below ---
    # Used for articles without Aberdeen metadata (e.g., Kastner Blog posts, web articles)
    fl = first_nonblank.strip()
    is_headline_shape = (
        10 <= len(fl) <= 200
        and not fl[0].islower()
        and not fl.endswith(".")
        and not CONTINUATION_LOWERCASE_START.match(fl)
    )

    # Count substantive body lines after the first non-blank
    body_line_count = sum(
        1 for l in lines if l.strip() and len(l.strip()) > 30
    )

    if is_headline_shape and body_line_count >= 3:
        return {
            "classification": "ARTICLE_HEAD",
            "headline": fl,
            "publication_hint": None,
            "page_number": None,
            "date_string": None,
            "confidence": "medium",
            "reason": "headline-shape first line + sustained prose (no Page+Date metadata)",
            "first_line": fl[:150],
            "top_chars": top_chars,
        }

    # --- Test 3: continuation-page signals ---
    # A continuation page has NO Page+Date metadata (already tested above) AND no
    # headline-shape first line (already tested above). Three remaining signals:
    #   (a) first line starts mid-sentence (lowercase or conjunction)
    #   (b) majority of body lines are indented (typical pdftotext -layout body prose)
    # IMPORTANT: indent check uses the UN-stripped `body` (preserves leading whitespace);
    # `lines` was derived from body_stripped (whitespace-stripped) so we must re-derive.
    raw_lines = body.split("\n")
    first_raw_line = next((l for l in raw_lines if l.strip()), "")
    nonblank_raw = [l for l in raw_lines if l.strip()]
    indent_ratio = sum(
        1 for l in nonblank_raw if l.startswith("  ") or l.startswith("\t")
    ) / max(1, len(nonblank_raw))

    if CONTINUATION_LOWERCASE_START.match(fl) or CONTINUATION_CONJ_START.match(fl):
        return {
            "classification": "ARTICLE_CONTINUATION",
            "headline": None,
            "publication_hint": None,
            "page_number": None,
            "date_string": None,
            "confidence": "high",
            "reason": f"first line starts mid-sentence: {fl[:60]!r}",
            "first_line": fl[:150],
            "top_chars": top_chars,
        }

    if indent_ratio >= 0.6 and first_raw_line.startswith(" "):
        return {
            "classification": "ARTICLE_CONTINUATION",
            "headline": None,
            "publication_hint": None,
            "page_number": None,
            "date_string": None,
            "confidence": "medium",
            "reason": f"first line indented + {100 * indent_ratio:.0f}% body lines indented — prose continuation",
            "first_line": fl[:150],
            "top_chars": top_chars,
        }

    # --- Test 4: catch-all UNKNOWN ---
    return {
        "classification": "UNKNOWN",
        "headline": None,
        "publication_hint": None,
        "page_number": None,
        "date_string": None,
        "confidence": "low",
        "reason": "no Page+Date metadata, no clear headline-shape, no continuation signal",
        "first_line": fl[:150],
        "top_chars": top_chars,
    }


def assemble_articles(segments: list[str], classifications: list[dict]) -> list[dict]:
    """Pass 2: merge ARTICLE_CONTINUATION segments into preceding ARTICLE_HEAD.
    Returns list of article records with body text + page range.
    UNKNOWN segments are merged into the prior ARTICLE_HEAD (best-guess heuristic;
    flagged in diagnostics)."""
    articles = []
    current_article = None
    current_segments_idx = []

    for i, (seg, cls) in enumerate(zip(segments, classifications)):
        if cls["classification"] == "EMPTY":
            continue
        if cls["classification"] == "ARTICLE_HEAD":
            # Close previous article
            if current_article is not None:
                current_article["body_text"] = "\f".join(
                    segments[idx] for idx in current_segments_idx
                )
                current_article["page_range"] = [
                    current_segments_idx[0] + 1,
                    current_segments_idx[-1] + 1,
                ]
                current_article["is_multi_page"] = len(current_segments_idx) > 1
                articles.append(current_article)
            # Start new
            current_article = {
                "article_seq": len(articles) + 1,
                "headline": cls["headline"],
                "publication_hint": cls["publication_hint"],
                "date_hint": cls["date_string"],
                "page_range": None,
                "body_text": None,
                "is_multi_page": False,
                "classification_confidence": cls["confidence"],
            }
            current_segments_idx = [i]
        elif cls["classification"] in ("ARTICLE_CONTINUATION", "UNKNOWN"):
            if current_article is None:
                # Continuation without preceding HEAD → orphan; create a stub article
                current_article = {
                    "article_seq": len(articles) + 1,
                    "headline": "[ORPHAN — no preceding ARTICLE_HEAD]",
                    "publication_hint": None,
                    "date_hint": None,
                    "page_range": None,
                    "body_text": None,
                    "is_multi_page": False,
                    "classification_confidence": "low",
                }
                current_segments_idx = [i]
            else:
                current_segments_idx.append(i)

    # Close final article
    if current_article is not None:
        current_article["body_text"] = "\f".join(
            segments[idx] for idx in current_segments_idx
        )
        current_article["page_range"] = [
            current_segments_idx[0] + 1,
            current_segments_idx[-1] + 1,
        ]
        current_article["is_multi_page"] = len(current_segments_idx) > 1
        articles.append(current_article)

    return articles


def match_articles_to_csv(
    articles: list[dict], csv_path: Path
) -> tuple[int, int, list[dict]]:
    """Pass 3: for each CSV (publication, date, headline) triple, check whether a matching
    article exists in the detected article set.

    Returns (matched_count, total_unique_csv_articles, unmatched_csv_articles)."""
    if not csv_path.exists():
        return (0, 0, [])

    with open(csv_path) as f:
        rows = list(csv.DictReader(f))

    # Build unique CSV article set
    csv_articles = {}
    for r in rows:
        key = (
            r["publication"].strip(),
            r["date"].strip(),
            r["headline"].strip(),
        )
        csv_articles.setdefault(key, []).append(r["row_id"])

    # Build searchable detected-article corpus with 3-tier index:
    #   (1) exact normalized headline
    #   (2) subtitle prefix (portion before `; ` or ` - `)
    #   (3) first-50-char prefix of normalized headline (partial-prefix fallback)
    detected_set = set()
    detected_subtitle_set = set()
    detected_prefix50_set = set()
    for a in articles:
        h = a["headline"] or ""
        n = normalize_text(h)
        if not n:
            continue
        detected_set.add(n)
        sp = subtitle_prefix(h)
        if sp:
            detected_subtitle_set.add(sp)
        if len(n) >= 50:
            detected_prefix50_set.add(n[:50])

    matched = 0
    match_tier_counts = {"exact": 0, "subtitle": 0, "prefix50": 0}
    unmatched = []
    for (pub, date, headline), row_ids in csv_articles.items():
        if not headline:
            continue
        norm = normalize_text(headline)
        # Tier 1: exact normalized match
        if norm in detected_set:
            matched += 1
            match_tier_counts["exact"] += 1
            continue
        # Tier 2: subtitle prefix match (csv has subtitle, detector got main clause)
        csv_sub = subtitle_prefix(headline)
        if csv_sub and (csv_sub in detected_set or csv_sub in detected_subtitle_set):
            matched += 1
            match_tier_counts["subtitle"] += 1
            continue
        # Tier 3: 50-char prefix match (catches small wording variance / truncation)
        if len(norm) >= 50 and norm[:50] in detected_prefix50_set:
            matched += 1
            match_tier_counts["prefix50"] += 1
            continue
        # Also try the csv subtitle's prefix50 if applicable
        if csv_sub and len(csv_sub) >= 50 and csv_sub[:50] in detected_prefix50_set:
            matched += 1
            match_tier_counts["prefix50"] += 1
            continue
        unmatched.append(
            {
                "publication": pub,
                "date": date,
                "headline": headline,
                "row_ids": row_ids,
            }
        )

    return (matched, len(csv_articles), unmatched, match_tier_counts)


# ---------- driver ----------


def run(commit: bool = False) -> None:
    print(f"[detect_article_boundaries_v2] {datetime.now(timezone.utc).isoformat()}")
    print(f"Mode: {'COMMIT' if commit else 'DRY-RUN (use --commit to write index)'}")
    print(f"PDF: {PDF_PATH}")
    print(f"CSV: {CSV_PATH}")
    print()

    # ---------- Extract + split ----------
    print("→ extracting PDF text...")
    pdf_text = extract_pdf_text(PDF_PATH)
    print(f"  raw chars: {len(pdf_text):,}")

    segments = split_into_page_segments(pdf_text)
    print(f"  form-feed-delimited segments: {len(segments)}")
    print()

    # ---------- Classify ----------
    print("→ classifying segments...")
    classifications = [
        classify_segment(seg, is_first=(i == 0)) for i, seg in enumerate(segments)
    ]

    counts = Counter(c["classification"] for c in classifications)
    confidence = Counter(c["confidence"] for c in classifications)
    print(f"  classifications: {dict(counts)}")
    print(f"  confidence:      {dict(confidence)}")
    print()

    # ---------- Diagnostic samples ----------
    def sample_n(cls_label: str, n: int = 5) -> list[tuple[int, dict, str]]:
        out = []
        for i, c in enumerate(classifications):
            if c["classification"] == cls_label and len(out) < n:
                out.append((i, c, segments[i]))
        return out

    print("→ sample ARTICLE_HEAD segments (5):")
    for idx, cls, seg in sample_n("ARTICLE_HEAD", 5):
        print(f"  [page {idx + 1}] headline={cls['headline']!r}")
        print(f"           page_no={cls['page_number']}  date={cls['date_string']}")
        print(f"           reason: {cls['reason']}")
        print(f"           first 200 chars of body: {seg.strip()[:200]!r}")
        print()

    print("→ sample ARTICLE_CONTINUATION segments (5):")
    for idx, cls, seg in sample_n("ARTICLE_CONTINUATION", 5):
        print(f"  [page {idx + 1}] first_line={cls['first_line']!r}")
        print(f"           reason: {cls['reason']}")
        print()

    print("→ sample UNKNOWN segments (5):")
    for idx, cls, seg in sample_n("UNKNOWN", 5):
        print(f"  [page {idx + 1}] first_line={cls['first_line']!r}")
        print(f"           full top 400 chars: {seg.strip()[:400]!r}")
        print()

    # ---------- Headline length histogram (HEAD only) ----------
    head_headlines = [
        c["headline"] for c in classifications if c["classification"] == "ARTICLE_HEAD"
    ]
    head_with_headline = [h for h in head_headlines if h]
    if head_with_headline:
        lens = [len(h) for h in head_with_headline]
        print(
            f"→ headline length: min={min(lens)}  max={max(lens)}  "
            f"mean={sum(lens) / len(lens):.1f}  null={len(head_headlines) - len(head_with_headline)}"
        )
        print()

    # ---------- Assemble articles ----------
    print("→ assembling articles (merging continuations into HEADs)...")
    articles = assemble_articles(segments, classifications)
    print(f"  detected articles: {len(articles)}")
    multi_page = sum(1 for a in articles if a["is_multi_page"])
    print(f"  multi-page articles: {multi_page}")
    orphans = sum(
        1
        for a in articles
        if a["headline"] and a["headline"].startswith("[ORPHAN")
    )
    print(f"  orphan articles (continuation without preceding head): {orphans}")
    print()

    # ---------- Match against CSV ----------
    print("→ matching detected articles to CSV unique-article triples...")
    matched, total_csv, unmatched, tier_counts = match_articles_to_csv(articles, CSV_PATH)
    print(f"  CSV unique articles: {total_csv}")
    print(f"  matched (normalized headline found in detected set): {matched}")
    print(f"  match tiers: {tier_counts}")
    if total_csv > 0:
        print(f"  match rate: {100 * matched / total_csv:.1f}%")
    print(f"  unmatched CSV articles: {len(unmatched)}")
    print()
    print("  → sample unmatched (10):")
    for u in unmatched[:10]:
        print(f"     {u['publication']:30s}  {u['date']:12s}  {u['headline'][:80]!r}")
    print()

    # ---------- Acceptance bar ----------
    if total_csv > 0:
        rate = 100 * matched / total_csv
        if rate >= 85:
            verdict = "GREEN ≥85% — detector validated, proceed to scoring pipeline"
        elif rate >= 70:
            verdict = f"YELLOW {rate:.1f}% — detector acceptable but flag missing articles"
        else:
            verdict = f"RED {rate:.1f}% — detector needs iteration before scoring"
        print(f"→ ACCEPTANCE: {verdict}")
        print()

    # ---------- Commit ----------
    if commit:
        if not OUTPUT_PATH.parent.exists():
            sys.exit(f"FATAL: output directory does not exist: {OUTPUT_PATH.parent}")
        OUTPUT_PATH.write_text(
            json.dumps(
                {
                    "schema_version": "v1",
                    "generated_at": datetime.now(timezone.utc).isoformat(),
                    "pdf_path": str(PDF_PATH),
                    "pdf_pages": len(segments),
                    "detected_articles": len(articles),
                    "multi_page_articles": multi_page,
                    "csv_match_rate_pct": round(100 * matched / total_csv, 2)
                    if total_csv
                    else None,
                    "articles": articles,
                    "unmatched_csv_articles": unmatched,
                },
                indent=2,
            )
        )
        print(f"→ wrote: {OUTPUT_PATH}")

        # Also save full diagnostic dump for review
        DIAG_PATH.write_text(
            "\n".join(
                f"page {i + 1}: {c['classification']:25s} {c['confidence']:6s} "
                f"reason={c['reason']!r} headline={c['headline']!r}"
                for i, c in enumerate(classifications)
            )
        )
        print(f"→ wrote: {DIAG_PATH}")
    else:
        print("→ DRY-RUN — no files written. Pass --commit to write _article_index.json.")


if __name__ == "__main__":
    run(commit="--commit" in sys.argv)
