def non_matching_characters(string: str):
    characters = [s for s in string]

    for i in range(len(characters)):
        if characters[i] is None:
            continue
        is_repeated = False
        for j in range(i + 1, len(characters)):
            if characters[i] == characters[j]:
                characters[j] = None
                is_repeated = True
        if is_repeated:
            characters[i] = None

    non_matching = [c for c in characters if c is not None]

    return non_matching
