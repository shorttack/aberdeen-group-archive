#!/usr/bin/env python3
"""Demo analysis script for Cisco ABU dataset."""
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

    predictions = [o for o in observations if o['observation_type'] == 'viability-prediction']
    outcomes = [o for o in observations if o['observation_type'] == 'actual-outcome']
    print(f"Predictions: {len(predictions)}, Outcomes: {len(outcomes)}")
    for p in predictions:
        print(f"  PRED: {p['metric_name']}: {p['metric_value'][:60]}")

if __name__ == "__main__":
    main()
