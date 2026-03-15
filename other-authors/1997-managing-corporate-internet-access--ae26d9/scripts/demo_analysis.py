"""
Demo Analysis Script — 1997-managing-corporate-internet-access--ae26d9
Managing Corporate Internet Access: A Business Priority
Aberdeen Group, April 1997
"""

import csv
from pathlib import Path
from collections import Counter

BASE = Path(__file__).parent.parent


def load_csv(name):
    with open(BASE / "data" / f"{name}.csv", newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def main():
    print("=" * 60)
    print("Aberdeen Group — Managing Corporate Internet Access (1997)")
    print("Frictionless Data Package Demo Analysis")
    print("=" * 60)

    studies = load_csv("studies")
    s = studies[0]
    print(f"\nStudy: {s['title']}")
    print(f"Analyst: {s['author']}")
    print(f"Date:    {s['date']}")
    print(f"\nScores:")
    print(f"  Importance: {s['importance']}/10")
    print(f"  Relevance:  {s['relevance']}/10")
    print(f"  Prescience: {s['prescience']}/10 (HIGH — bandwidth mgmt market correct)")

    obs = load_csv("observations")
    print(f"\nObservations: {len(obs)}")
    obs_types = Counter(o["observation_type"] for o in obs)
    for otype, count in obs_types.most_common():
        print(f"  {otype:<35} {count}")

    preds = [o for o in obs if o["observation_type"] == "viability-prediction"]
    outs  = [o for o in obs if o["observation_type"] == "actual-outcome"]
    print(f"\nPredictions made: {len(preds)}  |  Outcomes documented: {len(outs)}")

    print("\nKey Prediction Outcomes:")
    for o in outs:
        print(f"  [{o['year_observed']}] {o['metric_name'][:55]}")
        print(f"        → {o['metric_value'][:80]}")

    entities = load_csv("entities")
    print(f"\nEntities ({len(entities)}):")
    for e in entities:
        print(f"  {e['entity_name']:<45} {e['status'][:35]}")

    print("\n--- End of Demo Analysis ---")
    print("KEY: Xedia acquired by Lucent for $246M in 1999.")
    print("     Internet bandwidth management became QoS/SD-WAN industry.")


if __name__ == "__main__":
    main()
