#!/usr/bin/env python3
"""
apply_blog_artifact_cleaning_auto5_v1.py

Apply the five safest blog-artifact quote cleanups from
blog_artifact_cleaning_candidates_v2.csv to _master_quotations_prescience.csv.

Default mode is dry-run. Pass --commit to write.
"""
from __future__ import annotations

import argparse
import csv
import datetime as dt
import shutil
from pathlib import Path


AUTO_RECOMMENDATION = "auto_strip_blog_artifact"


def utc_stamp() -> str:
    return dt.datetime.now(dt.UTC).strftime("%Y%m%dT%H%M%SZ")


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument(
        "--master",
        default=str(Path.home() / "Desktop/Archive/aberdeen-group-archive/_master_quotations_prescience.csv"),
    )
    ap.add_argument(
        "--candidates",
        default=str(Path.home() / "Desktop/Archive/aberdeen-group-archive/Perplexity_Only/blog_artifact_cleaning_candidates_v2.csv"),
    )
    ap.add_argument("--commit", action="store_true")
    args = ap.parse_args()

    master = Path(args.master)
    candidates_path = Path(args.candidates)
    stamp = utc_stamp()
    audit_path = master.parent / "Perplexity_Only" / f"blog_artifact_cleaning_apply_auto5_v1_audit_{stamp}.csv"
    backup_path = master.with_suffix(f".csv.bak_blog_artifact_auto5_{stamp}")

    with candidates_path.open(newline="") as f:
        candidate_rows = list(csv.DictReader(f))
    replacements = {
        r["row_id"]: r
        for r in candidate_rows
        if r.get("recommendation") == AUTO_RECOMMENDATION
    }

    expected = {"1183", "1188", "1190", "1194", "1200"}
    found = set(replacements)
    if found != expected:
        raise SystemExit(f"Expected auto row_ids {sorted(expected)}, found {sorted(found)}. Aborting.")

    with master.open(newline="") as f:
        reader = csv.DictReader(f)
        fieldnames = reader.fieldnames or []
        rows = list(reader)

    if "quote" not in fieldnames or "blog_scrape_contamination_flag" not in fieldnames:
        raise SystemExit("Required columns missing. Aborting.")

    audit_rows = []
    changed = 0
    for row in rows:
        rid = row.get("row_id", "")
        if rid not in replacements:
            continue
        cand = replacements[rid]
        old_quote = row.get("quote", "")
        new_quote = cand.get("proposed_quote", "")
        if old_quote == new_quote:
            continue
        audit_rows.append(
            {
                "row_id": rid,
                "old_blog_scrape_contamination_flag": row.get("blog_scrape_contamination_flag", ""),
                "new_blog_scrape_contamination_flag": "false",
                "old_len": len(old_quote),
                "new_len": len(new_quote),
                "delta_len": len(new_quote) - len(old_quote),
                "old_quote": old_quote,
                "new_quote": new_quote,
            }
        )
        row["quote"] = new_quote
        row["blog_scrape_contamination_flag"] = "false"
        changed += 1

    print(f"Mode: {'COMMIT' if args.commit else 'DRY-RUN'}")
    print(f"Master: {master}")
    print(f"Candidates: {candidates_path}")
    print(f"Rows read: {len(rows)}")
    print(f"Rows to change: {changed}")
    for a in audit_rows:
        print(
            f"{a['row_id']}: flag {a['old_blog_scrape_contamination_flag']} -> "
            f"{a['new_blog_scrape_contamination_flag']}; len {a['old_len']} -> {a['new_len']}"
        )

    if not args.commit:
        print("DRY-RUN only. Re-run with --commit to write master, backup, and audit.")
        return 0

    shutil.copy2(master, backup_path)
    with master.open("w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames, quoting=csv.QUOTE_ALL)
        writer.writeheader()
        writer.writerows(rows)

    audit_path.parent.mkdir(parents=True, exist_ok=True)
    with audit_path.open("w", newline="") as f:
        writer = csv.DictWriter(
            f,
            fieldnames=[
                "row_id",
                "old_blog_scrape_contamination_flag",
                "new_blog_scrape_contamination_flag",
                "old_len",
                "new_len",
                "delta_len",
                "old_quote",
                "new_quote",
            ],
            quoting=csv.QUOTE_ALL,
        )
        writer.writeheader()
        writer.writerows(audit_rows)

    print(f"Backup: {backup_path}")
    print(f"Audit: {audit_path}")
    print("BLOG_ARTIFACT_AUTO5_APPLY_OK")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
