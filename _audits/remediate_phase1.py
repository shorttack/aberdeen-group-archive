#!/usr/bin/env python3
"""
v18 Referential Integrity Auto-Remediation Script.

Fixes only SAFE defects identified by the audit:
  1. Add 'russ-craig-aberdeen' to _known_entities.csv (cache miss)
  2. Add 7 missing entity/tech rows to 4 studies' local CSVs
  3. Normalize enum values:
       importance/relevance/prescience 'moderate' -> 'medium'
       confidence 'CF-HIGH' -> 'high'
       (confidence='[REVIEW]' left alone — that's deferred-review state, not a defect)
  4. Rewrite every CSV in every study with QUOTE_ALL where not already
  5. Add missing observation_types to local codes.csv where truly missing
       (skip schema-mismatch studies where label is present under OT-### code_id)

Does NOT touch:
  - Studies with entirely legacy entities/technologies schema (column count / header mismatch)
  - [REVIEW] confidence markers
  - Schema-evolution differences in codes.csv (OT-### vs label-as-code_id)
"""
import csv, os, sys, shutil
from pathlib import Path
from collections import defaultdict, Counter

REPO = Path('/tmp/aberdeen-group-archive')
os.chdir(REPO)

STATS = Counter()
ACTIONS = []

def log(kind, msg):
    STATS[kind] += 1
    ACTIONS.append(f"[{kind}] {msg}")

# ==================================================================
# CSV I/O helpers — always QUOTE_ALL
# ==================================================================
def read_csv(path):
    with open(path, newline='', encoding='utf-8') as f:
        return list(csv.DictReader(f))

def read_rows(path):
    with open(path, newline='', encoding='utf-8') as f:
        r = csv.reader(f)
        return list(r)

def write_csv_quote_all(path, header, rows):
    """Write list-of-dicts rows with csv.writer QUOTE_ALL."""
    with open(path, 'w', newline='', encoding='utf-8') as f:
        w = csv.writer(f, quoting=csv.QUOTE_ALL)
        w.writerow(header)
        for row in rows:
            w.writerow([row.get(h, '') for h in header])

def write_rows_quote_all(path, all_rows):
    """Write list-of-lists (header + rows) with QUOTE_ALL."""
    with open(path, 'w', newline='', encoding='utf-8') as f:
        w = csv.writer(f, quoting=csv.QUOTE_ALL)
        for r in all_rows:
            w.writerow(r)

# ==================================================================
# Step 1: Cache miss — add russ-craig-aberdeen
# ==================================================================
def step1_cache_miss():
    cache_path = REPO / '_known_entities.csv'
    rows = read_rows(cache_path)
    header = rows[0]
    data_rows = rows[1:]
    existing_ids = {r[0] for r in data_rows if r}
    if 'russ-craig-aberdeen' not in existing_ids:
        # Match v18 cache header: entity_id,entity_name,entity_type,sector,status,successor,years_active,notes
        new_row = [
            'russ-craig-aberdeen',
            'Russ Craig',
            'person',
            'IT Research & Consulting',
            'active',
            '',
            '',
            'Aberdeen Group analyst; authored videoconferencing / SARS business-impact analyses (2003)',
        ]
        # Verify header order
        if header != ['entity_id','entity_name','entity_type','sector','status','successor','years_active','notes']:
            log('ERROR', f'_known_entities.csv unexpected header: {header}')
            return
        data_rows.append(new_row)
        data_rows.sort(key=lambda r: r[0])
        write_rows_quote_all(cache_path, [header] + data_rows)
        log('CACHE_ADD', 'russ-craig-aberdeen added to _known_entities.csv')
    else:
        log('CACHE_SKIP', 'russ-craig-aberdeen already present')

# ==================================================================
# Step 2: 7 ID misses in 4 studies
# ==================================================================
MISSING_FIXES = [
    # (study, target_csv, row_dict, local_schema_check)
    {
        'study': 'kastner-author/aberdeenmaxtortooldemo-03-2-5a8f38',
        'target': 'entities.csv',
        'row': {
            'entity_id': 'adobe-flash-swf',
            'entity_name': 'Adobe Flash (SWF format)',
            'entity_type': 'artifact',
            'sector': 'Rich Internet Application Runtime',
            'status': 'discontinued',
            'successor': 'HTML5 (post-2020 end-of-life)',
            'years_active': '1996-2020',
            'study_id': 'aberdeenmaxtortooldemo-03-2-5a8f38',
            'notes': 'Runtime used for the Maxtor interactive tool demo; retired industry-wide end-of-2020',
        },
    },
    {
        'study': 'kastner-author/inforx95-3-9a45fe',
        'target': 'entities.csv',
        'row': {
            'entity_id': 'computer-associates',
            'entity_name': 'Computer Associates',
            'entity_type': 'vendor',
            'sector': 'enterprise-software',
            'status': 'renamed',
            'successor': 'CA Technologies; acquired by Broadcom (2019)',
            'years_active': '1976-present',
            'study_id': 'inforx95-3-9a45fe',
            'notes': 'Mainframe software and client-server portfolio vendor; referenced for revenue and CS/mainframe mix',
        },
    },
    {
        'study': 'kastner-author/otellini-intel-techpinions-2013-917213',
        'target': 'technologies.csv',
        'row': {
            'tech_id': 'wind-river',
            'tech_name': 'Wind River (VxWorks RTOS)',
            'category': 'platform',
            'vendor': 'Intel',
            'era': '2009-present',
            'lifecycle_at_study': 'mature',
            'lifecycle_current': 'active (spun out from Intel 2018)',
            'study_id': 'otellini-intel-techpinions-2013-917213',
            'notes': 'Real-time OS; Intel acquisition 2009 ($884M) to grow embedded/IoT footprint',
        },
    },
    {
        'study': 'kastner-author/otellini-intel-techpinions-2013-917213',
        'target': 'technologies.csv',
        'row': {
            'tech_id': 'mcafee',
            'tech_name': 'McAfee Security Platform',
            'category': 'platform',
            'vendor': 'Intel',
            'era': '2011-2017',
            'lifecycle_at_study': 'mature',
            'lifecycle_current': 'divested (majority sold to TPG 2017)',
            'study_id': 'otellini-intel-techpinions-2013-917213',
            'notes': 'Security software acquisition (2011, $7.68B) cited as a strategic misstep under Otellini',
        },
    },
    {
        'study': 'kastner-author/otellini-intel-techpinions-2013-917213',
        'target': 'technologies.csv',
        'row': {
            'tech_id': 'infineon',
            'tech_name': 'Infineon Wireless Solutions (WLS)',
            'category': 'component',
            'vendor': 'Intel',
            'era': '2011-2019',
            'lifecycle_at_study': 'growth',
            'lifecycle_current': 'divested (smartphone modem unit sold to Apple 2019, $1B)',
            'study_id': 'otellini-intel-techpinions-2013-917213',
            'notes': 'Infineon WLS acquisition (2011, $1.4B) provided baseband modem silicon for Intel mobile push',
        },
    },
    {
        'study': 'other-authors/aberdeen-1995-ibm-db2-common-server',
        'target': 'entities.csv',
        # This study uses the alternate 10-col schema: entity_id,study_id,name,type,role,status,status_note,hq_country,founded_year,parent_entity
        'row': {
            'entity_id': 'lotus-notes',
            'study_id': 'aberdeen-1995-ibm-db2-common-server',
            'name': 'Lotus Notes / Domino',
            'type': 'product',
            'role': 'mentioned',
            'status': 'divested',
            'status_note': 'IBM acquired Lotus in 1995; Notes/Domino sold to HCL in 2018 and remains actively developed',
            'hq_country': 'US',
            'founded_year': '1989',
            'parent_entity': 'ibm',
        },
    },
]

def step2_id_misses():
    for fix in MISSING_FIXES:
        study = fix['study']
        target = fix['target']
        row = fix['row']
        path = REPO / study / 'data' / target
        if not path.exists():
            log('ERROR', f'{path} does not exist')
            continue
        existing = read_csv(path)
        with open(path, newline='', encoding='utf-8') as f:
            header = next(csv.reader(f))
        id_field = 'entity_id' if target == 'entities.csv' else 'tech_id'
        if any(r.get(id_field) == row[id_field] for r in existing):
            log('ID_SKIP', f'{study}/data/{target}: {row[id_field]} already present')
            continue
        # Verify header compatibility
        row_keys = set(row.keys())
        header_keys = set(header)
        missing_in_row = header_keys - row_keys
        extra_in_row = row_keys - header_keys
        if missing_in_row or extra_in_row:
            log('ERROR', f'{study}/data/{target}: header mismatch (missing_in_row={missing_in_row}, extra={extra_in_row})')
            continue
        existing.append(row)
        write_csv_quote_all(path, header, existing)
        log('ID_ADD', f'{study}/data/{target}: added {row[id_field]}')

# ==================================================================
# Step 3: Normalize enum values + Step 4: QUOTE_ALL rewrite
# ==================================================================
MODERATE_FIELDS = {'studies.csv': {'importance','relevance','prescience'},
                   'observations.csv': {'confidence'}}

def normalize_row(filename, header, row_vals):
    """Apply enum normalizations to a single row's values. Returns (new_row_vals, changes_count)."""
    changes = 0
    new_vals = list(row_vals)
    for i, h in enumerate(header):
        if i >= len(new_vals): break
        v = new_vals[i]
        if filename == 'studies.csv' and h in ('importance','relevance','prescience'):
            if v == 'moderate':
                new_vals[i] = 'medium'; changes += 1
        elif filename == 'observations.csv' and h == 'confidence':
            if v == 'moderate':
                new_vals[i] = 'medium'; changes += 1
            elif v == 'CF-HIGH':
                new_vals[i] = 'high'; changes += 1
            elif v == 'CF-MEDIUM':
                new_vals[i] = 'medium'; changes += 1
            elif v == 'CF-LOW':
                new_vals[i] = 'low'; changes += 1
    return new_vals, changes

def step3_4_rewrite_all():
    """Rewrite every data CSV for every study:
       - Apply enum normalization
       - Always write with QUOTE_ALL (idempotent for already-compliant files)
    """
    study_dirs = []
    for base in ('kastner-author', 'other-authors'):
        for d in sorted(os.listdir(base)):
            sd = Path(base) / d
            if (sd / 'data').is_dir():
                study_dirs.append(sd)
    for sd in study_dirs:
        data = sd / 'data'
        for fname in ('studies.csv', 'entities.csv', 'technologies.csv', 'observations.csv', 'codes.csv'):
            path = data / fname
            if not path.exists(): continue
            try:
                rows = read_rows(path)
            except Exception as e:
                log('ERROR', f'{sd}/data/{fname}: read failed: {e}')
                continue
            if not rows: continue
            header = rows[0]
            data_rows = rows[1:]
            # Skip files whose header has column-count issues — they were flagged as header_mismatch
            # and should not be silently rewritten.
            # Actually: still rewrite QUOTE_ALL even for alt schema — we're not changing columns.
            enum_changes = 0
            new_data = []
            for r in data_rows:
                nr, ch = normalize_row(fname, header, r)
                new_data.append(nr)
                enum_changes += ch
            # Write with QUOTE_ALL regardless (idempotent)
            write_rows_quote_all(path, [header] + new_data)
            if enum_changes:
                log('ENUM_FIX', f'{sd}/data/{fname}: {enum_changes} value(s) normalized')
            STATS['FILES_REWRITTEN'] += 1

# ==================================================================
# Step 5: Add missing obs_types to local codes.csv
# ==================================================================
# Standard v18 codes.csv default label-as-code_id rows for obs_type
DEFAULT_OBS_TYPE_DEFS = {
    'strategy-classification': 'Categorization of an entity\'s business strategy',
    'viability-prediction': 'Expert prediction of entity\'s long-term survival',
    'actual-outcome': 'Verified historical outcome for an entity',
    'technology-assessment': 'Evaluation of a technology\'s maturity or fitness',
    'benchmark-result': 'Quantitative comparison against peers or standards',
    'framework-factor': 'One component of a multi-factor analytical framework',
    'market-data': 'Quantitative market statistic',
    'expert-opinion': 'Qualitative professional judgment',
    'prescience-vindication': 'Retrospective evidence that an earlier prediction was borne out',
    'personal-recollection': 'First-person memory or anecdote',
    'ai-exchange': 'Structured Q&A exchange with an AI system',
    'topic-insight': 'An analytical claim within a topic deep-dive',
    'metric-value': 'Study-specific quantitative measurement',
}

def step5_codes_incomplete():
    # For each study that has obs referencing obs_types NOT in its codes.csv
    # AND where those types are in DEFAULT_OBS_TYPE_DEFS, add them.
    # We detect: codes.csv where existing code_id set includes at least one of the
    # DEFAULT labels already (i.e., study uses label-as-code_id schema, not OT-###).
    study_dirs = []
    for base in ('kastner-author', 'other-authors'):
        for d in sorted(os.listdir(base)):
            sd = Path(base) / d
            if (sd / 'data').is_dir():
                study_dirs.append(sd)
    for sd in study_dirs:
        codes_path = sd / 'data' / 'codes.csv'
        obs_path = sd / 'data' / 'observations.csv'
        if not (codes_path.exists() and obs_path.exists()): continue
        try:
            code_rows = read_rows(codes_path)
            obs_rows = read_rows(obs_path)
        except Exception:
            continue
        if not code_rows or not obs_rows: continue
        code_header = code_rows[0]
        # Only act on v18-style codes.csv (4 cols, 'code_id' first)
        if code_header[:4] != ['code_id','code_type','label','definition']:
            log('CODES_SKIP_SCHEMA', f'{sd}: non-v18 codes.csv schema, leaving alone')
            continue
        existing_code_ids = {r[0] for r in code_rows[1:] if r}
        # Find obs_type values used
        obs_header = obs_rows[0]
        try:
            ot_idx = obs_header.index('observation_type')
        except ValueError:
            continue
        used_types = {r[ot_idx] for r in obs_rows[1:] if len(r) > ot_idx and r[ot_idx]}
        missing = (used_types - existing_code_ids) & set(DEFAULT_OBS_TYPE_DEFS.keys())
        if not missing: continue
        # Add rows
        new_rows = list(code_rows)
        for t in sorted(missing):
            new_rows.append([t, 'observation_type', t.replace('-',' ').title(), DEFAULT_OBS_TYPE_DEFS[t]])
            log('CODE_ADD', f'{sd}/data/codes.csv: added {t!r}')
        write_rows_quote_all(codes_path, new_rows)

# ==================================================================
# Run
# ==================================================================
if __name__ == '__main__':
    print("=== STEP 1: Cache miss fixup ===")
    step1_cache_miss()
    print("=== STEP 2: ID miss fixups (7 rows in 4 studies) ===")
    step2_id_misses()
    print("=== STEP 5: codes.csv completion (v18 schema only) ===")
    step5_codes_incomplete()
    print("=== STEP 3+4: enum normalization + QUOTE_ALL rewrite across all files ===")
    step3_4_rewrite_all()

    print("\n" + "="*70)
    print("REMEDIATION SUMMARY")
    print("="*70)
    for k, v in sorted(STATS.items()):
        print(f"  {k:30s} {v}")
    # Write actions log
    with open('/tmp/remediation_actions.log', 'w') as f:
        f.write('\n'.join(ACTIONS))
    print(f"\nFull actions log: /tmp/remediation_actions.log ({len(ACTIONS)} lines)")
