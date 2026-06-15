#!/usr/bin/env python3
"""
sh_gates_v2.py — Short-Horizon Acceptance Gates G1-G10.

Spec: short_horizon_acceptance_gates_v2_spec.md (locked v3)

Reads driver_v8 output CSV; emits JSON gate report + writes a markdown summary.
HARD gates cause exit nonzero. Promote script reads the JSON and refuses to
merge if any HARD gate has status=FAIL.

Usage:
  python3 sh_gates_v2.py \
    --input  calibration_sh_results_v1.csv \
    --report calibration_sh_gates_v1.json \
    --md     calibration_sh_gates_v1.md \
    [--g5-truth calibration_truth_v1.csv]   # optional G5 ground-truth file

G5 truth file format (when provided):
  obs_id, human_verdict_3y, human_verdict_5y    # ints 0..5
"""
from __future__ import annotations
import argparse
import csv
import json
import re
import sys
from collections import Counter
from pathlib import Path
from statistics import mean
from typing import Optional

VALID_SOURCE_PASS = {
    "pass_c_sh_combined", "pass_c_sh_3y_only",
    "pass_c_sh_pending", "pass_c_sh_no_anchor",
}
VALID_SCORER_VERSION = {"pass_c_sonar_sh_v1", "pass_c_sonar_sh_v1_parse_fail"}

REQUIRED_COLS = [
    "obs_id", "study_id",
    "prescience_3y", "confidence_3y", "rationale_3y",
    "prescience_5y", "confidence_5y", "rationale_5y",
    "windows_diverge", "divergence_note",
    "anchor_year", "anchor_source",
    "scored_at_sh", "scorer_version_sh", "source_pass_sh",
    "raw_response_sh",
]

PENDING_RE = re.compile(r"^window_not_elapsed:[35]y:cutoff_\d{4}$")
NO_ANCHOR_RE = re.compile(r"^no_anchor:")
PARSE_FAIL_RE = re.compile(r"^parse_fail:")
HEDGE_RE = re.compile(r"\b(likely|possibly|perhaps|might|may|could)\b", re.IGNORECASE)
YEAR_RE = re.compile(r"\b(\d{4})\b")


def coerce_int(v) -> Optional[int]:
    try:
        return int(v)
    except (TypeError, ValueError):
        return None


def load_rows(path: Path) -> list[dict]:
    with open(path, newline="") as f:
        return list(csv.DictReader(f))


# ---- Gate runners -----------------------------------------------------------

def gate_result(name, status, value, threshold, hard=False, notes=""):
    return {"gate": name, "status": status, "value": value,
            "threshold": threshold, "hard": hard, "notes": notes}


def g1_schema(rows) -> list[dict]:
    fails = []
    # Required columns present
    if rows:
        missing = [c for c in REQUIRED_COLS if c not in rows[0]]
        if missing:
            return [gate_result("G1_schema", "FAIL",
                                f"missing cols: {missing}", "all 16 cols", hard=True)]
    bad_rows = 0
    bad_examples = []
    for r in rows:
        p3 = coerce_int(r["prescience_3y"])
        p5 = coerce_int(r["prescience_5y"])
        sp = r["source_pass_sh"]
        sv = r["scorer_version_sh"]
        ok = True
        # invariants
        if p3 == -2:
            if r["confidence_3y"] != "" or not PENDING_RE.match(r["rationale_3y"] or ""):
                ok = False
        if p5 == -2:
            if r["confidence_5y"] != "" or not PENDING_RE.match(r["rationale_5y"] or ""):
                ok = False
        if p3 == -1:
            r3 = r["rationale_3y"] or ""
            if not (NO_ANCHOR_RE.match(r3) or PARSE_FAIL_RE.match(r3)):
                ok = False
        if p5 == -1:
            r5 = r["rationale_5y"] or ""
            if not (NO_ANCHOR_RE.match(r5) or PARSE_FAIL_RE.match(r5)):
                ok = False
        if sp == "pass_c_sh_pending" and not (p3 == -2 and p5 == -2):
            ok = False
        if sp == "pass_c_sh_no_anchor" and not (p3 == -1 and p5 == -1):
            ok = False
        wd = r["windows_diverge"]
        if wd == "true" and not (p3 is not None and 0 <= p3 <= 5 and
                                  p5 is not None and 0 <= p5 <= 5 and
                                  (r["divergence_note"] or "").strip() != ""):
            ok = False
        if sp not in VALID_SOURCE_PASS and sv != "pass_c_sonar_sh_v1_parse_fail":
            ok = False
        if not ok:
            bad_rows += 1
            if len(bad_examples) < 5:
                bad_examples.append({"obs_id": r["obs_id"],
                                      "p3": p3, "p5": p5, "sp": sp, "sv": sv})
    return [gate_result("G1_schema",
                        "PASS" if bad_rows == 0 else "FAIL",
                        f"{bad_rows} invariant violations",
                        "0 violations",
                        hard=True,
                        notes=f"examples: {bad_examples}" if bad_examples else "")]


def scored_cohort(rows, horizon):
    """Rows with a real 0..5 score in the given horizon."""
    col = f"prescience_{horizon}y"
    out = []
    for r in rows:
        v = coerce_int(r[col])
        if v is not None and 0 <= v <= 5:
            out.append(r)
    return out


def g2(rows) -> list[dict]:
    out = []
    for h in (3, 5):
        s = scored_cohort(rows, h)
        if not s:
            out.append(gate_result(f"G2a_mean_{h}y", "SKIP", "no scored rows",
                                    "[1.5, 3.5]"))
            out.append(gate_result(f"G2b_mode_{h}y", "SKIP", "no scored rows",
                                    "not 0 and not 5"))
            out.append(gate_result(f"G2c_balance_{h}y", "SKIP", "no scored rows",
                                    "max/min_nonzero ≤ 4.0"))
            continue
        scores = [coerce_int(r[f"prescience_{h}y"]) for r in s]
        m = mean(scores)
        out.append(gate_result(f"G2a_mean_{h}y",
                               "PASS" if 1.5 <= m <= 3.5 else "FLAG",
                               round(m, 3), "[1.5, 3.5]"))
        ctr = Counter(scores)
        mode = ctr.most_common(1)[0][0]
        out.append(gate_result(f"G2b_mode_{h}y",
                               "PASS" if mode not in (0, 5) else "FLAG",
                               mode, "not 0 and not 5"))
        nonzero = [c for s_, c in ctr.items() if s_ != 0 and c > 0]
        if nonzero:
            r = max(ctr.values()) / min(nonzero)
            out.append(gate_result(f"G2c_balance_{h}y",
                                   "PASS" if r <= 4.0 else "FLAG",
                                   round(r, 3), "≤ 4.0"))
        else:
            out.append(gate_result(f"G2c_balance_{h}y", "FLAG",
                                   "no nonzero classes", "≤ 4.0"))
    return out


def g3(rows) -> list[dict]:
    out = []
    for h in (3, 5):
        s = scored_cohort(rows, h)
        if not s:
            out.append(gate_result(f"G3a_class_presence_{h}y", "SKIP",
                                    "no scored rows", "{1,2,3} all present"))
            out.append(gate_result(f"G3b_monotonicity_{h}y", "SKIP",
                                    "no scored rows", "conf@5 ≥ conf@0"))
            continue
        confs = [coerce_int(r[f"confidence_{h}y"]) for r in s]
        confs = [c for c in confs if c is not None]
        present = set(confs)
        missing = {1, 2, 3} - present
        out.append(gate_result(f"G3a_class_presence_{h}y",
                               "PASS" if not missing else "FLAG",
                               f"present: {sorted(present)}",
                               "{1,2,3} all present"))
        s5 = [coerce_int(r[f"confidence_{h}y"]) for r in s
              if coerce_int(r[f"prescience_{h}y"]) == 5]
        s0 = [coerce_int(r[f"confidence_{h}y"]) for r in s
              if coerce_int(r[f"prescience_{h}y"]) == 0]
        s5 = [c for c in s5 if c is not None]
        s0 = [c for c in s0 if c is not None]
        if s5 and s0:
            mc5 = mean(s5); mc0 = mean(s0)
            out.append(gate_result(f"G3b_monotonicity_{h}y",
                                   "PASS" if mc5 >= mc0 else "FLAG",
                                   f"conf@5={round(mc5,2)} vs conf@0={round(mc0,2)}",
                                   "conf@5 ≥ conf@0"))
        else:
            out.append(gate_result(f"G3b_monotonicity_{h}y", "SKIP",
                                   f"score=5 n={len(s5)} score=0 n={len(s0)}",
                                   "needs both score=0 and score=5"))
    return out


def g4(rows) -> list[dict]:
    """Rationale quality: ≥ 90% of 50 sampled scored rows pass all 3 checks."""
    import random
    rng = random.Random(20260615)
    out = []
    for h in (3, 5):
        s = scored_cohort(rows, h)
        if len(s) == 0:
            out.append(gate_result(f"G4_rationale_{h}y", "SKIP",
                                    "no scored rows", "≥ 90% pass"))
            continue
        sample = rng.sample(s, min(50, len(s)))
        ok = 0
        for r in sample:
            anchor = coerce_int(r["anchor_year"])
            text = r[f"rationale_{h}y"] or ""
            if len(text) < 40:
                continue
            years = [int(y) for y in YEAR_RE.findall(text)]
            if anchor is None:
                continue
            in_window = any(anchor <= y <= anchor + h for y in years)
            if not in_window:
                continue
            # hedge check: hedge phrases ok IF concrete year is also present
            has_hedge = HEDGE_RE.search(text) is not None
            if has_hedge and not years:
                continue
            ok += 1
        pct = ok / len(sample) if sample else 0
        out.append(gate_result(f"G4_rationale_{h}y",
                               "PASS" if pct >= 0.90 else "FLAG",
                               f"{ok}/{len(sample)} = {round(pct*100,1)}%",
                               "≥ 90%"))
    return out


def g5(rows, truth_path: Path | None) -> list[dict]:
    out = []
    if not truth_path or not truth_path.exists():
        out.append(gate_result("G5_accuracy_3y", "DEFERRED",
                                "no truth file provided", "≥ 65%", hard=True))
        out.append(gate_result("G5_accuracy_5y", "DEFERRED",
                                "no truth file provided", "≥ 65%", hard=True))
        return out
    truth = {}
    with open(truth_path, newline="") as f:
        for r in csv.DictReader(f):
            oid = r["obs_id"]
            truth[oid] = (coerce_int(r.get("human_verdict_3y")),
                          coerce_int(r.get("human_verdict_5y")))
    for h_idx, h in enumerate((3, 5)):
        match = 0; total = 0
        for r in rows:
            t3, t5 = truth.get(r["obs_id"], (None, None))
            t = t3 if h == 3 else t5
            p = coerce_int(r[f"prescience_{h}y"])
            if t is None or p is None or p < 0:
                continue
            total += 1
            if p == t:
                match += 1
        pct = match / total if total else 0
        out.append(gate_result(f"G5_accuracy_{h}y",
                               "PASS" if pct >= 0.65 else "FAIL",
                               f"{match}/{total} = {round(pct*100,1)}%",
                               "≥ 65%", hard=True))
    return out


def g6(rows) -> list[dict]:
    bad = 0; bad_examples = []
    for r in rows:
        sp = r["source_pass_sh"]
        sv = r["scorer_version_sh"]
        # parse-fail rows have scorer_version flagged; source_pass still must be enum
        if sp not in VALID_SOURCE_PASS:
            bad += 1
            if len(bad_examples) < 5:
                bad_examples.append({"obs_id": r["obs_id"], "sp": sp, "sv": sv})
        if sv not in VALID_SCORER_VERSION:
            bad += 1
            if len(bad_examples) < 5:
                bad_examples.append({"obs_id": r["obs_id"], "sp": sp, "sv": sv})
    return [gate_result("G6_source_pass_labeling",
                        "PASS" if bad == 0 else "FAIL",
                        f"{bad} off-vocab values",
                        f"all in {VALID_SOURCE_PASS} & {VALID_SCORER_VERSION}",
                        hard=True,
                        notes=f"examples: {bad_examples}" if bad_examples else "")]


def g7(rows) -> list[dict]:
    out = []
    total = len(rows) or 1
    for h in (3, 5):
        n_pending = sum(1 for r in rows
                         if coerce_int(r[f"prescience_{h}y"]) == -2)
        rate = n_pending / total
        out.append(gate_result(f"G7_pending_{h}y",
                               "PASS" if rate <= 0.35 else "FLAG",
                               f"{n_pending}/{total} = {round(rate*100,1)}%",
                               "≤ 35%"))
    return out


def g8(rows) -> list[dict]:
    """Both-elapsed cohort: rows with both p3 and p5 in 0..5."""
    out = []
    elapsed = []
    for r in rows:
        p3 = coerce_int(r["prescience_3y"])
        p5 = coerce_int(r["prescience_5y"])
        if p3 is not None and p5 is not None and 0 <= p3 <= 5 and 0 <= p5 <= 5:
            elapsed.append((r, p3, p5))
    n = len(elapsed)
    if n == 0:
        out.append(gate_result("G8a_diverge_rate", "SKIP",
                                "no both-elapsed rows", "2-25%", hard=True))
        out.append(gate_result("G8b_model_vs_mechanical", "SKIP",
                                "no both-elapsed rows", "≥ 80%", hard=False))
        return out
    n_diverge = sum(1 for r, _, _ in elapsed if r["windows_diverge"] == "true")
    rate = n_diverge / n
    if rate < 0.02:
        status = "FLAG"
    elif rate <= 0.25:
        status = "PASS"
    else:
        status = "FAIL"
    out.append(gate_result("G8a_diverge_rate", status,
                           f"{n_diverge}/{n} = {round(rate*100,1)}%",
                           "2-25%", hard=True))
    # G8b: model vs mechanical
    agree = 0
    mismatches = []
    for r, p3, p5 in elapsed:
        model_div = r["windows_diverge"] == "true"
        mech_div = abs(p3 - p5) >= 2
        if model_div == mech_div:
            agree += 1
        else:
            if len(mismatches) < 20:
                mismatches.append({"obs_id": r["obs_id"], "p3": p3, "p5": p5,
                                    "model_div": model_div, "mech_div": mech_div})
    pct = agree / n
    if pct >= 0.80:
        st = "PASS"
    elif pct >= 0.60:
        st = "FLAG"
    else:
        st = "FLAG_HARD"
    out.append(gate_result("G8b_model_vs_mechanical", st,
                           f"{agree}/{n} = {round(pct*100,1)}%",
                           "≥ 80%",
                           notes=f"mismatches: {len(mismatches)} (first 20 saved)"))
    return out


def g9(rows) -> list[dict]:
    """Diverge=true rows must name a year in [A+1, A+5] in divergence_note."""
    diverge_rows = [r for r in rows if r["windows_diverge"] == "true"]
    if not diverge_rows:
        return [gate_result("G9_chronological_monotonicity", "SKIP",
                            "no diverge=true rows", "≥ 90%")]
    ok = 0
    for r in diverge_rows:
        a = coerce_int(r["anchor_year"])
        note = r["divergence_note"] or ""
        years = [int(y) for y in YEAR_RE.findall(note)]
        if a is None:
            continue
        if any(a + 1 <= y <= a + 5 for y in years):
            ok += 1
    pct = ok / len(diverge_rows)
    return [gate_result("G9_chronological_monotonicity",
                        "PASS" if pct >= 0.90 else "FLAG",
                        f"{ok}/{len(diverge_rows)} = {round(pct*100,1)}%",
                        "≥ 90%")]


def g10(rows) -> list[dict]:
    """Score-trajectory plausibility on both-elapsed cohort."""
    elapsed = []
    for r in rows:
        p3 = coerce_int(r["prescience_3y"])
        p5 = coerce_int(r["prescience_5y"])
        if p3 is not None and p5 is not None and 0 <= p3 <= 5 and 0 <= p5 <= 5:
            elapsed.append((p3, p5))
    n = len(elapsed) or 1
    labels = Counter()
    for p3, p5 in elapsed:
        if p3 == 0 and p5 == 0:
            labels["both_wrong"] += 1
        elif p3 == 0 and p5 >= 1:
            labels["late_vindication"] += 1
        elif p3 >= 1 and p5 == 0:
            labels["reversal"] += 1
        elif p3 >= 1 and p5 >= 1 and abs(p3 - p5) <= 1:
            labels["stable"] += 1
        else:
            labels["shift"] += 1
    reversal_rate = labels["reversal"] / n if n else 0
    return [gate_result("G10_trajectory_plausibility",
                        "PASS" if reversal_rate <= 0.10 else "FLAG",
                        dict(labels),
                        "reversal ≤ 10%",
                        notes=f"reversal_rate={round(reversal_rate*100,1)}%")]


# ---- Orchestrator -----------------------------------------------------------

ALL_GATES = ["g1", "g2", "g3", "g4", "g5", "g6", "g7", "g8", "g9", "g10"]


def run_all(rows, truth_path=None) -> list[dict]:
    results = []
    results += g1_schema(rows)
    results += g2(rows)
    results += g3(rows)
    results += g4(rows)
    results += g5(rows, truth_path)
    results += g6(rows)
    results += g7(rows)
    results += g8(rows)
    results += g9(rows)
    results += g10(rows)
    return results


def emit_md(results, total_rows, path: Path):
    hard_fail = sum(1 for r in results if r["hard"] and r["status"] == "FAIL")
    soft_fail = sum(1 for r in results if not r["hard"] and r["status"] in ("FLAG", "FAIL"))
    lines = ["# Short-Horizon Acceptance Gate Report", ""]
    lines.append(f"- Total rows: {total_rows}")
    lines.append(f"- HARD fails: {hard_fail}")
    lines.append(f"- Soft flags: {soft_fail}")
    lines.append(f"- Promote eligibility: "
                 f"{'BLOCKED' if hard_fail else 'CLEAR'}")
    lines.append("")
    lines.append("| Gate | Status | Value | Threshold | Hard |")
    lines.append("|---|---|---|---|---|")
    for r in results:
        lines.append(f"| {r['gate']} | {r['status']} | `{r['value']}` "
                     f"| {r['threshold']} | {'**Y**' if r['hard'] else ''} |")
    path.write_text("\n".join(lines))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--input",  required=True)
    ap.add_argument("--report", required=True, help="JSON output path")
    ap.add_argument("--md",     default=None, help="Markdown summary path")
    ap.add_argument("--g5-truth", default=None,
                    help="Optional CSV with human_verdict_3y/5y per obs_id")
    args = ap.parse_args()

    rows = load_rows(Path(args.input))
    truth_path = Path(args.g5_truth) if args.g5_truth else None
    print(f"[gates] loaded {len(rows)} rows from {args.input}")

    results = run_all(rows, truth_path)
    hard_fails = [r for r in results if r["hard"] and r["status"] == "FAIL"]
    soft_fails = [r for r in results if not r["hard"] and r["status"] in ("FLAG", "FAIL")]
    print(f"[gates] HARD fails: {len(hard_fails)}")
    print(f"[gates] soft flags: {len(soft_fails)}")

    report_path = Path(args.report)
    report_path.parent.mkdir(parents=True, exist_ok=True)
    report_path.write_text(json.dumps({
        "input": args.input,
        "total_rows": len(rows),
        "hard_fails": len(hard_fails),
        "soft_flags": len(soft_fails),
        "promote_eligible": len(hard_fails) == 0,
        "results": results,
    }, indent=2))
    print(f"[write] {report_path}")

    if args.md:
        emit_md(results, len(rows), Path(args.md))
        print(f"[write] {args.md}")

    for r in results:
        prefix = "✓" if r["status"] == "PASS" else "✗" if r["status"] in ("FAIL", "FLAG_HARD") else "·"
        print(f"  {prefix} {r['gate']:32s} {r['status']:9s} {r['value']}")

    sys.exit(1 if hard_fails else 0)


if __name__ == "__main__":
    main()
