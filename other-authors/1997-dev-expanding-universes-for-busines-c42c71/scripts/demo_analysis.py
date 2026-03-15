"""
Demo Analysis Script
Study: Expanding Universes For BusinessObjects And Its Users
Study ID: 1997-dev-expanding-universes-for-busines-c42c71
Aberdeen Group, June 1997
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
    study = load_csv('studies.csv')[0]

    print("=" * 65)
    print("Business Objects BI Profile — Aberdeen Group, June 1997")
    print("Demo Analysis")
    print("=" * 65)

    print(f"\nStudy: {study['title']}")
    print(f"Prescience Score: {study['prescience']}/10")
    print(f"Importance Score: {study['importance']}/10")

    # Observation type distribution
    obs_types = Counter(o['observation_type'] for o in observations)
    print("\nObservation Types:")
    for otype, count in obs_types.most_common():
        print(f"  {otype}: {count}")

    # Financial data from study
    print("\nFinancial Metrics from Study (1996):")
    financial_obs = [o for o in observations if o['observation_type'] == 'market-data' and int(o['year_observed']) < 1997]
    for o in financial_obs:
        print(f"  {o['metric_name']}: {o['metric_value'][:70]}")

    # Predictions vs. outcomes
    predictions = [o for o in observations if o['observation_type'] == 'viability-prediction']
    outcomes = [o for o in observations if o['observation_type'] == 'actual-outcome']
    print(f"\nPredictions (1997): {len(predictions)}")
    print(f"Researched Outcomes: {len(outcomes)}")

    # Key outcomes
    print("\nKey Actual Outcomes:")
    for o in sorted(outcomes, key=lambda x: x['year_observed']):
        print(f"  [{o['year_observed']}] {o['metric_name']}: {o['metric_value'][:75]}")

    # Technology lifecycle
    print("\nTechnology Lifecycle (1997 -> Current):")
    for t in technologies:
        if t['lifecycle_at_study'] != t['lifecycle_current']:
            print(f"  {t['tech_name'][:40]:<40} {t['lifecycle_at_study']:<12} -> {t['lifecycle_current']}")

    # Entity outcomes
    print("\nEntity Outcomes:")
    for e in entities:
        if e['status'] in ('Acquired', 'Merged', 'Rebranded'):
            print(f"  {e['entity_name']}: {e['status']} -> {e['successor']}")

    print("\nConclusion:")
    print("  Aberdeen's core prediction — Business Objects as stable top-tier supplier —")
    print("  was validated: revenues grew from $85M (1996) to $1.5B (2007), with")
    print("  SAP acquisition for $6.8B in January 2008.")


if __name__ == '__main__':
    main()
