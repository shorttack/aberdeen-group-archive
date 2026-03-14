#!/usr/bin/env python3
"""
demo_analysis.py — Archival Ingest Skill v13
Study: aberdeen-1996-hp-vectra-xw-personal-workstation
"""
import csv
import os

BASE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(BASE, '..', 'data')

def load_csv(name):
    path = os.path.join(DATA, name)
    with open(path, newline='', encoding='utf-8') as f:
        return list(csv.DictReader(f))

def main():
    studies = load_csv('studies.csv')
    entities = load_csv('entities.csv')
    technologies = load_csv('technologies.csv')
    observations = load_csv('observations.csv')
    codes = load_csv('codes.csv')

    print("=" * 60)
    print("STUDY SUMMARY")
    print("=" * 60)
    s = studies[0]
    print(f"  Title:       {s['title'][:60]}...")
    print(f"  Author:      {s['author']}")
    print(f"  Date:        {s['date']}")
    print(f"  Domain:      {s['subject_domain']}")
    print(f"  Importance:  {s['importance']}")
    print(f"  Relevance:   {s['relevance']}")
    print(f"  Prescience:  {s['prescience']}")
    print()

    print("=" * 60)
    print("TABLE COUNTS")
    print("=" * 60)
    print(f"  Entities:      {len(entities)}")
    print(f"  Technologies:  {len(technologies)}")
    print(f"  Observations:  {len(observations)}")
    print(f"  Codes:         {len(codes)}")
    print()

    type_counts = {}
    for o in observations:
        t = o['observation_type']
        type_counts[t] = type_counts.get(t, 0) + 1
    print("=" * 60)
    print("OBSERVATION TYPE BREAKDOWN")
    print("=" * 60)
    for k, v in sorted(type_counts.items(), key=lambda x: -x[1]):
        print(f"  {k:<30} {v}")
    print()

    print("=" * 60)
    print("REFERENTIAL INTEGRITY CHECKS")
    print("=" * 60)
    entity_ids = {e['entity_id'] for e in entities} | {''}
    tech_ids = {t['tech_id'] for t in technologies} | {''}
    code_ids = {c['code_id'] for c in codes}

    errors = []
    for o in observations:
        if o['entity_id'] not in entity_ids:
            errors.append(f"  [FAIL] obs {o['obs_id']}: entity_id '{o['entity_id']}' not found")
        if o['tech_id'] not in tech_ids:
            errors.append(f"  [FAIL] obs {o['obs_id']}: tech_id '{o['tech_id']}' not found")
        if o['observation_type'] not in code_ids:
            errors.append(f"  [FAIL] obs {o['obs_id']}: observation_type '{o['observation_type']}' not found")
        if o['methodology_code'] not in code_ids:
            errors.append(f"  [FAIL] obs {o['obs_id']}: methodology_code '{o['methodology_code']}' not found")

    if errors:
        for e in errors:
            print(e)
    else:
        print("  [PASS] All referential integrity checks passed.")
    print()

    print("=" * 60)
    print("PREDICTION ACCURACY")
    print("=" * 60)
    pairs = [
        ('aberdeen-1996-hp-vectra-xw-personal-workstation-OBS-017',
         'aberdeen-1996-hp-vectra-xw-personal-workstation-OBS-018'),
        ('aberdeen-1996-hp-vectra-xw-personal-workstation-OBS-019',
         'aberdeen-1996-hp-vectra-xw-personal-workstation-OBS-020'),
    ]
    verified = 0
    for pred_id, outcome_id in pairs:
        pred = next((o for o in observations if o['obs_id'] == pred_id), None)
        outcome = next((o for o in observations if o['obs_id'] == outcome_id), None)
        if pred and outcome:
            print(f"  Prediction: {pred['metric_name'][:55]}")
            print(f"    Outcome:  {outcome['metric_value'][:70]}")
            print(f"    Confidence: {outcome['confidence']}")
            if outcome['confidence'] == 'verified':
                verified += 1
            print()

    if pairs:
        print(f"  Prediction accuracy: {verified}/{len(pairs)} = {verified/len(pairs)*100:.0f}%")
    print()
    print("Analysis complete.")

if __name__ == '__main__':
    main()
