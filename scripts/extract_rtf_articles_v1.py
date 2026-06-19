#!/usr/bin/env python3
"""
extract_rtf_articles_v1.py

Extract articles from Pete's Computerworld RTF compilation
(~/Desktop/Archive/Kastner_cleaned_quotes.rtf).

Strategy: RTF format is regular. Every article ends with `CW Staff` or
`BY<author>, CW Staff`, then a blank line, then:

    <Headline>
    <Section/Subhead> <Author> Page: <N> <MM/DD/YY>
    ──────...
    <body>

We slice on the `Page: N MM/DD/YY` markers — each becomes an article
boundary, with the headline being the line immediately preceding the
metadata line, and the body being everything from after the separator
until the next Page-Date marker.

Output (dry-run by default, --commit writes):
  - /Users/scott/Desktop/Archive/aberdeen-group-archive/kastner-author/
    quotations/_rtf_article_index.json

Companion to detect_article_boundaries_v2 (PDF detector). Once both
indices exist, a downstream union step de-duplicates by date + headline
prefix to produce the final article corpus for v1.8.0 Pipeline 1.
"""
import json, re, subprocess, sys, unicodedata
from datetime import datetime, timezone
from pathlib import Path

RTF_PATH = Path("/Users/scott/Desktop/Archive/Kastner_cleaned_quotes.rtf")
OUTPUT_PATH = Path(
    "/Users/scott/Desktop/Archive/aberdeen-group-archive/kastner-author/quotations/_rtf_article_index.json"
)

# Page-Date pattern — same as PDF detector
PAGE_DATE_PATTERN = re.compile(
    r"Page:\s*(\d{1,4})\s+(\d{1,2}/\d{1,2}/\d{2,4})"
)


def extract_plain_text(rtf_path: Path) -> str:
    """Shell out to pandoc to convert RTF to plain text. pandoc is installed on
    Pete's Mac (verified)."""
    if not rtf_path.exists():
        sys.exit(f"FATAL: RTF not found at {rtf_path}")
    result = subprocess.run(
        ["pandoc", "-f", "rtf", "-t", "plain", str(rtf_path)],
        capture_output=True, text=True, check=False,
    )
    if result.returncode != 0:
        sys.exit(f"FATAL: pandoc failed: {result.stderr[:500]}")
    return result.stdout


def normalize_text(s: str) -> str:
    s = unicodedata.normalize("NFKD", s)
    s = s.replace("\u2019", "'").replace("\u2018", "'")
    s = s.replace("\u201c", '"').replace("\u201d", '"')
    s = s.replace("\u2014", "-").replace("\u2013", "-")
    s = re.sub(r"\s+", " ", s)
    s = s.strip().lower().strip("'\"").rstrip(";,.:")
    return s.strip()


def parse_mmddyy(s: str) -> str | None:
    """Parse MM/DD/YY or MM/DD/YYYY → ISO YYYY-MM-DD."""
    try:
        parts = s.split("/")
        if len(parts) != 3:
            return None
        mm, dd, yy = parts
        mm, dd = int(mm), int(dd)
        yy_i = int(yy)
        if len(yy) == 2:
            # Pete left Aberdeen 2007 — so 2-digit years 00-07 = 2000s, 50-99 = 1900s,
            # 08-49 ambiguous but unlikely (no source articles past 2007)
            yy_i = 2000 + yy_i if yy_i < 50 else 1900 + yy_i
        return f"{yy_i:04d}-{mm:02d}-{dd:02d}"
    except Exception:
        return None


def extract_articles(text: str) -> list[dict]:
    """Slice text on Page-Date markers, return list of article dicts."""
    matches = list(PAGE_DATE_PATTERN.finditer(text))
    if not matches:
        return []

    articles = []
    for i, m in enumerate(matches):
        # The metadata line is the line CONTAINING the Page-Date match
        # Find the start of that line
        meta_line_start = text.rfind("\n", 0, m.start()) + 1
        meta_line_end = text.find("\n", m.end())
        if meta_line_end == -1:
            meta_line_end = len(text)
        meta_line = text[meta_line_start:meta_line_end].strip()

        # Headline = preceding non-empty line, walking backward
        # (skip blank lines and the "CW Staff" boilerplate)
        hl = None
        cursor = meta_line_start - 1
        # Walk backward through lines looking for the headline
        hop = 0
        while cursor > 0 and hop < 20:
            line_end = cursor
            line_start = text.rfind("\n", 0, cursor) + 1
            line = text[line_start:line_end].strip()
            # Skip blank, separator, CW-staff-style boilerplate
            if not line:
                pass
            elif line.startswith("─"):
                pass
            elif re.match(r"^(BY[\w\s,.-]+,\s*)?CW Staff\s*$", line, re.I):
                pass
            elif re.match(r"^By\s+[\w\s,.'-]+$", line, re.I) and len(line) < 60:
                # short byline like "By Jean S. Bozman"
                pass
            else:
                # First non-skippable line is the headline candidate
                # Reject if it's itself a metadata-pattern line (shouldn't be, but
                # guards against degenerate cases)
                if not PAGE_DATE_PATTERN.search(line):
                    # Strip leading "CW Staff " / "CW staff " prefix (RTF compilation
                    # artifact where the previous article's terminating byline merged
                    # into the next article's headline line)
                    line = re.sub(r"^CW\s+[Ss]taff\s+", "", line)
                    # Strip trailing semicolons / commas / periods
                    hl = line.rstrip(";,.:").strip()
                    break
            cursor = line_start - 1
            hop += 1

        # Body = everything from after the metadata line up to the next match's
        # meta_line_start, OR end of text
        body_start = meta_line_end + 1
        if i + 1 < len(matches):
            next_m = matches[i + 1]
            next_meta_start = text.rfind("\n", 0, next_m.start()) + 1
            # Walk further back to exclude the headline + byline of the next article
            # Be conservative: stop at the position before any headline-line that we
            # would identify as belonging to the NEXT article.
            # Simplest: end body at start of next metadata line minus a small lookback
            # for the headline (~3 lines back)
            lookback_end = next_meta_start
            lines_back = 0
            cur = next_meta_start - 1
            while cur > body_start and lines_back < 4:
                cur = text.rfind("\n", 0, cur)
                if cur == -1: break
                lines_back += 1
            body_end = max(body_start, cur if cur > 0 else next_meta_start)
        else:
            body_end = len(text)

        body = text[body_start:body_end].strip()

        # Parse date
        iso_date = parse_mmddyy(m.group(2))

        # Try to pull author from meta_line: pattern "<section/header> <Author> Page: ..."
        # Author often "Lastname, Firstname" before "Page:"
        author = None
        before_page = meta_line[: meta_line.find("Page:")].rstrip()
        # Common author pattern: "..., X. Page:" or "Lastname, Firstname Page:"
        am = re.search(r"([A-Z][\w'.-]+(?:,\s*[A-Z][\w'.-]+(?:\s+[A-Z]\.?)?)?)\s*$", before_page)
        if am:
            author = am.group(1)

        articles.append({
            "source": "rtf",
            "article_idx": i,
            "headline": hl,
            "headline_norm": normalize_text(hl) if hl else None,
            "date": iso_date,
            "page_no": int(m.group(1)),
            "metadata_line": meta_line,
            "author_hint": author,
            "body_chars": len(body),
            "body_preview": body[:300],
            "body": body,
        })

    return articles


def match_against_csv(articles: list[dict], csv_path: Path) -> dict:
    """Match RTF-extracted articles against CSV unique-article triples by
    (date, normalized-headline)."""
    import csv as csv_mod
    if not csv_path.exists():
        return {"matched": 0, "total_csv": 0, "tier_counts": {}}

    with open(csv_path) as f:
        rows = list(csv_mod.DictReader(f))

    csv_set = {}
    for r in rows:
        h = r.get("headline", "").strip()
        d = r.get("date", "").strip()
        if not h: continue
        nh = normalize_text(h)
        # Index by both full normalized headline and prefix
        csv_set[nh] = (d, r.get("publication", ""), r.get("row_id", ""))

    detected_norm = {(a["headline_norm"]) for a in articles if a.get("headline_norm")}

    matched_exact = 0
    matched_prefix50 = 0
    for nh in detected_norm:
        if nh in csv_set:
            matched_exact += 1
        elif len(nh) >= 50 and any(k.startswith(nh[:50]) or nh.startswith(k[:50]) for k in csv_set):
            matched_prefix50 += 1

    return {
        "total_csv_unique": len({normalize_text(r.get("headline","").strip()) for r in rows if r.get("headline","").strip()}),
        "detected_rtf_articles": len(articles),
        "matched_exact": matched_exact,
        "matched_prefix50": matched_prefix50,
    }


def run(commit: bool = False):
    print(f"[extract_rtf_articles_v1] {datetime.now(timezone.utc).isoformat()}")
    print(f"Mode: {'COMMIT' if commit else 'DRY-RUN (use --commit to write index)'}")
    print(f"RTF: {RTF_PATH}")
    print()

    text = extract_plain_text(RTF_PATH)
    print(f"→ extracted plain text: {len(text):,} chars  ({text.count(chr(10)):,} lines)")

    articles = extract_articles(text)
    print(f"→ extracted articles: {len(articles)}")
    print()

    # Stats
    null_hl = sum(1 for a in articles if not a["headline"])
    null_date = sum(1 for a in articles if not a["date"])
    body_chars = [a["body_chars"] for a in articles]
    print(f"  headline null: {null_hl}")
    print(f"  date null:     {null_date}")
    if body_chars:
        print(f"  body chars: min={min(body_chars)} max={max(body_chars)} mean={sum(body_chars)//len(body_chars)}")
    print()

    print("→ sample articles (5):")
    for a in articles[:5]:
        print(f"  [{a['date'] or '?':10s}  p{a['page_no']:4d}] {a['headline']!r}")
        print(f"     author_hint={a['author_hint']!r}")
        print(f"     body_preview={a['body_preview'][:150]!r}")
        print()

    # Match against CSV
    csv_path = Path("/Users/scott/Desktop/Archive/aberdeen-group-archive/kastner-author/quotations/kastner_quotes_clean.csv")
    if csv_path.exists():
        stats = match_against_csv(articles, csv_path)
        print(f"→ match against CSV unique articles:")
        for k, v in stats.items():
            print(f"     {k}: {v}")

    if commit:
        if not OUTPUT_PATH.parent.exists():
            sys.exit(f"FATAL: output directory does not exist: {OUTPUT_PATH.parent}")
        # Write index (omit full body in JSON to keep file size reasonable;
        # body is recoverable from the RTF directly)
        index = {
            "schema_version": "v1",
            "generated_at": datetime.now(timezone.utc).isoformat(),
            "rtf_path": str(RTF_PATH),
            "article_count": len(articles),
            "articles": [
                {k: v for k, v in a.items() if k not in ("body",)}
                for a in articles
            ],
        }
        OUTPUT_PATH.write_text(json.dumps(index, indent=2))
        print(f"\n→ WROTE: {OUTPUT_PATH}")
    else:
        print("\n→ DRY-RUN — no files written. Pass --commit to write _rtf_article_index.json.")


if __name__ == "__main__":
    run(commit=("--commit" in sys.argv))
