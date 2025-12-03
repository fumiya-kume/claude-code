# Commands

This directory contains custom slash commands for Claude Code.

## Available Commands

### `/dig` - Plan Dig Mode

Clarify ambiguities in plans with structured questions using the AskUserQuestion tool.

**Purpose:**
Analyze the current plan or discussion, identify unclear points, and ask structured questions to clarify requirements before implementation.

**Features:**
- Auto-loads context files (CLAUDE.md, prd.md, README.md)
- Identifies ambiguities across multiple categories (Architecture, Data, API, UI/UX, Testing, DevOps, Scope)
- Generates 2-4 structured questions with concrete options including pros/cons
- Outputs decisions and next steps after receiving answers

**Usage:**
```
/dig
```

The command will:
1. Gather context from project files
2. Identify ambiguities in the current plan
3. Ask structured questions via AskUserQuestion tool
4. Summarize decisions and next steps after answers

---

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
