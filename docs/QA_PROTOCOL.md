# HISAB-AI — Dual-AI Task Approval Protocol (V2.3)

**Roles**: Owner = final acceptance and merge authority. ChatGPT = architect and independent QA reviewer. Gemini = coding implementer. GitHub repository, source code, commit history and actual test results = source of truth. Documents are summaries, not proof by themselves.

## Single official task lifecycle

`PLANNED -> IN_PROGRESS -> READY_FOR_QA -> QA_PASSED -> DONE`

On failed review: `READY_FOR_QA -> CHANGES_REQUESTED -> IN_PROGRESS -> READY_FOR_QA`. `BLOCKED` if technical access, legal approval, or required evidence is missing. `NEEDS_EVIDENCE` is not a pass.

### 1. Architect (ChatGPT)
- Define task ID, scope, dependencies, acceptance criteria, measurable tests, and applicable security/accounting/tax requirements in `docs/tasks/TASK-ID-slug.md`.
- Ensure the task is prioritized by `docs/ROADMAP.md` and does not contradict architecture/business decisions.

### 2. Developer (Gemini)
- Work only on a task branch `task/TASK-xxx-description`. Commit implementable code and task execution notes to the branch.
- Before requesting review, update the active task file's **Developer Report**: exact change paths, commit SHA and PR link, test commands and captured results, risks, blockers, deviation requests, and known failures.
- Set development state `READY_FOR_QA` only when evidence is available. Otherwise mark `IN_PROGRESS` or `BLOCKED`. Do **not** add to `docs/TASKS_DONE.md`, set QA result, impersonate QA, or alter `docs/qa/` official reviews.
- `CI PASS` means checks passed; it NEVER means `QA PASS` or `DONE`.

### 3. Independent QA (ChatGPT)
- Verify exact PR diff, relevant source code, tests, expected behavior, security implications, tenant isolation, database migrations and architecture compliance. Review QA claims independently. If unavailable, record `NEEDS_EVIDENCE`, not PASS.
- Create a **new** immutable historical review file: `docs/qa/TASK-xxx-review-01.md`, then `-02.md`, etc. Never overwrite earlier reviews.
- Record **reviewed exact commit SHA**, PR, artifacts examined, test evidence, acceptance-criterion verdicts, risk severity and disposition: `PASS`, `CHANGES_REQUESTED`, or `NEEDS_EVIDENCE`.
- A `PASS` is valid **only** for the reviewed SHA. Any change to implementation after this SHA requires another QA review. The owner must archive the QA report in Git independently of the developer.

### 4. Owner gate
- The user verifies the QA PASS recommendation and gives explicit approval to merge the exact reviewed PR/commit. ChatGPT does not silently grant merge permission.
- Merge only after required CI and applicable checks, and no new unreviewed commits; follow supported GitHub branch protection / owner review controls.
- After the approved code is merged on `main`, **owner-controlled** follow-up change records the task in `docs/TASKS_DONE.md`, with approved QA file, reviewed commit SHA, merge PR and date. Update `docs/STATUS.md`, `docs/SESSION_HANDOFF.md` and roadmap gate accordingly.
- A task with QA PASS but not merged is `QA_PASSED`, **not** `DONE`.

## Three complementary records (no duplicate truth)
1. **Task file** `docs/tasks/TASK-ID-*.md`: original requirements and developer execution evidence; open work can stay here indefinitely.
2. **QA reviews** `docs/qa/TASK-ID-review-NN.md`: append-only historical findings and decisions. A failed review NEVER goes in done ledger.
3. **Completion ledger** `docs/TASKS_DONE.md`: only owner-approved, merged tasks. This is an index, not a substitute for reviewing source code.

`docs/STATUS.md` answers "what is active/blocked today?". `docs/ROADMAP.md` answers "which milestone is next?". `docs/SESSION_HANDOFF.md` answers "how do I resume the last work?". They must not declare a feature completed from Gemini's narrative alone.

## Concrete example
- Gemini sends TASK-001 PR at SHA `aaaaaaa`; tests provided, state READY_FOR_QA.
- Reviewer finds missing tenant isolation test; creates `TASK-001-review-01.md`, `CHANGES_REQUESTED`.
- Gemini fixes issue in new commit SHA `bbbbbbb`; sends revised PR; previous FAIL stays on record.
- Reviewer checks SHA `bbbbbbb`, creates `TASK-001-review-02.md`, PASS.
- Owner approves and merges that exact commit. Only then add TASK-001 to `docs/TASKS_DONE.md`.

## Anti-cheating / access requirements
- **Text prompts alone cannot enforce permissions.** Do not give Gemini unrestricted access to the protected `main` branch or owner-only records.
- Use protected `main`, required status checks, owner-controlled merges, and CODEOWNERS for QA and done ledger when supported by the repository plan. Treat GitHub permissions as real controls and `AGENTS.md` as procedural guidance.
- Task PR checks included in this kit reject edits to `docs/TASKS_DONE.md` and `docs/qa/` under a `task/` branch. This is a supporting safeguard, not a security boundary; owner must review configuration/CI changes.
- Do not mark fiscal rules legally approved merely from software QA. Regulatory sign-off remains a separate mandatory step where applicable.

## V2.4 — architect-owned memory sync
- `docs/CHATGPT_ARCHITECT_MEMORY.md` is an **independent reviewer snapshot** maintained after every QA verdict (including `CHANGES_REQUESTED` and `NEEDS_EVIDENCE`), with exact candidate SHA/PR, latest numbered QA report and one next action.
- Gemini may read it, but may not modify it in developer PRs. Owner or authorized independent reviewer commits ChatGPT's checkpoint separately.
- No change to ledger gate: only independently passed, owner-approved, merged tasks enter `docs/TASKS_DONE.md`. The snapshot is **not** proof of PASS, merge or task completion.
- If an old snapshot conflicts with the repo, QA report or merge history, mark it STALE / NOT VERIFIED and correct through authorized owner/reviewer review. Never invent project state from this file.
