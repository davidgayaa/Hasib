# Cloud-first / Hybrid-ready deployment strategy
**State:** Proposed target design. No domain registered, server provisioned, deployment or audit completed.

## Phase 1: Managed cloud web application
- Marketing website on validated brand domain; authenticated app under a dedicated subdomain such as `app.<verified-domain>`; API behind TLS/reverse proxy. These are *patterns*, not real deployed URLs.
- Browser is untrusted presentation only: React/TypeScript PWA with secure session handling; no Gemini, WhatsApp or Telegram credentials in browser.
- Application server hosts tenant-scoped authenticated APIs, permission checks, annual entitlement checks, document ingestion, domain logic and controlled export endpoints.
- PostgreSQL in managed encrypted service with tenant boundaries and negative isolation tests; private encrypted document storage; async workers/queues for model calls.
- Daily backup policy proposed with separately protected copies; **prove** restores on schedule, enforce recovery targets via contract after engineering test.
- Three distinct environments: dev, staging, production. Migrations with rollback/forward-recovery, full logs excluding sensitive document contents, metrics, alerts and incident playbooks.
- Determine hosting residency and every subprocessor/AI destination before approving CNDP/legal notices and customer contractual terms. Do not assert that Moroccan storage alone resolves transfers.

## Phase 2: Optional on-premise edition (only if justified)
- Reuse accounting core/domain packages; package a separate desktop client or LAN-based server + UI after a deliberate feasibility assessment.
- Local DB, encrypted document store, tenant/firm roles, backups, install/upgrade tools, license validation policy and disaster recovery plan must be independently designed/tested.
- Avoid automatic assumption that local edition works without internet: cloud AI, official messaging, payment activation and optional updates may still require connectivity.
- No two-way cloud/local sync promised until conflict resolution, encryption, idempotency, timezones, offline revisions and regulatory effects are specified and tested.
- A perpetual local licence (if eventually chosen) may keep supported offline core operations running after optional support expiry. Never revoke access to historic customer records without contract and legal basis.

## Deployment decision matrix
| Requirement | Managed cloud MVP | Optional on-premise later |
|---|---|---|
| Updates / security patches | Centralized | Per-client controlled rollouts |
| AI provider connection | Server-side gateway | Local gateway to remote provider or approved local model |
| Backup duty | Vendor manages contractually | Shared/client-defined with validation |
| Upfront infrastructure | Our hosted environment | Client equipment/install complexity |
| Cost of supporting many sites | Lower initially | Significantly higher, unproven |

## Before spending on infrastructure
Confirm data locality, hosting vendor agreement, domain/trademark clearance, traffic expectations, budget, recovery targets (RTO/RPO), incident contact, subprocessor contracts and CNDP obligations with qualified counsel.
