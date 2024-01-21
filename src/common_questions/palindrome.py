# Question 2: How do you determine if a string is a palindrome?
from src.common_questions.reverse_string import reverse_string


def is_palindrome(arg: str) -> bool:
    if not arg:
        return False

    return arg == reverse_string(arg)
