"""
Tests for utils module
"""

from claude_code.utils import hello_claude, format_prompt


def test_hello_claude():
    """Test the hello_claude function."""
    result = hello_claude()
    assert result == "Hello from Claude Code!"
    assert isinstance(result, str)


def test_format_prompt_without_prefix():
    """Test format_prompt without a prefix."""
    text = "This is a test"
    result = format_prompt(text)
    assert result == "This is a test"


def test_format_prompt_with_prefix():
    """Test format_prompt with a prefix."""
    text = "This is a test"
    prefix = "USER"
    result = format_prompt(text, prefix)
    assert result == "USER: This is a test"


def test_format_prompt_with_empty_string():
    """Test format_prompt with empty string."""
    result = format_prompt("")
    assert result == ""


def test_format_prompt_with_empty_prefix():
    """Test format_prompt with empty prefix."""
    text = "This is a test"
    result = format_prompt(text, "")
    assert result == "This is a test"
