"""
Demo Analysis Script
Aberdeen Group Archive — IBM Ships First 64-bit RS/6000 Server (1997)
Study ID: 1997-ibm-ships-first-64-bit-rs-6000-serv-961e2c

Demonstrates loading and querying the Frictionless Data Package.
Note: This is an announcement abstract (~1,139 chars); 15 observations generated.
"""

import csv
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
        print(f"Author:     {s['author']}")
        print(f"Date:       {s['date']}")
        print(f"Type:       {s['type']}")
        print(f"Importance: {s['importance']}/10")
        print(f"Relevance:  {s['relevance']}/10")
        print(f"Prescience: {s['prescience']}/10")
        print()

    print("=" * 60)
    print(f"ENTITIES ({len(entities)})")
    print("=" * 60)
    for e in entities:
        status = e['status']
        successor = e.get('successor', '')
        line = f"  {e['entity_name']} — {status}"
        if successor:
            line += f" (successor: {successor[:50]})"
        print(line)

    print()
    print("=" * 60)
    print(f"TECHNOLOGIES ({len(technologies)})")
    print("=" * 60)
    for t in technologies:
        print(f"  {t['tech_name']} ({t['era']})")
        print(f"    1997: {t['lifecycle_at_study']} | Now: {t['lifecycle_current'][:60]}")

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

    print("\nPREDICTION → OUTCOME PAIRS:")
    for p in predictions:
        matching = [o for o in outcomes if o.get("tech_id") == p.get("tech_id")]
        print(f"\n  PREDICTION: {p['metric_name']} = {p['metric_value'][:80]}")
        for o in matching:
            print(f"  OUTCOME:    {o['metric_name']} = {o['metric_value'][:80]}")

if __name__ == "__main__":
    main()
