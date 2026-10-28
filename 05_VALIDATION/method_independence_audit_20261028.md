# Methodological-independence audit — 28 October 2026

Read-only audit of the original pilot, full-portfolio implementation and subsequent consolidation. No score, assignment, input workbook or codebook changed. Findings below supersede earlier broad descriptions of “independent” scoring. Technical preservation checks never established assessor independence.

## Conclusion

**Independent implementation of the judgement approaches cannot be demonstrated.** There is direct evidence of score reuse: initial singleton C copied A; initial B defaulted to A with specific contextual overrides. Multi-activity C has separately authored narrative/code entries, with no global C=max formula, but no blinded assessment or independent authoring record is evidenced. D1/D2 are deliberately derived maxima, not independent assessments. Current agreement is descriptive consistency within this implementation, not validation of methodological equivalence, correctness, or AI calibration.

## Questions and findings

| Question | What artifacts prove | What remains uncertain |
| --- | --- | --- |
| Was C independently holistic? | Original full-portfolio builder copies A code/status/evidence/rationale for all 69 singleton groups (AUD-E1, lines43–44). For32 multi-activity groups it reads an authored C code/rationale/source table (lines45–47), rather than computing C=max. | Separate narrative does not establish independent judgement: A/B were available and the same AI workflow authored the entries. Cognitive anchoring cannot be confirmed or excluded. |
| Was C assigned before D? | Pilot B/C run at15:54:14 UTC precedes D/export at15:58:21 on 23 October; C lock hashes still match (AUD-E2/E3). Full builder assigns each C before that track's D loop (AUD-E1 lines39–58). Latest consolidation likewise assigns C before its D loop (AUD-E4 lines65–84). | Full-run C and D were persisted/frozen together, after both calculations. No separately timestamped full-run C-only lock or per-judgement prompt record proves C was independently authored before any maximum was known. Source-file modification times are not treated as assessor evidence. |
| Does code force equality? | No universal equality constraint found in the inspected pilot, full-run and consolidation code. There is an explicit singleton C=A branch. Independently, D1=max eligible A and D2=max eligible B. For a complete singleton this mechanically yields equality. | Multi-track equality could arise from overlapping evidence, highest-supported-level semantics, coarse scale and/or anchoring. The numerical pattern alone cannot distinguish these explanations. |
| Were A/B independent? | A annotations were frozen before contextual materialisation and the A hash still matches (AUD-E5). B explicitly begins with A code/status/evidence/rationale; four initial override entries replace that default (AUD-E1 lines25–38). Of249 rows,216 followed the A-code default,29 lacked accepted membership and 4 used overrides. The pilot also deep-copies A for B (AUD-E2 lines37–44). | This is an incremental, score-aware contextual review, not a blind second assessment. Scope/link notes show some substantive review; they do not prove every unchanged code was independently rederived. The default branch only asks about a higher result, despite the codebook allowing B to decrease. Earlier pilot exposure is acknowledged in the A-freeze note and pilot protocol (AUD-E8). |
| Is comparison meaningful? | A/B can describe the recorded contextual revisions; C versus D can describe final endpoint agreement; deterministic maxima and bookkeeping are reproducible. | These figures cannot estimate independent method agreement, prove that B adds no information, demonstrate unbiased calibration or establish interchangeable methods. |

## How much agreement is structurally uninformative?

The original run had115 group rows:69 singleton,32 multi-activity and 14 unresolved review groups. The final analytical universe is93 defined provisional tracks:59 singleton and 34 multi-activity. Of82 tracks with valid C/D1/D2 on all three,53 are singleton and 29 multi-activity. Thus53/82 comparisons (64.6%) have identical one-record evidence scope and strong structural reasons for equality; many inherit the copied singleton construction. These are useful accounting controls, not independent holistic-method tests.

A current C rationale retains initial singleton wording in 57 rows, but some scopes were subsequently expanded and some C values/statuses reassessed. Wording alone is not used to classify current independence; immutable originals, code branches, scope and journals are considered together. Later scoped syntheses exist and do not retroactively prove the original method independent.

For multi-activity groups, using the same highest-supported result definition makes equality plausible even under sound separate reasoning: a clear supported level 4 in one activity can also support4 across combined text. Holistic C is not a stricter structural-impact test. Do not manufacture disagreement or impose stronger evidence requirements to make methods look different.

## Comparison exclusions

Only codes1–4 qualify for ordinal agreement. Code 6 remains insufficient information and is excluded; no-achieved, cancelled and unresolved statuses are not converted to0 or6.

| Comparison | Defined universe | Included | Excluded | Included singleton / multi |
| --- | ---: | ---: | ---: | --- |
| C versus D1 |93|82|11|53 /29|
| C versus D2 |93|83|10|53 /30|
| D1 versus D2 |93|82|11|53 /29|
| All C/D1/D2 |93|82|11|53 /29|

Exclusions are the affected incomplete C/D maxima and one information-insufficiency track. C/D2 includes one additional track where D2 is complete but D1 is not. Seven unresolved holding groups with 14 activities are outside the 93-track universe, not additional defined tracks; retain them visibly in review sheets. A/B includes221 of 249 activity records;28 fail the paired1–4 condition.

The restricted **Exact comparison exclusions.txt** lists every excluded track ID, label, C/D values, missing eligible activity IDs and source status, separately for each pair, plus all seven holding groups. It is outside Git with the immutable workbook. Do not publish row-level scoring contents in repository documentation.

## Minimum corrective action — recommendation, not executed

1. Keep all current provisional classifications and user decisions. Relabel present agreement as **recorded-output agreement under an incremental/shared-evidence workflow**, not independent consistency.
2. Exclude singletons from claims about added value of holistic synthesis; report them as same-scope controls. Present current multi-track agreement separately, still with the independence caveat.
3. If an independent C-versus-maximum comparison is required, conduct a separate C pass for the 34 current multi-activity tracks using only frozen chronological monitoring packets and the unchanged rules, with A/B/C/D hidden. Freeze and timestamp C judgements before revealing/calculating maxima. No need to rescore all singleton activities merely to test independence.
4. For B, a small prespecified blinded multi-activity sample can test whether the incremental default matters; allow confirmation, increase, decrease or unresolved with an explicit focal link/contradiction record. A pilot does not establish full-portfolio independence. Claiming an independent full-portfolio A/B comparison would require fresh B judgements for the intended non-singleton comparison population, with A hidden, not blanket rescoring of all 249.
5. Preserve full prompt text, visible input schema, model/version/settings if available, independent outputs, timestamps and adjudication. A different process/reviewer is preferable to reusing the same score-aware conversation. Separate independence of assessment from independent verification of outcomes.

No corrective scoring, new workbook or methodological threshold was implemented by this audit.

## Evidence references and limits

| Ref | Preserved artifact / exact locus | Evidential strength |
| --- | --- | --- |
| AUD-E1 | Private `full-portfolio-v1/build_scores.py`: A load20–23; B25–38; C39–47; D49–58; joint freeze69–72 | Direct executable implementation, reconciled with frozen score register |
| AUD-E2 | Private `stage3-pilot-v1/build_context_scores.py`: B37–44; authored C46–71; B/C lock72 | Direct code and surviving lock hashes; same workflow can see earlier scores |
| AUD-E3 | Pilot `deliver.py`8–18,29–35; existing runs40284889… and 68834972… | Hash-checked pilot chronology: C lock before D calculation; not assessor blinding |
| AUD-E4 | Private `final-consolidated-provisional-20261027-v1/consolidate.py`53–84; preserved C journals and final777-record register | Scoped C reauthoring/retention and separate subsequent maxima, not a global C=max rule |
| AUD-E5 | `full-portfolio-v1/freeze_a.py`, `A_frozen.json`, A TSV, `BC_frozen.json`; runs28b17440…,458a4ee2… | A before contextual materialisation; initial score hashes still match; earlier exposure acknowledged |
| AUD-E6 | `SCORING_CODEBOOK_DRAFT_v0.2.md` section7 and F1 conventions | Intended A/B/C definitions: B need not exceed A; C must not silently copy maximum. Intent is not implementation proof. |
| AUD-E8 | Private `stage3-pilot-v1/pilot_protocol.txt`, especially Blinding limitation and A/B/C instructions | Preserved intended workflow; explicitly disclaims cognitive isolation and independent raters. Not a complete per-call prompt/response archive. |
| AUD-E7 | Final immutable Country-tracks, Activities, Score register; first-analysis SQL checks; restricted audit/exclusion manifest | Actual current eligibility, counts, identities and exclusions; not claim truth |

Full file hashes and exact existing execution-record paths are in the restricted audit manifest. The source documents prove controlled input projection and preservation, not independent authorship. No complete immutable transcript of every scoring prompt/model response/settings, separate blind C assessor or complete full-run C-only authoring chronology was found in the reviewed artifacts. Missing provenance is reported as missing, not reconstructed as fact. This is an implementation audit by Codex, not independent human validation.
