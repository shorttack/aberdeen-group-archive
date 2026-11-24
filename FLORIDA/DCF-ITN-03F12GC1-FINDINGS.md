# DCF ITN 03F12GC1 — ACCESS Florida System Replacement, 2012–2013 (note first drafted November 23, 2026)

*Findings from the DCF production under request P257878-072926: the ITN v1.0 (F4863, June 22, 2012), the Response to Inquiries (F26854), Addendum 2 (F31900), the shortlist notice (F13332), and the Vendor Bid System intent-to-award notice. All are born-digital PDFs, so quotations come from the publisher's text layer, not OCR. In F26854, each vendor's question and the Department's response are attributed separately. The full batch review is at `~/Perplexity/Perplexity Memoirs/FLORIDA-update-review/batch-02-dcs-access-itn/BATCH-02-REVIEW.md`. Earlier analysis of the same production is in DCS-ANALYSIS.md and PENDING-CHANGES rows 111–119. This note adds rows 121 and 122.*

## Kastner's observation: a system with the life of a building

**Kastner firsthand analysis, November 23, 2026.** Recorded verbatim, with typing slips corrected in brackets. Responding to the finding that FLORIDA was planned to stay in service until at least May 2016, Kastner wrote:

> "Fascinating. About the life of the HVAC equipment and the building itself. So build the site, have big loading [dock] doors for the upgrades, and hire staff for a [career]."

**The point.** A statewide eligibility system has a service life on the order of a building's mechanical plant, not of a procurement. It should be planned as facility infrastructure: a site sized for decades, physical access designed for repeated hardware replacement, and a permanent technical staff hired for careers rather than rented through a series of contracts.

**What the record supports**

- **Service life.** FLORIDA was "Implemented in 1992" (F4863 p. 6). In 2012 it was still "the legacy mainframe that provides core functionality for the ACCESS Florida System" (F4863 p. 6). The replacement was to be implemented "by May 31, 2016" (F4863 p. 7). The incumbent provider was to support operations and maintenance "until the new system has been implemented and the ACCESS Florida System data has been archived or converted" (F26854 p. 17, Inquiry 127, Department response). That makes at least 24 years as planned. Whether FLORIDA actually retired then is open; see row 111's wording guard on One Model.
- **Upgrades as routine.** The main report's hardware chronology runs from the bid three-way processor to an eight-way flagship with a six-way communications machine beside it. By 2012, "Hardware is owned by the NSRC, and the Department does not control the refresh plan" (F26854 p. 7, Inquiry 54, Department response).
- **Staff rented by contract.** The main report documents:
  - Deloitte & Touche's programming-staff contract (June 1992);
  - its termination in March 1995, with about 60 percent of programmers and support staff leaving;
  - the emergency Unisys award, with a programming-support agreement from September 1995 amended thirteen times.

  In 2012, "Deloitte Consulting currently provides operations and maintenance services for the ACCESS Florida System" (F26854 p. 23, Inquiry 184, Department response). Deloitte then won the replacement (row 111).
- **The ageing plant.** "The most problematic technological issue is the underlying architecture of the FLORIDA mainframe which is inherently rigid and difficult to maintain" (F4863 p. 6). DCF also cited "an ever-increasing risk of infrastructure failure due to the age of the mainframe" (F4863 p. 51) and "on average 1 to 2 abends per day" (F26854 p. 12, Inquiry 83).
- **Contract terms against service life.** The 2012 contract was "expected to be three (3) years" (F4863 p. 8); Addendum 2 revised it to run to May 31, 2017 (F31900 p. 1). Each contract term was a small fraction of the system's service life.

**Where the evidence does not reach (inference, labeled)**

- **Data dictionary.** The FLORIDA IMS data dictionary "is dated 1/31/2001" (F26854 p. 6, Inquiry 47). An eleven-year-old dictionary is consistent with the loss of continuous in-house technical stewardship, but it does not prove staff churn.
- **Turnover figure.** The "approximately 15-16%" turnover estimate (F26854 p. 10, Inquiry 73) covers "the Department and Partners" in the context of training. That is the workforce using the system, not its programmers, so it should not be cited as IT-staff turnover.
- **HVAC comparison.** The life spans of HVAC plant and buildings are general engineering knowledge, not evidence in this archive. The comparison is Kastner's analogy and should be presented as his.

**Proposed home.** An epilogue to the main report, "What the 2012 replacement record shows," and the lessons in One Model, Forty Years. Logged as PENDING-CHANGES row 121 (P3). It is not to be propagated until the sweep.

## Documentary facts not yet in the log (row 122)

Each item below is the Department's response unless marked otherwise.

| Fact | Pinpoint |
|---|---|
| "There are currently several hundred open help desk tickets, and the maintenance priority list averages 150 total items for all systems across the environment." | F26854 p. 12, Inquiry 83 (Xerox) |
| "The current provider has not prepared benchmarks." (The question concerned the O&M scope, ITN p. 110. Any link to the 1991 benchmark/capacity tests is inference.) | F26854 p. 12, Inquiry 85 (Xerox) |
| "The performance measures listed in Appendix I, Attachment II, Exhibit A are not currently tracked." | F26854 p. 12, Inquiry 86 (Xerox) |
| "Existing transaction counts are based on a legacy architecture." (No counts were given; vendors were referred to Technical Architecture § 7.0. See row 119.) | F26854 p. 8, Inquiry 62 (Xerox) |
| The FLORIDA IMS data dictionary "is dated 1/31/2001"; the FLODS dictionary "is current". | F26854 p. 6, Inquiry 47 (Unisys) |
| Asked whether proposers could run an independent data-quality analysis of the legacy databases, the Department answered "No." | F26854 p. 6, Inquiry 48 (Unisys) |
| The ACCESS Florida System Feasibility Study by AHCA "will be completed in September 2012." (The question, from MAXIMUS, framed it as choosing between "remediation and enhancement of the State's legacy eligibility determination system or development of a new system".) | F26854 p. 22, Inquiry 173 |
| "Hardware is owned by the NSRC, and the Department does not control the refresh plan." | F26854 p. 7, Inquiry 54 (Xerox) |
| The incumbent provider supports O&M "until the new system has been implemented and the ACCESS Florida System data has been archived or converted." | F26854 p. 17, Inquiry 127 (Deloitte) |
| "Deloitte Consulting currently provides operations and maintenance services for the ACCESS Florida System. Deloitte Consulting is not precluded from bidding on ITN #03F12GC1." | F26854 p. 23, Inquiry 184 (ISF) |


## Facts from the recovered rows (row 123)

The first rebuild of the Response to Inquiries table dropped Inquiries 114–172, every row from Deloitte Consulting, because the vendor name began inside the inquiry-number column. The v2 rebuild (`rebuild_inquiry_table_v2.py`, November 23, 2026) takes row boundaries from the table's ruled lines and recovers all 184 rows. Page images confirm the rows quoted here, and every quotation used earlier in this note and in main report § 9 was rechecked against the v2 text.

| Fact | Pinpoint |
|---|---|
| "The system currently refers applications only to Florida Healthy Kids Corporation for CHIP." | F26854 p. 18, Inquiry 132 (Deloitte) |
| Asked how many workers and users need document access: "The current number of workers / users is based upon the architecture of the current environment." No number given. | F26854 p. 22, Inquiry 166 (HP Enterprise Services) |
| Xerox asked for "the remaining useful life of the hardware"; the Department referred it to Section 8 of the Technical Architecture Document. No useful-life figure given. | F26854 p. 7, Inquiry 54 (Xerox) |
| Vendor's words: "A 3-yr term would not appear to cover your expected implementation date of 5/31/16." The Department referred it to Inquiry 4, which points to Addendum 2. | F26854 p. 21, Inquiry 161 (HP); p. 1, Inquiry 4 (Northrop Grumman) |
| "Call center technology is included within the scope of ITN #03F12GC1. Call center operations are not included within the scope of ITN #03F12GC1." | F26854 p. 21, Inquiry 160 (HP) |
| "The Average Monthly Call Center Calls provided in Section 1.2 Statement of Purpose does not include calls to FHKC." So Kastner's 0.94 calls per household (row 117) is a floor, not the total (inference). | F26854 p. 22, Inquiry 174 (MAXIMUS) |


## Batch 03: addenda, shortlist and award record (row 124)

Read in the cloud on November 23, 2026: Addenda 1–15, the shortlist, the reply-opening notice and the Vendor Bid System record. All are born-digital, single-column PDFs. Most addenda only move dates in the schedule of events.

| Fact | Pinpoint |
|---|---|
| If AHCA's study found "the appropriate solution is to remediate rather than replace the ACCESS Florida System, the Department will post an addendum" calling for amended replies. No addendum of the fifteen did so. | F4863 PDF p. 5; Addenda 1–15 |
| Award posting slipped from December 4, 2012 to March 5, 2013 across Addenda 4–14; the intent to award Deloitte was posted March 8, 2013. | F7380; F11370; F12906; F21686; F14628; VBS record |
| Contract end May 31, 2017 "but will be dependent on the approach provided by the selected vendor." | F31900 p. 1 (Addendum 2, § 1.3) |
| Replies must "Describe how the solution will scale to meet Florida's transaction levels." | F4863 PDF p. 24; F31900 p. 3 |
| Replies must "Describe the skill sets, training, and technologies needed for Department staff to maintain the proposed solution." | F4863 PDF p. 24; F31900 p. 3 |
| The ACCESS Florida System is FLORIDA plus 22 named applications and subsystems (23 in all). | F4863 PDF p. 8; F31900 p. 1 |

## Sources

- Florida DCF, ITN 03F12GC1, ACCESS Florida System Replacement, v1.0, June 22, 2012 (F4863).
- Florida DCF, ITN 03F12GC1 Response to Inquiries (F26854).
- Florida DCF, ITN 03F12GC1 Addendum 2 (F31900); Notice of Shortlist (F13332); Vendor Bid System intent-to-award notice, March 8, 2013.
- Florida DCF, ITN 03F12GC1 Addenda 1 and 3–15 (F25539, F19431, F7380, F14148, F24466, F11370/F1467, F12906/F30667, F26343, F1909, F13593, F21686, F26277, F14628, F21251); Reply Opening Notice (F31660).
- Source PDFs: `~/Desktop/Memoirs/FLORIDA-documents/DCS P257878-072926/`.
