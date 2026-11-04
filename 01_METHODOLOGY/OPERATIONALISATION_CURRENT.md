# Current scoring operationalisation — provisional

Status 28 October 2026. Read with the unchanged Inception-aligned [codebook v0.2](SCORING_CODEBOOK_DRAFT_v0.2.md), [F1 application conventions](CALIBRATION_ADDENDUM_v0.2-F1.md) and [implementation audit](../05_VALIDATION/method_independence_audit_20261028.md). The owner selected the source basis and authorised execution; this is not formal approval of every judgement or extension. The full Inception Report/model-call archive is not available; the source table was supplied as a visible Appendix B screenshot.

## Classification and evidence

| Code | Meaning | Required monitoring claim |
| --- | --- | --- |
|1|Activity described|Text describes what CERF did; do not infer a completed output.|
|2|Output delivered|A distinct completed product/service/deliverable is reported.|
|3|Concrete use/follow-up|Another identifiable actor used the output or took a documented step.|
|4|External actor change reported|Policy, behaviour, practice, capacity, cooperation, finance or market change is described.|
|6|Insufficient information|Text too vague to support1–4; not an ordinal result above4.|

Use the highest text-supported achieved level. Plans/intentions and future potential remain separate Yes/No fields; missing achievement is not automatically6. Settled no-achieved and cancelled statuses remain distinct from genuinely unresolved classifications. Preserve original dates and uncertain precision. Monitoring reports are not independently verified outcomes. Evidence strength, classification confidence, future potential, rationale, source IDs and human-review state are separate fields.

Reported learning/cooperation can support4; no new requirement for independent verification, quantified effect, enacted law or structurally transformed practice is added. A generic indicator, attendance or enthusiasm alone does not establish a recipient change. Read actual actor roles, completion status and focal relevance. Plans, drafted/submitted/published/adopted/implemented stages are not interchangeable.

## Outputs, intended unit and actual implementation

| Output | Intended scope | Actual historical operationalisation / limit |
| --- | --- | --- |
|A|Focal activity's own monitoring only|Own-record annotations with later A freeze; previous pilot exposure acknowledged. Old human/AI fields excluded from evidence projection, not an erased conversation history.|
|B|Activity assessed within its full chronological track, including later records with focal links|Initially copies A by default and changes explicit contextual cases; singleton evidence is identical. Incremental review, not demonstrated blinded rederivation. Context can in principle lower a result; the original default searched for higher results.|
|C|One holistic classification from combined track monitoring|Separate authored multi-track table; initial singleton C explicitly copies A. Later scoped C journals exist. C is not universally computed from D, but independent holistic judgement is not established.|
|D1|Maximum eligible A for a country-track|Deterministic calculation; inherits A, membership and missingness limits.|
|D2|Maximum eligible B for a country-track|Deterministic calculation; inherits B, membership and missingness limits.|

A/B are activity observations. C/D1/D2 are country-track observations and must be counted once per defined unit even when repeated on activity rows. There are five output columns and four conceptual families (activity standalone, activity contextual, holistic track, maximum-based track); D1 and D2 are two versions of a derived summary, not independent assessments.

## Scope and maxima

Keep immutable original IDs and all source classifications; store effective provisional results and decisions separately. Membership must be defensible. Current units use accepted historical choices, nine case/whitespace aliases with lineage and two explicitly named programme placements, all source-specific and not a verified census of official programmes. Fourteen unmapped activities in seven holding groups remain unassigned. Do not merge differently worded labels by theme.

For each defined track and approach: exclude only the existing two cancelled rows from maximum eligibility. Among eligible numerical results, rank1–4 only. If every eligible code is6, retain information status 6, not a fabricated achieved level. If any eligible result remains nonnumeric, preserve the source's incomplete maximum and separately show its known lower bound; do not silently substitute that bound, even when it is4. No eligible rows means explicit no-result status, not0. Preserve ties and supporting IDs. These provisional D summaries are not the historical CERF-M001 proposal for a highest **human-checked** score; no blanket human checking is claimed.

## Interpretation and reproducibility

Code 6 and nonnumeric statuses are excluded from ordinal comparisons/means with clear denominators. Track counts exclude unresolved holding groups. Country means are exploratory ordinal descriptions, not precise effectiveness measures or rankings. Agreement may be structurally expected under the same highest-level scale and shared evidence; it is not a validation criterion. Read the independence audit before any method-equivalence claim.

Frozen workbooks, score registers, monitoring projections, annotation tables, restricted code and source hashes are indexed in handover and the protected manifest. They remain outside Git. Repository documentation and technical checks support traceability, not a complete public rerun of confidential scoring. Technical checks are distinct from evidence validity, human adjudication and final release.


## New post-freeze comparison evidence — 28 October 2026

The owner has supplied a separately frozen, score-masked C assessment for34 multi-activity tracks;33 numerical results and1 unresolved disposition are verified against the prepared inputs. The [post-freeze report](../05_VALIDATION/post_freeze_C_comparison_20261028.md) records30/33 agreement with original C,25/28 with D1 and26/29 with D2. Three numerical disagreements are downward; one status remains unresolved. Common-denominator rates are identical25/28. File/input integrity is verified; input isolation and freeze-before-reveal are documented assessor/user declarations without an independently signed access chronology. Neither output is a gold standard. No original or frozen score has changed. This is new evidence about an additional assessment, not a retraction of findings about original construction. Targeted four-case human adjudication is recommended before final classifications/bias claims; no broad rescoring is initiated.


## Current supervisor interface — 28 October 2026

A [single five-sheet workbook](../05_VALIDATION/supervisor_consolidation_20261028.md) now brings activity A/B, unique-track original C/D1/D2 and separate frozen C together for review. It changes no classifications, membership or evidence rules. All249 activities,93 defined units and7 clearly separate holding groups are reconciled. The four primary post-freeze questions are distinct from17 old source limitations,2 earlier diagnostics and3 readiness conditions. Blank reviewer notes have no automatic scoring effect. Descriptives count tracks once and expose valid/result-status denominators; they are not effectiveness rankings. Source/frozen files and detailed histories remain external to Git. This is the current review entry point, not a new authoritative scoring version or human approval.
# Current operationalisation

**4 November 2026 — CERF-FULL-20261104-W2.** Read [current rules](scoring_rules.md) first. This document applies the unchanged Inception-aligned definitions to the corrected 182-record universe. It replaces the older 249-record workflow as the current handover entry point; historical outputs and branch history remain intact.

## Inputs and mapping

The authoritative input is `AU-CORRECTED-20261104-001`, with 28 target variables and persistent Activity Codes. The source-to-target reference remains `CERF Restructuring (1).xlsx`, particularly Overview of variables, Field availability and Activity Universe Descriptions. Worksheet-specific adaptations address layout differences, not variable meanings. The reviewed evidence matrix is `MATRIX-FULL-20261104-01`. Exact locators and hashes are in the [restricted-file manifest](../02_ACTIVITY_DATA/restricted_manifest_20261104_v1.json).

Reported results and implementation often provide direct achievement evidence. Follow-up, lessons, actors and pathway fields may contain explicit achievements too. Goals, titles and indicator selections provide context unless their text itself reports an achieved result. Apply the same substantive tests regardless of column, country or monitoring period. Record planned, ongoing and completed status faithfully; no outcome inference or cross-activity transfer is allowed.

GREEN means direct extraction; ORANGE means explicit alternative-field recovery; RED is only external supplementary information (none collected in this run); MISSING represents Unknown values; CONTROLLED METADATA marks generated identifiers and confirmed metadata. These extraction categories are not evidence quality. Unknown source-derived information stays Unknown; later analytical fields in the Activity Universe remain blank. Scoring lives in separate versioned outputs.

## Activity review and scoring

Read the complete focal record, including comments and substantive qualifications. Use the highest directly supported achieved level 1–4; reserve 6 for information too vague to establish any level. A delivered advisory/training/facilitation service can support 2 without a commissioning-document requirement. Another actor's actual use or next step can support 3; intended usefulness cannot. Reported capacity or cooperation change can support 4 without enacted law or structural reform. Material actor, unit or claim conflicts stay unscored with alternatives and a supported minimum where defensible. Missing track membership alone is not a scoring gate.

Every proposal retains exact focal excerpts and original cell/comment references, variable, extraction route, Evidence Basis, reason, Future Potential, review flag and version. The four Evidence Basis labels in [current rules](scoring_rules.md) are working categories, not Inception-prescribed weights. Human review fields remain separate and blank until a reviewer acts. Historical scores are not an answer key.

## Track summaries and unresolved scope

Current output contains 51 exact source-code groups, 10 complete provisional numerical maxima and 41 pending groups. Another 36 memberships are unassigned and listed separately. These numbers are current working units, not a verified official country-track census. Use eligible accepted members and achievement 1–4 only; preserve all ties and conditional known-score lower bounds. All-6 means insufficient information; null scores and unresolved scope cannot disappear from denominators. Reviewer edits in static Excel do not recalculate maxima: save a new version and rerun the controlled calculation.

The approved reconstruction consolidates matched Nigeria versions while retaining differences in provenance, keeps regional records once without country duplication, retains conservative uncertain dates, and preserves possible duplicates and eligibility candidates for review. No new membership or scope decisions were made by scoring or this documentation update.

## Reproducibility and limits

Full provisional scoring is actually completed, not merely authorised. Coverage, focal quotation checks, mapping integrity, maxima/ties and original-input hashes passed. A relocated private replay reproduced the frozen judgement outputs with 138 matching input/snapshot hashes. The scripts replay recorded agent judgements; they do not recreate an independent human assessment. The targeted second pass was an agent consistency review, not inter-rater reliability or outcome verification.

The full Inception Report and separate final evidence-standardisation one-pager remain unavailable. A one-page Word methodology summary was recently prepared for review, but is not a final replacement for that missing document. The prior 249-record contextual/holistic approach, historic reviewer decisions and score sets have no verified crosswalk to the new IDs. Do not transplant them. See [status and limitations](../05_VALIDATION/project_state_20261104.md) and [history](../09_INTERNAL_DEEP_DIVE/technical_and_decision_history.md).
