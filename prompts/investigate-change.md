# Investigate Change

The orchestration hub invokes this prompt. The founder does not select investigation skills or identify technical files.

## Instructions

- Read shared agent rules, canonical project documents, and the active OpenSpec change.
- Confirm repository, branch, and exact change being investigated.
- Default to read-only and do not modify files, commit, deploy, or access production data.
- Use approved repository-aware clarification or domain-analysis skills only when routed by the orchestration hub.
- Do not make product or architecture decisions.
- Inspect the current user and data flow, relevant architecture, reusable components, tests, authentication, authorization, tenancy, migrations, security, privacy, and likely regression surface.
- Identify questions that need founder judgment separately from technical questions answerable through inspection.
- Recommend a bounded implementation surface without expanding scope.
- Map durable output into `repository-report.md`; do not create a competing specification or issue system.

## Required return

```text
Stage completed: Investigation
Repository and branch inspected:
Approved change reviewed:
Files and paths inspected:
Current behaviour and flow:
Reusable components or patterns:
Database and migration impact:
Authentication and tenant impact:
Security and privacy risk:
Existing tests and missing coverage:
Likely files in scope:
Technical unknowns:
Founder decisions still required:
Recommended implementation boundary:
Commands executed:
Skills used:
Files changed: None
Remaining uncertainty:
Permitted next action:
```
