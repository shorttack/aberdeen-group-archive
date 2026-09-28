# Workload 4 Bakeoff — Salvaged Pre-filter Report

No model output was regenerated. This report repairs post-processing only.

| Contestant | Narrative words | Length | Sidecar | Coverage | Coverage gate | Strict result |
|---|---:|:---:|---|---:|:---:|:---:|
| cloud | 1900 | FAIL | PASS (valid) | 0.3500 | FAIL | FAIL |
| pplx | 2253 | PASS | FAIL (missing keys: entity_cluster, methodology, prescience_anchors, pub_year_range, study_id, subject_domain) | 0.7714 | PASS | FAIL |
| ollama | 777 | FAIL | FAIL (missing keys: entity_cluster, methodology, prescience_anchors, pub_year_range, study_id, subject_domain, title) | 0.8077 | PASS | FAIL |
| ollama-q36-a3b | 2137 | PASS | FAIL (parse error: while parsing a block collection) | 0.0132 | FAIL | FAIL |
| ollama-q36-mlx | 1984 | FAIL | FAIL (missing keys: entity_cluster, methodology, prescience_anchors, pub_year_range, study_id, subject_domain) | 0.0000 | FAIL | FAIL |

## Interpretation

- The strict pre-filter is preserved. No contestant is promoted merely to make the bakeoff produce a winner.
- The diagnostic blind bundle includes all five narratives so Pete can still rank voice and factual fidelity.
- The blind files intentionally exclude each contestant's sidecar. Sidecar compliance remains visible in the table above.
- Do not open `blind/key.json` until the ranking is written.
