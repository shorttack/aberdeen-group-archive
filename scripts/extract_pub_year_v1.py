#!/usr/bin/env python3
"""
extract_pub_year_v1.py
======================

Fill missing pub_year values in v_studies (the Kastner Aberdeen Archive
materialization of _master_studies.csv).

Reads directly from the DuckDB database (read-only), applies 5 deterministic
passes in priority order, and emits a candidates CSV for Pete's review.

Where this script lives
-----------------------
On Pete's Mac:
    ~/Desktop/Archive/scripts/extract_pub_year_v1.py

In the archive repo (committed copy):
    shorttack/aberdeen-group-archive/scripts/extract_pub_year_v1.py

DB auto-detection
-----------------
The DuckDB lives in the wiki repo at:
    ~/Repos/kastner-aberdeen-wiki/db/kastner.duckdb

The script checks these locations in order:
    1. $KASTNER_WIKI_DB env var (full path to .duckdb file)
    2. ~/Repos/kastner-aberdeen-wiki/db/kastner.duckdb       (Pete's Mac)
    3. ~/Documents/kastner-aberdeen-wiki/db/kastner.duckdb   (alt location)

Override with --db /path/to/kastner.duckdb.

Passes
------
1. date_string                — regex 4-digit year in `date` field
2. filename_year_prefix       — `^YYYY[ _-]` in source_file
3. filename_qcode             — `NqYY` quarter code → year
4. filename_mmddyy            — last 6 digits as MMDDYY → year
5. aberdeen_collateral_default — `aberdeen*` or known-collateral prefix → 2005,
                                 flagged needs_pete_review=true

Confidence policy
-----------------
- Passes 1–4: high confidence → auto-apply (needs_pete_review=false)
- Pass 5    : low confidence → needs_pete_review=true (default year 2005)
- No match  : emit row with proposed_pub_year=NULL, source_rule=NULL,
              needs_pete_review=true (hand disposition)

Outputs (written to --out-dir, default CWD)
-------------------------------------------
- pub_year_candidates_v1.csv  (all missing-year studies)
- pub_year_summary_v1.txt     (per-rule counts + sample rows)

Usage
-----
    # from anywhere, auto-detect wiki db; outputs land in CWD
    cd ~/Desktop/Archive
    python3 scripts/extract_pub_year_v1.py

    # explicit db path
    python3 scripts/extract_pub_year_v1.py --db ~/Repos/kastner-aberdeen-wiki/db/kastner.duckdb

    # write outputs elsewhere
    python3 scripts/extract_pub_year_v1.py --out-dir /tmp/pub_year_review

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

# duckdb is imported lazily inside main() so this module can be unit-tested
# without the duckdb runtime installed (e.g. in the sandbox).


# ---------------------------------------------------------------------------
# Config
# ---------------------------------------------------------------------------

OUT_CANDIDATES = "pub_year_candidates_v1.csv"
OUT_SUMMARY = "pub_year_summary_v1.txt"

YEAR_MIN = 1970   # Aberdeen Group founded 1970; earliest plausible year
YEAR_MAX = 2026   # current year ceiling

ABERDEEN_COLLATERAL_DEFAULT = 2005  # midpoint of 2004-2007 ingestion period

# Known corporate-collateral prefixes that lived in the 2004-2007 ingestion
# batch (per Pete's note). All lowercase; matched as prefix on lowercased
# basename. Anything not in this list does NOT get the default.
ABERDEEN_COLLATERAL_PREFIXES = (
    "aberdeen",
    "about_aberdeen",
)


# ---------------------------------------------------------------------------
# Regex patterns (compiled once)
# ---------------------------------------------------------------------------

RE_4DIGIT_YEAR_IN_DATE = re.compile(r"\b((?:19|20)\d{2})\b")
RE_FILENAME_YEAR_PREFIX = re.compile(r"^((?:19|20)\d{2})[ _\-]")
RE_FILENAME_QCODE = re.compile(r"(?<![0-9])([1-4])q(\d{2})(?![0-9])", re.IGNORECASE)
RE_FILENAME_MMDDYY = re.compile(r"(?<![0-9])(\d{2})(\d{2})(\d{2})(?![0-9])")


# ---------------------------------------------------------------------------
# DB path discovery
# ---------------------------------------------------------------------------

def find_db_path(explicit: str | None) -> Path | None:
    """Locate kastner.duckdb. Returns Path or None."""
    if explicit:
        p = Path(explicit).expanduser().resolve()
        return p if p.exists() else None

    env = os.environ.get("KASTNER_WIKI_DB")
    if env:
        p = Path(env).expanduser().resolve()
        if p.exists():
            return p

    home = Path.home()
    candidates = [
        home / "Repos" / "kastner-aberdeen-wiki" / "db" / "kastner.duckdb",
        home / "Documents" / "kastner-aberdeen-wiki" / "db" / "kastner.duckdb",
    ]
    for c in candidates:
        if c.exists():
            return c.resolve()
    return None


# ---------------------------------------------------------------------------
# Extraction passes
# ---------------------------------------------------------------------------

def _year_in_range(y: int) -> bool:
    return YEAR_MIN <= y <= YEAR_MAX


def pass1_date_string(row: dict) -> int | None:
    """Parse 4-digit year from the `date` field."""
    d = (row.get("date") or "").strip()
    if not d:
        return None
    matches = RE_4DIGIT_YEAR_IN_DATE.findall(d)
    if not matches:
        return None
    years = [int(m) for m in matches if _year_in_range(int(m))]
    if not years:
        return None
    # If date contains an ambiguous range marker (~) and multiple distinct
    # years, skip — too uncertain.
    if "~" in d and len(set(years)) > 1:
        return None
    # Publication year = earliest mentioned (e.g. "2004-2005" -> 2004)
    return min(years)


def pass2_filename_year_prefix(row: dict) -> int | None:
    """`^YYYY[ _-]` at start of source_file basename."""
    sf = row.get("source_file") or ""
    basename = os.path.basename(sf)
    m = RE_FILENAME_YEAR_PREFIX.match(basename)
    if not m:
        return None
    y = int(m.group(1))
    return y if _year_in_range(y) else None


def pass3_filename_qcode(row: dict) -> int | None:
    """Quarter code NqYY → year. 70-99 → 19xx, 00-26 → 20xx."""
    sf = row.get("source_file") or ""
    basename = os.path.basename(sf)
    m = RE_FILENAME_QCODE.search(basename)
    if not m:
        return None
    yy = int(m.group(2))
    if 70 <= yy <= 99:
        y = 1900 + yy
    elif 0 <= yy <= 26:
        y = 2000 + yy
    else:
        return None
    return y if _year_in_range(y) else None


def pass4_filename_mmddyy(row: dict) -> int | None:
    """Last plausible MMDDYY 6-digit run in filename → year.

    Validation: MM in 1-12, DD in 1-31. Picks the last match (typically the
    date suffix on Aberdeen DTP filenames like `012705a`).
    """
    sf = row.get("source_file") or ""
    basename = os.path.basename(sf)
    candidates = []
    for m in RE_FILENAME_MMDDYY.finditer(basename):
        mm, dd, yy = int(m.group(1)), int(m.group(2)), int(m.group(3))
        if not (1 <= mm <= 12):
            continue
        if not (1 <= dd <= 31):
            continue
        if 70 <= yy <= 99:
            y = 1900 + yy
        elif 0 <= yy <= 26:
            y = 2000 + yy
        else:
            continue
        if _year_in_range(y):
            candidates.append(y)
    if not candidates:
        return None
    return candidates[-1]


def pass5_aberdeen_collateral_default(row: dict) -> int | None:
    """Aberdeen corporate collateral default → 2005 (midpoint of 2004-2007)."""
    sf = row.get("source_file") or ""
    basename = os.path.basename(sf).lower()
    for prefix in ABERDEEN_COLLATERAL_PREFIXES:
        if basename.startswith(prefix):
            return ABERDEEN_COLLATERAL_DEFAULT
    return None


# Ordered pipeline. (name, fn, auto_apply)
PASSES = [
    ("date_string",                  pass1_date_string,                  True),
    ("filename_year_prefix",         pass2_filename_year_prefix,         True),
    ("filename_qcode",               pass3_filename_qcode,               True),
    ("filename_mmddyy",              pass4_filename_mmddyy,              True),
    ("aberdeen_collateral_default",  pass5_aberdeen_collateral_default,  False),
]


def extract(row: dict) -> tuple[int | None, str | None, bool]:
    """Run passes in order, return (year, rule_name, auto_apply)."""
    for name, fn, auto in PASSES:
        y = fn(row)
        if y is not None:
            return y, name, auto
    return None, None, False


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main() -> int:
    ap = argparse.ArgumentParser(
        description="Extract pub_year candidates for studies with NULL pub_year"
    )
    ap.add_argument(
        "--db",
        help="Path to kastner.duckdb (default: auto-detect wiki repo location)",
    )
    ap.add_argument(
        "--out-dir",
        default=".",
        help="Directory to write candidates CSV + summary (default: CWD)",
    )
    args = ap.parse_args()

    db_path = find_db_path(args.db)
    if db_path is None:
        print("ERROR: could not locate kastner.duckdb.", file=sys.stderr)
        print("Tried:", file=sys.stderr)
        print("  $KASTNER_WIKI_DB", file=sys.stderr)
        print("  ~/Repos/kastner-aberdeen-wiki/db/kastner.duckdb", file=sys.stderr)
        print("  ~/Documents/kastner-aberdeen-wiki/db/kastner.duckdb", file=sys.stderr)
        print("Pass --db /path/to/kastner.duckdb to override.", file=sys.stderr)
        return 2

    out_dir = Path(args.out_dir).expanduser().resolve()
    out_dir.mkdir(parents=True, exist_ok=True)
    out_csv = out_dir / OUT_CANDIDATES
    out_txt = out_dir / OUT_SUMMARY

    try:
        import duckdb
    except ImportError:
        print("ERROR: duckdb python module not installed.", file=sys.stderr)
        print("Install with: pip3 install duckdb", file=sys.stderr)
        return 2

    print(f"DB:       {db_path}")
    print(f"Out dir:  {out_dir}")

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

    print(f"Loaded {len(rows)} studies with NULL pub_year from v_studies")

    rule_counts: Counter[str] = Counter()
    auto_count = 0
    review_count = 0
    no_match_count = 0

    out_rows = []
    for r in rows:
        d = dict(zip(cols, r))
        year, rule, auto = extract(d)

        if year is None:
            rule_counts["NO_MATCH"] += 1
            no_match_count += 1
            needs_review = True
        else:
            rule_counts[rule] += 1
            if auto:
                auto_count += 1
                needs_review = False
            else:
                review_count += 1
                needs_review = True

        out_rows.append({
            "study_id":          d["study_id"],
            "proposed_pub_year": year if year is not None else "",
            "source_rule":       rule or "",
            "needs_pete_review": "true" if needs_review else "false",
            "source_file":       d["source_file"] or "",
            "date_field":        d["date"] or "",
            "title":             (d["title"] or "")[:120],
        })

    fieldnames = [
        "study_id", "proposed_pub_year", "source_rule",
        "needs_pete_review", "source_file", "date_field", "title",
    ]
    with open(out_csv, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fieldnames)
        w.writeheader()
        w.writerows(out_rows)

    summary_lines = []
    summary_lines.append("=" * 70)
    summary_lines.append("pub_year extraction summary — extract_pub_year_v1.py")
    summary_lines.append(f"Run at: {datetime.now().isoformat()}")
    summary_lines.append(f"DB:     {db_path}")
    summary_lines.append("=" * 70)
    summary_lines.append(f"Total studies with NULL pub_year:  {len(rows)}")
    summary_lines.append(f"Auto-apply (passes 1-4):           {auto_count}")
    summary_lines.append(f"Needs review (pass 5 default):     {review_count}")
    summary_lines.append(f"No match (hand disposition):       {no_match_count}")
    summary_lines.append("")
    summary_lines.append("Per-rule breakdown:")
    for rule, _, _ in PASSES:
        summary_lines.append(f"  {rule:35s} {rule_counts.get(rule, 0):4d}")
    summary_lines.append(f"  {'NO_MATCH':35s} {rule_counts.get('NO_MATCH', 0):4d}")
    summary_lines.append("")

    summary_lines.append("=" * 70)
    summary_lines.append("Samples per rule (up to 5 each)")
    summary_lines.append("=" * 70)
    for rule, _, _ in PASSES:
        samples = [r for r in out_rows if r["source_rule"] == rule][:5]
        if not samples:
            continue
        summary_lines.append(f"\n--- {rule} ---")
        for s in samples:
            summary_lines.append(
                f"  {s['proposed_pub_year']}  "
                f"[{s['source_file'][:55]:55s}]  "
                f"date={s['date_field'][:20]}"
            )
    no_match_samples = [r for r in out_rows if r["source_rule"] == ""][:10]
    if no_match_samples:
        summary_lines.append("\n--- NO_MATCH (first 10) ---")
        for s in no_match_samples:
            summary_lines.append(
                f"  [{s['source_file'][:55]:55s}]  "
                f"date={s['date_field'][:20]}"
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
