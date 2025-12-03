# claude-code

A collection of personal Claude Code utilities and custom slash commands.

## Overview

This repository contains a Claude Code plugin (`kuu-claude-utils`) that provides custom commands to enhance your Claude Code workflow. The plugin is designed to help maintain code quality and consistency when working with AI-assisted development.

## Installation

To use this plugin with Claude Code, clone this repository and configure Claude Code to load the plugin from the `.claude-plugin` directory.

```bash
git clone https://github.com/fumiya-kume/claude-code.git
```

## Available Commands

### `/deslop` - Remove AI Code Slop

Removes AI-generated "slop" from code changes in the current branch. This command helps maintain code quality by identifying and removing unnecessary additions that AI assistants sometimes introduce.

**What it removes:**
- Extra comments that a human wouldn't add or are inconsistent with the rest of the file
- Unnecessary defensive checks or try/catch blocks that are abnormal for that area of the codebase
- Any other style inconsistencies with the existing file

**Usage:**
```
/deslop
```

The command analyzes the diff against the main branch, identifies AI-generated patterns, removes unnecessary additions, and provides a brief summary of changes made.

## Plugin Structure

```
.claude-plugin/
├── plugin.json     # Plugin metadata and configuration
├── commands/       # Custom slash commands
│   └── deslop.md   # The deslop command definition
├── agents/         # Custom agents (placeholder)
└── skills/         # Custom skills (placeholder)
```

## Contributing

Feel free to fork this repository and add your own custom commands, agents, or skills.

## Acknowledgments

The `/deslop` command was inspired by [this tweet](https://x.com/ericzakariasson/status/1995671800643297542).

## License

This project is licensed under the GNU General Public License v3.0 - see the [LICENSE](LICENSE) file for details.
