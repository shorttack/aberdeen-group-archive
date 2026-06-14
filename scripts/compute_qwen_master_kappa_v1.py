#!/usr/bin/env python3
"""
compute_qwen_master_kappa_v1.py
================================
Compute Qwen-vs-master quadratic-weighted Cohen's kappa using the salvaged
abandoned May 26 Qwen 3.5 27B MLX scores as the candidate, and Sonar / Claude
scores from `_master_prescience_scores.csv` as ground truth.

Inputs (read-only):
  scripts/audit_abandoned_qwen_rows_v1.csv       (2,723 Qwen rows — built by audit v1)
  _master_prescience_scores.csv                  (3,829 master rows, Sonar + Claude)

Outputs (next to this script):
  qwen_master_kappa_report_v1.md                 human-readable report
  qwen_master_kappa_paired_v1.csv                every obs paired Qwen<->master row
  qwen_master_kappa_confusion_sonar_v1.csv       6x6 confusion (incl. 0) Qwen vs Sonar
  qwen_master_kappa_confusion_claude_v1.csv      6x6 confusion (incl. 0) Qwen vs Claude

Methodology:
  - Inner-join on obs_id (one obs may have BOTH a Sonar row AND a Claude row in master;
    each pairing is counted independently in its own kappa computation).
  - Quadratic-weighted Cohen's kappa over the 5 ordinal labels {1,2,3,4,5}.
    Pairs where either side scored 0 (cannot assess) or -1 (pre-filter) are excluded
    from kappa — they're abstention, not disagreement.
  - Reports kappa, n, score histograms, and the 5x5 confusion matrix per (Qwen vs Sonar)
    and (Qwen vs Claude).
  - Bonus: 6x6 matrices including 0 (full disclosure of abstention pattern).

GO gate (after audit-salvaged data):
  kappa(Qwen vs Sonar)  >= 0.70  AND
  kappa(Qwen vs Claude) >= 0.70
=> full Qwen rescore of remaining ~21,500 obs is justified, no further calibration needed.

Run on Mac:
  cd ~/Desktop/Archive/aberdeen-group-archive
  python3 scripts/compute_qwen_master_kappa_v1.py
"""
from __future__ import annotations
import csv
import sys
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path

# ---------- paths ----------
HERE          = Path(__file__).resolve().parent
REPO          = HERE.parent
QWEN_CSV      = HERE / "audit_abandoned_qwen_rows_v1.csv"
MASTER_CSV    = REPO / "_master_prescience_scores.csv"

OUT_REPORT    = HERE / "qwen_master_kappa_report_v1.md"
OUT_PAIRED    = HERE / "qwen_master_kappa_paired_v1.csv"
OUT_CONF_SON  = HERE / "qwen_master_kappa_confusion_sonar_v1.csv"
OUT_CONF_CLD  = HERE / "qwen_master_kappa_confusion_claude_v1.csv"

# Ordinal label set used for kappa (excludes 0 / -1)
KAPPA_LABELS  = [1, 2, 3, 4, 5]
# Display set for confusion matrices (includes 0 for transparency)
DISPLAY_LABELS = [0, 1, 2, 3, 4, 5]

GO_THRESHOLD  = 0.70


def short(p: Path) -> str:
    try:
        return str(p.relative_to(Path.home()))
    except ValueError:
        return str(p)


def read_csv_rows(path: Path) -> list[dict]:
    if not path.exists():
        print(f"ERROR: missing {path}", file=sys.stderr)
        sys.exit(1)
    with path.open(newline="", encoding="utf-8") as fh:
        return list(csv.DictReader(fh))


def parse_score(v: str) -> int | None:
    if v is None:
        return None
    s = v.strip()
    if not s:
        return None
    try:
        n = int(s)
    except ValueError:
        return None
    return n


def quadratic_weighted_kappa(pairs: list[tuple[int, int]], labels: list[int]) -> tuple[float, int, list[list[int]]]:
    """Cohen's quadratic-weighted kappa on ordinal labels.

    pairs : list of (rater_a, rater_b) integer scores, both in `labels`.
    Returns (kappa, n, confusion) where confusion[i][j] counts (a=labels[i], b=labels[j]).
    """
    K = len(labels)
    idx = {lbl: i for i, lbl in enumerate(labels)}
    O = [[0] * K for _ in range(K)]
    for a, b in pairs:
        O[idx[a]][idx[b]] += 1

    n = sum(sum(row) for row in O)
    if n == 0:
        return float("nan"), 0, O

    # quadratic weights: w_ij = (i - j)^2 / (K-1)^2
    W = [[((i - j) ** 2) / ((K - 1) ** 2) for j in range(K)] for i in range(K)]

    row_marg = [sum(O[i]) for i in range(K)]
    col_marg = [sum(O[i][j] for i in range(K)) for j in range(K)]

    # Expected matrix under independence (same total n)
    E = [[(row_marg[i] * col_marg[j]) / n for j in range(K)] for i in range(K)]

    num = sum(W[i][j] * O[i][j] for i in range(K) for j in range(K))
    den = sum(W[i][j] * E[i][j] for i in range(K) for j in range(K))
    if den == 0:
        return float("nan"), n, O
    return 1.0 - (num / den), n, O


def confusion_table(pairs: list[tuple[int, int]], labels: list[int]) -> list[list[int]]:
    K = len(labels)
    idx = {lbl: i for i, lbl in enumerate(labels)}
    M = [[0] * K for _ in range(K)]
    for a, b in pairs:
        if a in idx and b in idx:
            M[idx[a]][idx[b]] += 1
    return M


def write_confusion_csv(path: Path, matrix: list[list[int]], labels: list[int], row_name: str, col_name: str) -> None:
    with path.open("w", newline="", encoding="utf-8") as fh:
        w = csv.writer(fh)
        w.writerow([f"{row_name}\\{col_name}"] + [str(c) for c in labels])
        for i, r in enumerate(labels):
            w.writerow([str(r)] + matrix[i])


def render_matrix_md(matrix: list[list[int]], labels: list[int], row_name: str, col_name: str) -> str:
    head = "| " + f"{row_name} \\ {col_name}" + " | " + " | ".join(str(c) for c in labels) + " | total |"
    sep  = "|" + "|".join(["---"] * (len(labels) + 2)) + "|"
    lines = [head, sep]
    col_totals = [0] * len(labels)
    grand = 0
    for i, r in enumerate(labels):
        row_total = sum(matrix[i])
        grand += row_total
        for j in range(len(labels)):
            col_totals[j] += matrix[i][j]
        lines.append("| " + str(r) + " | " + " | ".join(str(matrix[i][j]) for j in range(len(labels))) + f" | **{row_total}** |")
    lines.append("| **total** | " + " | ".join(f"**{t}**" for t in col_totals) + f" | **{grand}** |")
    return "\n".join(lines)


def main() -> int:
    qwen_rows   = read_csv_rows(QWEN_CSV)
    master_rows = read_csv_rows(MASTER_CSV)
    print(f"[kappa] qwen rows:   {len(qwen_rows)}")
    print(f"[kappa] master rows: {len(master_rows)}")

    # Index Qwen by obs_id (audit file has one Qwen row per obs_id; if multiple, last wins)
    qwen_by_obs: dict[str, dict] = {}
    for r in qwen_rows:
        oid = (r.get("obs_id") or "").strip()
        if oid:
            qwen_by_obs[oid] = r
    print(f"[kappa] unique qwen obs_ids: {len(qwen_by_obs)}")

    # Bucket master rows by model
    master_by_model: dict[str, list[dict]] = defaultdict(list)
    for r in master_rows:
        m = (r.get("model") or "").strip()
        master_by_model[m].append(r)
    print(f"[kappa] master models: { {m: len(v) for m, v in master_by_model.items()} }")

    # ---------- build paired rows ----------
    paired: list[dict] = []
    sonar_pairs: list[tuple[int, int]] = []      # (qwen, sonar) — kappa basis (1-5 both sides)
    claude_pairs: list[tuple[int, int]] = []     # (qwen, claude)
    sonar_pairs_with0: list[tuple[int, int]] = []   # includes 0 for confusion display
    claude_pairs_with0: list[tuple[int, int]] = []

    sonar_qwen_hist  = Counter()
    sonar_other_hist = Counter()
    claude_qwen_hist  = Counter()
    claude_other_hist = Counter()

    for m_row in master_rows:
        oid   = (m_row.get("obs_id") or "").strip()
        model = (m_row.get("model")  or "").strip()
        if not oid or oid not in qwen_by_obs:
            continue
        q_row = qwen_by_obs[oid]
        q_score = parse_score(q_row.get("prescience_score"))
        m_score = parse_score(m_row.get("prescience_score"))
        if q_score is None or m_score is None:
            continue

        paired.append({
            "obs_id":           oid,
            "study_id":         q_row.get("study_id") or m_row.get("study_id") or "",
            "qwen_score":       q_score,
            "qwen_confidence":  q_row.get("confidence", ""),
            "master_model":     model,
            "master_score":     m_score,
            "master_confidence": m_row.get("confidence", ""),
        })

        # confusion (includes 0)
        if q_score in DISPLAY_LABELS and m_score in DISPLAY_LABELS:
            if model == "sonar-reasoning-pro":
                sonar_pairs_with0.append((q_score, m_score))
                sonar_qwen_hist[q_score] += 1
                sonar_other_hist[m_score] += 1
            elif model.startswith("claude"):
                claude_pairs_with0.append((q_score, m_score))
                claude_qwen_hist[q_score] += 1
                claude_other_hist[m_score] += 1

        # kappa basis (both sides in 1..5)
        if q_score in KAPPA_LABELS and m_score in KAPPA_LABELS:
            if model == "sonar-reasoning-pro":
                sonar_pairs.append((q_score, m_score))
            elif model.startswith("claude"):
                claude_pairs.append((q_score, m_score))

    # ---------- write paired csv ----------
    if paired:
        with OUT_PAIRED.open("w", newline="", encoding="utf-8") as fh:
            w = csv.DictWriter(fh, fieldnames=list(paired[0].keys()))
            w.writeheader()
            for r in paired:
                w.writerow(r)
        print(f"[kappa] wrote {short(OUT_PAIRED)} ({len(paired)} pairings)")

    # ---------- compute kappas ----------
    k_sonar,  n_sonar,  cm_sonar_kappa  = quadratic_weighted_kappa(sonar_pairs,  KAPPA_LABELS)
    k_claude, n_claude, cm_claude_kappa = quadratic_weighted_kappa(claude_pairs, KAPPA_LABELS)

    cm_sonar_disp  = confusion_table(sonar_pairs_with0,  DISPLAY_LABELS)
    cm_claude_disp = confusion_table(claude_pairs_with0, DISPLAY_LABELS)

    write_confusion_csv(OUT_CONF_SON, cm_sonar_disp,  DISPLAY_LABELS, "qwen", "sonar")
    write_confusion_csv(OUT_CONF_CLD, cm_claude_disp, DISPLAY_LABELS, "qwen", "claude")
    print(f"[kappa] wrote {short(OUT_CONF_SON)}")
    print(f"[kappa] wrote {short(OUT_CONF_CLD)}")

    # ---------- gate ----------
    gate_sonar  = (k_sonar  >= GO_THRESHOLD) if k_sonar  == k_sonar  else False  # NaN safe
    gate_claude = (k_claude >= GO_THRESHOLD) if k_claude == k_claude else False
    verdict = "GO — full Qwen rescore approved" if (gate_sonar and gate_claude) else "NO-GO — diagnose confusion before rescore"

    # ---------- markdown report ----------
    def fmt(k: float) -> str:
        return f"{k:.4f}" if k == k else "NaN"

    report = f"""# Qwen-vs-Master Quadratic-Weighted Kappa Report

**Computed**: {datetime.now(timezone.utc).isoformat()}
**Inputs**:
- Qwen candidate: `{short(QWEN_CSV)}` ({len(qwen_rows)} rows, salvaged from May 26 abandoned run)
- Master ground truth: `{short(MASTER_CSV)}` ({len(master_rows)} rows)

**Method**: Inner-join on `obs_id`, quadratic-weighted Cohen's kappa on the ordinal label set {{1,2,3,4,5}}. Pairs where either side scored 0 (cannot assess) or -1 (pre-filter) are excluded from kappa; they're abstention, not disagreement. Confusion matrices below DO include 0 for full disclosure.

## Verdict

**{verdict}**

| Comparison | n (1-5 only) | Quadratic-weighted κ | Gate (≥ {GO_THRESHOLD}) |
|---|---|---|---|
| Qwen vs Sonar  | {n_sonar}  | **{fmt(k_sonar)}**  | {'PASS' if gate_sonar  else 'FAIL'} |
| Qwen vs Claude | {n_claude} | **{fmt(k_claude)}** | {'PASS' if gate_claude else 'FAIL'} |

Total Qwen↔master pairings (any score): {len(paired)}

## Score distributions on the overlap

### Qwen vs Sonar overlap (n with both scores = {sum(sonar_qwen_hist.values())})
- Qwen scores  : {dict(sorted(sonar_qwen_hist.items()))}
- Sonar scores : {dict(sorted(sonar_other_hist.items()))}

### Qwen vs Claude overlap (n with both scores = {sum(claude_qwen_hist.values())})
- Qwen scores   : {dict(sorted(claude_qwen_hist.items()))}
- Claude scores : {dict(sorted(claude_other_hist.items()))}

## Confusion matrices (rows = Qwen, cols = master; includes 0 for transparency)

### Qwen vs Sonar

{render_matrix_md(cm_sonar_disp, DISPLAY_LABELS, "qwen", "sonar")}

### Qwen vs Claude

{render_matrix_md(cm_claude_disp, DISPLAY_LABELS, "qwen", "claude")}

## How to read this

- **Diagonal** = exact agreement. Strong diagonal = high κ.
- **Off-by-one** (one cell either side of diagonal) = mostly fine for ordinal scoring.
- **Cross-cluster disagreement** (Qwen 5 vs master 1, or Qwen 1 vs master 5) = serious. Investigate prompt drift.
- **Row 0 / column 0** = abstention asymmetry. If Qwen abstains where master commits, the model may need more context. If master abstains where Qwen commits, Qwen may be over-confident.

## Files

- `{short(OUT_PAIRED)}` — every paired observation (Qwen vs master)
- `{short(OUT_CONF_SON)}` — Qwen vs Sonar 6×6 confusion CSV
- `{short(OUT_CONF_CLD)}` — Qwen vs Claude 6×6 confusion CSV

## Next moves by verdict

- **GO**: Pull obs_ids in `_master_observations.csv` NOT yet scored by Qwen (~24,221 − 2,722 = ~21,500), reuse the canonical Pass C runner against `prescience_score_prompt_v2.md`, append results to a fresh per-study working dir tree. Single-threaded, ~67h estimated.
- **NO-GO**: Inspect the confusion matrices. Look for systematic offsets (Qwen consistently scores 1 low? Qwen confuses 4 and 5?). Decide whether to (a) reprompt Qwen with calibration anchors, (b) refit thresholds, or (c) keep Sonar/Claude as primary scorer and use Qwen only as cheap pre-filter.
"""
    OUT_REPORT.write_text(report, encoding="utf-8")
    print(f"[kappa] wrote {short(OUT_REPORT)}")

    # ---------- stdout summary ----------
    print()
    print("=" * 60)
    print(f"VERDICT: {verdict}")
    print("=" * 60)
    print(f"Qwen vs Sonar:  n={n_sonar:<5}  κ={fmt(k_sonar)}   gate={'PASS' if gate_sonar else 'FAIL'}")
    print(f"Qwen vs Claude: n={n_claude:<5}  κ={fmt(k_claude)}   gate={'PASS' if gate_claude else 'FAIL'}")
    print(f"Total paired:   {len(paired)}")
    print(f"\nSee: {short(OUT_REPORT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
