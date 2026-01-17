# clarify

Create detailed specifications by iteratively clarifying unclear points through structured questions.

## Overview

This plugin is designed for Plan mode in Claude Code. It helps create comprehensive, unambiguous specifications by systematically identifying gaps and unclear points, then asking targeted questions until all requirements are fully defined.

## Installation

```
/plugin marketplace add fumiya-kume/claude-code
/plugin install clarify@fumiya-kume/claude-code
```

## Usage

Invoke the skill in Plan mode:

```
/clarify
```

## How it works

1. **Analyze** - Read existing plans, requirements, and project context
2. **Identify gaps** - Find all unclear, ambiguous, or missing specification points
3. **Ask questions** - Use structured questions with concrete options (2-4 options per question)
4. **Iterate** - Continue asking until all specifications are complete
5. **Document** - Write the final detailed specification with all decisions recorded

## Question Categories

The skill asks about:
- Scope (what's included/excluded)
- Behavior (system responses in specific scenarios)
- Data (format, validation, structure)
- Users (roles, permissions)
- Integration (system interactions)
- Constraints (technical/business limitations)
- Priority (essential vs nice-to-have)
- Edge cases (unusual situations)

## Allowed Tools

This skill uses the following tools:
- Read
- Write
- Edit
- Grep
- Glob
- TodoRead
- TodoWrite
- AskUserQuestion

## Plugin Structure

```
clarify/
├── .claude-plugin/
│   └── plugin.json
├── skills/
│   └── clarify/
│       └── SKILL.md
└── README.md
```

## License

GPL-3.0
