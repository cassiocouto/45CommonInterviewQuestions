# complexity: O(n)
def count_single_character(string: str, character: str) -> int:
    return string.count(character)


# complexity: O(n+m) instead of O(n.m)
def count_many_characters(string: str, characters: list) -> dict:
    histogram: dict = dict()
    for c in characters:
        histogram[c] = 0

    for element in string:
        if histogram.get(element) is not None:
            histogram[element] = histogram[element] + 1

    return histogram
