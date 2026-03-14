#!/usr/bin/env python3
"""Demo Analysis — HP Networking Vision Workgroups (1996)"""
import csv, os, sys
from collections import defaultdict

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def load_csv(name):
    with open(os.path.join(BASE,"data",f"{name}.csv"), newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))

def main():
    print("="*60)
    print("DEMO ANALYSIS: HP Networking Vision Workgroups (1996)")
    print("="*60)
    studies=load_csv("studies"); entities=load_csv("entities")
    technologies=load_csv("technologies"); observations=load_csv("observations"); codes=load_csv("codes")
    s=studies[0]
    print(f"\n[STUDY] {s['title'][:70]}...")
    print(f"  Importance={s['importance']} | Relevance={s['relevance']} | Prescience={s['prescience']}")
    print(f"\n[COUNTS] Entities={len(entities)} | Techs={len(technologies)} | Obs={len(observations)}")
    tc=defaultdict(int)
    for o in observations: tc[o["observation_type"]]+=1
    print("\n[OBS TYPES]")
    for t,c in sorted(tc.items(),key=lambda x:-x[1]): print(f"  {t:<30} {c}")
    print("\n[REFERENTIAL INTEGRITY]")
    eids={e["entity_id"] for e in entities}; tids={t["tech_id"] for t in technologies}; cids={c["code_id"] for c in codes}
    errors=[]
    for o in observations:
        if o["entity_id"].strip() and o["entity_id"].strip() not in eids: errors.append(f"  entity_id {o['entity_id']} missing")
        if o["tech_id"].strip() and o["tech_id"].strip() not in tids: errors.append(f"  tech_id {o['tech_id']} missing")
        if o["methodology_code"].strip() and o["methodology_code"].strip() not in cids: errors.append(f"  mc {o['methodology_code']} missing")
        if o["observation_type"].strip() not in cids: errors.append(f"  obs_type {o['observation_type']} missing")
    print("  PASS" if not errors else "\n".join(errors))
    preds=[o for o in observations if o["observation_type"]=="viability-prediction"]
    outs=[o for o in observations if o["observation_type"]=="actual-outcome"]
    print(f"\n[PREDICTIONS={len(preds)} OUTCOMES={len(outs)}]")
    print("="*60); print("Validation complete.")
    return 0 if not errors else 1

if __name__=="__main__": sys.exit(main())
