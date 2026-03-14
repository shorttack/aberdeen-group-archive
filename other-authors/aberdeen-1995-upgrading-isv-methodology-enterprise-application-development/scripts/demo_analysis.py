#!/usr/bin/env python3
"""
Demo analysis script for aberdeen-1995-upgrading-isv-methodology-enterprise-application-development
Validates referential integrity and reports statistics.
"""
import csv, os, sys
from collections import Counter
from pathlib import Path

BASE = Path(__file__).parent.parent / 'data'

def load_csv(name):
    path = BASE / name
    if not path.exists():
        print(f"ERROR: {path} not found")
        sys.exit(1)
    with open(path, newline='', encoding='utf-8') as f:
        return list(csv.DictReader(f))

def main():
    studies = load_csv('studies.csv')
    entities = load_csv('entities.csv')
    technologies = load_csv('technologies.csv')
    observations = load_csv('observations.csv')
    codes = load_csv('codes.csv')

    print(f"=== aberdeen-1995-upgrading-isv-methodology-enterprise-application-development ===")
    print(f"Studies     : {len(studies)} row(s)")
    print(f"Entities    : {len(entities)} row(s)")
    print(f"Technologies: {len(technologies)} row(s)")
    print(f"Observations: {len(observations)} row(s)")
    print(f"Codes       : {len(codes)} row(s)")
    print()

    # Referential integrity checks
    entity_ids = {r['entity_id'] for r in entities}
    tech_ids = {r['tech_id'] for r in technologies}
    errors = 0

    for obs in observations:
        eid = obs.get('entity_id', '').strip()
        tid = obs.get('tech_id', '').strip()
        if eid and eid not in entity_ids:
            print(f"  REF ERROR: obs {obs['obs_id']} entity_id={eid} not in entities.csv")
            errors += 1
        if tid and tid not in tech_ids:
            print(f"  REF ERROR: obs {obs['obs_id']} tech_id={tid} not in technologies.csv")
            errors += 1

    if errors == 0:
        print("  ✓ Referential integrity: PASS")
    else:
        print(f"  ✗ Referential integrity: {errors} error(s)")

    print()
    # Observation type distribution
    obs_types = Counter(obs['observation_type'] for obs in observations)
    print("Observation type distribution:")
    for otype, count in sorted(obs_types.items()):
        print(f"  {otype:<30} {count}")

    print()
    # Confidence distribution
    conf = Counter(obs['confidence'] for obs in observations)
    print("Confidence distribution:")
    for c, count in sorted(conf.items()):
        print(f"  {c:<10} {count}")

    print()
    # Entity status distribution
    status_dist = Counter(e['status'] for e in entities)
    print("Entity status distribution:")
    for s, count in sorted(status_dist.items()):
        print(f"  {s:<20} {count}")

    print()
    # Viability predictions vs actual outcomes
    predictions = [o for o in observations if o['observation_type'] == 'viability-prediction']
    outcomes = [o for o in observations if o['observation_type'] == 'actual-outcome']
    print(f"Viability predictions : {len(predictions)}")
    print(f"Actual outcomes       : {len(outcomes)}")

    print()
    # Studies assessment
    for s in studies:
        print(f"Study importance  : {s['importance']} — {s['importance_rationale'][:80]}...")
        print(f"Study relevance   : {s['relevance']} — {s['relevance_rationale'][:80]}...")
        print(f"Study prescience  : {s['prescience']} — {s['prescience_rationale'][:80]}...")

if __name__ == '__main__':
    main()
