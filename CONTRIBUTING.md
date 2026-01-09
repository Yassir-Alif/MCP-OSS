# Contributing to MCP-OSS

Contributions are welcome but subject to strict architectural rules.
This project prioritizes coherence and determinism over feature velocity.

---

## Fundamental Rule

RFC-0000 is the sole architectural source.

If it is not in the RFC:
- it is not a valid concept
- it must not be implemented
- it is not a feature

---

## Accepted Contributions

- bug fixes within existing semantics
- tests
- documentation improvements
- RFC-conformant reference implementations

---

## Rejected Contributions

- new concepts without RFC
- implicit semantics
- heuristics
- shortcuts
- mixing control and data plane
- agent logic
- autonomous decision mechanisms

---

## Hard Architecture Rules

### Intent
- root entity
- no code without explicit intent
- no implicit actions

### Decision
- deterministic
- reproducible
- no side effects

### Enforcement
- mandatory
- technically enforced
- no capability access without enforcement

### Capability
- explicit registration
- mandatory manifest
- fixed permissions
- required isolation

---

## Control vs Data Plane

Strict separation. No exceptions.

- control plane produces no IO
- data plane makes no decisions
- no execution feedback into decision

Violations result in immediate rejection.

---

## Error Handling

- every error is classified
- every error is auditable
- errors deterministically terminate intents

Silent failures or implicit fallbacks are prohibited.

---

## Tests

Contributions MUST:
- be deterministically testable
- produce reproducible results
- correctly model the intent lifecycle

---

## Pull Requests

Each PR MUST include:
- RFC reference (section or number)
- affected architecture component
- justification of RFC conformance

PRs without RFC reference will be closed.

---

## Philosophy

MCP-OSS is not:
- an experiment playground
- an agent sandbox
- a heuristics framework

MCP-OSS is a control plane.

If you do not accept these constraints,
this project is not suitable.
