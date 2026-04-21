# SARS Puts an End to Business as Usual in Asia

| Field | Value |
|-------|-------|
| Author | Sumner Lemon, IDG News Service (Computerworld Australia) |
| Date | 2003-04-03 |
| Type | news-article |
| Domain | IT-supply-chain-pandemic-risk |
| License | CC-BY-4.0 |

## Abstract

Computerworld Australia / IDG News Service feature (Apr 3 2003) documenting early SARS impact on the Asian IT industry. Disruption of operations in Hong Kong, Singapore, and China; worries about electronic component supply and pricing. First appearance in Guangdong province (home to much of China's low-cost electronics/IT hardware manufacturing); spread to Hong Kong, Singapore, Vietnam, and lesser numbers to Taiwan, Thailand, Malaysia, Indonesia. Article cites Aberdeen Group analysts 'Russ Craig and Peter Kastner' (jointly) from a report: 'At a minimum, the SARS epidemic will cause schedule slippages and disrupt the aggressive growth plans that global electronics companies have for the affected geographies. Worst case, it could result in major supply-chain disruptions and another downdraft for an already challenged industry.' WHO data: 1,804 worldwide cases / 62 deaths (Apr 1); 182 new cases / 4 deaths in the prior day. Hong Kong had 155 new cases in 24 hours. China: 806 cases / 34 deaths. Intel, Sun Microsystems (SunNetwork 2003 cancelled), AMD, Acer, Gartner's Dion Wiggins all weighed in. Kastner & Craig also quoted on PRC government deception: 'The deceit of the PRC government in hiding what has become a serious global health threat will not be quickly forgotten.'

## Data Tables

| Table | Rows |
|-------|------|
| studies.csv | 1 |
| entities.csv | 12 |
| technologies.csv | 2 |
| observations.csv | 10 |
| codes.csv | 25 |

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

Sumner Lemon, IDG News Service (Computerworld Australia) (2003). SARS Puts an End to Business as Usual in Asia.
Archived in Kastner Research Archive. DOI: [pending]

## Methodology

industry-analysis, analyst-commentary, journalistic
