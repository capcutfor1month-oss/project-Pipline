# Universal Agentic Project Pipeline

This repository is the canonical reusable development pipeline for all future projects owned by the founder.

## Founder Autopilot

The default experience is simple:

1. Start a new ChatGPT session.
2. Paste only the target project repository URL.
3. Describe the product problem, desired result, or feedback in normal language.

Example:

```text
https://github.com/capcutfor1month-oss/example-project

The dashboard is confusing. Owners should immediately understand what needs attention.
```

The orchestration hub must automatically read this common pipeline, inspect the target repository, recover current state, classify the request, select the necessary skills and agents, manage context, prepare specifications and handoffs, and return founder-readable evidence.

The founder is not expected to know skill names, slash commands, context-window strategy, technical agent selection, test frameworks, or audit-prompt structure.

Read `START_HERE.md` and `docs/FOUNDER_AUTOPILOT.md` for the exact behaviour.

## Explicit bootstrap trigger

The founder may also say:

> Apply my common project pipeline.

The orchestration hub must inspect the target project, preserve existing work, add only missing prerequisites, validate the result, and stop before product development unless separately approved.

## Core model

```text
Founder product problem or desired result
→ ChatGPT orchestration and automatic skill routing
→ Founder-approved product decisions
→ OpenSpec change
→ Gemini CLI or OpenCode investigation
→ Claude implementation
→ Fresh-context builder review
→ GitHub Actions
→ Playwright
→ Antigravity
→ Codex independent audit
→ Founder approval
→ Preview
→ Production
→ Sentry + PostHog
→ Next approved change
```

## Important boundary

This repository contains only the universal pipeline, rules, templates, prompts, and validation scripts. It does not contain any product implementation.

The target project repository stores project-specific truth and the instructions required by Claude, Codex, investigators, and verification tools. The founder should not need to paste the universal pipeline link into every agent chat.

Read `START_HERE.md`, `BOOTSTRAP_CONTRACT.md`, `MANIFEST.md`, `docs/FOUNDER_AUTOPILOT.md`, and `docs/PIPELINE.md` before applying it to another repository.
