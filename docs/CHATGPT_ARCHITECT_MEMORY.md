# HISAB-AI — ChatGPT Architect & QA Memory (authoritative resume dashboard)

> **Process version:** V2.4 (2026-10-18) | **Product specification:** V2.1  
> **Maintainer:** ChatGPT independent Architect/QA, archived in Git by the project owner or an authorized independent reviewer.  
> **Developer:** Gemini — READ ONLY. Do not let Gemini edit this file, `docs/TASKS_DONE.md`, or approved `docs/qa/` review reports.  
> **Critical:** This file is an **index of independently reviewed state**, not proof by itself. Verify the linked Git commits, PRs, code, test logs and approval. ChatGPT does **not** automatically sync with Gemini or GitHub between chats.

## 0. Quick resume — read this first

| Field | Confirmed state as of 2026-10-18 |
|---|---|
| Project | HISAB-AI (temporary name; trademark/domain unconfirmed) |
| Target product | Moroccan accountant-/fiduciaire-first, evidence-first pre-accounting SaaS |
| Business model | Cloud-first managed app, initial onboarding/package payment + **annual** service/maintenance renewal; optional on-prem edition later |
| Current lifecycle | **DESIGN / NOT IMPLEMENTED** |
| Active milestone | **M1 — Foundation & Security** (NOT STARTED) |
| Active task | **TASK-001** — `docs/tasks/TASK-001-foundation.md` (PLANNED) |
| Last Gemini task with reviewed code | **NONE — no code delivered** |
| Last ChatGPT independent QA verdict | **NOT_REVIEWED** (no QA review exists) |
| Most recent QA report | **NONE** |
| Last independently verified source commit / PR | **NONE — repository not supplied** |
| Owner-approved and merged tasks | **NONE** — `docs/TASKS_DONE.md` has no task rows |
| Open failed QA findings | **NONE** (not the same as 'all tests passed') |
| Next action | **Owner creates/accesses private GitHub repository, imports V2.4 kit, configures permissions; then Gemini implements first bounded part of TASK-001 on a task branch.** |
| Current blockers | No verifiable repo/branch/CI; no code/tests; trademark and hosting/vendor/privacy/legal validation pending |

**No application, data service, production deployment, tax connector, licensing system or CI evidence is verified in this document kit.** A planning file or code generated in a chat is not a completed implementation task.

## 1. How ChatGPT must resume, every single session
1. Read **this file first**. Then read `AGENTS.md`, `docs/QA_PROTOCOL.md`, `docs/TASKS_DONE.md`, `docs/STATUS.md`, `docs/ROADMAP.md`, `docs/SESSION_HANDOFF.md`, `docs/DECISIONS.md` and the active `docs/tasks/TASK-*.md`.
2. Obtain the **live repository**, the actual PR/diff or current code ZIP, the exact commit SHA, and relevant test output. If not accessible, state `NOT VERIFIED` or `NEEDS_EVIDENCE` — never guess progress from this file.
3. Cross-check the latest QA reports in `docs/qa/`, recent commits and owner-approved merges against the DONE ledger. A previously valid QA PASS is bound to one exact reviewed commit; code changed after that requires re-review.
4. State in plain language: **what is verified done**, **what is underway**, **what failed / remains blocked**, **what is the one next task**, and **what evidence is missing**.
5. **As architect**, write/confirm requirements and acceptance criteria before Gemini codes. **As QA**, issue a numbered audit of exact candidate SHA. **As owner**, the user approves merge and completion; ChatGPT never silently approves on the owner's behalf.
6. At the end of an actual independent QA/architecture review, propose changes to this file and archive the updated version in Git **through owner/reviewer-controlled workflow**. Update `docs/STATUS.md` and, if relevant, `docs/SESSION_HANDOFF.md`. If Git write access is unavailable, deliver edited files and explicitly say they have **not** been committed.

## 2. Known decisions — do not change without an ADR and owner consent
- Gemini is **implementation developer**. ChatGPT is **independent architect/QA**. Project owner makes final acceptance/merge decisions.
- The **source of truth** is the current code + Git commits + verified tests + owner merge evidence. `TASKS_DONE.md` is the accepted-task index; this memory is the auditor-facing snapshot.
- Commercial direction: **managed cloud-first**, first-year acquisition/onboarding + annual renewals. A local edition is **not** in MVP.
- Security: server-side AI credentials; tenant isolation at API/DB; RBAC, audit trail; no real financial documents/secrets in repository.
- Accounting: deterministic centimes/fixed-precision, immutable source evidence, human approval, versioned Moroccan tax rules; legal/tax sign-off is separate from software QA.
- Tax and DGI integrations are **not legally or technically validated** merely because the blueprint describes them.
- Gemini can set `READY_FOR_QA` but cannot write `TASKS_DONE.md`, official QA reports, or this architect memory. SHA-scoped QA PASS + owner approval + merge + evidence are required for DONE.

## 3. Verification ledger — latest independent QA checkpoint

| Item | Value | Evidence link/path |
|---|---|---|
| Last task audited | NONE | — |
| Candidate PR | NONE | — |
| Reviewed commit SHA | NONE | — |
| QA verdict / date | NOT_REVIEWED / — | — |
| Findings requiring Gemini fixes | NONE (not reviewed yet) | — |
| Owner approval + merge | NONE | — |
| Last DONE ledger update | NONE | `docs/TASKS_DONE.md` |

When a review happens, replace **only this summary checkpoint** with verified facts and reference the numbered, retained QA file. Never delete/change the historical `docs/qa/TASK-xxx-review-NN.md` records. In a FAIL, set verdict `CHANGES_REQUESTED` and describe the exact smallest corrective action. For lack of evidence use `NEEDS_EVIDENCE`. For PASS, record exact SHA but **do not say DONE** until owner approves and the code is merged.

## 4. Current task & next action queue

**NOW: TASK-001 — secure foundation (PLANNED)**  
Scope: project Git/monorepo foundation, auth, tenant-isolated API + PostgreSQL, minimal UI, test strategy, secure secrets, CI and staging plan. No fiscal automation, no real financial uploads and no live payment collection. See task acceptance criteria.

**Next verifiable action (only one):** Owner provides a **private GitHub repository URL or the current repo ZIP** and enables reviewable PRs. Then inspect files/branch and ask Gemini for the first TASK-001 implementation commit with real test evidence.

**Future, dependent on QA-approved milestones:** M2 document workflow → M3 deterministic accounting → M4 bank matching → M5 versioned tax/exports → M6 pilot → M7 launch. Consult `docs/ROADMAP.md`, not this summary alone.

**Independent review blockers / external sign-offs:** trademark and brand; hosting location and vendor DPAs/privacy compliance; real Moroccan accounting fixtures with lawful processing basis; official tax/EDI schemas and accountant/legal validation; tested backup recovery and security controls; validated economics/pricing.

## 5. Auditor update procedure — after EVERY audit, PASS or FAIL
- Record date, task, candidate PR and **exact** reviewed SHA, evidence examined, verdict, numbered QA report link, high-severity open findings, next corrective action, owner decision and merge state.
- PASS: set `QA_PASSED` on that exact SHA; don't add to DONE until separately approved and merged.
- FAIL: keep the FAIL report, set `CHANGES_REQUESTED`, list fix/verification instructions for Gemini. Re-audit the **new** SHA as a new review file.
- Missing logs/repo: `NEEDS_EVIDENCE`; say what is missing. Don't invent results or turn it into a FAIL without evidence of a defect.
- After owner-confirmed merge: reconcile `docs/TASKS_DONE.md`, `docs/STATUS.md` and roadmap; cite approved QA report and merged PR/commit. If not independently verifiable, keep `NOT VERIFIED`.
- Preserve **decisions** here but put detailed chronological failures in numbered QA reports, and temporary implementation notes in `docs/SESSION_HANDOFF.md`.
- Update this file only via owner/reviewer-controlled change; Gemini may suggest factual corrections in its developer task report, but must not edit this record.

## 6. Copy/paste message to resume ChatGPT in a new conversation

> Continue HISAB-AI as **Architect + Independent QA**, not as code developer. Gemini implements. Read `docs/CHATGPT_ARCHITECT_MEMORY.md` first, then `AGENTS.md`, `docs/QA_PROTOCOL.md`, `docs/TASKS_DONE.md`, `docs/STATUS.md`, `docs/ROADMAP.md`, `docs/SESSION_HANDOFF.md` and active task. Independently verify Git/PR/SHA/tests and existing QA reports. Tell me what is actually DONE, what is blocked or failed, and the exact next action. Audit Gemini at the exact SHA. Do not mark QA PASS without evidence and do not mark DONE without owner-approved merge. Propose an updated `CHATGPT_ARCHITECT_MEMORY.md` after your audit. If repo access is absent, say what is not verified and request current code/evidence.

## 7. Maintenance notes
- Keep this file **short and current**. If it grows, move historical details into timestamped QA reviews and ADRs; preserve pointers here.
- No confidential customer details, tokens, or credentials in this file.
- Last file-only initialization: **2026-10-18**. **No independently reviewed implementation exists at initialization.**
