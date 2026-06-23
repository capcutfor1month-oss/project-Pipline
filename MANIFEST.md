# Universal Pipeline Manifest

This manifest defines the common files and how they should be applied to a target repository.

## Required root files

| File | Purpose | Application rule |
|---|---|---|
| `README.md` | Project introduction and current boundary | Preserve an existing README; add pipeline links rather than replacing product content |
| `START_HERE.md` | Fresh-session recovery from a project repository URL | Required in the common pipeline repository |
| `AGENTS.md` | Rules shared by every AI agent | Create if missing; merge carefully if present |
| `CLAUDE.md` | Claude implementation rules | Create if missing; preserve stricter existing project rules |
| `GEMINI.md` | Gemini CLI investigation rules | Create if missing; preserve stricter existing project rules |
| `.gitignore` | Prevent accidental tracking of local or sensitive output | Merge rather than replace |
| `.env.example` | Document future configuration names without real values | Create only when appropriate; never place real credentials in it |

## Required canonical documents

| File | Purpose |
|---|---|
| `docs/INDEX.md` | Documentation registry and anti-duplication control |
| `docs/PRODUCT.md` | Approved product problem, users, and scope |
| `docs/ARCHITECTURE.md` | Approved current system architecture |
| `docs/CURRENT.md` | Small current-state and next-action summary |
| `docs/DECISIONS.md` | Durable decision log |
| `docs/PIPELINE.md` | Complete end-to-end project workflow |
| `docs/TOOLING.md` | Tool roles, status, and activation conditions |
| `docs/SKILLS.md` | Approved skill sources, activation rules, and safety boundaries |
| `docs/TESTING.md` | Testing strategy and required evidence |
| `docs/RELEASE.md` | Release-readiness and rollback checklist |

For a new project, `PRODUCT.md` and `ARCHITECTURE.md` must clearly state that they are not yet defined.

Each project `docs/SKILLS.md` must state which approved external skills are active, deferred, or not installed.

## Required change workspace

```text
openspec/
└── changes/
    └── <change-name>/
        ├── proposal.md
        ├── spec.md
        ├── design.md
        ├── tasks.md
        ├── repository-report.md
        ├── implementation-report.md
        ├── verification-report.md
        ├── ux-report.md
        └── audit-report.md
```

A real change folder is created only after the founder approves beginning product work.

## Required reusable templates

```text
templates/change/
├── proposal.md
├── spec.md
├── design.md
├── tasks.md
├── repository-report.md
├── implementation-report.md
├── verification-report.md
├── ux-report.md
└── audit-report.md
```

## Required reusable prompts

```text
prompts/
├── start-project-session.md
├── bootstrap-project.md
├── investigate-change.md
├── implement-change.md
├── verify-change.md
├── test-user-flow.md
└── audit-change.md
```

## Required GitHub configuration

```text
.github/
├── pull_request_template.md
└── workflows/
    └── pipeline-checks.yml
```

## Approved external skill sources

- `phuryn/pm-skills`
- `mattpocock/skills`
- `coreyhaines31/marketingskills`

These are approved capability sources. They must be selected and loaded lazily according to `docs/SKILLS.md`; they are not copied wholesale into every project.

## Conditional tools

Record immediately but configure only when technically possible:

- Playwright: after a runnable web application exists
- Antigravity: after a local or preview application exists
- Preview hosting: after hosting architecture is approved
- Sentry: after runtime and framework selection
- PostHog: after privacy-safe product events are defined
- GitHub Agentic Workflows: after the manual pipeline is understood and stable

## Pipeline-ready definition

A repository is pipeline-ready when:

- Canonical documents exist without duplicates
- Roles and boundaries are recorded
- Current status is truthful
- Product work has not started without approval
- Agents can recover context from repository files
- Skill sources and activation rules are recorded
- A fresh session can recover the project from GitHub
- The pipeline validation check passes
