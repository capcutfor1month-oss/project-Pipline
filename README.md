# Universal Agentic Project Pipeline

This repository is the canonical reusable development pipeline for all future projects owned by the founder.

## Repository identity — read this first

This is a development-governance repository. It governs how repository changes are clarified, approved, specified, investigated, implemented, tested, audited, and released.

It is not a target product. It does not contain, define, or supply any product philosophy, feature model, methodology, or domain terminology. If this URL was pasted into a conversation about a different project — at the start of that conversation or in the middle of one already underway — treat it only as a development-governance reference. Do not fold any of its concepts into that project's product philosophy, domain workflow, or terminology. The target project's own canonical documents remain authoritative for what that product is.

Being given this URL, by itself, does not authorize applying the Pipeline to whatever is currently being discussed. It does not prove whether the founder wants to inspect this repository, apply it to a named target project, brainstorm or shape a project with it as governance, compare it against another approach or repository, modify Project-Pipeline itself, or something else entirely. Resolve that intent — see `START_HERE.md` — before changing or reframing anything.

If the URL you were given resolves to this repository itself (`capcutfor1month-oss/project-Pipline`, or any copy or fork identified by its own canonical documents), read `START_HERE.md` before choosing what to do next.

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
