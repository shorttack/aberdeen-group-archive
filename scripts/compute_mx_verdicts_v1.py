#!/usr/bin/env python3
"""
compute_mx_verdicts_v1.py

Computes study-level prescience verdicts for the 13 scorable -mx studies
(expand-pc-deals v2 re-ingest) AND the matching A-side (v1) originals, using
ONE shared rule so the v1-vs-v2 comparison is apples-to-apples.

VERDICT RULE (locked 2026-06-27, Pete):
  used = [int(score) for score in obs if score is an integer 1..5]
         -> EXCLUDES 0 ("cannot assess" per rubric line 143), -1 (parse-fail/
            prefiltered), empty string, and any other non-1..5 sentinel.
  NO minimum-count gate (a sparse source like a weekly PC-deals bulletin is not
  penalized for genre; one genuine prediction still counts).
  if len(used)==0 -> 'not-applicable'
  elif mean(used) >= 3.5 -> 'high'
  elif mean(used) >= 2.0 -> 'medium'
  else                   -> 'low'

Every rationale DISCLOSES THE DENOMINATOR: how many obs were assessable (1..5)
vs not-assessable (0/blank) vs parse-fail (-1), so a thin-base verdict is
transparent, never hidden inside an average.

Reads:
  --mx-scores   the v7 Pass C output for the -mx batch (default pass_c_v7_mx_tier.csv)
  --master-pres _master_prescience_scores.csv (for A-side v1 scores)
Writes (with --commit):
  mx_verdicts_v1.csv        : study_id, verdict, mean, n_used, n_zero, n_neg,
                              n_total, prescience_rationale   (the 13 v2 studies)
  v1_v2_comparison_v1.csv   : study_base, v1_verdict, v1_mean, v1_n_used,
                              v2_verdict, v2_mean, v2_n_used, comparison_class
Dry-run by default; prints everything. --commit writes the two CSVs.
"""
import csv
import sys
from collections import defaultdict
from pathlib import Path

ARCH = Path.home() / "Desktop" / "Archive"
REPO = ARCH / "aberdeen-group-archive"
MX_SCORES = ARCH / "pass_c_v7_mx_tier.csv"
MASTER_PRES = REPO / "_master_prescience_scores.csv"
OUT_VERDICTS = ARCH / "mx_verdicts_v1.csv"
OUT_COMPARE = ARCH / "v1_v2_comparison_v1.csv"

commit = "--commit" in sys.argv


def bucket(vals):
    """vals = list of raw ints/None. Returns (verdict, mean, n_used, n_zero, n_neg, n_total)."""
    used = [v for v in vals if v is not None and 1 <= v <= 5]
    n_zero = sum(1 for v in vals if v == 0)
    n_neg = sum(1 for v in vals if v is not None and v < 0)
    n_total = len(vals)
    if not used:
        return "not-applicable", None, 0, n_zero, n_neg, n_total
    m = sum(used) / len(used)
    v = "high" if m >= 3.5 else "medium" if m >= 2.0 else "low"
    return v, round(m, 2), len(used), n_zero, n_neg, n_total


def rationale(verdict, m, n_used, n_zero, n_neg, n_total):
    if verdict == "not-applicable":
        return (f"not-applicable: 0 of {n_total} observations made an assessable "
                f"forward-looking prediction ({n_zero} were point-in-time market "
                f"data scored 0=cannot-assess, {n_neg} parse-fail/excluded). "
                f"Pass C v7, scores<1 excluded from mean.")
    return (f"{verdict}: mean {m} over {n_used} assessable prediction"
            f"{'s' if n_used != 1 else ''} (scores 1-5); "
            f"{n_zero} of {n_total} observations were point-in-time market data "
            f"scored 0=cannot-assess and excluded; {n_neg} parse-fail/excluded. "
            f"Verdict rule: scores<1 excluded, no min-count gate. Pass C v7.")


def load_scores_by_study(path, only=None):
    by = defaultdict(list)
    with open(path, newline="") as f:
        for r in csv.DictReader(f):
            sid = r.get("study_id", "")
            if only is not None and sid not in only:
                continue
            by[sid].append(parse_int(r.get("prescience_score", "")))
    return by


def parse_int(raw):
    try:
        return int(str(raw).strip())
    except (ValueError, TypeError):
        return None


def main():
    # ---- v2: the -mx studies from the v7 batch ----
    v2_by = load_scores_by_study(MX_SCORES)
    v2_studies = sorted(v2_by)
    print(f"=== v2 (-mx) verdicts: {len(v2_studies)} studies ===")
    print(f"{'study_id':46s} {'verdict':14s} {'mean':5s} {'used':4s} {'zero':4s} {'neg':3s} {'tot':3s}")
    print("-" * 90)
    v2_rows = []
    v2_verdict_by_base = {}
    for sid in v2_studies:
        verdict, m, nu, nz, nn, nt = bucket(v2_by[sid])
        base = sid[:-3] if sid.endswith("-mx") else sid
        v2_verdict_by_base[base] = (verdict, m, nu)
        rat = rationale(verdict, m, nu, nz, nn, nt)
        v2_rows.append({
            "study_id": sid, "verdict": verdict, "mean": m if m is not None else "",
            "n_used": nu, "n_zero": nz, "n_neg": nn, "n_total": nt,
            "prescience_rationale": rat,
        })
        print(f"{sid:46s} {verdict:14s} {str(m):5s} {nu:<4d} {nz:<4d} {nn:<3d} {nt:<3d}")

    from collections import Counter
    print("\nv2 verdict distribution:", dict(Counter(r["verdict"] for r in v2_rows)))

    # ---- v1: A-side originals (strip -mx), only those with scores ----
    bases = [s[:-3] if s.endswith("-mx") else s for s in v2_studies]
    v1_by = load_scores_by_study(MASTER_PRES, only=set(bases))
    print(f"\n=== v1 (A-side) verdicts: {len(v1_by)} of {len(bases)} originals have scores ===")
    print(f"{'study_base':46s} {'verdict':14s} {'mean':5s} {'used':4s} {'tot':3s}")
    print("-" * 80)
    v1_verdict_by_base = {}
    for base in bases:
        vals = v1_by.get(base, [])
        if not vals:
            v1_verdict_by_base[base] = ("<unscored-v1>", None, 0)
            continue
        verdict, m, nu, nz, nn, nt = bucket(vals)
        v1_verdict_by_base[base] = (verdict, m, nu)
        print(f"{base:46s} {verdict:14s} {str(m):5s} {nu:<4d} {nt:<3d}")

    # ---- comparison ----
    print(f"\n=== v1-vs-v2 comparison ===")
    print(f"{'study_base':46s} {'v1':14s} {'v2':14s} {'class':s}")
    print("-" * 92)
    cmp_rows = []
    for base in bases:
        v1v, v1m, v1n = v1_verdict_by_base[base]
        v2v, v2m, v2n = v2_verdict_by_base[base]
        if v1v == "<unscored-v1>":
            klass = "v1-missed (v2 first to score)"
        elif v1v == v2v:
            klass = "agree"
        else:
            order = {"low": 0, "medium": 1, "high": 2, "not-applicable": -1}
            klass = "v2-higher" if order.get(v2v, -1) > order.get(v1v, -1) else "v2-lower"
        cmp_rows.append({
            "study_base": base, "v1_verdict": v1v, "v1_mean": v1m if v1m is not None else "",
            "v1_n_used": v1n, "v2_verdict": v2v, "v2_mean": v2m if v2m is not None else "",
            "v2_n_used": v2n, "comparison_class": klass,
        })
        print(f"{base:46s} {v1v:14s} {v2v:14s} {klass}")

    print("\ncomparison class distribution:",
          dict(Counter(r["comparison_class"] for r in cmp_rows)))

    if not commit:
        print("\nDRY-RUN only — pass --commit to write mx_verdicts_v1.csv + v1_v2_comparison_v1.csv")
        return

    with open(OUT_VERDICTS, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(v2_rows[0].keys()), quoting=csv.QUOTE_ALL)
        w.writeheader()
        w.writerows(v2_rows)
    with open(OUT_COMPARE, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(cmp_rows[0].keys()), quoting=csv.QUOTE_ALL)
        w.writeheader()
        w.writerows(cmp_rows)
    print(f"\nWrote {OUT_VERDICTS} ({len(v2_rows)} rows)")
    print(f"Wrote {OUT_COMPARE} ({len(cmp_rows)} rows)")


if __name__ == "__main__":
    main()
