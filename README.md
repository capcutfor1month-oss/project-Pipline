# Universal Agentic Project Pipeline

This repository is the canonical reusable development pipeline for all future projects owned by the founder.

## Simplest fresh-session start

In a new ChatGPT session, paste only the target project repository URL.

Example:

```text
https://github.com/capcutfor1month-oss/example-project
```

The orchestration hub must automatically read this common pipeline, inspect the target repository, recover its current state, and continue without asking the founder to repeat the complete workflow.

Read `START_HERE.md` for the exact behavior.

## Explicit bootstrap trigger

The founder may also say:

> Apply my common project pipeline.

The orchestration hub must inspect the target project, preserve existing work, add only missing prerequisites, validate the result, and stop before product development unless separately approved.

## Core model

```text
Founder + ChatGPT
→ Product discovery and approved decisions
→ OpenSpec change
→ Gemini CLI or OpenCode investigation
→ Claude implementation
→ GitHub Actions
→ Playwright
→ Antigravity
→ Codex audit
→ Founder approval
→ Preview
→ Production
→ Sentry + PostHog
→ Next approved change
```

## Important boundary

This repository contains only the universal pipeline, rules, templates, prompts, and validation scripts. It does not contain any product implementation.

Read `START_HERE.md`, `BOOTSTRAP_CONTRACT.md`, `MANIFEST.md`, and `docs/PIPELINE.md` before applying it to another repository.
