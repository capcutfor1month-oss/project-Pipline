# Audit Change

Codex performs an independent read-only audit. Do not continue implementation or repair code during this stage.

## Review

- Complete approved specification and design
- Current ticket sequence and completion state
- Exact implementation diff and commit
- Implementation and verification evidence
- User-flow evidence
- Skills declared by prior stages
- Security and privacy risk
- Authentication, authorization, and tenant isolation
- Database migrations and historical-data preservation
- Regression surface and test quality
- Scope expansion, unrelated changes, and instruction conflicts
- Whether builder-side review was treated incorrectly as independent approval

## Verdict

Write one verdict to `audit-report.md`:

```text
PASS
FAIL
PASS WITH WARNINGS
```

`PASS WITH WARNINGS` is permitted only when no warning blocks the next explicitly named stage.

## Required return

```text
Stage completed: Independent audit
Verdict:
Repository, branch, and commit:
Specification reviewed:
Diff and files reviewed:
Evidence reviewed:
Skills declared by prior stages:
Blocking findings:
Non-blocking findings:
Security and privacy findings:
Authentication and tenant-isolation findings:
Migration and data findings:
Regression findings:
Test-quality findings:
Specification deviations:
Skill-governance findings:
Remaining uncertainty:
Founder manual testing required:
Deployment status:
Founder decision required:
Permitted next action:
```

Never approve work solely because the implementer or its internal reviewer reported success.
