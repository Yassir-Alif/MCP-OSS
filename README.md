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

## Reference Implementation: L-MCP

This repository includes a **reference implementation** of the MCP-OSS
architecture, referred to as **L-MCP (Local Model Context Plane)**.

### Purpose

L-MCP exists to:
- validate the architecture defined in RFC-0000
- demonstrate deterministic intent handling, decision, and enforcement
- provide a concrete, auditable execution model

L-MCP is **non-normative**.  
The RFC remains the sole architectural authority.

### Scope

The reference implementation focuses on:
- local execution
- explicit intent lifecycle management
- policy-based decision and enforcement
- capability isolation
- auditability and observability

It is **not** a product, framework, or SDK.

### Repository Structure

core/ – control plane logic (intent, decision, enforcement, audit)
host/ – local runtime and orchestration
server/ – capability execution interfaces
dashboard/ – reference monitoring and audit UI


### Conformance

L-MCP is intended to be **RFC-0000 compliant**.

Any deviation from the RFC must be explicitly documented.
Architecture changes require a new RFC.

---

## Contact

Yassir Alif  
yassir-alif@t-online.de
