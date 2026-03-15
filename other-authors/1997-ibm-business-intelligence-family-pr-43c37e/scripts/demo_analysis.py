#!/usr/bin/env python3
"""
Demo analysis: IBM Business Intelligence Family (1997)
Study ID: 1997-ibm-business-intelligence-family-pr-43c37e
"""
import csv, os

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def load_csv(name):
    with open(os.path.join(BASE, "data", f"{name}.csv")) as f:
        return list(csv.DictReader(f))

def main():
    obs = load_csv("observations")
    techs = load_csv("technologies")
    entities = load_csv("entities")

    print("=== IBM BI Family Study — Demo Analysis ===\n")
    
    outcomes = [o for o in obs if o["observation_type"] == "actual-outcome"]
    preds = [o for o in obs if o["observation_type"] == "viability-prediction"]
    frameworks = [o for o in obs if o["observation_type"] == "framework-factor"]
    
    print(f"Predictions: {len(preds)}, Outcomes: {len(outcomes)}, Framework factors: {len(frameworks)}")
    
    print("\n--- Key Aberdeen Framework Predictions ---")
    for f in frameworks:
        print(f"  {f['metric_name']}: {f['metric_value'][:80]}")
    
    print("\n--- Historical Outcomes ---")
    for o in outcomes:
        print(f"  [{o['year_observed']}] {o['metric_name']}: {o['metric_value'][:80]}")
    
    print("\n--- Technology Fates ---")
    for t in techs:
        print(f"  {t['tech_name']}: {t['lifecycle_at_study']} -> {t['lifecycle_current']}")

if __name__ == "__main__":
    main()
