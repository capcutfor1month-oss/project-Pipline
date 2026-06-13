# Pipeline Decision Log

## DEC-001 — Canonical source

**Decision:** `capcutfor1month-oss/project-Pipline` is the canonical source for the founder's common project pipeline.

**Reason:** The pipeline must be independent from any individual product repository.

**Status:** Active

---

## DEC-002 — Control model

**Decision:** ChatGPT remains the main strategy and orchestration hub; GitHub is durable project memory.

**Reason:** Long chat context must not be the only source of project truth.

**Status:** Active

---

## DEC-003 — Coding ownership

**Decision:** Claude is the default production-code implementer; Gemini CLI or OpenCode handles investigation and economical verification; Codex performs independent audit.

**Reason:** Role separation improves reliability and token efficiency.

**Status:** Active

---

## DEC-004 — Safe adoption

**Decision:** Empty repositories may receive the scaffold directly; existing repositories require inspection and a setup branch.

**Reason:** Existing code and project-specific instructions must be preserved.

**Status:** Active
