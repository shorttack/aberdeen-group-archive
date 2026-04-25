# Compaq Vows Support for Himalaya Post-HP (Securities Industry News)

| Field | Value |
|-------|-------|
| Author | Maria Trombly (Securities Industry News) |
| Date | 2002-04-01 |
| Type | trade-press-article |
| Domain | fault-tolerant-computing-financial-services |
| License | CC-BY-4.0 |

## Abstract

Securities Industry News (April 2002) by Maria Trombly. Final results of the HP-Compaq merger vote not yet in but early indications show approval. Compaq working overtime to ease customer concerns about Himalaya integration: 95% of the world's securities transactions go through Compaq Himalaya mainframes (formerly Tandem); 106 of the 120 world stock exchanges. Customers include J.D. Edwards, Prudential Securities, T.D. Waterhouse, and Nasdaq Stock Market. Compaq spokesman Arch Currid: 'We've already assured all of our customers, on every product front, that they can count on our ongoing long-term support.' Counter-warnings from analysts. Lance Travis (AMR Research): 'HP can certainly stand there and say yes... but who knows what will happen?... HP doesn't have anything directly to replace the Himalaya, [but] there is a risk that it will get shoved aside and starved to death. I think it behooves people to start looking for alternatives.' Quote from Peter Kastner of Aberdeen Group on customer impact: top-500 combined customers should continue to see very high levels of sales/support; but customers below that 500 line who were previously highly placed in the smaller company's pecking order may see less support — fewer direct sales force visits, possible loss of onsite sales/support office, account-team reshuffling. Kastner recommends IT organizations at major financial firms hold information-exchange meetings so newly assigned account staff can come up to speed on present and future needs.

## Data Tables

| Table | Rows |
|-------|------|
| studies.csv | 1 |
| entities.csv | 15 |
| technologies.csv | 4 |
| observations.csv | 11 |
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

Maria Trombly (Securities Industry News) (2002). Compaq Vows Support for Himalaya Post-HP (Securities Industry News).
Archived in Kastner Research Archive. DOI: [pending]

## Methodology

news-reporting, expert-interview, customer-interview
