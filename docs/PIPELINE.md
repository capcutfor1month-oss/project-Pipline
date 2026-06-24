# Universal Development Pipeline

```text
Founder + ChatGPT
    ↓
Product discovery and approved decisions
    ↓
Relevant PM and clarification skills
    ↓
OpenSpec change folder
    ↓
Gemini CLI or OpenCode investigation
    ↓
Relevant engineering skills
    ↓
Claude implementation
    ↓
GitHub Actions automated checks
    ↓
Playwright repeatable browser tests
    ↓
Antigravity exploratory UX verification
    ↓
Codex independent audit
    ↓
Founder approval
    ↓
Preview deployment
    ↓
Production release
    ↓
Sentry technical monitoring
    ↓
PostHog product-behaviour evidence
    ↓
Relevant marketing and growth skills
    ↓
Next approved change
```

## Stage ownership and skill routing

1. **Discovery — Founder + ChatGPT**  
   Use PM discovery, assumption mapping, opportunity-solution-tree, interview, and `grill-with-docs` skills when relevant.

2. **Strategy — Founder + ChatGPT**  
   Use product vision, value proposition, business-model, prioritisation, pre-mortem, and strategy-red-team skills. Skills advise; the founder decides.

3. **Specification — ChatGPT + founder approval**  
   Use PRD, roadmap, user-story, test-scenario, `to-prd`, `to-issues`, and domain-language skills. Save approved outcomes in the active OpenSpec change.

4. **Investigation — Gemini CLI or OpenCode**  
   Read-only by default. Use domain-modelling or architecture-analysis skills only when they improve repository understanding.

5. **Implementation — Claude**  
   Use `tdd`, `codebase-design`, and related engineering skills selectively. Implementation remains bounded by the approved specification.

6. **Automated checks — GitHub Actions**  
   Static checks, tests, build, migrations, and other deterministic gates.

7. **Repeatable browser tests — Playwright**

8. **Exploratory UX verification — Antigravity**

9. **Independent audit — Codex**  
   Audit the specification, diff, evidence, security, regressions, and test quality. Do not let the implementing skill or agent approve its own work.

10. **Final approval — Founder**

11. **Release — Approved hosting and deployment systems**

12. **Production evidence — Sentry and PostHog**

13. **Launch and growth — Founder + ChatGPT**  
   Use product-marketing, customer-research, copywriting, CRO, signup, analytics, launch, SEO, retention, referral, sales, and growth skills only after trustworthy product context exists.

## Skill-selection rule

The approved sources and precedence rules are in `docs/SKILLS.md`.

For every task:

1. Identify the current pipeline stage.
2. Select the smallest relevant skill set.
3. Load only those skills.
4. Record durable decisions and outputs in canonical project documents.
5. Do not let skills silently expand scope or override founder-approved truth.

## Prompt-efficiency rule

ChatGPT should write the smallest prompt that preserves correctness.

- Do not repeat repository, branch, role, workflow, or safety context already established in the active session or canonical project files.
- Reference existing documents, commits, issues, and audit reports instead of copying their contents.
- Include only the current objective, changed constraints, required behaviours, tests, and expected return.
- Remove repetitive commands and obvious restatements.
- Keep non-goals only when they prevent likely scope expansion.
- Use full handoffs only when context is changing agents, sessions, repositories, or phases.
- Never shorten a prompt by removing a critical acceptance criterion, security boundary, founder decision, or verification requirement.

Default compact handoff shape:

```text
Objective
Requirements
Verification
Files or scope
Return
```

## Risk scaling

- Documentation change: ChatGPT → reviewed repository update
- Small code change: specification → Claude → CI → founder
- Normal feature: discovery skills as needed → specification → investigation → engineering skills as needed → Claude → CI → Codex → founder
- UI-sensitive feature: add Playwright and Antigravity
- High-risk feature: research, assumption and strategy review, explicit specification, full automated checks, browser evidence, Codex, founder, controlled release
- Launch or growth change: establish product-marketing context first, then use only relevant marketing skills and measurable evidence

## Context recovery

Every new focused conversation reads:

- `docs/CURRENT.md`
- `docs/DECISIONS.md`
- `docs/PIPELINE.md`
- `docs/TOOLING.md`
- `docs/SKILLS.md`
- Active change folder

Chat is the control room. The repository is the memory.
