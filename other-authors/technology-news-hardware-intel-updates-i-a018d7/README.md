# Intel Updates Itanium 2 Processors

| Field | Value |
|-------|-------|
| Author | Gene J. Koprowski, TechNewsWorld |
| Date | 2004-04-13 |
| Type | news-article |
| Domain | 64-bit-server-processors-itanium |
| License | CC-BY-4.0 |

## Abstract

TechNewsWorld article (Apr 13 2004, Gene J. Koprowski) on Intel's Taipei developer-forum disclosure of two new lower-priced Itanium 2 processors (1.4 GHz and 1.6 GHz, both with 3 MB L3 cache; servers ~28% lower in price and up to 25% faster than prior Itanium 2). Intel's Richard Dracott positions this as merging Itanium and Xeon into common infrastructure. Audi AG cited as early Itanium 2 / HP Integrity adopter for automotive design simulation. Aberdeen chief research analyst Peter Kastner delivers the decisive skeptical read on 64-bit consumer demand: 'There are only about 100,000 Intel Itanium 64-bit machines on the market today, indicating that 64-bit computing will not be truly significant for users nor for software developers like Microsoft until Intel commits more wholeheartedly to the technology.' And the now-famous prediction: 'Very few consumer desktops can take advantage of 64-bit. Intel has to drop the other shoe and deem that the broad, mass market for consumers is ready for 64-bit. I predict that will not be this year.'

## Data Tables

| Table | Rows |
|-------|------|
| studies.csv | 1 |
| entities.csv | 10 |
| technologies.csv | 5 |
| observations.csv | 7 |
| codes.csv | 28 |

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

Gene J. Koprowski, TechNewsWorld (2004). Intel Updates Itanium 2 Processors.
Archived in Kastner Research Archive. DOI: [pending]

## Methodology

product-launch-analysis, analyst-commentary
