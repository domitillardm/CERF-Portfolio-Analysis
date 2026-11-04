# CERF portfolio analysis — start here

Current 28 October 2026. All 249 activities are retained in a **final consolidated provisional** scoring dataset. There are93 defined provisional country-tracks,14 unmapped activities in 7 holding groups and 3 unresolved factual-stage cases. Source data and exact evidence/decision histories remain outside Git; authoritative paths and hashes are in [handover](handover.json).

**Read the [methodological-independence audit](05_VALIDATION/method_independence_audit_20261028.md) before interpreting method agreement.** Initial B was A-default with contextual overrides; original singleton C copied A. Multi-track C was separately authored, but independent blinded judgement is not demonstrated. D1/D2 are derived maxima.100% paired C/D agreement is descriptive consistency, not independent methodological validation.

- [Current definitions and operationalisation](01_METHODOLOGY/OPERATIONALISATION_CURRENT.md), [source-aligned codebook v0.2](01_METHODOLOGY/SCORING_CODEBOOK_DRAFT_v0.2.md), and separate [F1 conventions](01_METHODOLOGY/CALIBRATION_ADDENDUM_v0.2-F1.md).
- [Scoring/decision history and coverage](09_INTERNAL_DEEP_DIVE/scoring_and_classification_history_20261028.md).
- [Technical guide](09_INTERNAL_DEEP_DIVE/technical_and_decision_history.md), [decision register](06_DECISIONS/decision_register.csv) and [reported session log](04_ANALYSIS_LOGS/session_events.jsonl).
- [Current limitations](05_VALIDATION/issues.md) and [provisional client appendix](08_CLIENT_APPENDIX/methodology_DRAFT.md), not released for client circulation.


## Current single-workbook entry point

Use the **five-sheet consolidated supervisor workbook** identified in handover.active_review_interface: Overview, Activity scores, Country-track comparison, Review questions and Descriptives. It preserves all249 activities and the93 defined tracks, with7 holding groups separately visible. Original and blinded C are separate. The four priority post-freeze questions are ready for discussion; existing limitations are retained without creating a new broad regrading cycle. Reviewer notes are blank and do not update scores automatically. See the [current consolidation note](05_VALIDATION/supervisor_consolidation_20261028.md). The original detailed/frozen workbooks remain unchanged.

## Holistic reassessment materials prepared

The [materials protocol](01_METHODOLOGY/BLINDED_C_MATERIALS_PROTOCOL_v1.md) and [validation note](05_VALIDATION/blinded_C_preparation_20261028.md) document preparation of34 score-masked packets containing176 activities. No new judgement/comparison exists. Hand over only the assessor archive in a fresh isolated session; retain the baseline manifest separately. Current portfolio classifications remain unchanged. Paths/hashes are in handover; preparation documentation is local pending any separate publication.

## Deliverables and use

The final consolidated workbook is authoritative. The three-sheet supervisor review and six-sheet first analytical review are static projections/extensions; they do not replace or automatically update source scores. All original scores, human selections and evidence are preserved. The new audit produces no workbook or score changes; its restricted exclusion annex lists all excluded unit IDs and reasons.

| Use | Current readiness |
| --- | --- |
| Provisional descriptive analysis | Usable with scope, coverage, ordinal and shared-process caveats. No effectiveness rankings. |
| Independent scoring-method comparison | Independence not demonstrated; current agreement must be qualified. Minimum corrective protocol is proposed separately, not executed. |
| Independent case-study grade comparison | Not ready: scale/missing-code equivalence, exact track crosswalk and validation/confidence arrangements unresolved. |
| Human validation | Ready for targeted review; no invented blanket approval or broad new reassessment queue. |
| Final external reporting | Subject to designated human methodological/factual/confidentiality/release review. |

## Working safely

Follow [AGENTS](AGENTS.md) and [environment workflow](ENVIRONMENT.md). Historical setup statements (“no codebook”, “no scoring yet”) describe earlier stages, not current execution. Prior root documents, reports and decisions are retained. `handover.latest_report` identifies the latest generated audit snapshot; curated root documents above are the current narrative. Agent logs and reconstructed history are not complete prompt transcripts. Git publication contains selected privacy-reviewed text only, not confidential workbooks, exact exclusion rows or annotated scoring code. A fresh checkout does not restore private data; SharePoint remains separate and unverified.


## New: post-freeze holistic comparison

The owner-transferred frozen C assessment is now compared with original results; see the [comparison report](05_VALIDATION/post_freeze_C_comparison_20261028.md). All34 tracks/176 members reconcile. Original C agreement is30/33, D1 agreement25/28 and D2 agreement26/29; different denominators are explicit. Three numerical disagreements plus one unresolved disposition are queued for targeted human judgement, not automatic replacement. Integrity hashes pass; freeze/exposure history has documented provenance limits. The comparison is ready for supervisor discussion, with no new broad scoring exercise or main-branch merge.
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
