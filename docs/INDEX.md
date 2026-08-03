# Documentation Index

This repository is the canonical source for the universal project pipeline.

## Core documents

| File | Purpose |
|---|---|
| `README.md` | Pipeline overview and simplest trigger |
| `START_HERE.md` | Fresh-session recovery from one target repository URL |
| `BOOTSTRAP_CONTRACT.md` | Safe application rules |
| `MANIFEST.md` | Required files and readiness definition |
| `AGENTS.md` | Shared AI-agent and skill-governance rules |
| `CLAUDE.md` | Claude implementation and builder-review rules |
| `GEMINI.md` | Gemini CLI investigation rules |
| `docs/FOUNDER_AUTOPILOT.md` | Product-language founder interface and automatic orchestration contract |
| `docs/FOUNDER_COMMUNICATION.md` | Founder-friendly response order, tone, term translation, and action guidance |
| `docs/CONTEXT_MANAGEMENT.md` | Context, ticket, handoff, and fresh-review rules |
| `docs/PIPELINE.md` | End-to-end operating model and automatic stage routing |
| `docs/TOOLING.md` | Tool and approved skill-source registry |
| `docs/SKILLS.md` | External capability sources, automatic activation, precedence, and context rules |
| `docs/CURRENT.md` | Current state and exact next action |
| `docs/DECISIONS.md` | Durable pipeline decisions |
| `docs/TESTING.md` | Validation strategy |
| `docs/RELEASE.md` | Pipeline version and adoption guidance |
| `docs/PIPELINE_UPDATE_RECOMMENDATIONS.md` | Approved improvement roadmap and pilot plan |

## Approved external skill sources

- `phuryn/pm-skills`
- `mattpocock/skills`
- `coreyhaines31/marketingskills`

These remain upstream capability libraries. Projects record availability, restrictions, and current activation in their own `docs/SKILLS.md`. The orchestration hub selects capabilities automatically rather than asking the founder to operate them.

## Supporting folders

- `templates/change/`
- `prompts/`
- `scripts/`
- `.github/`

## Founder communication rule

Every meaningful pipeline stage produces a founder-friendly explanation and a separate technical evidence record. The evidence report remains canonical, but it must not be pasted unchanged as the complete founder response.

## Anti-duplication rule

One canonical document exists per purpose. Git history stores older versions. External skills and temporary agent output must map durable approved results into these canonical documents rather than create parallel sources of truth.
