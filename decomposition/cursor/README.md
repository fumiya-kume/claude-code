# decomposition (Cursor)

Cursor Skill that auto-triggers on task-breakdown phrases and produces rich, actionable todos saved via the agent's todo tool. A summary section is appended to the active Cursor plan file.

This is the Cursor port of the [Claude Code edition](../README.md). Behavior is identical in spirit, but compressed to a single pass per the locked plan decisions.

## Install

### Option A — local symlink (recommended for development)

```bash
mkdir -p ~/.cursor/plugins/local
ln -s "$(pwd)/decomposition/cursor" ~/.cursor/plugins/local/decomposition
```

Then restart Cursor so the skill is picked up.

### Option B — Cursor marketplace (future)

Add this repository as a Cursor marketplace once it is published:

```
Add marketplace: fumiya-kume/claude-code  (path: .cursor-plugin/marketplace.json)
Install plugin:  decomposition
```

## Triggers

The skill auto-invokes on any of these phrases.

**English**

- "decompose"
- "break down task"
- "create detailed todos"
- "split into todos"

**Japanese**

- "タスク分解"
- "todo に落として"
- "細かい todo にして"

## What it does

1. Explores the codebase, the active plan file, and `CLAUDE.md` to build a concrete mental model.
2. Identifies major components and their dependencies.
3. Optionally runs one round of AskQuestion (2–4 questions, pros/cons embedded in option `label`) if any decomposition-affecting points are unclear.
4. Generates rich todos using the **What / Where / How / Why / Verify** template — each todo is specific, achievable, and ~5–30 minutes of focused work.
5. Saves todos via the agent's todo tool.
6. Appends a `## Decomposition Summary` section to the active Cursor plan file.

No iteration loop — single pass, single todo write, single plan update.

## Claude Code version

See [`../README.md`](../README.md) and the top-level [`../../README.md`](../../README.md) for the original Claude Code plugin.

## License

GPL-3.0
