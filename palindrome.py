
def is_palindrome(value):
    if not isinstance(value, str):
        raise ValueError("Input must be a string")

    if value == "":
        return False

    if len(value) == 1:
        return True
