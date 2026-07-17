# Start a Fresh Project Working Session

Use this file whenever a new ChatGPT conversation begins for any project.

## The founder's only required first message

Paste only the target project repository URL.

Example:

```text
https://github.com/capcutfor1month-oss/example-project
```

The founder may immediately add a product problem or desired result in normal language. No repeated explanation of the pipeline, agent roles, documentation rules, skill libraries, context strategy, or project process should be required.

Founder Autopilot Mode is the default. Read `docs/FOUNDER_AUTOPILOT.md`.

## Access preflight

Before claiming recovery, the orchestration hub must determine:

```text
Repository accessible: Yes / No
Default branch readable: Yes / No
Write access available: Yes / No / Unknown
GitHub Actions visible: Yes / No / Unknown
Canonical documents found: Yes / No / Partial
Active change found: Yes / No
Recovery confidence: High / Medium / Low
Unverified assumptions: <none or list>
```

When access is missing or partial, do not guess project state. Report the limitation and the safe recovery option.

## What the orchestration hub must do automatically

When the first meaningful message contains a GitHub project URL:

1. Recognize `capcutfor1month-oss/project-Pipline` as the canonical common pipeline.
2. Read:
   - `README.md`
   - `BOOTSTRAP_CONTRACT.md`
   - `MANIFEST.md`
   - `docs/FOUNDER_AUTOPILOT.md`
   - `docs/PIPELINE.md`
   - `docs/CONTEXT_MANAGEMENT.md`
   - `docs/TOOLING.md`
   - `docs/SKILLS.md`
   - `AGENTS.md`
3. Inspect the target repository before advising or writing.
4. Determine whether the target is empty, a starter repository, or an active existing product.
5. Search for target-project canonical files and the active OpenSpec change.
6. Recover current project state from GitHub rather than asking the founder to repeat old context.
7. Detect whether the common pipeline and governed skills layer are missing, partial, or installed.
8. If missing, propose or apply the bootstrap according to `BOOTSTRAP_CONTRACT.md`.
9. If installed, continue from the recorded next action or the founder's new request.
10. Classify the request automatically: continuation, idea, clarification, feature, bug, incident, audit, release, or prioritisation.
11. Select the smallest relevant skills and tools internally. Never require the founder to know or invoke them.
12. Ask only product-level questions that require founder judgment.
13. Decide whether work fits one focused context or requires a durable specification, tickets, and handoffs.
14. Do not start coding, architecture selection, marketing claims, destructive actions, or production changes without the required approval.
15. Return a founder-readable status and safe next action.

## First response format

```text
Project recognized: <project name>
Repository type: Empty / Starter / Existing product
Repository access: Full / Read-only / Partial / Unavailable
Common pipeline: Missing / Partial / Installed
Skills layer: Missing / Partial / Installed
Current phase: <phase>
Active change: <change or none>
Current blocker: <blocker or none>
Recorded next action: <next action>
Recovery confidence: High / Medium / Low
Unverified assumptions: <none or list>
Founder decision needed: <decision or none>
Coding started: Yes / No
```

Do not expose skill-selection menus or developer commands unless the founder explicitly asks for technical detail.

## Existing project recovery

For an existing project, do not treat missing documents as permission to guess. Inspect code and existing documentation, report uncertainty, and create a safe recovery proposal before modifying anything.

## New project behaviour

For a fresh repository:

- Apply common prerequisites.
- Create project-specific canonical documents and `docs/SKILLS.md`.
- Record product definition and architecture as not started.
- Configure only the pipeline and capability layer that is technically possible.
- Stop before brainstorming or implementation unless separately requested.

## Source-of-truth rule

The project repository stores project truth.

This pipeline repository stores the common operating method and approved capability policy.

The chat is the control room. It must not become the only copy of important decisions.
