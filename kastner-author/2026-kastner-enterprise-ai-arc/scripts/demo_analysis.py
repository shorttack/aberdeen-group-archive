#!/usr/bin/env python3
"""Validation and summary script for a single Frictionless Data Package."""
import csv, os, sys
from collections import Counter

def main():
    base = os.path.dirname(os.path.abspath(__file__))
    data = os.path.join(base, "..", "data")

    def load(name):
        with open(os.path.join(data, name)) as f:
            return list(csv.DictReader(f))

    studies = load("studies.csv")
    entities = load("entities.csv")
    techs = load("technologies.csv")
    obs = load("observations.csv")
    codes = load("codes.csv")

    print(f"Study: {studies[0]['title']}")
    print(f"Author: {studies[0]['author']}")
    print(f"Date: {studies[0]['date']}")
    print(f"Entities: {len(entities)}, Technologies: {len(techs)}, Observations: {len(obs)}")

    ent_ids = {e["entity_id"] for e in entities}
    tech_ids = {t["tech_id"] for t in techs}
    code_ids = {c["code_id"] for c in codes}
    errors = []
    for o in obs:
        if o["entity_id"] and o["entity_id"] not in ent_ids:
            errors.append(f"Missing entity: {o['entity_id']} in {o['obs_id']}")
        if o["tech_id"] and o["tech_id"] not in tech_ids:
            errors.append(f"Missing tech: {o['tech_id']} in {o['obs_id']}")
        if o["observation_type"] not in code_ids:
            errors.append(f"Missing code: {o['observation_type']} in {o['obs_id']}")

    if errors:
        print(f"VALIDATION ERRORS ({len(errors)}):")
        for e in errors:
            print(f"  - {e}")
    else:
        print("Validation: PASSED")

if __name__ == "__main__":
    main()
