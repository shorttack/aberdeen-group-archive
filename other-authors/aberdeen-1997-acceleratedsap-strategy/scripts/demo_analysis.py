#!/usr/bin/env python3
"""Demo analysis script for aberdeen-1997-acceleratedsap-strategy dataset."""
import csv
import os

BASE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(BASE, '..', 'data')

def load_csv(name):
    with open(os.path.join(DATA, name), encoding='utf-8') as f:
        return list(csv.DictReader(f))

def main():
    studies = load_csv('studies.csv')
    entities = load_csv('entities.csv')
    technologies = load_csv('technologies.csv')
    observations = load_csv('observations.csv')
    codes = load_csv('codes.csv')

    print("=== Aberdeen Group: AcceleratedSAP (1997) ===")
    print(f"Study: {studies[0]['title']}")
    print(f"Date: {studies[0]['date']} | Type: {studies[0]['type']}")
    print(f"Importance: {studies[0]['importance']} | Relevance: {studies[0]['relevance']} | Prescience: {studies[0]['prescience']}")
    print()
    print(f"Entities: {len(entities)}")
    print(f"Technologies: {len(technologies)}")
    print(f"Observations: {len(observations)}")
    print()

    # Observation type breakdown
    from collections import Counter
    obs_types = Counter(o['observation_type'] for o in observations)
    print("Observation type breakdown:")
    for t, c in sorted(obs_types.items()):
        print(f"  {t}: {c}")
    print()

    # Referential integrity
    entity_ids = {e['entity_id'] for e in entities}
    tech_ids = {t['tech_id'] for t in technologies}
    code_ids = {c['code_id'] for c in codes}
    errors = []
    for o in observations:
        if o['entity_id'] and o['entity_id'] not in entity_ids:
            errors.append(f"Missing entity_id: {o['entity_id']} in {o['obs_id']}")
        if o['tech_id'] and o['tech_id'] not in tech_ids:
            errors.append(f"Missing tech_id: {o['tech_id']} in {o['obs_id']}")
        if o['observation_type'] not in code_ids:
            errors.append(f"Unknown observation_type: {o['observation_type']} in {o['obs_id']}")
        if o['methodology_code'] not in code_ids:
            errors.append(f"Unknown methodology_code: {o['methodology_code']} in {o['obs_id']}")
    if errors:
        print("INTEGRITY ERRORS:")
        for e in errors:
            print(f"  [REVIEW] {e}")
    else:
        print("Referential integrity: PASSED")

    # Prediction accuracy
    preds = [o for o in observations if o['observation_type'] == 'viability-prediction']
    outcomes = [o for o in observations if o['observation_type'] == 'actual-outcome']
    print(f"\nViability predictions: {len(preds)}")
    print(f"Actual outcomes: {len(outcomes)}")
    verified = [o for o in outcomes if o['confidence'] == 'verified']
    print(f"Verified outcomes: {len(verified)}")
    for p in preds:
        print(f"  PREDICTION: {p['metric_name']} => {p['metric_value'][:80]}")
    for o in verified:
        print(f"  OUTCOME:    {o['metric_name']} => {o['metric_value'][:80]}")

if __name__ == '__main__':
    main()
