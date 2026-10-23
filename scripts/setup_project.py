#!/usr/bin/env python3
"""Create missing project scaffolds; never truncate or replace existing files."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TEMPLATE = ROOT / 'skill (2)' / 'cerf-audit-agent'


def main():
    for name in ['01_METHODOLOGY', '02_ACTIVITY_DATA', '03_CODE', '04_ANALYSIS_LOGS',
                 '05_VALIDATION', '06_DECISIONS', '07_RESULTS', '08_CLIENT_APPENDIX',
                 '09_INTERNAL_DEEP_DIVE']:
        (ROOT / name).mkdir(exist_ok=True)
    # Relative links survive cloning and checkout relocation; original tools stay
    # canonical in the reusable skill package.
    for name in ['session_log.py', 'audit_run.py', 'refresh_status.py', 'build_appendix.py', 'audit_metadata.py']:
        path = ROOT / 'scripts' / name
        if not path.exists() and not path.is_symlink():
            path.symlink_to(Path('..') / TEMPLATE.relative_to(ROOT) / 'scripts' / name)
    files = {
        'handover.json': json.dumps({k: 'NOT YET CONFIRMED' for k in
            ['purpose', 'phase', 'authoritative_dataset', 'approved_rules',
             'validated_output', 'owner', 'next_action', 'blocker']}, indent=2) + '\n',
        '00_START_HERE.md': '# CERF portfolio analysis — start here\n\n'
            'Read AGENTS.md and handover.json before analysis. Project context and approvals '
            'are NOT YET CONFIRMED.\n\nThe latest versioned status, internal history and '
            'client draft are in the directory named by handover.json.latest_report. '
            'If absent, no session has been finalized with the current workflow.\n\n'
            'See ENVIRONMENT.md for setup, session commands and persistence checks.\n',
        '01_METHODOLOGY/PROJECT_EXPLAINED.md': '# CERF portfolio context\n\n'
            'Programme, scope, unit of analysis, dataset provenance, countries/tracks, '
            'glossary and evidence standard: NOT YET CONFIRMED.\n',
        '01_METHODOLOGY/scoring_rules.md': '# Scoring rules\n\n'
            'NOT YET CONFIRMED. No approved scoring framework supplied.\n',
        '05_VALIDATION/issues.md': '# Validation issues\n\n'
            'Dataset, rules, analysis code and reviewer: NOT YET CONFIRMED.\n',
        '06_DECISIONS/decision_register.csv': 'decision_id,date,decision,rationale,status,approved_by\n',
        '05_VALIDATION/activity_scoring_register.csv': 'activity_id,dataset_version,rules_version,assigned_score,evidence_pointer,uncertainty,validation_state,reviewer,correction,timestamp\n',
        '02_ACTIVITY_DATA/README.md': '# Source inputs\n\nIgnored by default. Do not commit real CERF data.\n',
        '07_RESULTS/README.md': '# Analysis outputs\n\nIgnored by default. Use unique output names; review confidentiality before any release.\n',
    }
    for name, content in files.items():
        try:
            with (ROOT / name).open('x', encoding='utf-8') as stream:
                stream.write(content)
        except FileExistsError:
            pass
    print('Prepared repository project root:', ROOT)


if __name__ == '__main__':
    main()
