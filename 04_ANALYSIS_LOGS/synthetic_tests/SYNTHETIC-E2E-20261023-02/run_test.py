#!/usr/bin/env python3
"""TEST ONLY: isolated CERF documentation acceptance test; no Git mutations."""
import csv
import hashlib
import json
from pathlib import Path
import shutil
import subprocess
import sys

BASE = Path(__file__).resolve().parent
ROOT = BASE.parents[2]
PROJECT = BASE / 'project'
SESSION = BASE.name
ACTOR = 'synthetic-test-agent'


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def write(path, value):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(value, encoding='utf-8')


def json_write(path, value):
    write(path, json.dumps(value, indent=2) + '\n')


commands = []


def run(cwd, args, expected=0):
    result = subprocess.run(args, cwd=cwd, capture_output=True, text=True)
    commands.append(dict(cwd=str(cwd), command=args, expected_exit=expected,
                         actual_exit=result.returncode, stdout=result.stdout,
                         stderr=result.stderr))
    json_write(BASE / 'command_transcript.json', commands)
    assert result.returncode == expected, commands[-1]
    return result


def event(kind, summary, why='', evidence='', next_action='Review TEST ONLY documentation gaps'):
    run(PROJECT, [sys.executable, 'scripts/session_log.py', '--root', '.',
        '--session', SESSION, '--synthetic', '--actor', ACTOR, '--kind', kind,
        '--summary', 'TEST ONLY; NOT APPROVED. ' + summary, '--why', why,
        '--evidence', evidence, '--next', next_action, '--status', 'provisional'])


def main():
    assert not PROJECT.exists(), 'Use a new session folder for every invocation'
    # Hash documentation/code only. Never open real source datasets or results.
    protected = []
    for folder in ['01_METHODOLOGY', '04_ANALYSIS_LOGS', '05_VALIDATION',
                   '06_DECISIONS', '08_CLIENT_APPENDIX', '09_INTERNAL_DEEP_DIVE',
                   'scripts', 'skill (2)']:
        protected.extend(p for p in (ROOT / folder).rglob('*')
                         if p.is_file() and BASE not in p.parents and '__pycache__' not in p.parts)
    protected.extend(ROOT / p for p in ['AGENTS.md', '00_START_HERE.md', 'handover.json', 'ENVIRONMENT.md'])
    baseline = {str(p.relative_to(ROOT)): digest(p) for p in protected}
    json_write(BASE / 'protected_before.json', baseline)
    run(ROOT, [sys.executable, 'scripts/setup_project.py'])
    PROJECT.mkdir()
    for name in ['setup_project.py', 'finish_session.py', 'session_log.py',
                 'audit_run.py', 'refresh_status.py', 'build_appendix.py', 'audit_metadata.py']:
        target = PROJECT / 'scripts' / name
        target.parent.mkdir(exist_ok=True)
        shutil.copyfile(ROOT / 'scripts' / name, target)
    run(PROJECT, [sys.executable, 'scripts/setup_project.py'])
    script_hashes = {p.name: {'source': digest(ROOT / 'scripts' / p.name), 'copy': digest(p)}
                     for p in (PROJECT / 'scripts').glob('*.py')}
    assert all(v['source'] == v['copy'] for v in script_hashes.values())
    json_write(BASE / 'script_provenance.json', script_hashes)
    state = json.loads((PROJECT / 'handover.json').read_text())
    state.update(purpose='TEST ONLY synthetic documentation workflow; no CERF analysis',
                 phase='TEST ONLY; NOT APPROVED', owner=ACTOR,
                 custom_test_context='TEST ONLY unknown handover field must survive',
                 next_action='TEST ONLY baseline next action', blocker='TEST ONLY no approved methodology')
    json_write(PROJECT / 'handover.json', state)
    prior_handover = (PROJECT / 'handover.json').read_bytes()
    prior_report = PROJECT / '04_ANALYSIS_LOGS/reports/SYNTHETIC-PRIOR-FIXTURE'
    write(prior_report / 'README.md', '# TEST ONLY prior report sentinel\nPreserve these exact bytes.\n')
    prior_report_hash = digest(prior_report / 'README.md')
    decisions = PROJECT / '06_DECISIONS/decision_register.csv'
    with decisions.open('a', newline='') as stream:
        csv.writer(stream).writerow(['TEST-PRIOR-REJECTED', '2026-10-23',
            'TEST ONLY prior rejected fixture; never a CERF rule',
            'Preservation sentinel', 'rejected', ''])
    prior_decisions = decisions.read_bytes()
    event('discussion', 'Objective: test end-to-end documentation and audit capture. Scope: invented labels only; no real CERF inputs, scores, rule changes or publication.',
          'Validate documentation behavior independently of substantive CERF analysis.')
    event('discussion', 'SIMULATED discussion, not real participants: Approach A uses exact label equality; approach B uses token membership. On invented alpha and alpha beta, A treats the mixed label as unclassified, while B assigns alpha. A preserves ambiguity; B increases coverage but may overclassify.',
          'Exercise recording alternatives, tradeoffs and uncertainty without choosing a real CERF methodology.')
    decision = [SESSION + '-D1', '2026-10-23',
                'TEST ONLY; NOT APPROVED: provisionally use exact matching as the demonstration baseline',
                'TEST ONLY: expose mixed-label ambiguity; token matching remains a comparator; no CERF rule is adopted',
                'provisional', '']
    with decisions.open('a', newline='') as stream:
        csv.writer(stream).writerow(decision)
    event('decision', decision[2], decision[3], '06_DECISIONS/decision_register.csv')
    json_write(PROJECT / 'fixtures/labels.json', {'test_only': True, 'version': 'SYNTHETIC-v1',
               'records': [{'id': 'TEST-001', 'label': 'alpha'}, {'id': 'TEST-002', 'label': 'alpha beta'}]})
    write(PROJECT / 'experiment.py', '''"""TEST ONLY: invented labels; never CERF scoring."""
import json
from pathlib import Path
import sys
fixture = json.loads(Path('fixtures/labels.json').read_text())
assert fixture['test_only'] is True
records = fixture['records']
if sys.argv[1] == 'fail':
    print('TEST ONLY intentional failure: expected 3 invented records, observed ' + str(len(records)), file=sys.stderr)
    raise SystemExit(7 if len(records) != 3 else 0)
assert len(records) == 2
output = {'test_only': True, 'approved': False, 'dataset_version': fixture['version'],
          'rules_version': 'TEST-ONLY-demo-v1', 'records': [dict(id=r['id'],
          exact='alpha' if r['label'] == 'alpha' else 'unclassified',
          token='alpha' if 'alpha' in r['label'].split() else 'unclassified',
          uncertainty='Invented fixture; no CERF inference; mixed labels require review',
          evidence='fixtures/labels.json#' + r['id'], reviewer='NOT ASSIGNED',
          validation_state='TEST ONLY; NOT APPROVED') for r in records]}
assert sum(r['exact'] != r['token'] for r in output['records']) == 1
Path('outputs').mkdir(exist_ok=True)
Path('outputs/success.json').write_text(json.dumps(output, indent=2) + '\\n')
print('TEST ONLY success: 2 invented records; 1 designed disagreement; no real result')
''')
    for mode, expected in [('success', 0), ('fail', 7)]:
        output = 'outputs/success.json' if mode == 'success' else 'outputs/never_created.json'
        run(PROJECT, [sys.executable, 'scripts/audit_run.py', '--root', '.',
            '--session', SESSION, '--synthetic', '--task', SESSION + '-' + mode, '--owner', ACTOR,
            '--rules-version', 'TEST-ONLY-demo-v1', '--input', 'fixtures/labels.json',
            '--input', 'experiment.py', '--output', output,
            '--', sys.executable, 'experiment.py', mode], expected=expected)
    runs = [json.loads(p.read_text()) for p in (PROJECT / '04_ANALYSIS_LOGS').glob('*.json')]
    success = next(r for r in runs if r['task'].endswith('-success'))
    failure = next(r for r in runs if r['task'].endswith('-fail'))
    event('experiment', 'Success attempt exited 0: two invented records yielded one designed disagreement; this checks plumbing, not classification accuracy.',
          'Confirm command, input/code/output fingerprints and successful audit capture.', success['run_id'])
    event('error', 'Intentional failure exited 7: expected three invented records but fixture contains two. Failure output was deliberately never created. This is the expected negative test, not a failed CERF analysis.',
          'Exercise failed-command capture and missing-output recording; fixture was not corrupted.', failure['run_id'])
    event('validation', 'Two audit attempts captured with commands, exit codes, fingerprints and stream hashes. Only summaries and wrapped experiments are captured. The command transcript records scripted subprocesses including setup, event logging, audit runs and finalization; repository reads, fixture authoring and later report inspection are not captured there.',
          'Explain capture boundaries and avoid claiming complete automatic logging.', '../command_transcript.json')
    summary = ('TEST ONLY; NOT APPROVED. Synthetic comparison of exact and token matching completed; '
               'one provisional demonstration decision, no real CERF scoring. Success exit 0; '
               'intentional failure exit 7 because expected 3 invented records but observed 2. '
               'Failure created no output. Inspect reports for isolation, explanations and broken links; '
               'capture covers reported summaries and wrapped commands only.')
    run(PROJECT, [sys.executable, 'scripts/finish_session.py', '--session', SESSION, '--synthetic',
        '--actor', ACTOR, '--summary', summary,
        '--next-action', 'TEST ONLY: review acceptance results and proposed script changes; no commit, push or client release authorized.',
        '--blocker', 'TEST ONLY documentation acceptance review pending; real dataset, owner and approved rules remain NOT YET CONFIRMED.'])
    updated = json.loads((PROJECT / 'handover.json').read_text())
    report = PROJECT / updated['latest_report']
    overview = (report / '00_START_HERE.md').read_text()
    internal = (report / '09_INTERNAL_DEEP_DIVE/technical_and_decision_history.md').read_text()
    client = (report / '08_CLIENT_APPENDIX/methodology_DRAFT.md').read_text()
    checks = {}
    def check(name, condition):
        checks[name] = 'PASS' if condition else 'FAIL'
    check('Unmodified copies of current workflow scripts', all(v['source'] == v['copy'] for v in script_hashes.values()))
    check('Success audit has exit 0 and matching input/output fingerprints', success['status'] == 'completed' and success['exit_code'] == 0 and success['inputs'][0]['sha256'] == digest(PROJECT / 'fixtures/labels.json') and success['outputs'][0]['sha256'] == digest(PROJECT / 'outputs/success.json'))
    check('Intentional failure has exit 7 and absent output', failure['status'] == 'failed' and failure['exit_code'] == 7 and failure['outputs'][0]['exists'] is False)
    check('Prior handover exact bytes and unknown context preserved', (report / 'handover_before.json').read_bytes() == prior_handover and updated['custom_test_context'] == state['custom_test_context'])
    check('Prior synthetic report and decision preserved', digest(prior_report / 'README.md') == prior_report_hash and decisions.read_bytes().startswith(prior_decisions) and (report / '06_DECISIONS/decision_register.csv').read_bytes() == decisions.read_bytes())
    check('Prior real documentation, reports, decisions, handover and scripts unchanged', all((ROOT / p).exists() and digest(ROOT / p) == h for p, h in baseline.items()))
    check('Internal history includes alternatives, rationale, failure and next steps', all(s.lower() in internal.lower() for s in ['Approach A', 'Approach B', 'Why:', 'expected three', 'Next:', 'TEST ONLY', 'NOT APPROVED', 'TEST-PRIOR-REJECTED', decision[0]]))
    check('Overview explains what happened, failure reason and next steps', all(s in overview for s in ['TEST ONLY', 'expected 3', 'observed 2', 'Next action', 'exit 7']))
    check('Client draft excludes provisional decision and synthetic classification findings', decision[0] not in client and 'designed disagreement' not in client and 'Not approved for client circulation' in client and 'No approved decisions recorded' in client)
    check('Client draft explicitly labels its execution count as synthetic TEST ONLY', all('0 declared portfolio-analysis; 2 synthetic TEST ONLY' in text for text in [overview, internal, client]))
    check('Generated overview methodology and validation references resolve within report', all((report / p).is_file() for p in ['01_METHODOLOGY/PROJECT_EXPLAINED.md', '01_METHODOLOGY/scoring_rules.md', '05_VALIDATION/issues.md']))
    check('Experiment audit records have structured session and synthetic markers', all(r.get('session') == SESSION and r.get('test_only') is True for r in runs))
    json_write(BASE / 'acceptance_results.json', {'test_only': True, 'session': SESSION,
        'report': str(report.relative_to(ROOT)), 'checks': checks,
        'limitations': ['Real project register was empty; nonempty preservation checked with a rejected synthetic sentinel.',
                       'No real CERF data, commits, pushes, publication, hosted-session or remote persistence checks. Fresh GitHub clone attempted separately; see portability evidence.']})
    lines = ['# TEST ONLY — documentation workflow acceptance review', '',
        'NOT APPROVED. Synthetic invented labels only; no CERF findings. No commit, push or publication performed.', '',
        f'Session: `{SESSION}`. Generated report: `{report.relative_to(BASE)}`.', '',
        'Overall: ' + ('PASS — all 12 local checks.' if all(v == 'PASS' for v in checks.values()) else 'FAIL — inspect checks below.'), '',
        '| Check | Result |', '| --- | --- |']
    lines += [f'| {name} | {value} |' for name, value in checks.items()]
    lines += ['', '## What happened and why', '',
        'A simulated discussion compared exact matching with token matching. Exact matching was provisionally selected for this demonstration to preserve mixed-label ambiguity; token matching remained a comparator. The decision is TEST ONLY, provisional and has no approver.', '',
        'The successful experiment returned 0 and produced two invented classifications with one deliberately designed disagreement. The negative experiment returned 7 because it expected three records when only two existed. Its absent output and failure were correctly retained. Neither result measures real classification performance.', '',
        'The current finish_session.py was executed unchanged inside the isolated project. It retained the prior handover bytes, unknown context, prior synthetic report and rejected decision; generated all three audience documents; and updated only the synthetic handover. Main project files were verified against SHA-256 baselines. The real decision register was empty, so nonempty decision preservation used an explicitly synthetic rejected sentinel.', '',
        '## Fixes under review', '',
        'Updated metadata, count separation and snapshot context are implemented in the pending source changes. Historical test 01 is unchanged. See AUDIT_WORKFLOW.md for exact behavior.', '',
        '## Next steps and limits', '',
        'Review this report and proposed changes before implementing fixes or committing. Rerun this acceptance scenario after fixes. Real CERF dataset, rules, scope, owner and reviewer remain NOT YET CONFIRMED; no methodological approval is implied. Do not circulate the generated client scaffold.', '',
        'Inspect acceptance_results.json, command_transcript.json, script_provenance.json, protected_before.json, and the generated report. Commands and harmless console output are retained in the transcript; audit records intentionally store console hashes. Session events are reported summaries, not a verbatim chat archive. Fixture authoring and repository inspection are not automatically captured by audit_run.py. No Git commit/push test, SharePoint action or client publication was attempted.', '']
    write(BASE / 'REVIEW.md', '\n'.join(lines))
    print(json.dumps({'report': str(report), 'checks': checks}, indent=2))


if __name__ == '__main__':
    main()
