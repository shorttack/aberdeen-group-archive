#!/usr/bin/env python3
"""
demo_analysis.py
================
Demo analysis script for the Aberdeen Group HP SoftBench 5.0 (1995) data package.
Study ID: aberdeen-1995-hp-softbench

Loads all CSV files from the data package and produces summary statistics and
example analyses for:
  - Observation type distribution
  - Sentiment breakdown
  - Technology lifecycle status counts
  - Entity status distribution
  - Section-level observation counts

Usage:
    python scripts/demo_analysis.py

Requirements:
    pip install pandas tabulate
"""

import os
import sys
import csv
from pathlib import Path
from collections import Counter

# Resolve paths relative to this script's location
SCRIPT_DIR = Path(__file__).parent
PACKAGE_DIR = SCRIPT_DIR.parent
DATA_DIR = PACKAGE_DIR / "data"


def load_csv(filename: str) -> list[dict]:
    """Load a CSV file from the data directory and return a list of row dicts."""
    path = DATA_DIR / filename
    if not path.exists():
        raise FileNotFoundError(f"CSV file not found: {path}")
    with open(path, newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def print_section(title: str) -> None:
    print(f"\n{'='*60}")
    print(f"  {title}")
    print(f"{'='*60}")


def print_counter(counter: Counter, label: str = "Value", count_label: str = "Count") -> None:
    """Print a Counter as a simple table."""
    max_len = max((len(k) for k in counter), default=10)
    col_w = max(max_len, len(label))
    print(f"\n  {label:<{col_w}}  {count_label}")
    print(f"  {'-'*col_w}  {'-'*8}")
    for value, count in counter.most_common():
        print(f"  {value:<{col_w}}  {count}")


def analyze_studies(rows: list[dict]) -> None:
    print_section("STUDIES")
    for row in rows:
        print(f"\n  Study ID   : {row['study_id']}")
        print(f"  Title      : {row['title']}")
        print(f"  Author     : {row['author']}")
        print(f"  Date       : {row['date']}")
        print(f"  Type       : {row['type']}")
        print(f"  Domain     : {row['domain']}")
        print(f"  Methodology: {row['methodology']}")
        print(f"\n  Abstract:\n    {row['abstract']}")


def analyze_observations(rows: list[dict]) -> None:
    print_section(f"OBSERVATIONS  ({len(rows)} total)")

    # Observation type distribution
    type_counts = Counter(r["observation_type"] for r in rows)
    print_counter(type_counts, label="Observation Type")

    # Sentiment distribution
    sentiment_counts = Counter(r["sentiment"] for r in rows)
    print_counter(sentiment_counts, label="Sentiment")

    # Section distribution
    section_counts = Counter(r["section"] for r in rows)
    print_counter(section_counts, label="Document Section")

    # Page distribution
    page_counts = Counter(str(r["page_ref"]) for r in rows)
    print_counter(page_counts, label="PDF Page")

    # Sample positive analyst opinions
    print("\n  --- Sample Positive Analyst Opinions ---")
    for r in rows:
        if r["observation_type"] == "analyst-opinion" and r["sentiment"] == "positive":
            print(f"\n  [{r['obs_id']}] ({r['section']})")
            subject = r["subject"]
            claim = r["claim"]
            print(f"  Subject: {subject}")
            # Wrap claim at ~70 chars
            words = claim.split()
            lines, current = [], []
            for word in words:
                current.append(word)
                if len(" ".join(current)) > 70:
                    lines.append("  Claim: " + " ".join(current[:-1]) if not lines else "         " + " ".join(current[:-1]))
                    current = [word]
            if current:
                lines.append(("  Claim: " if not lines else "         ") + " ".join(current))
            print("\n".join(lines))


def analyze_technologies(rows: list[dict]) -> None:
    print_section(f"TECHNOLOGIES  ({len(rows)} total)")

    lifecycle_counts = Counter(r["lifecycle_status"] for r in rows)
    print_counter(lifecycle_counts, label="Lifecycle Status")

    # Group by category
    category_counts = Counter(r["category"] for r in rows)
    print_counter(category_counts, label="Category")

    # List active technologies
    active = [r for r in rows if r["lifecycle_status"] == "active"]
    print(f"\n  --- Active Technologies ({len(active)}) ---")
    for r in active:
        print(f"  {r['name']:<40} vendor: {r['vendor']}")

    # List obsolete/discontinued
    obsolete = [r for r in rows if r["lifecycle_status"] in ("obsolete", "discontinued")]
    print(f"\n  --- Obsolete / Discontinued Technologies ({len(obsolete)}) ---")
    for r in obsolete:
        print(f"  {r['name']:<40} ({r['lifecycle_status']})")


def analyze_entities(rows: list[dict]) -> None:
    print_section(f"ENTITIES  ({len(rows)} total)")

    status_counts = Counter(r["status"] for r in rows)
    print_counter(status_counts, label="Entity Status")

    type_counts = Counter(r["type"] for r in rows)
    print_counter(type_counts, label="Entity Type")

    # Notable status changes
    changed = [r for r in rows if r["status"] not in ("active",)]
    print(f"\n  --- Entities with Changed Status ({len(changed)}) ---")
    for r in changed:
        print(f"\n  {r['name']}")
        print(f"    Status: {r['status']}")
        note = r["status_note"]
        # wrap at 70 chars
        words = note.split()
        lines, current = [], []
        for word in words:
            current.append(word)
            if len(" ".join(current)) > 68:
                lines.append("    Note: " + " ".join(current[:-1]) if not lines else "          " + " ".join(current[:-1]))
                current = [word]
        if current:
            lines.append(("    Note: " if not lines else "          ") + " ".join(current))
        print("\n".join(lines))


def analyze_codes(rows: list[dict]) -> None:
    print_section(f"CODES  ({len(rows)} total)")
    code_type_counts = Counter(r["code_type"] for r in rows)
    print_counter(code_type_counts, label="Code Type")


def compute_summary_stats(observations: list[dict], technologies: list[dict], entities: list[dict]) -> None:
    print_section("SUMMARY STATISTICS")

    total_obs = len(observations)
    positive_obs = sum(1 for r in observations if r["sentiment"] == "positive")
    pct_positive = round(100 * positive_obs / total_obs, 1) if total_obs else 0

    analyst_opinion_count = sum(1 for r in observations if "analyst" in r["observation_type"])
    vendor_claim_count = sum(1 for r in observations if "vendor" in r["observation_type"] or r["observation_type"] == "product-claim")

    active_tech = sum(1 for r in technologies if r["lifecycle_status"] == "active")
    obsolete_tech = sum(1 for r in technologies if r["lifecycle_status"] in ("obsolete", "discontinued", "largely-obsolete"))
    legacy_tech = sum(1 for r in technologies if r["lifecycle_status"] == "legacy")

    active_entities = sum(1 for r in entities if r["status"] == "active")
    changed_entities = sum(1 for r in entities if r["status"] != "active")

    print(f"""
  Total observations extracted  : {total_obs}
  Positive sentiment observations: {positive_obs} ({pct_positive}%)
  Analyst-sourced observations  : {analyst_opinion_count}
  Product/vendor claim obs.     : {vendor_claim_count}

  Technologies tracked          : {len(technologies)}
    Active                      : {active_tech}
    Legacy                      : {legacy_tech}
    Obsolete / discontinued     : {obsolete_tech}

  Entities tracked              : {len(entities)}
    Still active (2026)         : {active_entities}
    Changed status since 1995   : {changed_entities}
""")


def main():
    print("\nAberdeen Group — HP C++ SoftBench 5.0 (1995)")
    print("Frictionless Data Package Demo Analysis")
    print(f"Data directory: {DATA_DIR.resolve()}")

    # Load all data files
    studies = load_csv("studies.csv")
    observations = load_csv("observations.csv")
    technologies = load_csv("technologies.csv")
    entities = load_csv("entities.csv")
    codes = load_csv("codes.csv")

    # Run analyses
    analyze_studies(studies)
    analyze_observations(observations)
    analyze_technologies(technologies)
    analyze_entities(entities)
    analyze_codes(codes)
    compute_summary_stats(observations, technologies, entities)

    print("\nDemo analysis complete.\n")


if __name__ == "__main__":
    main()
