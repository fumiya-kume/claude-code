---
name: deslop
description: "Remove AI-generated code slop from code changes in the current branch. Use when cleaning up LLM-authored diffs that contain unnecessary comments, defensive checks, or style inconsistencies before merging."
version: "1.0.0"
allowed-tools: "Read, Edit, Write, Bash, Grep, Glob, Task"
---

# Remove AI code slop

Identify and remove AI-generated artifacts from the current branch by comparing against main.

## Workflow

### Step 1: Get changed files

```bash
git diff --name-only main...HEAD -- '*.ts' '*.js' '*.py' '*.go' '*.rs' '*.java'
```

### Step 2: Review each file for slop patterns

For each changed file, read the full file and the diff (`git diff main...HEAD -- <file>`). Look for these patterns:

**Unnecessary comments** — comments that restate the code or were not present in surrounding unchanged code:

```diff
- // Check if the user is authenticated
  if (!user.isAuthenticated) {
```

**Excessive defensive checks** — try/catch blocks, null guards, or type checks that the surrounding codebase does not use in similar contexts:

```diff
- try {
    await db.save(record);
- } catch (error) {
-   console.error('Failed to save record:', error);
-   throw error;
- }
```

**Style inconsistencies** — naming conventions, import ordering, or formatting that differs from the rest of the file (e.g., adding JSDoc where the file uses none).

### Step 3: Apply fixes

Use the Edit tool to remove or rewrite each identified pattern. Match the style of the surrounding unchanged code.

### Step 4: Verify

Run `git diff main...HEAD --stat` to confirm only intended changes remain. Report a 1–3 sentence summary of what changed.
