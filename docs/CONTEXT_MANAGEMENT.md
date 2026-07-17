# Context Management

## Purpose

AI development quality degrades when a working context becomes overloaded, repetitive, contradictory, or detached from repository truth. The orchestration hub manages context automatically; the founder does not manage token budgets or decide when to clear a session.

## Core rule

```text
The repository stores durable truth.
A focused context performs one bounded stage or implementation slice.
Temporary chat history is never the only source of an approved decision.
```

## Same-context work

Continue in the same focused context when:

- The task is small and clearly specified
- Relevant repository state is already understood
- No major product or architecture decision is unresolved
- The work can reasonably finish as one implementation slice
- The agent continues to remember constraints and acceptance criteria accurately

Small work may follow:

```text
clarify briefly → implement → verify → report
```

## Durable specification and fresh context

Create or update the active OpenSpec change and start a fresh focused context when:

- Investigation consumed substantial context
- The work requires more than one implementation slice
- A different agent, tool, repository, branch, or pipeline stage will continue the work
- The agent repeats questions already answered
- Requirements are forgotten or contradicted
- Scope starts expanding without approval
- The agent struggles to locate prior decisions
- Raw logs, temporary summaries, or unrelated files dominate the session

Do not rely on a universal token-number threshold. Use behavioural evidence and task complexity.

## Specification and ticket roles

```text
spec.md = the approved destination, behaviours, boundaries, and acceptance criteria
tasks.md = the ordered implementation slices used to reach the destination
```

Create tickets only when the approved work needs multiple focused implementation contexts. Do not create a competing local issue tracker when OpenSpec already serves the purpose.

## One-ticket execution rule

For multi-session work:

```text
one approved ticket
→ one focused implementation context
→ tests and internal review
→ implementation evidence
→ update task status
→ clear context before the next ticket when needed
```

Every ticket remains subordinate to the complete approved specification. Completing a ticket does not prove the complete change is finished.

## Handoffs

A handoff is required when changing:

- Agent
- Session
- Repository
- Branch
- Pipeline stage
- Implementation ticket

A compact handoff should reference repository documents rather than copy the entire conversation.

```text
Objective
Approved specification and ticket
Current branch and commit
Files or areas in scope
Checks already run
Known failures or uncertainty
Required return
```

## Fresh-context review

The implementer should use a fresh reviewer context or subagent to check:

- Complete specification adherence
- Code quality and unnecessary complexity
- Test completeness
- Unrelated changes
- Missed acceptance criteria

This internal review is builder-side quality control. It cannot issue the independent release verdict. Codex remains the independent auditor when required by risk.

## Temporary material

Temporary summaries, exploratory notes, raw logs, and prototype output must not silently become canonical truth.

- Approved durable outcomes go into canonical project documents or the active OpenSpec change.
- Raw logs should be summarized and linked or stored outside the main context when retention is necessary.
- Disposable prototypes answer one named question and are not automatically production code.

## Founder experience

The founder must never be told to:

- Calculate context usage
- Choose when to clear the context
- Decide whether to create tickets
- Invoke a handoff skill
- Reconstruct a specification from old chat messages

The orchestration hub makes these decisions and explains only the product-relevant result and next approval gate.
