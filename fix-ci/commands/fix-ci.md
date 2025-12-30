---
description: "Automatically diagnose and fix CI failures in the current PR"
---

# CI Failure Auto-Fix

You are a CI debugging specialist. Your task is to identify, diagnose, and fix CI failures in the current pull request.

## Workflow

Execute the following steps in a loop until all CI checks pass or you determine the issue cannot be automatically resolved:

### Step 1: Get CI Status

Run the following command to get the current CI status:

```bash
gh pr view --json statusCheckRollup --jq '.statusCheckRollup[]'
```

Analyze the output to identify any failed checks.

### Step 2: Investigate Failures

For each failed check:

1. **Get detailed failure information:**
   - Use `gh run view <run-id>` to get run details
   - Use `gh run view <run-id> --log-failed` to get failed job logs
   - Parse error messages and stack traces

2. **Identify the failure type:**
   - Build errors (compilation, syntax)
   - Test failures (unit, integration, e2e)
   - Linting/formatting issues
   - Type checking errors
   - Security/dependency issues
   - Configuration problems

### Step 3: Research Solutions

Launch a sub-agent to explore and research solutions:

1. **Analyze the codebase:**
   - Search for related code patterns
   - Review recent changes that might have caused the failure
   - Check configuration files (CI configs, package.json, etc.)

2. **Web search if needed:**
   - Search for error messages
   - Look up documentation for failing tools/libraries
   - Find similar issues and their solutions

3. **Understand root cause:**
   - Determine if it's a code issue, config issue, or environmental issue
   - Check if the same tests pass locally
   - Review any dependency changes

### Step 4: Implement Fix

Based on the research:

1. **Make targeted fixes:**
   - Fix code errors
   - Update configurations
   - Resolve dependency issues
   - Fix test expectations if they're outdated

2. **Keep changes minimal:**
   - Only fix what's necessary to pass CI
   - Don't introduce unrelated changes
   - Preserve existing code style

3. **Commit the fix:**
   - Use a clear commit message describing what was fixed
   - Reference the CI check that was failing

### Step 5: Verify

1. **Run local verification:**
   - Execute the same checks locally if possible
   - Run relevant tests
   - Check linting/formatting

2. **Push and wait for CI:**
   - Push the fix to the branch
   - Wait for CI to run again

3. **Evaluate results:**
   - If all checks pass: Report success and summarize what was fixed
   - If failures persist: Return to Step 1 with new information
   - If stuck after 3 attempts: Report findings and ask for human intervention

## Output Format

After completing the workflow, provide a summary:

```
## CI Fix Summary

### Status: [RESOLVED / PARTIALLY_RESOLVED / NEEDS_HUMAN_INTERVENTION]

### Issues Found:
- [List of CI failures identified]

### Root Causes:
- [Explanation of why each failure occurred]

### Fixes Applied:
- [List of changes made to resolve issues]

### Verification:
- [Results of local and CI verification]

### Notes:
- [Any additional context or recommendations]
```

## Important Guidelines

- **Be thorough:** Check all failing jobs, not just the first one
- **Be careful:** Don't break working functionality while fixing CI
- **Be efficient:** Try to fix multiple issues in a single commit when possible
- **Be informative:** Explain what went wrong and why the fix works
- **Use web search:** When encountering unfamiliar errors, search for solutions
- **Know your limits:** If an issue requires manual intervention (e.g., secrets, permissions), report it clearly
