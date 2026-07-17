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

## DEC-006 — Automatic skill activation

**Decision:** Skills are selected automatically by the orchestration hub according to project stage, request type, and risk. The smallest relevant set is loaded and recorded; the founder is never responsible for skill routing.

**Reason:** The founder should work in product language while the system manages context efficiency and developer capability selection.

**Status:** Active

---

## DEC-007 — Instruction precedence

**Decision:** Founder-approved decisions, canonical project documents, and the approved active specification take precedence over external skill instructions.

**Reason:** Skills are advisers and execution aids; they must not silently change scope, architecture, or product truth.

**Status:** Active

---

## DEC-008 — Founder Autopilot default

**Decision:** Founder Autopilot Mode is the default operating experience. The founder provides product problems, desired behaviour, priorities, feedback, and approvals; the orchestration hub manages recovery, clarification, skills, agents, specifications, contexts, evidence, and handoffs.

**Reason:** The pipeline exists to let a non-coder founder operate a controlled software-development department without learning developer workflows.

**Status:** Active

---

## DEC-009 — Canonical skill-output mapping

**Decision:** External workflows must map approved durable output into the active OpenSpec change and canonical reports. They may not create competing specifications, ticket systems, or sources of truth.

**Reason:** Duplicate specs and issue systems create contradictions and make session recovery unreliable.

**Status:** Active

---

## DEC-010 — Context and ticket policy

**Decision:** The orchestration hub decides when work fits one focused context and when it requires a durable specification, tickets, and handoffs. Multi-session work normally uses one approved ticket per focused implementation context.

**Reason:** Context management is a technical orchestration responsibility and should not be pushed onto the founder.

**Status:** Active

---

## DEC-011 — Review separation

**Decision:** Claude may use a fresh-context builder-side review before handoff, but Codex remains the independent auditor when required by risk.

**Reason:** Agents often review their own recent work poorly; fresh review improves quality, while independent role separation preserves trust.

**Status:** Active

---

## DEC-012 — Manual safety gates

**Decision:** Founder Autopilot may automate development operations but may not bypass required founder approval for product behaviour, major architecture, destructive data actions, production migrations, customer data, production release, public launch, or unclear rollback decisions.

**Reason:** Automation should reduce operational burden without removing product authority or safety controls.

**Status:** Active
