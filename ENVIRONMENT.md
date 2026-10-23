# Repository-based CERF audit environment

Python 3.9+ and Git are sufficient; Python 3.12 was tested. No packages or running
services are needed. From the repository root:

```sh
python3 scripts/setup_project.py
python3 scripts/test_environment.py
```

Setup creates only missing files and relative script links. It does not overwrite
documentation, change methodology, install a second checkout or move/delete data.
The reusable skill package remains in `skill (2)/cerf-audit-agent/`.

The initial folders contain placeholders, not approved methodology or validated
analysis. Keep authoritative data outside Git or in ignored `02_ACTIVITY_DATA/`.
Outputs in `07_RESULTS/` are also ignored by default. Decisions, non-sensitive
session logs, handovers and validation documentation are eligible for Git.
Ignore patterns cannot detect confidential content in an otherwise allowed file.

## Analysis session workflow

Read AGENTS.md, project status, methodology, decisions and validation issues.
Confirm input, owner, scope and approved rules before analysis. Record objective,
scope and substantive discussion using a unique session ID:

```sh
python3 scripts/session_log.py --root . --session SESSION-ID --actor analyst \
  --kind discussion --summary "Non-sensitive objective and scope" --status provisional
python3 scripts/audit_run.py --root . --task TASK --owner analyst \
  --rules-version VERSION --input INPUT --output UNIQUE-OUTPUT -- python3 REVIEWED-SCRIPT
```

Use actual reviewed paths for the example placeholders. Keep command arguments
and logged file paths non-sensitive. Record validation results/issues and explicit
methodological decisions in their registers; keep new decisions provisional until
approved. No decisions are created or approved automatically.

At session end, update the handover and produce fresh reports:

```sh
python3 scripts/finish_session.py --session SESSION-ID --actor analyst \
  --summary "Non-sensitive completed work, checks and gaps" \
  --next-action "Specific next action" --blocker "Outstanding issue or none"
```

`handover.json.latest_report` points to a unique directory under
`04_ANALYSIS_LOGS/reports/`. It contains the new status, internal history, draft
appendix, prior handover and copies of the logs/decisions used to generate them.
Existing reports and human documentation are retained. Unknown handover fields
are preserved. This command updates next_action, blocker, latest_session and
latest_report; update other handover facts explicitly when supported by evidence.
Use one writer at a time. Do not run the original generators against the project
root; those utilities overwrite their target documents. The root start page is a
stable navigation page rather than a replaceable generated report.

## Persistence and release

Local files are not yet committed. A local commit is not a push. Cloud environment
publication is a separate filesystem snapshot and does not publish Git changes.
Before any authorized push, review the exact paths and diff for confidential
content, including logs and report snapshots. Stage selected safe files only.
Never force-add ignored data. After pushing, check the remote commit and clone it
into a fresh session to verify the documentation is retrievable. Do not claim
permanent persistence or colleague access based only on local tests.

`scripts/test_environment.py` uses synthetic data in temporary repositories. It
checks repeated setup, retained existing content, audit success/failure, distinct
session finalization, ignore rules and restoration through a local Git remote.
Separate Python processes and a fresh clone simulate session boundaries; they do
not verify a new hosted Codex session or GitHub write access.

The earlier `/workspace/cerf-project` folder is retained without deletion. Its
non-sensitive setup records were copied into this repository, with the original
documents also archived under `04_ANALYSIS_LOGS/legacy_setup/`. Future work uses
this repository only. No real CERF data was migrated.

Human review is required for methodological approvals, client release and secure
publication. SharePoint sync is not configured; manual upload and access checks
remain separate. Review/save the cloud configuration draft before publication.
