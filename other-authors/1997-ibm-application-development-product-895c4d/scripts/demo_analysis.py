#!/usr/bin/env python3
"""
Demo analysis: IBM Application Development Product Family (1997)
Study ID: 1997-ibm-application-development-product-895c4d
"""
import csv, os

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def load_csv(name):
    with open(os.path.join(BASE, "data", f"{name}.csv")) as f:
        return list(csv.DictReader(f))

def main():
    obs = load_csv("observations")
    techs = load_csv("technologies")

    print("=== IBM AD Product Family Study — Demo Analysis ===\n")
    
    outcomes = [o for o in obs if o["observation_type"] == "actual-outcome"]
    preds = [o for o in obs if o["observation_type"] == "viability-prediction"]
    
    print(f"Predictions: {len(preds)}, Outcomes: {len(outcomes)}")
    
    print("\n--- Technology Lifecycle Summary ---")
    for t in techs:
        print(f"  {t['tech_name']}:")
        print(f"    1997: {t['lifecycle_at_study']} -> Current: {t['lifecycle_current']}")
    
    print("\n--- Historical Outcomes ---")
    for o in outcomes:
        print(f"  [{o['year_observed']}] {o['metric_name']}: {o['metric_value']}")
    
    print("\n--- Aberdeen Predictions ---")
    for p in preds:
        print(f"  {p['metric_name']}: {p['metric_value']}")

if __name__ == "__main__":
    main()
