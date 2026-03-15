#!/usr/bin/env python3
"""
Demo analysis script for:
  Electronic Commerce to Internet Commerce: The Evolution of The InterNetworked Enterprise
  Aberdeen Group Executive White Paper, November 1997
  Study ID: 1997-electronic-commerce-to-internet-com-b26a35
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
    print("=" * 70)
    print("Aberdeen Group: Electronic Commerce to Internet Commerce (1997)")
    print("Executive White Paper — David Alschuler, November 1997")
    print("=" * 70)

    studies = load_csv("studies.csv")
    entities = load_csv("entities.csv")
    technologies = load_csv("technologies.csv")
    observations = load_csv("observations.csv")

    study = studies[0]
    print(f"\nTitle:  {study['title']}")
    print(f"Scores: Importance={study['importance']}/5  Relevance={study['relevance']}/5  Prescience={study['prescience']}/5")

    print("\nAberdeen's Framework for Internet Commerce Assessment (1997):")
    for obs in observations:
        if obs["observation_type"] == "framework-factor":
            print(f"  - {obs['metric_value']}")

    print("\nPrediction vs. Actual Outcome:")
    outcomes = [o for o in observations if o["observation_type"] == "actual-outcome"]
    for outcome in outcomes:
        topic = outcome["metric_name"].replace(" - outcome", "")
        print(f"\n  Topic: {topic}")
        print(f"  Outcome: {outcome['metric_value']}")

    print("\nTechnology Lifecycle (1997 → present):")
    for tech in technologies:
        print(f"  {tech['tech_name']:<40} {tech['lifecycle_at_study']:<20} → {tech['lifecycle_current']}")

    print("\nHistorical Context:")
    print("  - Amazon launched: 1994 (3 years before this report)")
    print("  - eBay launched: 1995")
    print("  - Aberdeen said: 'revolution is imminent' (November 1997)")
    print("  - Global e-commerce by 2024: ~$6.38 trillion (eMarketer)")

    print("\n" + "=" * 70)
    print("Source: https://web.archive.org/web/19980131062330/")
    print("  http://www.aberdeen.com:80/research/abstract/97110210.htm")
    print("License: CC-BY-4.0")


if __name__ == "__main__":
    main()
