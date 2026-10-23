#!/usr/bin/env python3
"""Append privacy-conscious session events. No raw prompts or source text."""
import argparse, datetime as dt, json, pathlib, uuid

from audit_metadata import add_arguments, metadata

def main():
 p=argparse.ArgumentParser();p.add_argument('--root',default='.');p.add_argument('--session',required=True);p.add_argument('--actor',required=True);p.add_argument('--kind',required=True,choices=['discussion','experiment','decision','error','correction','validation','handover','other']);p.add_argument('--summary',required=True);p.add_argument('--why',default='');p.add_argument('--evidence',default='');p.add_argument('--next',default='');p.add_argument('--status',choices=['provisional','approved','rejected','open'],default='provisional');add_arguments(p);a=p.parse_args();meta=metadata(a,p)
 root=pathlib.Path(a.root);d=root/'04_ANALYSIS_LOGS';d.mkdir(parents=True,exist_ok=True)
 rec={'event_id':str(uuid.uuid4()),'utc':dt.datetime.now(dt.timezone.utc).isoformat(),'session':a.session,'actor':a.actor,'kind':a.kind,'summary':a.summary,'rationale':a.why,'evidence_reference':a.evidence,'next_action':a.next,'status':a.status,'capture':'agent_or_human_reported_not_independently_verified'}
 rec.update(meta)
 with (d/'session_events.jsonl').open('a',encoding='utf8') as f:f.write(json.dumps(rec,ensure_ascii=False)+'\n')
 print(rec['event_id'])
if __name__=='__main__':main()
