"""
Basic usage example for Claude Code
"""

from claude_code.utils import hello_claude, format_prompt


def main():
    """Demonstrate basic usage of claude-code utilities."""
    # Basic greeting
    print(hello_claude())

    # Format prompts
    user_input = "What is the weather today?"
    formatted = format_prompt(user_input, "USER")
    print(formatted)

    # Format without prefix
    simple = format_prompt("Hello, Claude!")
    print(simple)


if __name__ == "__main__":
    main()
