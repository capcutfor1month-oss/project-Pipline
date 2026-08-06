# Current State

## Repository purpose

Canonical universal pipeline for all future projects.

## Current phase

Founder Autopilot communication experience improved; operational validation pending.

## Active change

`founder-friendly-communication-contract`

## Completed

- Bootstrap contract
- Pipeline manifest
- Shared agent rules
- End-to-end workflow
- Tool registry
- Fresh-session recovery entry point
- Reusable prompts and change templates
- GitHub validation workflow
- External skills registry
- Stage-based skill routing
- Skill precedence and context rules
- Founder Autopilot operating contract
- Automatic natural-language workflow routing
- Governed context, ticket, handoff, and review rules
- Matt Pocock skills mapped into OpenSpec without duplicate sources of truth
- Founder-readable evidence requirements
- Founder-Friendly Communication Contract
- Plain-language session recovery before technical status
- Founder summary separated from canonical technical evidence
- Mandatory `What you should do now` ending for meaningful responses
- Pipeline update recommendations recorded in the repository
- Risk-based validation strategy completed in `docs/TESTING.md` (base risk tiers, cumulative specialized evidence profiles, canonical recording surface, deterministic independent-audit triggers)
- Implementation test/output scope in `prompts/implement-change.md` bounded to the smallest tests covering the changed behaviour, expanding only on recorded risk, dependency surface, failure/uncertainty, or an explicit project gate, with commands/diffs/logs/test output kept summarized (commit `85ddab1`)
- Claude session action, canonical route, and compiled task brief separated as three distinct handoff parts in `docs/CONTEXT_MANAGEMENT.md`, wired into `START_HERE.md`'s fresh-session steps (lock founder decisions before agent prompts, choose continue/`/compact`/`/clear`/`/help` before each handoff, display the session action separately from the task prompt, interpret worker reports before routing, and not rely on old chat memory) (commit `203da50`)
- Fresh-session portability defect fixed: when only the pipeline/governance repository (or any copy or fork) is given, `START_HERE.md` offers four neutral paths — start a new project, resume an existing project, brainstorm and shape a new idea, or work on the Project-Pipeline itself — with no repository required before brainstorming, instead of recommending a named project (commit `1921748`, refining the earlier binary-question fix in commit `8677694`); hardcoded personal-project references removed from `docs/CURRENT.md`'s "Exact next action" (commit `8677694`) and from `docs/PIPELINE_UPDATE_RECOMMENDATIONS.md` and `docs/INDEX.md`'s pilot-plan wording (commit `0e2e621`)
- Repository-identity and authority-boundary correction implemented (DEC-017): `README.md` carries a first-screen, self-sufficient identity warning; `START_HERE.md` gains a "Repository identity, at any point in a conversation" check that fires regardless of message position, not only on the first meaningful message; `AGENTS.md` gains a durable "Target-domain authority vs development-governance authority" rule and a "Repository comprehension" rule requiring recovery of a repository's own canonical entry documents before any recommendation; `BOOTSTRAP_CONTRACT.md` requires preserving an existing target repository's domain authorities and stopping to ask when a change is ambiguously process-level vs product-level; `MANIFEST.md` requires each adopted project's `docs/INDEX.md` to record its own authority-boundary generically; `docs/TESTING.md` gains generic onboarding/repository-identity regression scenarios; `scripts/check_pipeline.py` validates the new required language and scans all Markdown for the specific real-world domain example that surfaced the defect

## Registered skill sources

- `phuryn/pm-skills`
- `mattpocock/skills`
- `coreyhaines31/marketingskills`

## Current blocker

The communication contract is defined, but it still needs pipeline validation and a real-project pilot to confirm that agents consistently guide the founder instead of returning audit-style status dumps.

## Not included

- Changes to workflow stages
- Changes to approval gates
- Changes to safety rules
- Changes to agent responsibilities
- Product definition
- Product architecture
- Application code
- Product deployment
- Fully autonomous production actions

## Exact next action

Validate the repository-identity and authority-boundary correction (run `scripts/check_pipeline.py`, confirm no regressions), then validate and merge the Founder-Friendly Communication Contract, then test fresh-session recovery, mid-conversation URL handling, and one real project stage on a target project the founder supplies. Treat any response that ends with a raw status table, technical verdict, or unexplained next action as a pipeline defect.
