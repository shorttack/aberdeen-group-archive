#!/usr/bin/env python3
"""
run_prescience_calibration_v5_qwen_30obs.py

Pass C v2 calibration gate: score the 30-obs manifest with Qwen 3.5 27B-MLX
(via Ollama) and compare against the existing Batch 1 (Sonar) and Batch 2
(Claude) scores. Batch 3 has no prior scores — Qwen scores are recorded for
inspection only (no kappa).

DOES NOT overwrite v4. Reads:
    Perplexity_Only/calibration_30_obs_v1.csv   (manifest from build script)
    _master_observations.csv                     (claim_text source if manifest col empty)
    _master_prescience_scores.csv                (existing Sonar/Claude scores)

Writes:
    Perplexity_Only/calibration_v5_qwen_scores.csv          (12-col v2 schema)
    Perplexity_Only/calibration_v5_qwen_spool.jsonl         (append-only)
    Perplexity_Only/calibration_report_v5.md                (kappas + go/no-go)

GO/NO-GO GATE: all three kappas >= 0.7 to proceed to full ~24,221-obs rescore.
    - kappa_B1: Qwen vs Sonar on 10 B1 obs
    - kappa_B2: Qwen vs Claude on 10 B2 obs
    - kappa_B1B2_overlap_sanity: Sonar vs Claude on 17-study overlap (reference)
"""

import csv
import hashlib
import json
import os
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

# ----- CONFIG -----
ARCHIVE_ROOT  = Path.home() / "Desktop" / "Archive"
ARCHIVE_MASTERS = ARCHIVE_ROOT / "archive_masters"
PASS_C_V2_DIR = ARCHIVE_ROOT / "pass_c_v2"
PERPLEXITY_ONLY = PASS_C_V2_DIR / "Perplexity_Only"

MANIFEST_CSV = PERPLEXITY_ONLY / "calibration_30_obs_v1.csv"
OBS_MASTER   = ARCHIVE_MASTERS / "_master_observations.csv"
PRESC_MASTER = ARCHIVE_MASTERS / "_master_prescience_scores.csv"

OUT_SCORES   = PERPLEXITY_ONLY / "calibration_v5_qwen_scores.csv"
OUT_SPOOL    = PERPLEXITY_ONLY / "calibration_v5_qwen_spool.jsonl"
OUT_REPORT   = PERPLEXITY_ONLY / "calibration_report_v5.md"

MODEL_NAME    = "qwen3.5:27b-mlx"   # adjust if Ollama tag differs
SCORER_VERSION = "pass_c_v2_calib_v5"
SOURCE_PASS    = "pass_c_v2_calibration"
KAPPA_GATE     = 0.70

# Ollama HTTP endpoint
OLLAMA_URL = "http://localhost:11434/api/generate"

# 12-col v2 schema
SCHEMA = [
    "obs_id", "study_id", "model", "prescience_score", "confidence",
    "rationale", "scored_at", "scorer_version", "source_pass",
    "elapsed_sec", "parse_ok", "prompt_hash",
]

PROMPT_TEMPLATE = """You are a prescience scorer for technology industry observations.

Given a claim made at a known point in time, rate how prescient the claim
turned out to be in light of what actually happened in the subsequent years.

CLAIM (from {year_observed}):
{claim_text}

OBSERVATION TYPE: {observation_type}
STUDY: {study_id}

Score on a 0-100 integer scale:
  0-19   Wrong / contradicted by events
  20-39  Partially wrong, missed key dynamics
  40-59  Mixed / ordinary forecasting
  60-79  Above-average insight, mostly right
  80-100 Highly prescient, ahead of consensus

Respond with ONLY a JSON object on a single line, no prose:
{{"score": <int 0-100>, "confidence": <float 0-1>, "rationale": "<<= 240 chars>"}}
"""

# ----- HELPERS -----
def prompt_hash(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()[:16]

def now_iso():
    return datetime.now(timezone.utc).isoformat(timespec="seconds")

def load_manifest():
    rows = []
    with open(MANIFEST_CSV, newline="", encoding="utf-8") as f:
        for r in csv.DictReader(f):
            rows.append(r)
    return rows

def load_obs_lookup():
    """obs_id -> dict with claim_text, observation_type, year_observed, study_id."""
    lut = {}
    with open(OBS_MASTER, newline="", encoding="utf-8") as f:
        for r in csv.DictReader(f):
            oid = r.get("obs_id") or r.get("observation_id")
            if not oid:
                continue
            lut[oid] = r
    return lut

def load_existing_scores():
    """obs_id -> {model: score_int}."""
    if not PRESC_MASTER.exists():
        return {}
    lut = {}
    with open(PRESC_MASTER, newline="", encoding="utf-8") as f:
        for r in csv.DictReader(f):
            oid = r.get("obs_id")
            model = r.get("model", "")
            try:
                score = int(float(r.get("prescience_score", "")))
            except (TypeError, ValueError):
                continue
            lut.setdefault(oid, {})[model] = score
    return lut

def call_ollama(prompt: str, timeout_s: int = 180) -> tuple[str, float, bool]:
    """Returns (raw_text, elapsed_sec, parse_ok). parse_ok=True if JSON parses."""
    import urllib.request
    payload = json.dumps({
        "model": MODEL_NAME,
        "prompt": prompt,
        "stream": False,
        "options": {"temperature": 0.0, "num_predict": 256},
    }).encode("utf-8")
    req = urllib.request.Request(
        OLLAMA_URL, data=payload, headers={"Content-Type": "application/json"}
    )
    t0 = time.time()
    try:
        with urllib.request.urlopen(req, timeout=timeout_s) as resp:
            body = json.loads(resp.read().decode("utf-8"))
        elapsed = time.time() - t0
        text = body.get("response", "").strip()
        return text, elapsed, True
    except Exception as e:
        return f"ERROR: {e}", time.time() - t0, False

def parse_score(raw: str):
    """Return (score:int|None, confidence:float|None, rationale:str, parse_ok:bool)."""
    raw = raw.strip()
    if raw.startswith("```"):
        raw = raw.strip("`").replace("json", "", 1).strip()
    # find first '{' ... last '}'
    i, j = raw.find("{"), raw.rfind("}")
    if i == -1 or j == -1:
        return None, None, raw[:240], False
    try:
        obj = json.loads(raw[i:j+1])
        s = int(obj.get("score"))
        c = float(obj.get("confidence", 0.0))
        r = str(obj.get("rationale", ""))[:240]
        if 0 <= s <= 100 and 0.0 <= c <= 1.0:
            return s, c, r, True
        return s, c, r, False
    except Exception:
        return None, None, raw[:240], False

# ----- KAPPA (quadratic-weighted, binned) -----
def bin_score(s: int) -> int:
    """Map 0-100 -> 5 ordinal bins matching the prompt rubric."""
    if s < 20:  return 0
    if s < 40:  return 1
    if s < 60:  return 2
    if s < 80:  return 3
    return 4

def quadratic_kappa(pairs):
    """pairs: list of (rater_a_bin, rater_b_bin), bins in 0..4."""
    if not pairs:
        return None
    K = 5
    obs = [[0]*K for _ in range(K)]
    a_hist = [0]*K
    b_hist = [0]*K
    for a, b in pairs:
        obs[a][b] += 1
        a_hist[a] += 1
        b_hist[b] += 1
    N = len(pairs)
    w = [[((i-j)**2) / ((K-1)**2) for j in range(K)] for i in range(K)]
    exp = [[(a_hist[i]*b_hist[j])/N for j in range(K)] for i in range(K)]
    num = sum(w[i][j]*obs[i][j] for i in range(K) for j in range(K))
    den = sum(w[i][j]*exp[i][j] for i in range(K) for j in range(K))
    if den == 0:
        return 1.0 if num == 0 else None
    return 1.0 - num/den

# ----- MAIN -----
def main():
    PERPLEXITY_ONLY.mkdir(parents=True, exist_ok=True)
    manifest = load_manifest()
    obs_lut  = load_obs_lookup()
    existing = load_existing_scores()
    print(f"[v5] manifest={len(manifest)}  obs_master={len(obs_lut)}  existing_scored_obs={len(existing)}")

    # restart-safe: read spool for already-scored obs_ids
    done = set()
    if OUT_SPOOL.exists():
        with open(OUT_SPOOL, encoding="utf-8") as f:
            for line in f:
                try:
                    done.add(json.loads(line)["obs_id"])
                except Exception:
                    pass
        print(f"[v5] resume: {len(done)} already scored in spool")

    new_rows = []
    spool_f = open(OUT_SPOOL, "a", encoding="utf-8")
    try:
        for i, m in enumerate(manifest, 1):
            oid = m["obs_id"]
            if oid in done:
                continue
            obs = obs_lut.get(oid, {})
            claim = m.get("claim_text") or obs.get("claim_text") or obs.get("observation_text") or ""
            otype = m.get("observation_type") or obs.get("observation_type") or ""
            yr    = m.get("year_observed") or obs.get("year_observed") or ""
            sid   = m.get("study_id") or obs.get("study_id") or ""
            if not claim:
                print(f"  [{i:02d}] {oid} SKIP (no claim_text)")
                continue
            prompt = PROMPT_TEMPLATE.format(
                claim_text=claim, observation_type=otype,
                year_observed=yr, study_id=sid,
            )
            ph = prompt_hash(prompt)
            raw, elapsed, ok_http = call_ollama(prompt)
            score, conf, rat, ok_parse = parse_score(raw)
            row = {
                "obs_id": oid,
                "study_id": sid,
                "model": MODEL_NAME,
                "prescience_score": score if score is not None else "",
                "confidence": conf if conf is not None else "",
                "rationale": rat,
                "scored_at": now_iso(),
                "scorer_version": SCORER_VERSION,
                "source_pass": SOURCE_PASS,
                "elapsed_sec": f"{elapsed:.2f}",
                "parse_ok": "true" if (ok_http and ok_parse) else "false",
                "prompt_hash": ph,
            }
            new_rows.append(row)
            spool_f.write(json.dumps(row) + "\n")
            spool_f.flush()
            batch = m.get("batch", "?")
            print(f"  [{i:02d}/{len(manifest)}] B{batch} {oid[:24]:24s} score={score} conf={conf} t={elapsed:.1f}s ok={ok_parse}")
    finally:
        spool_f.close()

    # Merge prior spool rows + new rows -> CSV
    all_rows = []
    if OUT_SPOOL.exists():
        with open(OUT_SPOOL, encoding="utf-8") as f:
            for line in f:
                try:
                    all_rows.append(json.loads(line))
                except Exception:
                    pass
    with open(OUT_SCORES, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=SCHEMA)
        w.writeheader()
        for r in all_rows:
            w.writerow({k: r.get(k, "") for k in SCHEMA})
    print(f"[v5] wrote {OUT_SCORES} ({len(all_rows)} rows)")

    # ----- KAPPAS -----
    qwen_by_oid = {r["obs_id"]: r for r in all_rows
                   if r.get("parse_ok") == "true" and r.get("prescience_score") != ""}

    pairs_b1, pairs_b2 = [], []
    for m in manifest:
        oid = m["obs_id"]
        batch = m.get("batch")
        q = qwen_by_oid.get(oid)
        if not q:
            continue
        q_bin = bin_score(int(q["prescience_score"]))
        prior = existing.get(oid, {})
        if batch == "1":
            sonar = next((v for k, v in prior.items() if "sonar" in k.lower()), None)
            if sonar is not None:
                pairs_b1.append((bin_score(sonar), q_bin))
        elif batch == "2":
            claude = next((v for k, v in prior.items() if "claude" in k.lower()), None)
            if claude is not None:
                pairs_b2.append((bin_score(claude), q_bin))

    # 17-study overlap sanity (Sonar vs Claude) — reference only
    overlap_pairs = []
    for oid, models in existing.items():
        sonar = next((v for k, v in models.items() if "sonar" in k.lower()), None)
        claude = next((v for k, v in models.items() if "claude" in k.lower()), None)
        if sonar is not None and claude is not None:
            overlap_pairs.append((bin_score(sonar), bin_score(claude)))

    k_b1 = quadratic_kappa(pairs_b1)
    k_b2 = quadratic_kappa(pairs_b2)
    k_ov = quadratic_kappa(overlap_pairs)

    def fmt(k):
        return "n/a" if k is None else f"{k:.3f}"

    b1_pass = (k_b1 is not None and k_b1 >= KAPPA_GATE)
    b2_pass = (k_b2 is not None and k_b2 >= KAPPA_GATE)
    go = b1_pass and b2_pass

    report = f"""# Pass C v2 Calibration Report (v5 / Qwen / 30 obs)

Generated: {now_iso()}

## Inputs
- Manifest: `{MANIFEST_CSV}`
- Scorer: `{MODEL_NAME}` via Ollama
- Scorer version: `{SCORER_VERSION}`
- Gate threshold: kappa >= {KAPPA_GATE}

## Coverage
- Manifest rows: {len(manifest)}
- Scored OK by Qwen: {len(qwen_by_oid)}
- B1 pairs (Qwen vs Sonar): {len(pairs_b1)}
- B2 pairs (Qwen vs Claude): {len(pairs_b2)}
- B1xB2 overlap pairs (Sonar vs Claude, reference): {len(overlap_pairs)}

## Quadratic-weighted Cohen's kappa (5 bins)

| Comparison                   | kappa     | n  | pass>={KAPPA_GATE}? |
|------------------------------|-----------|----|--------------------|
| Qwen vs Sonar  (Batch 1)     | {fmt(k_b1):9s} | {len(pairs_b1):2d} | {"YES" if b1_pass else "NO"} |
| Qwen vs Claude (Batch 2)     | {fmt(k_b2):9s} | {len(pairs_b2):2d} | {"YES" if b2_pass else "NO"} |
| Sonar vs Claude (reference)  | {fmt(k_ov):9s} | {len(overlap_pairs):2d} | reference only |

## Decision

**{"GO" if go else "NO-GO"}** for full ~24,221-obs Qwen rescore.

{"Both calibration kappas meet the >= " + str(KAPPA_GATE) + " gate. Proceed to write `run_prescience_pass_c_v6_qwen_full.py`." if go else "At least one kappa below gate. Inspect disagreements before scaling. Review the per-obs scores in `calibration_v5_qwen_scores.csv` and the rationales for the largest bin-distance pairs."}

## Notes
- Batch 3 (10 transcript obs) had no prior scores; Qwen scores are recorded in `calibration_v5_qwen_scores.csv` for spot-checking but contribute no kappa.
- Binning: 0-19 / 20-39 / 40-59 / 60-79 / 80-100 (matches prompt rubric).
"""
    OUT_REPORT.write_text(report, encoding="utf-8")
    print(f"[v5] wrote {OUT_REPORT}")
    print(f"[v5] kappas: B1={fmt(k_b1)}  B2={fmt(k_b2)}  ref={fmt(k_ov)}  decision={'GO' if go else 'NO-GO'}")

if __name__ == "__main__":
    sys.exit(main() or 0)
