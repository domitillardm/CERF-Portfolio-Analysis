#!/usr/bin/env python3
"""Build readable status without overwriting human-owned handover.json."""
import json,pathlib,sys
from audit_metadata import banner, category, context_links, coverage
root=pathlib.Path(sys.argv[1] if len(sys.argv)>1 else '.')
logs=root/'04_ANALYSIS_LOGS';runs=[];events=[]
for f in logs.glob('*.json'):
 try:runs.append(json.loads(f.read_text(encoding='utf8')))
 except (ValueError,OSError):pass
runs.sort(key=lambda r:r.get('started_utc',''))
p=logs/'session_events.jsonl'
if p.exists():
 for line in p.read_text(encoding='utf8').splitlines():
  try:events.append(json.loads(line))
  except ValueError:pass
handover=root/'handover.json'
try:h=json.loads(handover.read_text(encoding='utf8'))
except (OSError,ValueError):h={}
def field(k):return str(h.get(k) or 'NOT YET CONFIRMED')
lines=['# CERF Portfolio Analysis — START HERE','','> Auto-generated overview. Unverified items are explicitly marked. Read the linked records before relying on a conclusion.','','## In 60 seconds',banner(h),f'- **Purpose:** {field("purpose")}',f'- **Current phase:** {field("phase")}',f'- **Authoritative anonymised dataset:** {field("authoritative_dataset")}',f'- **Approved scoring framework:** {field("approved_rules")}',f'- **Latest validated deliverable:** {field("validated_output")}',f'- **Owner / contact role:** {field("owner")}',f'- **Next action:** {field("next_action")}',f'- **Blocking issue:** {field("blocker")}','','## What happened recently']
if events:
 for e in events[-12:][::-1]:lines.append(f'- {e.get("utc","")[:16]} | session {e.get("session") or "UNSPECIFIED"} | {category(e)} | {e.get("kind","")} [{e.get("status","")}] | {e.get("summary","")} (event {e.get("event_id","")})')
else:lines.append('- No recorded session events yet. This does not prove no work occurred.')
lines.extend(['','## Recorded analysis runs',coverage(runs)])
for r in runs[-5:][::-1]:lines.append(f'- {r.get("started_utc","")[:16]} | session {r.get("session") or "UNSPECIFIED"} | {category(r)} | {r.get("task","")} | {r.get("status","")} | run {r.get("run_id","")}')
lines.extend(['','## Resume work safely','1. Read `01_METHODOLOGY/PROJECT_EXPLAINED.md` and `01_METHODOLOGY/scoring_rules.md`.','2. Inspect `handover.json`, `06_DECISIONS/decision_register.csv` and open validation issues.','3. Confirm authoritative input, rules version, latest approved outputs and permission to process the data.','4. Reproduce the last approved run using its logged command and inputs; do not assume a hash alone proves correctness.','5. Record work with `scripts/audit_run.py` and `scripts/session_log.py`; update `handover.json` at session end.','6. Regenerate this page and the internal/client drafts; verify SharePoint publication separately.','','## Coverage and caveats','- Automatic capture is limited to instrumented commands. Discussions and GUI changes require session-event reporting.','- SharePoint synchronisation is not configured by these scripts.','- This page is a navigational summary, not methodological approval.'])
lines.extend([''] + context_links())
(root/'00_START_HERE.md').write_text('\n'.join(lines)+'\n',encoding='utf8')
