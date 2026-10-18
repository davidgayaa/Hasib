# AI Development Protocol — HISAB-AI

## Roles and mandatory two-agent review gate
- **Gemini = Implementer**: modifies code, tests, and developer portion of task file on a task branch. Can report `READY_FOR_QA` but never QA_PASS or DONE. Never touch `docs/TASKS_DONE.md` or `docs/qa/` final review records.
- **ChatGPT = Architect + Independent QA**: writes task requirements and audits exact PR commit with independent evidence; produces numbered review file, PASS / CHANGES_REQUESTED / NEEDS_EVIDENCE. No approval from developer narrative alone.
- **Project owner = final release/merge authority**: explicitly approves exact QA-reviewed commit/PR, merges, and records DONE in `docs/TASKS_DONE.md` after merge. QA PASS without merge is not DONE.
- **Always follow** `docs/QA_PROTOCOL.md` and `docs/GITHUB_QA_SETUP.md`. Review on the exact SHA; any subsequent implementation commit requires re-review. Never overwrite prior failed reviews. `CI PASS != QA PASS != DONE`.

## Architect memory / independent-audit checkpoint (process V2.4)
- Read `docs/CHATGPT_ARCHITECT_MEMORY.md` **first** at every new agent session. This is the short auditor-owned checkpoint and one-next-action summary; cross-verify every entry against live code, Git, tests and QA reports.
- Gemini can read this file, but **must not edit it**. Only ChatGPT QA (archived by owner/authorized reviewer) may propose/update it after independently reviewing evidence, including FAIL and NEEDS_EVIDENCE cases.
- `docs/SESSION_HANDOFF.md` is the operational developer handoff, not an independent QA certificate. `docs/CHATGPT_ARCHITECT_MEMORY.md` is the reviewer checkpoint, not a replacement for the Git/source-of-truth or `docs/TASKS_DONE.md`.
- If the owner cannot grant repository write permissions, ChatGPT delivers the updated file and explicitly leaves it uncommitted until the owner imports it.

## Mandatory session boot
1. Read `docs/CHATGPT_ARCHITECT_MEMORY.md`, `README.md`, `START_HERE.md`, `docs/ROADMAP.md`, `docs/STATUS.md`, `docs/SESSION_HANDOFF.md`, and the task's `docs/tasks/TASK-*.md`.
2. Read relevant `docs/ARCHITECTURE.md`, `docs/DECISIONS.md`, `docs/LEGAL_RULES_REGISTER.md` as needed. For deployment, pricing, billing or customer access, ALWAYS read `docs/COMMERCIAL_MODEL.md`, `docs/DEPLOYMENT_STRATEGY.md` and `docs/LICENSING_AND_ENTITLEMENTS.md`.
3. Inspect `git status`, current branch, recent commits, code, schema, tests and deployment configuration. **Do not infer code exists merely because docs say so.**
4. Restate task scope, current ground truth, required dependencies and acceptance criteria, then implement smallest safe change.

## Implementation guardrails
- Protect all tenant data server-side with RBAC + database tenant isolation; tests must cover cross-tenant denies.
- Never store secret keys, real customer invoices, passwords, tokens or tax identifiers in Git, agent task files or test fixtures.
- No AI-produced text or numbers may directly post a journal entry or file a tax declaration.
- Source original documents and financial facts in immutable evidence; document every override with who/when/why.
- Never invent law, supplier registries, DGI endpoints, XSD formats, integration coverage or test results.
- Use centime integers for posted money; Decimal/fixed-point intermediates for pricing/FX; use versioned rounding and tax rules.
- No unchecked browser direct model-key or Telegram bot-token usage.
- Launch product is **cloud-first managed service**, initial package + annual renewal; do not invent monthly-only subscriptions or call cloud access a perpetual licence.
- Renewal/entitlement rules must be server-enforced, idempotent and auditable. Never delete financial records because a contract expires; keep lawful customer export / transition access.
- Do not commit to local/offline/automatic bidirectional sync in MVP. Treat it as a separately costed, tested future product.
- Keep a clear migration/rollback plan for DB/schema/API changes.
- For all published factual finance/tax claims, cite validated law/regulatory version, mark unverified cases for qualified review.

## Developer handoff (NOT done)
Gemini must update task Developer Report with exact change paths, real test commands/logs, PR URL, SHA, risks and failures; set READY_FOR_QA only when evidence exists. ChatGPT/owner independently maintain numbered QA reviews.

## Definition of done
1. Change set implements scoped acceptance criteria.
2. Appropriate automated tests pass **and test command/output noted**; security and tenant isolation checks for affected operations.
3. ChatGPT reviewer verifies behavior and acceptance criteria at the **exact commit SHA**; report PASS; owner explicitly approves that reviewed SHA and merges with required CI.
4. **Only after merge**, owner updates `docs/TASKS_DONE.md` and `docs/STATUS.md` and `docs/SESSION_HANDOFF.md` and archives the new `docs/CHATGPT_ARCHITECT_MEMORY.md` reviewer checkpoint to reflect facts; update `docs/ROADMAP.md` milestones only with supporting test/evidence; update architecture or decisions if changed.
5. Update task file: paths touched, observed outputs, test results, risks, remaining work and next step.
6. Prepare atomic commit with meaningful message; **do not claim commit or deployment unless actually executed and verified**.

## On task failure
Record blocker, reproducible error, attempted commands, current files and rollback state. Failed independent QA is `CHANGES_REQUESTED` in numbered `docs/qa/` review, not a DONE entry. Technical inability to proceed is `BLOCKED`.

## Prohibitions
- Don't silently rewrite historic tax calculations when rules change.
- Don't auto-approve uncertain invoices just because total HT + TVA equals TTC.
- Don't auto-delete duplicates; retain evidence and explanatory flag.
- Don't overwrite posted journal entries. Create signed reversals/adjustments.
- Don't expose private docs to model providers without signed data-processing basis and security decision.
