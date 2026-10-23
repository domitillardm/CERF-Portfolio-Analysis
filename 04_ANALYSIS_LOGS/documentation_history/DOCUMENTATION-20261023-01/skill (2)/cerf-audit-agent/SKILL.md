---
name: cerf-audit-agent
description: Operate and document the CERF end-term evaluation portfolio analysis, including activity-universe cleaning, AI-assisted scoring, qualitative evidence classification, validation, team handovers, SharePoint-ready project status, internal technical deep dives and client methodological appendix drafts. Use for every Codex session involving CERF portfolio work.
---
# CERF audit and handover agent
1. Read the project's `AGENTS.md`, `00_START_HERE.md`, `handover.json`, methodology and decision register before analysis. If absent, initialise them and label missing information NOT YET CONFIRMED.
2. Establish the authoritative anonymised activity dataset, classification codebook, rules version, scope, owner and approval status. Never assume earlier draft choices are approved.
3. Instrument each substantive command with `scripts/audit_run.py`. Log discussion, attempted/failed experiments, interpretations, corrections and decisions using `scripts/session_log.py`; this is agent-reported, not automatic verbatim capture.
4. Keep activity-level scores traceable to immutable activity IDs, dataset/rules versions, evidence references, uncertainty, reviewer and adjudication. AI scores are provisional until reviewed.
5. At session end, ask the user to review a concise summary, unresolved issues and proposed handover edits. Update `handover.json` without erasing known context, then run `scripts/refresh_status.py` and `scripts/build_appendix.py`.
6. Maintain three audiences: plain-language `00_START_HERE.md` for any new colleague; internal `09_INTERNAL_DEEP_DIVE/technical_and_decision_history.md` for analysts and AI; client `08_CLIENT_APPENDIX/methodology_DRAFT.md` for controlled, reviewed external reporting.
7. Preserve failed experiments and provisional decisions; never silently promote to approved or rewrite history. Use version history or controlled immutable exports to prevent accidental overwrites.
8. Do not claim every Codex conversation, UI edit or command is automatically captured. Without approved SharePoint integration, publication is manual and must be verified. Do not include raw confidential data, personal information, tokens or secrets in logs.
9. Do not release client documents without a designated human reviewer confirming methodology, factual claims, confidentiality and reproducibility.
10. Consult `references/setup.md` for deployment and the handover acceptance test.
