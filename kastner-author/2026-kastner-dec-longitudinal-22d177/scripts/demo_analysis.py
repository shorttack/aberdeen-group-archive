#!/usr/bin/env python3
import csv
from collections import Counter
from pathlib import Path

root = Path(__file__).resolve().parents[1]
data = root / "data"

def rows(name):
    with (data / name).open(newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))

studies = rows("studies.csv")
entities = rows("entities.csv")
techs = rows("technologies.csv")
obs = rows("observations.csv")
codes = rows("codes.csv")

print("DEC longitudinal package")
print("study_id:", studies[0]["study_id"] if studies else "missing")
print("studies:", len(studies))
print("entities:", len(entities))
print("technologies:", len(techs))
print("observations:", len(obs))
print("codes:", len(codes))
print("verification_method:", dict(Counter(o["verification_method"] for o in obs)))
print("observation_type top:", Counter(o["observation_type"] for o in obs).most_common(10))

required = {"ingest-extraction", "web-source", "outcome-linkage", "unverified", "placeholder", "cross-reference"}
bad = sorted(set(o["verification_method"] for o in obs) - required)
if bad:
    raise SystemExit(f"Invalid verification_method values: {bad}")
if any(not o["verification_method"] for o in obs):
    raise SystemExit("Blank verification_method found")
print("QA: PASS")
