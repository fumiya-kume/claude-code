# dig (Cursor)

Cursor Skill that auto-triggers on planning phrases to challenge assumptions and stress-test plans through one focused round of AskQuestion. Decisions are written back to the active Cursor plan file as a `## Decisions` table.

This is the Cursor port of the [Claude Code edition](../README.md). Behavior is identical in spirit, but compressed to a single round of questioning per the locked plan decisions.

## Install

### Option A — local symlink (recommended for development)

```bash
mkdir -p ~/.cursor/plugins/local
ln -s "$(pwd)/dig/cursor" ~/.cursor/plugins/local/dig
```

Then restart Cursor so the skill is picked up.

### Option B — Cursor marketplace (future)

Add this repository as a Cursor marketplace once it is published:

```
Add marketplace: fumiya-kume/claude-code  (path: .cursor-plugin/marketplace.json)
Install plugin:  dig
```

## Triggers

The skill auto-invokes on any of these phrases.

**English**

- "dig"
- "challenge assumptions"
- "stress test plan"
- "find risks in plan"

**Japanese**

- "前提を疑って"
- "計画を深掘り"
- "プランに穴が無いか"

## What it does

1. Reads the active Cursor plan file, `CLAUDE.md`, and any referenced specs.
2. Maps implicit assumptions into Feasibility / User / Scope / Dependency / Timeline / Architectural buckets and ranks them by risk.
3. Runs one round of AskQuestion (2–4 questions) — pros/cons embedded in the option `label` since Cursor's AskQuestion only accepts `id` + `label`.
4. Writes a `## Decisions` table (Item / Choice / Reason / Notes) to the active plan file.
5. Posts a short summary in chat with key discoveries and remaining risks.

No iteration loop — single round, single summary, hand-off.

## Claude Code version

See [`../README.md`](../README.md) and the top-level [`../../README.md`](../../README.md) for the original Claude Code plugin.

## License

GPL-3.0
