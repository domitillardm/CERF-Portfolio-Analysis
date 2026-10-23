# Deployment: Codex Cloud with standard SharePoint folders

## Reality check
Codex Cloud is not a SharePoint service or a universal activity recorder. No GitHub or Microsoft Graph integration is assumed. The scripts operate only where the project files are available and Python can execute. Cloud workspaces may be temporary; export the entire publication package to a durable, organisation-approved location after each session. Manual SharePoint upload is the supported baseline. Full automatic publication requires an approved connector or IT-managed workflow.

## Initial setup
1. In this installation, use the existing repository, root `AGENTS.md` and `ENVIRONMENT.md`; do not overwrite them with the reusable asset. Use `scripts/setup_project.py` for missing scaffolds only in authorised writing sessions. Reusable utilities are relative links into this package; the root finaliser is installation-specific. Do not use the legacy `/workspace/cerf-project` folder for new work.
2. Create `01_METHODOLOGY`, `02_ACTIVITY_DATA`, `03_CODE`, `04_ANALYSIS_LOGS`, `05_VALIDATION`, `06_DECISIONS`, `07_RESULTS`, `08_CLIENT_APPENDIX`, `09_INTERNAL_DEEP_DIVE`. Keep sensitive source data out of published folders.
3. Create `handover.json` with keys `purpose`, `phase`, `authoritative_dataset`, `approved_rules`, `validated_output`, `owner`, `next_action`, `blocker`. Write UNKNOWN where needed, not guessed facts.
4. Create `01_METHODOLOGY/PROJECT_EXPLAINED.md` for a newcomer: what CERF is, why portfolio analysis, unit of analysis, country/track structure, dataset provenance, classification definitions, evidence standard, glossary, process and links to source references.
5. Create `06_DECISIONS/decision_register.csv` with `decision_id,date,decision,rationale,status,approved_by`; use `provisional` until approved. Add an activity-level scoring register with activity ID, dataset version, rules version, assigned score, evidence pointer, uncertainty, validation state and reviewer.
6. Use `python scripts/session_log.py --root . --session SESSION-001 --actor analyst --kind discussion --summary "Discussed rule ambiguity" --status provisional` for a discussion. This does not intercept Codex messages automatically.
7. Run analysis via `python scripts/audit_run.py --root . --task pilot --owner analyst --rules-version draft --input 02_ACTIVITY_DATA/anonymised.xlsx --output 07_RESULTS/pilot.csv -- python 03_CODE/score.py` (adapt command and filenames). Never run unknown code without review.
8. Preserve prior documentation, update supported handover facts and run `python3 scripts/finish_session.py --session SESSION-ID --actor analyst --summary "Non-sensitive summary" --next-action "Specific next action" --blocker "Outstanding issue or none"`. Inspect the unique directory referenced by `handover.json.latest_report`. Do not call the original report generators against the root; the finaliser invokes them only inside the new report directory. Generating an unapproved client scaffold does not publish it.
9. Publish only approved, non-sensitive outputs to a SharePoint folder: `00_START_HERE.md`, newcomer handbook, decision register, validation summary, reviewed client appendix and internal deep dive if access is restricted appropriately. Confirm upload/version and access manually. Preserve the previous version.
10. At end of session, present concrete documentation changes for human review, including unlogged work, provisional decisions, blockers, next actions and publication status. Do not commit, push or publish without authorisation. Read-only sessions must not run setup, loggers, finalisation or synthetic tests that write files or create commits.

## Multi-user controls
Assign a single editor for the authoritative workbook; use unique output filenames with run IDs. If collaboration grows, adopt an approved version-control and review process. Do not assume SharePoint resolves conflicting simultaneous workbook edits safely.

## Handover acceptance test
A colleague unfamiliar with CERF must be able to explain the programme and analysis, locate the authoritative dataset and approved rules, identify validated/provisional results, trace a sampled score, reproduce a verified run, locate failed experiments and open decisions, and perform the next action without the original analyst. Record the test date, reviewer and gaps; no continuity guarantee until this passes.

## Client release gate
Review the appendix against approved rules, documented evidence, QA results, frozen code/data versions and confidentiality policy. Raw internal discussion and errors should not be pasted indiscriminately into client deliverables.
