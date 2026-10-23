# Internal deep dive — CERF portfolio analysis

This is a navigation and audit record for analysts and AI assistants. Entries reported by the agent are not independent evidence.

## Instrumented runs
### d9b16b91-735b-4fea-848f-e9ae2e3a4d59
- Time: 2026-10-23T12:32:00.717423+00:00 to 2026-10-23T12:32:00.741758+00:00
- Task / owner / rules: SYNTHETIC-E2E-20261023-01-success / synthetic-test-agent / TEST-ONLY-demo-v1
- Status / exit: completed / 0
- Command: `["/opt/codex/runtimes/codex-primary-runtime/dependencies/python/bin/python3", "experiment.py", "success"]`
- Inputs: `[{"path": "fixtures/labels.json", "exists": true, "bytes": 197, "sha256": "f5c3cba155cfb3c24715435e67b016a2d31aa71e39e62932c40972efde27ac85"}, {"path": "experiment.py", "exists": true, "bytes": 1278, "sha256": "eb5b0eb400c988979df8a3b1ce40e3bc47b3bf97c90bb900230c4a8d2c40bc84"}]`
- Outputs: `[{"path": "outputs/success.json", "exists": true, "bytes": 770, "sha256": "15388d0b825c1cfc3f036290426543c9269e085c104789306a87213ec7d4d1cc"}]`

### d2640161-7808-40f1-95db-adba88de00ab
- Time: 2026-10-23T12:32:00.765913+00:00 to 2026-10-23T12:32:00.780687+00:00
- Task / owner / rules: SYNTHETIC-E2E-20261023-01-fail / synthetic-test-agent / TEST-ONLY-demo-v1
- Status / exit: failed / 7
- Command: `["/opt/codex/runtimes/codex-primary-runtime/dependencies/python/bin/python3", "experiment.py", "fail"]`
- Inputs: `[{"path": "fixtures/labels.json", "exists": true, "bytes": 197, "sha256": "f5c3cba155cfb3c24715435e67b016a2d31aa71e39e62932c40972efde27ac85"}, {"path": "experiment.py", "exists": true, "bytes": 1278, "sha256": "eb5b0eb400c988979df8a3b1ce40e3bc47b3bf97c90bb900230c4a8d2c40bc84"}]`
- Outputs: `[{"path": "outputs/never_created.json", "exists": false}]`

## Reported discussions, errors, experiments and handovers
- 2026-10-23T12:32:00.655710+00:00 | discussion | provisional | TEST ONLY; NOT APPROVED. Objective: test end-to-end documentation and audit capture. Scope: invented labels only; no real CERF inputs, scores, rule changes or publication. | Why: Validate documentation behavior independently of substantive CERF analysis. | Reference:  | Next: Review TEST ONLY documentation gaps
- 2026-10-23T12:32:00.674527+00:00 | discussion | provisional | TEST ONLY; NOT APPROVED. SIMULATED discussion, not real participants: Approach A uses exact label equality; approach B uses token membership. On invented alpha and alpha beta, A treats the mixed label as unclassified, while B assigns alpha. A preserves ambiguity; B increases coverage but may overclassify. | Why: Exercise recording alternatives, tradeoffs and uncertainty without choosing a real CERF methodology. | Reference:  | Next: Review TEST ONLY documentation gaps
- 2026-10-23T12:32:00.693307+00:00 | decision | provisional | TEST ONLY; NOT APPROVED. TEST ONLY; NOT APPROVED: provisionally use exact matching as the demonstration baseline | Why: TEST ONLY: expose mixed-label ambiguity; token matching remains a comparator; no CERF rule is adopted | Reference: 06_DECISIONS/decision_register.csv | Next: Review TEST ONLY documentation gaps
- 2026-10-23T12:32:00.800933+00:00 | experiment | provisional | TEST ONLY; NOT APPROVED. Success attempt exited 0: two invented records yielded one designed disagreement; this checks plumbing, not classification accuracy. | Why: Confirm command, input/code/output fingerprints and successful audit capture. | Reference: d9b16b91-735b-4fea-848f-e9ae2e3a4d59 | Next: Review TEST ONLY documentation gaps
- 2026-10-23T12:32:00.819649+00:00 | error | provisional | TEST ONLY; NOT APPROVED. Intentional failure exited 7: expected three invented records but fixture contains two. Failure output was deliberately never created. This is the expected negative test, not a failed CERF analysis. | Why: Exercise failed-command capture and missing-output recording; fixture was not corrupted. | Reference: d2640161-7808-40f1-95db-adba88de00ab | Next: Review TEST ONLY documentation gaps
- 2026-10-23T12:32:00.848941+00:00 | validation | provisional | TEST ONLY; NOT APPROVED. Two audit attempts captured with commands, exit codes, fingerprints and stream hashes. Only summaries and wrapped experiments are captured; repository reads, setup, fixture authoring and report inspection are in the command transcript, not automatic conversation capture. | Why: Explain capture boundaries and avoid claiming complete automatic logging. | Reference: ../command_transcript.json | Next: Review TEST ONLY documentation gaps
- 2026-10-23T12:32:00.889006+00:00 | handover | provisional | TEST ONLY; NOT APPROVED. Synthetic comparison of exact and token matching completed; one provisional demonstration decision, no real CERF scoring. Success exit 0; intentional failure exit 7 because expected 3 invented records but observed 2. Failure created no output. Inspect reports for isolation, explanations and broken links; capture covers reported summaries and wrapped commands only. | Why:  | Reference:  | Next: TEST ONLY: review acceptance results and proposed script changes; no commit, push or client release authorized.

## All methodological decisions (including provisional/rejected)
- {"decision_id": "TEST-PRIOR-REJECTED", "date": "2026-10-23", "decision": "TEST ONLY prior rejected fixture; never a CERF rule", "rationale": "Preservation sentinel", "status": "rejected", "approved_by": ""}
- {"decision_id": "SYNTHETIC-E2E-20261023-01-D1", "date": "2026-10-23", "decision": "TEST ONLY; NOT APPROVED: provisionally use exact matching as the demonstration baseline", "rationale": "TEST ONLY: expose mixed-label ambiguity; token matching remains a comparator; no CERF rule is adopted", "status": "provisional", "approved_by": ""}

## Known limits
- This does not automatically archive complete Codex conversations, unwrapped actions, Excel GUI edits or SharePoint activity.
- Validate all citations, evidence links and code before relying on summaries.
