# TEST ONLY — documentation workflow acceptance review

NOT APPROVED. Synthetic invented labels only; no CERF findings. No commit, push or publication performed.

Session: `SYNTHETIC-E2E-20261023-02`. Generated report: `project/04_ANALYSIS_LOGS/reports/20261023T124056Z_b9997ac414204eb69ee1ded0abcde19f`.

Overall: PASS — all 12 local checks.

| Check | Result |
| --- | --- |
| Unmodified copies of current workflow scripts | PASS |
| Success audit has exit 0 and matching input/output fingerprints | PASS |
| Intentional failure has exit 7 and absent output | PASS |
| Prior handover exact bytes and unknown context preserved | PASS |
| Prior synthetic report and decision preserved | PASS |
| Prior real documentation, reports, decisions, handover and scripts unchanged | PASS |
| Internal history includes alternatives, rationale, failure and next steps | PASS |
| Overview explains what happened, failure reason and next steps | PASS |
| Client draft excludes provisional decision and synthetic classification findings | PASS |
| Client draft explicitly labels its execution count as synthetic TEST ONLY | PASS |
| Generated overview methodology and validation references resolve within report | PASS |
| Experiment audit records have structured session and synthetic markers | PASS |

## What happened and why

A simulated discussion compared exact matching with token matching. Exact matching was provisionally selected for this demonstration to preserve mixed-label ambiguity; token matching remained a comparator. The decision is TEST ONLY, provisional and has no approver.

The successful experiment returned 0 and produced two invented classifications with one deliberately designed disagreement. The negative experiment returned 7 because it expected three records when only two existed. Its absent output and failure were correctly retained. Neither result measures real classification performance.

The current finish_session.py was executed unchanged inside the isolated project. It retained the prior handover bytes, unknown context, prior synthetic report and rejected decision; generated all three audience documents; and updated only the synthetic handover. Main project files were verified against SHA-256 baselines. The real decision register was empty, so nonempty decision preservation used an explicitly synthetic rejected sentinel.

## Fixes under review

Updated metadata, count separation and snapshot context are implemented in the pending source changes. Historical test 01 is unchanged. See AUDIT_WORKFLOW.md for exact behavior.

## Next steps and limits

Review this report and proposed changes before implementing fixes or committing. Rerun this acceptance scenario after fixes. Real CERF dataset, rules, scope, owner and reviewer remain NOT YET CONFIRMED; no methodological approval is implied. Do not circulate the generated client scaffold.

Inspect acceptance_results.json, command_transcript.json, script_provenance.json, protected_before.json, and the generated report. Commands and harmless console output are retained in the transcript; audit records intentionally store console hashes. Session events are reported summaries, not a verbatim chat archive. Fixture authoring and repository inspection are not automatically captured by audit_run.py. No Git commit/push test, SharePoint action or client publication was attempted.

## Final inspection and checkout verification

All 12 original local checks PASS. This does not mean GitHub retrieval passed.
The 73-file pre-change historical baseline was checked again after implementation:
all previous logs, reports, decisions, handover, scoring rules and failed test 01
remain byte-for-byte unchanged. Workflow copies tested in project/scripts still
match the current proposed workflow source. The first preservation baseline covers
history before edits; protected_before.json additionally checks no files changed
during the isolated acceptance run.

Fresh local checkout plus an uncommitted pending-file overlay: PASS. All 12
relative context links resolve from the three generated reports; all context
manifest hashes match; copied validation CSV is eligible under Git ignore rules;
regeneration in the disposable checkout reproduces identical documents. Both
regression suites pass in that checkout. See portability_results.json and
verify_portability.py for commands and evidence.

Fresh GitHub checkout: BLOCKED. The attempted command was:
`git clone --depth 1 https://github.com/domitillardm/CERF-Portfolio-Analysis.git /tmp/cerf-fresh-checkout-20261023-02`.
It exited 128: `Failed to connect to proxy port 8080 ... Could not connect to server`.
A local clone was used for portability testing, with its provenance explicitly
recorded. Updated GitHub retrieval remains unverified because no commit or push
was performed. After approval and restored connectivity, verify the authorized
remote commit and rerun checkout/link/hash checks against that exact commit.

Regression tests also passed for mixed synthetic/declared/legacy metadata,
exclusion of synthetic and legacy approved-decision fixtures, old CLI support,
required session and mutually exclusive flags, hashes when called outside --root,
immutable old records and missing-context failure before handover mutation.
The declared-portfolio branch used an invented metadata record only; it executed
no real portfolio analysis. Python 3.9 grammar parses the updated reusable tools;
runtime execution was tested with the installed Python only.

## Exact changes proposed for approval

- Canonical audit_run.py: optional --session; --synthetic / --portfolio-analysis;
  schema_version/session/test_only fields; input/output hashing relative to --root.
- Canonical session_log.py: matching flags/metadata on newly appended events only.
- New audit_metadata.py: shared conservative classification, count separation,
  synthetic banners and relative context links. Setup adds its relative script link.
- Canonical refresh_status.py and build_appendix.py: separate declared/synthetic/
  unknown counts, labelled session records and synthetic banners in all reports;
  synthetic and unknown decisions excluded from the client approved section.
- finish_session.py: propagate metadata; require context before logging; copy
  methodology/validation Markdown and activity register; write hashed snapshot
  manifest; exclude nested synthetic test projects from recursive log copying.
- .gitignore: allow non-sensitive validation registers only at versioned report and isolated test-project paths; unrelated legacy CSVs remain ignored.
- test_environment.py: commits and local pushes now require an explicit opt-in;
  default regression checks remain non-committing; legacy count expectation updated.
- New test_audit_workflow.py: legacy/mixed metadata, filtering, argument validation,
  root-relative hashes, history preservation and context-preflight regression tests.
- README.md: link to the new technical documentation.
- New AUDIT_WORKFLOW.md: CLI/schema, legacy compatibility, snapshot contents,
  verification, confidentiality review, capture limits and remote persistence limits.
- New acceptance session 02: isolated fixtures, command transcript, unchanged
  workflow copies, audit records, final reports, manifests, results and portability
  test evidence. Session 01 and its failed result were not edited or rerun.

Remaining limits: old records without markers are conservatively excluded, not
retrospectively classified; legacy approved decisions are retained internally but
withheld from the client approved section. No dataset/output package, real-data
validation, hosted-session continuity or client-release approval is established.
Local audit fingerprints retain execution-machine paths as provenance; context
links are relative and portable. The client draft remains a scaffold requiring
human review. No commit, push, scoring-rule change or client publication occurred.
