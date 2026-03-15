"""
Demo Analysis Script
Study: Desktop and Systems Management The HP Way
Study ID: 1997-desktop-and-systems-management-the--169a9b
Aberdeen Group, March 1997
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

    print("=" * 65)
    print("Desktop and Systems Management The HP Way — Aberdeen 1997")
    print("Demo Analysis")
    print("=" * 65)

    # Observation type distribution
    obs_types = Counter(o['observation_type'] for o in observations)
    print("\nObservation Types:")
    for otype, count in obs_types.most_common():
        print(f"  {otype}: {count}")

    # Predictions vs. outcomes
    predictions = [o for o in observations if o['observation_type'] == 'viability-prediction']
    outcomes = [o for o in observations if o['observation_type'] == 'actual-outcome']
    print(f"\nPredictions made (1997): {len(predictions)}")
    print(f"Actual Outcomes (researched): {len(outcomes)}")

    # Show predictions with their outcomes
    print("\nPrediction/Outcome Pairs:")
    print("  PRED: DMI will become a de facto standard -> OUTCOME: Partially true; DMI EOL 2005; WMI dominated")
    print("  PRED: HP will surpass Compaq using DMI  -> OUTCOME: HP acquired Compaq 2002 instead")
    print("  PRED: 50%+ TCO reduction possible       -> OUTCOME: Directionally true; specific figure unverifiable")
    print("  PRED: Magic Packet useful for mgmt      -> OUTCOME: CORRECT; became Wake-on-LAN standard")

    # Entity status
    print("\nEntity Status Summary:")
    for e in entities:
        status_str = f"{e['status']}"
        if e['successor'] and e['successor'] not in ('N/A', ''):
            status_str += f" -> {e['successor']}"
        print(f"  {e['entity_name']}: {status_str}")

    # Technology lifecycle changes
    print("\nTechnology Lifecycle Changes (1997 -> Current):")
    for t in technologies:
        arrow = "->"
        print(f"  {t['tech_name'][:35]:<35} {t['lifecycle_at_study']:<18} {arrow} {t['lifecycle_current']}")

    # Key market data
    print("\nKey Market Data from Study:")
    market_obs = [o for o in observations if o['observation_type'] == 'market-data']
    for o in market_obs:
        print(f"  [{o['year_observed']}] {o['metric_name']}: {o['metric_value'][:80]}")

    print("\nConclusion:")
    print("  Aberdeen correctly identified the TCO problem and DMI's near-term importance.")
    print("  However, WMI (not DMI) became the dominant standard, and HP acquired")
    print("  Compaq rather than defeating it through open-standards competition.")


if __name__ == '__main__':
    main()
