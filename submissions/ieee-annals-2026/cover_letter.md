# Cover Letter
## Submission to IEEE Annals of the History of Computing

**To:** Prof. Troy Astarte, Editor-in-Chief, IEEE Annals of the History of Computing

**From:** Peter S. Kastner
Independent Researcher / Chief Research Officer, Aberdeen Group (ret.)
pskastner@gmail.com
Savannah, Georgia, USA

**Date:** May 2026

**Submission title:** "The Enterprise AI Arc: Forty-Four Years of AI-Adjacent Product Claims in an Analyst Archive (1980–2024)"

**Submission type:** Feature article (peer-reviewed)

---

Dear Professor Astarte,

I am submitting for consideration a feature article documenting a continuous, machine-readable historical record of enterprise AI product claims spanning 1980 through 2024 — drawn from the Kastner IT Research Archive, a structured corpus of analyst research produced at Aberdeen Group and predecessor organizations between 1979 and 2026.

## Why This Article Belongs in Annals

The history of AI is most often narrated through research milestones: Turing (1950), LISP (1958), MYCIN (1972), the perceptron controversies, and the neural network revival. What is missing from that narrative is the commercial record — the product claims that vendors actually made, the analyst coverage that documented them, and the structured evidence that allows a historian to measure the distance between what was claimed and what was eventually delivered.

This article offers that record. The Kastner IT Research Archive, now publicly available on GitHub (DOI: 10.5281/zenodo.20245076), contains 947 Frictionless Data Packages representing studies by Aberdeen Group analysts from 1988 through 2007, supplemented by earlier and later Kastner-authored material. Every study is packaged as a machine-readable dataset with structured observations, entity records, technology records, and methodology codes. The archive is reproducible: every claim in this article can be verified against the primary CSV tables.

The article's central finding — that Oracle InterOffice (1995) contained a commercial document-summarization feature functionally identical to the headline LLM use case of 2022, twenty-seven years earlier — is not an interpretation. It is an archived product record with a specificity score of 5 (named feature, named product, named workflow) and a predictive distance of 27 years. The same evidentiary discipline applies to every observation in the study.

## Scope and Contribution

The Enterprise AI Arc study is structured as an 11-thread longitudinal decomposition running from XCON (1980) to Oracle 23ai (2024). It synthesizes three completed single-entity longitudinal studies — IBM (1,054 observations, 174 source studies), Oracle (327 observations, 73 source studies), and Intel (562 observations, 102 source studies) — against the 947-study master archive. The scoring method assigns each precursor observation a specificity score (1–5) and a predictive distance in years to the 2022 LLM mainstream baseline, producing a composite that weights early, precise predictions most heavily.

The article makes four historically grounded claims:

1. **The LLM revolution was not a discontinuity.** Every major enterprise LLM capability had a documented commercial precursor in the archive between 1980 and 2005, at a specificity of 3 or higher on the scoring scale.

2. **The 1995–1997 period is the archive's densest AI cluster.** Oracle InterOffice (1995), IBM ViaVoice (1996), IBM MedSpeak (1997), IBM Intelligent Miner (1997), Tandem ORDM (1997), and IBM Deep Blue (1997) form a cohort of commercially documented AI-adjacent claims that predate LLM mainstream by 25–27 years. No prior historian has assembled these claims as a coherent group against a common scoring framework.

3. **The IBM AI pattern is empirically distinctive.** IBM produced the broadest pre-2000 commercial AI portfolio in the archive, yet converted none of its AI research leadership into durable market positions. Deep Blue was decommissioned; Watson Health was sold. The archive's structured refutation records document this pattern across four decades.

4. **The Oracle InterOffice → Oracle 23ai arc is the strongest single-company AI continuity thread in the archive.** The same company named the same functional capability (document intelligence) in 1995 and delivered its production-grade equivalent in 2024 — a 29-year arc under continuous corporate identity. No other company in the archive matches this span.

## Archival Methodology and Reproducibility

The archive is constructed on Frictionless Data Package standards. Every observation carries an `obs_id`, an `entity_id`, a `tech_id`, a confidence rating, a methodology code, and a source reference. The scoring method used in this article (specificity 1–5, predictive distance in years, composite = specificity × distance/5) is explicit, documented in the study package, and verifiable by any reader with access to the GitHub repository.

The dataset is deposited at Zenodo (DOI: 10.5281/zenodo.20245076) and will be additionally uploaded to IEEE DataPort upon acceptance, as encouraged by Annals policy. The primary submission artifact — the Enterprise AI Arc study package (`kastner-author/2026-kastner-enterprise-ai-arc/`) — is publicly available at https://github.com/shorttack/aberdeen-group-archive.

## Relationship to Prior Work

The article is an original synthesis. There is no prior publication of this material in any form, conference or otherwise. The three supporting longitudinal studies (IBM, Oracle, Intel) were completed in May 2026 and are cited as supporting evidence; they have not been submitted elsewhere. A SocArXiv preprint will be posted concurrent with submission, as permitted by IEEE Annals policy, to establish priority and invite community feedback before peer review concludes.

## Suggested Reviewers

The following scholars have been identified as having directly relevant expertise in computing history and/or AI history. I have not discussed this submission with any of them; these are suggestions based on published work.

- **Tom Haigh** (University of Wisconsin-Milwaukee) — history of computing, software history, database systems
- **Marie Hicks** (Illinois Institute of Technology) — history of computing, labor and computing
- **Jeffrey Yost** (Charles Babbage Institute) — business history of computing, software industry
- **Nathan Ensmenger** (Indiana University) — history of programming, computing professions

## Conflict of Interest Statement

I am the sole author and the primary subject of the archive on which this article is based. This is disclosed fully in the article. The archive-as-protagonist framing is a deliberate methodological choice: the article presents the archive's documented record, not my personal recollections, as its primary evidentiary basis. Observations are structured data rows, not memoir claims.

## Word Count Compliance

The manuscript is approximately 6,800 words including abstract, keywords, all body text, bibliography, and author biography — within the 5,000–8,000 word guideline.

## Data Availability

All primary data are openly available:
- Archive repository: https://github.com/shorttack/aberdeen-group-archive
- Zenodo DOI: https://doi.org/10.5281/zenodo.20245076
- Enterprise AI Arc study: `kastner-author/2026-kastner-enterprise-ai-arc/`
- Intel longitudinal: `kastner-author/2026-kastner-intel-longitudinal-776f7e/`
- Oracle longitudinal: `kastner-author/2026-kastner-oracle-longitudinal/`
- IBM longitudinal: `kastner-author/2026-kastner-ibm-longitudinal/`

I would be grateful for the Editorial Board's consideration. I am available for any editorial questions at pskastner@gmail.com.

Respectfully,

**Peter S. Kastner**
Chief Research Officer (ret.), Aberdeen Group, Boston
Co-founder, Aberdeen Group
MIT S.B., S.M.; UC Berkeley M.B.A.
Savannah, Georgia, USA
