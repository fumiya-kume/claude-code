---
name: deslop
description: "Remove AI-generated code slop from code changes in the current branch"
version: "1.0.1"
allowed-tools:
  - Read
  - Edit
  - Write
  - Bash
  - Grep
  - Glob
  - Task
context: fork
agent: General-purpose
model: sonnet
---

# Remove AI code slop

Check the diff against the default branch and remove all AI-generated slop introduced in this branch.

## Workflow

### Step 1: Decide the base branch

Pick the most appropriate base ref in this order:

1. `origin/main` (if it exists)
2. `origin/master` (if it exists)
3. `main` (local)
4. `master` (local)

Use a base like `<base>` in the rest of the steps.

### Step 2: Inspect the diff

- View the file list:
  - `git diff --name-only <base>...HEAD`
- View the full diff:
  - `git diff <base>...HEAD`

### Step 3: Remove AI-generated slop

Edit the changed files to remove slop while preserving intended behavior.

This includes:
- Extra comments that a human wouldn't add or is inconsistent with the rest of the file
- Extra defensive checks or try/catch blocks that are abnormal for that area of the codebase (especially if called by trusted / validated codepaths)
- Unnecessary indirection/wrappers, over-abstraction, or noisy helper functions introduced without clear value
- Any other style that is inconsistent with the file or project conventions

Guidelines:
- Keep the change scope minimal: only touch what is necessary to remove slop.
- Do not rewrite or reformat code unless required for the cleanup.
- Prefer deleting unnecessary code over adding new abstractions.
- If uncertain about intent, infer it from surrounding code and keep behavior compatible.

### Step 4: Final report

Report at the end with only a **1-3 sentence** summary of what you changed.
