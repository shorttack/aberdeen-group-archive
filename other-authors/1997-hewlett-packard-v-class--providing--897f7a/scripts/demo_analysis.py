#!/usr/bin/env python3
"""
Demo analysis for: HP V-Class Enterprise Server Profile (1997)
Study ID: 1997-hewlett-packard-v-class--providing--897f7a
"""
import csv, os

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def load_csv(name):
    rows = []
    with open(os.path.join(BASE, "data", f"{name}.csv")) as f:
        for row in csv.DictReader(f):
            rows.append(row)
    return rows

def main():
    obs = load_csv("observations")
    techs = load_csv("technologies")
    entities = load_csv("entities")

    print("=== HP V-Class Study — Demo Analysis ===\n")
    
    benchmarks = [o for o in obs if o["observation_type"] == "benchmark-result"]
    predictions = [o for o in obs if o["observation_type"] == "viability-prediction"]
    outcomes = [o for o in obs if o["observation_type"] == "actual-outcome"]
    
    print(f"Benchmark data points: {len(benchmarks)}")
    print(f"Viability predictions: {len(predictions)}")
    print(f"Actual outcomes: {len(outcomes)}")
    
    print("\n--- TPC-D Benchmark Comparison (1997) ---")
    for o in benchmarks:
        if "TPC-D" in o["metric_name"] or "tpm" in o["metric_value"]:
            print(f"  {o['entity_id']}: {o['metric_name']}: {o['metric_value']}")
    
    print("\n--- Vendor Predictions vs Outcomes ---")
    for p in predictions:
        print(f"  PRED [{p['year_observed']}]: {p['metric_name']}: {p['metric_value']}")
    for o in outcomes:
        print(f"  OUTCOME [{o['year_observed']}]: {o['metric_name']}: {o['metric_value']}")
    
    print("\n--- Technology Fates ---")
    for t in techs:
        print(f"  {t['tech_name']}: {t['lifecycle_at_study']} -> {t['lifecycle_current']}")

if __name__ == "__main__":
    main()
