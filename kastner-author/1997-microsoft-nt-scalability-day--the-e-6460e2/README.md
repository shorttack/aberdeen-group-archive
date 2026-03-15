# Microsoft NT Scalability Day: The Emperor Has No Clothes

**Aberdeen Group Impact Brief | May 21, 1997**

## Study Metadata

| Field | Value |
|-------|-------|
| study_id | 1997-microsoft-nt-scalability-day--the-e-6460e2 |
| title | Microsoft NT Scalability Day: The Emperor Has No Clothes |
| author | Peter S. Kastner |
| date | 1997-05-21 |
| type | impact-brief |
| subject_domain | enterprise-server-platforms |
| methodology | industry-analysis, competitive-profiling |
| source_file | 1997 Microsoft NT Scalability Day_ The Emperor Has No Clothes im.pdf |
| license | CC-BY-4.0 |

## Abstract

Peter S. Kastner of Aberdeen Group delivers a pointed critique of Microsoft's Scalability Day event in New York, where Bill Gates declared NT and BackOffice ready for any enterprise. Kastner dissects five benchmark demonstrations as unrealistic or misleading, argues NT remains best suited to departmental (not enterprise) applications, and warns that Microsoft's all-or-nothing platform claims risk opening a 'trust gap' with enterprise customers. He concludes Unix, the AS/400, and even the mainframe legitimately retain the enterprise high-end.

## Document Assessment

| Dimension | Rating | Rationale |
|-----------|--------|-----------|
| Importance | high | One of Aberdeen's most provocative NT analyses; Kastner's 'Emperor Has No Clothes' title became a widely-cited characterization of Microsoft's enterprise marketing overreach in 1997. Documents the benchmark-theater tactics that characterized Microsoft's enterprise push. |
| Relevance | medium | The analytical framework—questioning benchmark realism, calling out hype vs. reality, and distinguishing departmental from enterprise fitness—remains applicable to cloud and AI vendor claims today. |
| Prescience | high | Kastner's assessment that NT would be 'better in 1998' but was not yet enterprise-ready proved accurate: NT's enterprise limitations persisted through Windows 2000 and beyond. His prediction that NT's trust gap with enterprise customers would widen also proved prescient—Unix dominated enterprise computing well into the 2000s and Linux ultimately won the server market. |

## Data Tables

| Table | Rows | Description |
|-------|------|-------------|
| studies.csv | 1 | Study metadata and assessments |
| entities.csv | 9 | Organizations referenced |
| technologies.csv | 8 | Technologies discussed |
| observations.csv | 22 | Extracted analytical observations |
| codes.csv | 21 | Controlled vocabulary |

## Quick Load (Python)

```python
import pandas as pd
obs = pd.read_csv("data/observations.csv")
print(obs.groupby("observation_type").size())
```

## Validation

```bash
frictionless validate datapackage.json
```

## Citation

Peter S. Kastner. (1997). *Microsoft NT Scalability Day: The Emperor Has No Clothes*. Aberdeen Group Impact Brief.
Archived: https://web.archive.org/web/19970604114249/http://www.aberdeen.com:80/secure/impacts/1997/ms/body.htm
License: CC-BY-4.0
