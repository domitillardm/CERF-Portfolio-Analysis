# CERF internal technical guide — current 28 October 2026

Read [operationalisation](../01_METHODOLOGY/OPERATIONALISATION_CURRENT.md), [scoring history](scoring_and_classification_history_20261028.md) and [independence audit](../05_VALIDATION/method_independence_audit_20261028.md). This current guide supersedes the historical setup-only status; prior bytes remain in documentation history and earlier commits.

## Critical audit result

A/B are not demonstrated independent scoring passes: B was initially A-default with explicit contextual overrides. C for 69 original singleton groups copied A;32 multi-group C entries were authored separately, but no blinding or full-run independent C-only freeze is evidenced. D1/D2 are calculated summaries. Pilot C was locked before D; full materialisation assigns C before D in code but freezes them together afterward. Current 100% paired track agreement is recorded-output agreement, not independent method validation. See precise evidence labels and corrective recommendations in the audit.

## Source and version boundaries

`handover.json.current_provisional_dataset` identifies the immutable authoritative workbook; lean/analytical workbooks are static presentation/analysis copies. Detailed score histories, source fields, literal owner choices, exact evidence IDs and scripts with confidential annotations live under `/workspace/cerf-private`, not Git. Source hashes establish identity, not truth. Public documentation contains aggregate coverage and algorithm descriptions only. The protected exclusion annex enumerates every excluded unit and reason without publishing row-level scores.

## Reproduction and handover

Run setup only in authorised writing sessions, and use audit_run/session_log/finish_session per AGENTS. Preserve snapshots before editing root documents. The finaliser invokes generators inside a unique report directory, never against human-maintained root documents. Generated historical client scaffolds are not the current populated provisional appendix; use the root appendix linked from the start page. Existing report folders remain local history; curated, reviewed documentation is what this publication commits.

The session log is agent-reported, not a complete prompt/model transcript. Wrapped commands, fingerprints and outcomes are available; unwrapped annotation authorship is not independently reconstructable. Full confidential scoring cannot be replayed from a Git checkout alone. Obtain authorised private artifacts and exact source/method versions. Missing model/settings/full prompt archives and independent human validation must remain explicit.

## Corrections and publication

Earlier XML namespace/property defects and literal escape-marker encoding were repaired with preserved prior files and fresh-library exports. Independent SQL/engine checks are technical QA, not rescoring or outcome verification. Current documentation replaces stale setup status and corrects overstrong independence language while retaining original decision rows and histories. Publish only explicitly selected privacy-reviewed text; never `git add .`. User authorised this documentation commit/push, not client release or scoring changes. Verify remote SHA and fresh checkout before claiming GitHub persistence; SharePoint remains separate and unverified.


## New post-freeze comparison evidence — 28 October 2026

The owner has supplied a separately frozen, score-masked C assessment for34 multi-activity tracks;33 numerical results and1 unresolved disposition are verified against the prepared inputs. The [post-freeze report](../05_VALIDATION/post_freeze_C_comparison_20261028.md) records30/33 agreement with original C,25/28 with D1 and26/29 with D2. Three numerical disagreements are downward; one status remains unresolved. Common-denominator rates are identical25/28. File/input integrity is verified; input isolation and freeze-before-reveal are documented assessor/user declarations without an independently signed access chronology. Neither output is a gold standard. No original or frozen score has changed. This is new evidence about an additional assessment, not a retraction of findings about original construction. Targeted four-case human adjudication is recommended before final classifications/bias claims; no broad rescoring is initiated.


## Current supervisor interface — 28 October 2026

A [single five-sheet workbook](../05_VALIDATION/supervisor_consolidation_20261028.md) now brings activity A/B, unique-track original C/D1/D2 and separate frozen C together for review. It changes no classifications, membership or evidence rules. All249 activities,93 defined units and7 clearly separate holding groups are reconciled. The four primary post-freeze questions are distinct from17 old source limitations,2 earlier diagnostics and3 readiness conditions. Blank reviewer notes have no automatic scoring effect. Descriptives count tracks once and expose valid/result-status denominators; they are not effectiveness rankings. Source/frozen files and detailed histories remain external to Git. This is the current review entry point, not a new authoritative scoring version or human approval.
