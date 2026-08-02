# Pipeline Adoption and Versioning

## Adoption

A target repository is pipeline-ready when:

- Canonical documents exist without duplicates
- Agent roles and boundaries are recorded
- Current state is truthful
- Pipeline validation passes
- No product work began without approval

## Versioning

Git history is the pipeline version history.

Do not create files named:

- `pipeline-final.md`
- `pipeline-latest.md`
- `pipeline-v2.md`

## Updating adopted projects

Future pipeline improvements must not be pushed blindly into every project. Inspect each target repository and apply only compatible changes through a reviewed update.

## Post-release validation (Stage 16)

This section is this repository's software-specific mechanics for DEC-016 ("Bounded validation after lock"). It applies to Stage 16, "Production evidence," in `docs/PIPELINE.md`, and does not generalize that stage beyond software.

After release, Stage 16 evidence (Sentry, PostHog, logs, smoke tests) is checked against the change's acceptance criteria.

- If evidence matches the approved change, the change is complete.
- If evidence shows a failure, repair follows the existing change workflow in `AGENTS.md`: Claude fixes within the originally approved scope, not a redefinition of it.
- Repair depth and required audit rigor scale with the risk tier already recorded for the change in `docs/TESTING.md`. This section does not define a separate attempt count.
- Each repair produces another instance of `verification-report.md` against the same change lineage — not a new report file.
- `docs/CURRENT.md` records the current repair attempt and the failing evidence under the existing `Active change` and `Exact next action` fields — no new field is added.
- A successful repair returns to the same Stage 16 production verification, not a new validation target.
- If repair would require changing the locked scope or acceptance criteria, exhausts the tier-appropriate bounded attempt allowance, or leaves risk unresolved, escalate to the existing Production-incident route (`docs/PIPELINE.md`) and the manual rollback and production-migration gates already required by DEC-012. Do not repeat repair attempts past this point and do not roll back automatically.

Verification and independent audit stages do not perform this repair themselves (`prompts/verify-change.md`, `prompts/audit-change.md`); repair returns to Claude's implementation stage, then back through fresh verification and audit before the change is considered complete again.
