# Claude Fable 5.1 — Lane C Fixture Score

**Fixture:** `DB_LONGITUDINAL_DOSSIER_v2.md`  
**Model:** Claude Fable 5.1  
**Run date:** 2026-09-07  
**Prompt:** identical locked Workload 4 narrative prompt

## Mechanical score

| Check | Result | Detail |
|---|:---:|---|
| Narrative length | **PASS** | 3,363 words; required 2,000–3,500 |
| `---SIDECAR---` separator | **PASS** | Present exactly once |
| YAML parse | **PASS** | Valid YAML |
| Required sidecar keys | **PASS** | All seven required keys present |
| Anchor coverage at run threshold | **PASS** | 0.7255; threshold 0.50 |
| Anchor coverage at original aspirational threshold | **FAIL** | 0.7255; original reference 0.90 |
| Strict result under the executed bakeoff rules | **PASS** | First contestant to pass all executed mechanical checks |

## Factual spot-check

Ten representative claim clusters were checked against the dossier:

1. Alias-consolidated vendor counts.
2. 1993–1997 observation peaks.
3. DebitCredit/TPC lineage.
4. Kastner's Stratus ET-1/TP-1 role.
5. DEC Blue Monday numbers and failed share forecast.
6. Open OLTP guide and Korean-edition prescience score.
7. 1993 RDBMS Report Card findings.
8. Jungle vehicle metaphors and prescience values.
9. 1996 tpmC price/performance rows.
10. ITT Hartford observations and Windows 95 prediction/outcome.

All ten clusters were traceable to the dossier. This is a spot-check, not a claim-by-claim audit.

## Qualitative observations for Pete

- Strong opening thesis: measurement and the stopwatch as the organizing device.
- Better handling of the word “decade” than several original contestants: it identifies the operative span as roughly 1985–1996 rather than treating the full 1970–2005 evidence window as one decade.
- Correctly distinguishes Kastner's personal actions from Aberdeen's institutional actions in most passages.
- Includes explicit reckoning on DEC share, Ingres, and the limits of benchmark arithmetic.
- The close is thematically coherent and stronger than several original candidates, though “the next eight chapters” is a structural assertion not established by the dossier.
- Some first-person scene-setting (“the paper landed on my desk as a weapon”) is literary reconstruction rather than a directly documented fact; Pete should judge whether that is acceptable memoir voice.

## Comparison with the original five

Claude Fable 5.1 is the only contestant that passed all mechanical checks under the executed 0.50 coverage threshold. That does not determine its blind narrative rank; Pete's voice and factual-fidelity judgment remains controlling.

## Pete's qualitative comments

- "Obvious Fable AI = That is the thesis of this book, and I want to state it before the evidence rather than after:"
- "Not Pete's voice 'I want to be honest about'"
- "Not Pete's voice 'Here is the reckoning, and I would rather put it early than bury it.'"
- "Misreading DEC vs Tandem 'I told them DEC's debit-credit cost per transaction was less than one-third of an IBM mainframe's and about twice Tandem's'"
- "Not Pete's voice 'I want to be precise about the nature of the error, because it recurs.'"
- "Why does Fable think it is writing a 3,500 word 'book?'"
- "Fable goes out of its way to weave available evidence into the story."

## Follow-up on “the next eight chapters”

Asked to outline the nine chapters it had in mind, Fable produced a nine-part structure by splitting the dossier's RDBMS core and OLTP/benchmark material into additional chapters. It then stated:

> The dossier explicitly supplies six chapter sections (one labeled "Chapter 1–2," plus OLTP/TPC, Hardware, Enterprise apps, ITT Hartford/NCR integration, and the 20% remainder) and references a "Ch. 6" and "Ch. 8" numbering, but the specific nine-chapter split above — particularly separating the RDBMS core into two chapters and OLTP/benchmarks into two — was inferred by me to fit those hints into nine, not stated in the dossier.

**Finding:** the phrase “the next eight chapters” was an invented structural assertion, not a fact supplied by the dossier.
