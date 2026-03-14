"""
Demo Analysis Script
Study: aberdeen-1996-advanced-planning-engines-white-paper
Advanced Planning Engine Technologies
Aberdeen Group, February 1996
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
    print("Study: aberdeen-1996-advanced-planning-engines-white-paper")
    print("=" * 60)

    studies = load_csv("studies.csv")
    entities = load_csv("entities.csv")
    technologies = load_csv("technologies.csv")
    observations = load_csv("observations.csv")

    s = studies[0]
    print(f"\nTitle: {s['title'][:80]}...")
    print(f"Date: {s['date']} | Type: {s['type']}")
    print(f"Importance: {s['importance']} | Relevance: {s['relevance']} | Prescience: {s['prescience']}")

    # Market data observations
    print(f"\n--- Vendor Market Data (1995 Revenues) ---")
    market_obs = [o for o in observations if o["observation_type"] == "market-data" and "revenue" in o["metric_name"]]
    for o in sorted(market_obs, key=lambda x: x["entity_id"]):
        print(f"  {o['entity_id']}: {o['metric_value']}")

    print(f"\n--- Entities ({len(entities)}) ---")
    for e in entities:
        print(f"  {e['entity_name']} [{e['entity_type']}] — {e['status']}")

    print(f"\n--- Observations ({len(observations)}) ---")
    type_counts = Counter(o["observation_type"] for o in observations)
    for ot, count in sorted(type_counts.items()):
        print(f"  {ot}: {count}")

    print("\n--- Key Prescience Findings ---")
    print("  1. Red Pepper acquired by PeopleSoft for $225M in Sept 1996 (same year as study)")
    print("  2. i2 Technologies IPO April 1996 at ~$700M valuation")
    print("  3. i2 Technologies acquired by JDA Software for $604M in January 2010")
    print("  4. Manugistics acquired by JDA Software in July 2006")
    print("  5. Supply chain planning became standard enterprise software category by 2000")
    print("  6. ROI case studies: $5.5M savings, 70% order cost reduction, 150% productivity gains — documented")

    print("\nAnalysis complete.")


if __name__ == "__main__":
    main()
