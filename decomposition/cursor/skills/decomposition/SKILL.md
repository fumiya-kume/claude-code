---
name: decomposition
description: This skill should be used when the user asks to "decompose", "break down task", "create detailed todos", "split into todos". Also triggers when the user says in Japanese: "タスク分解", "todo に落として", "細かい todo にして".
---

# Decomposition (Cursor Skill)

Break a complex task into rich, self-contained todos that can be executed independently. Run a single pass: explore, identify components, optionally ask one round of clarifying questions, then write todos via the agent's todo tool and append a summary to the active plan file.

## Persistence Target

Persist the decomposition summary to the active Cursor plan file:

- Look up the currently active plan via the agent's plan tools (e.g. `read_plan` / `update_plan`).
- If no plan is active, create `./PLAN.md` and treat that as the active plan.
- Always append a `## Decomposition Summary` section after writing the todos.

## Process (single pass)

### Step 1. Explore the codebase

Build a concrete mental model before decomposing anything:

- Read the current task or goal from the conversation context and the active plan file.
- Read `CLAUDE.md` and / or `AGENTS.md` if present.
- Read related code, configs, or specs the task references.
- Map the directory layout for affected modules.
- Identify existing patterns for similar features (so todos can reference them).

Do not skip this step — todos generated without exploration are usually too vague to execute.

### Step 2. Identify major components

Decompose the overall task into distinct components:

- What are the phases or areas of work?
- What are the dependencies between components?
- What is the natural execution order?

Keep this internal — the next steps turn it into todos.

### Step 3. (Optional) One round of AskQuestion

Only if there are unclear points that meaningfully affect decomposition (scope boundaries, ordering, granularity, acceptance criteria, risk-spike vs direct implementation), run **one** round of AskQuestion via the Cursor AskQuestion tool.

Question rules:

- 2 to 4 questions per round.
- Each question has 2 to 4 concrete options.
- Cursor AskQuestion options accept only `id` and `label`. Embed pros/cons in the `label` string. Example:
  - `"Modify existing service — Pros: smaller diff, reuses tests / Cons: harder to revert, couples concerns"`
  - `"New service module — Pros: clean boundary, easier rollback / Cons: more files, new test scaffold"`
- Do not include an "Other" option — let the user type a custom answer.

If everything is already clear from Step 1, skip this step. Single pass: do not run a second round later.

### Step 4. Create rich todos

For each component, produce todos that are Specific, Achievable, and Small enough (~5–30 minutes each, single responsibility, independently verifiable).

Each todo's description must follow this template:

```text
What:   <specific action, with action verb>
Where:  <exact file path(s), function/class/component names, line ranges if known>
How:    <implementation approach referencing existing patterns in the codebase>
Why:    <purpose and how it fits into the larger task>
Verify: <concrete verification — test command and expected output, or manual check procedure>
```

Use action verbs (`Create`, `Add`, `Update`, `Remove`, `Implement`, `Configure`, ...). Use real file paths and real function / class names from Step 1. Vague references are not acceptable.

### Step 5. Save todos via the agent's todo tool

Save the decomposed todos via the agent's todo tool (the standard built-in Cursor todo writer — refer to it generically as "the todo tool"; do not hard-code a specific tool name in case the implementation evolves):

- One todo per atomic unit of work.
- Status `pending` for all new todos.
- Imperative mood, starting with an action verb.
- The full What / Where / How / Why / Verify body lives in the todo's description / content field.

### Step 6. Append summary to the plan file

Append a section like the following to the active plan file:

```markdown
## Decomposition Summary

### Original Task
<one-paragraph description of the task that was decomposed>

### Decomposed Todos
1. <Todo 1 title> — <one-line essence>
2. <Todo 2 title> — <one-line essence>
...

### Dependencies
- <Todo X> must complete before <Todo Y>
- <other ordering / parallelism notes>

### Estimated Scope
- Total todos: <N>
- Complexity: <Low | Medium | High>

### Open Questions / Follow-ups
- <anything the user should still answer or watch for>
```

Then stop. Do not loop back into another decomposition round — this is single-pass by contract.

## Guidelines

- Single pass only. One exploration, one optional question round, one todo write, one summary. No retry loop.
- Explore before decomposing. Vague todos almost always come from skipping Step 1.
- Reference real code. Use actual file paths, function names, and patterns from the codebase.
- Every todo must be verifiable. Include a concrete test command, expected output, or manual check.
- Embed pros/cons in option labels. Cursor's AskQuestion exposes only `id` and `label`.
- Persist to the plan file. The chat-only summary is not enough — the plan file is the source of truth.
