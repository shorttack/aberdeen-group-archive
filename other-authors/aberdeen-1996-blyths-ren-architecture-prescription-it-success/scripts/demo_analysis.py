#!/usr/bin/env python3
"""Demo analysis script for aberdeen-1996-blyths-ren-architecture-prescription-it-success."""
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
    print(f"Entities: {len(entities)}, Technologies: {len(technologies)}, Observations: {len(observations)}")

    entity_ids = {e['entity_id'] for e in entities}
    tech_ids = {t['tech_id'] for t in technologies}
    code_ids = {c['code_id'] for c in codes}
    errors = []
    for o in observations:
        if o['entity_id'] and o['entity_id'] not in entity_ids:
            errors.append(f"MISSING entity: {o['entity_id']}")
        if o['tech_id'] and o['tech_id'] not in tech_ids:
            errors.append(f"MISSING tech: {o['tech_id']}")
        if o['observation_type'] not in code_ids:
            errors.append(f"MISSING code: {o['observation_type']}")
    print("Integrity:", "PASSED" if not errors else errors)

    predictions = [o for o in observations if o['observation_type'] == 'viability-prediction']
    outcomes = [o for o in observations if o['observation_type'] == 'actual-outcome']
    print(f"Predictions: {len(predictions)}, Outcomes: {len(outcomes)}")

if __name__ == "__main__":
    main()
