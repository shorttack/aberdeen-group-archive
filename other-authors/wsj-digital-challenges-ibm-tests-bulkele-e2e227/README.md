# WSJ — Digital Challenges Tests by IBM Of Firms' Midrange Computers (Bulkeley, 17-Jun-1988)

| Field | Value |
|-------|-------|
| Author | William M. Bulkeley — The Wall Street Journal |
| Date | 1988-06-17 |
| Type | newspaper-feature |
| Domain | vendor-benchmark-credibility-disputes |
| License | CC-BY-4.0 |

## Abstract

The Wall Street Journal Friday June 17, 1988 page 32 (Media and Marketing section) feature by William M. Bulkeley reporting on the public dispute between Digital Equipment Corporation and IBM over midrange-computer performance benchmarks. Article covers: (a) IBM's 1987 publication of RAMP-C tests showing IBM AS/400 surpassing DEC VAX; (b) Kenneth MacMorran (IBM midrange systems performance evaluation center manager) defending the tests; (c) DEC's H. Neal Houtz (director of competitive strategies) sending 'truth squads' to analysts and reporters in advance of IBM's expected Silverlake (AS/400) announcement; (d) DEC's specific complaint that IBM set up VAX with communications lines '1% as fast as IBM's lines' and used a network 10x slower than DEC's typical customer environment; (e) IBM's refusal to release RAMP-C source for independent audit. Includes Aberdeen Group consultant John Logan calling RAMP-C 'one of the cheapest tricks IBM could have pulled' because 'a benchmark should be something that is widely circulated and can be duplicated and verified.' George Weiss of Gartner Group adds: 'It indicates a degree of desperation in this marketplace.' Article notes IBM-Digital combined accounted for ~43% of $29.8B 1987 midrange sales. Also reports an unrelated J. Walter Thompson advertising win for the Del Taco Naugles fast-food chain. Article appears 5 months before Aberdeen Group's December 1988 founding press advisory naming Logan as co-founder/Chairman.

## Data Tables

| Table | Rows |
|-------|------|
| studies.csv | 1 |
| entities.csv | 11 |
| technologies.csv | 4 |
| observations.csv | 11 |
| codes.csv | 37 |

## Load with Python

```python
import pandas as pd
studies = pd.read_csv('data/studies.csv')
observations = pd.read_csv('data/observations.csv')
```

## Validate

```bash
frictionless validate datapackage.json
```

## Citation

William M. Bulkeley — The Wall Street Journal (1988). WSJ — Digital Challenges Tests by IBM Of Firms' Midrange Computers (Bulkeley, 17-Jun-1988).
Archived in Kastner Research Archive. DOI: [pending]

## Methodology

journalistic-reporting
