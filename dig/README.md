# dig

Clarify ambiguities in plans with structured questions using the AskUserQuestion tool.

## Overview

This plugin helps analyze the current plan or discussion, identify unclear points, and ask structured questions to clarify requirements before implementation.

## Installation

```
/plugin marketplace add fumiya-kume/claude-code
/plugin install dig@fumiya-kume/claude-code
```

## Usage

The skill is automatically invoked by Claude when clarification is needed, or you can manually invoke it:

```
/dig
```

## Features

- Auto-loads context files (CLAUDE.md, prd.md, README.md)
- Identifies ambiguities across multiple categories (Architecture, Data, API, UI/UX, Testing, DevOps, Scope)
- Generates 2-4 structured questions with concrete options including pros/cons
- Outputs decisions and next steps after receiving answers

## How it works

1. Gather context from project files
2. Identify ambiguities in the current plan
3. Ask structured questions via AskUserQuestion tool
4. Summarize decisions and next steps after answers

## Allowed Tools

This skill uses the following tools:
- Write
- Edit
- Read
- Grep
- Glob
- TodoRead
- TodoWrite
- AskUserQuestion

## Plugin Structure

```
dig/
├── .claude-plugin/
│   └── plugin.json
├── skills/
│   └── dig/
│       └── SKILL.md
└── README.md
```

## License

GPL-3.0
