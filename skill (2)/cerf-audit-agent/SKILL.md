---
name: cerf-audit-agent
description: Operate and document the CERF end-term evaluation portfolio analysis, including activity-universe cleaning, AI-assisted scoring, qualitative evidence classification, validation, team handovers, SharePoint-ready project status, internal technical deep dives and client methodological appendix drafts. Use for every Codex session involving CERF portfolio work.
---
# CERF audit and handover agent
1. Read the project's `AGENTS.md`, `00_START_HERE.md`, `handover.json`, handbook, methodology, decision register, validation issues and latest versioned report before analysis. In this installation use the existing repository and `scripts/setup_project.py` only to create missing scaffolds. Label missing information NOT YET CONFIRMED. Root instructions and the user's task scope take precedence over this reusable guide.
2. Establish the authoritative anonymised activity dataset, classification codebook, rules version, scope, owner and approval status. Never assume earlier draft choices are approved.
3. Instrument substantive executable analysis with `scripts/audit_run.py`. Log discussion, attempted/failed experiments, interpretations, corrections and decisions using `scripts/session_log.py`; this is agent-reported, not automatic verbatim capture. Honour read-only tasks: do not run setup, loggers, generators, finalisers or synthetic tests that write files. Report unrun checks and logging gaps honestly.
4. Keep activity-level scores traceable to immutable activity IDs, dataset/rules versions, evidence references, uncertainty, reviewer and adjudication. AI scores are provisional until reviewed.
5. For an authorised writing session, preserve pre-edit documentation and handover history, update supported handover facts without erasing known context, and use `python3 scripts/finish_session.py --session ID --actor ACTOR --summary "Non-sensitive summary" --next-action "Next action" --blocker "Outstanding issue or none"`. This installation's finaliser generates a unique versioned report directory and retains the prior handover. Never run `refresh_status.py` or `build_appendix.py` against the project root: those overwrite their targets. Show the concrete proposed documentation changes and unresolved questions for review. Do not commit or push without user approval.
6. Maintain a stable newcomer start page and handbook, a stable internal guide at `09_INTERNAL_DEEP_DIVE/technical_and_decision_history.md`, and generated status/internal history/unapproved client scaffold in the directory referenced by `handover.json.latest_report`. Generating a client draft is not approval or publication. Keep old reports unchanged.
7. Preserve failed experiments and provisional decisions; never silently promote to approved or rewrite history. Use version history or controlled immutable exports to prevent accidental overwrites.
8. Do not claim every Codex conversation, UI edit or command is automatically captured. Without approved SharePoint integration, publication is manual and must be verified. Do not include raw confidential data, personal information, tokens or secrets in logs.
9. Do not release client documents without a designated human reviewer confirming methodology, factual claims, confidentiality and reproducibility.
10. Consult `references/setup.md` for deployment and the handover acceptance test.

## CERF analytical safeguards

The Climate and Energy Response Facility portfolio analysis supports the End-Term
Evaluation with breadth across activities/tracks, complementing case studies,
interviews and surveys. Tracks are the main analytical unit; supporting activities
are organised by country, track and chronological order. The handbook records the
owner-provided context and remaining source gaps; do not invent programme details.

Distinguish achieved results from future potential and result classification from
evidence strength. Monitoring outcomes are reported claims, not independently
verified findings. Do not infer missing information or equate missing evidence
with no results. Frequencies are not programme success rates. Codex proposes
classifications; humans review and decide final scores and methodological changes.

Data preparation/anonymisation are reported complete outside the repository, not
independently validated here. Locate supporting versions and validation records.
Review existing prompts/rules and the Inception Report scoring table before
proposing revised definitions; keep proposed rules separate and versioned until
human approval. Preserve existing AI scores unchanged; record revised proposals
separately with baseline links, evidence, uncertainty and review/adjudication.

CERF-M001 (highest human-checked activity score per country-track) is a proposal
pending human confirmation, not an approved aggregation rule. Establish confidence
in classifications before comparing with independent case-study evidence. Do not
invent confidence thresholds, score definitions or approval records. Distinguish
repository checks, owner reports, proposed methods and approved decisions.
