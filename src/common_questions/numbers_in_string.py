def calculate_numbers_in_str(arg: str) -> int | None:
    if not arg:
        return None

    result = "".join([char for char in arg if char.isdigit()])

    return int(result) if result else None
