# HISAB-AI — delivery roadmap

**Version:** 2026-10-18 (process V2.2). **Source of truth:** actual repository code, schema, tests and Git history. This roadmap tracks plans and evidence; no phase may be called complete without validation. Commercial product will be hosted cloud-first, with annual service and maintenance renewals; local/on-premise is separate future feasibility work.

| Milestone | Scope | Gate / required evidence | State | Next task |
|---|---|---|---|---|
| M0: Discovery & specification | Product V2.1, business model, architecture, legal risk register | Reviewed draft docs; open sign-offs tracked | SPEC DRAFTED; validations pending | Qualify potential customers; brand/legal review |
| M1: Foundation & Security | Repo, TypeScript monorepo, UI shell, API, PostgreSQL, auth/RBAC, tenant RLS, audit, secret management, CI, staging plan | Reproducible setup; API+DB cross-tenant deny tests; CI output; migration/restore evidence | NOT STARTED | `TASK-001-foundation.md` |
| M2: Document workflow | Signed uploads, safe storage, scanning, PDF image workflows, extraction suggestions, source-linked evidence, corrections | Test corpus field metrics; access controls; review trace; no secret exposure | NOT STARTED | To create after M1 |
| M3: Deterministic accounting | Centime integer posting, Decimal intermediates, PCGE mappings, double-entry drafts, approvals/audit/reversals | Golden tests, professional review, no direct AI posting | NOT STARTED | To create after M2 |
| M4: Bank & matching | Bank CSV/Excel/PDF import, integrity checks, partial and 1:N matching, dispute queue | Bank fixture reconciliation, no duplicate transactions | NOT STARTED | To create after M3 |
| M5: Tax & exports | Versioned Moroccan tax rules, approved TVA/RAS cases, adapter-based exports | Official schemas independently validated, accountant/legal approval, external acceptance evidence where applicable | NOT STARTED | To create after M4 |
| M6: Controlled cloud pilot | Domain, security/privacy contract work, customer onboarding, backup restoration, quotas & entitlements, support process | Pilot sign-off, response/reliability metrics, recovery drill, data exit test, real pricing economics | NOT STARTED | To create after M5 |
| M7: Market launch & scale | Sales, billing, renewal, support, monitoring, usability benchmarks | Paid pilot/renewal contract proof; measured competitor baseline; secure operations | NOT STARTED | To create after M6 |
| Future: optional on-premise | Self-hosted deployment/licensing after validated demand | Independent installation, upgrade, backup, security and licence testing | DEFERRED | Not in MVP |

## Prioritization rules
- Never mark a feature complete from design mockups, generated code alone, or undocumented claims.
- Promote a milestone to COMPLETE only after its gate evidence is archived in tasks and tests.
- If scope changes, log an ADR and impact on price, security, privacy, time and maintenance obligations.
- Keep unverified Moroccan regulatory assumptions in `docs/LEGAL_RULES_REGISTER.md` until authorized validation.

## Near-term decision queue
1. Verify GitHub ownership/access and private repo.
2. Confirm provisional tech stack and local development setup; record open ADRs.
3. Execute TASK-001 in small tested increments.
4. Interview Moroccan accountants and price-test proposed first-year + annual maintenance packages.
5. Investigate CNDP/privacy processing, providers and hosting location before real data is uploaded.

## Completion-control update V2.3
A roadmap milestone cannot be marked COMPLETE merely because Gemini claims success or CI passes. The relevant tasks must be approved by independent QA at the reviewed commit, explicitly accepted by the owner, merged to protected `main`, and indexed in `docs/TASKS_DONE.md`. Failed QA iterations remain in `docs/qa/`. See `docs/QA_PROTOCOL.md`.

## Process V2.4 — architect continuation
The independent QA resume index is `docs/CHATGPT_ARCHITECT_MEMORY.md`. ChatGPT reads it first, then verifies the current milestone against this roadmap, `docs/TASKS_DONE.md`, the latest QA report, actual Git/CI and application code. Current M1 remains **NOT STARTED**, TASK-001 is **PLANNED**; the additional file does not complete development work.
