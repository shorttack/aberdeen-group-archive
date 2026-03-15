"""
Demo Analysis Script — 1997-infinite-resource-planning-wp-893815
Infinite Resource Planning: A Manifesto For 21st Century Enterprise Applications
Aberdeen Group, May 1997

This script demonstrates basic analysis of the structured data in this package.
"""

import csv
import json
from pathlib import Path
from collections import Counter

BASE = Path(__file__).parent.parent


def load_csv(name):
    with open(BASE / "data" / f"{name}.csv", newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def load_json(path):
    with open(BASE / path, encoding="utf-8") as f:
        return json.load(f)


def main():
    print("=" * 60)
    print("Aberdeen Group — Infinite Resource Planning (1997)")
    print("Frictionless Data Package Demo Analysis")
    print("=" * 60)

    # Study metadata
    studies = load_csv("studies")
    s = studies[0]
    print(f"\nStudy: {s['title']}")
    print(f"Date:  {s['date']}")
    print(f"Type:  {s['type']}")
    print(f"Domain:{s['subject_domain']}")
    print(f"\nScores:")
    print(f"  Importance: {s['importance']}/10 — {s['importance_rationale'][:80]}...")
    print(f"  Relevance:  {s['relevance']}/10  — {s['relevance_rationale'][:80]}...")
    print(f"  Prescience: {s['prescience']}/10 — {s['prescience_rationale'][:80]}...")

    # Observations analysis
    obs = load_csv("observations")
    print(f"\nObservations: {len(obs)} total")
    
    obs_types = Counter(o["observation_type"] for o in obs)
    print("\nObservation Types:")
    for otype, count in obs_types.most_common():
        print(f"  {otype:<35} {count}")

    # Prediction vs outcome pairs
    predictions = [o for o in obs if o["observation_type"] == "viability-prediction"]
    outcomes    = [o for o in obs if o["observation_type"] == "actual-outcome"]
    print(f"\nPredictions made:    {len(predictions)}")
    print(f"Outcomes documented: {len(outcomes)}")

    # Technologies
    techs = load_csv("technologies")
    print(f"\nTechnologies tracked: {len(techs)}")
    tech_cats = Counter(t["category"] for t in techs)
    print("Categories:")
    for cat, cnt in tech_cats.most_common():
        print(f"  {cat:<40} {cnt}")

    # Lifecycle analysis
    print("\nTechnology Lifecycle Changes (1997 → 2026):")
    for t in techs:
        if t["lifecycle_at_study"] != t["lifecycle_current"]:
            print(f"  {t['tech_name']:<45} {t['lifecycle_at_study']:<25} → {t['lifecycle_current']}")

    # Entities
    entities = load_csv("entities")
    print(f"\nEntities tracked: {len(entities)}")

    print("\n--- End of Demo Analysis ---")


if __name__ == "__main__":
    main()
