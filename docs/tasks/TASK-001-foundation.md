# TASK-001 — secure foundation and real project state
**Status:** NOT STARTED | **Owner:** Unassigned | **Created:** 2026-10-18 | **Revised:** 2026-10-18

## Goal
Create a working version-controlled **cloud-first** project with an authenticated, tenant-isolated shell, backend, CI, staging deployment plan and persistent status documentation. No financial automation or live billing yet.

## Suggested work
- Validate framework choices in ADR, initialize Git monorepo web/api/worker/shared packages and lint/format/test scripts.
- Add PostgreSQL migrations for firms, entities, membership, audit events and sanitized document metadata; RBAC and strict RLS test. Define subscription/entitlement interfaces only; do not implement payment collection in this task.
- Implement server-side secrets config, user auth, secure health endpoint, empty portfolio UI, CI and basic cloud deployment staging. Do not put AI credentials in browser.
- Run security checks and publish *actual* commands and outcomes.

## Acceptance criteria
- Clone -> boot instructions reproducible on developer machine.
- Cross-tenant read/write access is rejected by API and DB-level tests.
- No API or messaging tokens present in client bundle/Git.
- Schema migration forward and backward plan tested.
- Architecture describes an annual renewal and secure exit/export approach consistent with contracts, without pretending to have implemented checkout.
- Unit/integration/security tests and CI pass, no false 'done' status.
- `docs/STATUS.md`, architecture ADR, this task file updated with results and next task.

## Evidence log — to be filled on execution
- Git branch / commit: **NOT YET EXECUTED**
- Files changed: **NOT YET EXECUTED**
- Commands/test results: **NOT YET EXECUTED**
- Deploy link: **NOT YET EXECUTED**
- Risks / blockers: **UNASSESSED**

## Developer / QA handoff protocol — V2.3
- **Implementer:** Gemini. **Independent reviewer:** ChatGPT. **Final approval/merge:** project owner.
- **Developer state:** PLANNED. **QA verdict:** NOT_REVIEWED. **Owner decision:** PENDING.
- Gemini must append developer report containing exact branch/PR/commit SHA, code paths and actual test outputs. Gemini must not set QA PASS or edit the completed ledger.
- ChatGPT must create fresh numbered `docs/qa/TASK-001-review-NN.md` for each independent review. No QA result exists yet.
- A FAIL becomes CHANGES_REQUESTED; a missing diff/log becomes NEEDS_EVIDENCE. Neither is DONE. PASS requires review of exact implementation commit.
- Only after explicit owner approval and merge on main may TASK-001 appear in `docs/TASKS_DONE.md`.
