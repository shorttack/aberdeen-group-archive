#!/usr/bin/env python3
'''ingest_volume2_ch01_v1.py — append the Volume 2, Chapter 1 memoir study + 3
curated observations to the masters. Dry-run by default; --commit to write.
Hybrid memoir: observations left UNSCORED (empty prescience fields) for a Pass C
run; study prescience verdict computed later via Rule A.
Invariants: backup before write (QUOTE_ALL), row-parity reported, idempotent
(aborts if study_id already present).
'''
import csv, shutil, sys, datetime
from pathlib import Path

A=Path.home()/'Desktop/Archive/aberdeen-group-archive'
STUD=A/'_master_studies.csv'; OBS=A/'_master_observations.csv'
SID='volume-2-ch01-managed-conversation-analyst-relations'
COMMIT='--commit' in sys.argv
TS=datetime.datetime.now(datetime.UTC).strftime('%Y%m%dT%H%M%SZ')

STUDY={
 'study_id':SID,
 'title':'Chapter 1: The Managed Conversation — Analyst Relations and Executive Access in the Golden Age of IT',
 'author':'Peter S. Kastner',
 'date':'2026-07-10',
 'type':'memoir',
 'subject_domain':'memoir/volume-2',
 'methodology':'oral-history',
 'source_file':'Kastner Memoir/volume-2-ch01-managed-conversation-analyst-relations/source/original_text.md',
 'abstract':("Peter S. Kastner's memoir of the analyst-relations (AR) era at Aberdeen Group, tracing AR's evolution "
   'from a 1990s logistics function (Microsoft\'s outsourced Waggoner Edstrom; the Hood Canal briefing) into a '
   'sophisticated discipline of narrative control and competitive intelligence (IBM\'s three-inch clippings folder). '
   'Recounts how accountable executives broke free of AR for candid analyst counsel — Bill Zeitler\'s AS/400 lunch at '
   'Somers, Lew Platt\'s Palo Alto dinners, Charles Wang\'s St. Martin gathering and the Prudential CEO introduction, '
   'Larry Ellison\'s Atherton interview and the Dubai conference ego-trip platform, Greg Joswiak\'s iPod briefing — and '
   'contrasts the controlling AR apparatus with its enabling ideal (NCR\'s Tom Rampenthal on the Asia OLTP tour).'),
 'license':'CC-BY-4.0',
 'importance':'high',
 'importance_rationale':('First-hand account of how vendor analyst-relations functions operated and evolved (1990s-2000s), '
   'documenting the informal executive-access channels across IBM, HP, CA, Apple, Microsoft, Oracle, and NCR that shaped '
   'independent IT research.'),
 'relevance':'high',
 'relevance_rationale':('Documents Kastner\'s direct executive relationships and the institutional dynamics behind Aberdeen\'s '
   'research independence; primary-source context for the vendor longitudinal studies that form the rest of Volume 2.'),
 'prescience':'','prescience_rationale':'',
 'prescience_3y_enum':'','prescience_3y_rationale':'','prescience_5y_enum':'','prescience_5y_rationale':'',
}

OBS_ROWS=[
 {'obs_id':SID+'-OBS-001','study_id':SID,'entity_id':'microsoft','tech_id':'windows-nt',
  'observation_type':'market-prediction','year_observed':'1993',
  'metric_name':'Windows NT on x86 as dominant enterprise platform',
  'metric_value':('In the 1993 Hood Canal fireside conversation with Bill Gates, Kastner judged that Windows NT on x86 '
    'servers would become one of the two dominant enterprise development platforms of the late 1990s-2000s, and that '
    'completing the platform would require a relational database alongside NT — a direction Gates did not yet see, being '
    'focused on defending the desktop. Later published as the 1997 memo "NT: The Emperor Has No Clothes."'),
  'confidence':'high','verification_method':'ingest-extraction','methodology_code':'mc-oh',
  'source_page':'The Early Days: Waggoner Edstrom and the Hood Canal','notes':'Memoir recollection (Volume 2 Ch.1); dated to the 1993 Hood Canal conversation with Bill Gates.',
  'collection':'','thread_tag':'','section':'','legacy_obs_id':''},
 {'obs_id':SID+'-OBS-002','study_id':SID,'entity_id':'microsoft','tech_id':'windows-nt',
  'observation_type':'expert-assessment','year_observed':'1993',
  'metric_name':'Windows NT development methodology critique',
  'metric_value':('At the 1993 Hood Canal briefing, Jim Allchin described the Windows NT project as ~4,000 programmers writing '
    'in C with crude tools and no repository. Kastner assessed this as an architectural problem being solved with headcount, '
    'invoking Brooks\'s Mythical Man-Month ("adding programmers to a late project makes it later") — the basis of the 1997 '
    '"Emperor Has No Clothes" critique.'),
  'confidence':'high','verification_method':'ingest-extraction','methodology_code':'mc-oh',
  'source_page':'The Early Days: Waggoner Edstrom and the Hood Canal','notes':'Memoir recollection; dated to the 1993 Allchin conversation at Hood Canal.',
  'collection':'','thread_tag':'','section':'','legacy_obs_id':''},
 {'obs_id':SID+'-OBS-003','study_id':SID,'entity_id':'apple','tech_id':'ipod',
  'observation_type':'product-assessment','year_observed':'2001',
  'metric_name':'iPod as music experience, not gadget',
  'metric_value':('In the original-iPod analyst briefing with Greg Joswiak, Kastner read the iPod not as a technology category '
    'but as a music experience — a restoration of serious listening lost in the CD era — a framing Joswiak affirmed '
    '("Finally, someone who gets it").'),
  'confidence':'high','verification_method':'ingest-extraction','methodology_code':'mc-oh',
  'source_page':'The Briefing That Said Everything','notes':'Memoir recollection; dated to the original iPod launch (Oct 2001).',
  'collection':'','thread_tag':'','section':'','legacy_obs_id':''},
]

print(f'Mode: {"COMMIT" if COMMIT else "DRY-RUN"}  utc={TS}')

# studies
with open(STUD,newline='') as f: rd=csv.reader(f); SH=next(rd); srows=list(rd)
if SID in {r[0] for r in srows}: sys.exit(f'ABORT: {SID} already in studies master.')
assert list(STUDY.keys())==SH, f'STUDY key order mismatch\n{SH}\n{list(STUDY.keys())}'
print(f'[studies] {len(srows)} -> {len(srows)+1} (cols {len(SH)})')

# observations
with open(OBS,newline='') as f: rd=csv.reader(f); OH=next(rd); orows=list(rd)
assert list(OBS_ROWS[0].keys())==OH, f'OBS key order mismatch\n{OH}\n{list(OBS_ROWS[0].keys())}'
existing_obs={r[0] for r in orows}
new_obs=[o for o in OBS_ROWS if o['obs_id'] not in existing_obs]
print(f'[observations] {len(orows)} -> {len(orows)+len(new_obs)} (+{len(new_obs)}; cols {len(OH)})')
for o in new_obs: print(f'   + {o["obs_id"]}  {o["entity_id"]}/{o["tech_id"]}  yr={o["year_observed"]}  score=<unscored>')

if COMMIT:
    b1=STUD.with_suffix(STUD.suffix+f'.bak_vol2ch01_{TS}'); shutil.copy2(STUD,b1); print('  backup:',b1.name)
    with open(STUD,'w',newline='') as f:
        w=csv.writer(f,quoting=csv.QUOTE_ALL); w.writerow(SH); w.writerows(srows); w.writerow([STUDY[c] for c in SH])
    b2=OBS.with_suffix(OBS.suffix+f'.bak_vol2ch01_{TS}'); shutil.copy2(OBS,b2); print('  backup:',b2.name)
    with open(OBS,'w',newline='') as f:
        w=csv.writer(f,quoting=csv.QUOTE_ALL); w.writerow(OH); w.writerows(orows)
        for o in new_obs: w.writerow([o[c] for c in OH])
    print('WROTE studies + observations.')
else:
    print('DRY-RUN only. Pass --commit to write.')
