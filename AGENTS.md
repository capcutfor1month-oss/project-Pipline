# Shared Agent Rules

These rules apply to every AI agent working in a project that adopts this pipeline.

## Product authority

1. The founder owns product decisions.
2. Do not choose scope, users, workflows, pricing, architecture, or quality trade-offs without approval.
3. Do not begin implementation until an approved specification exists.

## Source of truth

1. GitHub is the durable source of truth.
2. Read `docs/INDEX.md` before creating Markdown files.
3. Update canonical documents rather than creating duplicates.
4. Git history is version history.
5. Never create `final`, `latest`, `updated`, `new`, or numbered duplicates.

## Change workflow

1. Work from one named change at a time.
2. Read the approved proposal, specification, design, tasks, and reports.
3. Stay within approved scope.
4. Stop and report when a product decision is missing.
5. One agent writes to a branch at a time.
6. Do not modify production directly.
7. Do not expose secrets.

## Evidence

Every report must include:

- Files inspected
- Files changed
- Commands executed
- Checks passed
- Checks failed
- Remaining uncertainty
- Recommended next action

Never claim success without evidence.
