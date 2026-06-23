# Documentation Index

This repository is the canonical source for the universal project pipeline.

## Core documents

| File | Purpose |
|---|---|
| `README.md` | Pipeline overview and trigger |
| `START_HERE.md` | Fresh-session recovery from one project repository URL |
| `BOOTSTRAP_CONTRACT.md` | Safe application rules |
| `MANIFEST.md` | Required files and readiness definition |
| `AGENTS.md` | Shared AI-agent and skill-governance rules |
| `CLAUDE.md` | Claude role rules |
| `GEMINI.md` | Gemini CLI role rules |
| `docs/PIPELINE.md` | End-to-end operating model and stage-based skill routing |
| `docs/TOOLING.md` | Tool and approved skill-source registry |
| `docs/SKILLS.md` | External skill sources, activation model, precedence, and context rules |
| `docs/CURRENT.md` | Current state of this pipeline repository |
| `docs/DECISIONS.md` | Pipeline decisions |
| `docs/TESTING.md` | Validation strategy |
| `docs/RELEASE.md` | Pipeline version and adoption guidance |

## Approved external skill sources

- `phuryn/pm-skills`
- `mattpocock/skills`
- `coreyhaines31/marketingskills`

These remain upstream capability libraries. Projects record selected activation in their own `docs/SKILLS.md` rather than copying every skill into permanent context.

## Supporting folders

- `templates/change/`
- `prompts/`
- `scripts/`
- `.github/`

## Anti-duplication rule

One canonical document exists per purpose. Git history stores older versions.
