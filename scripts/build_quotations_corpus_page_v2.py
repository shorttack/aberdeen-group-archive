#!/usr/bin/env python3
"""
build_quotations_corpus_page_v2.py

Emit a single browseable + embeddable wiki page listing all 334 quotes from
_master_quotations_prescience.csv.

Layout (v2):
  - Flat sequence — no analyst grouping (corpus is single-author: Peter S. Kastner)
  - Sort: final_bucket (high -> medium -> low) -> date ASC
  - One H2 per bucket, one H4 per quote
  - YAML frontmatter for Obsidian/Dataview

Author: Kastner Archive pipeline
Version: v2 (2026-06-19) — drops analyst grouping per Pete (single-author corpus)
"""

import csv
import sys
import datetime
from pathlib import Path
from collections import defaultdict

ARCHIVE = Path.home() / "Desktop/Archive/aberdeen-group-archive"
WIKI = Path.home() / "Repos/kastner-aberdeen-wiki"
MASTER = ARCHIVE / "_master_quotations_prescience.csv"
OUT_DIR = WIKI / "wiki" / "methodology"
OUT_PATH = OUT_DIR / "quotations_corpus_v1.md"

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


def render_quote_block(r):
    bucket = (r.get("final_bucket") or "").strip()
    score = (r.get("final_score") or "").strip()
    conf = (r.get("final_confidence") or "").strip()
    pipeline = (r.get("final_pipeline") or "").strip()
    publication = (r.get("publication") or "").strip()
    date = (r.get("date") or "").strip()
    horizon = (r.get("horizon_label") or "").strip()
    headline = (r.get("headline") or "").strip()
    quote = (r.get("quote") or "").strip()
    rationale = (r.get("final_rationale") or "").strip()
    rid = (r.get("row_id") or "").strip()
    contam = (r.get("blog_scrape_contamination_flag") or "").strip().lower()
    contam_note = " ⚠️ blog-scrape contamination" if contam in ("true", "1", "yes") else ""

    lines = []
    lines.append(f"#### {date} — {publication}{contam_note}")
    lines.append("")
    lines.append(f"- **row_id**: {rid}")
    lines.append(f"- **headline**: {headline}")
    lines.append(f"- **horizon**: {horizon}")
    lines.append(f"- **final**: bucket={bucket} | score={score} | confidence={conf} | pipeline={pipeline}")
    lines.append("")
    lines.append("**Quote:**")
    lines.append("")
    for ql in (quote.splitlines() or [quote]):
        lines.append(f"> {ql}")
    lines.append("")
    if rationale:
        lines.append("**Rationale:**")
        lines.append("")
        for rl in (rationale.splitlines() or [rationale]):
            lines.append(f"> {rl}")
        lines.append("")
    return "\n".join(lines)


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

    now_iso = datetime.datetime.now(datetime.UTC).strftime("%Y-%m-%dT%H:%M:%SZ")
    out = []
    out.append("---")
    out.append("title: Quotations Corpus v1")
    out.append("type: methodology")
    out.append("slug: quotations-corpus-v1")
    out.append("author: Peter S. Kastner")
    out.append("scorer_version: quotations_corpus_v1")
    out.append("source_pass: quotations_corpus")
    out.append(f"generated_at: {now_iso}")
    out.append(f"n_quotes: {n}")
    out.append(f"n_high: {bucket_counts['high']}")
    out.append(f"n_medium: {bucket_counts['medium']}")
    out.append(f"n_low: {bucket_counts['low']}")
    out.append(f"n_blog_scrape_contamination: {contam_count}")
    out.append("tags: [methodology, quotations, prescience, corpus]")
    out.append("---")
    out.append("")
    out.append("# Quotations Corpus v1")
    out.append("")
    out.append(
        f"Browseable index of all **{n} published predictions** by Peter S. Kastner, "
        f"scored by the v1.8.0 quotations corpus pipeline. Source master: "
        f"`_master_quotations_prescience.csv` (334×31). Sort: final_bucket "
        f"(high → medium → low) → date ASC."
    )
    out.append("")
    out.append("## Shape")
    out.append("")
    out.append(f"- Quotes: **{n}**")
    out.append(f"- High: **{bucket_counts['high']}** ({bucket_counts['high']*100/n:.1f}%)")
    out.append(f"- Medium: **{bucket_counts['medium']}** ({bucket_counts['medium']*100/n:.1f}%)")
    out.append(f"- Low: **{bucket_counts['low']}** ({bucket_counts['low']*100/n:.1f}%)")
    out.append(f"- Blog-scrape contamination flagged: **{contam_count}**")
    out.append("")
    out.append("## Table of Contents")
    out.append("")
    for b in ("high", "medium", "low"):
        anchor = BUCKET_LABELS[b].lower().replace(" ", "-")
        out.append(f"- [{BUCKET_LABELS[b]}](#{anchor}) — {bucket_counts[b]} quote{'s' if bucket_counts[b]!=1 else ''}")
    out.append("")

    by_bucket = defaultdict(list)
    for r in rows:
        b = (r.get("final_bucket") or "").strip().lower()
        by_bucket[b].append(r)

    for b in ("high", "medium", "low"):
        out.append(f"## {BUCKET_LABELS[b]}")
        out.append("")
        out.append(
            f"_{bucket_counts[b]} quote{'s' if bucket_counts[b]!=1 else ''} "
            f"({bucket_counts[b]*100/n:.1f}% of corpus) — sorted by date ASC_"
        )
        out.append("")
        for r in by_bucket[b]:  # already sorted globally; within bucket = date ASC
            out.append(render_quote_block(r))
            out.append("---")
            out.append("")

    out.append("")
    out.append("## Provenance")
    out.append("")
    out.append("- **Source master**: `_master_quotations_prescience.csv` (334 rows × 31 cols)")
    out.append("- **Scorer version**: `quotations_corpus_v1`")
    out.append("- **Source pass**: `quotations_corpus`")
    out.append(f"- **Generated**: {now_iso}")
    out.append("- **Generator**: `scripts/build_quotations_corpus_page_v2.py`")
    out.append("")

    md = "\n".join(out)
    md_bytes = len(md.encode("utf-8"))
    print(f"Markdown size: {md_bytes:,} bytes (~{md_bytes/1024:.1f} KB)")
    print(f"Output path: {OUT_PATH}")

    if commit:
        OUT_DIR.mkdir(parents=True, exist_ok=True)
        OUT_PATH.write_text(md, encoding="utf-8")
        print(f"WROTE: {OUT_PATH}")
    else:
        print("DRY-RUN only — pass --commit to write the file.")
        print("\n--- First 30 lines preview ---")
        for line in md.splitlines()[:30]:
            print(line)


if __name__ == "__main__":
    main()
