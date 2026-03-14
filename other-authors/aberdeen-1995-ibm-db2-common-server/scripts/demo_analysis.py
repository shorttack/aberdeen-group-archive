#!/usr/bin/env python3
"""
Demo Analysis Script
Dataset: Aberdeen Group — DB2 Common Server RDBMS (1995)
Study ID: aberdeen-1995-ibm-db2-common-server

Demonstrates how to load, validate, and analyze the Frictionless Data Package.

Usage:
    pip install frictionless pandas tabulate
    python scripts/demo_analysis.py
"""

import os
import sys
import pandas as pd

# Resolve paths relative to this script
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
BASE_DIR = os.path.dirname(SCRIPT_DIR)
DATA_DIR = os.path.join(BASE_DIR, "data")


def load_data():
    """Load all CSV files into DataFrames."""
    dfs = {}
    tables = ["studies", "entities", "technologies", "observations", "codes"]
    for t in tables:
        path = os.path.join(DATA_DIR, f"{t}.csv")
        dfs[t] = pd.read_csv(path)
        print(f"  Loaded {t}.csv — {len(dfs[t])} rows, {len(dfs[t].columns)} columns")
    return dfs


def validate_package():
    """Attempt Frictionless validation if available."""
    try:
        from frictionless import Package
        pkg_path = os.path.join(BASE_DIR, "datapackage.json")
        package = Package(pkg_path)
        report = package.validate()
        if report.valid:
            print("  ✓ Frictionless validation PASSED")
        else:
            print("  ✗ Frictionless validation FAILED:")
            for error in report.flatten(["rowNumber", "fieldNumber", "message"]):
                print(f"    {error}")
    except ImportError:
        print("  (frictionless not installed — skipping package validation)")
    except Exception as e:
        print(f"  Validation error: {e}")


def analysis_study_overview(dfs):
    """Print study metadata."""
    s = dfs["studies"].iloc[0]
    print(f"\n  Title   : {s['title']}")
    print(f"  Author  : {s['author']}")
    print(f"  Date    : {s['date']}")
    print(f"  Type    : {s['type']}")
    print(f"  Domain  : {s['domain']}")
    print(f"  Methods : {s['methodology']}")
    print(f"  Pages   : {s['page_count']}")
    print(f"  Source  : {s['source_url']}")


def analysis_entities(dfs):
    """Summarize entities by status."""
    ents = dfs["entities"]
    status_counts = ents["status"].value_counts()
    print(f"\n  Total entities: {len(ents)}")
    for status, count in status_counts.items():
        print(f"    {status:10s}: {count}")

    print("\n  Entity roster:")
    for _, row in ents.iterrows():
        parent = f" → {row['parent_entity']}" if pd.notna(row.get("parent_entity")) and row["parent_entity"] else ""
        print(f"    [{row['role']:10s}] {row['name']:30s} {row['status']:10s}{parent}")


def analysis_technologies(dfs):
    """Summarize technologies by lifecycle status and category."""
    tech = dfs["technologies"]
    print(f"\n  Total technologies: {len(tech)}")

    lifecycle_counts = tech["lifecycle_status"].value_counts()
    for lc, count in lifecycle_counts.items():
        print(f"    {lc:10s}: {count}")

    print("\n  Active technologies (still in use):")
    active = tech[tech["lifecycle_status"] == "active"]
    for _, row in active.iterrows():
        print(f"    {row['name']:35s} [{row['category']}]")

    print("\n  Obsolete technologies:")
    obsolete = tech[tech["lifecycle_status"] == "obsolete"]
    for _, row in obsolete.iterrows():
        print(f"    {row['name']:35s} [{row['category']}] — {row['lifecycle_note']}")


def analysis_observations(dfs):
    """Analyze the observation dataset."""
    obs = dfs["observations"]
    print(f"\n  Total observations: {len(obs)}")

    print("\n  Observations by type (top 10):")
    type_counts = obs["obs_type"].value_counts().head(10)
    for otype, count in type_counts.items():
        print(f"    {otype:35s}: {count}")

    print("\n  Observations by sentiment:")
    sent_counts = obs["sentiment"].value_counts()
    for sent, count in sent_counts.items():
        print(f"    {sent:10s}: {count}")

    print("\n  Quantitative observations (with numeric values):")
    quant = obs[obs["numeric_value"].notna()][
        ["obs_id", "subject", "predicate", "numeric_value", "unit"]
    ].sort_values("numeric_value", ascending=False)
    for _, row in quant.iterrows():
        print(f"    {row['obs_id']}: {row['subject']} — {row['numeric_value']:,.2f} {row['unit'] if pd.notna(row['unit']) else ''}")
        print(f"      ({row['predicate']})")

    print("\n  Observations by study section:")
    section_counts = obs["section"].value_counts()
    for section, count in section_counts.items():
        print(f"    {section:35s}: {count}")


def analysis_competitive_context(dfs):
    """Extract competitive observations."""
    obs = dfs["observations"]
    competitive = obs[obs["obs_type"].isin(["competitive-assessment", "market-assessment"])]
    print(f"\n  Competitive/market observations: {len(competitive)}")
    for _, row in competitive.iterrows():
        print(f"\n  [{row['obs_id']}] {row['subject']} — {row['predicate']}")
        print(f"    Value: {row['object_value'][:120]}...")
        print(f"    Sentiment: {row['sentiment']} | Confidence: {row['confidence']}")


def analysis_financial_data(dfs):
    """Extract financial observations."""
    obs = dfs["observations"]
    financial = obs[obs["obs_type"].isin(["revenue", "profit", "market-data"])]
    print(f"\n  Financial/market data observations: {len(financial)}")
    for _, row in financial.iterrows():
        val_str = f"{row['numeric_value']:,.1f} {row['unit']}" if pd.notna(row.get("numeric_value")) else row["object_value"]
        print(f"  {row['subject']:25s} | {row['predicate']:30s} | {val_str}")


def main():
    print("=" * 70)
    print("ABERDEEN GROUP — DB2 COMMON SERVER RDBMS (1995)")
    print("Frictionless Data Package Demo Analysis")
    print("=" * 70)

    print("\n[1] Loading data files...")
    dfs = load_data()

    print("\n[2] Validating Frictionless Data Package...")
    validate_package()

    print("\n[3] Study Overview")
    print("-" * 50)
    analysis_study_overview(dfs)

    print("\n[4] Entity Analysis")
    print("-" * 50)
    analysis_entities(dfs)

    print("\n[5] Technology Lifecycle Analysis")
    print("-" * 50)
    analysis_technologies(dfs)

    print("\n[6] Observation Analysis")
    print("-" * 50)
    analysis_observations(dfs)

    print("\n[7] Competitive Context")
    print("-" * 50)
    analysis_competitive_context(dfs)

    print("\n[8] Financial Data Points")
    print("-" * 50)
    analysis_financial_data(dfs)

    print("\n" + "=" * 70)
    print("Analysis complete.")
    print("=" * 70)


if __name__ == "__main__":
    main()
