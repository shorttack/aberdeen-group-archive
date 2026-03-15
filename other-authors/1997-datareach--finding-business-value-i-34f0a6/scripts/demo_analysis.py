"""
Demo Analysis Script
Study: DataReach: Finding Business Value in Extracting Data
Study ID: 1997-datareach--finding-business-value-i-34f0a6
Aberdeen Group, 1997
Author: David Hill
"""

import csv
import os
from collections import Counter

DATA_DIR = os.path.join(os.path.dirname(__file__), '..', 'data')


def load_csv(filename):
    path = os.path.join(DATA_DIR, filename)
    with open(path, newline='', encoding='utf-8') as f:
        return list(csv.DictReader(f))


def main():
    observations = load_csv('observations.csv')
    entities = load_csv('entities.csv')
    technologies = load_csv('technologies.csv')

    print("=" * 60)
    print("DataReach Aberdeen Group Profile — 1997")
    print("Demo Analysis")
    print("=" * 60)

    # Observation type distribution
    obs_types = Counter(o['observation_type'] for o in observations)
    print("\nObservation Types:")
    for otype, count in obs_types.most_common():
        print(f"  {otype}: {count}")

    # Predictions vs. outcomes
    predictions = [o for o in observations if o['observation_type'] == 'viability-prediction']
    outcomes = [o for o in observations if o['observation_type'] == 'actual-outcome']
    print(f"\nPredictions: {len(predictions)}")
    print(f"Actual Outcomes (researched): {len(outcomes)}")

    # Entity status
    print("\nEntity Status Summary:")
    for e in entities:
        print(f"  {e['entity_name']}: {e['status']}")
        if e['successor'] and e['successor'] != 'N/A':
            print(f"    -> Successor: {e['successor']}")

    # Technology lifecycle
    print("\nTechnology Lifecycle (1997 -> Current):")
    for t in technologies:
        print(f"  {t['tech_name']}: {t['lifecycle_at_study']} -> {t['lifecycle_current']}")

    # Key findings
    print("\nKey Findings:")
    print("  - DataReach was a joint EMC/BMC product to bypass mainframe data scheduling constraints")
    print("  - Aberdeen predicted it would help Global 2000 enterprises extract mainframe data")
    print("  - The product did NOT achieve long-term market success (obsolete by ~2000)")
    print("  - The underlying problem was real; ETL platforms became the dominant solution")
    print("  - EMC acquired by Dell 2016; BMC Software went private 2013")
    print("\nNote: Only the abstract page was captured; full text required authentication")


if __name__ == '__main__':
    main()
