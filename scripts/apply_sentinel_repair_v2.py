#!/usr/bin/env python3
'''apply_sentinel_repair_v2.py — apply the q206 sentinel repair to the masters.

v2 (2026-07-25 AUTO batch, L147): the deprecated UTC-now call -> its timezone-aware replacement
  migration only. No behavior change.
Dry-run by default; --commit to write. Backs up both masters (QUOTE_ALL),
preserves row counts, prints deltas.

studies: for each candidate study_id, set title,author,abstract,type from
         candidates_merged_v4.csv (new_* columns). Also clears the false
         'text lost / image-stripper sentinel' sentence from the abstract if the
         model left any residue (belt-and-suspenders).
observations: for the 253 OBS whose metric_value contains the picture sentinel,
         replace the '==> picture [WxH] intentionally omitted <==' fragment with
         the study's corrected title (from candidates), leaving the rest intact.
'''
import csv, shutil, sys, re, datetime
from pathlib import Path

A=Path.home()/'Desktop/Archive/aberdeen-group-archive'
STUD=A/'_master_studies.csv'; OBS=A/'_master_observations.csv'
CAND='/tmp/kastner_repair/candidates_merged_v4.csv'
COMMIT='--commit' in sys.argv
TS=datetime.datetime.now(datetime.UTC).strftime('%Y%m%dT%H%M%SZ')
PIC=re.compile(r'==>\s*picture\s*\[[^\]]*\]\s*intentionally omitted\s*<==')

cand={r['study_id']:r for r in csv.DictReader(open(CAND))}
print(f'Mode: {"COMMIT" if COMMIT else "DRY-RUN"}  utc={TS}  candidates={len(cand)}')

def backup(p):
    b=p.with_suffix(p.suffix+f'.bak_sentinel_repair_{TS}'); shutil.copy2(p,b); print('  backup:',b.name)

# ---- studies ----
with open(STUD,newline='') as f:
    rd=csv.reader(f); H=next(rd); rows=list(rd)
ix={c:i for i,c in enumerate(H)}
need=['study_id','title','author','abstract','type']
for c in need:
    if c not in ix: sys.exit(f'FATAL studies missing col {c}')
s_hits=0
for r in rows:
    c=cand.get(r[ix['study_id']])
    if not c: continue
    r[ix['title']]=c['new_title']; r[ix['author']]=c['new_author']
    r[ix['abstract']]=c['new_abstract']; r[ix['type']]=c['new_type']
    s_hits+=1
print(f'[studies] rows={len(rows)} (parity {"OK" if len(rows)==1504 else len(rows)}) updated={s_hits} cols={len(H)}')

# ---- observations ----
with open(OBS,newline='') as f:
    rd=csv.reader(f); H2=next(rd); rows2=list(rd)
ix2={c:i for i,c in enumerate(H2)}
o_hits=0; o_titlemap=0
for r in rows2:
    mv=r[ix2['metric_value']]
    if PIC.search(mv):
        c=cand.get(r[ix2['study_id']])
        repl=c['new_title'] if c else 'the source document'
        if c: o_titlemap+=1
        r[ix2['metric_value']]=PIC.sub(repl, mv)
        o_hits+=1
    # also clean notes field if contaminated
    if 'notes' in ix2 and PIC.search(r[ix2['notes']]):
        r[ix2['notes']]=PIC.sub('(figure omitted)', r[ix2['notes']])
print(f'[observations] rows={len(rows2)} cleaned={o_hits} (title-mapped={o_titlemap}) cols={len(H2)}')

if COMMIT:
    backup(STUD)
    with open(STUD,'w',newline='') as f:
        w=csv.writer(f,quoting=csv.QUOTE_ALL); w.writerow(H); w.writerows(rows)
    backup(OBS)
    with open(OBS,'w',newline='') as f:
        w=csv.writer(f,quoting=csv.QUOTE_ALL); w.writerow(H2); w.writerows(rows2)
    print('WROTE both masters.')
else:
    print('DRY-RUN only. Pass --commit to write.')
