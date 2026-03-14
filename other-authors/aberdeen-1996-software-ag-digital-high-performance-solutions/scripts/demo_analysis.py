#!/usr/bin/env python3
"""
Demo Analysis Script - aberdeen-1996-software-ag-digital-high-performance-solutions
Archival Ingest Skill v13 — Validation and Summary
"""
import csv
import os
import sys

BASE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(BASE, "..", "data")

def load_csv(name):
    path = os.path.join(DATA, name)
    with open(path, newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))

def main():
    print("=" * 60)
    print(f"STUDY: aberdeen-1996-software-ag-digital-high-performance-solutions")
    print("=" * 60)

    studies = load_csv("studies.csv")
    entities = load_csv("entities.csv")
    technologies = load_csv("technologies.csv")
    observations = load_csv("observations.csv")
    codes = load_csv("codes.csv")

    s = studies[0]
    print(f"Title     : {s['title']}")
    print(f"Author    : {s['author']}")
    print(f"Date      : {s['date']}")
    print(f"Importance: {s['importance']} — {s['importance_rationale'][:80]}...")
    print(f"Relevance : {s['relevance']} — {s['relevance_rationale'][:80]}...")
    print(f"Prescience: {s['prescience']} — {s['prescience_rationale'][:80]}...")
    print()

    print(f"Entities   : {len(entities)}")
    print(f"Technologies: {len(technologies)}")
    print(f"Observations: {len(observations)}")
    print()

    # Observation type breakdown
    obs_types = {}
    for o in observations:
        ot = o["observation_type"]
        obs_types[ot] = obs_types.get(ot, 0) + 1
    print("Observation Types:")
    for ot, cnt in sorted(obs_types.items()):
        print(f"  {ot:<35} {cnt}")
    print()

    # Referential integrity: entity_id
    valid_entities = {e["entity_id"] for e in entities}
    valid_entities.add("")
    bad_entity_refs = [
        o["obs_id"] for o in observations
        if o["entity_id"] not in valid_entities
    ]
    if bad_entity_refs:
        print(f"[WARN] {len(bad_entity_refs)} observations with unknown entity_id: {bad_entity_refs}")
    else:
        print("[OK] All entity_id references valid.")

    # Referential integrity: tech_id
    valid_techs = {t["tech_id"] for t in technologies}
    valid_techs.add("")
    bad_tech_refs = [
        o["obs_id"] for o in observations
        if o["tech_id"] not in valid_techs
    ]
    if bad_tech_refs:
        print(f"[WARN] {len(bad_tech_refs)} observations with unknown tech_id: {bad_tech_refs}")
    else:
        print("[OK] All tech_id references valid.")

    # Code coverage
    valid_obs_types = {c["code_id"] for c in codes if c["code_type"] == "observation_type"}
    bad_codes = [
        o["obs_id"] for o in observations
        if o["observation_type"] not in valid_obs_types
    ]
    if bad_codes:
        print(f"[WARN] {len(bad_codes)} observations with unknown observation_type: {bad_codes}")
    else:
        print("[OK] All observation_type codes valid.")

    # Prediction accuracy
    predictions = [o for o in observations if o["observation_type"] == "viability-prediction"]
    outcomes = [o for o in observations if o["observation_type"] == "actual-outcome"]
    print(f"\nPrediction pairs: {len(predictions)} predictions / {len(outcomes)} outcomes")
    if predictions:
        coverage = len(outcomes) / len(predictions) * 100
        print(f"Outcome coverage: {coverage:.0f}%")
        verified = [o for o in outcomes if o["confidence"] == "verified"]
        print(f"Verified outcomes: {len(verified)}/{len(outcomes)}")

    print()
    print("Validation complete.")

if __name__ == "__main__":
    main()
