# Bacon's Shopping List: Is Buying a Consulting Firm the Next Step for Microsoft?

| Field | Value |
|-------|-------|
| Author | Jeff Meisner (Puget Sound Business Journal) |
| Date | 2002-05 |
| Type | trade-press-feature |
| Domain | Microsoft-strategy/IT-consulting/M&A |
| License | CC-BY-4.0 |

## Abstract

Puget Sound Business Journal feature (May 2002) on speculation that Microsoft might spend up to $15 billion of its $38 billion war chest to acquire a major consulting firm like Accenture Ltd. or PricewaterhouseCoopers LLP. Anchors on a Gartner report by Thomas Bittman predicting an acquisition by end-2005. Quotes Aberdeen Group's Peter Kastner: 'It'd be a huge change in direction for Microsoft. I think Wall Street would interpret a move like that as an indication that Microsoft's core business of selling software is failing. I think investors would run for the exits.' Documents Microsoft's recent acquisition spree (Navision $1.3B 2002, Great Plains $1.1B Dec 2000, Visio $1.3B Sept 1999, Hotmail $400M Dec 1997, WebTV $425M April 1997) and the Microsoft-Accenture joint venture Avanade (created March 2000, Accenture took 70% ownership Feb 2002, Microsoft <20%).

## Data Tables

| Table | Rows |
|-------|------|
| studies.csv | 1 |
| entities.csv | 23 |
| technologies.csv | 4 |
| observations.csv | 11 |
| codes.csv | 29 |

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

Jeff Meisner (Puget Sound Business Journal) (2002). Bacon's Shopping List: Is Buying a Consulting Firm the Next Step for Microsoft?.
Archived in Kastner Research Archive. DOI: [pending]

## Methodology

press-feature-with-analyst-quotes
