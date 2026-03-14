#!/usr/bin/env python3
"""
demo_analysis.py — Archival Ingest Skill v13
Study: aberdeen-1996-ibm-aix-4-not-your-fathers-325
"""
import csv
import os
import sys

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
    print(f"  Title:       {s['title']}")
    print(f"  Author:      {s['author']}")
    print(f"  Date:        {s['date']}")
    print(f"  Domain:      {s['subject_domain']}")
    print(f"  Importance:  {s['importance']} — {s['importance_rationale'][:60]}...")
    print(f"  Relevance:   {s['relevance']} — {s['relevance_rationale'][:60]}...")
    print(f"  Prescience:  {s['prescience']} — {s['prescience_rationale'][:60]}...")
    print()

    print("=" * 60)
    print(f"TABLE COUNTS")
    print("=" * 60)
    print(f"  Entities:      {len(entities)}")
    print(f"  Technologies:  {len(technologies)}")
    print(f"  Observations:  {len(observations)}")
    print(f"  Codes:         {len(codes)}")
    print()

    # Observation type breakdown
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

    # Referential integrity: entity_id
    print("=" * 60)
    print("REFERENTIAL INTEGRITY CHECKS")
    print("=" * 60)
    entity_ids = {e['entity_id'] for e in entities} | {''}
    tech_ids = {t['tech_id'] for t in technologies} | {''}
    code_ids = {c['code_id'] for c in codes}

    errors = []
    for o in observations:
        if o['entity_id'] not in entity_ids:
            errors.append(f"  [FAIL] obs {o['obs_id']}: entity_id '{o['entity_id']}' not in entities.csv")
        if o['tech_id'] not in tech_ids:
            errors.append(f"  [FAIL] obs {o['obs_id']}: tech_id '{o['tech_id']}' not in technologies.csv")
        if o['observation_type'] not in code_ids:
            errors.append(f"  [FAIL] obs {o['obs_id']}: observation_type '{o['observation_type']}' not in codes.csv")
        if o['methodology_code'] not in code_ids:
            errors.append(f"  [FAIL] obs {o['obs_id']}: methodology_code '{o['methodology_code']}' not in codes.csv")

    if errors:
        for e in errors:
            print(e)
    else:
        print("  [PASS] All entity_id, tech_id, observation_type, methodology_code references valid.")
    print()

    # Prediction accuracy
    print("=" * 60)
    print("PREDICTION ACCURACY")
    print("=" * 60)
    predictions = {o['obs_id']: o for o in observations if o['observation_type'] == 'viability-prediction'}
    outcomes = {o['obs_id']: o for o in observations if o['observation_type'] == 'actual-outcome'}

    # Match by pairing: OBS-015->OBS-016, OBS-017->OBS-018
    pairs = [
        ('aberdeen-1996-ibm-aix-4-not-your-fathers-325-OBS-015',
         'aberdeen-1996-ibm-aix-4-not-your-fathers-325-OBS-016'),
        ('aberdeen-1996-ibm-aix-4-not-your-fathers-325-OBS-017',
         'aberdeen-1996-ibm-aix-4-not-your-fathers-325-OBS-018'),
    ]

    verified = 0
    for pred_id, outcome_id in pairs:
        pred = next((o for o in observations if o['obs_id'] == pred_id), None)
        outcome = next((o for o in observations if o['obs_id'] == outcome_id), None)
        if pred and outcome:
            print(f"  Prediction: {pred['metric_name'][:50]}")
            print(f"    Claimed:  {pred['metric_value'][:70]}")
            print(f"    Outcome:  {outcome['metric_value'][:70]}")
            print(f"    Confidence: {outcome['confidence']}")
            if outcome['confidence'] == 'verified':
                verified += 1
            print()

    if pairs:
        accuracy = verified / len(pairs) * 100
        print(f"  Prediction accuracy: {verified}/{len(pairs)} = {accuracy:.0f}%")
    print()
    print("Analysis complete.")

if __name__ == '__main__':
    main()
