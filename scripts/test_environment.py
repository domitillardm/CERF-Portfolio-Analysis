#!/usr/bin/env python3
"""Synthetic installation, session continuity and local Git round-trip checks."""
import hashlib
import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile

ROOT = Path(__file__).resolve().parents[1]


def run(cwd, *command, expected=0):
    result = subprocess.run(command, cwd=cwd, text=True, capture_output=True)
    assert result.returncode == expected, (command, result.returncode, result.stdout, result.stderr)
    return result.stdout


def hashes(root):
    return {str(p.relative_to(root)): hashlib.sha256(p.read_bytes()).hexdigest()
            for p in root.rglob('*') if p.is_file() and '.git' not in p.parts}


def main():
    with tempfile.TemporaryDirectory(prefix='cerf-continuity-') as tmp:
        base = Path(tmp)
        first = base / 'session-one'
        first.mkdir()
        for name in ['scripts', 'skill (2)']:
            shutil.copytree(ROOT / name, first / name, symlinks=True,
                            ignore=shutil.ignore_patterns('__pycache__'))
        for name in ['AGENTS.md', '.gitignore', 'ENVIRONMENT.md']:
            shutil.copy2(ROOT / name, first / name)
        run(first, 'git', 'init', '-q')
        run(first, sys.executable, 'scripts/setup_project.py')
        # An existing document and unknown handover field must survive setup.
        handbook = first / '01_METHODOLOGY/PROJECT_EXPLAINED.md'
        handbook.write_text('Synthetic existing colleague-owned context\n')
        state = json.loads((first / 'handover.json').read_text())
        state['custom_context'] = 'Synthetic colleague context'
        (first / 'handover.json').write_text(json.dumps(state))
        before = hashes(first)
        run(first, sys.executable, 'scripts/setup_project.py')
        assert hashes(first) == before, 'Setup changed existing content'

        source = first / '02_ACTIVITY_DATA/synthetic.csv'
        source.write_text('id,value\nSYNTHETIC,1\n')
        output = first / '07_RESULTS/synthetic.csv'
        run(first, sys.executable, 'scripts/audit_run.py', '--root', '.',
            '--task', 'synthetic-success', '--owner', 'fixture', '--rules-version', 'synthetic',
            '--input', str(source), '--output', str(output), '--', sys.executable, '-c',
            "from pathlib import Path; Path('07_RESULTS/synthetic.csv').write_text(Path('02_ACTIVITY_DATA/synthetic.csv').read_text())")
        run(first, sys.executable, 'scripts/audit_run.py', '--root', '.',
            '--task', 'synthetic-failure', '--owner', 'fixture', '--rules-version', 'synthetic',
            '--', sys.executable, '-c', 'raise SystemExit(7)', expected=7)
        records = [json.loads(p.read_text()) for p in (first / '04_ANALYSIS_LOGS').glob('*.json')]
        success = next(r for r in records if r['task'] == 'synthetic-success')
        assert success['inputs'][0]['sha256'] == hashlib.sha256(source.read_bytes()).hexdigest()
        assert success['outputs'][0]['sha256'] == hashlib.sha256(output.read_bytes()).hexdigest()
        assert next(r for r in records if r['task'] == 'synthetic-failure')['status'] == 'failed'
        decisions = first / '06_DECISIONS/decision_register.csv'
        with decisions.open('a') as stream:
            stream.write('TEST,,Synthetic provisional decision,fixture,provisional,\n')
        finalize = [sys.executable, 'scripts/finish_session.py', '--actor', 'fixture',
                    '--summary', 'Synthetic checks only', '--next-action', 'Continue synthetic test',
                    '--blocker', 'none']
        run(first, *finalize, '--session', 'SYNTHETIC-ONE')
        state = json.loads((first / 'handover.json').read_text())
        old_report = first / state['latest_report']
        assert json.loads((old_report / 'handover_before.json').read_text())['custom_context'] == state['custom_context']
        assert '2 instrumented runs' in (old_report / '00_START_HERE.md').read_text()
        client = (old_report / '08_CLIENT_APPENDIX/methodology_DRAFT.md').read_text()
        assert 'Not approved for client circulation' in client
        assert 'Synthetic provisional decision' not in client
        assert 'Synthetic provisional decision' in (old_report / '09_INTERNAL_DEEP_DIVE/technical_and_decision_history.md').read_text()
        frozen = hashes(old_report)
        # Ignore checks do not require creating credentials or private contents.
        for path in ['02_ACTIVITY_DATA/synthetic.csv', '07_RESULTS/synthetic.csv',
                     '.env', '.env.local', 'private/notes.md', 'credentials.json',
                     'anywhere/data.csv', 'anywhere/data.xlsx', 'tmp/file.txt']:
            run(first, 'git', 'check-ignore', '-q', path)
        for path in ['AGENTS.md', 'handover.json', '04_ANALYSIS_LOGS/session_events.jsonl',
                     '06_DECISIONS/decision_register.csv', '05_VALIDATION/activity_scoring_register.csv']:
            run(first, 'git', 'check-ignore', '-q', path, expected=1)

        # Only synthetic fixtures are committed to this temporary local remote.
        selected = ['AGENTS.md', '.gitignore', 'ENVIRONMENT.md', 'scripts', 'skill (2)',
                    '00_START_HERE.md', 'handover.json', '01_METHODOLOGY', '02_ACTIVITY_DATA/README.md',
                    '04_ANALYSIS_LOGS', '05_VALIDATION', '06_DECISIONS', '07_RESULTS/README.md']
        run(first, 'git', 'add', '--', *selected)
        run(first, 'git', '-c', 'user.name=Synthetic Test', '-c', 'user.email=synthetic@example.invalid',
            '-c', 'core.hooksPath=/dev/null', 'commit', '-qm', 'Synthetic continuity fixture')
        remote = base / 'remote.git'
        run(base, 'git', 'init', '--bare', '-q', str(remote))
        run(first, 'git', 'push', str(remote), 'HEAD:refs/heads/main')
        second = base / 'session-two'
        run(base, 'git', 'clone', '-q', '--branch', 'main', str(remote), str(second))
        assert run(first, 'git', 'rev-parse', 'HEAD') == run(second, 'git', 'rev-parse', 'HEAD')
        assert hashes(second / state['latest_report']) == frozen
        assert not (second / '02_ACTIVITY_DATA/synthetic.csv').exists()
        assert not (second / '07_RESULTS/synthetic.csv').exists()
        before = hashes(second)
        run(second, sys.executable, 'scripts/setup_project.py')
        assert hashes(second) == before, 'Setup changed restored files'
        run(second, *finalize, '--session', 'SYNTHETIC-TWO')
        new_state = json.loads((second / 'handover.json').read_text())
        assert new_state['latest_session'] == 'SYNTHETIC-TWO'
        assert new_state['custom_context'] == 'Synthetic colleague context'
        assert new_state['latest_report'] != state['latest_report']
        assert hashes(second / state['latest_report']) == frozen
        assert (second / '01_METHODOLOGY/PROJECT_EXPLAINED.md').read_text() == handbook.read_text()
        assert (second / '06_DECISIONS/decision_register.csv').read_bytes() == decisions.read_bytes()
        events = [json.loads(line) for line in (second / '04_ANALYSIS_LOGS/session_events.jsonl').read_text().splitlines()]
        assert [e['session'] for e in events] == ['SYNTHETIC-ONE', 'SYNTHETIC-TWO']
    print('PASS: idempotent setup; existing documentation preserved; audit hashes and failed exits;')
    print('versioned reports and handover history; provisional decision filtering; ignore rules;')
    print('local Git commit/push/fresh-clone continuity; second-session log append and retained context.')
    print('Simulation only: no hosted session restoration or GitHub push was performed.')


if __name__ == '__main__':
    main()
