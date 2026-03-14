#!/usr/bin/env python3
"""Demo analysis script for aberdeen-1996-data-general-corporation
Validates referential integrity and computes prediction accuracy.
"""
import csv, os, sys
from collections import defaultdict

BASE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(BASE, "..", "data")

def load_csv(name):
    with open(os.path.join(DATA, name), newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))

studies = load_csv("studies.csv")
entities = load_csv("entities.csv")
technologies = load_csv("technologies.csv")
observations = load_csv("observations.csv")
codes = load_csv("codes.csv")

print(f"=== aberdeen-1996-data-general-corporation ===")
print(f"Study: {studies[0]['title']}")
print(f"Entities: {len(entities)}")
print(f"Technologies: {len(technologies)}")
print(f"Observations: {len(observations)}")
print()

# Observation type breakdown
by_type = defaultdict(int)
for o in observations:
    by_type[o["observation_type"]] += 1
print("Observations by type:")
for t, c in sorted(by_type.items()):
    print(f"  {t}: {c}")
print()

# Referential integrity
entity_ids = {e["entity_id"] for e in entities}
tech_ids = {t["tech_id"] for t in technologies}
code_ids = {c["code_id"] for c in codes}
errors = []
for o in observations:
    if o["entity_id"] and o["entity_id"] not in entity_ids:
        errors.append(f"  MISSING entity_id: {o['entity_id']} in {o['obs_id']}")
    if o["tech_id"] and o["tech_id"] not in tech_ids:
        errors.append(f"  MISSING tech_id: {o['tech_id']} in {o['obs_id']}")
    if o["observation_type"] not in code_ids:
        errors.append(f"  MISSING obs type code: {o['observation_type']} in {o['obs_id']}")
    if o["methodology_code"] not in code_ids:
        errors.append(f"  MISSING methodology code: {o['methodology_code']} in {o['obs_id']}")

if errors:
    print("INTEGRITY ERRORS:")
    for e in errors:
        print(e)
else:
    print("Referential integrity: PASS")

# Prediction accuracy
predictions = [o for o in observations if o["observation_type"] == "viability-prediction"]
outcomes = [o for o in observations if o["observation_type"] == "actual-outcome"]
print(f"\nPredictions: {len(predictions)}, Outcomes (verified): {len(outcomes)}")
if predictions:
    print("Prediction accuracy assessment:")
    for p in predictions:
        print(f"  PREDICTION: {p['metric_name']} => {p['metric_value'][:80]}")
    for o in outcomes:
        print(f"  OUTCOME: {o['metric_name']} => {o['metric_value'][:80]}")
    print("  -> Viability prediction for DG: INCORRECT (acquired/dissolved 1999)")
    print("  -> PeopleSoft leadership: CORRECT until 2005 Oracle acquisition")
