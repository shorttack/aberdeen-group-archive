# Tech Investor: Instant Messaging goes corporate

| Field | Value |
|-------|-------|
| Author | Eric Hellweg, CNN/Money |
| Date | 2002-11-08 |
| Type | column-opinion |
| Domain | enterprise-collaboration |
| License | CC-BY-4.0 |

## Abstract

CNN/Money Tech Investor column (Nov 8 2002) by Eric Hellweg on the corporate instant-messaging market opportunity. AOL launched Enterprise AIM Services this week; Yahoo! and Microsoft pushing competing corporate IM offerings. Peter Kastner, chief research officer for Aberdeen Research, frames the strategic prize as integration rather than IM itself: 'into the existing corporate communications infrastructure, which includes calendar and e-mail and will eventually include WebEx services.' Michael Gartenberg (Jupiter Research) warns that while AOL/Yahoo/Microsoft consumer-IM dominance is 'some validation for WebEx,' it should also be 'a cause for concern' if the big three decide to subsume the web-conferencing market.

## Data Tables

| Table | Rows |
|-------|------|
| studies.csv | 1 |
| entities.csv | 9 |
| technologies.csv | 3 |
| observations.csv | 6 |
| codes.csv | 26 |

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

Eric Hellweg, CNN/Money (2002). Tech Investor: Instant Messaging goes corporate.
Archived in Kastner Research Archive. DOI: [pending]

## Methodology

analyst-commentary, vendor-commentary
