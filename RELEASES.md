# Releases and Versioning – MCP-OSS

This document defines the release and versioning scheme for MCP-OSS.
It is derived from RFC-0000 and applies to both specification and code.

---

## Versioning Model

MCP-OSS follows a dual-track versioning model:

- **RFC Versions** define architecture
- **Code Versions** validate RFCs

RFCs are authoritative.

---

## RFC Versioning

RFCs use monotonically increasing numbers.

Examples:
- RFC-0000 (core architecture)
- RFC-0001 (streaming and cancellation)
- RFC-0002 (distributed MCP)

Rules:
- RFCs are append-only
- Changes require new RFCs or new RFC versions
- Breaking changes require a new major RFC

---

## Code Versioning

Code releases follow semantic versioning:
MAJOR.MINOR.PATCH


### Meaning
- MAJOR: incompatible architectural change (new RFC)
- MINOR: new RFC-conformant features
- PATCH: bug fixes only

---

## Release Tags

### RFC Tags
Used for specification milestones.

Format:
rfc-0000-draft-00
rfc-0000-final


---

### Code Tags
Used for repository releases.

Format:
v0.1.0
v0.2.0
v1.0.0


Optional suffixes:
- `-rc1`, `-rc2` for release candidates
- `-exp` for experimental builds

---

## Mapping RFC ↔ Code

Every code release MUST reference:
- the supported RFC(s)
- the RFC version

Example:
v0.1.0

conforms to RFC-0000 Draft-00


---

## Release Rules

- No release without RFC reference
- Experimental features must be labeled
- `main` branch is always RFC-conformant
- Experiments live on feature branches only

---

## Stability Guarantees

- RFC-0000 Draft-00: architecture stable, implementation evolving
- RFC-0000 Final: architecture frozen
- Code v1.0.0: stable reference implementation

---

## Philosophy

Architecture leads.
Code follows.
Releases reflect this order.


