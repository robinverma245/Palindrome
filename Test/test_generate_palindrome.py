"""Unit tests for the palindrome function."""

import pytest
from palindrome import is_palindrome


def test_invalid_input():
    """Check that non-string input raises ValueError."""
    with pytest.raises(ValueError):
        is_palindrome(123)


def test_empty_string():
    """Check that an empty string is not a palindrome."""
    assert is_palindrome("") is False


def test_single_character():
    """Check that a single character is a palindrome."""
    assert is_palindrome("a") is True


def test_two_same_characters():
    """Check that two identical characters form a palindrome."""
    assert is_palindrome("bb") is True


def test_different_characters():
    """Check that different characters are not a palindrome."""
    assert is_palindrome("abc") is False


def test_laval():
    """Check that laval is a palindrome."""
    assert is_palindrome("laval") is True


def test_toronto():
    """Check that toronto is not a palindrome."""
    assert is_palindrome("toronto") is False


def test_sentence_palindrome():
    """Check that spaces and capitalization are ignored."""
    assert is_palindrome("Able was I ere I saw Elba") is True
