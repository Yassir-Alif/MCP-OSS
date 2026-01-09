# Security Policy – MCP-OSS

This document describes the security model of MCP-OSS.
It is normative and derived directly from RFC-0000.

Security is an architectural invariant.

---

## Foundations

- language models are untrusted
- inputs may be malicious
- capabilities are inherently dangerous
- security must be enforceable, not heuristic

---

## Default Deny

- all actions are denied by default
- capabilities require explicit grants
- implicit permissions are forbidden

No execution without decision and enforcement.

---

## Least Privilege

- minimal required permissions
- statically bound
- no dynamic escalation

Permissions are part of the capability manifest.

---

## Control vs Data Plane

Hard rule:
- control plane has no side effects
- data plane makes no decisions

Any mixing is a security violation.

---

## Enforcement as Anchor

- enforcement is technically binding
- no direct capability access
- no bypass via code paths or config

Security is achieved by mechanism, not convention.

---

## Isolation and Sandboxing

- capabilities must be isolated
- sandbox assumptions documented
- escapes are security vulnerabilities

---

## Error Handling and Fail-Safe

- errors cause deterministic abort
- no automatic retries without new intent
- no silent degradation

Fail-safe means abort, not continue.

---

## Auditability

- every intent is auditable
- every decision traceable
- every error classified

Non-auditable actions are security incidents.

---

## Reporting

Report security issues directly to the maintainer.

Contact:
Yassir Alif  
yassir-alif@t-online.de
