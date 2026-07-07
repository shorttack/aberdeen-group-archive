#!/usr/bin/env python3
"""
apply_entity_metadata_v1.py — Phase B of the 2026-07-07 master-CSV cleanse.

Fixes 4 metadata fields (entity_type, sector, status, successor) on entity rows
whose ingest carried bleed/false metadata (Informix→Siemens-Nixdorf,
Microsoft→HP Inc./HPE, Intel→Compaq→HP, Sybase→Compaq→HP→HPE-NonStop, etc.).

READS entity_metadata_candidates_v1.csv, WRITES only _master_entities.csv.

Invariants:
  - Row count MUST be unchanged (hard assert).
  - Only the 4 listed fields can change per row; entity_id, entity_name, years_active,
    notes are frozen.
  - Empty proposed value = write empty string (not null - CSV keeps col shape).
  - Timestamped .bak; csv.QUOTE_ALL; dry-run default.
  - Every field change logged to audit trail.

Usage:
  python3 apply_entity_metadata_v1.py                                # dry-run
  python3 apply_entity_metadata_v1.py --commit                       # write
"""
import argparse
import csv
import datetime as _dt
import shutil
import sys
from pathlib import Path

DEFAULT_ARCHIVE = Path.home() / "Desktop/Archive/aberdeen-group-archive"
DEFAULT_CANDIDATES = Path.home() / "Desktop/Archive/entity_metadata_candidates_v1.csv"
EDITABLE_FIELDS = ("entity_type", "sector", "status", "successor")


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

    if not ent_master.exists(): sys.exit(f"ERROR: {ent_master} not found")
    if not candidates.exists(): sys.exit(f"ERROR: {candidates} not found")

    # Read candidates
    cand_map = {}
    with open(candidates, newline="") as f:
        for row in csv.DictReader(f):
            cand_map[row["entity_id"]] = row

    print(f"Mode: {'COMMIT' if args.commit else 'DRY-RUN'}")
    print(f"Candidates: {candidates}")
    print(f"Rows to update: {len(cand_map)}")

    # Read entities
    with open(ent_master, newline="") as f:
        r = csv.reader(f)
        header = next(r)
        rows = list(r)
    idx = {col: i for i, col in enumerate(header)}
    for req in ("entity_id",) + EDITABLE_FIELDS:
        if req not in idx:
            sys.exit(f"ERROR: _master_entities.csv missing column '{req}'")

    pre = len(rows)

    # Apply edits
    changes = []  # (entity_id, field, before, after)
    updated = 0
    for row in rows:
        eid = row[idx["entity_id"]]
        c = cand_map.get(eid)
        if not c: continue
        row_changed = False
        for f_name in EDITABLE_FIELDS:
            current = row[idx[f_name]]
            proposed = c.get(f"proposed_{f_name}", "")
            if current != proposed:
                changes.append((eid, f_name, current, proposed))
                row[idx[f_name]] = proposed
                row_changed = True
        if row_changed: updated += 1

    post = len(rows)

    print()
    print(f"Row count: {pre} -> {post} (Δ {post - pre}; MUST be 0)")
    if post != pre:
        print(f"  🔴 ERROR: row count changed. Aborting.")
        sys.exit(2)

    print(f"Rows updated: {updated}")
    print(f"Field-level changes: {len(changes)}")

    # Report entities in candidates but missing from master (typos, deleted rows, etc.)
    missing = set(cand_map.keys()) - {row[idx["entity_id"]] for row in rows}
    if missing:
        print(f"  ⚠️  {len(missing)} candidate entity_ids NOT found in master: {sorted(missing)}")

    print()
    print("=== Change detail ===")
    for eid, f_name, before, after in changes:
        b = before if before else "(empty)"
        a = after if after else "(empty)"
        print(f"  {eid:32s} .{f_name}: {b!r} -> {a!r}")

    if not args.commit:
        print()
        print("DRY-RUN — no file written. Re-run with --commit to apply.")
        return 0

    stamp = utc_stamp()
    bak = ent_master.with_suffix(f".csv.bak_phase_b_entity_metadata_{stamp}")
    shutil.copy2(ent_master, bak)
    print(f"Backup: {bak.name}")

    with open(ent_master, "w", newline="") as f:
        w = csv.writer(f, quoting=csv.QUOTE_ALL)
        w.writerow(header)
        w.writerows(rows)
    print(f"Wrote: {ent_master}")

    audit = archive / f"entity_metadata_apply_v1_applied_{stamp}.txt"
    with open(audit, "w") as f:
        f.write(f"Phase B — entity metadata bleed fix\n")
        f.write(f"Timestamp: {stamp}\n")
        f.write(f"Candidates: {candidates}\n")
        f.write(f"Row count: {pre} -> {post} (unchanged, as required)\n")
        f.write(f"Rows updated: {updated}\n")
        f.write(f"Field-level changes: {len(changes)}\n\n")
        for eid, f_name, before, after in changes:
            f.write(f"  {eid} .{f_name}: {before!r} -> {after!r}\n")
    print(f"Audit: {audit}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
