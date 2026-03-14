# AS/400 and the Year 2000: IBM Leading Users Across an Unknown Chasm
> Archived from: https://web.archive.org/web/19961023174751/http://www.aberdeen.com:80/secure/viewpnts/v9n17/htframe.htm
> Original publication date: September 27, 1996
> Author: Aberdeen Group

---

## Original Document Text

Volume 9 / Number 17 — September 27, 1996

**AS/400 and the Year 2000: IBM Leading Users Across an Unknown Chasm**

What will the impact of the Year 2000 problem be on your AS/400 or System/3X operations? Or for that matter, your mainframe, UNIX, VMS, or other application operating environments? If you think you know, you probably have not yet heard about all the subtle problems — gotchas — that are continuously surfacing. And if you know you do not know, please consider yourself among the Year 2000 savvy.

Understanding the management and technology complexity involved in managing the Year 2000 dilemma, the trade-offs involved in solving it within each enterprise, and the scarcity and increasing cost of available resources, IBM's AS/400 division is proactively establishing a leadership role in helping its installed base make the Year 2000 transition — and providing a safe haven that IS professionals from other operating environments can quickly jump to.

**Executive Summary**

The Year 2000 problem — the result of programming systems software and applications assuming "19" as the first two digits of the year-date — is real. Very disconcertingly, the impact on each individual enterprise and system within an enterprise will be different — there simply is no "silver bullet" solution that can uniformly cure all the problems at each site.

Solving the Year 2000 transition dilemma will require the efforts of both an enterprise's senior executive and MIS management. After rigorously analyzing the implications of the Year 2000 upon its operations, every enterprise finds that the predicament is larger and more complex than ever imagined.

No supplier of computer hardware, software, or services can by itself fix all the industry's Year 2000 transition issues. However, Aberdeen believes that IBM's AS/400 division is doing all that a hardware systems supplier can possibly do — and considerably more than its competitors — to assist its customers and independent AS/400-focused application software providers achieve Year 2000 safety and compliance.

With the latest release of OS/400 Version 3, the AS/400's operating system is now Year 2000 safe. IBM has published the listing of its licensed systems software products that are Year 2000 ready. It has requested that independent software vendors (ISVs) who provide applications to run on the AS/400 publicly state that they are Year 2000 compliant.

The AS/400 division is doing its best to make its customers, including business unit executives within enterprises that rely on the AS/400, aware of the Year 2000 issues and is in the process of developing software to help users assess their Year 2000 vulnerability.

Going even deeper into the applications support area, the AS/400 division is suggesting alternative methods to manage the Year 2000 problems in existing applications and publicly releasing date-calculation algorithms that have been built into OS/400 for use with new or migrated applications.

In addition, the AS/400 division is recruiting independent professional service organizations that have the skills necessary to help customers make the Year 2000 transition with as little pain as possible.

In comparison, most other hardware suppliers seem unsure of what they should or can do to assist their installed base of customers. After all, most of the problems will be found in ISV-licensed or in-house-developed applications and system software — not their problem in their opinion. And with what seems to be a multitude of lawyers closely scrutinizing the situation, there is a natural reluctance on the part of any supplier to act until a leader successfully initiates the process of providing direct and/or auxiliary support.

IBM's AS/400 division is taking the industry-leadership position in helping users understand and manage Year 2000 transition issues. This is a very courageous position — many are ready to shoot the Year 2000 bad-news messenger. However, Aberdeen believes that IBM's efforts are proactive, correct, and will soon be rewarded with even greater user loyalty — if that is possible — to the AS/400.

**AS/400 and The Year 2000 Dilemma — Why It Is Real**

Simply put, 10-to-30 years ago when computer hardware resources (such as disk drives and memory) were scarce and expensive, programmers assumed the two digits, "19", in year dates. In addition, hard-coding "19" saved countless hours of valueless end-user data entry. The prevailing wisdom was that 1960-1980's applications and systems software would be replaced early in the 1990s and no harm done.

But, as demand for new types of more responsive business-critical and PC applications has grown dramatically over the last decade, enterprises have invested in these new opportunities. The replacement of working, production applications has only occurred in a few rare instances. Organizations preferred to surround and enhance their working systems with newer technologies without running the risk of endangering proven systems.

Now that it is time to make production systems Year 2000 safe, organizations are finding obstacles that were never expected. For example, it is often not practical to expand a 2-digit date representation to a 4-digit code on many legacy storage systems — new databases running on new disk arrays must be used. Or, different applications — just like countries — use different date-coding schemes and there is no agreed upon standard for moving forward. And just as frustratingly in the U.S., the Financial Standards Accounting Board (FASB) currently insists that Year 2000 MIS-remedial efforts be expensed, instead of capitalized, causing the full impact of these additional, non-productive costs to drop to a company's bottom line.

Current AS/400 users must face all the same Year 2000 transition issues as classic glasshouse data centers. (Visit http://www.year2000.com for a more in-depth education on the numerous facets of the Year 2000 transition issues.) The same limited physical resources and requirement to minimize 96-column card keypunching efforts encouraged System/3X programmers to assume "19" in the date year. And until OS/400 version 3, the AS/400 operating system could return ambiguous — probably erroneous — year dates when relied upon to make calculations past 2000 and would require manual date input upon startup — try that until your operator makes an error — after January 1, 2000. Even today, the AS/400 uses a fixed window calendar that runs between 1940 and 2039. (More on the use of 100-year windows to manage Year 2000 application logic issues later.)

---

## Frictionless Data Package Metadata
> Auto-generated by Archival Ingest Skill v13

### Study Record

| Field | Value |
|-------|-------|
| study_id | aberdeen-1996-as400-year-2000-ibm-leading-users |
| title | AS/400 and the Year 2000: IBM Leading Users Across an Unknown Chasm |
| author | Aberdeen Group |
| date | September 27, 1996 |
| series | Volume 9, Number 17 |
| type | market-viewpoint |
| subject_domain | Year 2000 compliance / IBM AS/400 |
| methodology | analyst-commentary |
| license | CC-BY-4.0 |

### Abstract

Aberdeen Group market viewpoint examining the Y2K problem in the context of IBM AS/400 and System/3X installed base. Praises IBM's AS/400 division for proactive Y2K leadership — OS/400 v3 declared Year 2000 safe, compliant software lists published, ISV compliance requested, professional services recruited, and date-assessment tools in development. Contrasts IBM favorably against other hardware suppliers who remained reluctant to engage with Y2K issues.

### Document Assessment

| Dimension | Rating | Rationale |
|-----------|--------|-----------|
| Importance | high | Historically significant as one of the earliest systematic Y2K risk analyses for a specific platform; published 3+ years before Y2K; influenced IBM's strategy and customer planning. |
| Relevance | high | Directly relevant to IT risk management, legacy system management, and platform migration decisions. Y2K was one of the largest IT remediation efforts in history. |
| Prescience | high | Predictions of increased user loyalty, no single-supplier fix, and continuous 'gotcha' problems all confirmed. The AS/400 platform survived and thrived post-Y2K. |

### Prescience Detail

| Prediction (September 1996) | Outcome (Verified) |
|----------------------------|--------------------|
| IBM's Y2K leadership will result in even greater user loyalty to AS/400 | Confirmed: AS/400 maintained strong installed base; rebranded as iSeries/System i/IBM i, still active |
| No silver bullet — no single supplier can fix all Y2K issues | Confirmed: required massive industry-wide effort; no single fix |
| Subtle Y2K 'gotchas' will continue to surface | Confirmed: embedded systems, chip-level issues, leap year 2000 were unexpected problems |
| Y2K impact larger and more complex than imagined at each enterprise | Confirmed: most organizations found Y2K remediation costs exceeded initial estimates |

### Entities Referenced

| entity_id | entity_name | type | status |
|-----------|-------------|------|--------|
| IBM | IBM Corporation | vendor | active |
| IBM-AS400-DIV | IBM AS/400 Division | organizational-unit | active (renamed Power Systems) |
| ABERDEEN-GROUP | Aberdeen Group | analyst-firm | active |
| FASB | Financial Accounting Standards Board | standards-body | active |

### Technologies Referenced

| tech_id | tech_name | lifecycle_at_study | lifecycle_current |
|---------|-----------|-------------------|-------------------|
| AS400 | IBM AS/400 | mature | legacy |
| OS400V3 | OS/400 Version 3 | current | legacy |
| SYSTEM3X | IBM System/3X | legacy | obsolete |
| YEAR2000-TECH | Y2K Date Remediation | emerging | obsolete |
| DATE-WINDOWING | 100-Year Window Algorithm | growth | obsolete |
| MAINFRAME | IBM Mainframe | mature | legacy |
| VMS | DEC VMS | mature | legacy |

### Observation Summary

| observation_type | count |
|-----------------|-------|
| strategy-classification | 7 |
| viability-prediction | 4 |
| actual-outcome | 5 |
| technology-assessment | 5 |
| framework-factor | 3 |
| market-data | 2 |
| expert-opinion | 4 |
| **Total** | **30** |
