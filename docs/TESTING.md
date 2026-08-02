# Pipeline Validation Strategy

## Purpose

Testing effort should match risk, not habit. A copy-only doc change and an auth-schema migration must not receive the same gate. This document defines the risk tiers, the required evidence per tier, and how that evidence maps into canonical reports.

## Pipeline self-validation

The universal pipeline itself is validated by `scripts/check_pipeline.py` and `.github/workflows/pipeline-checks.yml`, which check:

- Required canonical files exist
- Duplicate version-style Markdown names are absent
- Prompts and templates exist
- Approved skill sources are recorded in `docs/SKILLS.md`
- Required governance language is present in canonical documents
- Current status remains truthful

This self-validation runs on every change to the pipeline repository itself and does not scale by risk — it is a fixed structural check.

## Product-level risk tiers

After adoption into a product repository, application-specific testing is added only after the stack is selected. Every approved change is then classified into one tier before implementation. The specification records the tier and the reason.

| Tier | Examples | Required evidence |
|---|---|---|
| **Trivial** | Copy, docs, comments, non-behavioural refactor | Reviewed repository update. No test run required beyond existing CI. |
| **Low** | Internal tool, non-customer-facing config, isolated bug fix with existing test coverage | Static checks, unit tests covering the change, founder preview |
| **Standard** | Normal feature, UI change, new endpoint without sensitive data | Static checks, unit tests, integration tests, builder-side review, CI, founder preview |
| **UI-sensitive** | New or changed user-facing flow, navigation, forms | Standard tier plus Playwright repeatable browser tests and Antigravity exploratory UX verification, recorded in `ux-report.md` |
| **Data-sensitive** | Schema or migration change, data model change, bulk write | Standard tier plus migration test, data-preservation check, tenancy-isolation check, rollback plan recorded in `verification-report.md` |
| **High** | Authentication, payments, secrets, tenant isolation, production migration, customer data | Data-sensitive or UI-sensitive tier (whichever applies) plus mandatory Codex independent audit and founder manual approval before release |
| **Incident** | Production is broken now | Dedicated incident workflow — reproduction evidence, smallest fix, regression test, rapid audit, production verification. Normal gate order may compress but not disappear. |

This table is the same risk scaling already declared in `docs/PIPELINE.md`; this document defines what evidence each tier must produce, not a separate policy.

## Test layers

Available layers, used only where the tier requires them:

1. **Static checks** — lint, type check, pipeline validation
2. **Unit tests** — the smallest unit covering the changed behaviour
3. **Integration tests** — cross-module or cross-service behaviour the change affects
4. **End-to-end browser tests** — Playwright, for UI-sensitive tier and above
5. **Security tests** — for High tier: auth, injection, access control, secret handling
6. **Independent audit** — Codex, for High tier and when risk otherwise requires it
7. **Founder usability testing** — manual approval step before release, for Standard tier and above

Do not add a layer a tier does not require. A Trivial or Low-tier change that grows a Playwright suite or demands a Codex audit is a pipeline defect in the other direction — wasted verification cost with no matching risk.

## Evidence mapping

Test evidence is not a free-standing artifact. It is recorded in the canonical reports already defined in `docs/PIPELINE.md`:

```text
static + unit + integration results  → verification-report.md
browser and UX test results          → ux-report.md
independent audit findings           → audit-report.md
```

Do not create a separate test-tracking document or duplicate issue system for evidence that already has a canonical home.

## Tier mismatch

If investigation or implementation reveals the actual risk is higher than the tier recorded in the specification (for example, a "Standard" change turns out to touch authentication), stop and reclassify before continuing. Do not finish implementation under the original tier and add missing evidence retroactively.
