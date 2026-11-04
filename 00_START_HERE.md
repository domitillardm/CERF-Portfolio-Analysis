# CERF portfolio analysis — start here

**Current at 4 November 2026: full provisional scoring of the corrected 182-activity universe is complete. Technical validation passed; human score validation is pending.**

## Purpose

The Climate and Energy Response Facility (CERF) portfolio analysis supports the End-Term Evaluation with breadth across activities and country-tracks. It classifies reported achievements and preserves possible result pathways, evidence gaps and qualifications for review alongside case studies, interviews and surveys. Monitoring claims do not establish programme effectiveness or CERF causality.

## What is complete and what needs review

| Component | Verified current status |
| --- | --- |
| Activity Universe | 182 activities, 28 agreed columns, permanent identifiers and cell-level provenance; corrected reconstruction and evidence recovery checks passed. |
| Calibration | Revised 20-activity calibration approved by the owner as the working basis for full provisional scoring. Six material cases remain held. |
| Full scoring | All 182 records assessed: 126 achievement classifications, two code-6 information statuses and 54 unscored cases. No completed human-validation decisions are recorded in this run. |
| Country-track summary | 51 exact source-code groups: 10 provisional numerical maxima, 41 pending; 36 activity memberships remain unassigned separately. These groups are not a verified census of official programmes. |
| Quality checks | 525 exact focal-record excerpts verified; identifiers and prior inputs preserved; maxima/ties checked; relocated reproduction passed. Targeted agent checks are not independent human validation. |

## Current files and access

Confidential workbooks and evidence are **outside Git**. The versioned [restricted-file manifest](02_ACTIVITY_DATA/restricted_manifest_20261104_v1.json) gives safe references, exact local locators and SHA-256 hashes. Ask the project owner for an approved internal transfer and confirm access; cloning this repository does not retrieve these files.

| Use | Current file reference |
| --- | --- |
| Corrected Activity Universe and provenance | `AU-CORRECTED-20261104-001`; `AU-PROVENANCE-20261104-001` |
| Full provisional scoring workbook | `SCORING-FULL-20261104-01` |
| Human review register and track summary | `REVIEW-FULL-20261104-01`; `TRACKS-FULL-20261104-01` |
| Evidence, mapping and working rules | `EVIDENCE-FULL-20261104-01`; `MATRIX-FULL-20261104-01`; `AU-MAPPING-20261104-001`; `RULES-FULL-20261104-W2` |
| Validation and internal reproduction | `REPORT-FULL-20261104-01`; `QA-FULL-20261104-01`; `QA-REPLAY-20261104-01`; `REPRO-FULL-20261104-01` |

## How scoring works

Use the highest directly supported achieved level in the **focal activity's own record**: **1** activity described; **2** output delivered; **3** concrete use or follow-up reported; **4** change in an external actor reported. **6 means insufficient information, never an achievement above 4.** Materially unresolved classifications stay unscored with a review question and supported lower bound where defensible. An unresolved track does not automatically block an activity score.

Future Potential is a separate Yes/No classification, with uncertainty recorded separately. Evidence Basis is also separate; a named source is not independent corroboration. GREEN/ORANGE identify direct extraction/alternative-field recovery, not evidence strength. Equivalent evidence is treated consistently across monitoring layouts.

Country-track summaries take the maximum supported achievement **1–4** among eligible accepted members. Code 6 is excluded from the numerical maximum. Incomplete groups remain pending with known-score lower bounds, supporting codes and ties; an all-6 eligible group means insufficient information. No contextualised activity or holistic track scoring is current.

Read [current scoring rules](01_METHODOLOGY/scoring_rules.md) and [operational guidance](01_METHODOLOGY/OPERATIONALISATION_CURRENT.md). The unchanged [codebook v0.2](01_METHODOLOGY/SCORING_CODEBOOK_DRAFT_v0.2.md) and [F1 conventions](01_METHODOLOGY/CALIBRATION_ADDENDUM_v0.2-F1.md) retain historical proposals; only compatible conventions and the latest owner decisions apply. The separate final evidence-standardisation one-pager remains **pending**; the recent Word summary is a review draft, not that missing authority.

## What the colleague should do next

1. Obtain the current restricted files and preserve the baseline. Read the validation report and current rules.
2. Start with the 25 P1 review entries, then other material ambiguities and the 54 unscored records. The 147 review rows include group controls as well as activity questions, not 147 separate scoring errors.
3. Record human decisions, source evidence, rationale, reviewer and date separately from AI proposals. Resolve relevant membership, eligibility and duplicate cases before settling pending maxima. Three out-of-universe eligibility candidates remain excluded pending review.
4. Save a new version and rerun the controlled maxima calculation; reviewer edits in static workbooks do not recalculate automatically. Confirm coverage and denominators before preparing evaluation outputs.
5. Obtain human approval before treating scores as validated or using them for final evaluation conclusions.

For detail: [project handbook](01_METHODOLOGY/PROJECT_EXPLAINED.md), [outstanding issues](05_VALIDATION/issues.md), [verified status and limits](05_VALIDATION/project_state_20261104.md), [technical history](09_INTERNAL_DEEP_DIVE/technical_and_decision_history.md), [decision register](06_DECISIONS/decision_register.csv) and [machine-readable handover](handover.json). The older 249-record A/B/C/D workflow is historical and has no verified crosswalk to these 182 IDs. Do not combine their counts or scores.
