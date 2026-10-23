#!/usr/bin/env python3
"""TEST ONLY: fresh local checkout plus pending overlay; never commit or push."""
import hashlib
import json
from pathlib import Path
import re
import shutil
import subprocess
import sys
import tempfile

BASE = Path(__file__).resolve().parent
ROOT = BASE.parents[2]


def main():
    transcript = []

    def run(cwd, args, expected=0):
        result = subprocess.run(args, cwd=cwd, capture_output=True, text=True)
        transcript.append(dict(command=args, exit_code=result.returncode,
                               stdout=result.stdout, stderr=result.stderr))
        assert result.returncode == expected, transcript[-1]
        return result.stdout.strip()

    with tempfile.TemporaryDirectory(prefix='cerf-fresh-local-') as temporary:
        checkout = Path(temporary) / 'checkout'
        run(ROOT, ['git', 'clone', '--quiet', '--no-hardlinks', str(ROOT), str(checkout)])
        commit = run(checkout, ['git', 'rev-parse', 'HEAD'])
        # No staging, commits or remote writes. Overlay the exact pending candidate.
        for name in ['scripts', 'skill (2)']:
            shutil.copytree(ROOT / name, checkout / name, dirs_exist_ok=True,
                            ignore=shutil.ignore_patterns('__pycache__'))
        shutil.copyfile(ROOT / '.gitignore', checkout / '.gitignore')
        run(checkout, [sys.executable, 'scripts/setup_project.py'])
        state = json.loads((BASE / 'project/handover.json').read_text())
        original = BASE / 'project' / state['latest_report']
        relocated = checkout / '04_ANALYSIS_LOGS/reports/TEST-RELOCATED'
        shutil.copytree(original, relocated)
        manifest = json.loads((relocated / 'snapshot_manifest.json').read_text())
        for relative, expected in manifest['context_sha256'].items():
            assert hashlib.sha256((relocated / relative).read_bytes()).hexdigest() == expected
        documents = ['00_START_HERE.md',
                     '09_INTERNAL_DEEP_DIVE/technical_and_decision_history.md',
                     '08_CLIENT_APPENDIX/methodology_DRAFT.md']
        links = []
        for name in documents:
            page = relocated / name
            for target in re.findall(r'\]\(([^)]+)\)', page.read_text()):
                assert not Path(target).is_absolute()
                assert (page.parent / target).is_file(), (page, target)
                links.append(dict(page=name, target=target))
        # Each snapshot context file must be eligible for normal Git staging.
        for relative in manifest['context_sha256']:
            run(checkout, ['git', 'check-ignore', '-q',
                           str((relocated / relative).relative_to(checkout))], expected=1)
        before = {name: (relocated / name).read_bytes() for name in documents}
        # Regenerate only the disposable relocated copy, never original evidence.
        run(checkout, [sys.executable, 'scripts/refresh_status.py', str(relocated)])
        run(checkout, [sys.executable, 'scripts/build_appendix.py', str(relocated)])
        assert all((relocated / name).read_bytes() == value for name, value in before.items())
        run(checkout, [sys.executable, 'scripts/test_environment.py'])
        run(checkout, [sys.executable, 'scripts/test_audit_workflow.py'])
        result = dict(test_only=True, local_checkout='PASS', source_commit=commit,
                      overlay='Uncommitted pending workflow files and isolated synthetic snapshot',
                      relative_links_verified=links, context_hashes='PASS',
                      validation_register_git_eligibility='PASS', regeneration='PASS',
                      github_checkout='BLOCKED',
                      github_failure='git clone: Failed to connect to proxy port 8080; could not connect to server',
                      remote_updated_version='NOT VERIFIED: changes are uncommitted and unpushed',
                      commands=transcript)
        (BASE / 'portability_results.json').write_text(json.dumps(result, indent=2) + '\n')
        print('PASS: fresh local checkout + pending overlay, 12 relative links, context hashes,')
        print('Git eligibility, deterministic regeneration, legacy and mixed-record regression tests.')
        print('BLOCKED: actual fresh GitHub checkout; proxy unreachable. No commits or pushes.')


if __name__ == '__main__':
    main()
