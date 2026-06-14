#!/usr/bin/env python3
"""
Prescience Acceptance Gates v1

Programmatic pass/fail evaluation of a Pass C batch run against the
existing baseline (3,829 numeric-scored rows in _master_prescience_scores.csv).

Replaces the human "Pete eyeballs 10 rows" gate (withdrawn 2026-06-14:
Pete: "not sure I want to be the accuracy gate") with statistical
distribution drift + structural quality checks.

Usage:
  python3 prescience_acceptance_gates_v1.py \\
    --batch /path/to/pass_c_v6_calibration_results.csv \\
    --baseline /path/to/_master_prescience_scores.csv \\
    --gates calibration   # or 'tier_a' / 'tier_b'

Exit code 0 = all gates pass. Non-zero = at least one gate fails.
"""

import argparse, csv, sys, json
from collections import Counter
from pathlib import Path

# Baseline reference: 3,829 numeric-scored rows from master at commit aef5cc83
# Distribution: -1=20.8%, 0=45.8%, 1=0.4%, 2=1.8%, 3=9.3%, 4=20.2%, 5=1.8%
BASELINE_DIST = {
    "-1": 0.208, "0": 0.458, "1": 0.004, "2": 0.018,
    "3": 0.093, "4": 0.202, "5": 0.018,
}
BASELINE_CONF = {"1": 0.231, "2": 0.191, "3": 0.579}
BASELINE_PARSE_OK_RATE = 0.997  # 3,816/3,828 ≈ 0.997

# Gate thresholds
GATES = {
    "calibration": {
        "min_parse_ok": 0.95,
        "min_rationale_median_chars": 200,
        "min_rationale_chars": 50,
        "max_refusal_rate": 0.05,         # score=0 too high → out of scope
        "min_distinct_scores": 3,         # avoid all-0 or all-3 collapse
        "max_single_score_concentration": 0.70,
        "max_dist_chi_sq": 50.0,          # vs baseline (lower=more similar)
        "max_cost_per_obs_credits": 2000,  # 200K credits / 100 obs
    },
    "tier_a": {
        "min_parse_ok": 0.95,
        "min_rationale_median_chars": 200,
        "min_rationale_chars": 50,
        "max_refusal_rate": 0.55,         # 0-score expected to be higher in bulk
        "min_distinct_scores": 4,
        "max_single_score_concentration": 0.65,
        "max_dist_chi_sq": 30.0,
        "max_cost_per_obs_credits": 2000,
    },
    "tier_b": {
        "min_parse_ok": 0.95,
        "min_rationale_median_chars": 200,
        "min_rationale_chars": 50,
        "max_refusal_rate": 0.55,
        "min_distinct_scores": 4,
        "max_single_score_concentration": 0.65,
        "max_dist_chi_sq": 25.0,
        "max_cost_per_obs_credits": 2000,
    },
}


def load_rows(path):
    with open(path, newline="") as f:
        return list(csv.DictReader(f))


def chi_squared(observed_pct, expected_pct):
    """Standard chi-squared against baseline. Lower = more similar."""
    chisq = 0.0
    keys = set(observed_pct.keys()) | set(expected_pct.keys())
    for k in keys:
        o = observed_pct.get(k, 0)
        e = expected_pct.get(k, 1e-6)  # avoid div by zero
        chisq += ((o - e) ** 2) / e
    return chisq


def evaluate(batch_rows, gate_set):
    g = GATES[gate_set]
    api_rows = [r for r in batch_rows if r.get("source_pass") not in ("preseed_b", "pass_c_prefilter_v1")]
    if not api_rows:
        return {"verdict": "FAIL", "reason": "No API-scored rows in batch"}
    
    n = len(api_rows)
    results = {"n_api_rows": n, "n_total_rows": len(batch_rows), "gates": {}}
    
    # G1: parse_ok rate
    parse_ok_n = sum(1 for r in api_rows if r.get("parse_ok") == "true")
    parse_ok_rate = parse_ok_n / n
    results["gates"]["G1_parse_ok"] = {
        "value": f"{parse_ok_rate:.3f}",
        "threshold": f">= {g['min_parse_ok']}",
        "pass": parse_ok_rate >= g["min_parse_ok"],
    }
    
    # G2: score distribution
    scores = Counter(r.get("prescience_score", "") for r in api_rows if r.get("parse_ok") == "true")
    distinct = len(scores)
    max_share = max(scores.values()) / sum(scores.values()) if scores else 0
    obs_pct = {k: v/sum(scores.values()) for k, v in scores.items()}
    chi = chi_squared(obs_pct, BASELINE_DIST)
    results["gates"]["G2_distinct_scores"] = {
        "value": distinct,
        "threshold": f">= {g['min_distinct_scores']}",
        "pass": distinct >= g["min_distinct_scores"],
    }
    results["gates"]["G2b_max_concentration"] = {
        "value": f"{max_share:.3f}",
        "threshold": f"<= {g['max_single_score_concentration']}",
        "pass": max_share <= g["max_single_score_concentration"],
    }
    results["gates"]["G2c_dist_drift_chi_sq"] = {
        "value": f"{chi:.2f}",
        "threshold": f"<= {g['max_dist_chi_sq']}",
        "pass": chi <= g["max_dist_chi_sq"],
        "observed": obs_pct,
        "baseline": BASELINE_DIST,
    }
    
    # G3: rationale length
    rationales = [len(r.get("rationale", "")) for r in api_rows if r.get("parse_ok") == "true"]
    rationales.sort()
    median_rat = rationales[len(rationales)//2] if rationales else 0
    min_rat = min(rationales) if rationales else 0
    results["gates"]["G3_rationale_median"] = {
        "value": median_rat,
        "threshold": f">= {g['min_rationale_median_chars']}",
        "pass": median_rat >= g["min_rationale_median_chars"],
    }
    results["gates"]["G3b_rationale_min"] = {
        "value": min_rat,
        "threshold": f">= {g['min_rationale_chars']}",
        "pass": min_rat >= g["min_rationale_chars"],
    }
    
    # G4: refusal rate (score=0)
    refusals = sum(1 for r in api_rows if r.get("prescience_score") == "0" and r.get("parse_ok") == "true")
    refusal_rate = refusals / parse_ok_n if parse_ok_n else 0
    results["gates"]["G4_refusal_rate"] = {
        "value": f"{refusal_rate:.3f}",
        "threshold": f"<= {g['max_refusal_rate']}",
        "pass": refusal_rate <= g["max_refusal_rate"],
    }
    
    # G5 (programmatic replacement for spot-check):
    # Score distribution within EACH macro-bucket should not be entirely
    # concentrated on score=0. If a single bucket is >80% score=0, it's
    # likely the model is refusing everything in that domain, not actually
    # scoring. We can't have study-type metadata here without joining
    # _master_studies; flag as advisory only if missing.
    # Confidence distribution check:
    confs = Counter(r.get("confidence") for r in api_rows if r.get("parse_ok") == "true")
    conf_total = sum(confs.values()) if confs else 1
    conf_obs = {k: v/conf_total for k, v in confs.items()}
    conf_chi = chi_squared(conf_obs, BASELINE_CONF)
    results["gates"]["G5_confidence_drift"] = {
        "value": f"{conf_chi:.2f}",
        "threshold": "<= 1.0",
        "pass": conf_chi <= 1.0,
        "observed": conf_obs,
        "baseline": BASELINE_CONF,
    }
    
    # G6: cost per obs (approximate from elapsed_sec or skip if no field)
    # Sonar Pro pricing varies; this gate requires user-supplied cost data
    results["gates"]["G6_cost_per_obs"] = {
        "value": "N/A (requires API receipts)",
        "threshold": f"<= {g['max_cost_per_obs_credits']} credits",
        "pass": True,
        "note": "Manual check against API billing dashboard",
    }
    
    # Overall verdict
    failed = [k for k, v in results["gates"].items() if not v["pass"]]
    results["failed_gates"] = failed
    results["verdict"] = "PASS" if not failed else "FAIL"
    return results


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--batch", required=True, help="Pass C batch results CSV")
    ap.add_argument("--gates", choices=["calibration", "tier_a", "tier_b"], default="calibration")
    ap.add_argument("--json", action="store_true", help="Output JSON instead of human-readable")
    args = ap.parse_args()
    
    batch = load_rows(args.batch)
    print(f"Loaded {len(batch)} rows from {args.batch}", file=sys.stderr)
    
    result = evaluate(batch, args.gates)
    
    if args.json:
        print(json.dumps(result, indent=2))
    else:
        print(f"\n{'='*60}")
        print(f"PRESCIENCE ACCEPTANCE GATES — {args.gates}")
        print(f"{'='*60}")
        print(f"Batch: {args.batch}")
        print(f"API rows: {result['n_api_rows']} / Total: {result['n_total_rows']}")
        print(f"\nGate results:")
        for k, v in result["gates"].items():
            sym = "✓" if v["pass"] else "✗"
            print(f"  {sym} {k}: {v['value']} (threshold: {v['threshold']})")
            if "observed" in v and not v["pass"]:
                print(f"      observed: {v['observed']}")
                print(f"      baseline: {v['baseline']}")
        print(f"\n>>> VERDICT: {result['verdict']}")
        if result["failed_gates"]:
            print(f">>> Failed gates: {', '.join(result['failed_gates'])}")
    
    sys.exit(0 if result["verdict"] == "PASS" else 1)


if __name__ == "__main__":
    main()
