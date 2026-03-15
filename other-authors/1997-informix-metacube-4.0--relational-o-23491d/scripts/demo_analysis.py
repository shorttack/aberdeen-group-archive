"""
Demo Analysis Script — 1997-informix-metacube-4.0--relational-o-23491d
Informix MetaCube 4.0: Relational OLAP and RDBMS Create an Integrated DSS Environment
Aberdeen Group / Bob Moran, November 1997
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
    print("=" * 60)
    print("Aberdeen Group — Informix MetaCube 4.0 Profile (1997)")
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
    print(f"  Prescience: {s['prescience']}/10")

    obs = load_csv("observations")
    print(f"\nObservations: {len(obs)}")
    obs_types = Counter(o["observation_type"] for o in obs)
    for otype, count in obs_types.most_common():
        print(f"  {otype:<35} {count}")

    predictions = [o for o in obs if o["observation_type"] == "viability-prediction"]
    outcomes = [o for o in obs if o["observation_type"] == "actual-outcome"]
    print(f"\nPredictions: {len(predictions)}  Outcomes: {len(outcomes)}")

    techs = load_csv("technologies")
    print(f"\nTechnologies: {len(techs)}")
    print("Lifecycle changes (1997 → current):")
    for t in techs:
        if t["lifecycle_at_study"] != t["lifecycle_current"]:
            print(f"  {t['tech_name']:<40} → {t['lifecycle_current']}")

    print("\n--- End of Demo Analysis ---")


if __name__ == "__main__":
    main()
