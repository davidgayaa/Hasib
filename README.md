# HISAB-AI V2.4 Architect Memory + Dual-AI QA Process — product specification V2.1
**Working title; trademark clearance pending.** Moroccan accountant-first, evidence-first pre-accounting platform. **Go-to-market decision:** Cloud-first managed app sold with first-year entry/onboarding package + annual service/maintenance renewals; optional separately licensed local edition later.

## Start here
1. Start with `START_HERE.md` and **`docs/CHATGPT_ARCHITECT_MEMORY.md`**. Read `AGENTS.md`, `docs/ROADMAP.md`, `docs/STATUS.md`, `docs/SESSION_HANDOFF.md`, and relevant sections of `docs/ARCHITECTURE.md` before a task.
2. `MASTER_BLUEPRINT_V2.md` is the provisional product specification, **not binding legal authority**. For all pricing/deployment/renewal work, also read `docs/COMMERCIAL_MODEL.md`, `docs/DEPLOYMENT_STRATEGY.md`, and `docs/LICENSING_AND_ENTITLEMENTS.md`.
3. Every task needs a specific `docs/tasks/TASK-xxx-*.md`, verifiable acceptance criteria and tests.
4. Never implement automatic tax posting or filing without versioned rules plus professional sign-off.
5. Actual code, DB migration history and Git are the source of truth; docs summarize and must be updated afterward.

## Current state
Design-only. No app, repository, infrastructure, business integrations, or tests have been built or executed by this kit. See `docs/STATUS.md`.

## Deliverables in this kit
- `MASTER_BLUEPRINT_V2.md`: product, competitive, security, legal, architecture, business and roadmap.
- `AGENTS.md`: repeatable AI coding workflow and guardrails.
- `docs/ARCHITECTURE.md`: target bounded contexts and data flow.
- `docs/STATUS.md`: status and next actions.
- `docs/CHATGPT_ARCHITECT_MEMORY.md`: reviewer-owned quick resume — last audit, exact SHA, QA verdict, open failures, next action.
- `docs/DECISIONS.md`: proposed architecture decisions and pending approvals.
- `docs/LEGAL_RULES_REGISTER.md`: regulatory risks, rule version template.
- `docs/TEST_MATRIX.md`: acceptance controls.
- `docs/COMMERCIAL_MODEL.md`: pricing and annual renewal hypotheses, customer sales.
- `docs/DEPLOYMENT_STRATEGY.md`: managed cloud MVP and optional future local deployment.
- `docs/LICENSING_AND_ENTITLEMENTS.md`: subscription, access, quotas and customer data exit.
- `CHANGELOG.md`: change history for blueprint and memory files.
- `docs/tasks/TASK-001-foundation.md`: first implementation task template.

## Session continuity
At each new conversation, use the ready-to-copy prompt in `START_HERE.md`. Update `docs/SESSION_HANDOFF.md` at the end of every coding task, with real Git and test evidence. Do not rely on assistant chat memory alone.

## Development governance — Process V2.3
The product specification and commercial decisions remain V2.1. The **development process** is V2.3: Gemini implements, ChatGPT independently audits, and the owner approves merged work. Follow `docs/QA_PROTOCOL.md`; only owner-accepted, merged tasks appear in `docs/TASKS_DONE.md`. Historical reviews live in `docs/qa/`. GitHub PR branch policies are documented in `docs/GITHUB_QA_SETUP.md`.
