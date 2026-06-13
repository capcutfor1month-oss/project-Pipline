# Start a Fresh Project Working Session

Use this file whenever a new ChatGPT conversation begins for any project.

## The founder's only required first message

Paste only the target project repository URL.

Example:

```text
https://github.com/capcutfor1month-oss/example-project
```

No repeated explanation of the pipeline, agent roles, documentation rules, or project process should be required.

## What the orchestration hub must do automatically

When the first meaningful message contains a GitHub project URL:

1. Recognize `capcutfor1month-oss/project-Pipline` as the canonical common pipeline.
2. Read:
   - `README.md`
   - `BOOTSTRAP_CONTRACT.md`
   - `MANIFEST.md`
   - `docs/PIPELINE.md`
   - `docs/TOOLING.md`
   - `AGENTS.md`
3. Inspect the target repository before advising or writing.
4. Determine whether the target is:
   - Empty
   - A starter repository
   - An active existing product
5. Search for the target project's canonical files:
   - `docs/INDEX.md`
   - `docs/CURRENT.md`
   - `docs/DECISIONS.md`
   - `docs/PIPELINE.md`
   - `docs/TOOLING.md`
   - Active OpenSpec change folder
6. Recover the current project state from GitHub rather than asking the founder to repeat old context.
7. Detect whether the common pipeline is already installed.
8. If missing, propose or apply the bootstrap according to `BOOTSTRAP_CONTRACT.md`.
9. If already installed, continue from the project's recorded next action.
10. Do not start coding, architecture selection, or product decisions unless the founder explicitly asks.

## First response format

The orchestration hub should answer with:

```text
Project recognized: <project name>
Repository type: Empty / Starter / Existing product
Common pipeline: Missing / Partial / Installed
Current phase: <phase>
Active change: <change or none>
Current blocker: <blocker or none>
Recorded next action: <next action>
Founder decision needed: <decision or none>
```

Then wait for or follow the founder's actual task.

## Existing project recovery

For an existing project, do not treat missing repository documents as permission to guess. Inspect the codebase and existing documentation, report uncertainty, and create a safe recovery proposal before modifying anything.

## New project behavior

For a fresh project repository:

- Apply the common prerequisites.
- Record product definition and architecture as not started.
- Configure only the pipeline layer that is technically possible.
- Stop before brainstorming or implementation unless separately requested.

## Source-of-truth rule

The project repository stores project truth.

This pipeline repository stores the common operating method.

The chat is only the active control room and must not become the sole copy of important decisions.
