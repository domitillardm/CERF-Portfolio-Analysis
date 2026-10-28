#!/usr/bin/env python3
"""Check current privacy-safe documentation; never reads or modifies private scores."""
import csv,json,re,sys
from pathlib import Path
ROOT=Path(sys.argv[1] if len(sys.argv)>1 else Path(__file__).resolve().parents[1])
required=['00_START_HERE.md','README.md','handover.json','01_METHODOLOGY/PROJECT_EXPLAINED.md','01_METHODOLOGY/scoring_rules.md','01_METHODOLOGY/OPERATIONALISATION_CURRENT.md','01_METHODOLOGY/SCORING_CODEBOOK_DRAFT_v0.2.md','01_METHODOLOGY/CALIBRATION_ADDENDUM_v0.2-F1.md','05_VALIDATION/issues.md','05_VALIDATION/method_independence_audit_20261028.md','05_VALIDATION/independence_artifact_index.json','06_DECISIONS/decision_register.csv','04_ANALYSIS_LOGS/session_events.jsonl','08_CLIENT_APPENDIX/methodology_DRAFT.md','09_INTERNAL_DEEP_DIVE/technical_and_decision_history.md','09_INTERNAL_DEEP_DIVE/scoring_and_classification_history_20261028.md']
assert all((ROOT/p).is_file() for p in required)
h=json.loads((ROOT/'handover.json').read_text());assert h['method_independence_audit']['independent_judgement_demonstrated'] is False;assert h['method_independence_audit']['scores_changed']==h['method_independence_audit']['memberships_changed']==0
assert h['method_independence_audit']['current_defined_tracks']==93 and h['method_independence_audit']['current_singletons']==59 and h['method_independence_audit']['current_multi']==34
assert h['method_independence_audit']['all_three_comparable_singletons']==53
with (ROOT/'06_DECISIONS/decision_register.csv').open(newline='') as f:dec=list(csv.DictReader(f))
assert len({x['decision_id'] for x in dec})==len(dec)
for d in dec:
 if d['status'].lower()=='approved':assert d['approved_by'].strip(),'Approved decision lacks approver'
assert all(d['status']=='provisional' and not d['approved_by'] for d in dec if d['decision_id'].startswith('CERF-IND-'))
events=[json.loads(x) for x in (ROOT/'04_ANALYSIS_LOGS/session_events.jsonl').read_text().splitlines() if x.strip()];assert events and all(e.get('event_id') and e.get('capture') for e in events)
errors=[]
for name in required:
 p=ROOT/name;t=p.read_text()
 # Row-level scores/evidence and credentials do not belong in the publication set.
 assert not re.search(r'ACT[AB]-\d{3}|PCT-[A-F0-9]{16}|\[(?:PERSON|ORGANISATION)\d+\]',t),name
 assert not re.search(r'gh[pousr]_[A-Za-z0-9]{20,}|github_pat_[A-Za-z0-9_]+|AKIA[A-Z0-9]{16}|-----BEGIN [A-Z ]*PRIVATE KEY-----',t),name
 if p.suffix=='.md':
  for dest in re.findall(r'\]\(([^)]+)\)',t):
   if dest.startswith(('http:','https:','mailto:','#')):continue
   dest=dest.split('#',1)[0]
   if dest and not (p.parent/dest).exists():errors.append((name,dest))
assert not errors,errors
appendix=(ROOT/'08_CLIENT_APPENDIX/methodology_DRAFT.md').read_text();assert 'not approved for client circulation' in appendix.lower();assert 'singleton C copied A' in appendix
assert 'independ' in (ROOT/'00_START_HERE.md').read_text().lower()
print(json.dumps({'documentation_checks':'passed','required_files':len(required),'decision_rows':len(dec),'reported_events':len(events),'relative_links':'resolved','no_case_level_records_or_credential_patterns':True,'private_data_access_required':False},indent=2))
