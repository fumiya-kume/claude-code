# Commands

This directory contains custom slash commands for Claude Code.

## Available Commands

### `/deslop` - Remove AI Code Slop

Removes AI-generated "slop" from code changes in the current branch.

**Purpose:**
This command helps maintain code quality by identifying and removing unnecessary additions that AI assistants sometimes introduce, ensuring code remains consistent with the project's existing style and practices.

**What it removes:**
- Extra comments that a human wouldn't add or are inconsistent with the rest of the file
- Extra defensive checks or try/catch blocks that are abnormal for that area of the codebase (especially if called by trusted/validated codepaths)
- Any other style that is inconsistent with the file

**Usage:**
```
/deslop
```

The command will:
1. Check the diff against the main branch
2. Analyze changes for AI-generated patterns
3. Remove unnecessary additions
4. Provide a brief 1-3 sentence summary of what was changed

# Special thanks

Inspired by https://x.com/ericzakariasson/status/1995671800643297542?s=20
