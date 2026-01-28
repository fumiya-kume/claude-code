# decomposition

Decompose complex tasks into detailed, actionable todos with rich descriptions.

|||
|---|---|
|<img alt="image" src="https://github.com/user-attachments/assets/e4c85464-d912-4940-9f5e-f8fb5a867e8a" />|<img alt="image" src="https://github.com/user-attachments/assets/592a742d-fe65-4f32-a0c3-ffab02d13173" />|

## Overview

This plugin helps break down complex tasks into specific, achievable, and small todos. Each todo has a rich description that contains all the information needed to execute the task independently.

## Installation

```bash
/plugin marketplace add fumiya-kume/claude-code
/plugin install decomposition@fumiya-kume/claude-code
```

## Usage

Invoke the command:

```bash
/decomposition
```

## How it works

1. **Analyze** - Read the current context, plans, and related files
2. **Identify components** - Break down the task into major components
3. **Create todos** - Generate detailed todos for each component
4. **Write rich descriptions** - Add What, Where, How, Why, Done when to each todo
5. **Write todos** - Use TodoWrite tool to save the decomposed tasks

## Todo Quality Criteria

Each decomposed todo should be:

- **Specific** - Clear action verb, exact locations, expected inputs/outputs
- **Achievable** - Can be completed without external blockers
- **Small enough** - Takes roughly 5-30 minutes, single responsibility

## Rich Description Format

Each todo includes:

- **What**: Specific action to take
- **Where**: File path or location
- **How**: Brief implementation approach
- **Why**: Purpose and context
- **Done when**: Verification criteria

## Plugin Structure

```text
decomposition/
├── .claude-plugin/
│   └── plugin.json
├── commands/
│   └── decomposition.md
└── README.md
```

## License

GPL-3.0
