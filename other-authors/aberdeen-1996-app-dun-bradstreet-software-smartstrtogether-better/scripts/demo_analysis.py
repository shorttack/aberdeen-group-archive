"""
Demo Analysis Script
Study: aberdeen-1996-app-dun-bradstreet-software-smartstrtogether-better
D&B Software SmartStream Distributed Enterprise
Aberdeen Group, April 1996
"""

import csv
import os
from collections import Counter

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, "data")


def load_csv(filename):
    path = os.path.join(DATA_DIR, filename)
    with open(path, newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def main():
    print("=" * 60)
    print("Aberdeen Group Archival Analysis")
    print("Study: aberdeen-1996-app-dun-bradstreet-software-smartstrtogether-better")
    print("=" * 60)

    studies = load_csv("studies.csv")
    entities = load_csv("entities.csv")
    technologies = load_csv("technologies.csv")
    observations = load_csv("observations.csv")

    s = studies[0]
    print(f"\nTitle: {s['title'][:80]}...")
    print(f"Date: {s['date']} | Type: {s['type']}")
    print(f"Importance: {s['importance']} | Relevance: {s['relevance']} | Prescience: {s['prescience']}")

    # Key market data
    print(f"\n--- Key Market Metrics (1995/1996) ---")
    market_obs = [o for o in observations if o["observation_type"] == "market-data"]
    for o in market_obs:
        print(f"  {o['metric_name']}: {o['metric_value']}")

    print(f"\n--- Entities ({len(entities)}) ---")
    for e in entities:
        print(f"  {e['entity_name']} [{e['entity_type']}] — {e['status']}")

    print(f"\n--- Observations ({len(observations)}) ---")
    type_counts = Counter(o["observation_type"] for o in observations)
    for ot, count in sorted(type_counts.items()):
        print(f"  {ot}: {count}")

    # Actual outcomes
    print(f"\n--- Actual Outcomes (verified) ---")
    outcomes = [o for o in observations if o["observation_type"] == "actual-outcome"]
    for o in outcomes:
        print(f"  {o['year_observed']}: {o['notes'][:80]}...")

    print("\n--- Prescience Assessment ---")
    print("  CONFIRMED: Single-RDBMS limitation was persistent competitive disadvantage")
    print("  NOT FULFILLED: SmartStream DE leadership prediction — acquired by Geac 1998")
    print("  CONFIRMED: SmartStream manufacturing abandoned by Geac 1997 (CNET reported)")
    print("  CONFIRMED: SAP/Oracle workflow lagging D&B in 1996")

    print("\nAnalysis complete.")


if __name__ == "__main__":
    main()
