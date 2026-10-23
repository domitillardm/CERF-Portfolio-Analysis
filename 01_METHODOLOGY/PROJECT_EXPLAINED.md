# CERF portfolio analysis — project handbook

Updated 2026-10-23 from project-owner instructions. This is a documentation proposal
for review, not approval of a scoring framework. Unknown facts remain explicit.

## Programme and evaluation purpose

The Climate and Energy Response Facility (CERF) supported climate and energy
initiatives in partner countries through policy advice, technical assistance,
studies, workshops, missions and partnership development.

The End-Term Evaluation (ETE) assesses programme implementation and reported
results. Portfolio analysis provides breadth across CERF activities and tracks,
complementing deeper evidence from case studies, interviews and surveys.

The portfolio analysis aims to identify reported activities, outputs, follow-up
and possible outcomes; reconstruct possible pathways from activities to results;
assess the quality, completeness and traceability of monitoring evidence; identify
recurring mechanisms, constraints, lessons and gaps; and generate provisional
findings and hypotheses for the wider evaluation.

This context is supplied by the project owner. The Inception Report, programme
source documents, exact evaluation period, country/track list, portfolio coverage
and formal evaluation-question references have not yet been linked here.

## Working research questions

The following questions operationalise the owner's aims for documentation review;
their wording and mapping to the Inception Report await human confirmation:

1. What activities, outputs, follow-up and possible outcomes are reported across
   the portfolio and within each country-track combination?
2. What possible activity-to-result pathways can be reconstructed chronologically,
   and which links are supported by monitoring evidence or remain uncertain?
3. How complete, traceable and informative is the monitoring evidence for each
   classification, and where are evidence gaps?
4. Which mechanisms, constraints and lessons recur across tracks and countries?
5. Which provisional findings and hypotheses warrant examination through the
   wider evaluation's case studies, interviews and surveys?

## Analytical structure and interpretive limits

CERF tracks are the main analytical unit. Activities provide supporting evidence;
they are not independent measures of programme success. Organise activity records
by country, track and chronological order to support country-track narratives and
analysis. Track definitions, country-track identifiers, activity-to-track mapping,
date fields, multi-track attribution and treatment of unknown dates still need
confirmation. Do not invent missing identifiers or dates.

Keep achieved results separate from future potential, and result classification
separate from evidence strength. Reported outcomes are monitoring claims, not
independently verified findings. A classification rationale is not independent
evidence. Missing information must remain missing; it is not proof of no results.
Portfolio frequencies must not be interpreted as programme success rates.

Chronology can support a possible pathway, but does not establish causation or
CERF attribution. Coverage and reporting differences may affect patterns;
their extent cannot be assessed until source coverage is documented. Confidence
in classifications must be established before comparison with independent
case-study evidence. The review method and acceptance criteria for confidence
are still to be agreed; no numerical thresholds or validated confidence values
are currently supplied.

## Stages and evidence status

| Stage | Current status | Evidence or dependency |
| --- | --- | --- |
| Data preparation and anonymisation | Completed outside this repository according to the owner; not independently validated here | Source versions, preparation records, anonymisation checks and validation records must be linked |
| Operational audit environment | Implemented; prior synthetic tests reported passed | `ENVIRONMENT.md`, setup validation and repository scripts; these do not validate CERF results |
| Existing AI scoring | Existing scores are referenced by the owner; their file/version and review status are not linked | Preserve originals; do not assume scores are reviewed or validated |
| Grading-instruction improvement | Current priority; substantive review not yet evidenced in this repository | Obtain existing prompts/rules and the Inception Report scoring table |
| Country-track analysis | Current priority; planned implementation | Confirm grouping, chronology, mappings and summary approach |
| Revised definitions and pilot | Planned, pending source review and human approval | No scoring-rule revisions or grading performed in this documentation session |
| Human validation and confidence | Planned; protocol and reviewers unconfirmed | Agree independent review, disagreement/adjudication and confidence criteria |
| Wider-evaluation comparison and synthesis | Planned after classification confidence is established | Independent case-study evidence and comparison protocol not linked |
| Client methodological appendix | Existing unapproved scaffold | Requires approved method, actual validation evidence and human release review |

## Scoring and human-review workflow

1. Establish the authoritative anonymised dataset, existing-score baseline,
   provenance, immutable activity IDs, country/track mapping and chronology.
   Identify the responsible owner and designated human reviewers.
2. Retrieve the existing prompts and grading rules and the exact Inception Report
   scoring table (version and page/table reference). Review ambiguities before
   drafting revised definitions. Do not reconstruct the table from memory.
3. Propose revised instructions separately with a version, rationale, source
   references and approval status. `scoring_rules.md` has no approved framework;
   it is unchanged by this documentation update. Methodological changes require
   human approval before operational use.
4. After approval and authorisation to run a pilot, use reviewed code and the audit
   wrapper with declared input/output paths and rules version. Log experiments,
   unsuccessful attempts and corrections as well as successful runs.
5. Preserve existing AI scores unchanged. Record proposed revised scores in a
   separate versioned output/register linked to original activity IDs and baseline
   versions. Retain original, proposed and human-final scores as distinct records;
   do not overwrite one with another. Exact revised-output schema is pending.
6. Record evidence pointers, classification, evidence strength and uncertainty
   separately; keep reviewer, correction, adjudication and review status traceable.
   Codex proposes classifications; humans decide final scores. Missing-evidence
   codes and evidence-strength categories must be specified by approved rules.
7. Establish confidence using the agreed review protocol before comparison with
   independent case-study evidence. Document disagreements and limitations.
8. Produce country-track narratives and track-level synthesis using a confirmed
   summary method; preserve activity-level traceability and achieved/potential
   distinctions. No country-track aggregation rule is approved here.

## Outstanding proposal and approvals

The owner reports a meeting proposal to use the **highest human-checked activity
score within each country-track combination**. It is recorded as `CERF-M001` in
`06_DECISIONS/decision_register.csv`, with status `provisional` and no approver.
The meeting date, minutes and participants are not supplied. It must not be used
as an approved method.

Before a human decision, clarify which score dimension is summarised, what
human-checked means, eligible activities, absent reviews, missing scores, ties,
chronology, achieved results versus future potential, and how evidence strength
will accompany the summary. A maximum could foreground one activity and obscure
variation; this is a methodological concern to review, not an observed finding.
Any comparison with alternative summaries or sensitivity analysis requires an
agreed plan and a recorded decision. No alternative method is adopted here.

Other outstanding confirmations: exact Inception Report definitions and rules
version; prompts and model/configuration records; activity/country/track mapping;
evidence and missing-data conventions; human-review protocol, confidence criteria
and adjudication; reviewer identities and approval authority; and release scope.

## Expected deliverables and immediate next actions

Expected deliverables, subject to scope confirmation: a traceable portfolio
inventory; reviewed grading instructions derived from the Inception Report;
separate original/proposed/human-final scoring records; country-track evidence
narratives and track synthesis; validation and decision records; provisional
findings/hypotheses for the ETE; and a reviewed methodological appendix. No
substantive deliverable is currently validated in this repository.

Next, obtain secure references and versions for the prepared dataset, preparation
validation records, existing scores/prompts/rules and Inception Report. Confirm
country-track structure, reviewers and approvals; then prepare an instruction
revision and review plan. Do not begin grading or overwrite existing scores.

## Navigation and reproducibility

Read `AGENTS.md`, `handover.json`, `05_VALIDATION/issues.md` and the decision
register. `09_INTERNAL_DEEP_DIVE/technical_and_decision_history.md` is the stable
internal guide. `handover.json.latest_report` locates the latest generated status,
audit history and unapproved client draft. `04_ANALYSIS_LOGS/session_events.jsonl`
contains reported events, not complete conversation capture. Execution records
exist only for wrapped commands; there were zero portfolio execution records at
the independent handover test. Hashes establish file identity, not score validity.

Portfolio results cannot yet be reproduced from this checkout: authoritative
data, substantive analysis code, approved rules, baseline scores and validated
outputs are not linked. External completion claims must remain owner-reported
until supporting records are inspected. Keep confidential data out of Git/logs;
record only non-sensitive identifiers and use approved access-controlled locations.

The setup commit `b51a58eea6f9a870f2d6ce4ead5692939b8c879d` is present locally and
identified by the owner as verified on GitHub. This session did not independently
recheck the remote. Setup documentation is accessible in this new Cloud session;
this does not prove fresh GitHub retrieval, future restoration or colleague access.
SharePoint upload and permissions are separate and unverified.
