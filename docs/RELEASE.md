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
