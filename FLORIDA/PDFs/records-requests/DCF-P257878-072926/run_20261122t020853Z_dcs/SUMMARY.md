# FLORIDA Production OCR summary -- run run_20261122t020853Z_dcs

- created: 2026-11-22T03:00:20Z  (unknown)
- host: Mac-M5.local
- operator model: unknown/unverified
- policy: references/production-ocr.md v2.1 (supersedes experimental OCR)

## Tools (recorded, not guessed)
- ocrmypdf: 17.14.2
- tesseract: tesseract 5.5.4
- poppler_pdftotext: pdftotext version 26.11.0
- poppler_pdfinfo: pdfinfo version 26.11.0
- qpdf: qpdf version 12.4.2

## Result per input
| input | status | ocr_rc | pages | qpdf | warns | after_chars | output_dir |
|---|---|---|---|---|---|---|---|
| F11370_20121113DCF13ACCESSFloridaSystemProjectITNADDENDUM7.pdf | TECHNICAL_PASS | 0 | 2 | True | 3 | 3077 | F11370_20121113DCF13ACCESSFloridaSystemProjectITNADDENDUM7_d02783d1 |
| F12906_ITN03F12GC1Addendum8.pdf | TECHNICAL_PASS | 0 | 1 | True | 1 | 2445 | F12906_ITN03F12GC1Addendum8_29f2421a |
| F13332_SHORTLISTOFVENDORS.pdf | TECHNICAL_PASS | 0 | 1 | True | 1 | 728 | F13332_SHORTLISTOFVENDORS_5f3d0b74 |
| F13593_Addendum11.pdf | TECHNICAL_PASS | 0 | 2 | True | 2 | 3279 | F13593_Addendum11_56bc7048 |
| F14148_Addendum5.pdf | TECHNICAL_PASS | 0 | 1 | True | 1 | 732 | F14148_Addendum5_f0258e97 |
| F14628_20130211DCF13ACCESSFloridaSystemReplacementITN.v.1.0Addendum14.pdf | TECHNICAL_PASS | 0 | 1 | True | 1 | 3033 | F14628_20130211DCF13ACCESSFloridaSystemReplacementITN.v.1.0Addendum14_46cadd44 |
| F1467_20121113DCF13ACCESSFloridaSystemProjectITNADDENDUM7.pdf | TECHNICAL_PASS | 0 | 2 | True | 3 | 3077 | F1467_20121113DCF13ACCESSFloridaSystemProjectITNADDENDUM7_17190594 |
| F1909_Addendum10.pdf | TECHNICAL_PASS | 0 | 2 | True | 2 | 3278 | F1909_Addendum10_0a6a25e1 |
| F19431_ITN03F12GC1Addendum3.pdf | TECHNICAL_PASS | 0 | 1 | True | 2 | 3635 | F19431_ITN03F12GC1Addendum3_3e761eab |
| F21251_20130211DCF13ACCESSFloridaSystemReplacementITN.v.1.0Addendum15.pdf | TECHNICAL_PASS | 0 | 1 | True | 1 | 3191 | F21251_20130211DCF13ACCESSFloridaSystemReplacementITN.v.1.0Addendum15_06343775 |
| F21686_20130206DCF13ACCESSFloridaSystemProjectITNADDENDUM12.pdf | TECHNICAL_PASS | 0 | 2 | True | 2 | 3253 | F21686_20130206DCF13ACCESSFloridaSystemProjectITNADDENDUM12_c2033839 |
| F24466_F19431_ITN03F12GC1Addendum6.pdf | TECHNICAL_PASS | 0 | 1 | True | 1 | 2453 | F24466_F19431_ITN03F12GC1Addendum6_e82d4b44 |
| F25539_ITN03F12GC1Addendum1UpdatetoScheduleofEventsandDeadlines.pdf | TECHNICAL_PASS | 0 | 1 | True | 2 | 2443 | F25539_ITN03F12GC1Addendum1UpdatetoScheduleofEventsandDeadlines_3da53bc2 |
| F26277_20130211DCF13ACCESSFloridaSystemReplacementITN.v.1.0Addendum13.pdf | TECHNICAL_PASS | 0 | 1 | True | 2 | 2936 | F26277_20130211DCF13ACCESSFloridaSystemReplacementITN.v.1.0Addendum13_a95b9288 |
| F26343_Addendum9.pdf | TECHNICAL_PASS | 0 | 2 | True | 2 | 3260 | F26343_Addendum9_6fa59cf5 |
| F26854_ITN03F12GC1ResponsetoInquiries.pdf | TECHNICAL_PASS | 0 | 23 | True | 23 | 91190 | F26854_ITN03F12GC1ResponsetoInquiries_028ea176 |
| F30667_ACCESSFloridaReplacementITNv10Addendum8.pdf | TECHNICAL_PASS | 0 | 1 | True | 1 | 2445 | F30667_ACCESSFloridaReplacementITNv10Addendum8_68c41899 |
| F31660_ReplyOpeningNoticeVBSv2.pdf | TECHNICAL_PASS | 0 | 1 | True | 1 | 793 | F31660_ReplyOpeningNoticeVBSv2_3bf0bb65 |
| F31900_ITN03F12GC1Addendum2.pdf | TECHNICAL_PASS | 0 | 8 | True | 9 | 31119 | F31900_ITN03F12GC1Addendum2_4c80815c |
| F4863_20120622DCF10ACCESSFloridaReplacementITNv1.0.pdf | TECHNICAL_PASS | 0 | 147 | True | 147 | 487944 | F4863_20120622DCF10ACCESSFloridaReplacementITNv1.0_a2617288 |
| F7380_ITN03F12GC1Addendum4.pdf | TECHNICAL_PASS | 0 | 2 | True | 2 | 6147 | F7380_ITN03F12GC1Addendum4_01f3ee9e |
| VBS Advertisement - Intent to award.pdf | TECHNICAL_PASS | 0 | 4 | True | 4 | 8981 | VBS Advertisement - Intent to award_ddde5069 |

## Counts (recomputed from rows, not asserted)
- TECHNICAL_PASS: 22
- REVIEW_REQUIRED: 0
- FAILED: 0


## No-false-completion caveat
- TECHNICAL_PASS means the structural checks passed. It is NOT citation verification and does NOT promise error-free OCR.
- Sidecars exclude pages that already carried text (--skip-text); .md/.layout.md are the canonical extractions, neither is guaranteed reading order.
- Missing artifacts or unresolved flags are reported, not papered over. No inputs were moved; canonical state untouched.
