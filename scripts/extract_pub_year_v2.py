#!/usr/bin/env python3
"""
extract_pub_year_v2.py
======================

Second-pass pub_year extractor for the Kastner Aberdeen Archive.

Strategy
--------
For every study where v_studies.pub_year IS NULL, open:
    ~/Desktop/Archive/prepared/<study_id>/source/_raw_text.txt

Read the first 10 and last 10 lines. Find all 4-digit years in [1970, 2026].
Propose the EARLIEST year as pub_year.

If the text file is missing or no year is found in those 20 lines, the row
is emitted with proposed_pub_year blank and a notes column explaining why.

Where this script lives
-----------------------
On Pete's Mac:
    ~/Desktop/Archive/scripts/extract_pub_year_v2.py

In the archive repo (committed copy):
    shorttack/aberdeen-group-archive/scripts/extract_pub_year_v2.py

DB auto-detection
-----------------
The DuckDB lives in the wiki repo at:
    ~/Repos/kastner-aberdeen-wiki/db/kastner.duckdb

Checked in order:
    1. $KASTNER_WIKI_DB env var
    2. ~/Repos/kastner-aberdeen-wiki/db/kastner.duckdb
    3. ~/Documents/kastner-aberdeen-wiki/db/kastner.duckdb

Override with --db /path/to/kastner.duckdb.

Archive root auto-detection
---------------------------
Used to locate the per-study _raw_text.txt under prepared/<study_id>/source/.
Checked in order:
    1. $ARCHIVE_ROOT env var (full path to the directory containing prepared/)
    2. ~/Desktop/Archive                                     (Pete's Mac)

Override with --archive-root /path/to/Archive.

Output
------
- pub_year_candidates_v4.csv  (all studies with NULL pub_year)
- pub_year_v2_summary.txt     (per-rule counts + samples)

Columns:
  study_id, proposed_pub_year, source_rule, needs_pete_review,
  source_file, date_field, title, candidate_years_found, notes

source_rule values:
  raw_text_earliest_year     auto-apply (true confidence)
  ""                         no match — needs_pete_review=true, see notes

Usage
-----
    cd ~/Desktop/Archive
    python3 scripts/extract_pub_year_v2.py

Author: Pete Kastner / agent (BlueBridge Group)
"""

from __future__ import annotations

import argparse
import csv
import os
import re
import sys
from collections import Counter
from datetime import datetime
from pathlib import Path


# ---------------------------------------------------------------------------
# Config
# ---------------------------------------------------------------------------

OUT_CANDIDATES = "pub_year_candidates_v4.csv"
OUT_SUMMARY = "pub_year_v2_summary.txt"

YEAR_MIN = 1970
YEAR_MAX = 2026

HEAD_LINES = 10
TAIL_LINES = 10

RE_4DIGIT_YEAR = re.compile(r"\b((?:19|20)\d{2})\b")


# ---------------------------------------------------------------------------
# Path discovery
# ---------------------------------------------------------------------------

def find_db_path(explicit: str | None) -> Path | None:
    if explicit:
        p = Path(explicit).expanduser().resolve()
        return p if p.exists() else None
    env = os.environ.get("KASTNER_WIKI_DB")
    if env:
        p = Path(env).expanduser().resolve()
        if p.exists():
            return p
    home = Path.home()
    for c in [
        home / "Repos" / "kastner-aberdeen-wiki" / "db" / "kastner.duckdb",
        home / "Documents" / "kastner-aberdeen-wiki" / "db" / "kastner.duckdb",
    ]:
        if c.exists():
            return c.resolve()
    return None


def find_archive_root(explicit: str | None) -> Path | None:
    if explicit:
        p = Path(explicit).expanduser().resolve()
        return p if (p / "prepared").is_dir() else None
    env = os.environ.get("ARCHIVE_ROOT")
    if env:
        p = Path(env).expanduser().resolve()
        if (p / "prepared").is_dir():
            return p
    home = Path.home()
    p = home / "Desktop" / "Archive"
    return p.resolve() if (p / "prepared").is_dir() else None


# ---------------------------------------------------------------------------
# Year extraction
# ---------------------------------------------------------------------------

def years_in_text_window(text_file: Path) -> tuple[list[int], str | None]:
    """Return (sorted_unique_years, error_or_None) from first/last N lines."""
    try:
        with text_file.open("r", encoding="utf-8", errors="replace") as f:
            lines = f.readlines()
    except OSError as e:
        return [], f"read_error: {e}"

    if not lines:
        return [], "empty_file"

    head = lines[:HEAD_LINES]
    tail = lines[-TAIL_LINES:] if len(lines) > HEAD_LINES else []
    window = "".join(head) + "\n" + "".join(tail)

    raw = RE_4DIGIT_YEAR.findall(window)
    years = sorted({int(y) for y in raw if YEAR_MIN <= int(y) <= YEAR_MAX})
    return years, None


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main() -> int:
    ap = argparse.ArgumentParser(
        description="v2 pub_year extractor: grep first/last 10 lines of _raw_text.txt"
    )
    ap.add_argument("--db", help="Path to kastner.duckdb (default: auto-detect)")
    ap.add_argument(
        "--archive-root",
        help="Directory containing prepared/<study_id>/ tree (default: ~/Desktop/Archive)",
    )
    ap.add_argument(
        "--out-dir", default=".",
        help="Output directory for candidates CSV + summary (default: CWD)",
    )
    args = ap.parse_args()

    db_path = find_db_path(args.db)
    if db_path is None:
        print("ERROR: could not locate kastner.duckdb.", file=sys.stderr)
        return 2

    arch_root = find_archive_root(args.archive_root)
    if arch_root is None:
        print("ERROR: could not locate archive root containing prepared/ directory.", file=sys.stderr)
        return 2

    out_dir = Path(args.out_dir).expanduser().resolve()
    out_dir.mkdir(parents=True, exist_ok=True)
    out_csv = out_dir / OUT_CANDIDATES
    out_txt = out_dir / OUT_SUMMARY

    try:
        import duckdb
    except ImportError:
        print("ERROR: duckdb python module not installed.", file=sys.stderr)
        return 2

    print(f"DB:           {db_path}")
    print(f"Archive root: {arch_root}")
    print(f"Out dir:      {out_dir}")

    con = duckdb.connect(str(db_path), read_only=True)
    rows = con.execute(
        """
        SELECT study_id, title, author, date, source_file, type
        FROM v_studies
        WHERE pub_year IS NULL
        ORDER BY study_id
        """
    ).fetchall()
    cols = [d[0] for d in con.description]
    con.close()

    print(f"Loaded {len(rows)} studies with NULL pub_year")

    rule_counts: Counter[str] = Counter()
    note_counts: Counter[str] = Counter()
    out_rows = []

    for r in rows:
        d = dict(zip(cols, r))
        study_id = d["study_id"]
        text_path = arch_root / "prepared" / study_id / "source" / "_raw_text.txt"

        proposed = ""
        rule = ""
        needs_review = True
        candidate_years = []
        note = ""

        if not text_path.exists():
            note = "raw_text_not_found"
            note_counts[note] += 1
        else:
            years, err = years_in_text_window(text_path)
            candidate_years = years
            if err:
                note = err
                note_counts[note] += 1
            elif not years:
                note = "no_year_in_window"
                note_counts[note] += 1
            else:
                proposed = min(years)
                rule = "raw_text_earliest_year"
                needs_review = False
                rule_counts[rule] += 1

        if not rule:
            rule_counts["NO_MATCH"] += 1

        out_rows.append({
            "study_id":              study_id,
            "proposed_pub_year":     proposed if proposed != "" else "",
            "source_rule":           rule,
            "needs_pete_review":     "true" if needs_review else "false",
            "source_file":           d["source_file"] or "",
            "date_field":            d["date"] or "",
            "title":                 (d["title"] or "")[:120],
            "candidate_years_found": ";".join(str(y) for y in candidate_years),
            "notes":                 note,
        })

    fieldnames = [
        "study_id", "proposed_pub_year", "source_rule", "needs_pete_review",
        "source_file", "date_field", "title", "candidate_years_found", "notes",
    ]
    with open(out_csv, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fieldnames)
        w.writeheader()
        w.writerows(out_rows)

    # Summary
    auto_count = rule_counts.get("raw_text_earliest_year", 0)
    no_match = rule_counts.get("NO_MATCH", 0)

    summary_lines = [
        "=" * 70,
        "pub_year v2 extraction summary — extract_pub_year_v2.py",
        f"Run at:       {datetime.now().isoformat()}",
        f"DB:           {db_path}",
        f"Archive root: {arch_root}",
        "=" * 70,
        f"Total studies with NULL pub_year:  {len(rows)}",
        f"Auto-apply (raw_text_earliest):    {auto_count}",
        f"No match (hand disposition):       {no_match}",
        "",
        "NO_MATCH breakdown by reason:",
    ]
    for reason, count in note_counts.most_common():
        summary_lines.append(f"  {reason:25s} {count:4d}")

    summary_lines.append("")
    summary_lines.append("=" * 70)
    summary_lines.append("Samples (first 10 auto-apply rows)")
    summary_lines.append("=" * 70)
    auto_samples = [r for r in out_rows if r["source_rule"] == "raw_text_earliest_year"][:10]
    for s in auto_samples:
        summary_lines.append(
            f"  {s['proposed_pub_year']}  "
            f"[{s['source_file'][:50]:50s}]  "
            f"years={s['candidate_years_found'][:40]}"
        )

    summary_lines.append("")
    summary_lines.append("Samples (first 10 NO_MATCH rows)")
    summary_lines.append("=" * 70)
    nm_samples = [r for r in out_rows if r["source_rule"] == ""][:10]
    for s in nm_samples:
        summary_lines.append(
            f"  [{s['source_file'][:50]:50s}]  "
            f"reason={s['notes']}"
        )

    summary_text = "\n".join(summary_lines)
    out_txt.write_text(summary_text + "\n", encoding="utf-8")

    print()
    print(summary_text)
    print()
    print(f"Wrote: {out_csv}  ({len(out_rows)} rows)")
    print(f"Wrote: {out_txt}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
