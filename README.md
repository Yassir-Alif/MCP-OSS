# MCP-OSS

## Model Context Plane – Open System Stack

MCP-OSS defines an explicit **Model Context Plane** for LLM-based systems.

It introduces a strict architectural separation between:

- **Intent**
- **Decision**
- **Enforcement**
- **Capabilities**

This separation enables **deterministic execution**, **policy-based control**, and **full auditability** of model-driven actions.

MCP-OSS is **not** an agent framework and **not** a tool orchestration layer.  
It is a **control plane** that governs how actions are requested, approved, and executed.

---

## What Problem MCP-OSS Solves

Large Language Models currently mix:

- reasoning  
- decision-making  
- execution  
- security assumptions  

inside a single, opaque runtime.

This leads to:

- non-deterministic behavior  
- weak or implicit security boundaries  
- missing audit trails  
- unclear responsibility between model and system  

MCP-OSS separates these concerns **by design**.

---

## Architecture Overview

MCP-OSS enforces a fixed and explicit execution flow:

Intent → Decision → Enforcement → Capability


Key architectural properties:

- Intent is a first-class, addressable entity.
- Decisions are policy-based and externally auditable.
- Enforcement is explicit and deterministic.
- Capabilities are isolated, replaceable, and non-authoritative.

The architecture is invariant across **local**, **hybrid**, and **distributed** deployments.

---

## Reference Implementation (L-MCP)

This repository contains a **frozen Local MCP (L-MCP) reference implementation**.

Location:


Key architectural properties:

- Intent is a first-class, addressable entity.
- Decisions are policy-based and externally auditable.
- Enforcement is explicit and deterministic.
- Capabilities are isolated, replaceable, and non-authoritative.

The architecture is invariant across **local**, **hybrid**, and **distributed** deployments.

---

## Reference Implementation (L-MCP)

This repository contains a **frozen Local MCP (L-MCP) reference implementation**.

Location:

reference/l-mcp/AISys_Gemini


Status:

- ✅ Frozen proof-of-concept  
- ✅ Normative reference for MCP-OSS  
- ❌ Not production-hardened  

The implementation strictly follows:

- RFC-0000  
- The MCP-OSS architecture model  

It exists to **demonstrate architectural correctness**, not performance or scalability.

See:

reference/l-mcp/AISys_Gemini/FROZEN.md


---

## What MCP-OSS Is Not

MCP-OSS is deliberately **not**:

- a chatbot framework  
- an agent runtime  
- a workflow engine  
- a prompt-management tool  

MCP-OSS operates **below** these layers as a control plane.

---

## Governance and Status

- Specification-driven (RFC-based)
- Architecture-first
- Security and auditability as primary constraints

Current maturity:

- Architecture: stable  
- RFC: published (Draft-00)  
- Reference implementation: frozen  
- Production usage: explicitly out of scope  

---

## Repository Structure

RFC/ # Normative specification (RFC-0000)
reference/l-mcp/ # Frozen L-MCP reference implementation
ARCHITECTURE.md # Visual and structural architecture overview
TERMINOLOGY.md # Consistent terminology glossary
GOVERNANCE.md # Project governance model
SECURITY.md # Security model and assumptions
CONTRIBUTING.md # Contribution rules and architectural constraints
RELEASES.md # Release and versioning notes


---

## License

Apache License 2.0

