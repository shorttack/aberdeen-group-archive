#!/usr/bin/env python3
"""
demo_analysis.py — Archival Ingest Skill v13
Study: aberdeen-1996-unisys-clearpath-smp-servers
"""
import csv, os

BASE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(BASE, '..', 'data')

def load_csv(name):
    with open(os.path.join(DATA, name), newline='', encoding='utf-8') as f:
        return list(csv.DictReader(f))

def main():
    studies = load_csv('studies.csv')
    entities = load_csv('entities.csv')
    technologies = load_csv('technologies.csv')
    observations = load_csv('observations.csv')
    codes = load_csv('codes.csv')

    s = studies[0]
    print("="*60)
    print(f"STUDY: {s['title']}")
    print(f"  Date: {s['date']} | Importance: {s['importance']} | Relevance: {s['relevance']} | Prescience: {s['prescience']}")
    print(f"  Entities: {len(entities)} | Technologies: {len(technologies)} | Observations: {len(observations)}")
    print()

    type_counts = {}
    for o in observations:
        type_counts[o['observation_type']] = type_counts.get(o['observation_type'], 0) + 1
    print("Observation Types:")
    for k, v in sorted(type_counts.items(), key=lambda x: -x[1]):
        print(f"  {k:<30} {v}")
    print()

    entity_ids = {e['entity_id'] for e in entities} | {''}
    tech_ids = {t['tech_id'] for t in technologies} | {''}
    code_ids = {c['code_id'] for c in codes}
    errors = [o['obs_id'] for o in observations
              if o['entity_id'] not in entity_ids or o['tech_id'] not in tech_ids
              or o['observation_type'] not in code_ids or o['methodology_code'] not in code_ids]
    print(f"Referential integrity: {'PASS' if not errors else 'FAIL: '+', '.join(errors)}")
    print()

    pairs = [
        ('aberdeen-1996-unisys-clearpath-smp-servers-OBS-019',
         'aberdeen-1996-unisys-clearpath-smp-servers-OBS-020'),
    ]
    verified = 0
    for pred_id, outcome_id in pairs:
        pred = next((o for o in observations if o['obs_id'] == pred_id), None)
        outcome = next((o for o in observations if o['obs_id'] == outcome_id), None)
        if pred and outcome:
            print(f"Prediction: {pred['metric_name']}")
            print(f"  Outcome: {outcome['metric_value'][:80]}")
            print(f"  Confidence: {outcome['confidence']}")
            if outcome['confidence'] == 'verified': verified += 1
    if pairs:
        print(f"\nPrediction accuracy: {verified}/{len(pairs)} = {verified/len(pairs)*100:.0f}%")

if __name__ == '__main__':
    main()
