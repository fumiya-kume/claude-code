---
description: "Decompose complex tasks into detailed, actionable todos. Each todo has a rich description that is executable from the description alone."
version: "1.1.0"
context: fork
agent: General-purpose
---

# Task Decomposition

Break down complex tasks into detailed, actionable todos that can be executed independently.

## Process

### Step 1: Explore the Codebase

Before planning, build a concrete understanding of the current state.

Read and analyze:
- The current task or goal from conversation context
- CLAUDE.md (if available) for project context
- Related code, documentation, and existing plans

Explore specifically:
- **Project structure**: directories, modules, packages
- **Existing patterns**: how similar features are currently implemented
- **Relevant files**: which files will be affected
- **Dependencies**: libraries, APIs, internal modules involved

Do not decompose what you have not explored.

### Step 2: Identify Major Components

Break the task into major areas of work:
- What are the distinct phases?
- What are the dependencies between components?
- What order should they be tackled?

### Step 3: Interview for Unclear Points

Before creating detailed todos, resolve ambiguities by interviewing the user.

<rules>
- Use AskUserQuestion tool for all clarifications
- 2–4 questions per round, each with 2–4 concrete options with brief pros/cons
- "Other" option is auto-added — do not include it
- Focus on: scope boundaries, approach (modify vs. create), ordering, granularity, acceptance criteria, risk spikes
- Continue until all unclear points affecting decomposition are resolved
</rules>

### Step 4: Create Detailed Todos

For each component, create todos that are:
- **Specific** — exact file paths, function/class names, expected inputs/outputs
- **Achievable** — completable without external blockers
- **Small** — 5–30 minutes of focused work, single responsibility

### Step 5: Write Rich Descriptions

Each todo description must include:

```
**What**: [Specific action to take]
**Where**: [Exact file paths, function/class names, line ranges]
**How**: [Implementation approach referencing existing codebase patterns]
**Why**: [Purpose and how it fits into the larger task]
**Verify**: [Concrete verification — test command, expected output, or manual check]
```

### Step 6: Write Todos and Review

Write decomposed tasks as todos (all pending, imperative mood starting with action verb).

Review for completeness:
- Does the full set cover the entire original task?
- Does each todo have concrete verification steps?
- Are there remaining unclear points? If so, return to Step 3.

## Example

<example>
Original task: "Add user authentication to the API"

1. **Create User model in database schema**
   - What: Add User table with id, email, password_hash, created_at fields
   - Where: src/models/user.ts, src/migrations/003_create_users.ts
   - How: Follow existing model pattern in src/models/post.ts
   - Why: Store user credentials as the foundation for auth
   - Verify: Run `npm run migrate` and confirm with `npm test -- --grep "User model"`

2. **Implement password hashing utility**
   - What: Create hashPassword() and verifyPassword() functions
   - Where: src/utils/password.ts (new file), following src/utils/token.ts pattern
   - How: Use bcrypt with salt rounds of 12
   - Why: Secure password storage for registration and login
   - Verify: Run `npm test -- --grep "password"` — hash returns string, verify returns true for match
</example>
