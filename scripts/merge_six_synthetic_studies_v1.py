#!/usr/bin/env python3
"""merge_six_synthetic_studies_v1.py

Merge the six synthetic 2026-kastner-* study packages into the Aberdeen archive masters.
DRY-RUN by default. Pass --commit to write.

Adds ROWS ONLY. No new columns, no new master files, no relocations.
Follows kastner-archive-pipeline invariants:
  - dry-run default; --commit opt-in
  - timestamped UTC backup of every master touched, BEFORE any write
  - csv.QUOTE_ALL on every write
  - row-count parity reported before/after
  - dedup entities/techs by id against existing masters (add only new)
  - link tables (_master_entity_studies, _master_tech_studies) get a row per
    (id, study_id) referenced, new-or-existing, deduped against existing links

Master schemas (verified live 2026-07-14):
  _master_studies.csv        20 cols (16 base + 4 SH: prescience_3y_enum/rationale, prescience_5y_enum/rationale)
  _master_observations.csv   17 cols (12 base + verification_method, collection, thread_tag, section, legacy_obs_id)
  _master_entities.csv        8 cols (NO study_id — link via _master_entity_studies)
  _master_technologies.csv    8 cols (NO study_id — link via _master_tech_studies)
  _master_entity_studies.csv  2 cols (entity_id, study_id)
  _master_tech_studies.csv    2 cols (tech_id, study_id)

Usage:
  python3 merge_six_synthetic_studies_v1.py            # dry-run
  python3 merge_six_synthetic_studies_v1.py --commit   # write
"""
import csv, os, sys, glob, datetime, shutil

ARCHIVE = os.path.expanduser("~/Desktop/Archive/aberdeen-group-archive")
PKG_ROOT = os.path.expanduser("~/Desktop/Archive/ingest_six_output")  # where Pete unpacks the bundle
COMMIT = "--commit" in sys.argv
TS = datetime.datetime.utcnow().strftime("%Y%m%dT%H%M%SZ")

M_STUDIES = os.path.join(ARCHIVE, "_master_studies.csv")
M_OBS     = os.path.join(ARCHIVE, "_master_observations.csv")
M_ENT     = os.path.join(ARCHIVE, "_master_entities.csv")
M_TECH    = os.path.join(ARCHIVE, "_master_technologies.csv")
M_ENTST   = os.path.join(ARCHIVE, "_master_entity_studies.csv")
M_TECHST  = os.path.join(ARCHIVE, "_master_tech_studies.csv")

def read_csv(p):
    with open(p, newline="", encoding="utf-8") as f:
        r = list(csv.reader(f))
    return r[0], r[1:]

def write_csv(p, header, rows):
    with open(p, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f, quoting=csv.QUOTE_ALL)
        w.writerow(header); w.writerows(rows)

def backup(p):
    b = f"{p}.bak_merge_six_{TS}"
    shutil.copy2(p, b)
    return b

def dget(header, row, col, default=""):
    return row[header.index(col)] if col in header else default

# ---- load package data ----
pkg_studies, pkg_obs, pkg_ent, pkg_tech = [], [], [], []
pkg_dirs = sorted(glob.glob(os.path.join(PKG_ROOT, "2026-kastner-*", "data")))
if not pkg_dirs:
    sys.exit(f"No packages found under {PKG_ROOT}/2026-kastner-*/data — unpack the bundle there first.")

for d in pkg_dirs:
    sh, sr = read_csv(os.path.join(d, "studies.csv"))
    pkg_studies.append((sh, sr[0]))
    oh, orr = read_csv(os.path.join(d, "observations.csv"));  pkg_obs.append((oh, orr))
    eh, err = read_csv(os.path.join(d, "entities.csv"));       pkg_ent.append((eh, err))
    th, trr = read_csv(os.path.join(d, "technologies.csv"));   pkg_tech.append((th, trr))

sids = [row[hdr.index("study_id")] for hdr, row in pkg_studies]

# ---- load masters ----
sH, sD = read_csv(M_STUDIES)
oH, oD = read_csv(M_OBS)
eH, eD = read_csv(M_ENT)
tH, tD = read_csv(M_TECH)
esH, esD = read_csv(M_ENTST)
tsH, tsD = read_csv(M_TECHST)

existing_sids   = {r[sH.index("study_id")] for r in sD}
existing_eids   = {r[eH.index("entity_id")] for r in eD}
existing_tids   = {r[tH.index("tech_id")] for r in tD}
existing_es     = {(r[0], r[1]) for r in esD}   # (entity_id, study_id)
existing_ts     = {(r[0], r[1]) for r in tsD}   # (tech_id, study_id)

# ---- guard: no duplicate study_ids ----
dupe = [s for s in sids if s in existing_sids]
if dupe:
    sys.exit(f"ABORT: study_id(s) already in master: {dupe}")

# ---- build new study rows (16 -> 20 cols; pad 4 SH cols) ----
new_study_rows = []
for hdr, row in pkg_studies:
    base = {c: row[hdr.index(c)] for c in hdr}
    out = [base.get(c, "") for c in sH[:16]]  # first 16 align 1:1
    out += ["[DEFERRED]", "SH pending", "[DEFERRED]", "SH pending"]  # SH 3y/5y enums+rationales
    assert len(out) == len(sH), f"study row {len(out)} != {len(sH)}"
    new_study_rows.append(out)

# ---- build new obs rows (12 -> 17 cols) ----
# collection = study subject_domain; verification_method = ingest-extraction; section from source_page
study_domain = {}
for hdr, row in pkg_studies:
    study_domain[row[hdr.index("study_id")]] = row[hdr.index("subject_domain")]

new_obs_rows = []
for oh, orr in pkg_obs:
    for r in orr:
        g = {c: r[oh.index(c)] for c in oh}
        out = [
            g["obs_id"], g["study_id"], g["entity_id"], g["tech_id"], g["observation_type"],
            g["year_observed"], g["metric_name"], g["metric_value"], g["confidence"],
            "ingest-extraction",                 # verification_method
            g["methodology_code"], g["source_page"], g["notes"],
            study_domain.get(g["study_id"], ""), # collection
            "",                                  # thread_tag
            g.get("source_page", ""),            # section (reuse source_page label)
            "",                                  # legacy_obs_id (already canonical)
        ]
        assert len(out) == len(oH), f"obs row {len(out)} != {len(oH)}"
        new_obs_rows.append(out)

# ---- build new entity rows (dedup by id; 9->8, drop study_id) + link rows ----
new_ent_rows, new_es_rows = [], []
seen_new_e = set()
for eh, err in pkg_ent:
    for r in err:
        g = {c: r[eh.index(c)] for c in eh}
        eid = g["entity_id"]; sid = g["study_id"]
        if eid not in existing_eids and eid not in seen_new_e:
            new_ent_rows.append([g["entity_id"], g["entity_name"], g["entity_type"], g["sector"],
                                 g["status"], g["successor"], g["years_active"], g["notes"]])
            seen_new_e.add(eid)
        if (eid, sid) not in existing_es:
            new_es_rows.append([eid, sid]); existing_es.add((eid, sid))

# ---- build new tech rows (dedup) + link rows ----
new_tech_rows, new_ts_rows = [], []
seen_new_t = set()
for th, trr in pkg_tech:
    for r in trr:
        g = {c: r[th.index(c)] for c in th}
        tid = g["tech_id"]; sid = g["study_id"]
        if tid not in existing_tids and tid not in seen_new_t:
            new_tech_rows.append([g["tech_id"], g["tech_name"], g["category"], g["vendor"],
                                  g["era"], g["lifecycle_at_study"], g["lifecycle_current"], g["notes"]])
            seen_new_t.add(tid)
        if (tid, sid) not in existing_ts:
            new_ts_rows.append([tid, sid]); existing_ts.add((tid, sid))

# ---- report ----
print(f"{'COMMIT' if COMMIT else 'DRY-RUN'} — merge six synthetic studies  ({TS})")
print(f"  studies:       {len(sD):>6} -> {len(sD)+len(new_study_rows):>6}  (+{len(new_study_rows)})")
print(f"  observations:  {len(oD):>6} -> {len(oD)+len(new_obs_rows):>6}  (+{len(new_obs_rows)})")
print(f"  entities:      {len(eD):>6} -> {len(eD)+len(new_ent_rows):>6}  (+{len(new_ent_rows)} new; rest already exist)")
print(f"  technologies:  {len(tD):>6} -> {len(tD)+len(new_tech_rows):>6}  (+{len(new_tech_rows)} new)")
print(f"  entity_studies:{len(esD):>6} -> {len(esD)+len(new_es_rows):>6}  (+{len(new_es_rows)} links)")
print(f"  tech_studies:  {len(tsD):>6} -> {len(tsD)+len(new_ts_rows):>6}  (+{len(new_ts_rows)} links)")
print(f"  new study_ids: {', '.join(sids)}")

if not COMMIT:
    print("\nDRY-RUN only — no files written. Re-run with --commit after review.")
    sys.exit(0)

# ---- commit: backup then append ----
print("\nBacking up + writing...")
for p, H, D, NEW in [
    (M_STUDIES, sH, sD, new_study_rows),
    (M_OBS,     oH, oD, new_obs_rows),
    (M_ENT,     eH, eD, new_ent_rows),
    (M_TECH,    tH, tD, new_tech_rows),
    (M_ENTST,   esH, esD, new_es_rows),
    (M_TECHST,  tsH, tsD, new_ts_rows),
]:
    b = backup(p)
    write_csv(p, H, D + NEW)
    print(f"  {os.path.basename(p)}: backup {os.path.basename(b)}; wrote {len(D)+len(NEW)} rows")

# parity re-read
_, sD2 = read_csv(M_STUDIES); _, oD2 = read_csv(M_OBS)
assert len(sD2) == len(sD)+len(new_study_rows), "studies parity fail"
assert len(oD2) == len(oD)+len(new_obs_rows), "obs parity fail"
print("\nCOMMIT complete. Parity checks passed.")
print("Next: Phase 1+2 rebuild, then Pass C v7 on the new obs.")
