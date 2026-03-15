#!/usr/bin/env python3
"""
Demo analysis: HP NT Strategy White Paper (1997)
Study ID: 1997-hewlett-packard's-strategy-to-surpa-905013
"""
import csv, os

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def load_csv(name):
    with open(os.path.join(BASE, "data", f"{name}.csv")) as f:
        return list(csv.DictReader(f))

def main():
    obs = load_csv("observations")
    entities = load_csv("entities")
    techs = load_csv("technologies")

    print("=== HP NT Strategy Study — Demo Analysis ===\n")
    preds = [o for o in obs if o["observation_type"] == "viability-prediction"]
    outcomes = [o for o in obs if o["observation_type"] == "actual-outcome"]
    mkt = [o for o in obs if o["observation_type"] == "market-data"]
    
    print(f"Predictions: {len(preds)}, Outcomes: {len(outcomes)}, Market data: {len(mkt)}")
    
    print("\n--- Market Sizing (1997) ---")
    for o in mkt:
        print(f"  {o['metric_name']}: {o['metric_value']}")
    
    print("\n--- Predictions vs Actual ---")
    for p in preds:
        print(f"  PRED: {p['metric_name']}: {p['metric_value']}")
    for o in outcomes:
        print(f"  ACTUAL [{o['year_observed']}]: {o['metric_name']}: {o['metric_value']}")
    
    print("\n--- Company Fates ---")
    for e in entities:
        if e["status"] != "active":
            print(f"  {e['entity_name']}: {e['status']} -> {e['successor']}")

if __name__ == "__main__":
    main()
