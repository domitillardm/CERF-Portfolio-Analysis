# CERF portfolio analysis — start here

Current 28 October 2026. All 249 activities are retained in a **final consolidated provisional** scoring dataset. There are93 defined provisional country-tracks,14 unmapped activities in 7 holding groups and 3 unresolved factual-stage cases. Source data and exact evidence/decision histories remain outside Git; authoritative paths and hashes are in [handover](handover.json).

**Read the [methodological-independence audit](05_VALIDATION/method_independence_audit_20261028.md) before interpreting method agreement.** Initial B was A-default with contextual overrides; original singleton C copied A. Multi-track C was separately authored, but independent blinded judgement is not demonstrated. D1/D2 are derived maxima.100% paired C/D agreement is descriptive consistency, not independent methodological validation.

- [Current definitions and operationalisation](01_METHODOLOGY/OPERATIONALISATION_CURRENT.md), [source-aligned codebook v0.2](01_METHODOLOGY/SCORING_CODEBOOK_DRAFT_v0.2.md), and separate [F1 conventions](01_METHODOLOGY/CALIBRATION_ADDENDUM_v0.2-F1.md).
- [Scoring/decision history and coverage](09_INTERNAL_DEEP_DIVE/scoring_and_classification_history_20261028.md).
- [Technical guide](09_INTERNAL_DEEP_DIVE/technical_and_decision_history.md), [decision register](06_DECISIONS/decision_register.csv) and [reported session log](04_ANALYSIS_LOGS/session_events.jsonl).
- [Current limitations](05_VALIDATION/issues.md) and [provisional client appendix](08_CLIENT_APPENDIX/methodology_DRAFT.md), not released for client circulation.

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
