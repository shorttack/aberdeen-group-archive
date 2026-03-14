#!/usr/bin/env python3
"""
Demo Analysis Script — AS/400 And NT Server — IBM and Microsoft Working Together To Comprehensively Meet Real User Requirements
Archival Ingest Skill v13 | Generated 2026-03-14
"""

import csv
import os
import sys

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def load_csv(filename):
    with open(os.path.join(BASE, 'data', filename), newline='', encoding='utf-8') as f:
        return list(csv.DictReader(f))

def main():
    print("=" * 60)
    print(f"Aberdeen Archival Dataset: aberdeen-1997-as400-nt-server-ibm-microsoft-working-together")
    print("=" * 60)

    studies = load_csv('studies.csv')
    entities = load_csv('entities.csv')
    technologies = load_csv('technologies.csv')
    observations = load_csv('observations.csv')
    codes = load_csv('codes.csv')

    print(f"\nStudy: {studies[0]['title']}")
    print(f"Date: {studies[0]['date']}")
    print(f"Author: {studies[0]['author']}")
    print(f"\nRatings:")
    print(f"  Importance: {studies[0]['importance']} — {studies[0]['importance_rationale'][:80]}...")
    print(f"  Relevance:  {studies[0]['relevance']} — {studies[0]['relevance_rationale'][:80]}...")
    print(f"  Prescience: {studies[0]['prescience']} — {studies[0]['prescience_rationale'][:80]}...")

    print(f"\nData Summary:")
    print(f"  Entities:     {len(entities)}")
    print(f"  Technologies: {len(technologies)}")
    print(f"  Observations: {len(observations)}")
    print(f"  Codes:        {len(codes)}")

    # ── Observation type breakdown ──────────────────────────────────────────
    obs_types = {}
    for obs in observations:
        ot = obs['observation_type']
        obs_types[ot] = obs_types.get(ot, 0) + 1
    print(f"\nObservations by type:")
    for k, v in sorted(obs_types.items()):
        print(f"  {k:<30} {v}")

    # ── Referential integrity ───────────────────────────────────────────────
    print("\nReferential Integrity Checks:")
    entity_ids = {e['entity_id'] for e in entities} | {''}
    tech_ids = {t['tech_id'] for t in technologies} | {''}
    code_ids = {c['code_id'] for c in codes}

    failures = []
    for obs in observations:
        if obs['entity_id'] not in entity_ids:
            failures.append(f"  [FAIL] obs {obs['obs_id']}: entity_id '{obs['entity_id']}' not in entities.csv")
        if obs['tech_id'] not in tech_ids:
            failures.append(f"  [FAIL] obs {obs['obs_id']}: tech_id '{obs['tech_id']}' not in technologies.csv")
        if obs['observation_type'] not in code_ids:
            failures.append(f"  [FAIL] obs {obs['obs_id']}: observation_type '{obs['observation_type']}' not in codes.csv")
        if obs['methodology_code'] not in code_ids:
            failures.append(f"  [FAIL] obs {obs['obs_id']}: methodology_code '{obs['methodology_code']}' not in codes.csv")

    if failures:
        for f in failures:
            print(f)
    else:
        print("  [PASS] All entity_id, tech_id, observation_type, methodology_code references valid.")

    # ── Prediction accuracy ─────────────────────────────────────────────────
    predictions = [o for o in observations if o['observation_type'] == 'viability-prediction']
    outcomes = [o for o in observations if o['observation_type'] == 'actual-outcome']
    print(f"\nPrescience Analysis:")
    print(f"  Viability predictions: {len(predictions)}")
    print(f"  Verified outcomes:     {len(outcomes)}")
    if predictions:
        coverage = len(outcomes) / len(predictions) * 100
        print(f"  Outcome coverage:      {coverage:.0f}%")
        print(f"  Overall prescience rating: {studies[0]['prescience']}")

    # ── Completeness check ──────────────────────────────────────────────────
    required_fields = ['study_id','title','author','date','type','subject_domain',
                       'methodology','source_file','abstract','license',
                       'importance','importance_rationale','relevance','relevance_rationale',
                       'prescience','prescience_rationale']
    missing = [f for f in required_fields if not studies[0].get(f)]
    print(f"\nCompleteness Check:")
    if missing:
        print(f"  [REVIEW] Missing fields: {missing}")
    else:
        print("  [PASS] All 16 required studies.csv fields populated.")

    print("\n" + "=" * 60)
    print("Validation complete.")
    print("=" * 60)

if __name__ == '__main__':
    main()
