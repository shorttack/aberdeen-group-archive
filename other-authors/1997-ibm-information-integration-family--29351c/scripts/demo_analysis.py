"""
Demo Analysis Script
Aberdeen Group Archive — IBM Information Integration Family (1997)
Study ID: 1997-ibm-information-integration-family--29351c

Demonstrates loading and querying the Frictionless Data Package.
"""

import csv
import json
from pathlib import Path
from collections import Counter

BASE = Path(__file__).parent.parent

def load_csv(name):
    with open(BASE / "data" / f"{name}.csv", newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))

def main():
    studies = load_csv("studies")
    entities = load_csv("entities")
    technologies = load_csv("technologies")
    observations = load_csv("observations")

    print("=" * 60)
    print("STUDY SUMMARY")
    print("=" * 60)
    for s in studies:
        print(f"Title:      {s['title']}")
        print(f"Date:       {s['date']}")
        print(f"Importance: {s['importance']}/10")
        print(f"Relevance:  {s['relevance']}/10")
        print(f"Prescience: {s['prescience']}/10")
        print()

    print("=" * 60)
    print(f"ENTITIES ({len(entities)})")
    print("=" * 60)
    for e in entities:
        print(f"  {e['entity_name']} — {e['status']}")

    print()
    print("=" * 60)
    print(f"TECHNOLOGIES ({len(technologies)})")
    print("=" * 60)
    for t in technologies:
        print(f"  {t['tech_name']}")
        print(f"    1997: {t['lifecycle_at_study']} | Now: {t['lifecycle_current'][:60]}...")

    print()
    print("=" * 60)
    print(f"OBSERVATIONS ({len(observations)})")
    print("=" * 60)
    obs_types = Counter(o["observation_type"] for o in observations)
    for otype, count in sorted(obs_types.items()):
        print(f"  {otype}: {count}")

    predictions = [o for o in observations if o["observation_type"] == "viability-prediction"]
    outcomes = [o for o in observations if o["observation_type"] == "actual-outcome"]
    print(f"\nPredictions: {len(predictions)}, Actual outcomes: {len(outcomes)}")

    # Technology lifecycle summary
    print("\nTECHNOLOGY LIFECYCLE CHANGES (1997 → 2026):")
    for t in technologies:
        print(f"  {t['tech_name']}: {t['lifecycle_at_study']} → {t['lifecycle_current'][:50]}")

if __name__ == "__main__":
    main()
