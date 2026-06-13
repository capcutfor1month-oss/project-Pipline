# Universal Development Pipeline

```text
Founder + ChatGPT
    ↓
Product discovery and approved decisions
    ↓
OpenSpec change folder
    ↓
Gemini CLI or OpenCode investigation
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
Next approved change
```

## Stage ownership

1. **Discovery:** Founder + ChatGPT
2. **Specification:** ChatGPT + founder approval
3. **Investigation:** Gemini CLI or OpenCode
4. **Implementation:** Claude
5. **Automated checks:** GitHub Actions
6. **Repeatable browser tests:** Playwright
7. **Exploratory UX verification:** Antigravity
8. **Independent audit:** Codex
9. **Final approval:** Founder
10. **Release:** Approved hosting and deployment systems
11. **Production evidence:** Sentry and PostHog

## Risk scaling

- Documentation change: ChatGPT → reviewed repository update
- Small code change: specification → Claude → CI → founder
- Normal feature: specification → investigation → Claude → CI → Codex → founder
- UI-sensitive feature: add Playwright and Antigravity
- High-risk feature: research, explicit specification, full automated checks, browser evidence, Codex, founder, controlled release

## Context recovery

Every new focused conversation reads:

- `docs/CURRENT.md`
- `docs/DECISIONS.md`
- `docs/PIPELINE.md`
- `docs/TOOLING.md`
- Active change folder

Chat is the control room. The repository is the memory.
