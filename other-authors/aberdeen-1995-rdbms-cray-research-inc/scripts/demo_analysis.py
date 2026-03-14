"""
Demo Analysis Script
Study: aberdeen-1995-rdbms-cray-research-inc
Cray Research, Inc.: RDBMS and Commercial Database Market Position
Aberdeen Group, 1995
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
    print("Study: aberdeen-1995-rdbms-cray-research-inc")
    print("=" * 60)

    # Load data
    studies = load_csv("studies.csv")
    entities = load_csv("entities.csv")
    technologies = load_csv("technologies.csv")
    observations = load_csv("observations.csv")

    # Study metadata
    s = studies[0]
    print(f"\nTitle: {s['title']}")
    print(f"Date: {s['date']} | Type: {s['type']}")
    print(f"Importance: {s['importance']} | Relevance: {s['relevance']} | Prescience: {s['prescience']}")
    print(f"\nAbstract:\n{s['abstract']}")

    # Entity summary
    print(f"\n--- Entities ({len(entities)}) ---")
    for e in entities:
        print(f"  {e['entity_name']} [{e['entity_type']}] — {e['status']}")

    # Technology lifecycle
    print(f"\n--- Technologies ({len(technologies)}) ---")
    for t in technologies:
        print(f"  {t['tech_name']}: {t['lifecycle_at_study']} → {t['lifecycle_current']}")

    # Observation breakdown
    print(f"\n--- Observations ({len(observations)}) ---")
    type_counts = Counter(o["observation_type"] for o in observations)
    for ot, count in sorted(type_counts.items()):
        print(f"  {ot}: {count}")

    # Viability predictions vs outcomes
    predictions = [o for o in observations if o["observation_type"] == "viability-prediction"]
    outcomes = [o for o in observations if o["observation_type"] == "actual-outcome"]
    print(f"\n  Viability Predictions: {len(predictions)}")
    print(f"  Actual Outcomes (verified): {len(outcomes)}")

    # Confidence distribution
    conf_counts = Counter(o["confidence"] for o in observations)
    print(f"\n--- Confidence Distribution ---")
    for conf, count in sorted(conf_counts.items()):
        print(f"  {conf}: {count}")

    print("\n--- Key Prescience Finding ---")
    print("  Aberdeen predicted Cray would be 'a major force' in commercial databases.")
    print("  OUTCOME: Cray Research acquired by SGI for $740M just months later (Feb 1996).")
    print("  CS6400 tech divested to Sun → became Sun Enterprise 10000 (Starfire): highly successful.")
    print("  The underlying SMP architecture prediction was highly prescient.")

    print("\nAnalysis complete.")


if __name__ == "__main__":
    main()
