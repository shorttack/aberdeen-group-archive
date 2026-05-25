#!/usr/bin/env python3
"""
apply_year_observed_v2.py
==========================
v2 — QUOTE_ALL compliance + post-write verification.

Changes from v1
---------------
* Uses `csv.writer(..., quoting=csv.QUOTE_ALL)` per archive §16.5 rule.
* Adds `--verify-only` mode: re-reads current master, compares against
  backup (or any reference master), and asserts only expected cells
  differ. No writes. Useful after v1 ran with QUOTE_MINIMAL to confirm
  the master is still byte-clean.
* Adds `--rewrite-quoting` mode: reads the current master and rewrites
  it with QUOTE_ALL quoting, no value changes. One-time fix for the
  v1 run output.

Three modes
-----------
  (default, no flags)    → Stage 1 preview only (dry run, no master writes)
  --apply                → Stage 2 apply (writes very_high proposals)
  --verify-only          → Compare current master against a backup
                           and report cell-level diff
  --rewrite-quoting      → Rewrite current master with QUOTE_ALL,
                           no value changes (one-time v1 cleanup)

Default install location
------------------------
    /Users/scott/Desktop/Archive/scripts/apply_year_observed_v2.py

Version
-------
v2 — QUOTE_ALL + verification + rewrite-quoting modes
v1 — initial apply (QUOTE_MINIMAL — non-compliant)
"""

import argparse
import csv
import datetime as dt
import shutil
import sys
from pathlib import Path

PROVENANCE = "local_date_extraction_v3_copyright_anchor"


def load_proposals(p: Path) -> list[dict]:
    with p.open(newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def load_master(p: Path) -> tuple[list[str], list[dict]]:
    with p.open(newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        return reader.fieldnames or [], list(reader)


def write_master_quote_all(path: Path, fieldnames: list[str], rows: list[dict]) -> None:
    """Atomic write with QUOTE_ALL quoting per archive §16.5."""
    tmp = path.with_suffix(".csv.tmp")
    with tmp.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fieldnames, quoting=csv.QUOTE_ALL)
        w.writeheader()
        w.writerows(rows)
    tmp.replace(path)


def diff_masters(current: Path, reference: Path, key_col: str = "obs_id") -> dict:
    """Compare two master CSVs cell-by-cell, keyed on obs_id.

    Returns a dict with counts and a sample of differing cells.
    """
    _, cur_rows = load_master(current)
    _, ref_rows = load_master(reference)
    cur_by_id = {r[key_col]: r for r in cur_rows}
    ref_by_id = {r[key_col]: r for r in ref_rows}

    only_in_current = cur_by_id.keys() - ref_by_id.keys()
    only_in_reference = ref_by_id.keys() - cur_by_id.keys()
    common = cur_by_id.keys() & ref_by_id.keys()

    cell_diffs: list[dict] = []
    columns_changed: dict[str, int] = {}
    for oid in common:
        c = cur_by_id[oid]
        r = ref_by_id[oid]
        for col in c:
            if c.get(col, "") != r.get(col, ""):
                columns_changed[col] = columns_changed.get(col, 0) + 1
                if len(cell_diffs) < 20:
                    cell_diffs.append({
                        "obs_id": oid,
                        "column": col,
                        "ref_value": r.get(col, ""),
                        "cur_value": c.get(col, ""),
                    })
    return {
        "current_rows": len(cur_rows),
        "reference_rows": len(ref_rows),
        "only_in_current": len(only_in_current),
        "only_in_reference": len(only_in_reference),
        "columns_changed": columns_changed,
        "sample_diffs": cell_diffs,
    }


def mode_apply(args) -> int:
    proposals_path = args.proposals or args.workspace / "proposed_year_observed_v3.csv"
    masters_path = args.masters_dir / "_master_observations.csv"
    preview_path = args.workspace / "apply_preview_year_observed_v2.csv"
    audit_path = args.workspace / "year_observed_apply_audit_v2.csv"

    if not proposals_path.is_file():
        print(f"ERROR: proposals CSV not found: {proposals_path}", file=sys.stderr)
        return 2
    if not masters_path.is_file():
        print(f"ERROR: master CSV not found: {masters_path}", file=sys.stderr)
        return 2

    args.workspace.mkdir(parents=True, exist_ok=True)

    proposals = load_proposals(proposals_path)
    eligible = [
        p for p in proposals
        if p.get("confidence") == args.confidence and p.get("candidate_1")
    ]
    print(f"Proposals: {len(proposals):,} total, "
          f"{len(eligible):,} at confidence='{args.confidence}'")
    proposal_by_obs = {p["obs_id"]: p for p in eligible}

    master_fields, master_rows = load_master(masters_path)
    print(f"Master: {len(master_rows):,} rows")

    if "year_observed" not in master_fields or "obs_id" not in master_fields:
        print("ERROR: required columns missing from master.", file=sys.stderr)
        return 2

    plan: list[dict] = []
    skip_already_filled = 0
    skip_orphan = 0
    will_apply = 0
    by_obs = {r["obs_id"]: r for r in master_rows}

    for obs_id, prop in proposal_by_obs.items():
        if obs_id not in by_obs:
            skip_orphan += 1
            plan.append({"obs_id": obs_id, "current_value": "",
                         "proposed_value": prop["candidate_1"],
                         "study_id": prop.get("study_id", ""),
                         "evidence_snippet": prop.get("evidence_snippet", "")[:200],
                         "will_apply": "no_orphan_proposal"})
            continue
        current = (by_obs[obs_id].get("year_observed") or "").strip()
        if current:
            skip_already_filled += 1
            plan.append({"obs_id": obs_id, "current_value": current,
                         "proposed_value": prop["candidate_1"],
                         "study_id": prop.get("study_id", ""),
                         "evidence_snippet": prop.get("evidence_snippet", "")[:200],
                         "will_apply": "no_already_filled"})
            continue
        will_apply += 1
        plan.append({"obs_id": obs_id, "current_value": "",
                     "proposed_value": prop["candidate_1"],
                     "study_id": prop.get("study_id", ""),
                     "evidence_snippet": prop.get("evidence_snippet", "")[:200],
                     "will_apply": "yes"})

    with preview_path.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=["obs_id", "current_value",
                                          "proposed_value", "study_id",
                                          "evidence_snippet", "will_apply"],
                           quoting=csv.QUOTE_ALL)
        w.writeheader()
        w.writerows(plan)

    print(f"\nPreview: {preview_path}  ({len(plan):,} rows)")
    print(f"  will_apply=yes:           {will_apply:,}")
    print(f"  skip (already filled):    {skip_already_filled:,}")
    print(f"  skip (orphan proposal):   {skip_orphan:,}")

    if not args.apply:
        print("\nDRY RUN — no master changes. Re-run with --apply to write.")
        return 0

    if will_apply == 0:
        print("\nNothing to apply. Exiting.")
        return 0

    ts = dt.datetime.now(dt.timezone.utc).strftime("%Y%m%d_%H%M%SZ")
    backup_dir = args.archive / f"archive_masters_pre_year_observed_apply_{ts}"
    backup_dir.mkdir(parents=True, exist_ok=True)
    backup_path = backup_dir / masters_path.name
    shutil.copy2(masters_path, backup_path)
    print(f"\nBacked up master → {backup_path}")

    audit_rows: list[dict] = []
    applied_at = dt.datetime.now(dt.timezone.utc).isoformat()
    for row in master_rows:
        oid = row["obs_id"]
        if oid not in proposal_by_obs:
            continue
        if (row.get("year_observed") or "").strip():
            continue
        prop = proposal_by_obs[oid]
        new_val = prop["candidate_1"]
        row["year_observed"] = new_val
        audit_rows.append({
            "obs_id": oid, "old_value": "", "new_value": new_val,
            "study_id": prop.get("study_id", ""),
            "source_snippet": prop.get("evidence_snippet", "")[:300],
            "provenance_tag": PROVENANCE,
            "applied_at_utc": applied_at,
        })

    write_master_quote_all(masters_path, master_fields, master_rows)
    print(f"Master updated (QUOTE_ALL): {masters_path}  "
          f"({len(audit_rows):,} rows changed)")

    if audit_path.exists():
        audit_path = audit_path.with_name(
            audit_path.stem + f"_{ts}" + audit_path.suffix)
    with audit_path.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(
            f,
            fieldnames=["obs_id", "old_value", "new_value", "study_id",
                        "source_snippet", "provenance_tag", "applied_at_utc"],
            quoting=csv.QUOTE_ALL,
        )
        w.writeheader()
        w.writerows(audit_rows)
    print(f"Audit log: {audit_path}")
    print(f"\nRollback: cp {backup_path} {masters_path}")
    return 0


def mode_verify(args) -> int:
    """Compare current master against a reference (typically the pre-v1 backup)."""
    masters_path = args.masters_dir / "_master_observations.csv"
    if not args.reference:
        print("ERROR: --reference <path> required for --verify-only.",
              file=sys.stderr)
        return 2
    if not masters_path.is_file() or not args.reference.is_file():
        print("ERROR: master or reference missing.", file=sys.stderr)
        return 2

    print(f"Comparing:\n  current:   {masters_path}\n  reference: {args.reference}")
    d = diff_masters(masters_path, args.reference)
    print(f"\nRow counts:  current={d['current_rows']:,}  reference={d['reference_rows']:,}")
    print(f"Only in current:   {d['only_in_current']}")
    print(f"Only in reference: {d['only_in_reference']}")
    print(f"\nColumns with differences: {dict(d['columns_changed'])}")
    if d["sample_diffs"]:
        print("\nSample differences (first 20):")
        for s in d["sample_diffs"]:
            print(f"  {s['obs_id']:>30}  {s['column']:>15}  "
                  f"ref='{s['ref_value'][:30]}'  cur='{s['cur_value'][:30]}'")
    total = sum(d["columns_changed"].values())
    print(f"\nTotal cell differences: {total:,}")
    expected_col = "year_observed"
    if d["columns_changed"].get(expected_col, 0) == 698 and len(d["columns_changed"]) == 1:
        print(f"\n✓ VERIFIED: exactly 698 cells differ, all in '{expected_col}'. Clean.")
        return 0
    print(f"\n⚠ UNEXPECTED: differences are NOT confined to {expected_col}=698. Review above.")
    return 1


def mode_rewrite_quoting(args) -> int:
    """Read current master, rewrite with QUOTE_ALL, no value changes."""
    masters_path = args.masters_dir / "_master_observations.csv"
    if not masters_path.is_file():
        print(f"ERROR: master not found: {masters_path}", file=sys.stderr)
        return 2

    ts = dt.datetime.now(dt.timezone.utc).strftime("%Y%m%d_%H%M%SZ")
    backup_dir = args.archive / f"archive_masters_pre_rewrite_quoting_{ts}"
    backup_dir.mkdir(parents=True, exist_ok=True)
    backup_path = backup_dir / masters_path.name
    shutil.copy2(masters_path, backup_path)
    print(f"Backed up → {backup_path}")

    fields, rows = load_master(masters_path)
    write_master_quote_all(masters_path, fields, rows)
    print(f"Rewrote {masters_path} with QUOTE_ALL ({len(rows):,} rows, no value changes).")
    print(f"\nRollback: cp {backup_path} {masters_path}")
    print("\nVerify with:")
    print(f"  python3 {__file__} --verify-only --reference {backup_path}")
    print("  (expect: 0 cell differences — only quoting style changed)")
    return 0


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[1])
    ap.add_argument("--archive", type=Path,
                    default=Path("/Users/scott/Desktop/Archive"))
    ap.add_argument("--masters-dir", type=Path,
                    default=Path("/Users/scott/Desktop/Archive/archive_masters"))
    ap.add_argument("--workspace", type=Path,
                    default=Path("/Users/scott/Desktop/Archive/v1.5_workspace"))
    ap.add_argument("--proposals", type=Path, default=None)
    ap.add_argument("--confidence", default="very_high")

    # Modes (mutually exclusive in spirit; first match wins)
    ap.add_argument("--apply", action="store_true")
    ap.add_argument("--verify-only", dest="verify_only", action="store_true")
    ap.add_argument("--rewrite-quoting", dest="rewrite_quoting",
                    action="store_true")
    ap.add_argument("--reference", type=Path, default=None,
                    help="Reference master for --verify-only")
    args = ap.parse_args()

    if args.verify_only:
        return mode_verify(args)
    if args.rewrite_quoting:
        return mode_rewrite_quoting(args)
    return mode_apply(args)


if __name__ == "__main__":
    sys.exit(main())
