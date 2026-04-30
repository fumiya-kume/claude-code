---
description: "Automatically diagnose and fix CI failures in the current PR"
version: "1.0.1"
allowed-tools:
  - Bash
  - Read
  - Edit
  - Write
  - Grep
  - Glob
  - WebSearch
  - Task
context: fork
---

# CI Failure Auto-Fix

Diagnose and fix CI failures in the current pull request using an iterative loop.

## Workflow

### Step 1: Verify GitHub CLI Authentication

```bash
gh auth status
```

If not authenticated, treat as **NEEDS_HUMAN_INTERVENTION** — instruct the user to run `gh auth login` locally or provide `GH_TOKEN`.

### Step 2: Get CI Status

```bash
gh pr view --json statusCheckRollup --jq '.statusCheckRollup[]'
```

Identify all failed checks. If no failures, report success and stop.

### Step 3: Inspect Failed Checks

For each failed check:

```bash
gh run view <run-id>
gh run view <run-id> --log-failed
```

If no `<run-id>` from the rollup output, use `gh pr checks` or `gh run list` to locate it.

Extract from logs:
- First actionable error message and stack trace
- Failing command (e.g., `npm test`, `ruff`, `go test`)
- Failing file paths and line numbers
- Failure type: build error, test failure, lint/format, type check, security/dependency, or configuration

### Step 4: Confirm Root Cause

1. Read the relevant source code and recent changes
2. Run the failing command locally to reproduce
3. Use WebSearch for unfamiliar error messages
4. Determine if fixable automatically — if it requires secrets, permissions, or manual approval, report as **NEEDS_HUMAN_INTERVENTION**

### Step 5: Explain and Fix

Before editing:
1. Explain the root cause in plain language
2. Describe the intended fix and why it should work
3. Note any risks (behavior changes, dependency bumps)

Apply targeted fixes — only what is necessary to pass CI. Preserve existing code style.

### Step 6: Commit and Push

```bash
git add <specific-files>
git commit -m "fix(ci): <short summary>"
git push
```

### Step 7: Wait and Iterate

```bash
gh pr checks --watch
```

- All checks pass → proceed to Step 8
- Failures persist → return to Step 3 with latest logs
- Stuck after 3 attempts → stop and report findings

### Step 8: Final Report

```markdown
## CI Fix Summary

### Status: [RESOLVED / PARTIALLY_RESOLVED / NEEDS_HUMAN_INTERVENTION]

### Issues Found
- [List of CI failures identified]

### Root Causes
- [Why each failure occurred]

### Fixes Applied
- [Changes made to resolve issues]

### Verification
- [Local and CI verification results]
```
