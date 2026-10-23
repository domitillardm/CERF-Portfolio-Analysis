#!/usr/bin/env python3
"""Regression tests using invented records only; no commits, pushes or real data."""
import csv
import hashlib
import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile

ROOT = Path(__file__).resolve().parents[1]


def main():
    with tempfile.TemporaryDirectory(prefix='cerf-audit-regression-') as temporary:
        base = Path(temporary)
        project = base / 'project'
        project.mkdir()
        for name in ['scripts', 'skill (2)']:
            shutil.copytree(ROOT / name, project / name, symlinks=True,
                            ignore=shutil.ignore_patterns('__pycache__'))

        def run(*args, expected=0, cwd=project):
            result = subprocess.run([sys.executable, *args], cwd=cwd,
                                    capture_output=True, text=True)
            assert result.returncode == expected, (args, result.stdout, result.stderr)
            return result

        run('scripts/setup_project.py')
        source = project / 'fixture.json'
        source.write_text('{"test_only": true}\n')
        audit = [str(project / 'scripts/audit_run.py'), '--root', str(project),
                 '--task', 'TEST ONLY regression', '--owner', 'fixture',
                 '--rules-version', 'TEST-ONLY-v1', '--input', 'fixture.json']
        # Run outside --root: fingerprints must resolve in the execution root.
        run(*audit, '--session', 'TEST', '--synthetic', '--', sys.executable,
            '-c', 'pass', cwd=base)
        # Old CLI remains valid but is explicitly unclassified.
        run(*audit, '--', sys.executable, '-c', 'pass')
        run(*audit, '--synthetic', '--', sys.executable, '-c', 'pass', expected=2)
        run(*audit, '--session', 'TEST', '--synthetic', '--portfolio-analysis',
            '--', sys.executable, '-c', 'pass', expected=2)
        records = [json.loads(p.read_text()) for p in (project / '04_ANALYSIS_LOGS').glob('*.json')]
        assert len(records) == 2
        assert all(r['inputs'][0]['sha256'] == hashlib.sha256(source.read_bytes()).hexdigest()
                   for r in records)
        # This is a declared-portfolio metadata FIXTURE, not a real analysis run.
        # It exercises the summary branch without executing portfolio analysis.
        log = project / '04_ANALYSIS_LOGS/declared-fixture.json'
        log.write_text(json.dumps(dict(run_id='TEST-DECLARED-FIXTURE', session='TEST-MIXED',
                                     test_only=False, status='completed', exit_code=0)))
        # A pre-schema historical record must remain byte-for-byte unchanged.
        legacy = project / '04_ANALYSIS_LOGS/legacy-fixture.json'
        legacy.write_text('{"run_id":"TEST-LEGACY-FIXTURE","status":"completed"}\n')
        legacy_before = legacy.read_bytes()
        decisions = project / '06_DECISIONS/decision_register.csv'
        with decisions.open('w', newline='') as stream:
            writer = csv.writer(stream)
            writer.writerow(['decision_id', 'date', 'decision', 'rationale', 'status',
                             'approved_by', 'session', 'test_only'])
            writer.writerow(['TEST-SYNTHETIC-APPROVED', '', 'must stay excluded', '',
                             'approved', 'fixture', 'TEST', 'true'])
            writer.writerow(['TEST-LEGACY-APPROVED', '', 'unknown provenance', '',
                             'approved', 'fixture', '', ''])
        finalize = ['scripts/finish_session.py', '--session', 'TEST-MIXED', '--actor', 'fixture',
                    '--summary', 'TEST ONLY mixed metadata fixture', '--next-action', 'review',
                    '--blocker', 'TEST ONLY no real analysis']
        run(*finalize)
        state = json.loads((project / 'handover.json').read_text())
        report = project / state['latest_report']
        paths = ['00_START_HERE.md', '09_INTERNAL_DEEP_DIVE/technical_and_decision_history.md',
                 '08_CLIENT_APPENDIX/methodology_DRAFT.md']
        for name in paths:
            text = (report / name).read_text()
            assert '1 declared portfolio-analysis; 1 synthetic TEST ONLY' in text
            assert '2 unclassified legacy/unspecified (excluded)' in text
        client = (report / paths[2]).read_text()
        assert 'TEST-SYNTHETIC-APPROVED' not in client
        assert 'TEST-LEGACY-APPROVED' not in client
        assert legacy.read_bytes() == legacy_before
        handover_before = (project / 'handover.json').read_bytes()
        events_before = (project / '04_ANALYSIS_LOGS/session_events.jsonl').read_bytes()
        (project / '05_VALIDATION/issues.md').unlink()
        run(*finalize, expected=1)
        assert (project / 'handover.json').read_bytes() == handover_before
        assert (project / '04_ANALYSIS_LOGS/session_events.jsonl').read_bytes() == events_before
    print('PASS: mixed/legacy separation, decision exclusion, required session/flag validation,')
    print('root-relative hashes, immutable legacy records, missing-context preflight; no Git writes.')


if __name__ == '__main__':
    main()
