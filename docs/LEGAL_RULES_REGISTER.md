# Legal and fiscal rule register — NOT IMPLEMENTATION AUTHORITY

Use this registry before coding, and require professional validation against CGI 2026 and relevant regulations; keep historical effective periods.

## Per-rule metadata
```yaml
rule_id: TVA_RATE_CATEGORY_SAMPLE
status: NEEDS_PROFESSIONAL_REVIEW
jurisdiction: MA
legal_basis: "CGI 2026 art. 99 (confirm exact clause for scenario)"
effective_from: YYYY-MM-DD
effective_to: null
payer_class: to_define
seller_class: to_define
activity_class: to_define
payment_event: to_define
rate_or_method: to_define
exceptions: []
rounding_method: to_define
source_document_sha256: to_define
reviewed_by: null
reviewed_at: null
tests: []
```

## Blocking legal work items
1. 2026 and historical TVA (10%/20% current positive standard classes; 7%/14% historical handling, exemptions) — CGI art. 99, 91, 92 and amendments.
2. Deductibility/payment modes, prorata, cash day+supplier/month thresholds and exceptions — CGI relevant articles (including 95, 104–106; revalidate).
3. Timbre 0.25% conditionality/exemptions — CGI art. 252.
4. RAS TVA based on payor/payee, equipment/works vs services, certificate and effective date — CGI art. 117-IV/V and DGI guidance.
5. Separate RAS IS/IR withholding families; foreign and rental mechanisms if in product scope.
6. Law 69-21 applicability, bill dates, thresholds, formula and cadence; regular DGI updates.
7. DGI Simpl-TVA file structure; no assumption of XSD; version by declaration.
8. e-invoice readiness, not unsupported claim of mandatory 2026 universal rollout.
9. CNDP 09-08 classification, contractor processing and cross-border transfer if relevant.

**Blocking rule:** any tax-sensitive action without signed rule_version and applicable evidence must remain `NEEDS_REVIEW`.
