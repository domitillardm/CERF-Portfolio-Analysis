# Audit workflow metadata and portable reports

These changes concern documentation only. They do not supply or change scoring
rules, approve methodology, or establish real CERF results.

## Recording a session

Run `python3 scripts/setup_project.py` first. The setup creates relative script
links, including the shared `audit_metadata.py` module. Keep that module beside
the reusable tools when copying them to another project. Python 3.9+ is supported.

Use the same unique `--session ID` on audit commands, reported events and
finalization. Explicitly select `--synthetic` for tests, or
`--portfolio-analysis` for authorized substantive analysis. These mutually
exclusive flags require a nonempty session. For example:

```sh
python3 scripts/audit_run.py --root . --session SYNTHETIC-EXAMPLE --synthetic \
  --task documentation-check --owner test-agent --rules-version TEST-ONLY-v1 \
  -- python3 -c 'print("TEST ONLY")'
python3 scripts/session_log.py --root . --session SYNTHETIC-EXAMPLE --synthetic \
  --actor test-agent --kind validation --summary 'TEST ONLY: reviewed audit record'
python3 scripts/finish_session.py --session SYNTHETIC-EXAMPLE --synthetic \
  --actor test-agent --summary 'TEST ONLY documentation check' \
  --next-action 'Review synthetic evidence' --blocker 'No real analysis authorized'
```

New executions and events have `schema_version: 2`, `session`, and `test_only`.
The marker is `true` for synthetic work, `false` for explicitly declared
portfolio analysis, and `null` when unspecified. Old audit commands still run
without these new arguments. Their session is null and their activity is
unclassified; this compatibility does not make them substantive analysis.
Paths passed to audit input/output options resolve relative to `--root`, matching
the command working directory.

All three generated reports show separate counts for declared portfolio analysis,
synthetic tests and unclassified records. Only explicit `test_only: false` with a
session is eligible for portfolio summaries. Counts describe executions, including
failures; they never prove validated results. Synthetic sessions carry a prominent
TEST ONLY banner. Internal history retains every record, with session and category.

Historical records are read without alteration. No inference from task names or
old prose promotes legacy work into portfolio analysis. Legacy records missing
metadata remain excluded until a separately reviewed provenance mechanism exists.
Do not edit historical records to add fields.

Decision CSVs with the existing six columns remain readable and unchanged.
New registers can optionally include `session` and `test_only`. The client
approved section admits only explicitly non-test, session-associated approved
decisions, and excludes every decision in a synthetic session. Legacy decisions
without metadata remain in the unchanged register and internal history, with a
client note explaining their exclusion. No status or approval is rewritten.

## Versioned snapshot contents

`finish_session.py` verifies required context before appending its handover event.
It retains prior handover bytes, updates only the current handover after report
generation succeeds, and creates a new unique report directory. Existing reports
are never regenerated in place.

The snapshot contains logs, the full decision register, methodology Markdown,
validation Markdown and the non-sensitive activity scoring register when present.
Required context is `01_METHODOLOGY/PROJECT_EXPLAINED.md`,
`01_METHODOLOGY/scoring_rules.md` and `05_VALIDATION/issues.md`.
`snapshot_manifest.json` records session metadata and SHA-256 hashes for copied
context. All audience reports link to those context files relative to their own
location. Additional Markdown in these designated non-sensitive folders is copied;
review confidentiality before staging a snapshot. Source datasets, analysis outputs
and arbitrary attachments are not bundled. They require separately controlled
retrieval; the report is not a self-contained analysis rerun package.

Nested `synthetic_tests` directories are excluded from report log copying to avoid
recursively bundling test projects. Original test records stay at their original
paths. Explicitly marked synthetic records in the main log directory remain in
snapshots and are counted separately. Ignore rules allow the copied validation
register, while other dataset CSVs remain ignored by default.

## Verification and persistence

Run `python3 scripts/test_environment.py` and
`python3 scripts/test_audit_workflow.py`. Both use synthetic temporary projects
and make no commits or pushes by default. The older local Git round-trip test now
requires explicit `--allow-local-git-roundtrip`; do not use it without permission.
Acceptance sessions and evidence remain under
`04_ANALYSIS_LOGS/synthetic_tests/`. Never rerun a harness against its used session
directory or overwrite a failed acceptance record.

A fresh local checkout with pending files overlaid tests relative links, symlinks,
ignore rules and portability before committing. A GitHub clone with an overlay
also remains an uncommitted candidate, not proof that the updated version is on
GitHub. Actual remote retrieval requires an authorized commit/push followed by
a fresh GitHub checkout and verification of the exact commit, snapshot hashes and
links. Record blocked or unrun remote checks explicitly. Never claim remote
persistence from a local checkout or environment publication.

Audit records retain console hashes rather than console text. Session events are
reported summaries, not automatic conversation capture. Acceptance transcripts
record only their scripted subprocesses; repository reads, fixture authoring and
later inspection require separate reporting. Client circulation remains subject
to human review and is not part of these tests.
