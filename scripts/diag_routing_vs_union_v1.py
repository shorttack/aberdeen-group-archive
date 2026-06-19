#!/usr/bin/env python3
"""
diag_routing_vs_union_v1.py — diagnose the 474 vs 217 partition discrepancy.

Walk both scripts' P1-eligibility logic side-by-side on the same inputs.
Find rows that union v2 routed to P1 but route_quotations_to_horizon_v1
did not (or vice versa). Print the first 10 differences with full row
context.
"""
from __future__ import annotations
import csv, json, re, sys, unicodedata
from pathlib import Path

QUOTATIONS = Path.home() / "Desktop/Archive/aberdeen-group-archive/kastner-author/quotations"
CORPUS_JSON = QUOTATIONS / "article_corpus_v1.json"
CSV_PATH    = QUOTATIONS / "kastner_quotes_clean.csv"
ADMITS_JSON = QUOTATIONS / "_format_mismatch_admits_v1.json"

def normalize_text(s: str) -> str:
    if not s: return ""
    s = unicodedata.normalize("NFKD", s)
    s = "".join(c for c in s if not unicodedata.combining(c))
    s = s.lower()
    s = re.sub(r"[^a-z0-9 ]+", " ", s)
    return re.sub(r"\s+", " ", s).strip()

# Load corpus
corpus = json.loads(CORPUS_JSON.read_text())
articles = corpus.get("articles", [])
corpus_norms_from_field = {a.get("headline_norm","") for a in articles if a.get("headline_norm")}
corpus_norms_recomputed = {normalize_text(a.get("headline","")) for a in articles}
print(f"corpus articles: {len(articles)}")
print(f"  distinct headline_norms (from JSON field):     {len(corpus_norms_from_field)}")
print(f"  distinct headline_norms (recomputed from headline): {len(corpus_norms_recomputed)}")
print(f"  set diff (field vs recomputed):                {len(corpus_norms_from_field ^ corpus_norms_recomputed)}")
print()
# Sample a few articles to see if headline_norm field matches recomputed
print("first 5 articles — field vs recomputed headline_norm:")
for a in articles[:5]:
    field = a.get("headline_norm","")
    recomp = normalize_text(a.get("headline",""))
    match = "✓" if field == recomp else "✗"
    print(f"  {match}  headline={a.get('headline','')[:60]!r}")
    if field != recomp:
        print(f"     field:    {field!r}")
        print(f"     recomp:   {recomp!r}")
print()

# Admits
admit_row_ids = set()
if ADMITS_JSON.exists():
    admit_row_ids = {int(r) for r in json.loads(ADMITS_JSON.read_text()).get("admit_row_ids", [])}
print(f"admit row_ids: {sorted(admit_row_ids)}")
print()

# Master
with open(CSV_PATH, newline="") as f:
    rows = list(csv.DictReader(f))
print(f"master rows: {len(rows)}")

# Partition using EACH set
p1_by_field = []
p1_by_recomp = []
for r in rows:
    nh = normalize_text(r.get("headline",""))
    try:
        rid = int(r.get("row_id",""))
    except:
        rid = None
    is_admit = rid is not None and rid in admit_row_ids
    if is_admit or (nh and nh in corpus_norms_from_field):
        p1_by_field.append(r)
    # separate count
    if is_admit or (nh and nh in corpus_norms_recomputed):
        p1_by_recomp.append(r)

print(f"\nP1 using corpus 'headline_norm' field:     {len(p1_by_field)}")
print(f"P1 using recomputed normalize(headline):    {len(p1_by_recomp)}")
print()

# Show the divergent rows
field_ids = {r['row_id'] for r in p1_by_field}
recomp_ids = {r['row_id'] for r in p1_by_recomp}
only_in_recomp = recomp_ids - field_ids
only_in_field = field_ids - recomp_ids
print(f"in recomputed but NOT in field: {len(only_in_recomp)}")
print(f"in field but NOT in recomputed: {len(only_in_field)}")
print()

# Sample 10 rows that ARE in recomputed but not field
if only_in_recomp:
    print("sample (10) of rows that recomputed-norm matches corpus but field-norm doesn't:")
    shown = 0
    for r in rows:
        if r['row_id'] in only_in_recomp:
            nh = normalize_text(r.get("headline",""))
            print(f"  row_id={r['row_id']} headline={r['headline'][:60]!r}")
            print(f"     recomp(row.headline) = {nh!r}")
            # Find which corpus article shares this recomputed norm
            for a in articles:
                if normalize_text(a.get("headline","")) == nh:
                    print(f"     corpus article: headline={a.get('headline','')[:60]!r}")
                    print(f"     corpus field headline_norm = {a.get('headline_norm','')!r}")
                    break
            shown += 1
            if shown >= 10: break

# Also: how many rows have non-empty headline and would match via recomputed?
nonempty_p1_recomp = [r for r in p1_by_recomp if r['row_id'] not in admit_row_ids]
print(f"\nnon-admit P1-by-recomputed: {len(nonempty_p1_recomp)}")
print(f"(union v2 reported 464 non-admit P1 rows; expected to match)")
