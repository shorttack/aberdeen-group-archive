#!/usr/bin/env python3
"""
Demo analysis for: Commercial RISC/Unix 1996 — Aberdeen Group Market Viewpoint
Study ID: 1997-commercial-risc-unix-1996-mvp-711569

Demonstrates reading the Frictionless Data Package and performing basic analysis.
"""

import csv
import json
import os
from pathlib import Path

BASE = Path(__file__).parent.parent

def load_csv(name):
    rows = []
    with open(BASE / "data" / f"{name}.csv") as f:
        reader = csv.DictReader(f)
        for row in reader:
            rows.append(row)
    return rows

def main():
    print("=" * 60)
    print("Aberdeen RISC/Unix 1996 Market Viewpoint — Demo Analysis")
    print("=" * 60)

    # Load data
    observations = load_csv("observations")
    entities = load_csv("entities")
    technologies = load_csv("technologies")

    # 1. Market size summary
    market_obs = [o for o in observations if o["observation_type"] == "market-data"]
    print("\n--- Market Data Observations ---")
    for o in market_obs:
        print(f"  {o['metric_name']}: {o['metric_value']} ({o['year_observed']})")

    # 2. Prediction vs outcome accuracy
    predictions = {o["obs_id"]: o for o in observations if o["observation_type"] == "viability-prediction"}
    outcomes = [o for o in observations if o["observation_type"] == "actual-outcome"]
    print(f"\n--- Predictions vs Outcomes ---")
    print(f"  Viability predictions made: {len(predictions)}")
    print(f"  Actual outcomes recorded: {len(outcomes)}")
    print("\n  Outcomes:")
    for o in outcomes:
        print(f"    [{o['obs_id']}] {o['metric_name']}: {o['metric_value']}")

    # 3. Entity status summary
    print("\n--- Entity Status Summary ---")
    status_counts = {}
    for e in entities:
        s = e["status"]
        status_counts[s] = status_counts.get(s, 0) + 1
    for status, count in sorted(status_counts.items()):
        print(f"  {status}: {count}")

    # 4. Technology lifecycle
    print("\n--- Technology Lifecycle Summary ---")
    lifecycle_counts = {}
    for t in technologies:
        lc = t["lifecycle_current"]
        lifecycle_counts[lc] = lifecycle_counts.get(lc, 0) + 1
    for lc, count in sorted(lifecycle_counts.items()):
        print(f"  {lc}: {count}")

    # 5. Benchmark data
    benchmarks = [o for o in observations if o["observation_type"] == "benchmark-result"]
    print("\n--- Benchmark Results ---")
    for b in benchmarks:
        ent = next((e["entity_name"] for e in entities if e["entity_id"] == b["entity_id"]), b["entity_id"])
        print(f"  {ent}: {b['metric_name']} = {b['metric_value']} ({b['year_observed']})")

if __name__ == "__main__":
    main()
