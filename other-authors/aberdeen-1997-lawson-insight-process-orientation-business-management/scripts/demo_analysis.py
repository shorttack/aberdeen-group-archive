#!/usr/bin/env python3
"""Demo analysis for aberdeen-1997-lawson-insight-process-orientation-business-management."""
import csv, os
from collections import Counter

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

    print("=== Aberdeen Group: Lawson Insight (1997) ===")
    print(f"Study: {studies[0]['title'][:80]}...")
    print(f"Importance: {studies[0]['importance']} | Relevance: {studies[0]['relevance']} | Prescience: {studies[0]['prescience']}")
    print()
    print(f"Entities: {len(entities)} | Technologies: {len(technologies)} | Observations: {len(observations)}")
    print()

    obs_types = Counter(o['observation_type'] for o in observations)
    print("Observation type breakdown:")
    for t, c in sorted(obs_types.items()):
        print(f"  {t}: {c}")
    print()

    entity_ids = {e['entity_id'] for e in entities}
    tech_ids = {t['tech_id'] for t in technologies}
    code_ids = {c['code_id'] for c in codes}
    errors = []
    for o in observations:
        if o['entity_id'] and o['entity_id'] not in entity_ids:
            errors.append(f"Missing entity_id: {o['entity_id']}")
        if o['tech_id'] and o['tech_id'] not in tech_ids:
            errors.append(f"Missing tech_id: {o['tech_id']}")
        if o['observation_type'] not in code_ids:
            errors.append(f"Unknown obs_type: {o['observation_type']}")
        if o['methodology_code'] not in code_ids:
            errors.append(f"Unknown method: {o['methodology_code']}")
    print("Referential integrity:", "PASSED" if not errors else f"FAILED — {errors}")

    preds = [o for o in observations if o['observation_type'] == 'viability-prediction']
    outcomes = [o for o in observations if o['observation_type'] == 'actual-outcome']
    verified = [o for o in outcomes if o['confidence'] == 'verified']
    print(f"\nViability predictions: {len(preds)}, Outcomes: {len(outcomes)} ({len(verified)} verified)")
    for p in preds:
        print(f"  PRED: {p['metric_name']}")
    for o in outcomes:
        print(f"  OUT:  {o['metric_name']} [{o['confidence']}]")

if __name__ == '__main__':
    main()
