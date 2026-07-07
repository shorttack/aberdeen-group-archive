#!/usr/bin/env python3
"""
apply_tech_mislabel_v1.py — Phase A of the 2026-07-07 master-CSV cleanse.

Reads tech_mislabel_candidates_v1.csv and applies MERGE_INTO dispositions to:
  1. _master_technologies.csv — delete alias rows, concat notes into canonical rows
  2. _master_tech_studies.csv — rewrite alias tech_ids to canonical, dedupe pairs

Invariants:
  - Dry-run default; --commit required to write.
  - Timestamped .bak backup per master before write; csv.QUOTE_ALL.
  - Audit trail written to tech_mislabel_apply_v1_applied_<utc>.txt.
  - Row-count assertions printed for both files.
  - Notes merged with `\n---\n` delimiter (Pete's Q4 lock).
  - Non-notes canonical fields NEVER overwritten (canonical row's metadata wins).

Usage:
  python3 apply_tech_mislabel_v1.py                                # dry-run
  python3 apply_tech_mislabel_v1.py --commit                       # write
  python3 apply_tech_mislabel_v1.py --archive PATH --candidates PATH
"""
import argparse
import csv
import datetime as _dt
import shutil
import sys
from pathlib import Path

DEFAULT_ARCHIVE = Path.home() / "Desktop/Archive/aberdeen-group-archive"
DEFAULT_CANDIDATES = Path.home() / "Desktop/Archive/tech_mislabel_candidates_v1.csv"
NOTES_DELIM = "\n---\n"


def utc_stamp() -> str:
    return _dt.datetime.now(_dt.UTC).strftime("%Y%m%dT%H%M%SZ")


def read_candidates(path: Path) -> list:
    rows = []
    with open(path, newline="") as f:
        for r in csv.DictReader(f):
            if r["disposition"] == "MERGE_INTO":
                rows.append(r)
    return rows


def main(argv):
    p = argparse.ArgumentParser()
    p.add_argument("--archive", default=str(DEFAULT_ARCHIVE))
    p.add_argument("--candidates", default=str(DEFAULT_CANDIDATES))
    p.add_argument("--commit", action="store_true")
    args = p.parse_args(argv[1:])

    archive = Path(args.archive).expanduser()
    candidates = Path(args.candidates).expanduser()
    tech_master = archive / "_master_technologies.csv"
    tech_join = archive / "_master_tech_studies.csv"

    if not tech_master.exists():
        sys.exit(f"ERROR: {tech_master} not found")
    if not tech_join.exists():
        sys.exit(f"ERROR: {tech_join} not found")
    if not candidates.exists():
        sys.exit(f"ERROR: {candidates} not found")

    cands = read_candidates(candidates)
    print(f"Mode: {'COMMIT' if args.commit else 'DRY-RUN'}")
    print(f"Candidates: {candidates}")
    print(f"MERGE_INTO rows to apply: {len(cands)}")
    for c in cands:
        print(f"  {c['alias_tech_id']:32s} -> {c['canonical_tech_id']}")

    # --- Read tech master
    with open(tech_master, newline="") as f:
        tech_reader = csv.reader(f)
        tech_header = next(tech_reader)
        tech_rows = list(tech_reader)
    idx = {col: i for i, col in enumerate(tech_header)}
    for req in ("tech_id", "tech_name", "notes"):
        if req not in idx:
            sys.exit(f"ERROR: _master_technologies.csv missing column '{req}'")

    tech_master_pre = len(tech_rows)

    # Build alias -> canonical map + concat notes into canonical
    alias_to_canonical = {c["alias_tech_id"]: c["canonical_tech_id"] for c in cands}

    # Group alias rows so we can concat their notes into the canonical row
    canonical_note_additions = {}  # canonical_tech_id -> [note_str, ...]
    for row in tech_rows:
        tid = row[idx["tech_id"]]
        if tid in alias_to_canonical:
            can_id = alias_to_canonical[tid]
            alias_note = row[idx["notes"]].strip()
            if alias_note:
                canonical_note_additions.setdefault(can_id, []).append(
                    f"[merged from {tid}] {alias_note}"
                )

    # Rebuild tech master: drop alias rows, append notes to canonical rows
    new_tech_rows = []
    canonicals_seen = set()
    for row in tech_rows:
        tid = row[idx["tech_id"]]
        if tid in alias_to_canonical:
            continue  # drop
        # If this is a canonical target, augment notes
        if tid in canonical_note_additions and tid not in canonicals_seen:
            existing_notes = row[idx["notes"]].strip()
            new_notes_parts = [existing_notes] if existing_notes else []
            new_notes_parts.extend(canonical_note_additions[tid])
            row = list(row)  # copy
            row[idx["notes"]] = NOTES_DELIM.join(new_notes_parts)
            canonicals_seen.add(tid)
        new_tech_rows.append(row)

    tech_master_post = len(new_tech_rows)

    # Verify all canonicals were found (else we'd silently lose merged notes)
    missing_canonicals = set(canonical_note_additions.keys()) - canonicals_seen
    # canonicals_seen only tracks those with note additions; canonicals with no
    # alias-side notes to add still count as "found" if they exist in the master.
    # Check the full canonical set:
    canonical_ids_present = {row[idx["tech_id"]] for row in new_tech_rows}
    for c in cands:
        if c["canonical_tech_id"] not in canonical_ids_present:
            print(f"  🔴 ERROR: canonical tech_id '{c['canonical_tech_id']}' does not exist in _master_technologies.csv")
            sys.exit(2)

    # --- Read tech join table
    with open(tech_join, newline="") as f:
        join_reader = csv.reader(f)
        join_header = next(join_reader)
        join_rows = list(join_reader)
    j_idx = {col: i for i, col in enumerate(join_header)}
    if "tech_id" not in j_idx or "study_id" not in j_idx:
        sys.exit(f"ERROR: _master_tech_studies.csv missing tech_id or study_id")

    join_pre = len(join_rows)

    # Rewrite alias -> canonical in join table
    rewrites = 0
    rewritten_rows = []
    for row in join_rows:
        tid = row[j_idx["tech_id"]]
        if tid in alias_to_canonical:
            row = list(row)
            row[j_idx["tech_id"]] = alias_to_canonical[tid]
            rewrites += 1
        rewritten_rows.append(row)

    # Dedup on (tech_id, study_id)
    seen = set()
    dedup_rows = []
    for row in rewritten_rows:
        key = (row[j_idx["tech_id"]], row[j_idx["study_id"]])
        if key in seen:
            continue
        seen.add(key)
        dedup_rows.append(row)
    join_post = len(dedup_rows)

    # --- Print summary
    print()
    print("=== Row-count summary ===")
    print(f"_master_technologies.csv:  {tech_master_pre} -> {tech_master_post} (Δ {tech_master_post - tech_master_pre})")
    print(f"  expected: Δ = -{len(cands)} (one deletion per alias)")
    print(f"_master_tech_studies.csv:  {join_pre} -> {join_post} (Δ {join_post - join_pre})")
    print(f"  rewrites: {rewrites}   dedup delta: {join_pre - rewrites - join_post + rewrites} (should be 0 unless studies had both alias + canonical)")

    if tech_master_post - tech_master_pre != -len(cands):
        print(f"  🔴 ERROR: unexpected row-count delta on _master_technologies.csv (expected {-len(cands)}, got {tech_master_post - tech_master_pre})")
        sys.exit(2)

    if not args.commit:
        print()
        print("DRY-RUN — no files written. Re-run with --commit to apply.")
        return 0

    # --- Backup + write
    stamp = utc_stamp()
    bak_master = tech_master.with_suffix(f".csv.bak_phase_a_tech_mislabel_{stamp}")
    bak_join = tech_join.with_suffix(f".csv.bak_phase_a_tech_mislabel_{stamp}")
    shutil.copy2(tech_master, bak_master)
    shutil.copy2(tech_join, bak_join)
    print(f"Backups: {bak_master.name}, {bak_join.name}")

    with open(tech_master, "w", newline="") as f:
        w = csv.writer(f, quoting=csv.QUOTE_ALL)
        w.writerow(tech_header)
        w.writerows(new_tech_rows)
    with open(tech_join, "w", newline="") as f:
        w = csv.writer(f, quoting=csv.QUOTE_ALL)
        w.writerow(join_header)
        w.writerows(dedup_rows)
    print(f"Wrote: {tech_master}")
    print(f"Wrote: {tech_join}")

    # --- Audit trail
    audit = archive / f"tech_mislabel_apply_v1_applied_{stamp}.txt"
    with open(audit, "w") as f:
        f.write(f"Phase A — tech mislabel apply\n")
        f.write(f"Timestamp: {stamp}\n")
        f.write(f"Candidates: {candidates}\n\n")
        f.write(f"_master_technologies.csv: {tech_master_pre} -> {tech_master_post}\n")
        f.write(f"_master_tech_studies.csv: {join_pre} -> {join_post} (rewrites={rewrites})\n\n")
        f.write("Merges applied:\n")
        for c in cands:
            f.write(f"  {c['alias_tech_id']} -> {c['canonical_tech_id']}\n")
    print(f"Audit: {audit}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
