# deslop

Remove AI-generated "slop" from code changes in the current branch.

## Overview

This plugin helps maintain code quality by identifying and removing unnecessary additions that AI assistants sometimes introduce, ensuring code remains consistent with the project's existing style and practices.

## Installation

```
/plugin marketplace add fumiya-kume/claude-code
/plugin install deslop@fumiya-kume/claude-code
```

## Usage

```
/deslop
```

## What it removes

- Extra comments that a human wouldn't add or are inconsistent with the rest of the file
- Extra defensive checks or try/catch blocks that are abnormal for that area of the codebase (especially if called by trusted/validated codepaths)
- Any other style that is inconsistent with the file

## How it works

1. Check the diff against the main branch
2. Analyze changes for AI-generated patterns
3. Remove unnecessary additions
4. Provide a brief 1-3 sentence summary of what was changed

## Plugin Structure

```
deslop/
├── .claude-plugin/
│   └── plugin.json
├── commands/
│   └── deslop.md
└── README.md
```

## Acknowledgments

Inspired by [this tweet](https://x.com/ericzakariasson/status/1995671800643297542).

## License

GPL-3.0
