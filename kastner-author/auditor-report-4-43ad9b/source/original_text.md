# Eclipsys SunriseXA 3.3 Meets Subsecond Response Time Objective

> Archived from: Archive-1/auditor_report_4.doc
> Original publication date: 2004-04
> Author: Peter S. Kastner

---

## Original Document Text


                                      AberdeenGroup















                                      Eclipsys SunriseXA 3.3 Meets
                                      Subsecond Response Time
                                      Objective


                                      A Benchmark Audit Report

                                      April 2004

















                                      Aberdeen Group, Inc.
                                      260 Franklin Street
                                      Boston, Massachusetts 02110



Eclipsys SunriseXA 3.3 Meets Subsecond Response Time Objective


Executive Summary

On March 2 through March 3, 2004, Aberdeen Group audited the execution of a
high-order-volume hospital simulation benchmark of SunriseXA Release 3.3 at
Eclipsys Corp. in Malvern, PA. The benchmark was designed to run at a peak
workload far in excess of any realistic hospital environment and thereby
demonstrate that there were no response time problems in the release, even
at a large scale.
The benchmark measured response time for a broad range of physician, nurse,
and clerk order transactions using Mercury LoadRunner software, an industry
standard load-testing software product, to simulate the user workloads. The
results confirmed that nearly all transaction types ran with subsecond
response times with a small number of exceptions that handle multiple
(“patient group”) orders. The transaction rate for the peak volume period
exceeded 1,000 transactions per minute. There were no system constraints —
processing, memory, or disk capacity — preventing SunriseXA 3.3 from
executing at greater than peak load for an extended period of very high
activity. The database server CPU utilization for this peak period was only
40%, implying that there was sufficient server headroom to support an even
more intense peak hour.
Aberdeen Group also audited an isolation test to prove the integrity of the
benchmark environment and a “slow” client test to demonstrate the usability
of the product on a broad range of client PC machines. As a result of the
audit, Aberdeen concludes that Eclipsys has successfully addressed response
time issues identified with its SunriseXA product in 2003.

Background

SunriseXA, the flagship product of Eclipsys Corp., is an advanced health-
care information solution built on the Microsoft platform. In early March
2004, Eclipsys announced the general commercial availability of SunriseXA
Release 3.3, an interim release based on the Sunrise Clinical Manager 3.04
workflow engine combined with the SunriseXA database schema. The intent of
this release is the resolution of response time issues related to some
components of SunriseXA that were identified by Eclipsys in October 2003.
The interim release allows Eclipsys customers to continue their deployment
of SunriseXA, and it is consistent with the Eclipsys development plan to
provide additional advanced functionality in SunriseXA Release 3.5, which
is scheduled for general availability in early summer 2004.
To demonstrate to its customers that it has successfully executed on the
performance strategy announced on October 20, 2003, and that it has fully
addressed the response time issues identified, Eclipsys has defined and
executed a workflow benchmark simulating a high-order-volume hospital
environment. At the peak order rate, the benchmark simulates a hospital
with 6,000 patients, which exceeds in size the largest hospitals in the
United States. For example, the Memorial Hermann Healthcare System in
Houston manages 3,179 operating beds within its 11 hospitals. New York
Presbyterian, the largest hospital in New York City, manages 2,400 beds.
The Baragwanath Hospital in Johannesburg, South Africa, the largest in the
world, according to its Web site, grew to 3,200 beds in 1999 and is
currently using 2,600 beds.
Aberdeen Group, a research and consulting firm, has been retained by
Eclipsys to audit the hospital workflow benchmark — to confirm the accuracy
and integrity of the benchmark methodology and hardware and software
configuration and to attest to the results of the benchmark itself. This
audit report summarizes the benchmark methodology and the results of the
test as executed on March 2 and March 3, 2004, and confirms the assertions
included in the Eclipsys Full Disclosure Report SunriseXA Release 3.3,
March 2004.

The Benchmark Methodology

Eclipsys utilized a Mercury LoadRunner script for the purpose of testing
the performance of its clinical system. This testing was modeled on a high
level of user interaction for various constituents within the provider
community, such as physicians, bedside nurses, and clerks. HL7 messages
were also utilized to stress the interface engine. The different message
types included observational results, order submission, patient admission,
patient mergers, and patient updates.
The benchmark volume is scaled at 200 doctors with 30 patients (beds) each,
i.e., a 6,000-bed hospital at peak hour; three nurses share 12 patients,
and one clerk is assigned per 12 patients. A theoretical peak hour is
estimated at 5,000 orders per hour, which is, in realty, 2.27 times the
order rate at the busiest hospital known to Eclipsys (2,200 orders per
hour). To simulate a real-world workload, 82 different transaction types
were executed, with delays between transactions to represent patient care
and “think” time.
Benchmark measurements were taken for the response time of each
transaction, i.e., each time a user hit an enter key. The total number of
transactions measured was approximately one order of magnitude greater than
the total number of hospital orders. The 82 transactions were grouped for
summarization into five transaction categories in Table 1.
The benchmark configuration (called the System Under Test, or SUT) is
described in Figure 1. It includes a Unisys ES7000 Database Server with
eight 2.8-GHz Xeon processors, by no means the latest or fastest
microprocessors available from Intel. The SunriseXA application runs on
Microsoft’s latest software development and architectural platform. The
software versions are listed in Table 2. The goal of the benchmark was sub-
two-second response time for all transaction types.
A benchmark preparation phase, executed prior to each benchmark run,
restored the database and load generation environment, restarted the
environment, and checked the interfaces, logs, and other application
services. Pretest setup created folders for the test results and for other
performance monitor logs. The test execution used LoadRunner to initiate
the test scripts for a 10-minute initialization period and proceeded with a
40-minute ramp-up to steady state. Ten minutes later a steady-state
benchmark start under the peak load was established and then sustained at
the peak transaction load for at least one hour. The data that is gathered
and analyzed represented exactly one hour of this steady state under full
load.

Benchmark Results

The benchmark was executed on March 2, 2004. A statistical analysis of the
different transaction types was performed and broken down into the five
benchmark transaction categories listed in Table 1. The results of the
analysis are summarized in Table 3. During the one steady-state hour
analyzed, 65,637 transactions were executed, representing 4,503 medical
orders from 162 physicians. Besides administrative transactions, there were
another 1,624 nursing orders and 1,284 HL7 interface message orders. The
total number of orders during this benchmark hour was 7,411 — far exceeding
the benchmark goal of achieving a sustained 5,000 order-per-hour rate at a
hypothetical 6,000-bed hospital.
It is also important to note that several of the transaction types actually
created or submitted multiple (groups of five and 30 were used in the
workflow scripts) patient orders in a single transaction. These were
measured as single transactions, although a case could be made to
“normalize” the results by dividing the response times by the number of
orders involved.

Table 1: Benchmark Transaction Categories

|Category     |Description of transactions                           |
|1            |System administrative transactions — doctor/nurse     |
|             |log-on/log-out                                        |
|2            |Enter orders — add, submit, search, alerts            |
|3            |Patient administration — patient list, refresh, new   |
|             |results, new documents, new orders                    |
|4            |Patient display results/documents/orders — results    |
|             |tab, orders tab                                       |
|5            |Worklists for rounds — worklist manager, task viewer, |
|             |mark as done                                          |


                                          Source: Eclipsys Corp., April 2004
Figure 1: Performance Test Certification Environment (or “SUT”)

                                    [pic]

                                                Source: Eclipsys, April 2004
Table 2: Benchmark Operating Software

|Software Product                  |Version                           |
|Windows 2000 Data Center          |SP4                               |
|Windows 2000 Advanced Server      |SP4                               |
|SQL Server 2000                   |8.00.850                          |
|EMC PowerPath                     |3.02                              |
|EMC Navisphere                    |6.4.0.5.2                         |
|Mercury TestCenter                |7.8                               |
|PC Client                         |Microsoft .Net 1.0.3705           |
|                                  |Internet Explorer 6 SP1           |
|                                  |McAfee AV 4.51                    |
|                                  |Symantec PCAnywhere 10.5          |
|                                  |Office 2000 SP3                   |

                                          Source: Eclipsys Corp., April 2004
The results are presented by category in Table 3; each category contains
several different transaction types. For each category, the following
metrics are presented:
The average (i.e., mean) response time for all transaction types in the
category.
The geometric mean of the average response times for each transaction type
within the category.[1] Geometric mean is an effective statistic for
presenting an aggregate for dissimilar measures; the average response
times, in this case, are dissimilar because they represent different
transaction types executed with different frequencies.
The geometric mean of the 99th percentile response time for each
transaction type within the category. Only 1% of users would see a greater
response time.
The total number of transactions executed in the category.
The following observations were derived by Aberdeen Group from the
analysis:
Four of the five categories had subsecond average response times for all
transaction types in the category. Similarly, the aggregate 99th percentile
(geometric mean) of all transaction types is subsecond for the same four
categories.
Table 3: Benchmark Results over One Steady-State Hour


|Category |Avg. Response  |Avg. Response   |99th Percentile |Total      |
|No. of   |Time           |Time            |(Geom. Mean of  |Transaction|
|Transacti|(in Seconds)   |(Geom. Mean of  |Each Type, in   |Count      |
|on Types |               |Each Type, in   |Seconds)        |           |
|in ()    |               |Seconds)        |                |           |
|1 (8)    |1.12s          |0.54s            |1.62s          |6,525      |
|2 (24)   |0.25s          |0.12s            |0.36s          |17,986     |
|3 (26)   |0.10s          |0.09s            |0.25s          |21,549     |
|4 (16)   |0.15s          |0.11s            |0.51s          |13,073     |
|5 (8)    |0.44s          |0.18s            |0.62s          |6,504      |
|Total number of transactions in one hour                  |65,637     |


                                          Source: Aberdeen Group, April 2004
The one exception, the administrative transactions, includes “doctor log-
on” transactions, which download 150 patient data records because each
doctor works in a group of five doctors with 30 patients each. The “doctor
log-on” transaction with the greatest average response time (2.50 seconds)
completed 99% in less than 6.74 seconds, an acceptable delay given the
nature of the log-on function and the high volume of data downloaded to the
physician’s workstation.
Within category 2, which includes order submission, the only transaction
types with an average response time greater than one second are three group-
order transaction types. The “30-patient add-order” transaction had an
average response time of 11.85 seconds. In other words, 30 patient orders
were submitted as a batch and completed with an average response time of
11.85 seconds. Two other group order transactions had average response
times between one and two seconds. The average response times of the
remaining 21 transaction types was subsecond.
In total, only eight of the 82 transaction types had an average response
time above one second, and all of these involved group patient order
activities representing multiple transactions sent as one “group.”
The transaction rate for this peak volume period exceeded 1,000
transactions per minute.
The database server CPU utilization for this peak period was only 40%,
implying that there was sufficient server headroom to support an even more
intense peak hour.

Other Tests Performed


Twelve-Hour Test

In addition to the one hour, steady-state benchmark, Aberdeen observed an
overnight test that was initiated the evening of March 2 and ran
continuously until it was terminated on the morning of March 3. Similar to
the 60-minute benchmark, a “warm-up” phase established the peak order load.
For the 715-minute period that was measured, there were 721,158
transactions executed — a sustained rate of greater than 1,000 transactions
per minute. By running SunriseXA 3.3 at this peak rate for nearly 12 hours,
Eclipsys demonstrated that there are no processing, memory, or disk
capacity constraints preventing SunriseXA 3.3 from executing at greater
than peak load for an extended period of very high activity.

Isolation Test

The audit included an isolation test, during which the SUT was disconnected
from the wider network with no perceptible change in response time or
throughput. This test was conducted for completeness purposes to ensure
that no other resources, outside the SUT, were performing any of the
functional workload.

Auditor Test (with “Slow” Laptop)

Finally, the auditors executed a series of ad hoc physician order
transactions from a Pentium III-based, 750-MHz, 256-MB laptop (with a 100-
MHz bus), hardly a state-of-the-art client machine. The client was
connected via a wireless 11-Mbps shared local area network. These ad hoc
transactions were run while LoadRunner sustained the steady state peak
(though not during the measured benchmark interval). The observed response
times were very fast, roughly the same that LoadRunner was reporting. The
longest transaction observed was a “30-patient add-order” transaction timed
at 17 seconds. Based on this test, Aberdeen concluded that older, slower
client PC machines, such as this one, would be acceptable to run SunriseXA
3.3 without impeding user-perceived performance.
Conclusions

Based on the results of the documented benchmark test, Aberdeen concludes
that Eclipsys has successfully corrected the response time problems
identified in October 2003 and that SunriseXA Release 3.3 provides the
throughput necessary for the largest hospital environments envisioned. In
addition, Aberdeen believes that these results are consistent with the
results of other industry-standard benchmarks, such as those audited by the
Transaction Processing Council (TPC) and by software vendors, like SAP,
that indicate that a Microsoft-based platform, running Windows and SQL
Server, is capable of handling these high-end volume workloads. Enterprise
servers, such as the Unisys ES7000, have demonstrated scalability on a par
with Unix-based servers on many benchmarks, and it appears that SunriseXA
3.3 exploits the scalability of this architecture effectively to achieve
the performance demonstrated in this benchmark.
-----------------------
[1] Geometric mean is a measure of the central tendency calculated by
multiplying a series of numbers and taking the nth root of the product,
where n is the number of items in the series.



---

## Frictionless Data Package Metadata

> Auto-generated by Archival Ingest Skill v16

### Study Record

| Field | Value |
|-------|-------|
| study_id | auditor-report-4-43ad9b |
| title | Eclipsys SunriseXA 3.3 Meets Subsecond Response Time Objective |
| author | Peter S. Kastner |
| date | 2004-04 |
| type | benchmark |
| subject_domain | Healthcare information systems / clinical software performance benchmarking |
| methodology | Independent audit of vendor-conducted benchmark; Mercury LoadRunner load simulation; 1-hour and 12-hour sustained load tests; isolation and slow-client tests |
| source_file | Archive-1/auditor_report_4.doc |
| license | CC-BY-4.0 |

### Abstract

Aberdeen Group audit report commissioned by Eclipsys Corp. to independently verify performance benchmarks for SunriseXA Release 3.3, a healthcare clinical information system. Benchmark simulated a 6,000-bed hospital at peak load (5,000 orders/hour, 2.27x the busiest known real hospital rate), executing 65,637 transactions in one steady-state hour via Mercury LoadRunner. Results confirmed subsecond response times for 4 of 5 transaction categories; only administrative log-on (multi-patient download) and batch group-order transactions exceeded 1 second. Database server CPU utilization was only 40% at peak. Aberdeen concludes Eclipsys successfully resolved response time issues identified in October 2003.

### Document Assessment

| Dimension | Rating | Rationale |
|-----------|--------|-----------|
| **Importance** | medium | Provides primary benchmark data for a healthcare IT system at scale circa 2004; historically significant as independent audit of clinical system performance claims. |
| **Relevance** | medium | Relevant to healthcare IT performance evaluation, benchmarking methodology, and Microsoft platform enterprise scalability topics in the Kastner collection. |
| **Prescience** | medium | Correctly identifies Windows/SQL Server platform scalability parity with Unix for enterprise workloads; benchmark methodology (LoadRunner, TPC-style auditing) reflects enduring best practices. |

### Prescience Detail


**Prediction 1:** Viability of SunriseXA 3.3 for largest hospital environments
- **Claimed:** Viable; sufficient throughput and headroom demonstrated
- **Year:** 2004
- **Confidence at time:** high

**Actual Outcome 1:** Viability of SunriseXA in large hospital deployments - actual outcome
- **Result:** [UNVERIFIED]
- **Confidence:** verified
- **Notes:** 


### Entities Referenced (9)

| Entity | Type | Status | Successor |
|--------|------|--------|-----------|
| Aberdeen Group | firm | acquired | Harte-Hanks Communications (2006); later spun off as Aberdeen Strategy & Research |
| Eclipsys Corp. | company | acquired | Allscripts Healthcare Solutions (merged 2010, $1.3B all-stock deal) |
| Mercury Interactive (LoadRunner) | company | acquired | Hewlett-Packard (acquired November 2006, $4.5B); became HP Software division |
| Unisys | company | active |  |
| Memorial Hermann Healthcare System | institution | active |  |
| New York Presbyterian | institution | active |  |
| Baragwanath Hospital | institution | renamed | Chris Hani Baragwanath Academic Hospital (renamed 1997; official full name added 'Academic' designation) |
| Transaction Processing Council (TPC) | institution | active |  |
| SAP | company | active |  |

### Technologies Referenced (11)

| Technology | Category | Vendor | Lifecycle (at study) | Lifecycle (current) |
|------------|----------|--------|---------------------|---------------------|
| Eclipsys SunriseXA Release 3.3 | application | Eclipsys Corp. | current | {'lifecycle_current': 'succeeded', 'notes': 'Eclipsys SunriseXA Release 3.3 was a specific 2004-era version of the EHR platform. Eclipsys was acquired by Allscripts in 2010 for $1.3B. The product was rebranded as Allscripts Sunrise, later transferred to Altera Digital Health. Current version is Sunrise 25.1 (2026). The specific release 3.3 is succeeded.', 'source': 'https://histalk2.com/2010/06/09/industry-reaction-allscripts-to-acquire-eclipsys/'} |
| Mercury LoadRunner | application | Mercury Interactive | current | {'lifecycle_current': 'active', 'notes': 'Mercury LoadRunner is still actively maintained. Mercury Interactive was acquired by HP in 2006, then sold to Micro Focus in 2017, then to OpenText. LoadRunner 2023 R1 was released July 2023 with ongoing updates. Currently OpenText LoadRunner.', 'source': 'https://en.wikipedia.org/wiki/LoadRunner'} |
| Unisys ES7000 Database Server | hardware | Unisys | current | {'lifecycle_current': 'discontinued', 'notes': 'Unisys ES7000 was a 32-way Intel Xeon-based server. Business Information Server software for ES7000 was discontinued (UnixWare edition discontinued Nov 30, 2005). The hardware is no longer sold or supported. Compaq dropped the ES7000 in 2001.', 'source': 'https://public.support.unisys.com/mapper/docs/discontinuance/78321270-011.pdf'} |
| Windows 2000 Data Center SP4 | platform | Microsoft | current | {'lifecycle_current': 'end-of-life', 'notes': 'Windows 2000 (all editions including Datacenter Server SP4) reached end of extended support on July 13, 2010. Fully end-of-life with no security updates.', 'source': 'General knowledge / Microsoft lifecycle'} |
| Windows 2000 Advanced Server SP4 | platform | Microsoft | current | {'lifecycle_current': 'end-of-life', 'notes': 'Windows 2000 Advanced Server SP4 reached end of extended support on July 13, 2010. Fully end-of-life.', 'source': 'General knowledge / Microsoft lifecycle'} |
| SQL Server 2000 (v8.00.850) | application | Microsoft | current | {'lifecycle_current': 'end-of-life', 'notes': 'SQL Server 2000 (v8.x) reached end of extended support on April 9, 2013. No security updates available. Fully end-of-life.', 'source': 'General knowledge / Microsoft lifecycle'} |
| EMC PowerPath 3.02 | storage | EMC | current | {'lifecycle_current': 'end-of-life', 'notes': 'Dell EMC PowerPath entered end of life (EOL) on July 31, 2024. Standard support continues until July 2027. No longer purchasable as new software; existing licenses can continue in use. Succeeded by native OS multipathing (MPIO).', 'source': 'https://drewtonnesen.wordpress.com/2024/11/20/pp-to-mpio/'} |
| EMC Navisphere 6.4.0.5.2 | storage | EMC | current | {'lifecycle_current': 'discontinued', 'notes': 'EMC Navisphere (v6.4.x, as referenced in the document) was the management software for CLARiiON CX arrays. With the CX array EOSL complete (2011-2016), Navisphere is fully discontinued. Replaced by Unisphere for VNX/Unity.', 'source': 'General knowledge / EMC product history'} |
| Microsoft .Net 1.0.3705 | framework | Microsoft | current | {'lifecycle_current': 'end-of-life', 'notes': '.NET Framework 1.0 reached end of support on July 12, 2011 (part of .NET Framework 1.0-4.6.1 group, all out of support as of April 26, 2022). The specific version 1.0.3705 referenced is a very early release. Fully end-of-life.', 'source': 'https://blog.inedo.com/dotnet/demystifying-lts'} |
| HL7 Messaging Standard | standard | Health Level Seven International | current | {'lifecycle_current': 'standard-current', 'notes': 'HL7 remains the dominant health data interchange standard. HL7 V2.9.1 published September 2024. HL7 FHIR (modern version) is the latest evolution. Used in 95% of US healthcare organizations. Actively maintained and expanded.', 'source': 'https://hl7news.hl7.org/2025/01/13/hl7-standards-published-since-august-2024/'} |
| Sunrise Clinical Manager 3.04 workflow engine | application | Eclipsys Corp. | current | {'lifecycle_current': 'succeeded', 'notes': 'Sunrise Clinical Manager 3.04 was an Eclipsys-era product. Eclipsys was acquired by Allscripts in 2010, and then Altera Digital Health took over Sunrise in 2022. Current version is Sunrise 25.1 (2026). The specific 3.04 workflow engine is succeeded by many subsequent versions.', 'source': 'https://www.alterahealth.com/solution/sunrise/'} |

### Observation Summary

- Total observations: 21
- By type: benchmark-result: 17, expert-opinion: 1, product-evaluation: 1, viability-prediction: 1, actual-outcome: 1
