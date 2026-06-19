#!/usr/bin/env python3
"""
build_quotations_per_quote_v1.py

Emit one wiki page per quote (334 pages) from _master_quotations_prescience.csv,
plus a slim index page replacing the monolithic v1 page.

Why: bge-m3 has an ~8192-token effective context. The v1 monolith (377 KB) embedded
as a single chunk had a centroid of "methodology + buckets" not "Oracle 1997" — so
quote-level kw ask retrieval failed. Per-quote pages give each prediction its own
retrievable embedding.

Layout:
  wiki/quotations/quote-<row_id>.md       (334 pages, ~1-5 KB each)
  wiki/methodology/quotations_corpus_v1.md (slim index, ~30 KB)

Author: Kastner Archive pipeline
Version: v1 (2026-06-19) — supersedes monolithic build_quotations_corpus_page_v2.py
"""

import csv
import sys
import datetime
import re
from pathlib import Path
from collections import defaultdict

ARCHIVE = Path.home() / "Desktop/Archive/archive_masters"
WIKI = Path.home() / "Repos/kastner-aberdeen-wiki"
MASTER = ARCHIVE / "_master_quotations_prescience.csv"
QUOTES_DIR = WIKI / "wiki" / "quotations"
INDEX_PATH = WIKI / "wiki" / "methodology" / "quotations_corpus_v1.md"

BUCKET_ORDER = {"high": 0, "medium": 1, "low": 2}
BUCKET_LABELS = {"high": "High prescience", "medium": "Medium prescience", "low": "Low prescience"}

commit = "--commit" in sys.argv


def load_rows():
    with open(MASTER, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        rows = list(reader)
    return rows


def sort_key(r):
    bucket = (r.get("final_bucket") or "").strip().lower()
    date = (r.get("date") or "").strip()
    return (BUCKET_ORDER.get(bucket, 99), date)


def slug_from_row_id(rid):
    """Slug-safe row_id (already numeric in this corpus, but be defensive)."""
    return re.sub(r"[^a-zA-Z0-9_-]", "-", str(rid).strip())


def render_quote_page(r):
    rid = (r.get("row_id") or "").strip()
    bucket = (r.get("final_bucket") or "").strip().lower()
    score = (r.get("final_score") or "").strip()
    conf = (r.get("final_confidence") or "").strip()
    pipeline = (r.get("final_pipeline") or "").strip()
    publication = (r.get("publication") or "").strip()
    date = (r.get("date") or "").strip()
    horizon = (r.get("horizon_label") or "").strip()
    headline = (r.get("headline") or "").strip()
    quote = (r.get("quote") or "").strip()
    rationale = (r.get("final_rationale") or "").strip()
    analyst = (r.get("analyst") or "Peter S. Kastner").strip()
    contam = (r.get("blog_scrape_contamination_flag") or "").strip().lower() in ("true", "1", "yes")

    # Frontmatter — every value YAML-safe
    def y(v):
        s = str(v).replace('"', '\\"')
        return f'"{s}"'

    lines = []
    lines.append("---")
    lines.append(f"title: Quote {rid} — {publication} ({date})")
    lines.append("type: quotation")
    lines.append(f"slug: quote-{slug_from_row_id(rid)}")
    lines.append(f"row_id: {rid}")
    lines.append(f"author: {y(analyst)}")
    lines.append(f"publication: {y(publication)}")
    lines.append(f"date: {y(date)}")
    lines.append(f"headline: {y(headline)}")
    lines.append(f"horizon: {y(horizon)}")
    lines.append(f"final_bucket: {bucket}")
    lines.append(f"final_score: {score}")
    lines.append(f"final_confidence: {conf}")
    lines.append(f"final_pipeline: {pipeline}")
    lines.append(f"blog_scrape_contamination: {'true' if contam else 'false'}")
    lines.append("scorer_version: quotations_corpus_v1")
    lines.append("source_pass: quotations_corpus")
    lines.append("tags: [quotation, prescience, kastner]")
    lines.append("---")
    lines.append("")
    lines.append(f"# {publication} — {date}")
    lines.append("")
    if headline:
        lines.append(f"**Headline**: {headline}")
        lines.append("")
    lines.append(f"**Verdict**: {bucket.upper()} prescience — score={score}, confidence={conf}, horizon={horizon}, pipeline={pipeline}")
    if contam:
        lines.append("")
        lines.append("⚠️ **Note**: This quote was flagged for blog-scrape contamination (footer text / share-buttons mixed with the prediction). The verdict applies to the predictive content; the surrounding text is artifact.")
    lines.append("")
    lines.append("## Quote")
    lines.append("")
    for ql in (quote.splitlines() or [quote]):
        lines.append(f"> {ql}")
    lines.append("")
    if rationale:
        lines.append("## Rationale")
        lines.append("")
        for rl in (rationale.splitlines() or [rationale]):
            lines.append(rl)
        lines.append("")
    lines.append("## Provenance")
    lines.append("")
    lines.append(f"- **row_id**: {rid}")
    lines.append(f"- **Source master**: `_master_quotations_prescience.csv`")
    lines.append(f"- **Scorer version**: quotations_corpus_v1")
    lines.append(f"- **Author**: {analyst}")
    lines.append("")
    return "\n".join(lines)


def render_index(rows, bucket_counts, contam_count, n_pages):
    now_iso = datetime.datetime.now(datetime.UTC).strftime("%Y-%m-%dT%H:%M:%SZ")
    out = []
    out.append("---")
    out.append("title: Quotations Corpus v1 — Index")
    out.append("type: methodology")
    out.append("slug: quotations-corpus-v1")
    out.append("author: Peter S. Kastner")
    out.append("scorer_version: quotations_corpus_v1")
    out.append("source_pass: quotations_corpus")
    out.append(f"generated_at: {now_iso}")
    out.append(f"n_quotes: {len(rows)}")
    out.append(f"n_high: {bucket_counts['high']}")
    out.append(f"n_medium: {bucket_counts['medium']}")
    out.append(f"n_low: {bucket_counts['low']}")
    out.append(f"n_blog_scrape_contamination: {contam_count}")
    out.append("tags: [methodology, quotations, prescience, corpus, index]")
    out.append("---")
    out.append("")
    out.append("# Quotations Corpus v1 — Index")
    out.append("")
    out.append(
        f"Index of **{len(rows)} published predictions** by Peter S. Kastner, scored "
        f"by the v1.8.0 quotations corpus pipeline. Each quote is its own page under "
        f"`wiki/quotations/` for retrieval — see links below grouped by verdict + date."
    )
    out.append("")
    out.append("## Shape")
    out.append("")
    out.append(f"- Total quotes: **{len(rows)}** (wiki pages: {n_pages})")
    out.append(f"- High: **{bucket_counts['high']}** ({bucket_counts['high']*100/len(rows):.1f}%)")
    out.append(f"- Medium: **{bucket_counts['medium']}** ({bucket_counts['medium']*100/len(rows):.1f}%)")
    out.append(f"- Low: **{bucket_counts['low']}** ({bucket_counts['low']*100/len(rows):.1f}%)")
    out.append(f"- Blog-scrape contamination flagged: **{contam_count}**")
    out.append("")

    by_bucket = defaultdict(list)
    for r in rows:
        b = (r.get("final_bucket") or "").strip().lower()
        by_bucket[b].append(r)

    for b in ("high", "medium", "low"):
        out.append(f"## {BUCKET_LABELS[b]} ({bucket_counts[b]})")
        out.append("")
        for r in by_bucket[b]:
            rid = (r.get("row_id") or "").strip()
            date = (r.get("date") or "").strip()
            pub = (r.get("publication") or "").strip()
            headline = (r.get("headline") or "").strip()
            slug = f"quote-{slug_from_row_id(rid)}"
            contam = (r.get("blog_scrape_contamination_flag") or "").strip().lower() in ("true", "1", "yes")
            cmark = " ⚠️" if contam else ""
            # Obsidian wikilink — relative path-safe
            out.append(f"- [[{slug}|{date} — {pub}]]{cmark}{' — ' + headline if headline else ''}")
        out.append("")

    out.append("## Provenance")
    out.append("")
    out.append("- **Source master**: `_master_quotations_prescience.csv` (334 rows × 31 cols)")
    out.append("- **Per-quote pages**: `wiki/quotations/quote-<row_id>.md` (334 pages)")
    out.append("- **Scorer version**: quotations_corpus_v1")
    out.append("- **Source pass**: quotations_corpus")
    out.append(f"- **Generated**: {now_iso}")
    out.append("- **Generator**: `scripts/build_quotations_per_quote_v1.py`")
    out.append("")
    out.append("## Why per-quote pages")
    out.append("")
    out.append(
        "The original v1 page was a single 377 KB markdown listing all 334 quotes. "
        "bge-m3 has an effective ~8192-token context window — a 377 KB embedding "
        "centroid resolved to \"methodology / buckets\" rather than any specific "
        "prediction. Per-quote chunking gives each prediction its own retrievable "
        "embedding, so `kw ask \"what did Pete predict about Oracle\"` surfaces the "
        "actual quote pages, not just the longitudinal study summaries."
    )
    out.append("")
    return "\n".join(out)


def main():
    rows = load_rows()
    n = len(rows)
    print(f"Loaded {n} rows from {MASTER}")
    print(f"Mode: {'COMMIT' if commit else 'DRY-RUN'}")

    rows.sort(key=sort_key)

    bucket_counts = defaultdict(int)
    contam_count = 0
    for r in rows:
        b = (r.get("final_bucket") or "").strip().lower()
        bucket_counts[b] += 1
        if (r.get("blog_scrape_contamination_flag") or "").strip().lower() in ("true", "1", "yes"):
            contam_count += 1

    print(f"Buckets: high={bucket_counts['high']} medium={bucket_counts['medium']} low={bucket_counts['low']}")
    print(f"Contaminated rows flagged: {contam_count}")

    # Build per-quote pages
    pages = []
    total_bytes = 0
    for r in rows:
        rid = (r.get("row_id") or "").strip()
        slug = slug_from_row_id(rid)
        path = QUOTES_DIR / f"quote-{slug}.md"
        body = render_quote_page(r)
        pages.append((path, body))
        total_bytes += len(body.encode("utf-8"))

    avg_kb = (total_bytes / len(pages)) / 1024 if pages else 0
    print(f"Per-quote pages: {len(pages)} files, total {total_bytes/1024:.1f} KB, avg {avg_kb:.1f} KB/page")

    # Build index
    index_md = render_index(rows, bucket_counts, contam_count, len(pages))
    index_bytes = len(index_md.encode("utf-8"))
    print(f"Index page: {index_bytes/1024:.1f} KB → {INDEX_PATH}")

    if commit:
        QUOTES_DIR.mkdir(parents=True, exist_ok=True)
        INDEX_PATH.parent.mkdir(parents=True, exist_ok=True)
        for path, body in pages:
            path.write_text(body, encoding="utf-8")
        INDEX_PATH.write_text(index_md, encoding="utf-8")
        print(f"WROTE: {len(pages)} per-quote pages under {QUOTES_DIR}")
        print(f"WROTE: index {INDEX_PATH}")
    else:
        print("DRY-RUN only — pass --commit to write all files.")
        print("\n--- Sample per-quote page (first row) ---")
        sample = pages[0][1]
        for line in sample.splitlines()[:40]:
            print(line)
        if len(sample.splitlines()) > 40:
            print(f"... ({len(sample.splitlines())-40} more lines)")


if __name__ == "__main__":
    main()
