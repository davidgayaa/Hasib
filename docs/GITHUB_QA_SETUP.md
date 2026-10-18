# GitHub setup — practical independent QA gate

1. Create one private repo and configure a protected default branch `main`. **Never let Gemini push directly to main.** Give Gemini a working branch and least-privilege credentials only, when applicable.
2. Require PRs for `main` and require the validation checks available under your GitHub plan. Owner alone authorizes merges. Turn on review requirements and CODEOWNERS for protected paths if supported. Some protections depend on GitHub plan/repository settings; verify your account.
3. Keep `docs/TASKS_DONE.md` and `docs/qa/**` under owner/reviewer control. Developer PRs use prefix `task/TASK-xxx-*`; CI rejects protected record edits from those branches. Never accept CI workflow/script changes in the same implementation PR without manual owner security review.
4. Gemini commits code and its task-specific **Developer Report**. Gemini opens PR. ChatGPT verifies exact candidate commit and produces a QA review. Owner uploads and commits QA report separately from developer work.
5. After QA PASS, owner approves reviewed SHA and merges unchanged PR. Owner separately updates the DONE ledger and status. Any post-review implementation change -> fresh review.
6. Keep real CI logs and commits in GitHub. This kit's lightweight validator checks documentation consistency only: it does not run product tests, verify cloud configuration, or prove a reviewer is independent.
7. Run `python scripts/validate_task_ledger.py` locally. The included workflow runs it on commits/PRs; repo admins must independently configure protected branch and status checks.

**Warning:** If Gemini has full admin access or uses the same unrestricted GitHub credentials as the owner, no text-file rule can truly prevent it from changing approval records. Permissions and human review are essential.

## V2.4 — protect the architect checkpoint
- Add `docs/CHATGPT_ARCHITECT_MEMORY.md` to CODEOWNERS / owner-reviewed paths where supported, together with `docs/qa/**` and `docs/TASKS_DONE.md`.
- This kit's CI rejects `task/` branch PRs touching any of these paths, but only GitHub permissions and required reviews can provide effective enforcement. An unrestricted admin token defeats text rules.
- Owner/reviewer separately imports ChatGPT's checkpoint update after the audit; Gemini's implementation branch must not write reviewer verdict or next-action ground truth.
