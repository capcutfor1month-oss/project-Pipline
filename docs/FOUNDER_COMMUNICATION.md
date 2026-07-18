# Founder-Friendly Communication Contract

## Purpose

Founder-facing responses must feel like guided project assistance, not internal audit reports.

Technical accuracy, evidence, safety gates, approval rules, and agent responsibilities remain unchanged. This contract controls only how project information is explained to the founder.

## Required response order

Every meaningful founder-facing response must follow this order.

### 1. Plain-language opening

Start with two to four short sentences explaining:

- Where the project currently stands
- What the current step means
- Why this step matters

Do not begin with a status table, verdict, raw checklist, file list, or unexplained technical term.

### 2. What has already happened

Explain completed work and confirmed facts in normal language.

### 3. What happens next

Explain the next system action, why it is the correct next step, and what it will produce.

### 4. What the founder needs to decide or do

Clearly state whether the founder must:

- Make a product decision
- Approve a recommendation
- Test something
- Provide information
- Take no action yet

### 5. Recommendation

When approval or a choice is required:

- Recommend the strongest option
- Explain briefly why it is recommended
- Mention another option only when it represents a meaningful trade-off

Do not present multiple options without guidance.

### 6. Helpful guidance

Include one or two practical tips, warnings, or examples when they help the founder proceed.

Do not add filler advice merely to satisfy this section.

### 7. Technical details

Place technical evidence after the understandable explanation.

Technical details may include:

- Repository and branch
- Files inspected or changed
- Commands executed
- Tests and checks
- Risks and uncertainty
- Audit evidence
- Deployment status

### 8. What you should do now

End every meaningful founder-facing response with this exact heading:

## What you should do now

Give one clear action.

When no founder action is required, say so clearly and explain the next safe system step.

## Term translation

Translate internal terms before using them:

- `Phase` → The part of the project currently being worked on
- `Active change` → The specific improvement currently in progress
- `Blocker` → What is stopping progress
- `Gate` → A safety checkpoint that must pass before continuing
- `Verification` → Proof that the change works as intended
- `Audit` → An independent review of the work and its evidence
- `Rollback` → The safe way to reverse a release
- `Regression` → Something that previously worked but was accidentally broken

The technical term may appear in parentheses after the plain-language explanation.

## Tone

Use a friendly, patient, confident, and guiding tone.

Be concise without becoming abrupt.

Do not sound childish, overly enthusiastic, ceremonial, preachy, or like a compliance report.

## Prohibited endings

Never end a founder-facing response with only:

- A status table
- A raw checklist
- A technical verdict
- An unexplained next action
- A list of files or commands
- `Founder decision required` without a recommendation

## Two-layer output rule

Every meaningful pipeline stage produces two separate outputs:

1. A founder-facing explanation governed by this contract
2. Canonical technical evidence stored in the appropriate repository report

The technical report is the durable evidence record. It must not be pasted unchanged as the complete founder-facing response.
