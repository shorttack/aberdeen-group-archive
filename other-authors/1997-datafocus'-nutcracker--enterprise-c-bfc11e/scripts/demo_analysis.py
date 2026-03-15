#!/usr/bin/env python3
"""
Demo analysis for: DataFocus NuTCRACKER: Enterprise-Class Unix Applications for NT
Study ID: 1997-datafocus'-nutcracker--enterprise-c-bfc11e
"""
import csv
from pathlib import Path

BASE = Path(__file__).parent.parent

def load_csv(name):
    with open(BASE / "data" / f"{name}.csv") as f:
        return list(csv.DictReader(f))

def main():
    print("=" * 60)
    print("DataFocus NuTCRACKER — Aberdeen White Paper Analysis")
    print("=" * 60)

    obs = load_csv("observations")
    entities = load_csv("entities")
    technologies = load_csv("technologies")

    # Cost/Performance benchmarks
    benchmarks = [o for o in obs if o["observation_type"] == "benchmark-result"]
    print("\n--- Cost & Performance Benchmarks (1997) ---")
    for b in benchmarks:
        print(f"  {b['metric_name']}: {b['metric_value']}")

    # Entity outcomes
    print("\n--- Entity Outcomes ---")
    for e in entities:
        print(f"  {e['entity_name']}: {e['status']} -> {e['successor']}")

    # Technology lifecycle
    print("\n--- Technology Lifecycle Changes ---")
    for t in technologies:
        print(f"  {t['tech_name']}: [{t['lifecycle_at_study']}] -> [{t['lifecycle_current']}]")

    # Predictions vs outcomes
    preds = [o for o in obs if o["observation_type"] == "viability-prediction"]
    outcomes = [o for o in obs if o["observation_type"] == "actual-outcome"]
    print(f"\n--- Prediction Tracking ---")
    print(f"  Predictions made: {len(preds)}")
    print(f"  Outcomes recorded: {len(outcomes)}")

if __name__ == "__main__":
    main()
