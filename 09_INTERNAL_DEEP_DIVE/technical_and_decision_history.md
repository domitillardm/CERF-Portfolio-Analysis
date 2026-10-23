# CERF internal guide and documentation history

Updated 2026-10-23. This stable, human-readable guide complements generated audit
reports; do not target the original report generators at this repository root.

## Current interpretation and evidence status

Read `01_METHODOLOGY/PROJECT_EXPLAINED.md` for programme purpose, working research
questions, stages, limitations and the proposed scoring workflow. Programme context
and core principles were supplied by the owner in this chat. External preparation
and anonymisation are owner-reported completion claims; source and validation
records are not linked. Existing scores/prompts/rules are referenced but not
accessible as authoritative inputs here. No CERF result or confidence assessment
is validated by this documentation work.

Country-track analysis supports the main track-level analysis through activities
ordered chronologically. Preserve achieved/potential and classification/evidence
strength distinctions. Keep original AI scores intact; proposed revisions and
human-final decisions must be separately traceable. The Inception Report scoring
table is the required source for future revised definitions, but is not supplied.

## Decisions and approvals

`06_DECISIONS/decision_register.csv` records CERF-M001: the meeting proposal to use
the highest human-checked activity score per country-track. Status is provisional;
no approver or meeting record is supplied. The handbook lists questions requiring
confirmation. No score aggregation or revised scoring definition is adopted.
Owner instructions are documented as instructions, not fabricated approval rows.
Working research-question wording and the documentation package await review.

## History and correction of stale status

- Earlier setup records are retained under `04_ANALYSIS_LOGS/legacy_setup/` and
  `04_ANALYSIS_LOGS/reports/20261023T112600Z_8a47129bf90649f6a502d5dcda748a02/`.
- Setup records report successful synthetic checks, not CERF portfolio analysis.
- Commit `b51a58eea6f9a870f2d6ce4ead5692939b8c879d` contains the repository setup.
  Local presence was independently checked in this Cloud session. The owner
  identifies it as verified on GitHub; no new remote verification was performed.
  Historical claims that setup was uncommitted are superseded, not rewritten.
- `05_VALIDATION/handover_test_20261023.md` retrospectively records this chat's
  read-only handover test and its limits. Documentation accessibility passed;
  research reproduction remained blocked.
- Pre-edit copies of this session's existing documentation and baseline hashes
  are in `04_ANALYSIS_LOGS/documentation_history/DOCUMENTATION-20261023-01/`.
  These are historical copies; follow current root instructions when resuming.

## Audit operation and gaps

Use `scripts/session_log.py` for non-sensitive reported discussions, experiments,
failed attempts, corrections, validation and decisions. Use `scripts/audit_run.py`
for substantive executable analysis with explicit versions and input/output paths.
The wrapper records commands, fingerprints, exit status and stream hashes; it
does not validate score correctness or archive full discussions. Unwrapped work
is not automatically captured. Do not log confidential source text or links.

No grading experiments or scoring-rule revisions were performed in this session.
No scoring definitions, model configuration or evidence-strength thresholds were
invented. The validation record identifies unrun checks and documentation errors.
Methodological changes require human approval; no provisional decision is promoted
by report generation. Preserve rejected proposals and failed runs when they occur.

Use `scripts/finish_session.py` once documentation and validation are ready. It
retains the immediately preceding handover and generates a new status, internal
execution/event history and unapproved client scaffold in a unique directory.
Follow `handover.json.latest_report` for those generated files; this stable guide
is not their replacement. Prior documents are additionally retained by this
session's documentation snapshot. No client release or SharePoint upload occurs.

## Next researcher and deliverables

Resolve `05_VALIDATION/issues.md` first: obtain secure references to the prepared
dataset/validation, existing scores/prompts/rules and exact Inception Report table;
confirm scope, mapping, reviewers and decision authority. Prepare separate
instruction revisions and a human-review plan, then seek methodological approval
before any authorised pilot. Establish classification confidence before comparison
with independent case-study evidence. Produce traceable country-track narratives,
track synthesis and provisional ETE hypotheses only after the relevant checks.
An appendix requires actual approved rules, QA evidence and reproducible versions.

This package is proposed local documentation. No commit or push is authorised until
the user reviews it. GitHub, cloud snapshots and SharePoint are distinct persistence
channels; present-session access does not verify all three.
