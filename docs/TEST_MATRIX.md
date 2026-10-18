# QA and independent acceptance test matrix

| Test family | High-risk examples | Required evidence |
|---|---|---|
| Money | 0.1+0.2, quantity with 6 decimals, rate rounding, large balances, negative credit note | Golden-centime assertions, no float drift |
| Ledger | balanced vs misclassified entry, reversal, year lock, duplicate posting | Journal and audit event tests |
| Tax | historical 7/14; current 10/20; exemptions; RAS 75/100 applicability; prorata; cash/day/month | Signed versioned rules, scenario expected outputs |
| Extraction | mixed VAT invoice, two pages, 40-page multi-doc, low quality, overlapping fields | Per-field exact source coordinates, reviewer corrections |
| Bank | opening/closing, missing page, repeated txn, partial, 1:N, N:M, foreign currency | Per-statement integrity and manual review |
| Security | tenant A tries tenant B document ID, IDOR, malicious upload, token leak, XSS, unsafe exports | Isolation negative tests, security scan logs |
| Reliability | worker retry/duplicate event, provider outage, partial DB commit, restore | Idempotency & disaster-recovery report |
| Export | each target schema, special characters, DGI ZIP, success vs uploaded vs accepted states | Golden fixtures and acceptance evidence |
| UX | keyboard navigation, support RTL, reviewer flow, accessibility | Timed usability sessions, baseline delta |
| SaaS contracts | first-year fee vs renewal, expiry reminder, quota, successful annual renewal, unpaid dispute | Contract-version fixtures and entitlement integration tests |
| Access after expiry | paid extraction denied at expiry, permitted read-only/export window, full attachment export | Time-travel tests, independent customer export validation |
| Billing security | forged payment webhook, replay, tenant-crossing, price override, duplicated usage | Signed webhook validation, idempotency, RBAC and negative tests |
| Deployment | private API credentials, TLS, region/subprocessor review, environment split, backup restores | Threat model, config test logs, restore drill |

**Release guardrails:** 0 known critical uncaught financial errors; 0 unauthorized tenant access paths in tests; provenance + history for every sensitive edit; EDI acceptance claim backed by actual external response; backup-restoration drill; controller and privacy assessment.
