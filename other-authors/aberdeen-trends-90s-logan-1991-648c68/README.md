# Aberdeen Group 'Trends in Computing in the 90's: Are There Any Right Answers?' (John R. Logan VP, 1991)

| Field | Value |
|-------|-------|
| Author | John R. Logan (Vice-President, Aberdeen Group) |
| Date | 1991 |
| Type | consulting-presentation-deck |
| Domain | enterprise-IT-strategy |
| License | CC-BY-4.0 |

## Abstract

Logan's 1991 Aberdeen deck establishes the firm's 'Inverted Computing Pyramid' framework that PSK and the Aberdeen team carry through the decade. The processor section forecasts crossover where merchant RISC chips (75 MIPS, 100 instructions) overtake captive CISC mainframe processors (40 MIPS, 300 instructions). The desktop section forecasts that by 1994 MS-NT, IBM/Apple Big Pink, and Solaris will replace 1991's MS-DOS/OS/2/Unix triad — partially correct (NT and Solaris shipped; Big Pink/Taligent failed). Supplier-alliance taxonomy lists OSF v UI, ACE v Big Pink, Object Management Group, SQL Access Group, Digital/MIPS, IBM/Thinking Machines, Digital/Masspar, Sun/HP. Client-server taxonomy: Remote Presentation / Remote Database / Cooperative Processing / Distributed Database. Object technology framed as 'objects for the future' with interoperability/ease-of-use/multi-user-LAN benefits.

## Data Tables

| Table | Rows |
|-------|------|
| studies.csv | 1 |
| entities.csv | 8 |
| technologies.csv | 13 |
| observations.csv | 8 |
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

John R. Logan (Vice-President, Aberdeen Group) (1991). Aberdeen Group 'Trends in Computing in the 90's: Are There Any Right Answers?' (John R. Logan VP, 1991).
Archived in Kastner Research Archive. DOI: [pending]

## Methodology

Aberdeen Group consulting deck by VP John R. Logan (Boston, 92 State Street). Inverted Computing Pyramid framework: Applications / Production Environments (DBMS+Communications) / System Platforms (HW+OS) / Processors. Walks through processor-level trends (RISC vs CISC; 100 vs 300 instructions; merchant vs captive; 75 MIPS by 1991), high-end systems (traditional supercomputer / mainframe-with-vector / massively-parallel / superscalar-server), departmental minisuper/compute server, and desktop OS rightsizing (1991 MS-DOS/OS/2/Unix; 1994 forecast MS-NT/Big Pink/Solaris).
