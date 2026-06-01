#!/usr/bin/env python3
"""
extract_missing_dates_v3.py
============================
v3 — autodetect masters location.

Changes from v2
---------------
* **Masters autodetect**: tries multiple known paths and uses whichever
  has the newest _master_*.csv. Logs the choice. Same logic as
  migrate_pdfs_to_restricted_v2.py for consistency.
* `--masters-dir` flag overrides autodetect.

Behavior otherwise unchanged from v2: copyright-year anchor + fallback
to sentence-anchor proximity. Read-only. Two proposal CSVs.

Default install location (per Pete's standing rule)
---------------------------------------------------
    /Users/scott/Desktop/Archive/scripts/extract_missing_dates_v3.py

Output
------
Two CSVs in --out-dir:
  * proposed_year_observed_v3.csv
  * proposed_years_active_v3.csv

Confidence ladder
-----------------
  very_high — copyright-year anchor matched (near-ground-truth)
  high      — year appears in same sentence as anchor AND multiple times
  medium    — year appears in same sentence as anchor once
  low       — most-common year in doc, no anchor proximity
  none      — no year found, or source file missing

Usage
-----
    python3 /Users/scott/Desktop/Archive/scripts/extract_missing_dates_v3.py

Version
-------
v3 — masters autodetect.
v2 — copyright-year anchor.
v1 — initial cut.
"""

import argparse
import csv
import re
import sys
from collections import Counter
from pathlib import Path

YEAR_RE = re.compile(r"\b(19[6-9]\d|20[0-2]\d)\b")
SENTENCE_SPLIT_RE = re.compile(r"(?<=[.!?])\s+")

COPYRIGHT_RE = re.compile(
    r"(?:copyright|©|\(c\))\s*(?:©\s*)?(?P<year>19[6-9]\d|20[0-2]\d)"
    r"(?:\s*[-–]\s*(?:19[6-9]\d|20[0-2]\d))?"
    r"\s*(?:by\s+)?aberdeen",
    re.IGNORECASE,
)
COPYRIGHT_LOOSE_RE = re.compile(
    r"(?:copyright|©|\(c\))\s*(?P<year>19[6-9]\d|20[0-2]\d)",
    re.IGNORECASE,
)

MASTERS_CANDIDATES = [
    "archive_masters",
    "aberdeen-group-archive",
    "masters",
    "output/masters",
]


def autodetect_masters_dir(archive: Path) -> Path | None:
    """Return the directory containing _master_*.csv (not the CSV itself)."""
    found: list[tuple[float, Path]] = []
    for rel in MASTERS_CANDIDATES:
        candidate = archive / rel / "_master_observations.csv"
        if candidate.is_file():
            found.append((candidate.stat().st_mtime, candidate.parent))
    if not found:
        for p in archive.rglob("_master_observations.csv"):
            if "backup" in str(p).lower():
                continue
            try:
                rel = p.relative_to(archive)
                if len(rel.parts) > 4:
                    continue
            except ValueError:
                continue
            found.append((p.stat().st_mtime, p.parent))
    if not found:
        return None
    found.sort(reverse=True)
    return found[0][1]


def load_master(path: Path) -> tuple[list[str], list[dict]]:
    with path.open(newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        return reader.fieldnames or [], list(reader)


def find_text_file(archive: Path, study_id: str) -> Path | None:
    base = archive / "prepared" / study_id
    if not base.is_dir():
        return None
    candidates = [
        base / "source" / "original_text.md",
        base / "source" / "text.md",
        base / "source" / "text.txt",
    ]
    for c in candidates:
        if c.is_file():
            return c
    src = base / "source"
    if src.is_dir():
        for ext in ("*.md", "*.txt"):
            hits = sorted(src.glob(ext))
            if hits:
                return hits[0]
    return None


def detect_copyright_year(text: str) -> tuple[str | None, str]:
    tail = text[-5_000:] if len(text) > 5_000 else text
    m = COPYRIGHT_RE.search(tail)
    if m:
        start = max(0, m.start() - 40)
        end = min(len(tail), m.end() + 80)
        return m.group("year"), tail[start:end].strip().replace("\n", " ")
    m = COPYRIGHT_LOOSE_RE.search(tail)
    if m:
        start = max(0, m.start() - 40)
        end = min(len(tail), m.end() + 80)
        return m.group("year"), tail[start:end].strip().replace("\n", " ")
    return None, ""


def extract_year_candidates(
    text: str, anchor: str | None
) -> list[tuple[str, str, int]]:
    out: list[tuple[str, str, int]] = []
    anchor_low = anchor.lower() if anchor else None
    sample = text[:30_000]
    for sentence in SENTENCE_SPLIT_RE.split(sample):
        years = YEAR_RE.findall(sentence)
        if not years:
            continue
        score = 100 if (anchor_low and anchor_low in sentence.lower()) else 10
        for y in years:
            out.append((y, sentence.strip()[:200], score))
    agg: dict[str, dict] = {}
    for y, s, sc in out:
        if y not in agg:
            agg[y] = {"score": 0, "snippet": s, "count": 0}
        agg[y]["score"] += sc
        agg[y]["count"] += 1
        if sc > 10 and len(s) > len(agg[y].get("snippet", "")):
            agg[y]["snippet"] = s
    ranked = sorted(
        agg.items(), key=lambda kv: (kv[1]["score"], kv[1]["count"]), reverse=True
    )
    return [(y, d["snippet"], d["score"]) for y, d in ranked]


def confidence_label(
    cr_year: str | None, candidates: list[tuple[str, str, int]]
) -> str:
    if cr_year:
        return "very_high"
    if not candidates:
        return "none"
    top_score = candidates[0][2]
    if top_score >= 200:
        return "high"
    if top_score >= 100:
        return "medium"
    return "low"


class StudyCache:
    def __init__(self, archive: Path):
        self.archive = archive
        self._text: dict[str, str | None] = {}
        self._cr: dict[str, tuple[str | None, str]] = {}
        self._path: dict[str, Path | None] = {}

    def path(self, study_id: str) -> Path | None:
        if study_id not in self._path:
            self._path[study_id] = find_text_file(self.archive, study_id)
        return self._path[study_id]

    def text(self, study_id: str) -> str | None:
        if study_id not in self._text:
            p = self.path(study_id)
            self._text[study_id] = (
                p.read_text(encoding="utf-8", errors="ignore") if p else None
            )
        return self._text[study_id]

    def copyright_year(self, study_id: str) -> tuple[str | None, str]:
        if study_id not in self._cr:
            t = self.text(study_id)
            self._cr[study_id] = detect_copyright_year(t) if t else (None, "")
        return self._cr[study_id]


def process_rows(
    cache: StudyCache,
    rows: list[dict],
    target_col: str,
    id_col: str,
    extra_cols: list[str],
    anchor_col: str,
    out_path: Path,
) -> tuple[int, Counter]:
    conf_counts: Counter = Counter()
    written = 0
    fieldnames = (
        [id_col]
        + extra_cols
        + [
            "study_id",
            "current_value",
            "study_copyright_year",
            "candidate_1",
            "candidate_2",
            "candidate_3",
            "confidence",
            "evidence_snippet",
            "source_file",
        ]
    )
    with out_path.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fieldnames)
        w.writeheader()
        for row in rows:
            value = (row.get(target_col) or "").strip()
            if value:
                continue
            study_id = (row.get("study_id") or "").strip()
            if not study_id:
                continue
            cr_year, cr_snippet = cache.copyright_year(study_id)
            text = cache.text(study_id)
            anchor = (row.get(anchor_col) or "")[:80]
            fallback = extract_year_candidates(text, anchor) if text else []
            if cr_year:
                ranked_years = [cr_year]
                snippet = cr_snippet
                for y, _s, _sc in fallback:
                    if y != cr_year and y not in ranked_years:
                        ranked_years.append(y)
                    if len(ranked_years) >= 3:
                        break
                cands = ranked_years[:3]
            else:
                cands = [y for y, _s, _sc in fallback[:3]]
                snippet = fallback[0][1] if fallback else ""
            conf = confidence_label(cr_year, fallback)
            conf_counts[conf] += 1
            out_row = {
                id_col: row.get(id_col, ""),
                "study_id": study_id,
                "current_value": "",
                "study_copyright_year": cr_year or "",
                "candidate_1": cands[0] if len(cands) > 0 else "",
                "candidate_2": cands[1] if len(cands) > 1 else "",
                "candidate_3": cands[2] if len(cands) > 2 else "",
                "confidence": conf,
                "evidence_snippet": snippet,
                "source_file": str(cache.path(study_id) or ""),
            }
            for col in extra_cols:
                out_row[col] = row.get(col, "")
            w.writerow(out_row)
            written += 1
    return written, conf_counts


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[1])
    ap.add_argument("--archive", type=Path,
                    default=Path("/Users/scott/Desktop/Archive"))
    ap.add_argument("--masters-dir", type=Path, default=None,
                    help="Override masters directory (autodetect by default)")
    ap.add_argument("--out-dir", type=Path,
                    default=Path("/Users/scott/Desktop/Archive/v1.5_workspace"))
    ap.add_argument("--skip-observations", action="store_true")
    ap.add_argument("--skip-entities", action="store_true")
    args = ap.parse_args()

    if args.masters_dir:
        masters = args.masters_dir
        print(f"Masters dir (override): {masters}")
    else:
        masters = autodetect_masters_dir(args.archive)
        if masters:
            print(f"Masters dir (autodetected): {masters}")
        else:
            print(f"ERROR: No masters dir found under {args.archive}",
                  file=sys.stderr)
            return 2
    if not masters.is_dir():
        print(f"ERROR: masters dir is not a directory: {masters}",
              file=sys.stderr)
        return 2
    args.out_dir.mkdir(parents=True, exist_ok=True)

    cache = StudyCache(args.archive)

    if not args.skip_observations:
        obs_path = masters / "_master_observations.csv"
        print(f"\nLoading {obs_path}…")
        _, obs_rows = load_master(obs_path)
        print(f"  {len(obs_rows):,} observation rows")
        out = args.out_dir / "proposed_year_observed_v3.csv"
        n, conf = process_rows(
            cache, obs_rows,
            target_col="year_observed",
            id_col="obs_id",
            extra_cols=[],
            anchor_col="observation_text",
            out_path=out,
        )
        print(f"  wrote {n:,} proposals → {out}")
        print(f"  confidence: {dict(conf)}")

    if not args.skip_entities:
        ent_path = masters / "_master_entities.csv"
        print(f"\nLoading {ent_path}…")
        _, ent_rows = load_master(ent_path)
        print(f"  {len(ent_rows):,} entity rows")
        out = args.out_dir / "proposed_years_active_v3.csv"
        n, conf = process_rows(
            cache, ent_rows,
            target_col="years_active",
            id_col="entity_id",
            extra_cols=["entity_name"],
            anchor_col="entity_name",
            out_path=out,
        )
        print(f"  wrote {n:,} proposals → {out}")
        print(f"  confidence: {dict(conf)}")

    print("\nDone. Review CSVs before applying values back to masters.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
