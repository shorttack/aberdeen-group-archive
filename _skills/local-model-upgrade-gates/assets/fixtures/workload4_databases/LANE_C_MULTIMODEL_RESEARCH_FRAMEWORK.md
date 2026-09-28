# Lane C Multi-Model Research Framework

## Purpose

Use multiple models to assemble, challenge, and organize a longitudinal-study corpus, then give Claude Fable 5.1 one adjudicated writer packet for a single narrative pass.

The framework separates four jobs that the first bakeoff incorrectly combined:

1. Finding and counting evidence.
2. Interpreting evidence from different analytical perspectives.
3. Adjudicating conflicts and gaps.
4. Writing in Pete Kastner's voice.

Fable does job 4. It should not be asked to discover the book structure, invent missing transitions, decide which facts are authoritative, or manufacture a sidecar while writing.

## Governing principles

- **Many models research; one model writes.** Model diversity belongs upstream, where disagreement is useful.
- **SQL owns quantitative truth.** Counts, timelines, study inventories, aliases, and prescience values come from DuckDB or masters, not model recall.
- **A claims ledger is the contract.** Every usable claim has an identifier, source, date, evidence text, confidence, and narrative purpose.
- **Models contribute, not vote.** Minority insights and counterevidence survive if sourced. Consensus is not a substitute for evidence.
- **Pete adjudicates biography and voice.** Pete-supplied facts remain authoritative but are labeled as Pete context when not archive-backed.
- **The writer receives no unresolved contradictions.** Conflicting claims must be resolved, qualified, or explicitly marked as open before Fable sees them.
- **Narrative and mechanics are separate.** Citations, sidecars, schema checks, and anchor coverage run after the prose pass.

## The eight research passes

### Pass 0: Scope, thesis, and exclusions

**Owner:** Pete plus orchestrator  
**Model:** none required  
**Output:** `<TOPIC>_SCOPE_v1.md`

Lock:

- Research question.
- Time window.
- Included entity and technology clusters.
- Explicit exclusions.
- Candidate thesis statements.
- Proposed chapter or section structure.
- Which claims are period-primary, synthetic-secondary, Pete-context, or externally verified.

This is where the Databases study should have stated that 1970–2005 is the evidence window, not "the decade." Fable must never infer a nine-chapter book structure from section-number hints.

**Pete gate:** approve scope and provisional thesis before corpus extraction.

### Pass 1: Deterministic archive extraction

**Owner:** DuckDB/SQL  
**Model:** none  
**Output:** `<TOPIC>_EVIDENCE_LEDGER_v1.csv` plus `<TOPIC>_DOSSIER_v1.md`

Use read-only SQL for:

- Alias-resolved entity and technology totals.
- Studies and observations by year and five-year bucket.
- Study inventory by proposed section.
- Verbatim representative observations.
- Pete-authored study markers.
- Prescience enum, mean, maximum, and count.
- Primary versus synthetic source classification.
- Missing or under-tagged evidence.

Reuse existing `entity_alias_map_v1_<cluster>_only.csv` files. Do not silently merge `KEEP_SEPARATE` rows.

The evidence ledger should carry:

```text
claim_id
section_id
claim_text
evidence_quote
study_id
obs_id
pub_year
source_class
author_role
prescience_value
confidence
contradiction_group
notes
```

The ledger, not prose, becomes the shared substrate for every later pass.

### Pass 2: Semantic recall and gap discovery

**Owner:** `kw search` and `kw ask`  
**Models:** bge-m3 retrieval; Qwen 3.6 MLX synthesis where needed  
**Output:** `<TOPIC>_SEMANTIC_GAPS_v1.md`

Ask questions designed to find evidence the SQL taxonomy missed:

- Which studies express the thesis without using the expected entity tag?
- Which studies contradict the proposed chronology?
- Which Pete-authored studies contain first-person context or signature phrases?
- Which later studies describe the actual outcome of an earlier prediction?
- Which relevant technologies ride inside platform or application studies rather than database tags?

Run exact counts through SQL first. Use `kw ask` only for interpretive retrieval.

Every new candidate from this pass must be resolved back to a real `study_id` or `obs_id` before entering the ledger.

### Pass 3: Historical chronology and causal arc

**Owner:** Ollama Qwen 3.6 35B MLX  
**Output:** `<TOPIC>_CHRONOLOGY_MEMO_q36mlx_v1.md`

Qwen 3.6 MLX ranked first in Pete's blind narrative bakeoff. Use it upstream to propose:

- Ten to twenty turning points.
- Causal links between technology, vendor economics, customer buying, and outcomes.
- Candidate chapter boundaries.
- Which forecasts were early, right, wrong, or merely descriptive.
- Where the evidence changes direction.

Required format:

```text
turning_point_id
date
one_sentence_event
supporting_claim_ids
causal_interpretation
counterevidence_claim_ids
confidence
```

It may interpret. It may not add facts not already in the ledger.

### Pass 4: Competing strategy and technology lenses

Run these passes independently. Do not show one model another model's memo.

#### Pass 4A: Vendor and market-structure lens

**Model:** Ollama Qwen 3.6 35B A3B  
**Output:** `<TOPIC>_MARKET_MEMO_q36a3b_v1.md`

Ask:

- Why did technically strong vendors lose?
- Which platform economics, sales channels, installed bases, or application dependencies decided outcomes?
- What did customers actually choose, and what had already been chosen for them?
- Where does Pete's analysis confuse technical merit with commercial survival?

#### Pass 4B: Broad evidence-coverage lens

**Model:** PPLX Hybrid Qwen 3.6 35B, optional when the UI workflow is worth the friction  
**Output:** `<TOPIC>_COVERAGE_MEMO_pplx_v1.md`

The bakeoff showed strong research coverage but obvious AI prose. Use PPLX as a gap finder, not the writer:

- Missing vendors, studies, and chapter threads.
- Facts supported by multiple dossier sections.
- Evidence clusters that deserve more weight.
- Claims that appear only in synthetic studies.

If Hybrid still requires manual paste and copy, this pass is optional. Do not impose that workflow on every study.

#### Pass 4C: Contrarian and counterevidence lens

**Model:** Perplexity cloud default or another frontier cloud model  
**Output:** `<TOPIC>_COUNTEREVIDENCE_MEMO_cloud_v1.md`

Ask the model to attack the provisional thesis:

- What evidence does not fit?
- Which claims are hindsight reconstruction?
- Which conclusions depend on one source?
- Where are vendor-funded studies being treated as independent analysis?
- Which chronology or causality claims overreach the data?
- What would a skeptical contemporary have said?

This pass should produce objections tied to claim IDs, not an alternative narrative.

### Pass 5: Outcome and prescience verification

**Owner:** deterministic prescience tables plus grounded scoring where required  
**Models:** Sonar/grounded Pass C only when an outcome is not already established  
**Output:** `<TOPIC>_OUTCOME_AUDIT_v1.md`

For each dated prediction:

- Prediction text and date.
- Actual outcome.
- Evaluation horizon.
- Existing prescience score and provenance.
- Pete-authored rebuttal or Path-B note.
- Whether the narrative may call it right, wrong, mixed, or unresolved.

Do not use a frozen local model to invent historical outcomes. The archive's scored evidence, grounded Pass C, and Pete's rebuttal layer control.

### Pass 6: Pete context and voice packet

**Owner:** Pete  
**Model:** optional extraction assistant, never final authority  
**Output:** `<TOPIC>_PETE_PACKET_v1.md`

Pete adds:

- Private engagements and personal relationships.
- What he knew at the time versus learned later.
- Correct I/we attribution.
- Opinions he still holds.
- Calls he wants to own or reject.
- Terms and phrases he would actually use.
- Voice anti-patterns.

The Databases voice packet should explicitly prohibit:

- "That is the thesis of this book..."
- "I want to be honest about..."
- "Here is the reckoning..."
- "I want to be precise about the nature of the error..."
- Invented book or chapter structure.
- Unverified first-person scene setting such as a paper "landing on my desk."
- Incorrect benchmark comparisons, especially directionality such as DEC being "about twice Tandem's" cost per transaction.

It should also reinforce:

- Correct Aberdeen "we" versus personal "I."
- Plain declarative language.
- Strong argument without announcing the argument mechanically.
- Concrete numbers over literary throat-clearing.
- No generic AI confession formula.

**Pete gate:** approve this packet and supply corrections before corpus fusion.

### Pass 7: Corpus fusion and adjudication

**Owner:** orchestrator plus Qwen 3.6 MLX as a structured assistant  
**Output:** `<TOPIC>_DOSSIER_v2.md`, `<TOPIC>_CLAIMS_FINAL.csv`, and `<TOPIC>_WRITER_PACKET_v1.md`

This pass does not write narrative. It merges the earlier products into one authoritative writer packet.

For each claim:

- Keep only traceable evidence.
- Resolve duplicates.
- Attach counterevidence.
- Mark vendor-funded or synthetic sources.
- Resolve I/we attribution.
- State whether the claim is permitted, qualified, or prohibited.
- Flag any conflict Pete must decide.

The writer packet should contain:

1. Approved thesis.
2. Approved section outline.
3. Chronological turning points.
4. Final claims ledger, grouped by section.
5. Verbatim quotations worth using.
6. Data anchors.
7. What Pete got right and wrong.
8. Counterevidence and caveats.
9. Archive gaps.
10. Voice packet and prohibited phrases.
11. Citation identifiers.
12. A short "do not infer" list.

**Pete gate:** approve the writer packet. At this point the research corpus is frozen.

## The Fable writing pass

**Model:** Claude Fable 5.1  
**Input:** `<TOPIC>_WRITER_PACKET_v1.md` only  
**Output:** `<TOPIC>_NARRATIVE_FABLE_v1.md`

Fable receives no open research task. Its instructions are:

- Write the approved structure once.
- Use only approved claims.
- Preserve I/we attribution.
- Do not announce the thesis with stock AI phrasing.
- Do not invent a book structure, chapter count, memory, or scene.
- Do not generate YAML.
- Use `[claim-<id>]` or `[study-<id>]` markers, but do not manage final citation numbering.
- Leave a visible gap rather than bridge it with invention.

The target should be the full study length Pete wants, not an arbitrary 3,500-word cap. Fable's one-pass cost is justified only after the writer packet is complete.

## Post-writing passes

### Pass 8A: Deterministic citation and sidecar build

Generate:

- Unicode superscript citations and end citations.
- Sidecar YAML from the approved ledger.
- Claim-to-source coverage report.
- List of uncited factual sentences.

This is code, not model work.

### Pass 8B: Factual audit

**Models:** cloud counterevidence model plus Qwen 3.6 MLX, independently  
**Output:** `<TOPIC>_FACT_AUDIT_v1.md`

Audit each factual sentence against the final claims ledger. Models identify possible mismatches; deterministic lookup establishes the result.

### Pass 8C: Pete voice review

Pete reviews:

- Voice authenticity.
- I/we errors.
- AI diction.
- Misread benchmarks.
- Invented structure.
- Weak opening or close.
- Claims needing nuance.

Edits should be surgical. Do not ask a second model to rewrite the entire narrative unless the first pass fails fundamentally.

## Recommended model allocation

| Job | Default |
|---|---|
| Quantitative extraction | DuckDB/SQL |
| Semantic retrieval | bge-m3 plus `kw search`; Qwen 3.6 MLX for synthesis |
| Chronology and causal arc | Ollama Qwen 3.6 35B MLX |
| Vendor and market lens | Ollama Qwen 3.6 35B A3B |
| Broad evidence gap scan | PPLX Hybrid, optional |
| Counterevidence | Cloud frontier/default |
| Outcomes/prescience | Existing scores plus grounded Pass C where needed |
| Biography and voice truth | Pete |
| Corpus fusion | Orchestrator plus Qwen 3.6 MLX structured pass |
| Final narrative | Claude Fable 5.1 |
| Citations and sidecar | Deterministic code |

## Minimum viable version

For a smaller study, run:

1. Scope lock.
2. SQL evidence ledger.
3. `kw search` gap pass.
4. Qwen 3.6 MLX chronology memo.
5. Cloud counterevidence memo.
6. Pete packet.
7. Fused writer packet.
8. One Fable narrative pass.
9. Deterministic citations plus Pete review.

Add A3B and PPLX only when the topic is broad enough that extra perspectives justify the work.

## Success criteria

The framework succeeds when:

- Fable introduces no source, chapter, scene, or causal claim absent from the writer packet.
- Pete finds no I/we errors.
- Every factual sentence maps to a claim ID.
- Counterevidence remains visible.
- Vendor-funded and synthetic sources are labeled.
- The narrative sounds like Pete without using stock "voice imitation" phrases.
- A future model can reproduce the research corpus without rerunning the final prose.

