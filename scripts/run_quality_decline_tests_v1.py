#!/usr/bin/env python3
"""
run_quality_decline_tests_v1.py

Aggregates SH sweep results for the "Prescience Decline Across Aberdeen Eras"
study (kastner-author/studies/study_prescience_decline_aberdeen_eras_v1.md).

Tests:
  T1  Anchor-decade aggregation (primary: anchor<=2011; secondary: anchor<=2015)
  T3  Methodology-code aggregation (joined from _master_observations.csv)

  T2  (author ranking) is DEFERRED to a future Kastner-accuracy study and is
       intentionally NOT computed here.

Sentinel handling:
  -99  content_unrecoverable  -> excluded from numerators, tracked in denom table
  -1   parse_fail:malformed   -> excluded from numerators, tracked
  -2   pending (window short) -> excluded from numerators, tracked

Inputs (defaults assume repo root):
  --sweep      Perplexity_Only/sh_sweep_le_2015_results.csv
  --master     _master_observations.csv
  --outdir     Perplexity_Only/

Outputs:
  quality_decline_tests_v1_report.json
  quality_decline_tests_v1_report.md
  quality_decline_t1_by_decade_primary.csv
  quality_decline_t1_by_decade_secondary.csv
  quality_decline_t3_by_methodology.csv

CLI:
  python3 scripts/run_quality_decline_tests_v1.py \
      --sweep Perplexity_Only/sh_sweep_le_2015_results.csv \
      --master _master_observations.csv \
      --outdir Perplexity_Only/
"""
import argparse
import csv
import json
import sys
import statistics
from collections import Counter, defaultdict
from pathlib import Path

SENTINELS = {-99, -1, -2}


def to_int(v):
    try:
        return int(v)
    except (TypeError, ValueError):
        try:
            return int(float(v))
        except (TypeError, ValueError):
            return None


def anchor_decade(year):
    if year is None:
        return None
    try:
        y = int(year)
    except (TypeError, ValueError):
        return None
    if y < 1970 or y > 2030:
        return None
    return f"{(y // 10) * 10}s"


def load_sweep(path):
    rows = []
    with open(path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for r in reader:
            rows.append(r)
    return rows


def load_master_methodology(path):
    """Return dict obs_id -> methodology_code (or None)."""
    out = {}
    with open(path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        cols = reader.fieldnames or []
        mcol = None
        for cand in ("methodology_code", "methodology", "method_code"):
            if cand in cols:
                mcol = cand
                break
        if mcol is None:
            print(f"[warn] no methodology column in {path}; T3 will be empty",
                  file=sys.stderr)
            return out
        for r in reader:
            obs_id = r.get("obs_id") or r.get("observation_id")
            if not obs_id:
                continue
            out[obs_id] = (r.get(mcol) or "").strip() or None
    return out


def aggregate(rows, window):
    """rows: list of dicts with int scores already extracted for `window`.
       window: '3y' or '5y'.
       Returns dict with n_total, n_valid, sentinels split, mean, mode,
       share_4_5, share_0_1, divergence_with_other_window (computed in caller).
    """
    score_col = f"prescience_{window}"
    valid = []
    sentinel_counts = Counter()
    for r in rows:
        s = to_int(r.get(score_col))
        if s is None:
            sentinel_counts["null"] += 1
            continue
        if s in SENTINELS:
            sentinel_counts[str(s)] += 1
            continue
        if 0 <= s <= 5:
            valid.append(s)
        else:
            sentinel_counts["out_of_range"] += 1

    n_total = len(rows)
    n_valid = len(valid)
    if n_valid == 0:
        return {
            "n_total": n_total,
            "n_valid": 0,
            "sentinels": dict(sentinel_counts),
            "mean": None,
            "mode": None,
            "share_4_5": None,
            "share_0_1": None,
            "dist": {},
        }
    dist = Counter(valid)
    return {
        "n_total": n_total,
        "n_valid": n_valid,
        "sentinels": dict(sentinel_counts),
        "mean": round(statistics.fmean(valid), 4),
        "mode": statistics.mode(valid),
        "share_4_5": round(sum(1 for s in valid if s >= 4) / n_valid, 4),
        "share_0_1": round(sum(1 for s in valid if s <= 1) / n_valid, 4),
        "dist": {str(k): dist[k] for k in sorted(dist)},
    }


def divergence_rate(rows):
    """% rows where prescience_3y != prescience_5y (both valid)."""
    n = 0
    div = 0
    for r in rows:
        s3 = to_int(r.get("prescience_3y"))
        s5 = to_int(r.get("prescience_5y"))
        if s3 is None or s5 is None:
            continue
        if s3 in SENTINELS or s5 in SENTINELS:
            continue
        n += 1
        if s3 != s5:
            div += 1
    return (round(div / n, 4) if n else None, div, n)


def bucket_by(rows, keyfn):
    out = defaultdict(list)
    for r in rows:
        k = keyfn(r)
        if k is None:
            continue
        out[k].append(r)
    return out


def run_t1(rows, cutoff_year, label):
    elig = [r for r in rows if (to_int(r.get("anchor_year")) or 0) <= cutoff_year]
    by_dec = bucket_by(elig, lambda r: anchor_decade(r.get("anchor_year")))
    out = {
        "label": label,
        "cutoff_year": cutoff_year,
        "n_eligible": len(elig),
        "by_decade": {},
        "overall_3y": aggregate(elig, "3y"),
        "overall_5y": aggregate(elig, "5y"),
    }
    div_rate, div_n, div_d = divergence_rate(elig)
    out["overall_divergence"] = {
        "rate": div_rate, "diverging": div_n, "denom": div_d
    }
    for dec in sorted(by_dec):
        drows = by_dec[dec]
        dv_rate, dv_n, dv_d = divergence_rate(drows)
        out["by_decade"][dec] = {
            "n": len(drows),
            "3y": aggregate(drows, "3y"),
            "5y": aggregate(drows, "5y"),
            "divergence": {"rate": dv_rate, "diverging": dv_n, "denom": dv_d},
        }
    return out


def run_t3(rows, methodology_map):
    enriched = []
    for r in rows:
        oid = r.get("obs_id")
        m = methodology_map.get(oid)
        if m:
            r2 = dict(r)
            r2["_methodology"] = m
            enriched.append(r2)
    by_m = bucket_by(enriched, lambda r: r.get("_methodology"))
    out = {
        "n_with_methodology": len(enriched),
        "n_missing_methodology": len(rows) - len(enriched),
        "by_methodology": {},
    }
    for m in sorted(by_m):
        mrows = by_m[m]
        dv_rate, dv_n, dv_d = divergence_rate(mrows)
        out["by_methodology"][m] = {
            "n": len(mrows),
            "3y": aggregate(mrows, "3y"),
            "5y": aggregate(mrows, "5y"),
            "divergence": {"rate": dv_rate, "diverging": dv_n, "denom": dv_d},
        }
    return out


def write_decade_csv(t1, path):
    cols = [
        "decade", "n", "n_valid_3y", "mean_3y", "mode_3y",
        "share_4_5_3y", "share_0_1_3y",
        "n_valid_5y", "mean_5y", "mode_5y", "share_4_5_5y", "share_0_1_5y",
        "divergence_rate",
        "sentinels_99_3y", "sentinels_1_3y", "sentinels_2_3y",
    ]
    with open(path, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(cols)
        for dec in sorted(t1["by_decade"]):
            d = t1["by_decade"][dec]
            s3 = d["3y"]; s5 = d["5y"]
            sent3 = s3.get("sentinels", {})
            w.writerow([
                dec, d["n"],
                s3["n_valid"], s3["mean"], s3["mode"],
                s3["share_4_5"], s3["share_0_1"],
                s5["n_valid"], s5["mean"], s5["mode"],
                s5["share_4_5"], s5["share_0_1"],
                d["divergence"]["rate"],
                sent3.get("-99", 0), sent3.get("-1", 0), sent3.get("-2", 0),
            ])


def write_methodology_csv(t3, path):
    cols = [
        "methodology_code", "n", "n_valid_3y", "mean_3y", "mode_3y",
        "share_4_5_3y", "share_0_1_3y",
        "n_valid_5y", "mean_5y", "mode_5y", "share_4_5_5y", "share_0_1_5y",
        "divergence_rate",
    ]
    with open(path, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(cols)
        for m in sorted(t3["by_methodology"]):
            d = t3["by_methodology"][m]
            s3 = d["3y"]; s5 = d["5y"]
            w.writerow([
                m, d["n"],
                s3["n_valid"], s3["mean"], s3["mode"],
                s3["share_4_5"], s3["share_0_1"],
                s5["n_valid"], s5["mean"], s5["mode"],
                s5["share_4_5"], s5["share_0_1"],
                d["divergence"]["rate"],
            ])


def render_md(report):
    L = []
    L.append("# Quality Decline Tests v1 — Report")
    L.append("")
    L.append(f"- Generated: {report['generated_at']}")
    L.append(f"- Sweep input: `{report['inputs']['sweep']}`")
    L.append(f"- Master input: `{report['inputs']['master']}`")
    L.append(f"- Total sweep rows: {report['n_sweep_rows']}")
    L.append("")
    L.append("## T1 — Anchor-decade aggregation")
    for key in ("primary", "secondary"):
        t1 = report["T1"][key]
        L.append("")
        L.append(f"### T1 {key} (anchor ≤ {t1['cutoff_year']})")
        L.append(f"- n eligible: {t1['n_eligible']}")
        L.append(f"- overall 3y mean: {t1['overall_3y']['mean']}  "
                 f"mode: {t1['overall_3y']['mode']}  "
                 f"share 4–5: {t1['overall_3y']['share_4_5']}")
        L.append(f"- overall 5y mean: {t1['overall_5y']['mean']}  "
                 f"mode: {t1['overall_5y']['mode']}  "
                 f"share 4–5: {t1['overall_5y']['share_4_5']}")
        L.append(f"- divergence: {t1['overall_divergence']['rate']} "
                 f"({t1['overall_divergence']['diverging']}/"
                 f"{t1['overall_divergence']['denom']})")
        L.append("")
        L.append("| Decade | n | mean 3y | mode 3y | 4–5% 3y | mean 5y | 4–5% 5y | div. | -99 3y | -1 3y |")
        L.append("|---|---|---|---|---|---|---|---|---|---|")
        for dec in sorted(t1["by_decade"]):
            d = t1["by_decade"][dec]
            s3 = d["3y"]; s5 = d["5y"]
            sent3 = s3.get("sentinels", {})
            L.append("| {dec} | {n} | {m3} | {mo3} | {p3} | {m5} | {p5} | {dv} | {s99} | {s1} |".format(
                dec=dec, n=d["n"],
                m3=s3["mean"], mo3=s3["mode"], p3=s3["share_4_5"],
                m5=s5["mean"], p5=s5["share_4_5"],
                dv=d["divergence"]["rate"],
                s99=sent3.get("-99", 0), s1=sent3.get("-1", 0),
            ))
    L.append("")
    L.append("## T3 — Methodology-code aggregation")
    t3 = report["T3"]
    L.append(f"- n with methodology: {t3['n_with_methodology']}")
    L.append(f"- n missing methodology: {t3['n_missing_methodology']}")
    L.append("")
    L.append("| Methodology | n | mean 3y | mode 3y | 4–5% 3y | mean 5y | 4–5% 5y | div. |")
    L.append("|---|---|---|---|---|---|---|---|")
    for m in sorted(t3["by_methodology"]):
        d = t3["by_methodology"][m]
        s3 = d["3y"]; s5 = d["5y"]
        L.append(f"| {m} | {d['n']} | {s3['mean']} | {s3['mode']} | "
                 f"{s3['share_4_5']} | {s5['mean']} | {s5['share_4_5']} | "
                 f"{d['divergence']['rate']} |")
    L.append("")
    L.append("## Notes")
    L.append("- Sentinels excluded from numerators: -99 (content_unrecoverable), "
             "-1 (parse_fail), -2 (pending).")
    L.append("- T2 (author ranking) deferred to future Kastner-accuracy study.")
    L.append("- Primary cohort (anchor ≤ 2011) gives ≥ 15y elapsed for 5y window "
             "anchored on study.date as fallback.")
    return "\n".join(L) + "\n"


def main():
    import datetime as dt
    ap = argparse.ArgumentParser()
    ap.add_argument("--sweep", required=True)
    ap.add_argument("--master", required=True)
    ap.add_argument("--outdir", required=True)
    ap.add_argument("--primary-cutoff", type=int, default=2011)
    ap.add_argument("--secondary-cutoff", type=int, default=2015)
    args = ap.parse_args()

    outdir = Path(args.outdir)
    outdir.mkdir(parents=True, exist_ok=True)

    rows = load_sweep(args.sweep)
    print(f"[load] sweep rows: {len(rows)}")
    meth = load_master_methodology(args.master)
    print(f"[load] methodology entries: {len(meth)}")

    t1_primary = run_t1(rows, args.primary_cutoff, "primary")
    t1_secondary = run_t1(rows, args.secondary_cutoff, "secondary")
    t3 = run_t3(rows, meth)

    report = {
        "generated_at": dt.datetime.utcnow().isoformat(timespec="seconds") + "Z",
        "inputs": {"sweep": args.sweep, "master": args.master},
        "n_sweep_rows": len(rows),
        "T1": {"primary": t1_primary, "secondary": t1_secondary},
        "T3": t3,
    }

    jpath = outdir / "quality_decline_tests_v1_report.json"
    mpath = outdir / "quality_decline_tests_v1_report.md"
    p_csv = outdir / "quality_decline_t1_by_decade_primary.csv"
    s_csv = outdir / "quality_decline_t1_by_decade_secondary.csv"
    m_csv = outdir / "quality_decline_t3_by_methodology.csv"

    with open(jpath, "w", encoding="utf-8") as f:
        json.dump(report, f, indent=2)
    with open(mpath, "w", encoding="utf-8") as f:
        f.write(render_md(report))
    write_decade_csv(t1_primary, p_csv)
    write_decade_csv(t1_secondary, s_csv)
    write_methodology_csv(t3, m_csv)

    print(f"[write] {jpath}")
    print(f"[write] {mpath}")
    print(f"[write] {p_csv}")
    print(f"[write] {s_csv}")
    print(f"[write] {m_csv}")

    # console summary
    print("\n[summary] T1 primary (≤{}) overall 3y mean: {}  4–5%: {}".format(
        args.primary_cutoff,
        t1_primary["overall_3y"]["mean"],
        t1_primary["overall_3y"]["share_4_5"],
    ))
    print("[summary] T1 secondary (≤{}) overall 3y mean: {}  4–5%: {}".format(
        args.secondary_cutoff,
        t1_secondary["overall_3y"]["mean"],
        t1_secondary["overall_3y"]["share_4_5"],
    ))
    print("[summary] T3 methodology codes: {}".format(
        len(t3["by_methodology"]),
    ))


if __name__ == "__main__":
    main()
