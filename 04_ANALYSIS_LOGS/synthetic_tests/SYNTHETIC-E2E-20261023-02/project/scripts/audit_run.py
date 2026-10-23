#!/usr/bin/env python3
"""Capture verifiable command execution and input/output fingerprints."""
import argparse, datetime as dt, hashlib, json, os, pathlib, subprocess, sys, uuid

from audit_metadata import add_arguments, metadata

def digest(path, root):
    p=pathlib.Path(path)
    if not p.is_absolute(): p=root/p
    if not p.is_file(): return {"path":str(p),"exists":False}
    h=hashlib.sha256()
    with p.open('rb') as f:
        for block in iter(lambda:f.read(1024*1024),b''): h.update(block)
    return {"path":str(p),"exists":True,"bytes":p.stat().st_size,"sha256":h.hexdigest()}

def main():
    a=argparse.ArgumentParser()
    a.add_argument('--root',default='.')
    a.add_argument('--session')
    add_arguments(a)
    a.add_argument('--task',required=True)
    a.add_argument('--owner',required=True)
    a.add_argument('--rules-version',required=True)
    a.add_argument('--input',action='append',default=[])
    a.add_argument('--output',action='append',default=[])
    a.add_argument('command',nargs=argparse.REMAINDER)
    x=a.parse_args(); cmd=x.command[1:] if x.command[:1]==['--'] else x.command
    if not cmd: a.error('Provide a command after --')
    meta=metadata(x,a)
    root=pathlib.Path(x.root).resolve(); folder=root/'04_ANALYSIS_LOGS'; folder.mkdir(parents=True,exist_ok=True)
    now=lambda:dt.datetime.now(dt.timezone.utc).isoformat()
    record={'run_id':str(uuid.uuid4()),'task':x.task,'owner':x.owner,'rules_version':x.rules_version,'started_utc':now(),'command':cmd,'inputs':[digest(v,root) for v in x.input], 'status':'running'}
    record.update(meta)
    # Do not log environment variables or file contents. Review command arguments for secrets.
    try:
        result=subprocess.run(cmd,cwd=root,check=False,stdout=subprocess.PIPE,stderr=subprocess.PIPE,text=True,errors='replace')
        record['exit_code']=result.returncode
        record['status']='completed' if result.returncode==0 else 'failed'
        # Store only digests of console streams to avoid accidental disclosure.
        record['stdout_sha256']=hashlib.sha256(result.stdout.encode()).hexdigest()
        record['stderr_sha256']=hashlib.sha256(result.stderr.encode()).hexdigest()
        sys.stdout.write(result.stdout); sys.stderr.write(result.stderr)
    except Exception as e:
        record['status']='execution_error';record['error_type']=type(e).__name__;record['exit_code']=127
    record['ended_utc']=now();record['outputs']=[digest(v,root) for v in x.output]
    path=folder/(record['started_utc'][:10]+'_'+record['run_id']+'.json')
    path.write_text(json.dumps(record,indent=2)+'\n',encoding='utf-8')
    print('AUDIT_RECORD='+str(path),file=sys.stderr)
    return record['exit_code']
if __name__=='__main__': sys.exit(main())
