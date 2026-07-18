# Universal Development Pipeline

Founder Autopilot Mode is the default interface. The founder describes product problems, desired results, priorities, feedback, and approvals. The orchestration hub automatically manages technical workflow, skills, contexts, agents, specifications, evidence, and safe progression.

```text
Founder product problem or desired result
    ↓
ChatGPT repository recovery and automatic workflow classification
    ↓
Automatic product clarification and relevant skills
    ↓
Founder-approved decisions
    ↓
Prototype only when a named uncertainty needs runnable evidence
    ↓
OpenSpec change and risk classification
    ↓
Tickets only when multiple focused contexts are required
    ↓
Gemini CLI or OpenCode investigation
    ↓
Claude implements one approved slice
    ↓
Fresh-context builder-side review
    ↓
GitHub Actions automated checks
    ↓
Playwright repeatable browser tests
    ↓
Antigravity exploratory UX verification
    ↓
Codex independent audit
    ↓
Founder manual test and approval
    ↓
Preview deployment
    ↓
Production release and verification
    ↓
Sentry technical monitoring
    ↓
PostHog product-behaviour evidence
    ↓
Relevant marketing and growth skills
    ↓
Next approved change
```

## Founder interface

The founder should be able to say naturally:

```text
Continue this project
I have a new idea
This part is confusing
Build this approved feature
Something is broken
Check Claude's work
Prepare this for release
What should we build next?
```

The orchestration hub infers the correct workflow. Do not require special commands, skill names, token management, technical agent selection, or manual prompt construction.

Read `docs/FOUNDER_AUTOPILOT.md` for the complete operating contract.

## Founder communication layer

Every pipeline stage produces two outputs:

1. A founder-facing explanation governed by `docs/FOUNDER_COMMUNICATION.md`
2. Canonical technical evidence stored in the appropriate repository report

The technical report is the durable evidence record. It must not be pasted unchanged as the complete founder-facing response.

The orchestration hub must translate stage evidence into:

- Where the project stands
- What the current step means and why it matters
- What has already happened
- What happens next
- What the founder needs to decide or do
- The recommended action and reason

Technical evidence follows the understandable explanation. Every meaningful founder-facing response ends with `What you should do now`.

## Automatic request routing

| Request type | Default route |
|---|---|
| Continue | Recover `CURRENT.md`, decisions, active change, branch, evidence, and exact next action |
| New idea | Discovery, assumptions, feasibility, clarification, and product approval |
| Confusing experience | User journey clarification, repository inspection, scoped specification, UX verification |
| Small safe change | Brief inspection, lightweight approval record, implementation, checks, founder preview |
| Normal feature | Clarification, specification, investigation, implementation, review, CI, audit, founder test |
| Large feature | Clarification, prototype if needed, complete specification, tickets, one focused context per slice, final spec comparison |
| Bug | Reproduction, diagnosis, regression test, smallest fix, checks, risk-scaled audit |
| Production incident | Freeze unrelated work, evidence, diagnosis, hotfix, regression test, rapid audit, approval, production verification |
| Audit request | Read-only independent review of specification, diff, evidence, security, regressions, and tests |
| Release request | Verify preview or production gates before any deployment action |
| Prioritisation | Recover product evidence, blockers, risks, and propose the smallest valuable next change |

## Stage ownership and internal skill routing

The orchestration hub chooses skills automatically. Skill names are implementation details and may be reported afterward for transparency.

1. **Recovery — ChatGPT**  
   Confirm access, read canonical documents, inspect active state, report recovery confidence, and avoid guessing.

2. **Discovery and clarification — Founder + ChatGPT**  
   Use relevant PM discovery, assumption, opportunity, interview, and repository-aware clarification workflows such as `grill-with-docs`. Ask the founder only product-level questions.

3. **Strategy — Founder + ChatGPT**  
   Use product vision, value proposition, business model, prioritisation, pre-mortem, and red-team workflows when the decision needs them. Skills advise; the founder decides.

4. **Prototype decision — Orchestration hub**  
   Prototype only when discussion and static inspection cannot answer a named uncertainty. A prototype is disposable, isolated, uses no production data, answers one question, and is not automatically production code.

5. **Specification — ChatGPT + founder approval**  
   Store the approved destination, behaviours, boundaries, risks, and acceptance criteria in the active OpenSpec change. Use specification skills internally when useful.

6. **Ticketing — Orchestration hub**  
   Create or update `tasks.md` only when work requires multiple focused implementation contexts. Do not create competing local tickets, issues, or specifications without a distinct approved purpose.

7. **Investigation — Gemini CLI or OpenCode**  
   Read-only by default. Inspect architecture, existing flows, reusable components, tests, data, access control, and risks. Do not make product decisions.

8. **Implementation — Claude**  
   Use relevant engineering workflows such as TDD, disciplined diagnosis, domain modelling, and codebase design. Implement one approved slice and remain bounded by the complete specification.

9. **Builder-side review — Fresh context or subagent**  
   Compare the implementation against the complete specification, code quality, tests, and unrelated changes. This improves work but is not independent release approval.

10. **Automated checks — GitHub Actions**  
    Run static checks, tests, build, migrations, pipeline validation, and other deterministic gates against the exact commit.

11. **Repeatable browser tests — Playwright**

12. **Exploratory UX verification — Antigravity**

13. **Independent audit — Codex**  
    Audit the specification, diff, evidence, security, privacy, tenancy, migrations, regressions, and test quality. The implementer or its internal review cannot replace this stage when risk requires it.

14. **Final approval — Founder**

15. **Release — Approved hosting and deployment systems**

16. **Production evidence — Sentry, PostHog, logs, and smoke tests**

17. **Launch and growth — Founder + ChatGPT**  
    Use marketing and growth capabilities only after trustworthy product context and measurable evidence exist.

## Canonical skills-output mapping

```text
OpenSpec spec.md
= approved destination and acceptance criteria

OpenSpec tasks.md
= ordered implementation slices

repository-report.md
= investigation evidence

implementation-report.md
= builder evidence

verification-report.md
= deterministic verification evidence

ux-report.md
= user-flow evidence

audit-report.md
= independent Codex verdict
```

A skill may generate or transform information, but approved durable output must be mapped into these canonical records rather than create a competing source of truth.

## Skill-selection rule

The approved sources and precedence rules are in `docs/SKILLS.md`.

For every task, the orchestration hub must:

1. Identify the current stage and request type.
2. Determine risk and required gates.
3. Select the smallest relevant capability set.
4. Load only the instructions needed by the working agent.
5. Record durable approved outcomes in canonical project documents.
6. Prevent skills from expanding scope or overriding founder-approved truth.

The founder is not responsible for these steps.

## Context-management rule

Read `docs/CONTEXT_MANAGEMENT.md`.

- Continue in one context for small, clear, bounded work.
- Create durable specification and tasks for multi-session work.
- Use one approved ticket per focused implementation context.
- Start fresh contexts or handoffs when changing agent, stage, branch, repository, or when the context shows repetition, contradiction, forgotten requirements, or scope drift.
- Do not use one fixed token threshold for every model.

## Prompt-efficiency rule

ChatGPT should write the smallest prompt that preserves correctness.

- Do not repeat context already established in canonical files.
- Reference existing documents, commits, issues, and reports.
- Include the current objective, changed constraints, required behaviours, verification, permitted actions, and expected return.
- Keep non-goals only when they prevent likely scope expansion.
- Use full handoffs only when changing context boundary.
- Never remove critical acceptance criteria, safety boundaries, founder decisions, or verification requirements to save tokens.

Default compact handoff:

```text
Objective
Approved specification and ticket
Requirements
Verification
Files or scope
Permissions and prohibitions
Required return
```

## Risk scaling

- Documentation change: ChatGPT → reviewed repository update
- Small safe code change: lightweight specification → Claude → CI → founder preview
- Normal feature: clarification → specification → investigation → Claude → builder review → CI → Codex → founder
- UI-sensitive feature: add Playwright and Antigravity
- Database-sensitive feature: add migration, preservation, tenancy, and recovery evidence
- Authentication, payments, secrets, or tenant-isolation change: full high-risk gates and controlled release
- Production incident: dedicated incident workflow and production verification
- Launch or growth change: establish product-marketing context and measurable evidence first

## Context recovery

Every new focused conversation reads:

- `docs/CURRENT.md`
- `docs/DECISIONS.md`
- `docs/FOUNDER_AUTOPILOT.md`
- `docs/FOUNDER_COMMUNICATION.md`
- `docs/PIPELINE.md`
- `docs/CONTEXT_MANAGEMENT.md`
- `docs/TOOLING.md`
- `docs/SKILLS.md`
- Active OpenSpec change

Chat is the control room. The repository is the memory.
