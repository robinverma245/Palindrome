"""Palindrome validation using a deque."""

from collections import deque


def is_palindrome(value):
    """Check whether a string is a palindrome."""
    if not isinstance(value, str):
        raise ValueError("Input must be a string")

    if value == "":
        return False

    characters = deque(
        character.lower()
        for character in value
        if character.isalnum()
    )

    if not characters:
        return False

    while len(characters) > 1:
        if characters.popleft() != characters.pop():
            return False

    return True