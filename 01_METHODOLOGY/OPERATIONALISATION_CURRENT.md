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
