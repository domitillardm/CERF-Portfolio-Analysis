"""TEST ONLY: invented labels; never CERF scoring."""
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
Path('outputs/success.json').write_text(json.dumps(output, indent=2) + '\n')
print('TEST ONLY success: 2 invented records; 1 designed disagreement; no real result')
