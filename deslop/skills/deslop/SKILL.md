---
name: deslop
description: "Remove AI-generated code slop from code changes in the current branch"
version: "1.0.0"
context: fork
allowed-tools:
  - Read
  - Edit
  - Write
  - Bash
  - Grep
  - Glob
  - Task
context: fork
agent: Explore
---

# Remove AI code slop

Check the diff against main, and remove all AI generated slop introduced in this branch.
You will launch the sub-agent to proceed this process

This includes:
- Extra comments that a human wouldn't add or is inconsistent with the rest of the file
- Extra defensive checks or try/catch blocks that are abnormal for that area of the codebase (especially if called by trusted / validated codepaths)
- Any other style that is inconsistent with the file

Report at the end with only a 1-3 sentence summary of what you changed
