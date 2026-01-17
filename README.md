# claude-code

A collection of personal Claude Code utilities and custom slash commands.

## Overview

This repository contains a Claude Code plugin marketplace that provides custom commands to enhance your Claude Code workflow. The plugins are designed to help maintain code quality and consistency when working with AI-assisted development.

## Installation

### From Claude Code (Recommended)

You can install plugins directly from Claude Code using the plugin management system:

1. Add this repository as a marketplace:
   ```
   /plugin marketplace add fumiya-kume/claude-code
   ```

2. Install the plugins:
   ```
   /plugin install deslop@fumiya-kume/claude-code
   /plugin install dig@fumiya-kume/claude-code
   /plugin install fix-ci@fumiya-kume/claude-code
   ```

3. Restart Claude Code to activate the plugins.

### Manual Installation

Alternatively, you can clone this repository and use it as a local marketplace:

```bash
git clone https://github.com/fumiya-kume/claude-code.git
```

Then in Claude Code:
```
/plugin marketplace add ./claude-code
```

## Available Plugins

| Plugin | Description |
|--------|-------------|
| [deslop](deslop/) | Remove AI-generated "slop" from code changes |
| [dig](dig/) | Clarify ambiguities in plans with structured questions |
| [fix-ci](fix-ci/) | Automatically diagnose and fix CI failures |

## Commands

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

### `/deslop` - Remove AI Code Slop

Removes AI-generated "slop" from code changes in the current branch.

**Purpose:**
This command helps maintain code quality by identifying and removing unnecessary additions that AI assistants sometimes introduce, ensuring code remains consistent with the project's existing style and practices.

**What it removes:**
- Extra comments that a human wouldn't add or are inconsistent with the rest of the file
- Extra defensive checks or try/catch blocks that are abnormal for that area of the codebase
- Any other style that is inconsistent with the file

**Usage:**
```
/deslop
```

### `/fix-ci` - Fix CI Failures

Automatically diagnose and fix CI failures using sub-agent exploration.

**Purpose:**
This command helps quickly identify and resolve CI pipeline failures by analyzing logs, identifying root causes, and applying fixes.
It checks `gh` authentication up front (and may ask you to log in), then iterates by pushing fixes and waiting for CI to rerun until checks are green or human intervention is required.
For the detailed workflow, see [`fix-ci/commands/fix-ci.md`](fix-ci/commands/fix-ci.md).

**Usage:**
```
/fix-ci
```

## Plugin Structure

This repository is organized as a plugin marketplace containing multiple plugins:

```
.claude-plugin/
└── marketplace.json    # Marketplace metadata

deslop/                 # deslop plugin
├── .claude-plugin/
│   └── plugin.json
├── commands/
│   └── deslop.md
└── README.md

dig/                    # dig plugin
├── .claude-plugin/
│   └── plugin.json
├── commands/
│   └── dig.md
└── README.md

fix-ci/                 # fix-ci plugin
├── .claude-plugin/
│   └── plugin.json
├── commands/
│   └── fix-ci.md
└── README.md
```

## Contributing

Feel free to fork this repository and add your own custom commands, agents, or skills.

## Acknowledgments

The `/deslop` command was inspired by [this tweet](https://x.com/ericzakariasson/status/1995671800643297542).

## License

This project is licensed under the GNU General Public License v3.0 - see the [LICENSE](LICENSE) file for details.
