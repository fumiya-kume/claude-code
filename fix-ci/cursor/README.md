# fix-ci (Cursor)

Cursor Skill that auto-triggers on CI failure phrases, dispatches an `explore` subagent for read-only log/codebase analysis, applies a minimal fix in the main agent, and commits + pushes — single pass, no retry loop.

This is the Cursor port of the [Claude Code edition](../README.md). Behavior is identical in spirit but slimmed down to one attempt per the locked plan decisions.

## Install

### Option A — local symlink (recommended for development)

```bash
mkdir -p ~/.cursor/plugins/local
ln -s "$(pwd)/fix-ci/cursor" ~/.cursor/plugins/local/fix-ci
```

Then restart Cursor so the skill is picked up.

### Option B — Cursor marketplace (future)

Add this repository as a Cursor marketplace once it is published:

```
Add marketplace: fumiya-kume/claude-code  (path: .cursor-plugin/marketplace.json)
Install plugin:  fix-ci
```

## Triggers

The skill auto-invokes on any of these phrases.

**English**

- "fix CI"
- "fix failed checks"
- "PR is red"
- "diagnose CI failure"

**Japanese**

- "CI 直して"
- "CI が落ちてる"
- "PR の CI を直して"

## What it does

1. Runs `gh auth status` and bails if not authenticated.
2. Reads PR check status via `gh pr view --json statusCheckRollup`.
3. Pulls failed logs via `gh run view --log-failed`.
4. Dispatches one `explore` subagent (read-only) to correlate logs with the codebase.
5. Proposes a fix in plain language, then applies edits in the main agent.
6. Commits, pushes, and watches CI once via `gh pr checks --watch`.
7. Appends a `## CI Fix Summary` section to the active Cursor plan file (or creates `./PLAN.md`).

If the single attempt does not turn the PR green, the skill hands off to the user with a `NEEDS_HUMAN_INTERVENTION` report.

## Claude Code version

See [`../README.md`](../README.md) and the top-level [`../../README.md`](../../README.md) for the original Claude Code plugin.

## License

GPL-3.0
