"""
Utility functions for Claude Code
"""


def hello_claude() -> str:
    """
    Simple greeting function.

    Returns:
        A greeting message
    """
    return "Hello from Claude Code!"


def format_prompt(text: str, prefix: str = "") -> str:
    """
    Format a text prompt with an optional prefix.

    Args:
        text: The text to format
        prefix: Optional prefix to add before the text

    Returns:
        The formatted text
    """
    if prefix:
        return f"{prefix}: {text}"
    return text
