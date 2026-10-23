# TEST ONLY — documentation workflow acceptance review

NOT APPROVED. Synthetic invented labels only; no CERF findings. No commit, push or publication performed.

Session: `SYNTHETIC-E2E-20261023-01`. Generated report: `project/04_ANALYSIS_LOGS/reports/20261023T123200Z_99a3508d02a3481b828012fc747b3de5`.

Overall: FAIL — core capture works; three documentation/isolation gaps remain.

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
| Client draft explicitly labels its execution count as synthetic TEST ONLY | FAIL |
| Generated overview methodology and validation references resolve within report | FAIL |
| Experiment audit records have structured session and synthetic markers | FAIL |

## What happened and why

A simulated discussion compared exact matching with token matching. Exact matching was provisionally selected for this demonstration to preserve mixed-label ambiguity; token matching remained a comparator. The decision is TEST ONLY, provisional and has no approver.

The successful experiment returned 0 and produced two invented classifications with one deliberately designed disagreement. The negative experiment returned 7 because it expected three records when only two existed. Its absent output and failure were correctly retained. Neither result measures real classification performance.

The current finish_session.py was executed unchanged inside the isolated project. It retained the prior handover bytes, unknown context, prior synthetic report and rejected decision; generated all three audience documents; and updated only the synthetic handover. Main project files were verified against SHA-256 baselines. The real decision register was empty, so nonempty decision preservation used an explicitly synthetic rejected sentinel.

## Failures and proposed changes — not implemented

1. The client draft says "2 instrumented execution records exist" without identifying these as synthetic. Add structured test/session metadata and render a prominent TEST ONLY banner; report synthetic counts separately from real work.
2. The generated overview tells a reader to open methodology and validation files absent from the report snapshot. Copy the non-sensitive methodology/validation context or generate verified links to the project root. Avoid treating this incomplete snapshot as a self-contained handover.
3. Audit records have no structured session or test_only fields. This run uses separate directories plus task/rules labels, but scripts cannot reliably filter mixed records. Add --session and a synthetic flag across logging, auditing and finalization, with consistent report filtering.

## Next steps and limits

Review this report and proposed changes before implementing fixes or committing. Rerun this acceptance scenario after fixes. Real CERF dataset, rules, scope, owner and reviewer remain NOT YET CONFIRMED; no methodological approval is implied. Do not circulate the generated client scaffold.

Inspect acceptance_results.json, command_transcript.json, script_provenance.json, protected_before.json, and the generated report. Commands and harmless console output are retained in the transcript; audit records intentionally store console hashes. Session events are reported summaries, not a verbatim chat archive. Fixture authoring and repository inspection are not automatically captured by audit_run.py. No Git commit/push test, SharePoint action or client publication was attempted.

Inspection correction: the initial case-sensitive check expected "Approach B" while the report contains "approach B". Case-insensitive reinspection passes. The test harness was corrected; generated reports and audit evidence were not rewritten. Final result: 9 PASS, 3 FAIL.

Logging gap correction: the generated validation event overstates command-transcript coverage. That transcript contains only scripted subprocesses (setup, logging, audited runs and finalization); initial repository reads, fixture authoring and later inspection are not recorded there. This correction preserves the original generated evidence and corrects the harness for future sessions.
