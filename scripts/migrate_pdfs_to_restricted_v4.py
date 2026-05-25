#!/usr/bin/env python3
"""
migrate_pdfs_to_restricted_v4.py
=================================
v4 — final exclude list locked, ready for real run.

Changes from v3
---------------
* **EXCLUDE_PATH_PREFIXES** locked per Pete's decisions:
  * `kastner-author/memoirs/`        — Pete's photos & memorabilia, stay public
  * `kastner-author/employer/aberdeen-group/categories-created/` — Pete-authored category notes, stay public
  * `submissions/`                   — work-in-progress (IEEE preprint etc.), stay public
* Oracle-Ellison-and-PSK-7.pdf was MOVED into `memoirs/photos/` in
  a prior commit (62c50c1), so it's now caught by the memoirs/ exclude.
* Year=2025 (PSA) and year=2026 (IEEE) edge cases are now excluded
  by the new prefixes, so no defensive year-guard needed.

Expected output
---------------
~142 PDFs migrate (148 − 2 PSA − 1 IEEE − 2 memoirs − 1 Oracle-Ellison)

Source / target layout — unchanged from v3:
  /Users/scott/Desktop/Archive/aberdeen-group-archive/  (public clone)
    →  /Users/scott/Desktop/kastner-restricted-sources/pdfs/<year>/<flat>.pdf

Manifest: migration_manifest_v4.csv (QUOTE_ALL per §16.5)

Usage
-----
    python3 /Users/scott/Desktop/Archive/scripts/migrate_pdfs_to_restricted_v4.py --dry-run
    python3 /Users/scott/Desktop/Archive/scripts/migrate_pdfs_to_restricted_v4.py

Version
-------
v4 — final exclude list locked, QUOTE_ALL manifest
v3 — sourced from public-repo clone
v2 — autodetect masters + downloads
v1 — initial cut
"""

import argparse
import csv
import re
import shutil
import sys
from collections import Counter
from pathlib import Path

YEAR_RE = re.compile(r"\b(19[6-9]\d|20[0-2]\d)\b")
PATH_YEAR_RE = re.compile(r"(?:^|[/_-])(19[6-9]\d|20[0-2]\d)(?:[-_/]|$)")
PDF_EXT = {".pdf", ".PDF"}

# Paths inside the public clone we should NOT migrate (relative to clone root)
EXCLUDE_DIR_NAMES = {".git", "scripts", "Kastner Memoir"}
EXCLUDE_PATH_PREFIXES = (
    "kastner-author/memoirs/",
    "kastner-author/employer/aberdeen-group/categories-created/",
    "submissions/",
)


def load_study_years(masters_csv: Path) -> dict[str, str]:
    out: dict[str, str] = {}
    if not masters_csv.is_file():
        return out
    with masters_csv.open(newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            sid = (row.get("study_id") or "").strip()
            date = (row.get("date") or "").strip()
            year = "unknown"
            if date:
                m = re.search(r"(19[6-9]\d|20[0-2]\d)", date)
                if m:
                    year = m.group(1)
            if sid:
                out[sid] = year
    return out


def year_from_path(rel_path: Path) -> str | None:
    years: list[str] = []
    for seg in rel_path.parts:
        m = PATH_YEAR_RE.search(seg)
        if m:
            years.append(m.group(1))
    if not years:
        return None
    return min(years)


def year_from_filename(name: str) -> str | None:
    hits = YEAR_RE.findall(name)
    return min(hits) if hits else None


def resolve_year(
    rel_path: Path, study_years: dict[str, str]
) -> tuple[str, str]:
    y = year_from_path(rel_path)
    if y:
        return y, "path"
    if len(rel_path.parts) >= 2:
        for candidate in (rel_path.parts[-2],
                          rel_path.parts[-3] if len(rel_path.parts) >= 3 else ""):
            if candidate in study_years:
                yr = study_years[candidate]
                if yr != "unknown":
                    return yr, f"masters:{candidate}"
    y = year_from_filename(rel_path.name)
    if y:
        return y, "filename"
    return "unknown", "none"


def flatten_rel_path(rel_path: Path) -> str:
    return "__".join(rel_path.parts)


def is_excluded(rel_path: Path) -> tuple[bool, str]:
    """Return (excluded, reason)."""
    parts = rel_path.parts
    for ex in EXCLUDE_DIR_NAMES:
        if ex in parts:
            return True, f"dir:{ex}"
    rel_str = str(rel_path).replace("\\", "/")
    for pfx in EXCLUDE_PATH_PREFIXES:
        if rel_str.startswith(pfx):
            return True, f"prefix:{pfx}"
    return False, ""


def iter_source_pdfs(
    public_clone: Path,
) -> tuple[list[Path], list[tuple[Path, str]]]:
    """Return (kept, excluded_with_reason)."""
    kept: list[Path] = []
    excluded: list[tuple[Path, str]] = []
    for p in public_clone.rglob("*"):
        if not p.is_file() or p.suffix not in PDF_EXT:
            continue
        try:
            rel = p.relative_to(public_clone)
        except ValueError:
            continue
        excl, reason = is_excluded(rel)
        if excl:
            excluded.append((rel, reason))
        else:
            kept.append(p)
    return kept, excluded


def copy_with_idempotency(src: Path, dest: Path, dry_run: bool) -> str:
    if dest.exists():
        if dest.stat().st_size == src.stat().st_size:
            return "skipped_exists"
        v2 = dest.with_name(dest.stem + "_v2" + dest.suffix)
        if dry_run:
            return f"would_copy_v2:{v2.name}"
        v2.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(src, v2)
        return f"copied_v2:{v2.name}"
    if dry_run:
        return "would_copy"
    dest.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(src, dest)
    return "copied"


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[1])
    ap.add_argument("--public-clone", type=Path,
                    default=Path("/Users/scott/Desktop/Archive/aberdeen-group-archive"))
    ap.add_argument("--private-clone", type=Path,
                    default=Path("/Users/scott/Desktop/kastner-restricted-sources"))
    ap.add_argument("--masters", type=Path, default=None)
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    if not args.public_clone.is_dir():
        print(f"ERROR: public clone not found: {args.public_clone}", file=sys.stderr)
        return 2
    if not args.private_clone.is_dir():
        print(f"ERROR: private clone not found: {args.private_clone}", file=sys.stderr)
        return 2

    # Masters
    if args.masters:
        masters_csv = args.masters
    else:
        for cand in [
            args.public_clone / "_master_studies.csv",
            Path("/Users/scott/Desktop/Archive/archive_masters/_master_studies.csv"),
        ]:
            if cand.is_file():
                masters_csv = cand
                break
        else:
            masters_csv = None
    if masters_csv and masters_csv.is_file():
        study_years = load_study_years(masters_csv)
        print(f"Masters: {masters_csv}")
        print(f"  Loaded {len(study_years):,} study→year mappings")
    else:
        study_years = {}
        print("Masters: not found")

    # Enumerate
    kept, excluded = iter_source_pdfs(args.public_clone)
    print(f"\nFound {len(kept):,} PDFs to migrate "
          f"({len(excluded):,} excluded)")
    if excluded:
        print("\nExcluded:")
        for rel, reason in excluded:
            print(f"  [{reason:>30}] {rel}")

    # Plan + copy
    actions: Counter = Counter()
    year_dist: Counter = Counter()
    reason_dist: Counter = Counter()
    rows: list[dict] = []
    unmapped: list[dict] = []

    for src in kept:
        rel = src.relative_to(args.public_clone)
        year, reason = resolve_year(rel, study_years)
        flat = flatten_rel_path(rel)
        dest = args.private_clone / "pdfs" / year / flat
        action = copy_with_idempotency(src, dest, args.dry_run)
        actions[action] += 1
        year_dist[year] += 1
        reason_dist[reason] += 1

        row = {
            "source_repo_path": str(rel),
            "dest_path": str(dest.relative_to(args.private_clone)),
            "year": year,
            "year_source": reason,
            "size_bytes": src.stat().st_size,
            "action": action,
        }
        rows.append(row)
        if year == "unknown":
            unmapped.append(row)

    manifest = args.private_clone / "migration_manifest_v4.csv"
    unmapped_path = args.private_clone / "unmapped_v4.csv"

    if not args.dry_run and rows:
        fieldnames = ["source_repo_path", "dest_path", "year", "year_source",
                      "size_bytes", "action"]
        with manifest.open("w", newline="", encoding="utf-8") as f:
            w = csv.DictWriter(f, fieldnames=fieldnames, quoting=csv.QUOTE_ALL)
            w.writeheader()
            w.writerows(rows)
        print(f"\nManifest: {manifest}  ({len(rows):,} rows)")
        if unmapped:
            with unmapped_path.open("w", newline="", encoding="utf-8") as f:
                w = csv.DictWriter(f, fieldnames=fieldnames, quoting=csv.QUOTE_ALL)
                w.writeheader()
                w.writerows(unmapped)
            print(f"Unmapped: {unmapped_path}  ({len(unmapped):,} rows)")

    print(f"\nActions: {dict(actions)}")
    print(f"Year resolution: {dict(reason_dist)}")
    print(f"\nYear distribution:")
    for year in sorted(year_dist.keys()):
        print(f"  {year}: {year_dist[year]}")

    total_bytes = sum(r["size_bytes"] for r in rows)
    print(f"\nTotal: {len(rows):,} PDFs, {total_bytes/(1024*1024):.1f} MB")

    if args.dry_run:
        print("\nDRY RUN — no files copied. Re-run without --dry-run to apply.")
    else:
        print("\nDone. Source PDFs in public repo unchanged.")
        print("\nNext steps:")
        print(f"  cd {args.private_clone}")
        print("  git add pdfs/ migration_manifest_v4.csv")
        print("  git commit -m 'Initial PDF migration from public repo (142 PDFs)'")
        print("  git push")
    return 0


if __name__ == "__main__":
    sys.exit(main())
