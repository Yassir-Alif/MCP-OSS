# RFC 0000 – MCP-OSS  
## Model Context Plane – Open System Stack

---

## Status
Draft-00

## Category
Informational / Architecture

## Author
Yassir Alif

## Contact
yassir-alif@t-online.de

## Date
2026-01-09

## License
Creative Commons Attribution 4.0 International (CC BY 4.0)

---

## Abstract

This specification defines MCP-OSS (Model Context Plane – Open System Stack),
an architectural control plane for LLM-based systems.
MCP-OSS explicitly separates Intent, Decision, Enforcement, and Capabilities,
enabling secure, deterministic, and auditable execution of actions independent
of the underlying language model.

---

## 1. Motivation and Objectives

Large Language Models (LLMs) are highly capable in text generation but lack an
inherent control plane for the safe, auditable, and deterministic execution of
actions. Existing approaches such as tool-calling, agent frameworks, or
workflow systems tightly couple decision logic, execution, and security
assumptions, resulting in implicit and difficult-to-audit control flows.

MCP-OSS addresses this structural gap by introducing an explicit **Model Context
Plane** that acts as an independent control layer between the model, the user,
and the execution environment.

### 1.1 Objectives

- Explicit modeling of intents
- Deterministic decision and enforcement paths
- Strict separation of control plane and data plane
- Full auditability of all actions
- Model-, vendor-, and runtime-independence

### 1.2 Non-Goals

- Autonomous agent systems
- Self-learning decision logic
- Workflow orchestration
- Prompt engineering or model optimization

---

## 2. Terms and Definitions (Normative)

**MCP Client**  
Component responsible for creating structured intents and submitting them to
the MCP-OSS Core.

**MCP-OSS Core**  
Central control plane consisting of the MCP-OSS Host and MCP Server (Standard).

**MCP-OSS Host**  
Runtime environment for decision and enforcement logic.

**MCP Server (Standard)**  
Component responsible for the controlled execution of registered capabilities.

**MCP-OSS Agent**  
Optional execution plane for external or distributed capabilities.

**Intent**  
An explicit, structured representation of an intended action, including context
and metadata.

**Decision**  
Evaluation of an intent against policies, context, and system state.

**Enforcement**  
Deterministic technical enforcement of a decision outcome.

**Capability**  
An explicitly declared, isolated capability with statically bound permissions.

**Control Plane**  
Layer responsible for intent handling, decision-making, and enforcement.

**Data Plane**  
Layer responsible for actual execution with side effects.

---

## 3. Design Principles (Normative)

- Intent is the root entity of all actions
- Every action has an explicit lifecycle
- Decisions are reproducible
- Enforcement is mandatory
- Security follows a default-deny model
- Auditability is an invariant

---

## 4. System Architecture (Normative)

MCP-OSS consists of logically separated components:

- MCP Client
- MCP-OSS Core  
  - MCP-OSS Host  
  - MCP Server (Standard)
- Optional: MCP-OSS Agent

### 4.1 Responsibility Separation

- The control plane decides **whether** an action may be executed
- The data plane executes **what** has been decided
- No feedback loop from data plane to control plane is allowed

---

## 5. Intent Model (Normative)

### 5.1 Intent Structure

An intent MUST contain at least:
- a unique `intent_id`
- a declared action
- a target capability
- contextual information
- a timestamp

### 5.2 Intent Lifecycle

CREATED → APPROVED → EXECUTION_PENDING → EXECUTED | FAILED


### 5.3 State Rules

- Transitions are explicit
- Backward transitions are prohibited
- Every transition generates audit entries

### 5.4 Derived Artifacts

- AuditLog
- DecisionTrace
- ExecutionResult

---

## 6. Decision Model (Normative)

### 6.1 Decision Inputs

- Intent
- Policy set
- System context
- Capability metadata

### 6.2 Decision Outcomes

- APPROVED
- REJECTED
- DEFERRED (optional)

Decision outcomes are final for the given intent.

---

## 7. Enforcement Model (Normative)

- Enforcement is strictly deterministic
- No capability access without a valid decision
- Enforcement must technically enforce policy results

---

## 8. Capability Model (Normative)

### 8.1 Registration

- Every capability must be explicitly registered
- Registration may be static or controlled dynamic

### 8.2 Manifest

A capability manifest defines:
- name
- allowed actions
- required permissions
- isolation properties

### 8.3 Isolation

- Capabilities MUST NOT introduce implicit side effects
- Sandbox assumptions MUST be explicitly documented

---

## 9. Control Plane vs Data Plane (Normative)

| Control Plane | Data Plane |
|--------------|-----------|
| Intent       | Execution |
| Decision     | Side Effects |
| Enforcement  | IO |
| Audit        | Resources |

Any mixing of responsibilities is architecturally invalid.

---

## 10. Error and Failure Model (Normative)

### 10.1 Error Categories

- PolicyError
- PermissionError
- ExecutionError
- SystemError

### 10.2 Error Rules

- Every error is classified
- Every error generates audit data
- Errors deterministically terminate the intent lifecycle

---

## 11. Security Model (Normative)

- Default-deny principle
- Least-privilege
- Explicit capability grants
- No implicit trust assumptions

---

## 12. Observability and Audit (Normative)

- Every intent must be fully traceable
- Logs must be correlatable
- Audit data must be immutable

---

## 13. Reference Implementation (Non-Normative)

The L-MCP implementation serves as a reference to validate this specification.
Implementation details are non-normative as long as all normative requirements
of this RFC are fulfilled.

---

## 14. Scope and Non-Scope (Informative)

MCP-OSS is:
- not an agent framework
- not a tool-calling wrapper
- not a workflow system

MCP-OSS is a control plane.

---

## 15. Versioning and Evolution

- RFCs are the normative source
- Implementations follow RFCs
- Breaking changes require new major RFCs
- Extensions are introduced via new RFCs

---

