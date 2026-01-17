# fix-ci

Automatically diagnose and fix CI failures in the current pull request.

## Overview

This plugin uses a sub-agent to analyze CI failures, research solutions, and implement fixes automatically. It's designed to handle common CI issues like build errors, test failures, linting issues, and more.

## Installation

```
/plugin marketplace add fumiya-kume/claude-code
/plugin install fix-ci@fumiya-kume/claude-code
```

## Usage

The skill is automatically invoked by Claude when CI failures are detected, or you can manually invoke it:

```
/fix-ci
```

Run this command when your PR has failing CI checks. The plugin will:

1. Fetch CI status using GitHub CLI
2. Analyze failed checks and retrieve detailed logs
3. Research solutions using codebase exploration and web search
4. Implement targeted fixes
5. Verify changes and iterate if needed

## How it works

### Workflow

1. **Status Check**: Uses `gh pr view --json statusCheckRollup` to get CI status
2. **Investigation**: Retrieves detailed failure logs with `gh run view`
3. **Research**: Sub-agent explores codebase and searches web for solutions
4. **Fix**: Implements minimal, targeted fixes
5. **Verify**: Runs local checks and pushes for CI verification
6. **Iterate**: Repeats until all checks pass or human intervention is needed

### Supported Failure Types

- Build errors (compilation, syntax)
- Test failures (unit, integration, e2e)
- Linting/formatting issues
- Type checking errors
- Security/dependency issues
- Configuration problems

## Output

After running, you'll receive a summary including:

- Status (RESOLVED / PARTIALLY_RESOLVED / NEEDS_HUMAN_INTERVENTION)
- Issues found and their root causes
- Fixes applied
- Verification results
- Additional recommendations

## Allowed Tools

This skill uses the following tools:
- Bash
- Read
- Edit
- Write
- Grep
- Glob
- WebSearch
- Task

## Requirements

- GitHub CLI (`gh`) must be installed and authenticated
- Must be run from within a git repository with an open PR

## Plugin Structure

```
fix-ci/
├── .claude-plugin/
│   └── plugin.json
├── commands/
│   └── fix-ci.md
└── README.md
```

## License

GPL-3.0
