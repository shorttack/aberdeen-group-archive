#!/usr/bin/env python3
"""Demo analysis script for Bull Sagister dataset."""
import os, csv

BASE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(BASE, "..", "data")

def load_csv(name):
    with open(os.path.join(DATA, name), newline="") as f:
        return list(csv.DictReader(f))

def main():
    studies = load_csv("studies.csv")
    entities = load_csv("entities.csv")
    technologies = load_csv("technologies.csv")
    observations = load_csv("observations.csv")
    codes = load_csv("codes.csv")

    s = studies[0]
    print(f"Study: {s['title']}")
    print(f"Prescience: {s['prescience']} - {s['prescience_rationale'][:100]}")
    print(f"Entities: {len(entities)}, Tech: {len(technologies)}, Obs: {len(observations)}")

    entity_ids = {e['entity_id'] for e in entities}
    tech_ids = {t['tech_id'] for t in technologies}
    code_ids = {c['code_id'] for c in codes}
    errors = [o['obs_id'] for o in observations
              if (o['entity_id'] and o['entity_id'] not in entity_ids)
              or (o['tech_id'] and o['tech_id'] not in tech_ids)
              or o['observation_type'] not in code_ids]
    print("Integrity:", "PASSED" if not errors else f"FAILED: {errors}")

    by_type = {}
    for o in observations:
        by_type[o['observation_type']] = by_type.get(o['observation_type'], 0) + 1
    for k,v in sorted(by_type.items()):
        print(f"  {k}: {v}")

if __name__ == "__main__":
    main()
