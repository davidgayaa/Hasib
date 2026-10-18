# Template — ChatGPT independent QA memory update

This is an instruction/template, not an independent audit record. Read `docs/CHATGPT_ARCHITECT_MEMORY.md` for the **current** snapshot.

After **each** ChatGPT audit (PASS / CHANGES_REQUESTED / NEEDS_EVIDENCE), owner/reviewer updates the architect memory fields:
1. Last reviewed task + PR URL and **exact candidate SHA** (never use an unverified SHA).
2. Numbered immutable `docs/qa/TASK-xxx-review-NN.md` file, verdict, date, failing criteria and evidence checked.
3. Task lifecycle: READY_FOR_QA / QA_PASSED / CHANGES_REQUESTED / BLOCKED / DONE; do not call DONE until owner-approved merge and ledger update.
4. High-severity open issues and precise corrective instructions for Gemini.
5. Last owner-approved merged task(s) cross-checked with `docs/TASKS_DONE.md` and Git.
6. **Exactly one** smallest next action, owner/developer/reviewer responsible and evidence needed to unlock it.
7. Any unverified facts written explicitly as `NOT VERIFIED`; don't hide them behind confident language.
8. Keep long histories only in QA review files and ADRs; this is a *current* dashboard.

Important: Gemini may **read**, never edit, architect memory. Archiving by Git is a separate, verifiable action performed by owner/authorized reviewer, not automatically by ChatGPT. Do not store client financial records, API keys or private identifiers.
