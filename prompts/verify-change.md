# Verify Change

The orchestration hub invokes verification against the exact implementation commit.

## Instructions

- Read the complete approved specification, current ticket status, implementation report, and project testing policy.
- Confirm repository, branch, commit, and environment tested.
- Run the repeatable checks required by the change risk.
- Verify every acceptance criterion, important failure state, and relevant historical-data behaviour.
- Check authentication, authorization, tenant isolation, migrations, mobile and desktop behaviour when relevant.
- Confirm no silent scope expansion or unrelated regression is evident.
- Do not make product decisions.
- Do not repair production code unless separately assigned.
- Summarize failures instead of pasting large logs.
- Write `verification-report.md`.

## Required return

```text
Stage completed: Verification
Repository, branch, commit, and environment:
Acceptance criteria verified:
Test data used:
Commands executed:
Checks passed:
Checks failed:
Failure states tested:
Database and historical-data findings:
Authentication and tenant findings:
UI and device findings:
Areas not tested:
Known risks:
Remaining uncertainty:
Founder manual-test steps:
Founder decision required:
Permitted next action:
```
