"""
Demo Analysis Script
Aberdeen Group Archive — IBM Extended Transaction Systems Family (1997)
Study ID: 1997-ibm-extended-transaction-systems-fa-0369fa

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
        print(f"Abstract:   {s['abstract'][:200]}...")
        print()

    print("=" * 60)
    print(f"ENTITIES ({len(entities)} total)")
    print("=" * 60)
    for e in entities:
        print(f"  [{e['entity_id']}] {e['entity_name']} — {e['status']}")

    print()
    print("=" * 60)
    print(f"TECHNOLOGIES ({len(technologies)} total)")
    print("=" * 60)
    for t in technologies:
        print(f"  [{t['tech_id']}] {t['tech_name']}")
        print(f"    Lifecycle 1997: {t['lifecycle_at_study']}")
        print(f"    Lifecycle now:  {t['lifecycle_current']}")

    print()
    print("=" * 60)
    print(f"OBSERVATIONS ({len(observations)} total)")
    print("=" * 60)
    obs_types = Counter(o["observation_type"] for o in observations)
    print("By type:")
    for otype, count in sorted(obs_types.items()):
        print(f"  {otype}: {count}")

    print()
    predictions = [o for o in observations if o["observation_type"] == "viability-prediction"]
    outcomes = [o for o in observations if o["observation_type"] == "actual-outcome"]
    print(f"Predictions: {len(predictions)}")
    print(f"Actual outcomes (post-hoc): {len(outcomes)}")

    print()
    print("PREDICTION → OUTCOME PAIRS:")
    for p in predictions:
        print(f"\n  PREDICTION [{p['obs_id']}]: {p['metric_name']}")
        print(f"    Value: {p['metric_value']}")
        matching = [o for o in outcomes if o.get("tech_id") == p.get("tech_id")]
        for o in matching:
            print(f"  OUTCOME [{o['obs_id']}]: {o['metric_name']} = {o['metric_value'][:100]}...")

if __name__ == "__main__":
    main()
