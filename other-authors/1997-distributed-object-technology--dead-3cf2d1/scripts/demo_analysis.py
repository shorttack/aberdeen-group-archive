#!/usr/bin/env python3
"""
Demo analysis script for:
  Distributed Object Technology: Dead Skunk Or Live Wire
  Aberdeen Group Technology Viewpoint, 1997
  Study ID: 1997-distributed-object-technology--dead-3cf2d1
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
    print("Aberdeen Group Study: Distributed Object Technology")
    print("Dead Skunk Or Live Wire (1997 Technology Viewpoint)")
    print("=" * 60)

    # Load all data
    studies = load_csv("studies.csv")
    entities = load_csv("entities.csv")
    technologies = load_csv("technologies.csv")
    observations = load_csv("observations.csv")

    # Study summary
    study = studies[0]
    print(f"\nTitle:   {study['title']}")
    print(f"Author:  {study['author']}")
    print(f"Date:    {study['date']}")
    print(f"Type:    {study['type']}")
    print(f"\nScores:")
    print(f"  Importance:  {study['importance']}/5 — {study['importance_rationale'][:80]}...")
    print(f"  Relevance:   {study['relevance']}/5 — {study['relevance_rationale'][:80]}...")
    print(f"  Prescience:  {study['prescience']}/5 — {study['prescience_rationale'][:80]}...")

    # Observation type breakdown
    print(f"\nObservations ({len(observations)} total):")
    obs_types = Counter(o["observation_type"] for o in observations)
    for otype, count in obs_types.most_common():
        print(f"  {otype:<30} {count}")

    # Prediction/outcome pairs
    predictions = [o for o in observations if o["observation_type"] == "viability-prediction"]
    outcomes = [o for o in observations if o["observation_type"] == "actual-outcome"]
    print(f"\nPrediction/Outcome pairs: {len(predictions)} predictions, {len(outcomes)} outcomes")

    # Technology lifecycle changes
    print(f"\nTechnology lifecycle changes (1997 → 2026):")
    for tech in technologies:
        print(f"  {tech['tech_name'][:40]:<40} {tech['lifecycle_at_study']:<20} → {tech['lifecycle_current']}")

    # Entity status
    print(f"\nEntities and current status:")
    for ent in entities:
        succ = f"→ {ent['successor']}" if ent['successor'] else ""
        print(f"  {ent['entity_name']:<35} {ent['status']:<15} {succ}")

    print("\n" + "=" * 60)
    print("Source: https://web.archive.org/web/19980131061426/")
    print("  http://www.aberdeen.com:80/research/abstract/97080139.htm")
    print("License: CC-BY-4.0")


if __name__ == "__main__":
    main()
