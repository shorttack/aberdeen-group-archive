#!/usr/bin/env python3
"""
Demo analysis for: DEC LinkWorks WebWorker — An Object Framework that Tames the Web
Study ID: 1997-dec-linkworks-webworker---an-object-db2d2a
"""

import csv
from pathlib import Path

BASE = Path(__file__).parent.parent

def load_csv(name):
    with open(BASE / "data" / f"{name}.csv") as f:
        return list(csv.DictReader(f))

def main():
    print("=" * 60)
    print("DEC LinkWorks WebWorker — Aberdeen Vendor Profile Analysis")
    print("=" * 60)

    obs = load_csv("observations")
    entities = load_csv("entities")
    technologies = load_csv("technologies")

    # Entity status
    print("\n--- Entity Outcomes ---")
    for e in entities:
        print(f"  {e['entity_name']}: {e['status']} -> {e['successor']}")

    # Technology fate
    print("\n--- Technology Lifecycle Changes ---")
    for t in technologies:
        print(f"  {t['tech_name']}: {t['lifecycle_at_study']} -> {t['lifecycle_current']}")

    # Prediction accuracy
    preds = [o for o in obs if o["observation_type"] == "viability-prediction"]
    outcomes = [o for o in obs if o["observation_type"] == "actual-outcome"]
    print(f"\n--- Prediction Tracking ---")
    print(f"  Predictions: {len(preds)}  |  Outcomes recorded: {len(outcomes)}")

    # Key technology assessments
    print("\n--- Technology Assessments ---")
    for o in obs:
        if o["observation_type"] == "technology-assessment":
            print(f"  {o['metric_name']}: {o['metric_value']}")

if __name__ == "__main__":
    main()
