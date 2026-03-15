#!/usr/bin/env python3
"""
Demo analysis for: Data Integration Management in Heterogeneous Computing Environments
Study ID: 1997-data-integration-management-in-hete-de2429
"""
import csv
from pathlib import Path

BASE = Path(__file__).parent.parent

def load_csv(name):
    with open(BASE / "data" / f"{name}.csv") as f:
        return list(csv.DictReader(f))

def main():
    print("=" * 60)
    print("ETI Data Integration — Aberdeen Vendor Profile Analysis")
    print("=" * 60)

    obs = load_csv("observations")
    entities = load_csv("entities")
    technologies = load_csv("technologies")

    # Financial data
    market_obs = [o for o in obs if o["observation_type"] == "market-data"]
    print("\n--- ETI Financial Metrics (FY1997) ---")
    for o in market_obs:
        print(f"  {o['metric_name']}: {o['metric_value']}")

    # Technology fate
    print("\n--- Technology Lifecycle Comparison ---")
    for t in technologies:
        arrow = "->" 
        print(f"  {t['tech_name']}: [{t['lifecycle_at_study']}] {arrow} [{t['lifecycle_current']}]")

    # Entity outcomes
    print("\n--- Competitor/Customer Entity Status ---")
    for e in entities:
        print(f"  {e['entity_name']}: {e['status']}")

    # Predictions vs outcomes
    preds = [o for o in obs if o["observation_type"] == "viability-prediction"]
    outcomes = [o for o in obs if o["observation_type"] == "actual-outcome"]
    print(f"\n--- Prediction Tracking ---")
    print(f"  Predictions made: {len(preds)}")
    print(f"  Outcomes recorded: {len(outcomes)}")

if __name__ == "__main__":
    main()
