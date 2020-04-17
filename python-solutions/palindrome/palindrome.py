
"""
Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

Note: For the purpose of this problem, we define empty string as valid palindrome.

EX:
f("madam") yield True since reverse("madam") == "madam"
"""


def invert_str(s: str) -> str:
    return s[::-1]


def is_palindrome(s: str) -> bool:
    return s == invert_str(s)


if __name__ == "__main__":
    print(is_palindrome("madam"))  # True
