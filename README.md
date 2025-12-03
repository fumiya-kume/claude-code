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

## Available Plugins

| Plugin | Description |
|--------|-------------|
| [deslop](commands/deslop/) | Remove AI-generated "slop" from code changes |
| [dig](commands/dig/) | Clarify ambiguities in plans with structured questions |

See each plugin's README for detailed usage and features.

## Plugin Structure

This repository is organized as a plugin marketplace containing multiple plugins:

```
.claude-plugin/
└── marketplace.json    # Marketplace metadata

commands/
├── deslop/             # deslop plugin
│   ├── .claude-plugin/
│   │   └── plugin.json
│   ├── commands/
│   │   └── deslop.md
│   └── README.md
└── dig/                # dig plugin
    ├── .claude-plugin/
    │   └── plugin.json
    ├── commands/
    │   └── dig.md
    └── README.md

agents/                 # Custom agents (placeholder)
skills/                 # Custom skills (placeholder)
```

## Contributing

Feel free to fork this repository and add your own custom commands, agents, or skills.

## Acknowledgments

The `/deslop` command was inspired by [this tweet](https://x.com/ericzakariasson/status/1995671800643297542).

## License

This project is licensed under the GNU General Public License v3.0 - see the [LICENSE](LICENSE) file for details.
