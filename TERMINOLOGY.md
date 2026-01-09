# Terminology – MCP-OSS

This glossary defines all normative terms used across MCP-OSS.
Terms are authoritative as defined in RFC-0000.

If a term is not listed here, it is not part of the architecture.

---

## Core Entities

**Intent**  
Explicit, structured representation of an intended action.
Root entity of all execution flows.

**Decision**  
Deterministic evaluation of an intent against policies, context,
system state, and capability metadata.

**Enforcement**  
Technical mechanism that enforces a decision result.
Mandatory for all executions.

**Capability**  
Explicitly declared, isolated ability with a manifest and
statically bound permissions.

---

## Architectural Layers

**Control Plane**  
Layer responsible for intent handling, decision-making,
enforcement, and audit.
Produces no side effects.

**Data Plane**  
Layer responsible for actual execution and side effects.
Contains no decision logic.

---

## Components

**MCP Client**  
Component that creates structured intents and submits them
to the MCP-OSS Core.

**MCP-OSS Core**  
Central control plane consisting of MCP-OSS Host and MCP-OSS Server.

**MCP-OSS Host**  
Runtime environment for decision and enforcement logic.

**MCP Server (Standard)**  
Component responsible for controlled capability execution.

**MCP-OSS Agent**  
Optional execution plane for external or distributed capabilities.

---

## Lifecycle and State

**Intent Lifecycle**  
The ordered set of states an intent passes through:
CREATED → APPROVED → EXECUTION_PENDING → EXECUTED | FAILED

**State Transition**  
Explicit, irreversible change between intent states.
Always audited.

---

## Security and Policy

**Policy**  
Explicit rule set evaluated during decision-making.

**Permission**  
Statically bound authorization required by a capability.

**Default-Deny**  
Security principle where all actions are denied unless
explicitly approved.

**Least Privilege**  
Principle of granting only the minimum required permissions.

---

## Observability

**AuditLog**  
Immutable record of intent states, decisions, enforcement,
and execution results.

**DecisionTrace**  
Record of inputs and outcome of a decision.

**ExecutionResult**  
Outcome of capability execution.

---

## Errors

**PolicyError**  
Violation of policy constraints.

**PermissionError**  
Missing or invalid permission.

**ExecutionError**  
Failure during capability execution.

**SystemError**  
Failure of the MCP system itself.

---

## Scope Rules

- Terms are case-sensitive.
- Definitions are normative.
- Synonyms are intentionally avoided.
- Ambiguous terms are invalid.

In case of conflict, RFC-0000 prevails.
