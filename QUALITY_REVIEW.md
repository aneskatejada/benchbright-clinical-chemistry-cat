# Clinical Chemistry Question Bank — Quality Review

## Source spreadsheet

`All_Chemistry_Questions_BOC_and_Harr.xlsx`, sheet **All Chemistry Questions**. This bank contains **976** indexed entries across 23 source subsections: **356 BOC Study Guide** and **620 Harr Medical Laboratory Science Review** entries. Other workbook sheets are subsets, indexes or OCR review aids and are *not* duplicated in the exam.

| Validation category | Count | CAT status |
|---|---:|---|
| All indexed source questions | 976 | Retained in CSV |
| Structurally usable Harr questions after footers and duplicates are handled | **608** | `ready` |
| BOC entries with OCR/figure/source uncertainty | **356** | `review` |
| Harr entries with missing options, duplicated choices or repeated stem | **12** | `review` |
| **Total excluded pending review** | **368** | `review` |

**Key source defect:** Most BOC items have OCR errors and missing/misaligned A/B/C/D choices. Some BOC answer options contain text from adjacent questions. These cannot be safely used for a live exam without checking the book or scans.

**Harr cleanup:** Some option D cells included book taxonomy footers starting `Chemistry/Apply`, `Chemistry/Evaluate`, etc. Those are stripped from displayed options. The original spreadsheet should be treated as the raw source. 8 incomplete Harr items, 1 repeated-option item, and 3 duplicate stems are excluded.

**Clinical accuracy is not guaranteed.** Structural checks confirm an answer and rationale are present, not that their medical science, thresholds, conventions, or rationale are correct. A qualified reviewer should assess the bank. Source workbook reports that MLS-only flags are OCR-dependent and not uniformly present; consequently **the exam does not enforce MLS-only versus MLT-only labeling.**

## Difficulty and adaptive testing

The supplied spreadsheet has no calibrated difficulty or IRT parameters. The ready items were assigned provisional difficulty 1–5 by a reproducible, topic-relative textual complexity heuristic. They are *not* known psychometric difficulties. The site's ability estimate uses this provisional mapping and is consequently a study indicator, not a certification prediction.

On each attempt the app creates a randomized 100-topic-slot plan approximately proportional to the reviewed topic distribution. After **each** answer, it updates an EAP ability estimate and chooses a fresh question in the designated topic near the student's estimated ability. Repeated questions in one exam are prevented, and answer orders are independently randomized. Multiple runs should not use an identical 100-question set.

## Editorial and rights review before publishing

1. Correct BOC OCR choices against the original sources. Mark `status=ready` only after full item/rationale verification.
2. Review the Harr items for outdated clinical thresholds, nomenclature and assay recommendations, and confirm every keyed answer.
3. Check repeated/similar items across both textbooks to avoid inflated topic frequency once BOC items are added.
4. Gather student pilot data to calibrate item difficulty/discrimination before calling the assessment a validated CAT.
5. Confirm you have **rights to redistribute and monetize** the original questions, rationales and excerpts. A publicly hosted GitHub Pages site exposes the item bank and answer keys to visitors.
