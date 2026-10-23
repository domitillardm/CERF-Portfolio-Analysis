#!/usr/bin/env python3
"""Finalize a session with retained handover history and new report versions."""
import argparse
import datetime as dt
import json
from pathlib import Path
import shutil
import subprocess
import sys
import uuid

ROOT = Path(__file__).resolve().parents[1]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    for field in ['session', 'actor', 'summary', 'next-action', 'blocker']:
        parser.add_argument('--' + field, required=True)
    args = parser.parse_args()
    handover = ROOT / 'handover.json'
    prior = handover.read_bytes()
    state = json.loads(prior)
    if not isinstance(state, dict):
        raise ValueError('handover.json must contain an object')
    version = dt.datetime.now(dt.timezone.utc).strftime('%Y%m%dT%H%M%SZ') + '_' + uuid.uuid4().hex
    reports = ROOT / '04_ANALYSIS_LOGS' / 'reports' / version
    reports.mkdir(parents=True)
    # Retain exact bytes, including unknown user fields, before updating status.
    (reports / 'handover_before.json').write_bytes(prior)
    subprocess.run([sys.executable, str(ROOT / 'scripts/session_log.py'), '--root', str(ROOT),
        '--session', args.session, '--actor', args.actor, '--kind', 'handover',
        '--summary', args.summary, '--next', args.next_action, '--status', 'provisional'], check=True)
    state.update(next_action=args.next_action, blocker=args.blocker,
                 latest_session=args.session, latest_report=str(reports.relative_to(ROOT)))
    # Generate in a new folder so existing documentation and analysis survive.
    (reports / 'handover.json').write_text(json.dumps(state, indent=2) + '\n', encoding='utf-8')
    shutil.copytree(ROOT / '04_ANALYSIS_LOGS', reports / '04_ANALYSIS_LOGS',
                    ignore=shutil.ignore_patterns('reports'))
    shutil.copytree(ROOT / '06_DECISIONS', reports / '06_DECISIONS')
    for script in ['refresh_status.py', 'build_appendix.py']:
        subprocess.run([sys.executable, str(ROOT / 'scripts' / script), str(reports)], check=True)
    # Update only the machine-readable handover after successful report generation;
    # prior handover and every generated report version remain available.
    handover.write_text(json.dumps(state, indent=2) + '\n', encoding='utf-8')
    print('Session reports:', reports.relative_to(ROOT))
    print('Files are local only until reviewed, committed and verified on the remote.')


if __name__ == '__main__':
    main()
