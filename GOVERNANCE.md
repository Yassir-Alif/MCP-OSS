# Governance – MCP-OSS

This document defines the governance model of MCP-OSS.
It is normative for all contributions, decisions, and releases.

MCP-OSS follows an RFC-first principle.

---

## Normative Basis

- RFC-0000 is the binding reference architecture
- Implementations are non-normative
- In conflicts, the RFC prevails

No code, PR, or discussion may introduce semantics outside an RFC.

---

## Roles

### Maintainer
- manages RFCs
- decides on RFC acceptance
- ensures architectural coherence
- may reject contributions without justification

Initial Maintainer:
- Yassir Alif

### Contributors
- provide code, docs, or tests
- have no architectural authority
- explicitly accept RFC precedence

---

## Decision Model

### Architecture
- decided exclusively via RFCs
- explicit and versioned
- never implicit via code

### Implementation
- must not extend or weaken RFCs
- is replaceable
- may be refactored at any time

---

## RFC Lifecycle

1. Draft submission
2. Discussion
3. Maintainer decision
4. Versioning
5. Optional reference implementation

RFCs are append-only.
Changes require new versions.

---

## Releases

- releases are RFC-conformant
- no release without RFC reference
- experimental features must be labeled

---

## Conflict Resolution

- no democratic voting on architecture
- maintainer decision is final
- forking is explicitly allowed

---

## Purpose

- protect the architecture
- prevent scope drift
- ensure long-term maintainability
- preserve technical clarity

MCP-OSS is a control plane.
Governance protects this property.
