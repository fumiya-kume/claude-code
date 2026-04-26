---
name: fix-ci
description: This skill should be used when the user asks to "fix CI", "fix failed checks", "PR is red", "diagnose CI failure". Also triggers when the user says in Japanese: "CI 直して", "CI が落ちてる", "PR の CI を直して".
---

# Fix CI (Cursor Skill)

Diagnose and fix CI failures on the current pull request in a single pass. Use the GitHub CLI to gather status and logs, dispatch an `explore` subagent for read-only investigation, then apply edits and push from the main agent. If the fix does not turn the PR green on the first attempt, hand off to the user with a clear report — do not enter a retry loop.

## Persistence Target

Persist intermediate findings and the final summary to the active Cursor plan file:

- Look up the currently active plan via the agent's plan tools (e.g. `read_plan` / `update_plan`).
- If no plan is active, create a new file at `./PLAN.md` and use that as the persistence target.
- Append the `## CI Fix Summary` section to the plan file once the fix is verified (or when handing off to the user).

## Workflow (single pass)

### Step 1. Verify GitHub CLI authentication

Run `gh auth status`. If unauthenticated:

- Surface the error to the user and stop.
- Do not attempt interactive `gh auth login` from the agent — Cursor's shell is not guaranteed to be interactive.
- Recommend the user run `gh auth login` (or set `GH_TOKEN`) and re-trigger the skill.

### Step 2. Read CI status on the current PR

Run:

```bash
gh pr view --json statusCheckRollup --jq '.statusCheckRollup[]'
```

Parse the output to identify failing checks and capture their `name`, `conclusion`, and `detailsUrl` / run id.

### Step 3. Pull failed logs

For each failing check:

```bash
gh run view <run-id>
gh run view <run-id> --log-failed
```

If a run id cannot be derived from the rollup, fall back to `gh pr checks` or `gh run list --branch <branch>` and pick the latest failing run.

Capture for each failure:

- The first actionable error message
- The failing command (e.g. `npm test`, `pytest`, `golangci-lint`, `gradle test`)
- File paths and line numbers
- Whether the failure looks like code, configuration, or environment / permissions

### Step 4. Dispatch an `explore` subagent for analysis

Dispatch one `Task` subagent of type `explore` (read-only). Pass it:

- The captured log excerpts and run ids
- The failing command(s)
- The file paths and line numbers from the logs
- The git diff range (e.g. base..HEAD on this branch) so it can correlate failures with recent changes

Ask the subagent to:

1. Locate the failing code and any related tests / configs.
2. Cross-reference recent commits on this branch.
3. Classify the failure (build / test / lint / type / dep / config / env).
4. Recommend the minimal fix.

The subagent must not make edits or run network commands beyond read-only exploration.

### Step 5. Propose the fix in plain language

Before editing, write a short paragraph in chat that covers:

- Root cause in plain language
- Intended fix and why it should work
- Risks (behavior change, dependency bump, scope creep)
- Out-of-scope notes (anything observed but deliberately not fixed)

### Step 6. Apply edits in the main agent

Apply the fix yourself (do not delegate edits to the subagent). Keep the change minimal:

- Fix only what is required to turn the failing check green.
- Preserve existing style and formatting.
- Do not refactor unrelated code.

### Step 7. Commit and push

Run, in order:

```bash
git status
git add -A
git commit -m "fix(ci): <short summary of the fix>"
git push
```

Use a clear message that names the failing check when helpful.

### Step 8. Watch CI (single attempt)

Run:

```bash
gh pr checks --watch
```

Wait for the run to complete. Do not start another retry pass — this skill is single-attempt by design.

### Step 9. Report and persist

Two outcomes:

- **All green:** Append the `## CI Fix Summary` section (template below) to the active plan file and post a short confirmation in chat.
- **Still failing or fix not possible:** Append a `## CI Fix Summary` section with status `NEEDS_HUMAN_INTERVENTION`, summarize what was tried and what is blocking, and explicitly hand off to the user.

## Output Template

Append this section to the active plan file:

```markdown
## CI Fix Summary

### Status
[RESOLVED | PARTIALLY_RESOLVED | NEEDS_HUMAN_INTERVENTION]

### Failing Checks (before fix)
- <check name> — <one-line failure>

### Root Causes
- <root cause per failure>

### Fixes Applied
- <file>: <what changed and why>

### Verification
- `gh pr checks --watch` outcome: <pass / fail / partial>
- Local checks run (if any): <commands and results>

### Recommendations / Follow-ups
- <items the user should consider next>
```

## Guidelines

- Single attempt only. Do not loop on failures — hand off instead.
- Auth gate first. Never attempt to fix CI without `gh auth status` succeeding.
- Subagent is read-only. All edits, commits, and pushes happen in the main agent.
- Keep edits minimal. The goal is to turn checks green, not to refactor.
- Persist before exiting. The active plan file (or `./PLAN.md`) must contain the summary.
- Surface unfixable cases. Permissions, secrets, infra, manual approvals, or sandbox-only blockers must be reported clearly with the user actions required.
