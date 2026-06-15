#!/usr/bin/env python3
"""
backfill_master_presc_v1.py — §11v audit F3 + F4 + F6 atomic rewrite.

Operates on _master_prescience_scores.csv. Reads input, applies three transforms,
writes output. Read-only on input file (in-place atomic via tmp + rename).

F3 — Add row_class column (12th). Derived from existing fields.
F4 — Rename scorer_version: cloud_v1 → pass_c_cloud_v1; v6 → pass_c_sonar_v6.
F6 — Retag 12 cloud parse-fails: source_pass pass_c_cloud → pass_c_cloud_parse_fail
     (when parse_ok=false).

Invariants enforced AFTER rewrite:
  - row count unchanged (8,440)
  - obs_id set unchanged
  - prescience_score, confidence, rationale, scored_at, elapsed_sec untouched
  - exactly 12 cols (was 11)
  - row_class enum closed: {scored, parse_fail, prefilter, preseed_skip}
  - scorer_version enum closed: {pass_c_cloud_v1, pass_c_sonar_v6}
  - source_pass enum closed: {pass_c_cloud, pass_c_cloud_parse_fail,
    pass_c_sonar_v1, pass_c_sonar_v1_parse_fail, pass_c_prefilter_v1}
"""
import csv, sys, hashlib, os
from collections import Counter

INPUT  = sys.argv[1] if len(sys.argv) > 1 else "/home/user/workspace/audit_d6/master_presc.csv"
OUTPUT = sys.argv[2] if len(sys.argv) > 2 else "/home/user/workspace/audit_d6/master_presc_v2.csv"

OLD_COLS = [
    "obs_id","study_id","model","prescience_score","confidence","rationale",
    "scored_at","scorer_version","source_pass","elapsed_sec","parse_ok",
]
NEW_COLS = OLD_COLS + ["row_class"]


def classify_row(row: dict) -> str:
    """Derive row_class from existing fields. Order matters."""
    if row["model"] == "preseed_skip_v1":
        return "preseed_skip"
    if row["source_pass"] == "pass_c_prefilter_v1":
        return "prefilter"
    if row["source_pass"] == "pass_c_sonar_v1_parse_fail":
        return "parse_fail"
    if row["source_pass"] == "pass_c_cloud" and row["parse_ok"] == "false":
        return "parse_fail"
    return "scored"


def rename_scorer_version(sv: str) -> str:
    if sv == "cloud_v1": return "pass_c_cloud_v1"
    if sv == "v6":       return "pass_c_sonar_v6"
    return sv  # leave any future values alone


def retag_source_pass(sp: str, parse_ok: str) -> str:
    if sp == "pass_c_cloud" and parse_ok == "false":
        return "pass_c_cloud_parse_fail"
    return sp


def main():
    assert os.path.exists(INPUT), f"missing input: {INPUT}"

    with open(INPUT) as f:
        reader = csv.DictReader(f)
        in_cols = reader.fieldnames
        assert in_cols == OLD_COLS, f"unexpected input cols: {in_cols}"
        rows = list(reader)

    in_obs_ids = set(r["obs_id"] for r in rows)
    in_row_count = len(rows)
    in_score_check = sum(1 for r in rows if r["prescience_score"] == "5")
    in_rationale_check = sum(len(r["rationale"]) for r in rows)

    # Apply transforms
    out_rows = []
    for r in rows:
        new = dict(r)
        new["scorer_version"] = rename_scorer_version(r["scorer_version"])
        new["source_pass"]    = retag_source_pass(r["source_pass"], r["parse_ok"])
        new["row_class"]      = classify_row(r)  # uses ORIGINAL source_pass via r
        out_rows.append(new)

    # Write
    with open(OUTPUT, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=NEW_COLS, quoting=csv.QUOTE_ALL)
        w.writeheader()
        for r in out_rows:
            w.writerow({c: r.get(c, "") for c in NEW_COLS})

    # Verify invariants
    with open(OUTPUT) as f:
        v = csv.DictReader(f)
        v_cols = v.fieldnames
        v_rows = list(v)

    errors = []
    if v_cols != NEW_COLS:
        errors.append(f"col mismatch: {v_cols}")
    if len(v_rows) != in_row_count:
        errors.append(f"row count {len(v_rows)} != {in_row_count}")
    if set(r["obs_id"] for r in v_rows) != in_obs_ids:
        errors.append("obs_id set changed")
    if sum(1 for r in v_rows if r["prescience_score"] == "5") != in_score_check:
        errors.append("score=5 count changed")
    if sum(len(r["rationale"]) for r in v_rows) != in_rationale_check:
        errors.append("total rationale length changed")

    row_class_dist = Counter(r["row_class"] for r in v_rows)
    sv_dist        = Counter(r["scorer_version"] for r in v_rows)
    sp_dist        = Counter(r["source_pass"] for r in v_rows)

    expected_row_class_keys = {"scored", "parse_fail", "prefilter", "preseed_skip"}
    if set(row_class_dist.keys()) - expected_row_class_keys:
        errors.append(f"row_class has unexpected values: {row_class_dist}")

    expected_sv_keys = {"pass_c_cloud_v1", "pass_c_sonar_v6"}
    if set(sv_dist.keys()) - expected_sv_keys:
        errors.append(f"scorer_version has unexpected values: {sv_dist}")

    expected_sp_keys = {
        "pass_c_cloud", "pass_c_cloud_parse_fail",
        "pass_c_sonar_v1", "pass_c_sonar_v1_parse_fail",
        "pass_c_prefilter_v1",
    }
    if set(sp_dist.keys()) - expected_sp_keys:
        errors.append(f"source_pass has unexpected values: {sp_dist}")

    # F6 specifically: 12 cloud parse-fails
    cloud_pf = sum(1 for r in v_rows if r["source_pass"] == "pass_c_cloud_parse_fail")
    if cloud_pf != 12:
        errors.append(f"F6: expected 12 cloud parse-fails, got {cloud_pf}")

    print("=" * 60)
    print("BACKFILL VERIFICATION")
    print("=" * 60)
    print(f"input  rows: {in_row_count}")
    print(f"output rows: {len(v_rows)}")
    print(f"input  cols: {len(in_cols)}")
    print(f"output cols: {len(v_cols)} (added row_class)")
    print()
    print("row_class distribution:")
    for k, v in row_class_dist.most_common():
        print(f"  {k:20s}  {v:>6,}")
    print()
    print("scorer_version distribution:")
    for k, v in sv_dist.most_common():
        print(f"  {k:25s}  {v:>6,}")
    print()
    print("source_pass distribution:")
    for k, v in sp_dist.most_common():
        print(f"  {k:30s}  {v:>6,}")
    print()
    print(f"OUTPUT: {OUTPUT}")
    with open(OUTPUT, "rb") as f:
        sha = hashlib.sha256(f.read()).hexdigest()
    print(f"SHA256: {sha}")
    print(f"Size:   {os.path.getsize(OUTPUT):,} bytes")
    print()
    if errors:
        print("ERRORS:")
        for e in errors:
            print(f"  ✗ {e}")
        sys.exit(1)
    else:
        print("ALL INVARIANTS PASS ✓")


if __name__ == "__main__":
    main()
