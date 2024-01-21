# Question 1: How do you reverse a string?
def reverse_string(arg: str) -> str | None:
    if not arg:
        return None
    return arg[::-1]
