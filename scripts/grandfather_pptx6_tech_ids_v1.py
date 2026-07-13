#!/usr/bin/env python3
"""
grandfather_pptx6_tech_ids_v1.py

Add the 3 benign new tech IDs from the pptx6 ingest to the Phase 0 audit
grandfather list so the regression gate passes. These are legitimate
ID-vs-name mismatches (product/vendor naming), not corruption:
  - teradata-dbms   "Teradata (data warehouse)"          (vendor teradata)
  - express-mdb     "IRI Express multidimensional database" (vendor iri-software)
  - vm-os           "IBM VM operating system"             (vendor ibm-corporation)

Backup + dry-run default. Also refreshes the baseline shape block to the
post-ingest live numbers so future drift alerts measure from the new floor.
"""
import json, sys, shutil, datetime
from pathlib import Path

BASE = Path.home()/"Desktop"/"Archive"/"Perplexity_Only"/"audit_masters_baseline.json"
COMMIT = "--commit" in sys.argv
TS = datetime.datetime.now(datetime.UTC).strftime("%Y%m%dT%H%M%SZ")
ADD = ["express-mdb", "teradata-dbms", "vm-os"]

# post-ingest live shape (from pipeline BEFORE audit + Phase 2 view counts, 2026-07-12)
NEW_SHAPE = {"studies":1511,"observations":25051,"entities":3316,"technologies":4393,"high_prescience":881}
NEW_COLLISION = {"entities_total":3316,"entities_distinct_norm":2929,"entities_ratio":0.8833,
                 "technologies_total":4393,"technologies_distinct_norm":4067,"technologies_ratio":0.9258}

b = json.load(open(BASE))
gl = b.get("tech_congruence_grandfathered_list", [])
before = len(gl)
for t in ADD:
    if t not in gl:
        gl.append(t)
b["tech_congruence_grandfathered_list"] = sorted(gl)
b["tech_congruence_grandfathered_count"] = len(b["tech_congruence_grandfathered_list"])
added = len(b["tech_congruence_grandfathered_list"]) - before

# refresh shape + collision floor so future audits measure drift from post-ingest state
b["shape"].update(NEW_SHAPE)
b["collision_ratio"].update(NEW_COLLISION)
b["captured_at_utc"] = datetime.datetime.now(datetime.UTC).strftime("%Y-%m-%dT%H:%M:%SZ")
b["source"] = "post pptx6 ingest (2026-07-12): grandfathered express-mdb/teradata-dbms/vm-os; shape+collision refreshed"

print(f"MODE: {'COMMIT' if COMMIT else 'DRY-RUN'} (stamp {TS})")
print(f"grandfather list: {before} -> {len(b['tech_congruence_grandfathered_list'])} (+{added})")
print(f"added: {[t for t in ADD if t in b['tech_congruence_grandfathered_list']]}")
print(f"shape now: {b['shape']}")

if COMMIT:
    shutil.copy2(BASE, BASE.with_name(BASE.name + f".bak_pptx6_{TS}"))
    json.dump(b, open(BASE, "w"), indent=2)
    print("wrote:", BASE)
else:
    print("DRY-RUN only — pass --commit to write.")
