# Universal Agentic Project Pipeline

This repository is the canonical reusable development pipeline for all future projects owned by the founder.

## Trigger

When the founder shares a GitHub repository and says:

> Apply my common project pipeline.

The orchestration hub must read this repository, inspect the target project, preserve existing work, add only missing prerequisites, validate the result, and stop before product development unless separately approved.

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

Read `BOOTSTRAP_CONTRACT.md`, `MANIFEST.md`, and `docs/PIPELINE.md` before applying it to another repository.
