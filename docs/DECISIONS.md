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

---

## DEC-005 — Approved skill sources

**Decision:** Approve `phuryn/pm-skills`, `mattpocock/skills`, and `coreyhaines31/marketingskills` as external capability sources for projects using this pipeline.

**Reason:** Together they add structured product management, engineering discipline, and marketing/growth workflows without replacing the pipeline or founder authority.

**Status:** Active

---

## DEC-006 — Lazy skill activation

**Decision:** Skills are selected by project stage and task, loaded in the smallest relevant set, and recorded in project-specific `docs/SKILLS.md` files. Entire libraries are not injected into every project or conversation.

**Reason:** This preserves capability while reducing context bloat, instruction conflicts, and unnecessary token use.

**Status:** Active

---

## DEC-007 — Instruction precedence

**Decision:** Founder-approved decisions, canonical project documents, and the approved active specification take precedence over external skill instructions.

**Reason:** Skills are advisers and execution aids; they must not silently change scope, architecture, or product truth.

**Status:** Active
