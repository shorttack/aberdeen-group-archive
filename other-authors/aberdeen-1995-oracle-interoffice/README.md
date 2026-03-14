# Oracle InterOffice: Helping IS Deploy Solutions to Business Partners and Customers Over the Internet

**Aberdeen Group Product Profile | December 13, 1995**

Archived study ID: `aberdeen-1995-oracle-interoffice`

---

## Overview

This Frictionless Data Package archives Aberdeen Group's December 13, 1995 product profile of **Oracle InterOffice** (code-named Pegasus), a modular cross-platform messaging, document management, workflow, and calendaring product announced by Oracle Corporation on the same date as this study's publication.

Aberdeen was struck by Oracle's sharp Internet focus and concluded that Oracle InterOffice was the first groupware product architecturally designed—from the ground up—for Internet-enabled business collaboration. The study introduced the concept of the **Electronic Economic Community**: a borderless network of businesses, partners, and customers enabled by ubiquitous Internet connectivity and dissolving the electronic walls that had long isolated enterprises from their supply chains and customer bases.

**Original source (Wayback Machine):** https://web.archive.org/web/19970112012152/http://www.aberdeen.com:80/secure/profiles/oracle/oracle.htm

---

## Key Findings

| Finding | Detail |
|---|---|
| Oracle revenue (1995) | $3 billion |
| Competitive lead claim | 6–12 months ahead of nearest rivals |
| Server platform support | 25+ platforms (NT, RISC/Unix including HP-9000, Sun, IBM RS/6000) |
| Client platforms | Windows NT, Windows 95, Windows 3.1, Motif, Macintosh, ASCII terminal, Web browser |
| Mobile/PDA | In development with hardware manufacturers |
| APIs supported | OLE Automation, OCX, MAPI 1.0 + SPI, ODMA, SQL/PL/SQL, Web browser; Java planned |
| Architecture pattern | Modular functional components sharing a Common Database Engine and Common Access Layer |
| Internet strategy | First groupware product designed for Internet — not merely adapted via gateways |
| Concept introduced | Electronic Economic Community |

---

## Package Structure

```
aberdeen-1995-oracle-interoffice/
├── datapackage.json          # Frictionless Data Package descriptor
├── README.md                 # This file
├── data/
│   ├── studies.csv           # Study metadata (1 row)
│   ├── entities.csv          # Organizations referenced (8 rows)
│   ├── technologies.csv      # Technologies referenced (31 rows)
│   ├── observations.csv      # Structured observations (48 rows)
│   └── codes.csv             # Controlled vocabulary (29 codes)
├── schema/
│   └── schema_org.json       # Schema.org JSON-LD metadata
└── scripts/
    └── demo_analysis.py      # Demonstration analysis script
```

---

## Data Resources

### studies.csv
One row describing the study. Fields: `study_id`, `title`, `author`, `date`, `type`, `domain`, `methodology`, `abstract`, `source_url`, `page_count`, `contact_name`, `contact_email`, `publisher_address`.

### entities.csv
Eight organizations referenced in the study. Includes current (2026) status:
- **Oracle Corporation** — primary vendor (active)
- **Aberdeen Group** — research author (acquired by Harte-Hanks 2001)
- **Microsoft Corporation** — competitor referenced (active)
- **Lotus Development Corporation** — competitor referenced (acquired by IBM 1995; product now HCL Notes)
- **Novell, Inc.** — competitor referenced (acquired by OpenText via Micro Focus / Attachmate chain)
- **Sun Microsystems** — planned technology partner for Java (acquired by Oracle 2010)
- **Hewlett-Packard Company** — platform vendor (active as HP Inc. / HPE)
- **IBM Corporation** — platform vendor (active)

### technologies.csv
31 technologies, standards, and platforms referenced in the study. Includes lifecycle status as of 2026:
- **Obsolete (11):** Oracle InterOffice, Oracle Office, Oracle Document Management, Oracle PowerObjects, ODMA, WFAPI, Windows NT 3.51, Windows 95, Windows 3.1, ASCII Terminal, HP-9000/PA-RISC
- **Active (9):** Oracle Database/PL/SQL, Java, World Wide Web/Browsers, SMTP, SQL, End-to-End Encryption, Microsoft Exchange, IBM RS/6000/AIX, Oracle Workflow (evolved)
- **Evolved (5):** OLE/OCX → ActiveX/.NET, Oracle ConText → Oracle Text, Macintosh OS → macOS, Internet Firewall → NGFW, Oracle Workflow
- **Active-Niche (4):** MAPI 1.0, MAPI SPI, Sun SPARC/Solaris, IBM RS/6000/AIX
- **Superseded (1):** Oracle Workflow (pre-InterOffice form)

### observations.csv
48 structured observations covering:
- Oracle's $3B revenue and strategic agility (obs-001–002)
- Product codename Pegasus and announcement date (obs-003, obs-047)
- 6–12 month competitive lead claims (obs-007, obs-041)
- 25+ platform support (obs-010)
- Electronic Economic Community concept (obs-006, obs-033, obs-038)
- Modular architecture and Common Access Layer (obs-017, obs-023)
- SQL/PL/SQL data access (obs-018)
- OLE/OCX development interfaces (obs-019)
- MAPI, ODMA, WFAPI support (obs-014, obs-020, obs-021)
- Java integration roadmap (obs-022)
- Three electronic walls: connectivity, security, application access (obs-030)
- Internet security misconception critique (obs-031–032)
- Data hostage problem and Web solution (obs-035–036)
- Market landscape: all groupware vendors scrambling for Internet (obs-028)
- IS strategic opportunity post-Web deployment (obs-037)

### codes.csv
Controlled vocabulary covering 8 schemes: `observation_type` (8 codes), `entity_type` (1), `entity_role` (6), `entity_status` (3), `tech_lifecycle` (5), `study_type` (1), `domain` (1), `methodology` (3).

---

## Historical Context

Oracle InterOffice was announced at a pivotal moment — December 1995 — when the commercial Internet was less than two years old as a public phenomenon and the World Wide Web was barely three years old. Aberdeen's assessment proved prescient about the Internet's disruptive potential for enterprise collaboration, but the specific product did not prevail: Oracle InterOffice was eventually discontinued in the late 1990s as Oracle pursued other strategic priorities. The Electronic Economic Community concept Aberdeen introduced anticipated what would become ubiquitous in the 2000s: SaaS-based B2B integration, API economies, and cloud collaboration platforms (Microsoft 365, Google Workspace, Slack).

Key technology trajectories from this study that proved accurate:
- Web browsers became the universal client interface (obs-016, obs-033)
- Java became a major cross-platform development platform (obs-022)
- Internet security fears did prove addressable (obs-031)
- OLE/OCX evolved into ActiveX and then .NET (obs-009, obs-019)
- SMTP remained the email transport standard (obs-029)

Key trajectories that did not materialize as predicted:
- Oracle InterOffice did not achieve its 6–12 month lead; Microsoft Exchange became the enterprise messaging standard
- PDAs as imagined in 1995 were superseded by smartphones

---

## License and Attribution

Data package: [Open Data Commons Attribution License (ODC-By 1.0)](https://opendatacommons.org/licenses/by/1-0/)

Original study copyright: Aberdeen Group, Inc., Boston, Massachusetts. Published for electronic distribution. All trademarks are property of their respective holders.

---

## Contact

Original Aberdeen Group contact: stevens@aberdeen.com  
Publisher: Aberdeen Group, Inc., One Boston Place, Boston, Massachusetts 02108  
Telephone: 617-723-7890 | FAX: 617-723-7897
