"""
Demo Analysis Script — 1997-lucent-delivers-internet-telephony--888598
Lucent Delivers Internet Telephony and Carrier-Grade Scale
Aberdeen Group / Daniel A. Taylor and Traver H. Kennedy, March 31, 1997
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
    print("Aberdeen Group — Lucent Internet Telephony Server SP (1997)")
    print("Frictionless Data Package Demo Analysis")
    print("=" * 60)

    studies = load_csv("studies")
    s = studies[0]
    print(f"\nStudy: {s['title'][:70]}")
    print(f"Analyst: {s['author']}")
    print(f"Date:    {s['date']}")
    print(f"\nScores:")
    print(f"  Importance: {s['importance']}/10")
    print(f"  Relevance:  {s['relevance']}/10")
    print(f"  Prescience: {s['prescience']}/10 (HIGH — VoIP revolution prediction accurate)")

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
    print("KEY FINDING: Aberdeen correctly predicted VoIP revolution.")
    print("Lucent merged with Alcatel 2006; Nokia acquired 2016.")
    print("Internet telephony became universal; long-distance prices collapsed.")


if __name__ == "__main__":
    main()
