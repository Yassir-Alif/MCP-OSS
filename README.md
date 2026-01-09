# MCP-OSS
## Model Context Plane – Open System Stack

MCP-OSS is an architectural control plane for LLM-based systems.
It explicitly separates Intent, Decision, Enforcement, and Capabilities,
enabling secure, deterministic, and auditable execution of actions.

This repository contains the reference implementation (L-MCP) and is
normatively derived from RFC-0000.

---

## Motivation

Large Language Models lack an inherent control plane.
Tool-calling, agent frameworks, and workflows mix decision-making,
execution, and security assumptions.

MCP-OSS introduces an explicit Model Context Plane between model, user,
and execution environment.

---

## Architecture Overview

MCP-OSS strictly separates two layers:

### Control Plane
- Intent
- Decision
- Enforcement
- Audit

### Data Plane
- Execution
- IO
- Side effects

Rule:
The control plane MUST NOT produce side effects.

---

## Core Concepts

### Intent
Explicit, structured description of an intended action.
Intent is the root entity of all flows.

### Lifecycle

CREATED → APPROVED → EXECUTION_PENDING → EXECUTED | FAILED


All transitions are deterministic, auditable, and irreversible.

---

### Decision
Evaluates an intent against policies, context, system state,
and capability metadata.

---

### Enforcement
Technically enforces the decision result.
No capability access without enforcement.

---

### Capability
Explicitly declared, isolated ability with a manifest,
statically bound permissions, and defined isolation.

---

## Components

- MCP Client
- MCP-OSS Core
  - MCP-OSS Host
  - MCP Server (Standard)
- Optional: MCP-OSS Agent

---

## Reference Implementation: L-MCP

This repository includes a fully functional reference implementation:

- deterministic intent state machine
- real enforcement
- capability isolation
- audit logging
- monitoring dashboard (read-only)

The implementation is non-normative and validates the RFC.

---

## RFC-First Principle

- RFC-0000 is normative
- Code follows the RFC
- No feature without RFC reference
- Architecture changes are RFC-first

---

## License

### Specification (RFC)
Creative Commons Attribution 4.0 International (CC BY 4.0)

### Code
See `LICENSE`.

---

## Status

- RFC-0000: Draft-00
- L-MCP: end-to-end validated reference implementation
- Dashboard: reference UI (monitoring/audit)

---

## Scope

MCP-OSS is not:
- an agent framework
- a tool-calling wrapper
- a workflow system

MCP-OSS is a control plane.

---

## Contact

Yassir Alif  
yassir-alif@t-online.de
