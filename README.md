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

This repository is organized as a plugin marketplace containing multiple plugins:

```
.claude-plugin/
└── marketplace.json    # Marketplace metadata

commands/
├── deslop/             # deslop plugin
│   ├── .claude-plugin/
│   │   └── plugin.json
│   └── commands/
│       └── deslop.md
└── dig/                # dig plugin
    ├── .claude-plugin/
    │   └── plugin.json
    └── commands/
        └── dig.md

agents/                 # Custom agents (placeholder)
skills/                 # Custom skills (placeholder)
```

## Contributing

Feel free to fork this repository and add your own custom commands, agents, or skills.

## Acknowledgments

The `/deslop` command was inspired by [this tweet](https://x.com/ericzakariasson/status/1995671800643297542).

## License

This project is licensed under the GNU General Public License v3.0 - see the [LICENSE](LICENSE) file for details.
