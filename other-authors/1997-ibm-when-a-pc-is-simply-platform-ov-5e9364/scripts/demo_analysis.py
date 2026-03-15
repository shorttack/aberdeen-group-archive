"""
Demo Analysis Script
Aberdeen Group Archive — When a PC is Simply Platform Overkill: IBM's Network Station Alternative (1997)
Study ID: 1997-ibm-when-a-pc-is-simply-platform-ov-5e9364

Demonstrates loading and querying the Frictionless Data Package.
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
        print(f"Date:       {s['date']}")
        print(f"Importance: {s['importance']}/10")
        print(f"Relevance:  {s['relevance']}/10")
        print(f"Prescience: {s['prescience']}/10")
        print()
        print(f"Prescience rationale:\n  {s['prescience_rationale'][:300]}...")
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
        print(f"    1997 lifecycle: {t['lifecycle_at_study']}")
        print(f"    Current:        {t['lifecycle_current'][:70]}")

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

    # Cost analysis
    cost_obs = [o for o in observations if "cost" in o.get("metric_name", "").lower() 
                or "price" in o.get("metric_name", "").lower()]
    print("\nCOST/PRICE OBSERVATIONS:")
    for o in cost_obs:
        print(f"  {o['metric_name']}: {o['metric_value']}")

    # Technology vindication
    print("\nNC CONCEPT VINDICATION (post-study):")
    vind = [o for o in outcomes if "chromebook" in o.get("notes", "").lower() 
            or "vdi" in o.get("notes", "").lower() or "cloud pc" in o.get("notes", "").lower()]
    for o in vind:
        print(f"  [{o['year_observed']}] {o['metric_name']}: {o['metric_value'][:100]}")

if __name__ == "__main__":
    main()
