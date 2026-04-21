# SARS wirft Schatten über elektronische Beschaffungskette

| Field | Value |
|-------|-------|
| Author | Robert Ristelhueber, EBN (EE Times Europe / Germany) |
| Date | 2003-04-08 |
| Type | news-article |
| Domain | IT-supply-chain-pandemic-risk |
| License | CC-BY-4.0 |

## Abstract

German-language EE Times Europe article (Apr 8 2003) by Robert Ristelhueber (EBN) on SARS's shadow over the electronic supply chain. Datelined Manhasset. Business travel to Asia has ground to a halt; manufacturing and distribution in China and Southeast Asia face problems. Cites Motorola's temporary Singapore night-shift closure (532 workers affected), HP and Intel employees with SARS/SARS-like symptoms in Hong Kong, Chartered Semiconductor Manufacturing's contingency plans, Flextronics International preventive measures, and quotes from Chuck Magee (EVP Sales/Marketing at America II Electronics, St. Petersburg FL), Steven Fox (Merrill Lynch NY analyst), Raymond Tsang (President Avnet Electronics Marketing Asia HK), Schuyler Glidden (President SG Industries Beverly MA), and Tony Tseng (Merrill Lynch Taipei). Most critically, Peter Kastner, analyst at the Boston-based Aberdeen Group, estimates the SARS impact will be far more far-reaching than companies currently imagine: 'Kurzfristig haben wir es mit einer Unterbrechung des Reiseverkehrs von Führungskräften und Verkaufsmitarbeitern nach und aus Asien zu tun. Sollten die Quarantänemaßnahmen jedoch zunehmen, wird das einen erheblichen Einfluss auf die Weltwirtschaft haben. Dann wird nichts mehr hergestellt — weder Kondensatoren noch Weihnachtsgeschenke.' Kastner further advises every executive to think through the 'unimaginable,' giving the example of laptop manufacturers asking: where do our power supplies come from? Everyone buys them from China. What happens if I cannot move goods by ship or air out of the country?

## Data Tables

| Table | Rows |
|-------|------|
| studies.csv | 1 |
| entities.csv | 12 |
| technologies.csv | 4 |
| observations.csv | 6 |
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

Robert Ristelhueber, EBN (EE Times Europe / Germany) (2003). SARS wirft Schatten über elektronische Beschaffungskette.
Archived in Kastner Research Archive. DOI: [pending]

## Methodology

industry-analysis, analyst-commentary
