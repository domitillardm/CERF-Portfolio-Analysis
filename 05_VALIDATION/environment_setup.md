# Environment setup validation — 2026-10-23

Command: `python3 scripts/test_environment.py` (Python 3.12.14).

Result: passed with synthetic fixtures only.

- Two setup invocations preserved every existing file byte-for-byte.
- Audited synthetic execution recorded input/output hashes and preserved a failing
  child command's exit code 7.
- Session finalization created a status page, internal report and unapproved client
  draft; provisional decisions were excluded from the client's approved section.
- Earlier handover bytes, colleague-owned documentation, unknown context fields,
  decisions and previous report versions survived the next session.
- Sensitive input/output paths, credential names and temporary files were ignored;
  intended logs, methodology and decision/validation registers remained eligible.
- Synthetic documents were committed and pushed to a temporary local bare Git
  repository, restored in a fresh clone, then reused by a separate Python process.
  The restored commit and report hashes matched. Synthetic data did not enter Git.

This is a session-boundary simulation, not a second hosted Codex session. No real
CERF data, scoring rules or GitHub repository writes were used in the test.

The installation changes in the actual checkout are local and uncommitted. A
read-only remote check found main at
`ceef0b1222b1b96a35630fa2b58b6e1dbb42b98d`, also the local HEAD before these changes.
The new documentation is absent from that commit. GitHub persistence and colleague
access are therefore unverified. Review selected non-sensitive changes, authorize
commit/push, verify the remote commit, and test a new hosted session before making
a cross-session cloud restoration claim. Cloud publication does not push to GitHub.
