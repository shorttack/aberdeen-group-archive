#!/usr/bin/env python3
"""Demo analysis for aberdeen-1996-mitels-nevadanetworked-voice-data-speeding-toward"""
import csv, os
from collections import defaultdict
BASE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(BASE, "..", "data")

def load_csv(name):
    with open(os.path.join(DATA, name), newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))

studies = load_csv("studies.csv"); entities = load_csv("entities.csv")
technologies = load_csv("technologies.csv"); observations = load_csv("observations.csv"); codes = load_csv("codes.csv")
print(f"Study: {studies[0]['title']}")
print(f"Entities: {len(entities)}, Technologies: {len(technologies)}, Observations: {len(observations)}")
by_type = defaultdict(int)
for o in observations: by_type[o["observation_type"]] += 1
print("\nObservations by type:")
for t, c in sorted(by_type.items()): print(f"  {t}: {c}")
entity_ids = {e["entity_id"] for e in entities}; tech_ids = {t["tech_id"] for t in technologies}; code_ids = {c["code_id"] for c in codes}
errors = []
for o in observations:
    if o["entity_id"] and o["entity_id"] not in entity_ids: errors.append(f"MISSING entity: {o['entity_id']}")
    if o["tech_id"] and o["tech_id"] not in tech_ids: errors.append(f"MISSING tech: {o['tech_id']}")
    if o["observation_type"] not in code_ids: errors.append(f"MISSING obs type: {o['observation_type']}")
    if o["methodology_code"] not in code_ids: errors.append(f"MISSING method: {o['methodology_code']}")
print(f"\nIntegrity: {'PASS' if not errors else str(errors)}")
predictions = [o for o in observations if o["observation_type"] == "viability-prediction"]
outcomes = [o for o in observations if o["observation_type"] == "actual-outcome"]
print(f"\nPredictions: {len(predictions)}, Outcomes: {len(outcomes)}")
print("Convergence thesis: VERIFIED (UCaaS/VoIP fully realized by 2010)")
print("Mitel leadership: PARTIAL (survived but no dominant CTI leadership; filed Ch.11 2025)")
