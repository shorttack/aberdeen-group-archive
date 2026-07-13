#!/usr/bin/env python3
"""
promote_pptx6_to_masters_v1.py

Promote the six new PPTX-derived study packages into the Aberdeen archive core
masters + reuse caches + join tables. Dry-run by default; --commit to write.

Studies promoted (kastner-author/):
  1994-surfing-the-parallel-architectures--c52d66   (TDMCOLOR)
  1995-midrange-oltp-platform-overview-pyr-44c8e4   (PYRAMI-1)
  1996-aberdeen-mercury-one-2-one-overview-a1c01a   (MERCUR-1)
  1996-oracle-interoffice-workgroup-collab-4e68a3   (ORACLE-1)
  199x-us-insurance-industry-overview-saga-6ce857   (SAGNAI-1)
  199x-y2k-live-dead-wounded-platforms-835ea1       (MSTY2K-1)

Invariants (kastner-archive-pipeline skill): backup before write, csv.QUOTE_ALL,
dry-run default, row-parity reported, forever-archive (append/dedupe, never drop).
"""
import csv, sys, shutil, datetime
from pathlib import Path

REPO = Path.home()/"Desktop"/"Archive"/"aberdeen-group-archive"
KA   = REPO/"kastner-author"
COMMIT = "--commit" in sys.argv
TS = datetime.datetime.utcnow().strftime("%Y%m%dT%H%M%SZ")

STUDIES = [
 "1994-surfing-the-parallel-architectures--c52d66",
 "1995-midrange-oltp-platform-overview-pyr-44c8e4",
 "1996-aberdeen-mercury-one-2-one-overview-a1c01a",
 "1996-oracle-interoffice-workgroup-collab-4e68a3",
 "199x-us-insurance-industry-overview-saga-6ce857",
 "199x-y2k-live-dead-wounded-platforms-835ea1",
]

# master headers (authoritative, from head -1 on live masters)
H_STUDIES = ["study_id","title","author","date","type","subject_domain","methodology","source_file","abstract","license","importance","importance_rationale","relevance","relevance_rationale","prescience","prescience_rationale","prescience_3y_enum","prescience_3y_rationale","prescience_5y_enum","prescience_5y_rationale"]
H_ENT     = ["entity_id","entity_name","entity_type","sector","status","successor","years_active","notes"]
H_TECH    = ["tech_id","tech_name","category","vendor","era","lifecycle_at_study","lifecycle_current","notes"]
H_OBS     = ["obs_id","study_id","entity_id","tech_id","observation_type","year_observed","metric_name","metric_value","confidence","verification_method","methodology_code","source_page","notes","collection","thread_tag","section","legacy_obs_id"]
H_ENT_ST  = ["entity_id","study_id"]
H_TECH_ST = ["tech_id","study_id"]
H_KENT    = ["entity_id","entity_name","entity_type","sector","status","successor","years_active","notes","source_studies"]
H_KTECH   = ["tech_id","tech_name","category","vendor","era","lifecycle_at_study","lifecycle_current","notes","source_studies"]
H_CSTATS  = ["collection","study_id","title","date","author","n_entities","n_technologies","n_observations","n_codes","importance","relevance","prescience"]

def read_rows(p):
    with open(p, newline="", encoding="utf-8") as f:
        r = csv.DictReader(f)
        return r.fieldnames, list(r)

def write_master(path, header, rows):
    bak = path.with_name(path.name + f".bak_promote_pptx6_{TS}")
    if COMMIT:
        shutil.copy2(path, bak)
    with open(path if COMMIT else path.with_suffix(path.suffix+".DRYRUN"), "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f, quoting=csv.QUOTE_ALL)
        w.writerow(header)
        for r in rows:
            w.writerow([r.get(c,"") for c in header])
    return bak

def load_study_csv(sid, name):
    return read_rows(KA/sid/"data"/name)[1]

def main():
    # collect per-study data
    per = {}
    for sid in STUDIES:
        per[sid] = {
            "studies": load_study_csv(sid,"studies.csv"),
            "entities": load_study_csv(sid,"entities.csv"),
            "technologies": load_study_csv(sid,"technologies.csv"),
            "observations": load_study_csv(sid,"observations.csv"),
            "codes": load_study_csv(sid,"codes.csv"),
        }

    report = []
    # ---------- STUDIES ----------
    h, rows = read_rows(REPO/"_master_studies.csv")
    assert h==H_STUDIES, f"studies header drift: {h}"
    existing = {r["study_id"] for r in rows}
    added=0
    for sid in STUDIES:
        srow = per[sid]["studies"][0]
        if srow["study_id"] in existing:
            continue
        nr = {c:"" for c in H_STUDIES}
        for c in srow: 
            if c in nr: nr[c]=srow[c]
        # SH enums deferred -> leave empty
        rows.append(nr); added+=1
    report.append(("_master_studies.csv", len(rows)-added, len(rows), added))
    write_master(REPO/"_master_studies.csv", H_STUDIES, rows)

    # ---------- ENTITIES (dedupe by entity_id) ----------
    h, rows = read_rows(REPO/"_master_entities.csv")
    assert h==H_ENT
    seen = {r["entity_id"] for r in rows}
    added=0
    for sid in STUDIES:
        for e in per[sid]["entities"]:
            if e["entity_id"] in seen: continue
            seen.add(e["entity_id"])
            rows.append({c:e.get(c,"") for c in H_ENT}); added+=1
    report.append(("_master_entities.csv", len(rows)-added, len(rows), added))
    write_master(REPO/"_master_entities.csv", H_ENT, rows)

    # ---------- TECHNOLOGIES (dedupe by tech_id) ----------
    h, rows = read_rows(REPO/"_master_technologies.csv")
    assert h==H_TECH
    seen = {r["tech_id"] for r in rows}
    added=0
    for sid in STUDIES:
        for t in per[sid]["technologies"]:
            if t["tech_id"] in seen: continue
            seen.add(t["tech_id"])
            rows.append({c:t.get(c,"") for c in H_TECH}); added+=1
    report.append(("_master_technologies.csv", len(rows)-added, len(rows), added))
    write_master(REPO/"_master_technologies.csv", H_TECH, rows)

    # ---------- OBSERVATIONS (append; map to 17-col superset) ----------
    h, rows = read_rows(REPO/"_master_observations.csv")
    assert h==H_OBS
    seen = {r["obs_id"] for r in rows}
    added=0
    for sid in STUDIES:
        coll = per[sid]["studies"][0].get("type","")
        for o in per[sid]["observations"]:
            if o["obs_id"] in seen: continue
            seen.add(o["obs_id"])
            nr = {c:"" for c in H_OBS}
            for c in o:
                if c in nr: nr[c]=o[c]
            nr["verification_method"]="ingest-extraction"
            nr["collection"]=coll
            nr["thread_tag"]=""
            nr["section"]=o.get("source_page","")
            nr["legacy_obs_id"]=""
            rows.append(nr); added+=1
    report.append(("_master_observations.csv", len(rows)-added, len(rows), added))
    write_master(REPO/"_master_observations.csv", H_OBS, rows)

    # ---------- ENTITY_STUDIES join ----------
    h, rows = read_rows(REPO/"_master_entity_studies.csv")
    assert h==H_ENT_ST
    seen = {(r["entity_id"],r["study_id"]) for r in rows}
    added=0
    for sid in STUDIES:
        for e in per[sid]["entities"]:
            key=(e["entity_id"],sid)
            if key in seen: continue
            seen.add(key); rows.append({"entity_id":e["entity_id"],"study_id":sid}); added+=1
    report.append(("_master_entity_studies.csv", len(rows)-added, len(rows), added))
    write_master(REPO/"_master_entity_studies.csv", H_ENT_ST, rows)

    # ---------- TECH_STUDIES join ----------
    h, rows = read_rows(REPO/"_master_tech_studies.csv")
    assert h==H_TECH_ST
    seen = {(r["tech_id"],r["study_id"]) for r in rows}
    added=0
    for sid in STUDIES:
        for t in per[sid]["technologies"]:
            key=(t["tech_id"],sid)
            if key in seen: continue
            seen.add(key); rows.append({"tech_id":t["tech_id"],"study_id":sid}); added+=1
    report.append(("_master_tech_studies.csv", len(rows)-added, len(rows), added))
    write_master(REPO/"_master_tech_studies.csv", H_TECH_ST, rows)

    # ---------- KNOWN ENTITIES cache (dedupe by entity_id; append source_studies) ----------
    h, rows = read_rows(REPO/"_known_entities.csv")
    assert h==H_KENT
    idx = {r["entity_id"]:r for r in rows}
    added=0
    for sid in STUDIES:
        for e in per[sid]["entities"]:
            eid=e["entity_id"]
            if eid in idx:
                ss=idx[eid].get("source_studies","")
                parts=[x for x in ss.split(";") if x]
                if sid not in parts:
                    parts.append(sid); idx[eid]["source_studies"]=";".join(parts)
            else:
                nr={c:"" for c in H_KENT}
                for c in H_ENT:
                    if c in e: nr[c]=e[c]
                nr["source_studies"]=sid
                rows.append(nr); idx[eid]=nr; added+=1
    report.append(("_known_entities.csv", len(rows)-added, len(rows), added))
    write_master(REPO/"_known_entities.csv", H_KENT, rows)

    # ---------- KNOWN TECHNOLOGIES cache ----------
    h, rows = read_rows(REPO/"_known_technologies.csv")
    assert h==H_KTECH
    idx = {r["tech_id"]:r for r in rows}
    added=0
    for sid in STUDIES:
        for t in per[sid]["technologies"]:
            tid=t["tech_id"]
            if tid in idx:
                ss=idx[tid].get("source_studies","")
                parts=[x for x in ss.split(";") if x]
                if sid not in parts:
                    parts.append(sid); idx[tid]["source_studies"]=";".join(parts)
            else:
                nr={c:"" for c in H_KTECH}
                for c in H_TECH:
                    if c in t: nr[c]=t[c]
                nr["source_studies"]=sid
                rows.append(nr); idx[tid]=nr; added+=1
    report.append(("_known_technologies.csv", len(rows)-added, len(rows), added))
    write_master(REPO/"_known_technologies.csv", H_KTECH, rows)

    # ---------- COLLECTION STATS ----------
    h, rows = read_rows(REPO/"_collection_stats.csv")
    assert h==H_CSTATS
    seen = {r["study_id"] for r in rows}
    added=0
    for sid in STUDIES:
        if sid in seen: continue
        s=per[sid]["studies"][0]
        rows.append({
          "collection":s.get("type",""),"study_id":sid,"title":s.get("title",""),
          "date":s.get("date",""),"author":s.get("author",""),
          "n_entities":str(len(per[sid]["entities"])),
          "n_technologies":str(len(per[sid]["technologies"])),
          "n_observations":str(len(per[sid]["observations"])),
          "n_codes":str(len(per[sid]["codes"])),
          "importance":s.get("importance",""),"relevance":s.get("relevance",""),
          "prescience":s.get("prescience",""),
        }); added+=1
    report.append(("_collection_stats.csv", len(rows)-added, len(rows), added))
    write_master(REPO/"_collection_stats.csv", H_CSTATS, rows)

    print(f"MODE: {'COMMIT' if COMMIT else 'DRY-RUN'}  (stamp {TS})")
    print(f"{'file':40s} {'before':>8s} {'after':>8s} {'added':>6s}")
    for name,b,a,add in report:
        print(f"{name:40s} {b:8d} {a:8d} {add:6d}")
    if not COMMIT:
        print("\nDRY-RUN: wrote *.DRYRUN preview files, live masters untouched. Pass --commit to write.")

if __name__=="__main__":
    main()
