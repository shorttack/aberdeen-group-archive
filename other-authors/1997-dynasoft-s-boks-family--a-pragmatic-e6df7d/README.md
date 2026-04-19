# DynaSoft's BoKS Family: A Pragmatic Choice for Single Sign-On

| Field | Value |
|-------|-------|
| Author | Aberdeen Group |
| Date | 1997-06-01 |
| Type | Profile |
| Domain | Enterprise Security / Single Sign-On |
| License | CC-BY-4.0 |

## Abstract

Aberdeen Group profile of DynaSoft AB (Stockholm, Sweden) and its BoKS product family, evaluating it as a pragmatic Single Sign-On (SSO) solution for enterprises. The report covers DynaSoft's SSO/SSSO product architecture (BoKS Desktop, BoKS Connect, BoKS Manager, ToolBoKS), its authentication framework using RSA cryptography and X.509 certificates, strategic partnerships with Hewlett-Packard and Sun Microsystems, and user testimonials from major enterprises including BankBoston, BP Oil, Citibank, Chase Manhattan Bank, Merrill Lynch, and Telstra. Aberdeen concludes BoKS delivers reliable, pragmatic SSO that users consistently recommend.

## Data Tables

| Table | Rows |
|-------|------|
| studies.csv | 1 |
| entities.csv | 15 |
| technologies.csv | 12 |
| observations.csv | 25 |
| codes.csv | 24 |

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

Aberdeen Group (1997). DynaSoft's BoKS Family: A Pragmatic Choice for Single Sign-On.
Archived in Kastner Research Archive. DOI: [pending]

## Methodology

Vendor profile with user interviews and product evaluation
