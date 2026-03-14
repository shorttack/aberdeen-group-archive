#!/usr/bin/env python3
"""
Demo Analysis Script — HP 9000 Enterprise Server: PA-8000 (1996)
Archival Ingest Skill v13 | Validation and analysis script
"""
import csv
import os
import sys
from collections import defaultdict

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def load_csv(name):
    path = os.path.join(BASE, "data", f"{name}.csv")
    with open(path, newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))

def main():
    print("=" * 60)
    print("DEMO ANALYSIS: HP 9000 PA-8000 Enterprise Server (1996)")
    print("=" * 60)

    studies = load_csv("studies")
    entities = load_csv("entities")
    technologies = load_csv("technologies")
    observations = load_csv("observations")
    codes = load_csv("codes")

    s = studies[0]
    print(f"\n[STUDY SUMMARY]")
    print(f"  Title:      {s['title'][:70]}...")
    print(f"  Date:       {s['date']}")
    print(f"  Importance: {s['importance']}")
    print(f"  Relevance:  {s['relevance']}")
    print(f"  Prescience: {s['prescience']}")

    print(f"\n[TABLE COUNTS]")
    print(f"  Entities:      {len(entities)}")
    print(f"  Technologies:  {len(technologies)}")
    print(f"  Observations:  {len(observations)}")

    print(f"\n[BENCHMARK RESULTS SUMMARY]")
    benchmarks = [o for o in observations if o["observation_type"] == "benchmark-result"]
    for b in sorted(benchmarks, key=lambda x: x["obs_id"]):
        print(f"  {b['metric_name'][:55]:<55} {b['metric_value'][:40]}")

    print(f"\n[REFERENTIAL INTEGRITY]")
    entity_ids = {e["entity_id"] for e in entities}
    tech_ids = {t["tech_id"] for t in technologies}
    code_ids = {c["code_id"] for c in codes}
    errors = []
    for o in observations:
        eid = o["entity_id"].strip()
        tid = o["tech_id"].strip()
        mc = o["methodology_code"].strip()
        ot = o["observation_type"].strip()
        if eid and eid not in entity_ids:
            errors.append(f"  [FAIL] {o['obs_id']}: entity_id '{eid}' missing")
        if tid and tid not in tech_ids:
            errors.append(f"  [FAIL] {o['obs_id']}: tech_id '{tid}' missing")
        if mc and mc not in code_ids:
            errors.append(f"  [FAIL] {o['obs_id']}: methodology_code '{mc}' missing")
        if ot not in code_ids:
            errors.append(f"  [FAIL] {o['obs_id']}: observation_type '{ot}' missing")
    if errors:
        for e in errors:
            print(e)
    else:
        print("  PASS — All foreign keys valid")

    print(f"\n[PREDICTION vs OUTCOME]")
    preds = [o for o in observations if o["observation_type"] == "viability-prediction"]
    outs = [o for o in observations if o["observation_type"] == "actual-outcome"]
    print(f"  Predictions: {len(preds)}, Outcomes: {len(outs)}")
    for p in preds:
        print(f"  PRED: {p['metric_name']} -> {p['metric_value'][:60]}")
    for o in outs:
        print(f"  OUT:  {o['metric_name']} -> {o['metric_value'][:60]}")

    print("\n" + "=" * 60)
    print("Validation complete.")
    return 0 if not errors else 1

if __name__ == "__main__":
    sys.exit(main())
