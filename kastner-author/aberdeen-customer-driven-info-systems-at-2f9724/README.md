# Aberdeen Group — Customer-Driven Information Systems (AT&T/NCR + Oracle Seminar, 1993)

| Field | Value |
|-------|-------|
| Author | Peter S. Kastner — Vice President, Aberdeen Group, Inc. |
| Date | 1993-01-01 |
| Type | sponsored-seminar-deck |
| Domain | decision-support-and-data-warehouse |
| License | CC-BY-4.0 |

## Abstract

Aberdeen Group seminar presentation deck delivered by Peter S. Kastner (Vice President, Aberdeen Group) at a 1993 seminar sponsored by AT&T/NCR and Oracle Corp, titled 'Customer-Driven Information Systems: Changing How Our Enterprises Do Business.' Boston office (617/723-7890). Defines Customer-Driven Information Systems as 'getting, moving, and using information to leverage our customers' goals' while 'refocusing IS on a customer-centric world.' Agenda: Definition, Business Dynamics (Unprecedented Change), Customer-Driven Business Challenges, The Role of IT, Wrap-up, Q&A. Worldwide Reality section cites primary drivers: U.S. Rules & Regulations; Europe Reconstruction & Open Markets; Japan Oligopoly & Pyramid-scheme financing. Driven to New Rules: corporation national → global, market: fragmented; product development cycle; performance: short-term → long-term. Trends Drive Business Issues: customers with greater expectations, global market access and competition, cycle time compression. Customer-Driven Business Challenges: success hinges on businesses that know what they're in, react faster, differentiate themselves, know their customers, deliver what customers want, control costs intelligently, run data for information. Rapid Evolution is Inevitable: 5,000,000 Fortune-1000 jobs lost since 1990; CIO turnover rate 30%/yr. Approaches for Business Issues: strategic leverage of information, enterprise empowerment, business reengineering. Includes the famous 'Red Summer Dress Problem' decision-support example. Role of Executive Management: increasing customer service while improving efficiency and lowering overhead — goals: higher repeat business, lower cost of sales, decreased competitive pressure, higher net profit. Old Approach (Computer as Accounting Machine) vs New Approach (Computer as Decision Support / data warehouse). Implicit context: NCR's 1991 acquisition of Teradata (while owned by AT&T) and Oracle's emerging data-warehouse positioning.

## Data Tables

| Table | Rows |
|-------|------|
| studies.csv | 1 |
| entities.csv | 8 |
| technologies.csv | 7 |
| observations.csv | 11 |
| codes.csv | 40 |

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

Peter S. Kastner — Vice President, Aberdeen Group, Inc. (1993). Aberdeen Group — Customer-Driven Information Systems (AT&T/NCR + Oracle Seminar, 1993).
Archived in Kastner Research Archive. DOI: [pending]

## Methodology

Aberdeen-Group-presentation-deck
