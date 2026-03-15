#!/usr/bin/env python3
"""
Demo analysis script for:
  Competitive Advantage Through Prism Metadata Scalability
  Aberdeen Group Vendor Profile, June 1997
  Study ID: 1997-dw-competitive-advantage-through-pr-b307c7
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
    print("Aberdeen Group: Competitive Advantage Through Prism Metadata Scalability")
    print("Vendor Profile, June 1997 — Prism Solutions Inc.")
    print("=" * 70)

    studies = load_csv("studies.csv")
    entities = load_csv("entities.csv")
    technologies = load_csv("technologies.csv")
    observations = load_csv("observations.csv")

    study = studies[0]
    print(f"\nTitle:  {study['title']}")
    print(f"Domain: {study['subject_domain']}")
    print(f"Scores: Importance={study['importance']}/5  Relevance={study['relevance']}/5  Prescience={study['prescience']}/5")

    # Key metrics
    print("\nKey Prism Metrics (1997):")
    for obs in observations:
        if obs["observation_type"] == "benchmark-result":
            print(f"  - {obs['metric_name']}: {obs['metric_value'][:80]}")

    # Observation distribution
    print(f"\nObservations ({len(observations)} total):")
    obs_types = Counter(o["observation_type"] for o in observations)
    for otype, count in obs_types.most_common():
        print(f"  {otype:<30} {count:>3}")

    # Technology lifecycle
    print("\nTechnology Lifecycle (1997 → 2026):")
    for tech in technologies:
        print(f"  {tech['tech_name'][:42]:<42} {tech['lifecycle_at_study']:<20} → {tech['lifecycle_current']}")

    # Acquisition chain
    print("\nPrism Solutions Acquisition Chain:")
    chain = [
        ("Prism Solutions Inc.", "1997", "$42M to Ardent Software (Jan 1999)"),
        ("Ardent Software Inc.", "1999", "~$880M to Informix Corporation (Mar 2000)"),
        ("Informix Corporation", "2000", "DB sold to IBM $1B (Apr 2001); rest → Ascential"),
        ("Ascential Software", "2001", "$1.1B to IBM (May 2005)"),
        ("IBM InfoSphere DataStage", "2005", "Active — enterprise ETL platform today"),
    ]
    for company, year, note in chain:
        print(f"  {year} | {company:<35} → {note}")

    print("\nKey Aberdeen Prediction vs. Outcome:")
    outcomes = [o for o in observations if o["observation_type"] == "actual-outcome"]
    for outcome in outcomes:
        topic = outcome["metric_name"].replace(" - outcome", "")
        print(f"\n  [{topic}]")
        print(f"  Outcome: {outcome['metric_value'][:100]}")

    print("\n" + "=" * 70)
    print("Source: https://web.archive.org/web/19970604113329/")
    print("  http://www.aberdeen.com:80/secure/profiles/1997/prism/body.htm")
    print("License: CC-BY-4.0")


if __name__ == "__main__":
    main()
