# Universal Skills Registry

This document defines the approved external skill libraries used by the universal project pipeline.

## Purpose

The pipeline controls the project process. Skills add specialist knowledge and repeatable workflows inside that process.

Skills do not replace:

- Founder product authority
- Canonical project documents
- Approved OpenSpec changes
- Deterministic tests and CI
- Independent Codex audit
- Founder release approval

## Approved skill sources

### Product management

Source: `phuryn/pm-skills`

Approved capability areas:

- Product discovery
- Product strategy
- Market research
- Product execution
- Data and metrics
- Marketing and growth
- Go-to-market
- AI-assisted shipping

High-value workflows include discovery, assumption mapping, opportunity-solution trees, customer interviews, product vision, value proposition, PRDs, outcome roadmaps, user stories, test scenarios, pre-mortems, strategy red-team, launch planning, and metrics design.

### Engineering discipline

Source: `mattpocock/skills`

Approved capability areas:

- Requirement clarification
- Shared domain language
- PRD and issue creation
- Test-driven development
- Disciplined bug diagnosis
- Domain modelling
- Codebase design
- Architecture improvement
- Git guardrails
- Pre-commit feedback loops
- Compact handoffs

High-value skills include `grill-with-docs`, `to-prd`, `to-issues`, `tdd`, `diagnosing-bugs`, `domain-modeling`, `codebase-design`, `improve-codebase-architecture`, `git-guardrails-claude-code`, `setup-pre-commit`, and `handoff`.

### Marketing and growth

Source: `coreyhaines31/marketingskills`

Approved capability areas include the full upstream library for:

- Product marketing
- Customer research
- Positioning and offers
- Copywriting and editing
- Conversion-rate optimisation
- Signup and onboarding
- SEO and site architecture
- Analytics and experiments
- Email, SMS, social, image, and video
- Pricing and monetisation
- Launch and public relations
- Referrals, retention, and churn prevention
- Sales enablement and revenue operations

The `product-marketing` context must be established before downstream marketing skills generate claims or campaigns.

## Skill activation model

Skills are **lazy-loaded by stage and task**, not injected into every conversation.

### New-product discovery

Use:

- PM discovery and assumption skills
- `grill-with-docs` or `grill-me`
- Product vision and value-proposition skills
- Customer-interview skills when real interviews are planned

### Specification and planning

Use:

- PM PRD, roadmap, user-story, test-scenario, pre-mortem, and strategy-red-team skills
- `to-prd`
- `to-issues`
- Domain modelling when shared terminology is unclear

### Implementation

Use:

- `tdd`
- `codebase-design`
- Domain modelling when implementation terminology affects architecture
- Git guardrails and pre-commit checks where supported

### Bug fixing

Use:

- `diagnosing-bugs`
- Regression-test discipline
- TDD for the smallest reproducible fix

### Launch and growth

After product direction and evidence exist, use:

- Product marketing
- Customer research
- Copywriting
- CRO
- Signup and onboarding
- Analytics and A/B testing
- Launch and go-to-market
- SEO, email, SMS, referrals, retention, and sales enablement as relevant

## Precedence and conflict rules

When instructions conflict, follow this order:

1. Founder-approved decision
2. Canonical project documents
3. Approved active change specification
4. Project agent rules
5. This universal pipeline
6. External skill instructions
7. General model knowledge

A skill may improve execution but may not silently expand scope, change architecture, invent product facts, or override a project decision.

## Context-bloat rule

Do not install or load every skill merely because it is available.

For each task:

1. Identify the current pipeline stage.
2. Select the smallest relevant skill set.
3. Load only those skill instructions.
4. Store durable outcomes in canonical project documents.
5. Remove temporary summaries and raw logs from the main context.

## Installation policy

- The three upstream repositories are approved sources.
- Record the exact upstream repository and selected skill names before installation.
- Prefer project-level installation for project-specific skills.
- Do not vendor or duplicate entire upstream libraries into every repository.
- Do not auto-update skills during an active change.
- Review upstream changes before upgrading.
- Never allow a skill installer to overwrite canonical project documents or agent rules.

## Project adoption requirement

Each adopted project should contain its own `docs/SKILLS.md` stating:

- Approved upstream sources
- Skills active in the current phase
- Skills deferred until later phases
- Project-specific safety boundaries
- Installation status

This keeps the full capability available while preventing unnecessary context and instruction conflicts.
