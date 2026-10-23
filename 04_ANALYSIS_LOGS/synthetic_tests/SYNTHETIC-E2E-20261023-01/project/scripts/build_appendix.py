#!/usr/bin/env python3
"""Create separate internal deep dive and client-facing DRAFT; never imply approval."""
import csv,json,pathlib,sys
root=pathlib.Path(sys.argv[1] if len(sys.argv)>1 else '.')
runs=[];events=[]
for f in (root/'04_ANALYSIS_LOGS').glob('*.json'):
 try:runs.append(json.loads(f.read_text(encoding='utf8')))
 except (OSError,ValueError):pass
runs.sort(key=lambda r:r.get('started_utc',''))
f=root/'04_ANALYSIS_LOGS/session_events.jsonl'
if f.exists():
 for s in f.read_text(encoding='utf8').splitlines():
  try:events.append(json.loads(s))
  except ValueError:pass
decisions=[];f=root/'06_DECISIONS/decision_register.csv'
if f.exists():
 with f.open(newline='',encoding='utf8') as stream:decisions=list(csv.DictReader(stream))
internal=['# Internal deep dive — CERF portfolio analysis','','This is a navigation and audit record for analysts and AI assistants. Entries reported by the agent are not independent evidence.','','## Instrumented runs']
for r in runs:internal.extend([f'### {r.get("run_id", "unknown")}',f'- Time: {r.get("started_utc")} to {r.get("ended_utc")}',f'- Task / owner / rules: {r.get("task")} / {r.get("owner")} / {r.get("rules_version")}',f'- Status / exit: {r.get("status")} / {r.get("exit_code")}',f'- Command: `{json.dumps(r.get("command",[]),ensure_ascii=False)}`',f'- Inputs: `{json.dumps(r.get("inputs",[]),ensure_ascii=False)}`',f'- Outputs: `{json.dumps(r.get("outputs",[]),ensure_ascii=False)}`',''])
internal.extend(['## Reported discussions, errors, experiments and handovers'])
for e in events:internal.append(f'- {e.get("utc")} | {e.get("kind")} | {e.get("status")} | {e.get("summary")} | Why: {e.get("rationale")} | Reference: {e.get("evidence_reference")} | Next: {e.get("next_action")}')
internal.extend(['','## All methodological decisions (including provisional/rejected)'])
for d in decisions:internal.append('- '+json.dumps(d,ensure_ascii=False))
internal.extend(['','## Known limits','- This does not automatically archive complete Codex conversations, unwrapped actions, Excel GUI edits or SharePoint activity.','- Validate all citations, evidence links and code before relying on summaries.'])
(root/'09_INTERNAL_DEEP_DIVE').mkdir(exist_ok=True)
(root/'09_INTERNAL_DEEP_DIVE/technical_and_decision_history.md').write_text('\n'.join(internal)+'\n',encoding='utf8')
client=['# DRAFT — CERF Portfolio Analysis Methodological Appendix','','**Not approved for client circulation.** The content below is a scaffold, not a claim of methodological validity.','','## Purpose and scope','[Explain portfolio, unit of analysis, countries, tracks, period, data provenance and inclusion criteria.]','','## Data preparation and anonymisation','[Document source versions, exclusions, cleaning rules, anonymisation checks and activity ID integrity.]','','## AI-assisted classification and scoring','[Insert approved operational definitions, prompt/model configuration if permitted, rules versions, evidence hierarchy, treatment of uncertainty and human oversight.]','','## Quality assurance and validation','[Report sampling method, independent manual checks, agreement/disagreement, adjudication and sensitivity analyses. Do not invent figures.]','','## Approved methodological decisions']
approved=[d for d in decisions if d.get('status','').lower()=='approved']
client.extend([f'- {d.get("decision_id","")}: {d.get("decision","")} — {d.get("rationale","")} (approved by {d.get("approved_by","")})' for d in approved] or ['- No approved decisions recorded.'])
client.extend(['','## Reproducibility and limitations',f'- {len(runs)} instrumented execution records exist (not necessarily all work).','[Provide frozen input identifiers, executable scripts, software versions, release tag and rerun steps.]','[Discuss incomplete records, scoring uncertainty and other limitations.]','','## Client release gate','[Human reviewer must check accuracy, confidentiality, approvals, and alignment with validated results.]'])
(root/'08_CLIENT_APPENDIX').mkdir(exist_ok=True)
(root/'08_CLIENT_APPENDIX/methodology_DRAFT.md').write_text('\n'.join(client)+'\n',encoding='utf8')
