#!/usr/bin/env python3
"""
Demo analysis script for:
  DynaFlo Systems: E-Mail For The Business Masses
  Aberdeen Group Vendor Profile, July 1997
  Study ID: 1997-dynaflo-systems----e-mail-for-the-b-854582
"""

import csv
import os
from collections import Counter

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, "data")


def load_csv(filename):
    path = os.path.join(DATA_DIR, filename)
    with open(path, newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def main():
    print("=" * 60)
    print("Aberdeen Group: DynaFlo Systems — E-Mail For The Business Masses")
    print("Vendor Profile, July 1997")
    print("=" * 60)

    studies = load_csv("studies.csv")
    entities = load_csv("entities.csv")
    technologies = load_csv("technologies.csv")
    observations = load_csv("observations.csv")

    study = studies[0]
    print(f"\nTitle:   {study['title']}")
    print(f"Authors: {study['author']}")
    print(f"Date:    {study['date']}")
    print(f"Type:    {study['type']}")
    print(f"\nScores: Importance={study['importance']}/5  Relevance={study['relevance']}/5  Prescience={study['prescience']}/5")

    print(f"\nKey Market Statistics from Aberdeen Field Research:")
    for obs in observations:
        if obs["observation_type"] == "market-data":
            print(f"  - {obs['metric_name']}: {obs['metric_value']}")

    print(f"\nPredictions and Outcomes:")
    predictions = {o["obs_id"]: o for o in observations if o["observation_type"] == "viability-prediction"}
    outcomes = [o for o in observations if o["observation_type"] == "actual-outcome"]
    for outcome in outcomes:
        print(f"  Prediction: {outcome['metric_name'].replace(' - outcome', '')}")
        print(f"  Outcome:    {outcome['metric_value']}")
        print()

    print(f"Technologies ({len(technologies)}):")
    for tech in technologies:
        print(f"  {tech['tech_name']:<35} {tech['lifecycle_at_study']:<20} → {tech['lifecycle_current']}")

    print("\n" + "=" * 60)
    print("Source: https://web.archive.org/web/19981202011504/")
    print("  http://www.aberdeen.com:80/research/abstract/97070128.htm")
    print("License: CC-BY-4.0")


if __name__ == "__main__":
    main()
