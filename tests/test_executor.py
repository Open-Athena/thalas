"""
Tests for the executor module.
"""

from thalas.execution.executor import get_greeting


def test_get_greeting():
    """Test that get_greeting returns the expected string."""
    result = get_greeting()
    assert result == "Hello from Thalas execution framework!"
    assert isinstance(result, str)


def test_get_greeting_not_empty():
    """Test that get_greeting returns a non-empty string."""
    result = get_greeting()
    assert len(result) > 0
