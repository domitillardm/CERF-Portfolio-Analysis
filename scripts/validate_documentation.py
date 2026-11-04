#!/usr/bin/env python3
"""Validate the current public handover; optional restricted checks never print evidence."""
import argparse
import csv
import hashlib
import json
import re
import subprocess
from pathlib import Path
from urllib.parse import unquote

PUBLIC_FILES = [
    '.gitignore', 'AGENTS.md', 'README.md', '00_START_HERE.md', 'handover.json',
    '01_METHODOLOGY/scoring_rules.md',
    '01_METHODOLOGY/OPERATIONALISATION_CURRENT.md',
    '01_METHODOLOGY/PROJECT_EXPLAINED.md',
    '01_METHODOLOGY/SCORING_CODEBOOK_DRAFT_v0.2.md',
    '01_METHODOLOGY/CALIBRATION_ADDENDUM_v0.2-F1.md',
    '02_ACTIVITY_DATA/README.md',
    '02_ACTIVITY_DATA/restricted_manifest_20261104_v1.json',
    '04_ANALYSIS_LOGS/documentation_update_20261104.json',
    '05_VALIDATION/issues.md', '05_VALIDATION/project_state_20261104.md',
    '05_VALIDATION/documentation_publication_20261104.md',
    '06_DECISIONS/decision_register.csv', '06_DECISIONS/README.md',
    '07_RESULTS/README.md', '08_CLIENT_APPENDIX/methodology_DRAFT.md',
    '09_INTERNAL_DEEP_DIVE/technical_and_decision_history.md',
    'scripts/validate_documentation.py',
]
SOURCE_COMMIT = '12c46a05d546fe01c02792b06c9928e2779d9422'


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def read_rows(path):
    with path.open(newline='') as stream:
        return list(csv.DictReader(stream))


def validate(root, private=False, staged=False):
    for name in PUBLIC_FILES:
        assert (root / name).is_file(), name
    handover = json.loads((root / 'handover.json').read_text())
    status = handover['verified_status']
    assert status['activity_count'] == 182
    assert status['score_counts'] == {'1': 12, '2': 41, '3': 18, '4': 55, '6': 2}
    assert status['achievement_count'] == 126 and status['unscored'] == 54
    assert sum(status['score_counts'].values()) + status['unscored'] == 182
    assert status['provisional_numeric_maxima'] + status['pending_maxima'] == status['country_track_groups'] == 51
    assert status['completed_human_score_reviews'] == status['completed_human_decisions'] == 0
    assert status['human_validation_complete'] is False
    assert handover['methodology']['achievement_codes'] == [1, 2, 3, 4]
    assert handover['methodology']['information_code'] == 6
    assert handover['methodology']['future_potential'] == ['Yes', 'No']
    assert handover['methodology']['no_contextual_or_holistic_scoring'] is True
    assert handover['approval']['full_provisional_execution_completed'] is True
    assert handover['approval']['merge_authorised'] is False
    assert handover['approval']['confidential_data_upload_authorised'] is False
    manifest = json.loads((root / handover['restricted_manifest']).read_text())
    assets = manifest['files']
    assert len({x['reference'] for x in assets}) == len(assets) == 20
    assert all(not x['in_git'] and re.fullmatch('[a-f0-9]{64}', x['sha256']) for x in assets)
    decisions = read_rows(root / '06_DECISIONS/decision_register.csv')
    assert len(decisions) == 67 and len({x['decision_id'] for x in decisions}) == 67
    assert sum(x['status'] == 'approved_working' for x in decisions) == 7
    assert all(x['approved_by'] for x in decisions if x['status'].startswith('approved'))
    assert all(x['status'] == 'provisional' for x in decisions[:60])
    # In a Git checkout, verify exact historical decision continuity and source bytes.
    historical_verified = False
    probe = subprocess.run(['git', 'cat-file', '-e', SOURCE_COMMIT], cwd=root, capture_output=True)
    if probe.returncode == 0:
        import io
        old = subprocess.check_output(['git', 'show', SOURCE_COMMIT + ':06_DECISIONS/decision_register.csv'], cwd=root).decode()
        assert decisions[:60] == list(csv.DictReader(io.StringIO(old)))
        for name in ['SCORING_CODEBOOK_DRAFT_v0.2.md', 'CALIBRATION_ADDENDUM_v0.2-F1.md']:
            old_bytes = subprocess.check_output(['git', 'show', SOURCE_COMMIT + ':01_METHODOLOGY/' + name], cwd=root)
            assert (root / '01_METHODOLOGY' / name).read_bytes() == old_bytes
        historical_verified = True
    link_count = 0
    for name in PUBLIC_FILES:
        path = root / name
        text = path.read_text()
        # Reject case-level records and secrets; this is supplemented by manual diff review.
        # A split spelling prevents these test literals from matching the validator itself.
        case_pattern = r'ACT' + r'(?:A|B)?-\d{3,}|PCT-[A-Fa-f0-9]{10,}|\[(?:PERSON|ORGANISATION)\d+\]'
        secret_pattern = r'gh[pousr]' + r'_[A-Za-z0-9]{20,}|github_pat_[A-Za-z0-9_]{20,}|AKIA[A-Z0-9]{16}|-----BEGIN [A-Z ]*PRIVATE KEY-----'
        assert not re.search(case_pattern, text), ('case-level identifier', name)
        assert not re.search(secret_pattern, text), ('credential marker', name)
        if path.suffix == '.json':
            json.loads(text)
        if path.suffix == '.md':
            for dest in re.findall(r'\]\(([^)]+)\)', text):
                if dest.startswith(('http:', 'https:', 'mailto:', '#')):
                    continue
                dest = unquote(dest.split('#', 1)[0])
                assert (path.parent / dest).is_file(), (name, dest)
                link_count += 1
    codebook = (root / '01_METHODOLOGY/SCORING_CODEBOOK_DRAFT_v0.2.md').read_text()
    for phrase in ['Activity described', 'Output delivered', 'Concrete use or follow-up reported', 'Change in an external actor reported', 'Insufficient information']:
        assert phrase in codebook
    rules = (root / '01_METHODOLOGY/scoring_rules.md').read_text()
    assert all(label in rules for label in handover['methodology']['evidence_basis'])
    assert 'not an achievement' in rules
    assert 'pending' in rules and '1–4 only' in rules
    assert 'pending' in (root / '00_START_HERE.md').read_text().lower()
    staged_count = 0
    if staged:
        changes = subprocess.check_output(['git', 'diff', '--cached', '--name-only', '-z'], cwd=root).decode().split('\0')
        for name in filter(None, changes):
            assert name in PUBLIC_FILES, ('unreviewed path in index', name)
            data = subprocess.check_output(['git', 'show', ':' + name], cwd=root)
            assert b'\0' not in data, ('binary in staged text', name)
            assert data == (root / name).read_bytes(), ('index differs from checked file', name)
            assert not re.search(case_pattern, data.decode()), ('staged case identifier', name)
            assert not re.search(secret_pattern, data.decode()), ('staged credential', name)
            staged_count += 1
        assert staged_count > 0, 'No staged publication set'
    private_count = 0
    if private:
        for item in assets:
            path = Path(item['workspace_locator'])
            assert path.is_file() and digest(path) == item['sha256'], item['reference']
            assert path.stat().st_size == item['bytes']
            private_count += 1
        loc = {x['reference']: Path(x['workspace_locator']) for x in assets}
        scoring = read_rows(loc['SCORING-ROWS-20261104-01'])
        assert len(scoring) == len({x['Activity Code'] for x in scoring}) == 182
        assert {k: sum(x['AI Score'] == k for x in scoring) for k in ['1', '2', '3', '4', '6', '']} == {**status['score_counts'], '': 54}
        assert not any(x['Human-reviewed score'] for x in scoring)
        for ref in ['QA-FULL-20261104-01', 'QA-REPLAY-20261104-01', 'AU-QA-20261104-001']:
            assert json.loads(loc[ref].read_text())['passed'] is True
        for ref, name in [('CODEBOOK-SNAPSHOT-20261104-01', 'SCORING_CODEBOOK_DRAFT_v0.2.md'), ('F1-SNAPSHOT-20261104-01', 'CALIBRATION_ADDENDUM_v0.2-F1.md')]:
            assert loc[ref].read_text().rstrip() == (root / '01_METHODOLOGY' / name).read_text().rstrip()
    return {'passed': True, 'public_files_checked': len(PUBLIC_FILES), 'relative_links_resolved': link_count,
            'historical_decisions_and_source_bytes_verified': historical_verified,
            'restricted_files_hash_checked': private_count, 'staged_files_checked': staged_count,
            'classification': 'Technical documentation/privacy controls; not human result validation'}


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root', type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument('--verify-restricted', action='store_true')
    parser.add_argument('--staged', action='store_true')
    args = parser.parse_args()
    print(json.dumps(validate(args.root.resolve(), args.verify_restricted, args.staged), indent=2))
