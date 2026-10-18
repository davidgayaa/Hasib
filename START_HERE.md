# HISAB-AI — START HERE / ابدأ من هنا

**Starter-process release:** V2.4 — 2026-10-18. The product specification is still V2.1. This is not an implemented application.

## One-time setup / أول مرة
1. Create a **private** GitHub repository, provisionally named `hisab-ai`, after confirming access and legal naming constraints. Do not publish project files or secrets publicly.
2. Extract this kit in the repo root. Preserve the `docs/` paths and task files. Keep `.env`, credentials and client financial documents out of Git.
3. Initialize Git, add an appropriate `.gitignore`, record the first commit and verify it exists. Never report a commit without checking it.
4. Use `docs/CHATGPT_ARCHITECT_MEMORY.md` as the **ChatGPT independent QA resume dashboard**, and `docs/ROADMAP.md` as milestone tracker, `docs/STATUS.md` as latest summary, `docs/SESSION_HANDOFF.md` as short-term handoff, and `docs/tasks/TASK-xxx-*.md` as task-specific evidence.
5. Start with `docs/tasks/TASK-001-foundation.md`. Do **not** start taxation integrations or real billing before safe tenant isolation and foundational tests.

## Each new conversation / كل محادثة جديدة
Send this message and attach or connect the current GitHub repository:

> We are continuing the HISAB-AI accounting project (cloud-first, accountants in Morocco, first-year onboarding package plus annual operating/maintenance renewal; optional future on-premise SKU). **Use the repository as the single source of truth.** Before touching code, read `docs/CHATGPT_ARCHITECT_MEMORY.md`, `AGENTS.md`, `README.md`, `docs/ROADMAP.md`, `docs/STATUS.md`, `docs/SESSION_HANDOFF.md`, `docs/DECISIONS.md` and the active task. Check Git status, recent commits, and current tests. Tell me what has actually been completed versus what is still planned, then work only on the next unblocked task. After implementing and testing, update the task log, `STATUS.md`, `SESSION_HANDOFF.md`, and `ROADMAP.md`; cite actual test output and Git commit. Do not claim execution or deployment without evidence. Do not change the scope, pricing model or architecture silently. If the repository is unavailable, ask for it and do not invent project state.

## Where to resume
- Milestone: **M1 Foundation & Security**, still not started.
- Active task: `docs/tasks/TASK-001-foundation.md`.
- Hosting vendor, domain and trademark are **not selected or purchased**.
- Product taxes, DGI integration and contractual details require validated sources and professional review.

## Minimal end-of-task checklist
- [ ] Check working tree and capture changed paths.
- [ ] Run relevant tests and record actual pass/fail with commands.
- [ ] Update the active task's evidence log and status.
- [ ] Update `docs/STATUS.md` and `docs/SESSION_HANDOFF.md`.
- [ ] Update `docs/ROADMAP.md` only when a checkpoint is truly verified.
- [ ] Update architecture/ADRs/rules if affected.
- [ ] Commit the verified change if possible; record the real hash. If no commit occurred, mark it clearly.

## V2.3 — exact two-agent protocol
- Active developer is **Gemini**. The independent architect/auditor is **ChatGPT**. Owner is the user.
- Read `docs/QA_PROTOCOL.md`, `docs/GITHUB_QA_SETUP.md`, `docs/TASKS_DONE.md` before claiming anything is completed.
- Gemini must hand over task branch, exact SHA, PR, files changed, and actual tests. It cannot mark QA PASS or write to completed-task ledger.
- ChatGPT issues numbered `docs/qa/TASK-xxx-review-NN.md` verdict based on evidence. If information unavailable, use `NEEDS_EVIDENCE`.
- Owner explicitly approves and merges reviewed SHA. **Only after merge** may a new row be added to `docs/TASKS_DONE.md`.
- QA PASS expires upon any new implementation commit; repeated review required. Old FAIL reports remain archived.
- Included `.github/workflows/task-ledger.yml` is a starter consistency check; GitHub branch protections and owner permissions must be configured separately.
