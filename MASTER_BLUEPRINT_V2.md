# HISAB-AI 2.0 — Master Product Blueprint (Working title)
**Version:** Draft 2.1 | **Updated:** 2026-10-18 | **Market:** Morocco | **Language:** Darija/FR/AR, with French accounting nomenclature.

> **Status:** Product and architecture proposal, NOT certified accounting software and NOT legal or tax advice. A qualified Moroccan accountant and legal/privacy adviser must sign off on the regulatory rules and exports before commercial use. This improves the uploaded v1 rather than claiming the entire Gemini dialogue was provided.

## 0. Executive decision
Build a **cabinet-first, evidence-first financial operations platform**, not another generic invoicing app. **Go-to-market decision: Cloud-first managed platform with a first-year acquisition/setup payment and annual recurring operations, updates and support; a separately licensed on-premise edition is a later option, not MVP.** The winning workflow is: collect a receipt/invoice/bank statement -> extract every line with provenance -> flag ambiguity -> apply versioned Moroccan accounting and tax rules -> have an authorized reviewer approve -> reconcile payment -> prepare auditable export -> record acceptance/rejection in downstream systems.

Core promise: **less re-entry, clearer exceptions, controlled automation, and traceability from original document to final output**. Do not promise zero mistakes, guaranteed compliance, zero latency, or fully autonomous official filing.

### The naming problem
The product name "HISAB" is already publicly used by **hisab.ma** for a Moroccan accounting/invoicing offering; this is a real market and brand collision risk. Use HISAB-AI as an internal codename only until OMPIC trademark, domain, SEO and app-store clearance. Example naming directions *for verification only*: MizanFlow, DossierPilot, Wathiq Finance. None is asserted available.

## 1. Evidence from the uploaded blueprint
Preserve: multi-dossiers; line-item extraction; split-screen keyboard-first accountant workspace; deterministic finance engine; Moroccan PCGE/CGNC references; Moroccan fiscal workflows including TVA/RAS; document capture and missing-piece requests; bank statement extraction and many-to-many matching; versioned exports to Sage/JBS/Odoo and DGI EDI; cash-flow and overdue-payment monitoring.

Correct: client-only database, client-side AI credentials and Telegram polling, hard-coded current VAT list, universal 0.25% stamp duty, fixed cash threshold without day/supplier and annual context, automatic supplier-only learning, '100% bank complete' from a single equation, assumption of a published TVA XSD, deadline permanently set to day 19, bank matching as sole proof of tax deductibility, a promise of real-time arrival in 3 seconds, and automatic posting solely because a ledger entry balances.

## 2. Competitive picture, verified from vendor websites (features are vendor claims, not independent performance tests)
| Competitor | Public positioning/features | What HISAB-AI must prove instead of asserting superiority |
|---|---|---|
| Experio — experio.ma | OCR invoices, multi-dossiers, automated entries, bank reconciliation, GED, fiscal teledeclarations | Superior reviewer speed on tested documents, confidence with source highlights, transparent exceptions, robust 1:N/N:M match review |
| Claris — claris.ma | Accounting, payroll, legal, OCR, TVA, close, bank, cabinets, Morocco hosting claims | Deep evidence traceability, modular adoption with existing accountants' software, low error escalation |
| Fawatir AI — fawatirai.com | Invoicing, OCR, WhatsApp/copilot, accounting, payroll, bank, low public pricing | Not compete solely on feature count or low price: focus on cabinet production throughput and auditability |
| Sahl Compta — sahlcompta.ma | General ledger, CGNC, payroll, tax, EDI, OCR, cabinet modules | Measured quality of exception workflow and reconciliation workflows |
| Hisab — hisab.ma | e-invoicing readiness, VAT, APIs, accountant plans | Distinct brand and differentiated workflow, not the same name |
| Odoo/Sage/JBS/Ciel | Established production ledger or ERP use cases | Be interoperable with them rather than forcing replacement in MVP |

**Validation:** Interview 8–12 accounting practices from different sizes. For each vendor, request a demo using **the same anonymized real Moroccan test pack** and record tasks, timings, errors, controls and failure recovery. Vendor website features alone do not prove implementation quality.

## 3. Target customers and jobs-to-be-done
**Primary buyer:** Accounting firms and fiduciaires operating 10–100+ client dossiers. They want speed, standardization, audit trails, predictable annual costs, and controlled staff access. Commercial model: upfront first-year package followed by annual renewal for hosting, usage entitlements, updates, security, maintenance and support.
**Secondary user:** Their TPE/PME clients sending invoices and answering missing-document requests through a minimal mobile portal and an opt-in messaging channel.
**Future users:** Multi-company SMEs with internal accountants, then specialized sectors and payroll teams. Avoid expanding to inventory/POS/payroll before the core capture-to-export loop is demonstrably better.

## 4. Product principles
1. **Accounting source of truth is the approved accounting ledger and evidence**, never chat output or model memory.
2. **AI suggests; deterministic engine checks; a permitted human approves** material financial actions.
3. No model request may update source invoices, rules, or ledgers outside versioned domain APIs and permission checks.
4. Historical amounts/tax rules are preserved when law changes; filings use the corresponding historical version.
5. Every field has provenance: document ID, page, bounding polygon if available, extracted text, model version, review status.
6. Status must distinguish detected -> reviewed -> approved -> exported -> accepted/rejected downstream.
7. Default to *draft* for low-confidence, unusual, contradictory, old-period, or tax-sensitive transactions.
8. A ten-minute onboarding exercise and low-friction keyboard-first review matter more than animations.
9. Every institution/connector is an adapter with published capability constraints; no implied official integrations.
10. Clear customer ownership, exportability, retention and deletion controls.
11. Deployment mode and contract entitlement are explicit: web access is a time-bound managed service, not an implied lifetime licence. Never disable customer access to their own data without a clear lawful transition/export process.

## 5. Modules
### 5.1 Firm control centre (MVP)
- Multi-tenant firm -> entities -> fiscal periods; staff invitations, RBAC (owner, accountant, reviewer, client, auditor), 2FA, data-scoped permission matrix; per-dossier configuration.
- Portfolio queue: new, duplicate warning, parsing, awaiting review, approved, ready for export, rejected, pending client reply; aging, overdue, throughput metrics, unknowns.
- Client portal: upload invoices and request status; no access to other clients' data; mobile-first capture with quality guidance.
### 5.2 Document hub (MVP)
- Web upload, drag-drop and email forwarding as secure incoming channels; mobile PWA camera, PDFs, JPG, PNG; check malware, MIME, file size, encrypted PDFs, page count, visual quality.
- PDF page clustering creates *suggestions* for document boundaries; allow an invoice spanning 2+ pages and a PDF containing many invoices.
- SHA-256 exact duplicate + vendor/number/date/amount fuzzy duplicate; keep an explanatory 'potential duplicate' warning, not silently delete evidence.
- Document inbox with missing-piece checks, versioning and original immutable attachment.
- Phase 2: official WhatsApp Business API and Telegram server-side webhook with signed/expiring client connection, opt-in/consent where needed, rate limits, idempotency and privacy messaging.
### 5.3 Extraction and accounting review (MVP)
- Structured JSON extraction with field provenance and per-field confidence; invoice headers, line items, discounts, unit, currencies, supplier/customer ICE/IF, HT, TVA, timbre, tax exemptions, TTC.
- Extraction schema confidence is **not** guaranteed accuracy. Source-linked confidence UI: highlight exact image bounding box on clicking each field; calculate discrepancy and explain why blocked.
- Split-screen PDF and data, customizable shortcuts (Ctrl+Enter only when validation passes), editable allocations, previous/next, batch triage; contrast, RTL and accessibility support.
- Suggest PCGE account with **vendor + purchased good/service + contract/activity + fixed asset policies + prior authorized corrections**; do not auto-post a new class of expense.
- Treat credit notes (avoirs), cancelled invoices, reverse entries, repairs, tax history and cross-period corrections as first-class use cases.
### 5.4 Deterministic Accounting & Moroccan Tax Engine (MVP plus successive packs)
- Amounts posted in integer MAD centimes; `DECIMAL` for quantity, unit price, tax rates and FX intermediate calculations; document per-tax rounding order and rounding mode for each rule. Never derive amounts with JavaScript `Number` arithmetic.
- Balance validation is mandatory but not sufficient: allowed journals, account type, period open, counterparty, taxes, approved documents, credit notes, partial payment allocation, controls for duplicates/reversals.
- Versioned PCGE mapping by dossier and date; reviewer corrections entered as scoped, explainable approval rules with effective date and override reason.
- Tax rule registry: legal basis, applicability predicate, effective_from/to, revision/version, exceptions, source URL, tests, sign-off, review_date. Rules must fail closed (review required) if law uncertain.
- Current 2026 default positive VAT rates typically 10% and 20%, while historic 7%/14% documents must remain valid according to their effective period and category; distinguish exempt with/without deduction and zero-rated situations.
- Tax treatments cover regimes des encaissements/débits, payments incl partial/cash/compensation, exclusions and exemptions, prorata, deductible vs non-deductible tax, timbre conditions and exceptions, cash-payment restrictions per supplier/day/month and legal effective period, RAS TVA and other independent RAS IS/IR mechanisms, foreign supplier and foreign currency.
- Legally sensitive routines require current primary-source check against official CGI and circulars and reviewer acceptance.
### 5.5 Bank reconciliation (first expansion after invoice loop)
- CSV/Excel primary, PDF supported with extra checking; provider import adapters are distinct (CIH, AWB, BCP, BOA) and documented per format, not a promise of live connectivity without consent/API.
- Ledger and imported statement transaction IDs and running balances; check opening/closing/running totals, page sequence, transaction counts, duplicated lines, gaps and exceptions. A matching total alone cannot prove completeness.
- Matching suggestions 1:1, 1:N, N:1, N:M, partial payments, overpayments, bank fees, unmatched credits, bank transfers and foreign exchange; show reason/confidence and approval.
- Cash payment, compensation and manual adjustments are evidence-backed; bank match is not the exclusive legal basis for deductible tax.
### 5.6 Morocco EDI/Exports (controlled rollout)
- Configurable, versioned adapters for Sage/JBS/Ciel/Odoo/CSV; independent golden-file and round-trip tests for each target.
- Export packs must include period, source invoice, accounting entry ID, tax classification, rule version, maker/checker and file checksum.
- SIMPL-TVA XML/ZIP generator only after obtaining a **current official DGI cahier des charges** for the specific declaration and testing with the actual acceptance workflow. Do not universally assume a public XSD exists. Labels: `Prepared`, `Validated locally`, `Uploaded by user`, `Accepted by DGI` (only if evidence), `Rejected`.
- Never store taxpayer DGI passwords, perform unsafe scraping, or claim to submit without a supported official authorized integration.
### 5.7 Payment deadlines and closing (later)
- Law 69-21 logic based on applicability/turnover by relevant fiscal period, invoices/dates, legal default and valid agreed term, amendments, partial payments, penalties, reporting cadence and sign-off. Prior-year filing cadence differs from 2026; version it.
- Closing co-pilot identifies missing supplier/customer docs, unmatched bank items, unreconciled VAT, journals pending review, duplicate credits, and month-lock readiness. It prepares an evidence-based checklist, not a final opinion.
### 5.8 Executive financial copilot (later, guarded)
- Natural-language explanations *with links to evidence*; draft follow-up messages and cash-flow scenarios; no direct posting/filing without reviewer approval.

## 6. Money, math and posting requirements
- Store posted MAD as `BIGINT` centimes; do not use `FLOAT/DOUBLE` for money. Preserve original source currency, original amounts, rate source/date, converted amounts and exchange realization.
- `DECIMAL(24,8)` or equivalent for high-precision quantities/unit prices/FX, then quantize *at the rule-defined stage*. Record roundoff adjustments separately with approved reasons.
- Use `line net HT = quantity × unit HT − discount` only when document's pricing/discount model matches; reconcile against displayed document, taxes, advances, retention, timbre and other charges; discrepant documents remain review-required.
- Example simple entry (not universal): D 6111 1,000.00; D 34552 200.00; C 4411 1,200.00 MAD. An entry may balance and still be wrong if the asset should be capitalized or tax is non-deductible.
- Use **two-phase workflow**: `draft_journal` -> verify/authorize -> `posted_journal` immutable. Fix a posted item via reversal/adjustment with references, not editing in place.
- Bank opening+credits−debits=closing is a necessary arithmetic check; add line counts, running balance and source layout verification.
- Model outputs never set a `passed` status themselves.

## 7. Tax and regulatory review log, to be signed off before implementing rules
| Topic | Why V1 is unsafe | Correct implementation principle | Reference |
|---|---|---|---|
| TVA 2026 | hard-codes 0,7,10,14,20 as contemporaneous | version by tax period: current positive normal/reduced rates 20/10 and historical 7/14, exemptions and category exceptions | CGI 2026 + reform |
| RAS TVA | default 75/100 without party/activity/attestation matrix | engine based on article 117 IV/V, payee/payor, works/equipment/service, attestation age/validity, exclusions, base and payment event | DGI official 2024 notice, subsequent CGI |
| RAS IS/IR | mixes independent withholding families | separate tax obligation objects by nature, payor/payee and effective dates | CGI 2026 |
| Prorata | multiplies any input VAT by 80% | per-applicable input/period and company basis, effect on asset/cost, adjustments | CGI |
| Cash thresholds | 'one invoice >5k' simplistic | check applicable article 106 conditions, day/supplier/month aggregation and exceptions, rule version | CGI article 106 |
| Timbre | always 0.25% cash | calculate when subject, validate exempt entities/operations and legal treatment | CGI art. 252 |
| TVA trigger | ties deducibility to bank match only | account for legal exigibility conditions and proof of effective payment, including alternatives and exceptions | CGI art. 95 et seq. |
| Délais de paiement | treats as simple 60/120 and one cadence | track turnover/cadence, initial/extended term, penalty rate and partial payments | Loi 69-21, DGI notices |
| Filing deadline | fixed 'day 19' | effective-date schedule per obligation/entity/calendar & official extensions; distinguish estimate vs filed | official DGI |
| e-facturation | claims 2026 DGI mandated formats | mark as readiness; do not assert UBL/CII mandatory DGI standard unless formally published | CGI art. 145-IX / official confirmation |
| EDI XML XSD | universal XSD claimed | use versioned official cahier des charges, sample files, acceptance tests; do not assume XSD exists for deductions | DGI portal |
| 10-year archiving | claims blanket storage without nuances | validate legal retention duty and privacy rules, access/legal holds/deletion policies per document class | CGI/CNDP legal review |

## 8. Technical architecture: modular monolith, secure from day one
**Recommended implementation:** TypeScript monorepo to keep shared contracts end-to-end. Web: React + TypeScript + Vite (PWA, React Query, Tailwind); API: NestJS (Fastify adapter); DB: PostgreSQL 16+ (RLS and tenant-scoped authorization); ORM: Prisma or Drizzle after spike; queues: Redis + BullMQ; object storage: S3-compatible private encrypted bucket; AI provider adapter: Google Gemini or replaceable alternative via server-side API; telemetry: OpenTelemetry; tests: Vitest + Playwright and API integration tests. Deploy separate web/api/worker or minimal shared deployment; use IaC and env staging/production. **Launch topology:** product domain + TLS web application; API and asynchronous workers in managed hosting; centralized PostgreSQL and private object storage with tested backups. Keep accounting rules and contracts provider-neutral so an on-premise distribution can be evaluated later; do not promise offline AI or effortless two-way sync.

**Data flow**:
`Client/Web/Email/Approved Messaging -> Upload API -> malware & format checks -> private object storage -> extraction queue -> AI gateway + provenance extraction -> deterministic accounting/tax engine -> human review -> immutable posting journal -> reconciliation -> export adapters -> user checks downstream acceptance.`

**Modular bounded contexts**:
- identity, firms, tenants, users, RBAC
- dossiers/fiscal-periods
- capture/documents/provenance
- extraction/jobs/model ledger
- parties/suppliers
- chart-of-accounts / journal entries / accounting rules
- tax-registry / tax-evaluation / audit
- bank-import / match / payments
- communications/tasks
- export-packages / external-delivery status
- usage/billing/entitlements/licensing/annual-renewals
- internal observability/admin

**Key record tables**:
`firms`, `entities`, `memberships`, `users`, `fiscal_periods`, `documents`, `document_pages`, `extraction_runs`, `extracted_fields`, `invoice_headers`, `invoice_lines`, `suppliers`, `customers`, `tax_rules`, `tax_evaluations`, `tax_rates`, `coa_accounts`, `posting_rules`, `draft_journals`, `posted_journals`, `journal_lines`, `statement_imports`, `bank_transactions`, `payment_allocations`, `review_actions`, `export_jobs`, `audit_events`, `notifications`, `task_runs`, `customer_requests`, `plans`, `subscriptions`, `contracts`, `entitlements`, `usage_ledger`, `invoices_billing`, `renewal_events`.

**Multitenancy:** tenant IDs in all tenant data, row-level security with policies that apply within a transaction and are verified with cross-tenant negative tests; API authorization and RLS are complementary, not interchangeable. Unique business IDs scoped to tenant/entity/period as appropriate. Uploads use private paths and short-lived signed URLs only.

**Messaging:** webhooks server-side; signed validation, dedup message IDs, safe retry, backoff, avoid auto-sharing private invoices in unrestricted group chats; no client-side Telegram token or polling.

**No auto posting from LLM:** service account on AI worker may propose extraction or suggestions but does not have DB permissions to post finalized journals.

## 9. Privacy, trust, operational resilience
- Conduct CNDP process for Morocco Law 09-08: declaration/authorization according to data types and international transfer formalities where applicable; legal review of third-party AI processing and cross-border hosting.
- Data minimization and PII redaction where possible; customer consent, terms, transparent AI processing and retention; specific customer portability/deletion procedures consistent with retention requirements.
- MFA for staff, role-limited access, per-tenant isolation, SOC-style immutable audit logs, end-to-end TLS, at-rest encryption, database backups and periodic restore drills, secrets management, dependency scanning, malware checks, rate limits, incident response and disaster recovery exercises.
- Do not send all customer source documents to unapproved model providers; evaluate vendor data usage, location and retention contracts.
- Performance SLO proposals to validate: p95 internal navigation under 200ms on benchmark machine, async extraction with visible queue/progress, recoverable failures, uploads durable before ACK, UI optimistic only for reversible operations.
- Zero customer financial data in code repositories, agent memory, demo fixtures or logs. Use consented anonymized document packs.

## 10. Differentiation: six testable advantages
1. **Evidence-linked review:** click a field and see exactly where it came from; a reviewer can correct it without leaving the keyboard.
2. **Exception-first queues:** accountants review only uncertainty and financially meaningful differences; measurable accuracy and time saved.
3. **Versioned Moroccan tax provenance:** each decision includes legal rule version, effective date, and human reviewer decision; never silently recalculate past filed months using new rules.
4. **Bank proof, not just bank matching:** running balance, page integrity, partials, N:M matching, trace from transaction to invoice and proof of payment.
5. **Closing cockpit:** close-ready state and a list of unresolved blockers (missing docs, mismatch, unapproved taxes) across all client entities.
6. **Interoperability and customer ownership:** standards-based exports, repeatable mapping, audit trail and reversible exit; do not force customers to abandon Sage/JBS/Odoo.

## 11. Benchmark dataset and go/no-go criteria
Prepare 150–300 **consented/anonymized** real Moroccan items across: clear scans; blurry/rotated phone photos; scanned vs digital PDF; double-page invoices; discounts/debours; multiple lines and historical VAT; credit notes; invoices with multiple payment terms; cash and compensation; foreign currency; no ICE; fake duplicates; supplier multipurpose items; 4+ Moroccan bank statement layouts; payment 1:N/N:M; partial payments; cash RAS and tax exceptions.

Suggested **pilot acceptance gates** (targets, not achieved results):
- 100% of posted journal entries balanced to the centime; 0 auto-posts on blocked document states.
- 100% cross-tenant forbidden-access tests blocked.
- Every edited/extracted tax-sensitive field has source and audit trail; 0 edits invisible in approved history.
- Under 1% undetected critical errors on validation pack *before* expanding automation, with stricter gate (zero known critical errors) for a release candidate.
- Extract 95%+ of required fields accurately on clearly legible pilot docs, independently evaluated; separately report quality by layout and bank.
- 100% current EDI golden examples pass local checks **and a real authorized upload acceptance trial**, before any 'DGI-ready' claim.
- Median human review time materially improves vs manual baseline on same pack (pilot benchmark, e.g. 30% faster). Marketing claims require evidence.
- Rehearsed restore from backup and simulated provider outage; no silent document loss.

**Metrics**: cost per page, per-document AI error rate by type, extraction queue latency, reviewer minutes/document, manual overrides, percentage auto-detected duplicates, reconciliation matched value and false positives, number of rejected EDI files, app uptime, client retention, time-to-first-value.

## 12. Commercial and deployment model — Cloud-first, one-time start + annual services
**User-preferred commercial direction (decided for design, not yet validated in market):** Sell to Moroccan accountants, fiduciaires and accounting firms with a first-year acquisition/onboarding package and recurring **annual service/maintenance/hosting/support renewal**. This replaces the prior monthly-first model. See `docs/COMMERCIAL_MODEL.md`, `docs/DEPLOYMENT_STRATEGY.md` and `docs/LICENSING_AND_ENTITLEMENTS.md` for the controlling details.

**Critical contractual distinction:** The cloud product is a *term-limited hosted service* with first-year entry/setup fees, **not** a perpetual installed software licence. If the future local/on-premise edition is sold as a perpetual licence, the contract must expressly specify which core offline functions continue after maintenance expiry; cloud AI/support/security updates can be separate renewals.

### Provisional price positioning — NOT published or approved offers
| Tier | First year, indicative HT | Renewal from year 2, indicative HT/year | Initial entitlement hypotheses |
|---|---:|---:|---|
| Essential | 6,900 MAD | 2,900 MAD | Up to 5 dossiers, 2 staff users, capped AI credits |
| Cabinet Pro | 12,900 MAD | 6,900 MAD | Up to 30 dossiers, 5 staff users, larger capped AI credits |
| Enterprise | Quote | Quote | Custom dossiers, volume, support SLA, optional dedicated future deployment |

The figures are **commercial testing hypotheses**, not validated margins. Calculate model/API cost per document/page, storage, backups, infrastructure, support load, payment fees, taxes and customer acquisition before pricing. No unlimited-AI promise. Pay-as-you-go document overage or prepaid AI packs require transparent consent.

### Renewal and data ownership
- Contract and invoice clearly separate upfront configuration/onboarding from annual managed access/maintenance as applicable; define initial 12-month service term and renewal dates.
- Entitlements are enforced **server-side**; the UI is not a licensing authority. Disputes and payment failures must not silently erase or corrupt financial records.
- Proposed non-renewal flow for legal/product review: notify well ahead of expiry; after expiry, disable new processing after a short clearly stated grace period, permit **read-only and export access for a documented transition window**; provide secure full customer export without punitive fees; handle retained records/deletion per legal obligations and contract. No indefinite free hosting is promised.
- Data controller/processor roles, retention, exit export format, data recovery, incident handling, availability and backup restore commitments must be included in signed terms.

### Deployment strategy
**Phase 1:** Cloud SaaS on verified domain, with secure server/API, encrypted database/object storage, segregated tenants and centralized model gateway. **Phase 2 only if buyers and cost justify it:** deploy the same modular business core in a customer's own environment with separate licensing, patching, backup and support commitments. Hybrid *readiness* is an architectural goal, not a commitment to offline sync at launch.

### Positioning and sales
- First market: accounting firms/fiduciaires rather than broad consumer invoicing.
- Sell speed of review, evidence provenance, reliable exports and auditability with documented pilot outcomes; vendor websites are not proof that HISAB-AI wins.
- Start with accountant demos and 3–5 limited-scope pilots. Use a consistent anonymized corpus and measure cost per page, review time, onboarding, renewal interest, and support cost.

## 13. Roadmap, ordered by evidence and risk rather than arbitrary calendar promises
**Gate 0 — Discovery/regulatory validation:** confirm actual accountant workflow, legal mapping, name clearance and pilot corpus, security/data flow; validate cloud hosting cost and annual renewal pricing; pick 1 pilot accountant and 1 standardized accounting export target.
**Gate 1 — Durable cloud foundation:** Git monorepo, AGENTS and docs, authentication, tenants, permissions, PostgreSQL, file storage, audit logging, secure AI gateway, entitlement skeleton, tested backups, staging, test and CI.
**Gate 2 — High-confidence invoice loop:** ingestion, extraction, source-linked review, validation, draft journals and reviewer approval, CSV/XLS export; prove accuracy and time advantage.
**Gate 3 — Bank and payment evidence:** 2–3 verified formats, source-backed reconciliation, N:M and partial matches, rules for reconciliation workflows.
**Gate 4 — Morocco tax pack:** formally signed versioned VAT/RAS rules, DGI XML pilot against actual official specs, tax reviewer UI, historic-rule tests.
**Gate 5 — Collaboration & closing:** authorized messaging, client missing-piece requests, deadline radar, closing cockpit.
**Gate 6 — Scale/advanced:** more banks, tailored agent with read-only evidence-grounded explanations, white-label options, optional integrations and analytics.

At every gate: demonstrable functional slice, architecture review, security checks, tests, customer feedback, rollback plan. No jumping ahead due to an AI-generated mega-prompt.

## 14. Open decisions/questions requiring evidence
1. Launch buyer: professional accounting firms or individual SMEs? Recommendation: cabinet-first.
2. Real target pilot bank statement examples / consent for anonymization.
3. One export target for the first pilot (Sage/JBS/etc) with a known import spec.
4. Hosting/data locality, managed annual services and which AI processing contracts make CNDP processes feasible.
5. Exact legally qualified RAS/tax tables and filing deadlines for 2026, incl transitional cases, validated by professional.
6. Trademark clearance / final name and domain availability.
7. WhatsApp official API access and documented permissions.
8. Whether posted journals are the system of record or just preparatory exports. Recommendation for phase 1: pre-accounting proposals, **not** a replacement for production ERP.
9. Validate proposed initial and renewal fees against detailed cost model and first 3–5 paying pilots; confirm VAT and contractual wording with Moroccan advisers.
10. Define exact post-expiry grace, export and legally mandated retention periods in customer terms.
11. Local edition: defer irreversible perpetual-licence/offline-sync promises until on-premise demand and cost of support are verified.

## 15. Documented source list (accessed/reviewed 2026-10-18)
- Moroccan Ministry of Economy and Finance, CGI 2026: https://www.finances.gov.ma/Publication/dgi/2025/CGI-2026-FR.pdf
- Moroccan government's explanation of staged 7/10/14/20 -> 10/20 VAT reform: https://alhoukouma.gov.ma/ (government publication about 2024–2026 VAT transition; search title if permalink changes)
- DGI/Ministry notice RAS VAT (2024, verify current 2026 rule): https://www.finances.gov.ma/fr/pages/detail-actualite.aspx?fiche=6947
- MEF law 69-21 legal texts: https://www.finances.gov.ma/fr/Pages/textes-juridiques.aspx
- Ministry 2026 declarations/timing: https://www.maroc.ma/fr/actualites/declarations-fiscales-annuelles-le-1er-avril-2026-dernier-delai-pour-plusieurs-categories-de
- CNDP conditions and international transfers: https://www.cndp.ma/conditions/ ; https://www.cndp.ma/procedures-de-notification-process/
- Google's Gemini key security: https://ai.google.dev/gemini-api/docs/api-key
- Verified vendor site claims: https://experio.ma/services/pre-comptabilite-automatique/ ; https://claris.ma/solutions/comptabilite/ ; https://fawatirai.com/fr ; https://sahlcompta.ma/features ; https://hisab.ma/fr
- Third-party cross-check (not DGI primary authority) for 2026 SIMPL XML specs: https://xmlsimpl.ma/specifications

**Source-hierarchy rule:** primary legislation/official DGI cahiers > official regulatory announcements > sector standards > professional expert sign-off > vendor commentary. If claims conflict, mark `LEGAL_REVIEW_REQUIRED`, do not silently prefer a blog or a model response.
