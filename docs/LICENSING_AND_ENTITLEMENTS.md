# Licensing, entitlements and renewal lifecycle
**Status:** Draft product policy, not legal contract or implemented code.

## Separate concepts
- `first_year_package_fee`: onboarding/setup + first annual service term, split clearly on invoices and in signed offer.
- `annual_service_renewal`: hosted access, planned software updates, platform security, allocated storage and AI credits, support and backup arrangements.
- `perpetual_license`: **not offered by the cloud MVP**. May be a distinct later on-premise contract, with permitted post-maintenance use specified separately.
- `data_ownership_and_export`: contractual right to retrieve customer's source and derived records, subject to legal/retention obligations.

## Entitlement data model (proposal)
- `plans`: version, limits by active dossiers, staff, monthly documents/pages, storage, integrations and included support.
- `contracts`: firm_id, commercial terms/version, signature, service start/end, retention policy, export window, contact.
- `subscriptions`: firm_id, plan_id, term start/end, status, paid-through, renewal decision, payment-provider external reference.
- `entitlements`: signed source, feature/limit type, quota and effective date (checked on server).
- `usage_ledger`: tenant, metered event idempotency key, provider usage, actual cost and document reference; never duplicate billing after retry.
- `renewal_events`: reminders, receipts, disputes, grace periods and explicit human interventions, immutable audit events.

## Proposed non-renewal state machine
`TRIAL / ACTIVE -> RENEWAL_DUE -> GRACE_PERIOD -> READ_ONLY_EXPORT -> CLOSED_FOR_NEW_WORK`.
Use explicit dates, communication and terms; permit legally required retention and secure data export. Final time windows require legal and commercial approval. No processing of paid AI inference in a non-entitled state unless contract explicitly permits it.

## Security / controls
Entitlement checks must not bypass tax/ledger authorization. Never use client-side license switches as sole enforcement. Protect webhook signatures, verify payment-state transitions server-side, segregate billing admin access from customer accounting records. Support overrides require reason, expiry and audit log. Billing issues may restrict new uploads but never mutate ledger balances or remove source evidence.

## Required tests before commercialization
Expired plan cannot create paid extraction jobs; tenant A cannot see B's billing or data; retry never bills twice; entitlements apply identically to API and UI; renewals restore permitted operations; grace/read-only retains export; customer export includes attachments, metadata and audit without cross-tenant leakage; outages do not irreversibly lock data.
