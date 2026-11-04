# Documentation publication checks

Scope: reconciled handover, unchanged v0.2/F1 sources, appended working decisions and a safe restricted-file manifest. No new scoring or confidential upload is authorised.

## Evidence checked before publication

- Current private dataset, full scoring/calibration files and stored validation records were located and verified, not inferred from authorisation.
- Direct counts confirm 182 unique activities, 126 achievement codes, two code-6 statuses, 54 unscored, 51 groups (10 numeric maxima/41 pending), 147 review rows and zero completed human decisions.
- Later branch source commit and codebook/F1 provenance were inspected; only trailing-newline differences exist against frozen snapshots.
- All 60 historical decision rows are retained; seven explicitly owner-approved working rows are appended without promoting old proposals.
- `scripts/validate_documentation.py` checks current status, source definitions, local Markdown links, decision continuity and staged text/privacy constraints. Optional private checks verify manifest hashes and current counts without printing source evidence.

## Publication controls and limits

Only an explicit allowlist of reviewed text documentation, safe metadata, validation code and a short sanitised session record is staged. Restricted workbooks, activity-level CSV/JSON, raw narratives, review records, private reproduction bundles and unrelated session logs are excluded. Original sources and scores are hash-checked unchanged. The confidentiality scan includes both case-level ID/record markers and credentials; manual inspection remains necessary because regex checks alone cannot certify confidentiality.

The final evidence-standardisation one-pager, full Inception Report and original prompt archive remain missing; reviewer/adjudication decisions and recipient internal-file permissions remain pending. The recent Word methodology summary is a review draft. The repository is a handover reference, not a data distribution endpoint or proof of outcome validity.

The branch is submitted through a PR to main; it must not be merged automatically. Remote branch/commit and fresh-retrieval verification are recorded after publication in the local session audit and PR summary. No scoring result is promoted to human validated by publishing these documents.
