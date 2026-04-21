# IBM Opens, Customizes Power Chips

| Field | Value |
|-------|-------|
| Author | Jay Lyman, TechNewsWorld |
| Date | 2004-04-01 |
| Type | news-article |
| Domain | embedded-processors-ip-licensing |
| License | CC-BY-4.0 |

## Abstract

TechNewsWorld article (Apr 1 2004, Jay Lyman) on IBM's Power Everywhere event in New York announcing opening of the Power microprocessor architecture to external customization, with China's Culturecom cited as first-mover (Chinese-language-character customization). IBM spokesperson Jim Larkin: 'We want to see the customers themselves do the customization on the microprocessor architecture, and that's never happened before.' Aberdeen chief research analyst Peter Kastner provides the strategic read: 'No one today considers designing a new product by designing the processor to run it, so IBM wants to sell more Power processor cores while not shoving a full-blown microprocessor design down designers' throats.' Kastner frames the play as IBM fighting Intel's two powerhouse architectures (x86 and XScale) for silicon in the next generation of consumer devices — cell phones, set-top boxes, cameras: 'Customization could be done economically and with low technology risk.' Gartner's Martin Reynolds adds the chip-redesign-cost context: 'It's going to be incredibly expensive to redesign chips.'

## Data Tables

| Table | Rows |
|-------|------|
| studies.csv | 1 |
| entities.csv | 10 |
| technologies.csv | 5 |
| observations.csv | 7 |
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

Jay Lyman, TechNewsWorld (2004). IBM Opens, Customizes Power Chips.
Archived in Kastner Research Archive. DOI: [pending]

## Methodology

announcement-analysis, analyst-commentary
