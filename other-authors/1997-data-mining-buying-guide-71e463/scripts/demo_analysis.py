#!/usr/bin/env python3
"""
Demo analysis for: Enterprise Data Mining Buying Guide: 1997 Edition
Study ID: 1997-data-mining-buying-guide-71e463
"""
import csv
from pathlib import Path

BASE = Path(__file__).parent.parent

def load_csv(name):
    with open(BASE / "data" / f"{name}.csv") as f:
        return list(csv.DictReader(f))

def main():
    print("=" * 60)
    print("Aberdeen Data Mining Buying Guide 1997 — Analysis")
    print("=" * 60)

    obs = load_csv("observations")
    entities = load_csv("entities")
    technologies = load_csv("technologies")

    # Vendor fate (all entities)
    print("\n--- Vendor Outcomes (all 8 profiled + Aberdeen) ---")
    for e in entities:
        print(f"  {e['entity_name']}: {e['status']} -> {e['successor']}")

    # Algorithm lifecycle
    algo_techs = [t for t in technologies if t["tech_name"] in 
                  ["Decision Trees", "Neural Networks", "Association Rules", "Clustering Algorithms"]]
    print("\n--- Algorithm Lifecycle (1997 → 2026) ---")
    for t in algo_techs:
        print(f"  {t['tech_name']}: {t['lifecycle_at_study']} -> {t['lifecycle_current']}")

    # Framework factors
    ff = [o for o in obs if o["observation_type"] == "framework-factor"]
    print("\n--- Evaluation Framework Criteria ---")
    for o in ff:
        print(f"  [{o['obs_id']}] {o['metric_name']}: {o['metric_value']}")

    # Predictions vs outcomes
    preds = [o for o in obs if o["observation_type"] == "viability-prediction"]
    outcomes = [o for o in obs if o["observation_type"] == "actual-outcome"]
    print(f"\n--- Prediction Tracking ---")
    print(f"  Predictions: {len(preds)}  |  Outcomes: {len(outcomes)}")
    print("\n  Key vendor outcomes:")
    for o in outcomes:
        if "fate" in o["metric_name"].lower():
            print(f"    {o['metric_name']}: {o['metric_value']}")

if __name__ == "__main__":
    main()
