# Architecture – MCP-OSS

This document is a visual and structural complement to RFC-0000.
It introduces no new semantics.

Normative definitions reside exclusively in the RFC.

---

## Overview

MCP-OSS implements an explicit Model Context Plane between user,
language model, and execution environment.

User / UI
|
v
MCP Client
|
v
+----------------------+
| MCP-OSS Core                 |
| ------------------------ |
| Intent                   |
| Decision                 |
| Enforcement              |
| Audit                    |
| +----------------------+ |
|                          |
| v                        |
| +----------------------+ |
| Data Plane               |
| ----------------------   |
| Capabilities             |
| Execution                |
| IO / Side Effects        |
| +----------------------+ |


---

## Control Plane

Responsibilities:
- intent handling
- decision-making
- enforcement
- audit

Properties:
- deterministic
- state-based
- no side effects

---

## Data Plane

Responsibilities:
- execution
- IO
- side effects

Properties:
- no decisions
- no policy evaluation
- no intent creation

---

## Intent Lifecycle

CREATED
|
v
APPROVED
|
v
EXECUTION_PENDING
|
+--> EXECUTED
|
+--> FAILED


All transitions are explicit, auditable, and irreversible.

---

## Decision and Enforcement Flow

Intent → Decision → Enforcement → Capability Execution


Direct jumps are not allowed.

---

## Capability Model

Capability
├─ Manifest
│ ├─ Name
│ ├─ Actions
│ ├─ Permissions
│ └─ Isolation
└─ Execution


Capabilities are explicitly registered, isolated,
and statically permission-bound.

---

## Audit Flow

Intent
├─ DecisionTrace
├─ EnforcementResult
└─ ExecutionResult


Audit is a primary architectural goal.

---

## Local vs Distributed MCP (Conceptual)

- L-MCP: all components local
- D-MCP: control plane local, execution distributed

Semantics remain identical.

---

## Boundaries

MCP-OSS is not:
- an agent framework
- a workflow system
- a tool-calling wrapper

MCP-OSS is a control plane.

---

## RFC Relationship

This document explains and visualizes.
RFC-0000 defines and decides.

In conflicts, RFC-0000 prevails.

