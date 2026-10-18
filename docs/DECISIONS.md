# Architecture Decision Records (ADRs)

| ID | Decision | Status | Reason |
|---|---|---|---|
| ADR-001 | Target accounting firms first; pre-accounting rather than a complete ERP in MVP | Proposed | Higher frequency of repeated work and clear high-value workflow |
| ADR-002 | PostgreSQL centrally from the first working pilot | Proposed | Client-only IndexedDB cannot safely act as authoritative multi-tenant ledger |
| ADR-003 | TypeScript monorepo; modular monolith API and background worker | Proposed | One primary stack, testable boundaries, minimal cross-service overhead |
| ADR-004 | Model extraction/suggestion only; deterministic finance engine; qualified human approval | Proposed | Safer material financial actions and auditable decisions |
| ADR-005 | Official connectors through backend; no browser Telegram long-polling or API tokens | Proposed | Protect credentials and preserve message processing reliability |
| ADR-006 | Current and historical tax rules versioned by effective date and source | Proposed | Avoid silent retroactive recalculation after law changes |
| ADR-007 | Internal working name HISAB-AI pending brand clearance | Proposed | Existing hisab.ma presents naming collision |
| ADR-008 | Prepare official EDI imports but don't claim direct DGI integration | Proposed | Acceptance depends on current specs and real authorized filings |

| ADR-009 | Launch managed Cloud SaaS on verified domain and secure hosted PostgreSQL + document storage; defer on-premise SKU | **Direction agreed 2026-10-18; vendor unchosen** | Lower per-customer support burden, secure centralized AI and automatic rule updates |
| ADR-010 | First-year package + annual managed service renewal for accounting practices, rather than monthly-only pricing | **Direction agreed 2026-10-18; prices provisional** | Matches desired Moroccan sales model and predictable yearly fees |
| ADR-011 | Do not market cloud service as perpetual purchase; future local licence to use separate legal contract | Proposed, needs legal sign-off | Avoid contractual mismatch between hosted recurring service and perpetual licence |
| ADR-012 | End-of-contract must preserve financial data, lawful retention and secure export transition | Proposed, needs terms/legal sign-off | Trust, privacy, portability and accounting evidence preservation |

### ADR template
`ID`, `date`, `problem`, `options`, `decision`, `consequences`, `reversal plan`, `evidence links`, `approver`.
