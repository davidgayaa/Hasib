# TASK-001-A — Monorepo, toolchain, CI and stack ADRs — Implementation Plan

**Developer state:** PLANNED (plan submitted for review; coding NOT authorized)
**Plan review:** Architect verdict 2026-10-18 = CONDITIONALLY ACCEPTED — NOT YET AUTHORIZED FOR CODING
**QA gate:** NOT_REVIEWED (no code exists for this task)
**Owner acceptance:** PENDING
**Milestone:** M1 — Foundation & Security (parent task: `docs/tasks/TASK-001-foundation.md`)
**Architect:** ChatGPT · **Implementer:** Gemini · **Final authority:** Project owner
**Base commit:** `e2fc408adfd49310e1eeb5fd459dfa77645995d9` (`main`, https://github.com/HamzaGhacham/Hasib)
**Plan branch (documentation only):** `task/TASK-001-A-plan`
**Implementation branch (only after authorization):** `task/TASK-001-A-monorepo-toolchain-ci`

> [!IMPORTANT]
> This file is a **plan**, not evidence of implementation, QA PASS or DONE. Merging this plan (if the owner chooses to) does not authorize coding; coding starts only after explicit architect + owner authorization. The project currently has **zero QA-approved coding tasks**.

---

## 0. Architect decisions applied (review of 2026-10-18)

| # | Decision | Effect on this plan |
|---|---|---|
| 1 | Node.js 24 LTS, pinned toolchain | §2 |
| 2 | **npm workspaces**, committed lockfile, reproducible `npm ci` | Replaces earlier pnpm proposal throughout |
| 3 | 001-A limited to monorepo foundation, toolchain, basic packages, tests, CI, setup docs | §1 scope / exclusions |
| 4 | Separate ADR files under `docs/adr/` | §3, §5 |
| 5 | ADR-014 (ORM) and ADR-015 (Auth) stay **PROPOSED** | §5 |
| 6 | Compare managed identity solutions with self-hosted authentication before choosing | §5.3 comparison matrix |
| 7 | Dedicated task branches and PRs | §8 |
| 8 | Never modify protected QA, Architect Memory or TASKS_DONE files | §3 "Never touched", AC-A12 |
| 9 | CI least-privilege, no production secrets | §4, AC-A07 |
| 10 | No TASK-001-B / database / auth implementation | §1 exclusions, AC-A14 |

## 1. Goal and scope

Establish a reproducible TypeScript monorepo foundation that later subtasks (001-B…E) build on:

1. Toolchain pinned to Node.js 24 LTS and its bundled npm; strict TypeScript, ESLint, Prettier, Vitest.
2. npm-workspaces skeleton with only the packages M1 needs (§3).
3. A **new** CI workflow (`ci.yml`) running clean install / format / lint / typecheck / test / dependency audit / secret scan on PRs and `main`.
4. ADRs: ADR-013 toolchain (decision for approval), ADR-014 ORM (PROPOSED), ADR-015 authentication (PROPOSED).
5. Reproducible clone → install → verify instructions, proven from a fresh clone.
6. Developer-side doc updates (`STATUS.md`, `SESSION_HANDOFF.md`, Developer Report) as authorized by the architect.

### Out of scope (explicitly excluded)
- NestJS, Fastify, React, Vite, BullMQ, PostgreSQL, Redis, Docker, any ORM or auth library installation → 001-B…D.
- Any auth, RBAC, RLS, migration, endpoint, UI, entitlement or tenant-data code → 001-B/C/D/E.
- Staging deployment / hosting (vendor not chosen; ADR-009) → staging *plan* in 001-E.
- Changes to `.github/workflows/task-ledger.yml`, `scripts/validate_task_ledger.py`, `scripts/check_architect_memory.py`.
- `CODEOWNERS` / branch protection — owner-controlled settings (recommendation in §9).

## 2. Toolchain (proposed in ADR-013)

| Concern | Choice | Evidence / reason |
|---|---|---|
| Node.js | **Node 24 LTS "Krypton"**, `.nvmrc` = `24`, `engines.node` = `>=24.0.0 <25`; reference version **v24.22.0** (released 2026-10-14) | Official schedule `nodejs/Release/schedule.json`, fetched 2026-10-18: v24 LTS since 2025-10-28, maintenance from 2026-10-20, **EOL 2028-04-30**. v26 becomes LTS only 2026-10-28; v22 EOL 2027-04-30. |
| Package manager | **npm workspaces** (architect decision #2), npm bundled with Node 24.22.0 = **11.19.1** (per `nodejs.org/dist/index.json`); `packageManager: "npm@11.19.1"`; `engines.npm` = `>=11 <12` | One tool shipped with Node; `npm ci` gives reproducible installs from `package-lock.json`. |
| Install policy | `.npmrc`: `engine-strict=true`, `save-exact=true`, `fund=false`; `package-lock.json` committed (lockfileVersion 3); CI uses `npm ci` only | Wrong Node major fails early; exact versions; no lockfile drift. |
| Workspace linking | Internal deps declared as `"@hisab/contracts": "*"` resolved from local workspace by npm | npm does not support the `workspace:` protocol. |
| Language | TypeScript `strict`, `noUncheckedIndexedAccess`, `exactOptionalPropertyTypes`, `noImplicitOverride`; `tsconfig.base.json` + project references; `tsc -b` | Maximum compile-time safety for a financial domain. |
| Lint | ESLint 9 flat config + `typescript-eslint` type-checked rules (`no-explicit-any`, `no-floating-promises`, `no-unsafe-*`) | |
| Format | Prettier (`--check` in CI) + `.editorconfig` + `.gitattributes` (`* text=auto eol=lf`) | Cross-platform deterministic diffs (Windows dev, Linux CI). |
| Tests | Vitest with root `vitest.config.ts` using `test.projects` (per-workspace), coverage via `@vitest/coverage-v8` | Same runner for later packages; matches blueprint §8. |
| Secret scan | gitleaks (full history) in CI | AC-A08. |
| Dependency audit | `npm audit --audit-level=high` | AC-A09. |
| Orchestration | Plain `npm run <script> --workspaces --if-present`; no Turborepo in 001-A | Smallest safe change. |

**Local machine:** currently Node v26.10.0 (not LTS). Node 24 LTS will be installed user-level via a version manager (proposed `fnm`; `nvm-windows` acceptable). No repository change. Node 26 migration = separate future task after its LTS date and ecosystem verification.

## 3. Proposed file list

### New files
```
.nvmrc
.npmrc
.editorconfig
.gitattributes
.prettierrc.json
.prettierignore
.gitleaks.toml
package.json                      # root: private, workspaces, scripts, engines, packageManager
package-lock.json                 # generated by npm 11.19.1, committed
tsconfig.base.json
tsconfig.json                     # solution file with project references
eslint.config.mjs
vitest.config.ts
.github/workflows/ci.yml          # NEW workflow; task-ledger.yml untouched
docs/DEVELOPMENT.md               # clone -> install -> verify, troubleshooting
docs/adr/ADR-013-toolchain-and-monorepo.md
docs/adr/ADR-014-orm-and-migrations.md      # Status: PROPOSED
docs/adr/ADR-015-authentication.md          # Status: PROPOSED
apps/api/{package.json,tsconfig.json,src/index.ts,src/index.test.ts}
apps/web/{package.json,tsconfig.json,src/index.ts,src/index.test.ts}
apps/worker/{package.json,tsconfig.json,src/index.ts,src/index.test.ts}
packages/contracts/{package.json,tsconfig.json,src/index.ts,src/index.test.ts}
packages/config/{package.json,tsconfig.json,src/index.ts,src/index.test.ts}
packages/testing/{package.json,tsconfig.json,src/index.ts,src/index.test.ts}
scripts/check-repo-hygiene.mjs
scripts/check-repo-hygiene.test.mjs
```

- Skeleton `src/index.ts` files export only a package identity constant (e.g. `export const PACKAGE_NAME = '@hisab/api'`). `apps/api` imports `@hisab/contracts` to prove cross-package resolution. **No framework, server, DB, env-secret read or business logic.**
- `packages/config`: typed placeholder only; no `process.env` reads in 001-A (env schema arrives in 001-C).
- Packages from `docs/ARCHITECTURE.md` **not** created yet (`money`, `tax-rules`, `coa`, `export-adapters`, `security`, `licensing`, `infra`) — created by the milestone that needs them, to avoid empty packages resembling features.

### Modified files
| File | Change |
|---|---|
| `.gitignore` | Append `*.tsbuildinfo`, `.vitest/`, `.npm/`; preserve all existing entries |
| `README.md` | Add pointer to `docs/DEVELOPMENT.md`; keep "Current state" factual (scaffold only, no application features) |
| `docs/DECISIONS.md` | Add index rows ADR-013 (for approval), ADR-014 (PROPOSED), ADR-015 (PROPOSED) linking to `docs/adr/` |
| `docs/STATUS.md` | Append dated factual entry (architect-authorized) |
| `docs/SESSION_HANDOFF.md` | Replace stale "repo not supplied" with verified repo/branch/SHA/test evidence (architect-authorized) |
| `docs/tasks/TASK-001-foundation.md` | Add sub-task index 001-A…E with links; no change to original AC wording |
| `docs/tasks/TASK-001-A-plan.md` | Developer Report section filled during implementation |

### Never touched
`docs/CHATGPT_ARCHITECT_MEMORY.md`, `docs/TASKS_DONE.md`, `docs/qa/**`, `.github/workflows/task-ledger.yml`, `scripts/validate_task_ledger.py`, `scripts/check_architect_memory.py`.

## 4. CI workflow design (`.github/workflows/ci.yml`)

- Triggers: `pull_request`; `push` to `main`.
- Workflow-level `permissions: contents: read`; no job requests broader permissions.
- **No secrets referenced** (`secrets.*` absent except the automatic read-only `GITHUB_TOKEN` where an action requires it); no environments, no deployment steps.
- `concurrency` group per ref, cancel-in-progress.
- Third-party actions pinned to **full commit SHA** with version comment; SHAs verified against the action's official release at implementation time.
- Jobs (ubuntu-latest, Node from `.nvmrc`, npm cache):
  1. `quality`: `npm ci` → `npm run format:check` → `npm run lint` → `npm run typecheck` → `npm run test:coverage` → `node scripts/check-repo-hygiene.mjs`.
  2. `audit`: `npm ci --ignore-scripts` → `npm audit --audit-level=high`.
  3. `secrets`: checkout `fetch-depth: 0` → gitleaks full-history scan using `.gitleaks.toml`.
- Existing `task-ledger.yml` continues unchanged (doc gate + protected-path guard for `task/` branches).

> [!WARNING]
> Per `docs/GITHUB_QA_SETUP.md` §3, the implementation PR adds a CI workflow and therefore requires **manual owner security review** in addition to architect QA. This will be stated in the PR description.

## 5. ADR content

### 5.1 ADR-013 — Toolchain & monorepo (decision requested)
Sections: ID, date, problem, options (Node 22/24/26; npm/pnpm/yarn; Turborepo vs none), decision (§2), consequences, reversal plan (Node upgrade task; package-manager change = lockfile regeneration + CI update), evidence links (Node schedule JSON, dist index), approver.

### 5.2 ADR-014 — ORM & migrations (STATUS: PROPOSED)
Criteria: RLS compatibility (tenant context via `SET LOCAL` / `set_config(..., true)` inside the **same transaction** as queries, safe with connection pooling); raw SQL for policies; **up and down** migrations; BIGINT/NUMERIC mapping without JS `Number` precision loss; type safety; maturity and maintenance.

| Option | Notes (to be validated by a spike in 001-B, after approval) |
|---|---|
| Prisma | Strong DX; RLS needs per-request interactive transactions + raw `set_config`; Prisma Migrate is forward-only (down via `migrate diff`) |
| Drizzle + explicit SQL up/down migrations (tentative) | SQL-close; explicit transactions make per-request `SET LOCAL` natural; RLS policies as reviewed SQL |
| Kysely / raw `pg` | Maximum control, more boilerplate |

Planned constraints independent of the choice: app DB role non-owner with `NOBYPASSRLS`; separate migration role; BIGINT never read as JS `number`. **No decision is made in 001-A.**

### 5.3 ADR-015 — Authentication (STATUS: PROPOSED) — managed vs self-hosted comparison (architect decision #6)

Requirements: staff MFA (blueprint §5.1); server-side sessions or equivalent with httpOnly/Secure/SameSite cookies, no tokens in browser storage; strong password hashing (argon2id) where passwords are held by us; rate limiting / lockout; session revocation; audit events; tenant context derived server-side from authenticated membership (never client-submitted `tenant_id`); roles owner/accountant/reviewer/client/auditor; CNDP Law 09-08 compatibility (data location, sub-processors, cross-border transfer); cost per user at annual-renewal pricing; exit/portability of identities.

| Criterion | Managed IdP (e.g. Auth0, Clerk, AWS Cognito, Microsoft Entra External ID) | Self-hosted IdP (e.g. Keycloak, Zitadel) | In-app auth with vetted primitives (argon2id + TOTP + DB sessions) |
|---|---|---|---|
| Time to secure MFA | Fastest | Medium | Slowest; must be built and tested |
| Personal data location / CNDP | Third-party processor, possibly cross-border → DPA + CNDP assessment required | Our infrastructure | Our database |
| Operational burden | Lowest | Highest (separate service to patch, back up, monitor) | Medium (inside our app) |
| Security surface we own | Smallest | Medium (config) | Largest (implementation) |
| Recurring cost | Per-MAU fees, vendor pricing changes | Infra + ops time | Dev + test time |
| Vendor lock-in / exit | Highest (user migration, password hashes export terms) | Low | Lowest |
| Fit with future on-prem edition | Weak (cloud dependency) | Good | Good |
| Enterprise SSO later | Built-in | Built-in | Via OIDC adapter seam |

Each option's specific product claims (MFA types, data regions, pricing) will be **verified from vendor documentation at ADR-writing time and cited**; none are asserted here. Tentative direction (not a decision): shortlist **one managed IdP with an acceptable data-processing basis** vs **in-app auth**, decided by the architect/owner after the CNDP/vendor review, before 001-C. No auth code in 001-A.

## 6. Acceptance criteria — verification, commands, expected outcomes

All commands run from the repository root on Node 24 / npm 11.19.1 unless stated. Outputs are captured verbatim (trimming marked) in the Developer Report.

| ID | Criterion | Verification method & command(s) | Expected outcome |
|---|---|---|---|
| **AC-A01** | Toolchain pinned: `.nvmrc`=`24`, `engines.node` `>=24.0.0 <25`, `engines.npm` `>=11 <12`, `packageManager` `npm@11.19.1`, `engine-strict=true` | `node -v; npm -v; npm ci` under Node 24. Negative: under Node 26 run `npm ci` | Node 24: `npm ci` exit 0. Node 26: exit ≠ 0 with `EBADENGINE` naming the required range |
| **AC-A02** | Workspace = `apps/{api,web,worker}`, `packages/{contracts,config,testing}`, each with `package.json`, `tsconfig.json`, `src/index.ts`, smoke test; no framework/business code | `npm query .workspace` and `git ls-files apps packages` | Exactly the 6 workspaces listed; only the files in §3 |
| **AC-A03** | Cross-package import through TS project references (`apps/api` → `@hisab/contracts`) builds and is tested | `npm run typecheck` (`tsc -b`) and `npx vitest run apps/api` | Both exit 0; api test asserts imported contracts constant |
| **AC-A04** | All quality gates pass from a **fresh clone** | `git clone <repo> <scratch>/hasib && cd <scratch>/hasib && git checkout <SHA> && npm ci && npm run format:check && npm run lint && npm run typecheck && npm test` | Every command exit 0; Vitest reports all tests passed (≥ 8 tests: 6 smoke + import + hygiene) |
| **AC-A05** | Gates reject violations | Temporarily add an uncommitted file with an `any` leak, a floating promise and bad formatting; run `npm run lint`, `npm run typecheck`, `npm run format:check`; then delete the file | Each command exits ≠ 0 and names the violation; tree clean afterwards (`git status --porcelain` empty) |
| **AC-A06** | `docs/DEVELOPMENT.md` reproduces setup on Windows and Linux, incl. engine-mismatch troubleshooting | Follow the doc literally in a fresh clone on Windows (dev machine); CI on ubuntu-latest | Windows log exit 0 per step; CI `quality` job green |
| **AC-A07** | `ci.yml`: PR + `main` triggers, `permissions: contents: read`, no secrets, SHA-pinned actions, `npm ci`, jobs `quality`/`audit`/`secrets` green on candidate SHA | Inspect `ci.yml`; `git grep -n "secrets\." .github/workflows/ci.yml`; GitHub Actions run for exact SHA | Only `contents: read`; grep returns no matches (or only documented `GITHUB_TOKEN` use); all 3 jobs succeed on the candidate SHA (run URL recorded) |
| **AC-A08** | No secrets in repo; hygiene script detects forbidden tracked files | CI gitleaks job; `node scripts/check-repo-hygiene.mjs`; `npx vitest run scripts` | gitleaks: no leaks found; hygiene exit 0 on clean tree; unit tests prove exit ≠ 0 for synthetic tracked `.env`, `x.pem`, `x.key`, `uploads/a.pdf`, `service-account-x.json` |
| **AC-A09** | No high/critical dependency vulnerabilities | `npm audit --audit-level=high` | exit 0, or each finding documented with justification + tracking note in Developer Report |
| **AC-A10** | ADR-013 complete; ADR-014 and ADR-015 complete with status **PROPOSED**; ADR-015 includes managed vs self-hosted comparison with cited sources; `DECISIONS.md` index updated | Doc review; `git grep -n "Status" docs/adr` | ADR-014/015 show `PROPOSED`; ADR-013 shows `PROPOSED — awaiting approval` until architect/owner approves |
| **AC-A11** | Existing documentation gate still passes | `python scripts/validate_task_ledger.py; python scripts/check_architect_memory.py`; `task-ledger.yml` run on PR | Both print `PASS`; workflow green |
| **AC-A12** | Protected files untouched | `git diff --name-only e2fc408..<SHA>` ; `git diff --name-only e2fc408..<SHA> -- docs/CHATGPT_ARCHITECT_MEMORY.md docs/TASKS_DONE.md docs/qa .github/workflows/task-ledger.yml scripts/validate_task_ledger.py scripts/check_architect_memory.py` | Second command prints nothing; `task-ledger.yml` protected-path guard green |
| **AC-A13** | `STATUS.md`, `SESSION_HANDOFF.md`, Developer Report updated with factual branch, PR, SHA, commands, outputs; `READY_FOR_QA` only with evidence; no QA PASS / DONE claims | Doc review; `git grep -n -i -E "QA_PASSED\|DONE" docs/STATUS.md docs/SESSION_HANDOFF.md docs/tasks/TASK-001-A-plan.md` | Matches only describe process/lifecycle, never claim this task passed or is done |
| **AC-A14** | No runtime/application functionality introduced | `git grep -n -E "listen\(\|process\.env\|createServer\|from 'pg'\|prisma\|drizzle\|@nestjs\|react" -- apps packages` | No matches (ADR docs excluded from search) |

## 7. Test plan

| Test | Type | Location / command |
|---|---|---|
| Package identity smoke tests (×6) | Unit | `apps/*/src/index.test.ts`, `packages/*/src/index.test.ts` — `npm test` |
| Cross-package import | Unit | `apps/api/src/index.test.ts` |
| Repo hygiene positive + negative cases | Unit | `scripts/check-repo-hygiene.test.mjs` — runs against temporary git repos in OS temp dir |
| Engine pin negative check | Manual, logged | AC-A01 |
| Lint/type/format negative check | Manual, logged | AC-A05 |
| Fresh-clone reproducibility | Manual, logged | AC-A04 / AC-A06 (clone in agent scratch dir, outside the repo) |
| CI pipeline | Automated | `ci.yml` on candidate SHA |
| Doc gate regression | Automated + local | `task-ledger.yml`; AC-A11 |

## 8. Execution sequence (only after authorization)

1. Install Node 24 LTS (user-level version manager); record `node -v` (expect `v24.x`) and `npm -v` (expect `11.x`).
2. Create `task/TASK-001-A-monorepo-toolchain-ci` from the then-current `main` (record SHA).
3. Commit root toolchain config + `package-lock.json`.
4. Commit workspace skeleton + smoke tests.
5. Commit hygiene script + tests, `.gitleaks.toml`, `ci.yml`.
6. Commit ADR-013/014/015, `DECISIONS.md` index, `DEVELOPMENT.md`, README pointer, TASK-001 sub-task index.
7. Run all AC commands locally + fresh-clone check; push branch; open PR to `main`; wait for CI.
8. Fill Developer Report, `STATUS.md`, `SESSION_HANDOFF.md` with exact SHA / PR / CI URLs → commit → confirm CI green on **that final SHA** → set `READY_FOR_QA` → stop and request independent QA.

Small atomic commits; the QA candidate is the PR head SHA. Any later commit invalidates a prior QA review.

## 9. Risks and mitigations

| Risk | Severity | Mitigation |
|---|---|---|
| Developer credentials may push to `main`; repo visibility/branch protection unverified | **High (process)** | Owner: confirm private repo, protect `main` (PR + required checks + owner review), CODEOWNERS for `docs/qa/**`, `docs/TASKS_DONE.md`, `docs/CHATGPT_ARCHITECT_MEMORY.md`, `.github/**`. Developer pushes only `task/*` branches |
| CI workflow added in implementation PR | Medium | Owner manual security review; `contents: read`; no secrets; SHA-pinned actions |
| Node 24 enters maintenance 2026-10-20 | Low | Supported to 2028-04-30; Node 26 upgrade as separate task after 2026-10-28 LTS |
| npm workspaces allow phantom (undeclared) dependencies | Low–Medium | ESLint `import/no-extraneous-dependencies` (or equivalent) per workspace; `npm ci` in CI |
| Empty skeletons mistaken for features | Medium | AC-A14; README/STATUS say "scaffold only"; only M1 packages |
| Windows/Linux differences | Low | `.gitattributes` LF, `.editorconfig`, Linux CI |
| Supply-chain vulnerabilities | Medium | Lockfile, exact versions, `npm audit`, minimal dev deps, `--ignore-scripts` in audit job |
| gitleaks false positives on docs | Low | Path+rule-scoped allowlist documented in `.gitleaks.toml`; no blanket ignores |
| Unverified vendor claims in ADR-015 | Medium | Cite vendor docs with access date; mark unverified items; no decision in 001-A |

## 10. Dependencies

| Dependency | Owner | Needed for |
|---|---|---|
| Architect review of this plan document | ChatGPT | Authorization |
| Project owner approval of this plan | Owner | Authorization |
| User-level install of Node 24 LTS on dev machine | Owner OK | Step 1 |
| Push access to `task/*` branches of `HamzaGhacham/Hasib` | Owner | PR + CI evidence |
| GitHub Actions enabled | Owner | AC-A07, AC-A08, AC-A11 |
| Branch protection / CODEOWNERS | Owner | Process control (recommended; not a 001-A blocker) |
| Not needed for 001-A: Docker, PostgreSQL, Redis, hosting, ORM/auth decisions | — | Required later for 001-B/C |

## 11. Remaining open points

1. **Skeleton depth:** plan assumes **framework-free** skeletons (decision #3 "basic packages"); NestJS arrives in 001-C, Vite/React in 001-D. Please confirm.
2. **Version manager:** `fnm` proposed for installing Node 24 locally; confirm or name an alternative.
3. **Plan PR disposition:** owner decides whether this documentation-only PR is merged, or kept open as the reference until implementation.

## Developer report (Gemini — filled only during/after authorized implementation)
- Branch: NOT STARTED
- PR: NOT STARTED
- Final candidate commit SHA: NOT STARTED
- Added / changed / deleted files: NOT STARTED
- Test commands and actual outputs: NOT EXECUTED
- CI link and status: NOT EXECUTED
- Security / tenant isolation check: N/A for 001-A (no tenant data); secret scan NOT EXECUTED
- Outstanding bugs and limitations: —
- Architecture deviations needing approval: none
- Next action: await architect review and owner authorization

## QA references (filled by owner/reviewer, not Gemini)
- Review 01 path:
- Final QA decision:
- Owner merge decision:
- Merged PR / commit:
- Completion ledger entry (only after owner approval and merge):
