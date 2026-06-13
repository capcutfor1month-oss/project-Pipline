# Tooling Registry

| Tool | Role | Initial status in a new project |
|---|---|---|
| GitHub | Durable source of truth | Active |
| OpenSpec | Change specification and scope | Ready to configure |
| Gemini CLI | Investigation and verification | Ready to configure |
| OpenCode | Low-cost alternate worker | Optional / ready to configure |
| Claude Code | Production implementation | Ready to configure |
| Codex | Independent audit | Ready when a diff exists |
| GitHub Actions | Automated checks | Active for pipeline validation |
| Playwright | Repeatable browser testing | Requires runnable web app |
| Antigravity | Exploratory UX verification | Requires local or preview app |
| Design OS | Complex UX design support | Optional |
| Agent OS | Permanent standards support | Partly represented by agent files |
| Task Master | Large task dependency management | Optional |
| BMAD | Full-team methodology reference | Optional |
| Preview hosting | Safe live testing | Requires approved architecture |
| Production hosting | Public runtime | Requires release candidate |
| Sentry | Technical production monitoring | Requires runtime/framework |
| PostHog | Product behaviour evidence | Requires privacy-safe events |
| GitHub Agentic Workflows | Low-risk repository automation | Add after manual pipeline is stable |

## Token-efficiency rule

Reserve Claude for implementation. Use scripts, GitHub Actions, Gemini CLI, or OpenCode for exploration, repetitive checks, and log summarization.

## Tool-selection rule

Do not use every tool for every change. Scale the pipeline according to risk.
