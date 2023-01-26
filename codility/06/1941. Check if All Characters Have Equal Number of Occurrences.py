def areOccurrencesEqual(s: str) -> bool:
    letters = {}
    for char in s:
        letters[char] = letters.get(char, 0) + 1

    temp = 0
    for key in letters:
        if temp == 0:
            temp = letters[key]
            continue
        if temp != letters[key]:
            return False

    return True