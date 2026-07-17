# Implement Change

The orchestration hub prepares this bounded implementation handoff. The founder is not responsible for selecting skills, files, tests, or context strategy.

## Preflight

- Read `AGENTS.md`, `CLAUDE.md`, canonical project documents, and the complete active OpenSpec change.
- Confirm repository, approved branch, working-tree state, exact specification, and current ticket.
- Confirm whether committing is permitted. Merging and deployment are not permitted unless separately stated.
- State intended files or areas before editing.
- Stop when a missing product or architecture decision changes behaviour, scope, or risk.

## Implementation

- Implement only the approved specification and current ticket.
- Keep the ticket subordinate to the complete specification.
- Use only orchestration-routed engineering skills.
- Do not create duplicate specifications or ticket systems.
- Add or update tests for changed behaviour and regressions.
- Do not alter unrelated behaviour or perform opportunistic refactoring.
- Do not access production secrets, production data, or production infrastructure.
- Run required static checks, tests, build, migration checks, and project-specific gates.
- Use a fresh reviewer context or subagent to compare the result against the complete specification, code quality, test quality, and unrelated changes when appropriate.
- Builder-side review does not replace Codex.
- Update `tasks.md` and `implementation-report.md` truthfully.

## Required return

```text
Stage completed: Implementation
Repository, branch, and commit:
Approved specification and ticket:
Skills used:
Files inspected:
Files changed:
What was not changed:
Behaviour implemented:
Tests added or updated:
Commands executed:
Checks passed:
Checks failed:
Builder-side review findings:
Specification deviations:
Known risks:
Remaining uncertainty:
Deployment status: Not deployed
Founder manual testing required:
Founder decision required:
Permitted next action:
```

Never declare completion while required checks fail. Never merge or deploy automatically.
