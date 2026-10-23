# CERF portfolio operating instructions

The project root is this Git repository. Keep non-sensitive methodology, decisions,
validation records, session logs and handovers here. Use the existing checkout;
cloud tasks are already isolated. Do not create a worktree unless requested.

Read `00_START_HERE.md`, `handover.json`, `01_METHODOLOGY/`,
`06_DECISIONS/decision_register.csv` and `05_VALIDATION/issues.md` before analysis.
Reusable agent instructions remain in `skill (2)/cerf-audit-agent/SKILL.md` and
`skill (2)/cerf-audit-agent/assets/AGENTS.md`. This root file specifies the safe
reporting and persistence workflow for this installation.

- Start with `python3 scripts/setup_project.py`. Setup only creates missing files;
  never replace project documentation, input data, analysis or approved rules.
- Confirm authoritative anonymised input, rules version, scope, owner and approval
  before scoring. Unknown facts remain NOT YET CONFIRMED. Never change methodology
  or promote scores/decisions to approved without a designated human reviewer.
- Assign a unique session ID. Record objective/scope, discussions, failed attempts,
  corrections, uncertainty and validation with `scripts/session_log.py`. This is
  reported summary logging, not automatic conversation capture.
- Wrap substantive analysis in `scripts/audit_run.py`, specifying task, owner,
  rules version and input/output paths. Run from the root with `--root .`; use
  unique output paths. Never modify authoritative inputs in place.
- Maintain activity IDs, dataset/rules versions, evidence pointers, uncertainty,
  reviewer and adjudication in the validation register. Do not put sensitive
  content, personal information, source text, credentials or confidential links
  in any log, command arguments or documentation.
- Record each new methodological decision explicitly in the decision register;
  keep it provisional until human approval. Preserve rejected decisions and
  failures. Do not invent a decision when none was made.
- End every analysis session with `python3 scripts/finish_session.py --session ID
  --actor ACTOR --summary "Non-sensitive summary" --next-action "Next action"
  --blocker "Outstanding issue or none"`. It snapshots the prior handover,
  updates the handover, logs the session and generates a new versioned status,
  internal history and client draft without replacing existing reports.
  Read the report directory referenced by `handover.json.latest_report` on resume.
  Do not run the original report generators against the project root: they
  overwrite files. The root start page is a stable navigation document.
- At handover, report completed work, validation, failed/unrun checks, unresolved
  decisions, next action and logging gaps. Require human review before client
  circulation. Verify SharePoint upload and permissions separately; no sync exists.
- Ignore rules are only a guardrail. Keep real source datasets outside Git or in
  ignored `02_ACTIVITY_DATA/`; keep sensitive outputs in ignored `07_RESULTS/`.
  Review content and paths before staging. Never use `git add .` or force-add data.
- Distinguish local files, local commits, verified remote commits and published
  cloud snapshots. Check Git status, inspect the exact selected diff and obtain
  authorization before pushing. A local file or commit is not GitHub persistence.
  Verify a pushed commit by remote read and fresh checkout before claiming that
  colleagues or future sessions can retrieve it. Environment publication alone
  does not push anything to GitHub.
