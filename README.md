# claude-code

Kuu's Claude Code utils for myself - A collection of utility functions and tools for working with Claude.

## Installation

### From Source

```bash
git clone https://github.com/fumiya-kume/claude-code.git
cd claude-code
pip install -e .
```

### Development Installation

```bash
pip install -e ".[dev]"
```

## Usage

```python
from claude_code.utils import hello_claude, format_prompt

# Basic greeting
print(hello_claude())

# Format prompts
user_message = "What is the weather today?"
formatted = format_prompt(user_message, "USER")
print(formatted)  # Output: USER: What is the weather today?
```

## Development

### Running Tests

```bash
pytest
```

### Code Formatting

```bash
black src/ tests/
```

### Type Checking

```bash
mypy src/
```

## Examples

Check out the `examples/` directory for more usage examples:

```bash
python examples/basic_usage.py
```

## License

This project is licensed under the GPL-3.0 License - see the [LICENSE](LICENSE) file for details.
