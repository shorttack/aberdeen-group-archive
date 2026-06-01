#!/usr/bin/env python3
"""
migrate_pdfs_to_restricted_v3.py
=================================
v3 — source is the LOCAL CLONE of shorttack/aberdeen-group-archive,
not /Archive/prepared/.

Why v3 exists
-------------
The 148 source PDFs we want to migrate to the private repo are
currently committed to the PUBLIC repo at paths like:
  kastner-author/1988-encore-oltp-market-tps-needs-deee45/source/original.pdf
  Project Examples/Sun AS-400/.../source/<filename>.pdf

This script copies those PDFs from the public-repo clone into the
private-repo clone, organized by year, then writes a manifest.

It does NOT delete anything from the public repo. That happens in a
separate, explicit step after you verify the private repo has all 148.

Year resolution (in priority order)
-----------------------------------
1. **Path prefix**: paths like `kastner-author/1988-encore-...` or
   `kastner-author/dct/dct-gateway-acquires-emachines-2004-03/...`
   contain a YYYY at the start of a study-dir segment.
2. **Study masters lookup**: parent dir name is a study_id → look up
   `_master_studies.date`.
3. **Filename year**: earliest YYYY in the PDF filename.
4. **Fallback**: `unknown` directory.

Target layout in shorttack/kastner-restricted-sources (local clone)
-------------------------------------------------------------------
    pdfs/
      <year>/
        <flattened_path>__<filename>.pdf
    migration_manifest_v3.csv
    unmapped_v3.csv

Flattened path encodes the original location so we can audit:
  kastner-author/1988-encore-... → kastner-author__1988-encore-...

Idempotency
-----------
* If dest exists and size matches → action=skipped_exists
* If dest exists and size differs → write `<name>_v2.pdf` (forever-archive)

Usage
-----
    # Default paths (uses repo clones in expected locations)
    python3 /Users/scott/Desktop/Archive/scripts/migrate_pdfs_to_restricted_v3.py --dry-run

    # Real run
    python3 /Users/scott/Desktop/Archive/scripts/migrate_pdfs_to_restricted_v3.py

Defaults
--------
  --public-clone   /Users/scott/Desktop/Archive/aberdeen-group-archive
  --private-clone  /Users/scott/Desktop/kastner-restricted-sources
  --masters        <public-clone>/_master_studies.csv  (preferred)
                   else /Users/scott/Desktop/Archive/archive_masters/_master_studies.csv

Version
-------
v3 — sources from public-repo clone instead of /Archive/prepared/
v2 — autodetect masters + downloads
v1 — initial cut
"""

import argparse
import csv
import hashlib
import re
import shutil
import sys
from collections import Counter
from pathlib import Path

YEAR_RE = re.compile(r"\b(19[6-9]\d|20[0-2]\d)\b")
# Year embedded in path segment, e.g. "1988-encore-..." or "dct-gateway-acquires-emachines-2004-03"
PATH_YEAR_RE = re.compile(r"(?:^|[/_-])(19[6-9]\d|20[0-2]\d)(?:[-_/]|$)")
PDF_EXT = {".pdf", ".PDF"}

# Paths inside the public clone we should NOT migrate
EXCLUDE_PATTERNS = {
    ".git",
    "scripts",
    "Kastner Memoir",  # epub, not aberdeen sources
}


def sha256_file(p: Path, chunk: int = 1 << 20) -> str:
    h = hashlib.sha256()
    with p.open("rb") as f:
        while True:
            b = f.read(chunk)
            if not b:
                break
            h.update(b)
    return h.hexdigest()


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
    """Look for YYYY in each path segment. Earliest wins."""
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
    if not hits:
        return None
    return min(hits)


def resolve_year(
    rel_path: Path, study_years: dict[str, str]
) -> tuple[str, str]:
    """Return (year, source_reason)."""
    # 1. Path prefix
    y = year_from_path(rel_path)
    if y:
        return y, "path"
    # 2. Masters lookup via parent dir
    if len(rel_path.parts) >= 2:
        # Try the second-to-last segment (the study dir), then the
        # last directory before the file.
        for candidate in (rel_path.parts[-2], rel_path.parts[-3] if len(rel_path.parts) >= 3 else ""):
            if candidate in study_years:
                yr = study_years[candidate]
                if yr != "unknown":
                    return yr, f"masters:{candidate}"
    # 3. Filename
    y = year_from_filename(rel_path.name)
    if y:
        return y, "filename"
    return "unknown", "none"


def flatten_rel_path(rel_path: Path) -> str:
    """Turn 'kastner-author/1988-encore-.../source/original.pdf' into
    'kastner-author__1988-encore-...__source__original.pdf' so dest
    filenames are unique even if many studies have 'original.pdf'."""
    parts = list(rel_path.parts)
    return "__".join(parts)


def iter_source_pdfs(public_clone: Path) -> list[Path]:
    out: list[Path] = []
    for p in public_clone.rglob("*"):
        if not p.is_file() or p.suffix not in PDF_EXT:
            continue
        try:
            rel = p.relative_to(public_clone)
        except ValueError:
            continue
        if any(part in EXCLUDE_PATTERNS for part in rel.parts):
            continue
        out.append(p)
    return out


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
    ap.add_argument("--masters", type=Path, default=None,
                    help="Override masters CSV path")
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    # --- Validate paths ------------------------------------------------------
    if not args.public_clone.is_dir():
        print(f"ERROR: public clone not found: {args.public_clone}", file=sys.stderr)
        return 2
    if not args.private_clone.is_dir():
        print(f"ERROR: private clone not found: {args.private_clone}", file=sys.stderr)
        print("       git clone https://github.com/shorttack/kastner-restricted-sources.git first",
              file=sys.stderr)
        return 2

    # --- Resolve masters -----------------------------------------------------
    if args.masters:
        masters_csv = args.masters
    else:
        # Prefer the clone's masters (it's the same as archive_masters, just synced)
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
        print("Masters: not found (continuing with path/filename year resolution only)")

    # --- Enumerate source PDFs -----------------------------------------------
    pdfs = iter_source_pdfs(args.public_clone)
    print(f"\nFound {len(pdfs):,} PDFs in public clone (excluding .git/, scripts/, Kastner Memoir/)")

    # --- Plan + copy ---------------------------------------------------------
    actions: Counter = Counter()
    year_dist: Counter = Counter()
    reason_dist: Counter = Counter()
    rows: list[dict] = []
    unmapped: list[dict] = []

    for src in pdfs:
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

    # --- Write manifest ------------------------------------------------------
    manifest = args.private_clone / "migration_manifest_v3.csv"
    unmapped_path = args.private_clone / "unmapped_v3.csv"

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
        print("  git add pdfs/ migration_manifest_v3.csv unmapped_v3.csv")
        print("  git commit -m 'Initial PDF migration from public repo (148 PDFs)'")
        print("  git push")
        print("\nAFTER private push succeeds, separate step will remove PDFs from public repo.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
