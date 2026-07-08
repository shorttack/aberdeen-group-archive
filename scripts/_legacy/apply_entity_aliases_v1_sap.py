#!/usr/bin/env python3
"""
apply_entity_aliases_v1_sap.py — Phase C-narrow (SAP cluster only) of the
2026-07-07 master-CSV cleanse.

Reads entity_alias_map_v1_sap_only.csv and merges the SAP-family alias rows
into canonical survivor `sap-ag`. Keeps `sap-america`, `sap-america-utilities`,
and `paul-wahl-sap` as separate rows (per Pete's Q9).

Writes:
  1. _master_entities.csv  — deletes 5 alias rows, concat-merges notes into
                             sap-ag row; row count Δ = -5 (3293 -> 3288).
  2. _master_entity_studies.csv — rewrites 46 alias-side join rows to sap-ag;
                                  dedupes on (entity_id, study_id); expected
                                  dedup delta = 0 (per pre-flight probe).

Invariants:
  - MERGE_INTO alias rows are DELETED from entities master; their entity_id
    in the join table is REWRITTEN to canonical; notes are concat-merged via
    `\n---\n`.
  - CANONICAL_SURVIVOR row's metadata (entity_type, sector, status, successor,
    years_active) is preserved; only its notes are augmented.
  - KEEP_SEPARATE rows are untouched.
  - Timestamped .bak per file; csv.QUOTE_ALL; dry-run default.

Usage:
  python3 apply_entity_aliases_v1_sap.py                # dry-run
  python3 apply_entity_aliases_v1_sap.py --commit       # write
"""
import argparse
import csv
import datetime as _dt
import shutil
import sys
from pathlib import Path

DEFAULT_ARCHIVE = Path.home() / "Desktop/Archive/aberdeen-group-archive"
DEFAULT_CANDIDATES = Path.home() / "Desktop/Archive/entity_alias_map_v1_sap_only.csv"
NOTES_DELIM = "\n---\n"


def utc_stamp() -> str:
    return _dt.datetime.now(_dt.UTC).strftime("%Y%m%dT%H%M%SZ")


def main(argv):
    p = argparse.ArgumentParser()
    p.add_argument("--archive", default=str(DEFAULT_ARCHIVE))
    p.add_argument("--candidates", default=str(DEFAULT_CANDIDATES))
    p.add_argument("--commit", action="store_true")
    args = p.parse_args(argv[1:])

    archive = Path(args.archive).expanduser()
    candidates = Path(args.candidates).expanduser()
    ent_master = archive / "_master_entities.csv"
    ent_join = archive / "_master_entity_studies.csv"

    if not ent_master.exists(): sys.exit(f"ERROR: {ent_master} not found")
    if not ent_join.exists(): sys.exit(f"ERROR: {ent_join} not found")
    if not candidates.exists(): sys.exit(f"ERROR: {candidates} not found")

    # Parse candidates
    merges = []       # list of alias entity_ids to delete
    survivor = None   # entity_id of the survivor
    keep_separate = []
    with open(candidates, newline="") as f:
        for row in csv.DictReader(f):
            if row["disposition"] == "CANONICAL_SURVIVOR":
                if survivor:
                    sys.exit(f"ERROR: multiple CANONICAL_SURVIVOR rows; expected exactly one.")
                survivor = row["alias_entity_id"]
            elif row["disposition"] == "MERGE_INTO":
                if row["canonical_entity_id"] != row.get("canonical_entity_id"):
                    sys.exit(f"ERROR: bad canonical_entity_id on {row['alias_entity_id']}")
                merges.append(row["alias_entity_id"])
            elif row["disposition"] == "KEEP_SEPARATE":
                keep_separate.append(row["alias_entity_id"])

    if not survivor:
        sys.exit("ERROR: no CANONICAL_SURVIVOR row in candidates")

    print(f"Mode: {'COMMIT' if args.commit else 'DRY-RUN'}")
    print(f"Candidates: {candidates}")
    print(f"Canonical survivor: {survivor}")
    print(f"Merges (to delete + re-point): {len(merges)}: {merges}")
    print(f"Keep-separate: {len(keep_separate)}: {keep_separate}")

    # --- Read entities master
    with open(ent_master, newline="") as f:
        r = csv.reader(f)
        header = next(r)
        rows = list(r)
    idx = {col: i for i, col in enumerate(header)}
    if "entity_id" not in idx or "notes" not in idx:
        sys.exit(f"ERROR: _master_entities.csv missing entity_id or notes column")

    ent_pre = len(rows)

    # Collect alias notes for concat
    alias_note_additions = []
    for row in rows:
        eid = row[idx["entity_id"]]
        if eid in merges:
            alias_note = row[idx["notes"]].strip()
            if alias_note:
                alias_note_additions.append(f"[merged from {eid}] {alias_note}")

    # Rebuild: delete alias rows, augment survivor notes
    new_rows = []
    survivor_found = False
    for row in rows:
        eid = row[idx["entity_id"]]
        if eid in merges:
            continue  # delete
        if eid == survivor:
            survivor_found = True
            if alias_note_additions:
                existing = row[idx["notes"]].strip()
                parts = [existing] if existing else []
                parts.extend(alias_note_additions)
                row = list(row)
                row[idx["notes"]] = NOTES_DELIM.join(parts)
        new_rows.append(row)

    if not survivor_found:
        sys.exit(f"ERROR: canonical survivor '{survivor}' not present in _master_entities.csv")

    ent_post = len(new_rows)
    expected_ent_delta = -len(merges)
    actual_ent_delta = ent_post - ent_pre
    if actual_ent_delta != expected_ent_delta:
        print(f"  🔴 ERROR: entities row-count delta {actual_ent_delta} != expected {expected_ent_delta}")
        sys.exit(2)

    # --- Read entity join
    with open(ent_join, newline="") as f:
        r = csv.reader(f)
        j_header = next(r)
        j_rows = list(r)
    j_idx = {c: i for i, c in enumerate(j_header)}
    if "entity_id" not in j_idx or "study_id" not in j_idx:
        sys.exit(f"ERROR: _master_entity_studies.csv missing entity_id or study_id")

    join_pre = len(j_rows)

    # Rewrite alias entity_ids to survivor
    rewrites = 0
    rewritten = []
    for row in j_rows:
        eid = row[j_idx["entity_id"]]
        if eid in merges:
            row = list(row)
            row[j_idx["entity_id"]] = survivor
            rewrites += 1
        rewritten.append(row)

    # Dedup on (entity_id, study_id)
    seen = set()
    dedup = []
    for row in rewritten:
        key = (row[j_idx["entity_id"]], row[j_idx["study_id"]])
        if key in seen:
            continue
        seen.add(key)
        dedup.append(row)
    join_post = len(dedup)
    dedup_delta = join_pre - join_post

    print()
    print("=== Row-count summary ===")
    print(f"_master_entities.csv:       {ent_pre} -> {ent_post} (Δ {actual_ent_delta}; expected {expected_ent_delta})")
    print(f"_master_entity_studies.csv: {join_pre} -> {join_post} (rewrites={rewrites}, dedup delta={dedup_delta})")

    if not args.commit:
        print()
        print("DRY-RUN — no files written. Re-run with --commit to apply.")
        return 0

    stamp = utc_stamp()
    bak_ent = ent_master.with_suffix(f".csv.bak_phase_c_sap_alias_{stamp}")
    bak_join = ent_join.with_suffix(f".csv.bak_phase_c_sap_alias_{stamp}")
    shutil.copy2(ent_master, bak_ent)
    shutil.copy2(ent_join, bak_join)
    print(f"Backups: {bak_ent.name}, {bak_join.name}")

    with open(ent_master, "w", newline="") as f:
        w = csv.writer(f, quoting=csv.QUOTE_ALL)
        w.writerow(header)
        w.writerows(new_rows)
    with open(ent_join, "w", newline="") as f:
        w = csv.writer(f, quoting=csv.QUOTE_ALL)
        w.writerow(j_header)
        w.writerows(dedup)
    print(f"Wrote: {ent_master}")
    print(f"Wrote: {ent_join}")

    audit = archive / f"entity_aliases_sap_apply_v1_applied_{stamp}.txt"
    with open(audit, "w") as f:
        f.write(f"Phase C-narrow — SAP alias merge\n")
        f.write(f"Timestamp: {stamp}\n")
        f.write(f"Canonical survivor: {survivor}\n")
        f.write(f"Merges: {merges}\n")
        f.write(f"_master_entities.csv:       {ent_pre} -> {ent_post}\n")
        f.write(f"_master_entity_studies.csv: {join_pre} -> {join_post} (rewrites={rewrites}, dedup={dedup_delta})\n\n")
        f.write(f"Notes concat: {len(alias_note_additions)} alias-note blocks merged into survivor\n")
    print(f"Audit: {audit}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
