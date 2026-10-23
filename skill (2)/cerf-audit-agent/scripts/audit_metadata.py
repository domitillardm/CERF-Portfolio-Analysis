"""Shared conservative classification; never migrate or rewrite old records."""


def add_arguments(parser):
    group = parser.add_mutually_exclusive_group()
    group.add_argument('--synthetic', dest='test_only', action='store_const', const=True)
    group.add_argument('--portfolio-analysis', dest='test_only', action='store_const', const=False)
    parser.set_defaults(test_only=None)


def metadata(args, parser):
    session = getattr(args, 'session', None)
    if args.test_only is not None and not (session and session.strip()):
        parser.error('--synthetic and --portfolio-analysis require a nonempty --session')
    return {'schema_version': 2, 'session': session, 'test_only': args.test_only}


def category(record):
    marker = record.get('test_only')
    if marker is True or str(marker).lower() == 'true':
        return 'synthetic TEST ONLY'
    if (marker is False or str(marker).lower() == 'false') and record.get('session'):
        return 'portfolio-analysis (declared; not validation)'
    return 'unclassified legacy/unspecified (excluded)'


def coverage(runs):
    counts = [sum(category(r) == label for r in runs) for label in
              ['portfolio-analysis (declared; not validation)', 'synthetic TEST ONLY',
               'unclassified legacy/unspecified (excluded)']]
    return (f'Execution records: {counts[0]} declared portfolio-analysis; '
            f'{counts[1]} synthetic TEST ONLY (excluded from portfolio analysis); '
            f'{counts[2]} unclassified legacy/unspecified (excluded). '
            'Execution counts do not establish validated CERF results.')


def banner(state):
    if category(state) == 'synthetic TEST ONLY':
        return '**TEST ONLY — synthetic documentation session; no real CERF analysis or results.**'
    return '**Synthetic TEST ONLY and unclassified records are excluded from portfolio-analysis summaries.**'


def context_links(prefix=''):
    return ['## Snapshot context', '',
            f'- [Project context]({prefix}01_METHODOLOGY/PROJECT_EXPLAINED.md)',
            f'- [Scoring rules]({prefix}01_METHODOLOGY/scoring_rules.md)',
            f'- [Validation issues]({prefix}05_VALIDATION/issues.md)',
            f'- [Snapshot manifest]({prefix}snapshot_manifest.json)', '']
