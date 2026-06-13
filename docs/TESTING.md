# Pipeline Validation Strategy

The universal pipeline itself is validated by checking:

- Required canonical files exist
- Duplicate version-style Markdown names are absent
- Prompts and templates exist
- GitHub workflow exists
- Current status remains truthful

After adoption into a product repository, application-specific testing is added only after the stack is selected.

Future product test layers:

1. Static checks
2. Unit tests
3. Integration tests
4. End-to-end browser tests
5. Security tests
6. Independent audit
7. Founder usability testing
