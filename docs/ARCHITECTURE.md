# Target architecture — pending validation

## Shape
**Modular monolith** first, split services when workload justifies it. TypeScript monorepo, React/Vite PWA frontend, NestJS/Fastify API, PostgreSQL with RLS, S3-compatible private object storage, Redis/BullMQ async processing, versioned accounting/tax core, server-side model gateway. Architectural choice is a proposal, not an implemented fact. **Product decision:** managed cloud web application at launch; separate local installation later only if validated. See `DEPLOYMENT_STRATEGY.md`.

## Sequence
1. Authenticated user/tenant posts metadata, gets short-lived upload grant.
2. Backend checks entitlements and tenant, uploads encrypted object, anti-malware/format checks, records immutable document hash, persists job.
3. Queue worker classifies/splits, extracts proposed fields (with page provenance), validates against static schemas and OCR/visual evidence.
4. Deterministic core checks amounts, vendor, dates, duplicates, correct historical tax rules, approved PCGE mapping; creates exception cases.
5. Reviewer sees original, field-by-field evidence and draft entry; corrects & approves; transaction commits approved posted journal with audit evidence.
6. Bank imports produce independently auditable statement movements and suggested allocations.
7. Export adapter creates versioned package, stores checksum/status, human controls external DGI import and acceptance evidence.

## Modules
`apps/web`, `apps/api`, `apps/worker`, `packages/contracts`, `packages/money`, `packages/tax-rules`, `packages/coa`, `packages/export-adapters`, `packages/security`, `packages/licensing`, `packages/testing`, `infra`.

## Contract enforcement and data portability
- `billing/entitlements` bounded context tracks first-year service, annual renewals, quota/cost ledger, grace/read-only/export states; all writes are checked in API not client JS.
- Expiry may restrict new paid work after contractual grace, but **never silently deletes documents, cancels approved journal entries, or prevents contractual lawful data export**.
- Future self-hosting can reuse domain core only if persistence, upgrades, licensing and customer data migration have independently passed acceptance tests.

## Security boundaries
- App API is the only write interface to approved financial records; AI worker can only write suggestions.
- Tenant context may not originate solely from user-submitted arbitrary tenant_id.
- RLS and application authorization tests with adversarial cross-dossier accesses.
- Keys exclusively server-side, managed secrets, role permissions, upload/file limits and audit.
- PostgreSQL transactions, idempotency keys and explicit state transitions; durable queues/retries; no 'successful' ACK until persisted.

## Status machine
`UPLOADED -> PROCESSING -> NEEDS_REVIEW -> APPROVED -> POSTED -> EXPORTED -> EXTERNALLY_ACCEPTED`.
`FAILED/REJECTED/DUPLICATE_SUSPECTED` are separate recognized states with reason codes and safe reprocessing.

## Open architecture ADRs
- Prisma vs Drizzle; resident hosting; primary AI vision model and fallback; multipart processing; bank adapters; first accounting export; exact tax rules. See `DECISIONS.md`.
