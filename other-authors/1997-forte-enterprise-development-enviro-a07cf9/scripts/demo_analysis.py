#!/usr/bin/env python3
"""
Demo analysis for: Forte Enterprise Development Environment (1997)
Study ID: 1997-forte-enterprise-development-enviro-a07cf9
"""
import csv, json, os

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def load_csv(name):
    rows = []
    with open(os.path.join(BASE, "data", f"{name}.csv")) as f:
        reader = csv.DictReader(f)
        for row in reader:
            rows.append(row)
    return rows

def main():
    obs = load_csv("observations")
    entities = load_csv("entities")
    techs = load_csv("technologies")

    print("=== Forte HADE Study — Demo Analysis ===\n")
    
    # Predictions vs outcomes
    preds = [o for o in obs if o["observation_type"] == "viability-prediction"]
    outcomes = [o for o in obs if o["observation_type"] == "actual-outcome"]
    print(f"Viability predictions: {len(preds)}")
    print(f"Verified actual outcomes: {len(outcomes)}")
    
    print("\n--- Actual Outcomes ---")
    for o in outcomes:
        print(f"  [{o['year_observed']}] {o['metric_name']}: {o['metric_value']}")
    
    print("\n--- Technology Lifecycle at Study vs Current ---")
    for t in techs:
        print(f"  {t['tech_name']}: {t['lifecycle_at_study']} -> {t['lifecycle_current']}")
    
    print("\n--- Entity Status ---")
    for e in entities:
        print(f"  {e['entity_name']} ({e['status']}) -> {e['successor']}")
    
    print("\n--- Market Data Points ---")
    for o in obs:
        if o["observation_type"] == "market-data":
            print(f"  {o['metric_name']}: {o['metric_value']}")

if __name__ == "__main__":
    main()
