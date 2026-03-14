#!/usr/bin/env python3
"""
demo_analysis.py
----------------
Demonstration analysis script for the Aberdeen Group (1995) Frictionless Data Package:
"Exploring Intersolv's Virtual Data Warehouse"

Data Package ID: aberdeen-1995-intersolv-virtual-data-warehouse

This script loads all CSV tables, performs a series of analytical queries,
and prints a structured summary report. It requires only pandas and the
Python standard library (no external API or database needed).

Usage:
    python scripts/demo_analysis.py

    # Or from repo root:
    python scripts/demo_analysis.py
"""

import os
import sys
import textwrap
from pathlib import Path

try:
    import pandas as pd
except ImportError:
    sys.exit("pandas is required. Install with: pip install pandas")


# ---------------------------------------------------------------------------
# Paths
# ---------------------------------------------------------------------------
SCRIPT_DIR = Path(__file__).resolve().parent
PKG_DIR = SCRIPT_DIR.parent
DATA_DIR = PKG_DIR / "data"


def load_tables():
    """Load all CSV tables into a dict of DataFrames."""
    tables = {}
    for name in ["studies", "entities", "technologies", "observations", "codes"]:
        path = DATA_DIR / f"{name}.csv"
        if not path.exists():
            sys.exit(f"Missing data file: {path}")
        tables[name] = pd.read_csv(path, dtype=str)
    return tables


def separator(title="", width=72):
    if title:
        pad = (width - len(title) - 2) // 2
        print("\n" + "=" * pad + f" {title} " + "=" * (width - pad - len(title) - 2))
    else:
        print("\n" + "=" * width)


def wrap(text, indent=4, width=68):
    """Word-wrap a string for terminal display."""
    return textwrap.fill(str(text), width=width, initial_indent=" " * indent,
                         subsequent_indent=" " * indent)


# ---------------------------------------------------------------------------
# Analysis functions
# ---------------------------------------------------------------------------

def study_overview(tables):
    separator("STUDY OVERVIEW")
    s = tables["studies"].iloc[0]
    print(f"  Title      : {s['title']}")
    print(f"  Author     : {s['author']}")
    print(f"  Date       : {s['date']}")
    print(f"  Type       : {s['type']}")
    print(f"  Domain     : {s['domain']}")
    print(f"  Methodology: {s['methodology']}")
    print(f"  Pages      : {s['page_count']}")
    print(f"  Words ~    : {s['word_count_approx']}")
    print(f"  Study #    : {s['study_num']}")
    print()
    print(wrap(s["abstract"]))


def entity_status_summary(tables):
    separator("ENTITY STATUS SUMMARY")
    ent = tables["entities"][["name", "entity_type", "status", "status_detail"]].copy()
    # Print each entity
    for _, row in ent.iterrows():
        print(f"\n  [{row['status'].upper():12s}] {row['name']} ({row['entity_type']})")
        print(wrap(row["status_detail"], indent=6))
    
    separator("Entity Status Counts")
    counts = ent["status"].value_counts()
    for status, count in counts.items():
        print(f"  {status:20s}: {count}")


def technology_lifecycle_summary(tables):
    separator("TECHNOLOGY LIFECYCLE SUMMARY")
    tech = tables["technologies"][["name", "category", "lifecycle_status", "successor_technology"]].copy()
    
    for _, row in tech.iterrows():
        successor = row["successor_technology"] if pd.notna(row["successor_technology"]) else "—"
        print(f"\n  [{row['lifecycle_status'].upper():12s}] {row['name']}")
        print(f"      Category : {row['category']}")
        print(f"      Successor: {successor}")
    
    separator("Lifecycle Status Counts")
    counts = tech["lifecycle_status"].value_counts()
    for status, count in counts.items():
        print(f"  {status:20s}: {count}")


def observation_distribution(tables):
    separator("OBSERVATION DISTRIBUTION")
    obs = tables["observations"]
    
    print("\n  By Observation Type:")
    type_counts = obs["observation_type"].value_counts()
    for otype, count in type_counts.items():
        bar = "█" * count
        print(f"    {otype:25s}: {count:2d}  {bar}")
    
    print("\n  By Sentiment:")
    sent_counts = obs["sentiment"].value_counts()
    for sent, count in sent_counts.items():
        bar = "█" * count
        print(f"    {sent:25s}: {count:2d}  {bar}")
    
    print("\n  By Section:")
    section_counts = obs["section"].value_counts()
    for section, count in section_counts.items():
        print(f"    {section:35s}: {count:2d}")


def positive_analyst_claims(tables):
    separator("TOP POSITIVE ANALYST CLAIMS (Aberdeen's Forward-Looking Assessments)")
    obs = tables["observations"]
    claims = obs[
        (obs["observation_type"] == "claim") & 
        (obs["sentiment"] == "positive")
    ][["obs_id", "text", "section"]].copy()
    
    for i, (_, row) in enumerate(claims.iterrows(), 1):
        print(f"\n  {i}. [{row['obs_id']}] Section: {row['section']}")
        print(wrap(row["text"]))


def user_feedback_summary(tables):
    separator("USER FEEDBACK SUMMARY")
    obs = tables["observations"]
    feedback = obs[obs["observation_type"] == "user-feedback"][["obs_id", "text", "sentiment"]].copy()
    
    for _, row in feedback.iterrows():
        print(f"\n  [{row['sentiment'].upper():8s}] {row['obs_id']}")
        print(wrap(row["text"]))


def competitive_observations(tables):
    separator("COMPETITIVE LANDSCAPE OBSERVATIONS")
    obs = tables["observations"]
    entities = tables["entities"][["entity_id", "name"]].copy()
    
    comp_obs = obs[obs["section"].str.contains("Competitive|competitive", na=False)].copy()
    comp_obs = comp_obs.merge(
        entities.rename(columns={"entity_id": "subject_entity_id", "name": "entity_name"}),
        on="subject_entity_id",
        how="left"
    )
    
    for _, row in comp_obs.iterrows():
        entity_label = row["entity_name"] if pd.notna(row.get("entity_name")) else "General"
        print(f"\n  Subject: {entity_label} | Type: {row['observation_type']} | Sentiment: {row['sentiment']}")
        print(wrap(row["text"]))


def pricing_observations(tables):
    separator("PRICING INFORMATION")
    obs = tables["observations"]
    pricing = obs[obs["observation_type"] == "pricing"][["obs_id", "text"]].copy()
    
    # Also grab any observations with pricing tags
    tagged = obs[obs["tags"].str.contains("pricing", na=False)][["obs_id", "text"]].copy()
    combined = pd.concat([pricing, tagged]).drop_duplicates("obs_id")
    
    for _, row in combined.iterrows():
        print(f"\n  [{row['obs_id']}]")
        print(wrap(row["text"]))


def tag_frequency(tables):
    separator("TOP TAGS (from observations)")
    obs = tables["observations"]
    all_tags = []
    for tags_str in obs["tags"].dropna():
        all_tags.extend([t.strip() for t in tags_str.split(",") if t.strip()])
    
    tag_series = pd.Series(all_tags).value_counts()
    print()
    for tag, count in tag_series.head(20).items():
        bar = "█" * count
        print(f"  {tag:35s}: {count:2d}  {bar}")


def vdw_product_features(tables):
    separator("VIRTUAL DATA WAREHOUSE — PRODUCT FEATURES")
    obs = tables["observations"]
    tech = tables["technologies"][["tech_id", "name"]].copy()
    
    features = obs[obs["observation_type"] == "product-feature"].copy()
    features = features.merge(
        tech.rename(columns={"tech_id": "subject_tech_id", "name": "tech_name"}),
        on="subject_tech_id",
        how="left"
    )
    
    # Group by technology
    for tech_name, group in features.groupby("tech_name"):
        print(f"\n  ── {tech_name} ──")
        for _, row in group.iterrows():
            print(wrap(f"• {row['text']}", indent=4))


def historical_context_note():
    separator("HISTORICAL CONTEXT NOTE")
    notes = [
        ("Virtual Data Warehouse → Data Virtualization",
         "The concept introduced by Intersolv in 1995 — metadata-driven access to "
         "distributed sources without physical ETL — directly anticipated modern data "
         "virtualization platforms (Denodo, TIBCO Data Virtualization) and data fabric "
         "architectures. The core insight proved correct; the product did not survive."),
        ("ODBC Longevity",
         "ODBC, central to Intersolv's architecture, remains an active standard in 2026. "
         "The DataDirect ODBC Pack evolved through multiple ownership changes "
         "(Intersolv → Merant → Progress Software) and continues as Progress DataDirect."),
        ("M&A Wave",
         "All major named vendors in this 1995 profile — Intersolv, TechGnosis, Cognos, "
         "Business Objects — were absorbed through acquisition within 13 years of "
         "publication. Only the DataDirect product brand and ODBC/SQL standards survived."),
    ]
    for title, text in notes:
        print(f"\n  {title}:")
        print(wrap(text))


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    print("\n" + "=" * 72)
    print("  Aberdeen Group (1995): Exploring Intersolv's Virtual Data Warehouse")
    print("  Frictionless Data Package — Demo Analysis")
    print("=" * 72)

    tables = load_tables()

    study_overview(tables)
    entity_status_summary(tables)
    technology_lifecycle_summary(tables)
    observation_distribution(tables)
    positive_analyst_claims(tables)
    user_feedback_summary(tables)
    competitive_observations(tables)
    pricing_observations(tables)
    vdw_product_features(tables)
    tag_frequency(tables)
    historical_context_note()

    separator()
    print("\n  Analysis complete.")
    print(f"  Data loaded from: {DATA_DIR}")
    print()


if __name__ == "__main__":
    main()
