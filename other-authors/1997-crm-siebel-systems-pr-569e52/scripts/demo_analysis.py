"""
Demo Analysis Script
Study: Siebel Systems: Customer Interaction Software Vendor Profile
Study ID: 1997-crm-siebel-systems-pr-569e52
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

    print("=" * 65)
    print("Siebel Systems CRM Profile — Aberdeen Group, June 1997")
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

    # Revenue trajectory
    print("\nSiebel Revenue Trajectory (from actual-outcome observations):")
    revenue_obs = [o for o in outcomes if 'revenue' in o['metric_name'].lower() or 'milestone' in o['metric_name'].lower()]
    for o in sorted(revenue_obs, key=lambda x: x['year_observed']):
        print(f"  {o['year_observed']}: {o['metric_value'][:80]}")

    # Partner analysis
    print("\nKey Partnership Entities:")
    partner_types = ['Professional Services']
    for e in entities:
        if e['entity_type'] in partner_types:
            print(f"  {e['entity_name']}: {e['status']} (-> {e['successor']})")

    # Prescience summary
    print("\nPrescience Summary (Score: 9/10):")
    print("  1997 Revenue: $120M     (Aberdeen predicted strong year)   [CORRECT]")
    print("  1998 Revenue: $391.5M   (89% growth)                       [CORRECT]")
    print("  2000 Revenue: $1B+      (fastest-growing US company 1999)  [CORRECT]")
    print("  2006 Acquisition: Oracle $5.85B, 45% CRM market share      [CORRECT]")
    print("  Microsoft alliance: Partially eroded (MSFT launched Dynamics CRM 2003)")
    print("  Mobile CRM: Directionally correct (Salesforce led, not Siebel)")

    # Technology lifecycle
    print("\nTechnology Lifecycle Changes:")
    for t in technologies:
        if t['lifecycle_at_study'] != t['lifecycle_current']:
            print(f"  {t['tech_name'][:35]:<35} {t['lifecycle_at_study']:<12} -> {t['lifecycle_current']}")


if __name__ == '__main__':
    main()
