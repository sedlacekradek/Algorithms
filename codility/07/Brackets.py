def solution(S):
    hashmap = {
        "(": ")",
        "[": "]",
        "{": "}"
    }

    stack = []

    for char in S:
        if char in "([{":
            stack.append(char)
        else:
            if len(stack) == 0 or hashmap[stack.pop()] != char:
                return 0

    if len(stack) != 0:
        return 0

    return 1

print(solution(")("))