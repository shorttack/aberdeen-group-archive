# Formulas for Disaster Recovery Scenario

> Archived from: 14-Formulas-Disaster-Scenario.txt
> Original publication date: 2003-01-01
> Author: Aberdeen Group

---

## Original Document Text



Formulas for disaster scenario

These are similar to the downtime scenario.

Benefits = (admin. cost savings from New solution) + (additional revenue from New solution) + (opportunity cost savings) [optionally, plus difference in acquisition costs between Old Way and New Way]

Acquisition cost (Old way) = cost/GB (online disk) * (# GB online disk) + ditto (nearline tape) + ditto (offline tape)
Acquisition cost (New way) = cost/GB (online disk * (# GB online disk) + ditto (midline disk) + ditto (nearline disk) + ditto (nearline tape) plus ditto (offline tape)

Constraints:
# GB online disk (New Way) + # GB midline disk (New Way) = # GB online disk (Old Way)
# GB nearline disk (New Way) + # GB nearline tape (New Way) = # GB nearline tape (Old Way)
[Note:  this is to equalize the comparison between the two Ways]
# GB online disk (Old Way) <= # GB nearline tape (Old Way)
# GB nearline tape (Old Way) <= # GB offline tape (Old Way)
# GB online disk (New Way) <= # GB nearline disk (New Way)
# GB midline disk (New Way <= # GB nearline tape (New Way)
# GB nearline disk (New Way) + # GB nearline tape (New Way) <= # GB offline tape (New Way)

Opportunity cost savings = (arbitrarily) 0.6 * savings from New solution

    1. Savings 2 = customers served (in backup time saved) * $/customer + administrative costs saved (in backup time saved)

Administrative cost savings = $100K salary * (1/10,000 hours per year) [= $10/hour]* (recovery time saved)
For example, if the New Solution saves recovery time of 5 hours, administrative cost savings are $10/hour * 5 hours or $50.

Recovery time saved = (# GB recovered/rate of backup [d/t] (Old Way) - (# of GB recovered/rate of backup [max, d/d or d/t] (New Way)

GB recovered (Old Way) = amount on online disk (Old Way, Stage 1) = online disk capacity (Old Way) * online disk % full (Old Way, Stage 1)
GB recovered (New Way) = GB recovered (Old Way) = online disk capacity (New Way) * online disk % full (New Way, Stage 1) + midline disk capacity (New Way) * midline disk % full (New Way, Stage 1)

This leads to an additional constraint:
Amount on online disk (New Way, Stage 1) + amount on midline disk (New Way, Stage 1) = amount on online disk (Old Way, Stage 1), where
Amount on disk/tape = disk/tape capacity * disk/tape % full (Stage 1)
Note:  we may also want to add a constraint that amount on online disk (New Way) = amount on midline disk (New Way) - for a kind of load balancing.

Back to the formulas:
Downtime = Outage Time + Recovery Time.   Assume a one-minute electrical disruption followed by 5 minutes for the servers and storage to boot back to a state where Recovery can begin.  The Outage Time is a constant of six minutes, affecting both old and new scenarios equally, but we may want to tweak it.

Recovery time (Old Way) = amount on online disk (Old Way, Stage 1)/rate of recovery disk/tape [=800 GB/hour]

Finally, the nasty part of figuring out the recovery time for the New Way:
Recovery time (New Way) = max (recovery time [disk/disk, New Way], recovery time [disk/tape, New Way])
Recovery time (disk/disk, New Way) = amount on online disk (New Way, Stage 1)/rate of backup disk/disk [= 1600 GB/hour]
Recovery time (disk/tape, New Way) = amount on midline disk (New Way, Stage 1)/rate of recovery disk/tape [=800 GB/hour]

Note that the Stages of the scenario change depending on whether disk/disk or disk/tape recovery is fastest in the New Way, and there are cases where they finish at the same time; the New Way is always faster than the Old Way.

To repeat:
Rate of recovery disk/tape = 800 GB/hr.
Rate of recovery disk/disk = 1600 GB/hr.

Also, note that in the New Way we do backup in parallel (online to nearline disk, midline to nearline tape)

If you're curious, the absolute minimum recovery time of the New Way is 1/3 the Old Way, and in that case amount on online disk (Stage 1) = 2 x amount on midline disk (Stage 1)

This brings up the issue of clock time.  Assume that recovery time (disk/tape, New Way) is greater than recovery time (disk/disk, New Way).  Then:

Clock time (Stage 1 and Stage 2) are TBD.
Clock time (Stage 3) = recovery time (disk/disk, New Way)
Clock time (Stage 4) = recovery time (disk/tape, New Way) - recovery time (disk/disk, New Way)
Clock time (Stage 5) = recovery time (Old Way) - recovery time (New Way) [which is between ½ and 2/3 of recovery time (Old Way)].

Now, back to the benefits calculation
Additional revenue for New Solution = custs served/hour * $/customer * recovery time saved

Numbers for Downtime Example
We will assume a medium/large online book/CD seller primarily selling in the U.S. (or Germany, or whatever) which looks a lot like Amazon.com. The crash and recovery occurs during peak business hours, when 50,000 customers will place orders each hour, each with a $20 30 order.  This represents $1,500,000 in revenue per hour lost.  The numbers are:
Custs served/hour = 50,000
$/customer = $2030

If the customer uses nearline tape the old way, the street price for the tape library is $130,000 for an 8 tape drive, 200 slot system of LTO-2 drives (400 MB/cartridge and 40 MB/sec at 2 to 1 compression).  The media cost $100 per cartridge so the total cost is $20,000 for the media so the total cost is $150,000.  The total capacity is 80 TB so the dollars per GB is $1.90/GB.

A nearline disk and nearline tape combination appliance would cost the following:
20TB of nearline disk would go for $100,000 so the dollars per GB is $5/GB.  However, a smaller tape library would be required.  Only a 4 drive system with 100 slots would be necessary.  This would cost $85,000 street price with $10,000 of media cost for a total of $95,000.  The capacity of the tape library would be 40 TB and the dollars per GB would be $2.50/GB.  The overall price for the solution would be $195,000.

$/GB
Online Disk $31.60 $/GB (HDS  9980V with 146GB disks) (High End) (use this number)
Online Disk $13.30 $/GB (EMC CX600 with 146 GB disks) (Midrange)
Midline Disk  $9.30 $/GB (70% of EMC)

Rate of recovery disk/tape = X GB/hr.  X = 800 GB/hr.
Rate of recovery disk/disk = Y GB/hr.   Y= 1600 GB/hr.

Other values as before (I don't have the records of what that was, except 1/3, 1/3, 1/3 structured/semi-/unstructured data).

Note:  all structured data has priority on online disk (New Way), followed by semi-structured.  Therefore, 

Structured data (online disk) = % structured * (total online/midline amount)
Semi-structured data (online disk) = minimum{[total online amount - structured data (online disk)], % semi-structured * (total online/midline amount)}
Etc.




---

## Frictionless Data Package Metadata

> Auto-generated by Archival Ingest Skill v16

### Study Record

| Field | Value |
|-------|-------|
| study_id | 14-formulas-disaster-scenario-c2f0b4 |
| title | Formulas for Disaster Recovery Scenario |
| author | Aberdeen Group |
| date | 2003-01-01 |
| type | case-analysis |
| subject_domain | enterprise-storage |
| methodology | financial-modeling, disaster-recovery, tco-analysis |
| source_file | 14-Formulas-Disaster-Scenario.txt |
| license | CC-BY-4.0 |

### Abstract

Companion document to the downtime strategy formulas, applying similar financial modeling to disaster recovery scenarios. Defines a multi-stage recovery time model comparing old tape-based architecture to a new midline disk hybrid. Uses an online book/CD seller scenario (modeled on Amazon.com) with 50,000 customers/hour at $20-30/order to quantify revenue impact of improved recovery time. Models parallel disk/disk and disk/tape recovery paths to show New Way always recovers faster than Old Way, with minimum recovery time at 1/3 of Old Way.

### Document Assessment

| Dimension | Rating | Rationale |
|-----------|--------|-----------|
| **Importance** | high | Companion financial model to study 13; together these documents represent the complete TCO toolkit developed by Aberdeen for the Maxtor midline category launch. Historical benchmark for enterprise disaster recovery economics in the early SAN era. |
| **Relevance** | high | Multi-stage disaster recovery time model with parallel recovery paths is directly applicable to modern hybrid cloud architectures; the formula structure (downtime = outage time + recovery time; parallel recovery advantages) is still valid for evaluating object storage vs block storage recovery. |
| **Prescience** | high | Predicted parallel recovery always outperforms single-path tape recovery; confirmed by industry adoption of disk-to-disk backup and cloud-based disaster recovery. Minimum recovery time at 1/3 of Old Way proved accurate as disk/disk became standard primary DR mechanism. |

### Prescience Detail

This study did not make forward-looking claims.

### Entities Referenced (5)

| Entity | Type | Status | Successor |
|--------|------|--------|-----------|
| Aberdeen Group | firm | acquired | Aberdeen/Harte-Hanks |
| David Hill | person | [DEFERRED] |  |
| EMC Corporation | company | acquired | Dell |
| Hitachi Data Systems | company | [DEFERRED] | Western Digital |
| Amazon.com | company | active |  |

### Technologies Referenced (5)

| Technology | Category | Vendor | Lifecycle (at study) | Lifecycle (current) |
|------------|----------|--------|---------------------|---------------------|
| Midline Storage | platform | Maxtor | emerging | legacy |
| LTO (Linear Tape Open) | storage | Various | growing | active |
| Fibre Channel (FC) | protocol | Various | mature | active |
| HDS StorageWorks 9980V | storage | Hitachi Data Systems | current | legacy |
| EMC CLARiiON CX600 | storage | EMC | current | legacy |

### Observation Summary

- Total observations: 20
- By type: financial-model: 5, benchmark-pricing: 5, performance-model: 3, analytical-finding: 2, benchmark: 2, constraint: 1, use-case: 1, multi-stage-model: 1
