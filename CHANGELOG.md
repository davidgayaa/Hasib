# Blueprint revision history

## 2.1 — 2026-10-18
- Retained proposed accounting, AI and tax safety principles from V2.
- Changed intended commercial model from monthly-first SaaS to **first-year acquisition/onboarding + annual hosted service/maintenance renewal** in line with user decision.
- Declared **managed cloud first** and separately evaluated on-premise/local SKU later, rather than immediate hybrid/offline delivery.
- Added initial unvalidated pricing hypotheses: Essential 6,900 / 2,900 MAD per first/following year; Cabinet Pro 12,900 / 6,900 MAD, all HT pending validation.
- Added docs for commercial model, deployment, entitlement/quota lifecycle and data portability/non-renewal rules.
- Updated ADRs, agents, status, test matrix, initial task and master blueprint to avoid contradictions.
- No code, infrastructure, purchase, legal review or external market tests were performed in this update.

## 2.0 — 2026-10-18
- Created secure, evidence-first accounting product concept and memory scaffold from the uploaded V1 blueprint.

## 2026-10-18 — V2.2 startup workflow (no product feature change)
- Added START_HERE.md, docs/ROADMAP.md and docs/SESSION_HANDOFF.md.
- Updated README, AGENTS and STATUS to require session boot, task evidence and milestone review.
- Product specification remains V2.1; no repository, code, tests or deployment completed.

## 2026-10-18 — V2.3 independent QA/task ledger governance
- Formalized Gemini implementer vs ChatGPT architect/QA auditor vs owner final approval roles.
- Introduced `docs/QA_PROTOCOL.md` lifecycle with immutable numbered QA reviews and SHA-scoped pass.
- Introduced owner-controlled `docs/TASKS_DONE.md`: only QA-passed, explicitly approved, merged tasks.
- Added QA/task templates, GitHub setup notes, starter documentation-consistency CI and validator.
- Updated session continuity/task/startup instructions, roadmap, status and first task to avoid premature DONE claims.
- No application code, production CI tests, repository branch permissions or hosted infrastructure were implemented.

## 2026-10-18 — V2.4 ChatGPT architect continuity (no product feature change)
- Added `docs/CHATGPT_ARCHITECT_MEMORY.md`: concise checkpoint with confirmed last QA verdict, exact reviewed SHA, open findings/blockers, verified DONE tasks, decisions and one next action.
- Clarified separation: Gemini updates task Developer Report and session handoff; ChatGPT independently audits and proposes architect memory updates; owner archives protected QA/memory records and authorizes merge/DONE.
- Updated boot instructions, architecture continuity, QA and GitHub gate docs; developer `task/` PR checks now reject edits to the architect memory file.
- Product specification remains V2.1. No repository/code/deployment/test/approval has been carried out by this documentation revision.
