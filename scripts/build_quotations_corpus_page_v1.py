#!/usr/bin/env python3
"""
build_quotations_corpus_page_v1.py

Emit a single browseable + embeddable wiki page listing all 334 quotes from
_master_quotations_prescience.csv.

Layout:
  - Sort: analyst ASC -> final_bucket (high, medium, low) -> date ASC
  - One H2 per analyst, one H4 per quote
  - YAML frontmatter for Obsidian/Dataview

Author: Kastner Archive pipeline
Version: v1 (2026-06-19)
"""

import csv
import sys
import datetime
from pathlib import Path
from collections import defaultdict

ARCHIVE = Path.home() / "Desktop/Archive/archive_masters"
WIKI = Path.home() / "Repos/kastner-aberdeen-wiki"
MASTER = ARCHIVE / "_master_quotations_prescience.csv"
OUT_DIR = WIKI / "wiki" / "methodology"
OUT_PATH = OUT_DIR / "quotations_corpus_v1.md"

BUCKET_ORDER = {"high": 0, "medium": 1, "low": 2}

commit = "--commit" in sys.argv


def load_rows():
    with open(MASTER, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        rows = list(reader)
    return rows


def sort_key(r):
    analyst = (r.get("analyst") or "").strip().lower()
    bucket = (r.get("final_bucket") or "").strip().lower()
    date = (r.get("date") or "").strip()
    return (analyst, BUCKET_ORDER.get(bucket, 99), date)


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
    lines.append(f"#### {date} — {publication} — {bucket.upper()}{contam_note}")
    lines.append("")
    lines.append(f"- **row_id**: {rid}")
    lines.append(f"- **headline**: {headline}")
    lines.append(f"- **horizon**: {horizon}")
    lines.append(f"- **final**: bucket={bucket} | score={score} | confidence={conf} | pipeline={pipeline}")
    lines.append("")
    lines.append("**Quote:**")
    lines.append("")
    # Block-quote each line
    for ql in quote.splitlines() or [quote]:
        lines.append(f"> {ql}")
    lines.append("")
    if rationale:
        lines.append("**Rationale:**")
        lines.append("")
        for rl in rationale.splitlines() or [rationale]:
            lines.append(f"> {rl}")
        lines.append("")
    return "\n".join(lines)


def main():
    rows = load_rows()
    n = len(rows)
    print(f"Loaded {n} rows from {MASTER}")
    print(f"Mode: {'COMMIT' if commit else 'DRY-RUN'}")

    rows.sort(key=sort_key)

    analysts = defaultdict(list)
    for r in rows:
        a = (r.get("analyst") or "(unknown)").strip() or "(unknown)"
        analysts[a].append(r)

    bucket_counts = defaultdict(int)
    contam_count = 0
    for r in rows:
        b = (r.get("final_bucket") or "").strip().lower()
        bucket_counts[b] += 1
        if (r.get("blog_scrape_contamination_flag") or "").strip().lower() in ("true", "1", "yes"):
            contam_count += 1

    print(f"Analysts: {len(analysts)}")
    print(f"Buckets: high={bucket_counts['high']} medium={bucket_counts['medium']} low={bucket_counts['low']}")
    print(f"Contaminated rows flagged: {contam_count}")

    # Build markdown
    now_iso = datetime.datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ")
    out = []
    out.append("---")
    out.append("title: Quotations Corpus v1")
    out.append("type: methodology")
    out.append("slug: quotations-corpus-v1")
    out.append("scorer_version: quotations_corpus_v1")
    out.append("source_pass: quotations_corpus")
    out.append(f"generated_at: {now_iso}")
    out.append(f"n_quotes: {n}")
    out.append(f"n_analysts: {len(analysts)}")
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
        f"Browseable index of all **{n} analyst quotes** scored by the v1.8.0 "
        f"quotations corpus pipeline. Source master: `_master_quotations_prescience.csv` "
        f"(334×31). Sort: analyst ASC → final_bucket (high → medium → low) → date ASC."
    )
    out.append("")
    out.append("## Shape")
    out.append("")
    out.append(f"- Quotes: **{n}**")
    out.append(f"- Analysts: **{len(analysts)}**")
    out.append(f"- High: **{bucket_counts['high']}** ({bucket_counts['high']*100/n:.1f}%)")
    out.append(f"- Medium: **{bucket_counts['medium']}** ({bucket_counts['medium']*100/n:.1f}%)")
    out.append(f"- Low: **{bucket_counts['low']}** ({bucket_counts['low']*100/n:.1f}%)")
    out.append(f"- Blog-scrape contamination flagged: **{contam_count}**")
    out.append("")
    out.append("## Table of Contents")
    out.append("")
    for a in sorted(analysts.keys(), key=lambda s: s.lower()):
        anchor = a.lower().replace(" ", "-").replace(".", "").replace(",", "")
        out.append(f"- [{a}](#{anchor}) — {len(analysts[a])} quote{'s' if len(analysts[a])!=1 else ''}")
    out.append("")

    # Per-analyst sections
    for a in sorted(analysts.keys(), key=lambda s: s.lower()):
        out.append(f"## {a}")
        out.append("")
        a_rows = analysts[a]
        a_buckets = defaultdict(int)
        for r in a_rows:
            a_buckets[(r.get("final_bucket") or "").strip().lower()] += 1
        out.append(
            f"_{len(a_rows)} quote{'s' if len(a_rows)!=1 else ''} — "
            f"high={a_buckets['high']}, medium={a_buckets['medium']}, low={a_buckets['low']}_"
        )
        out.append("")
        for r in a_rows:  # already sorted by global sort_key
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
    out.append("- **Generator**: `scripts/build_quotations_corpus_page_v1.py`")
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
        # Show a peek
        print("\n--- First 30 lines preview ---")
        for line in md.splitlines()[:30]:
            print(line)


if __name__ == "__main__":
    main()
