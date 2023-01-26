def isValid(s):
    """
    :type s: str
    :rtype: bool
    """

    stack = []

    hash = {
        "(": ")",
        "[": "]",
        "{": "}",
    }

    for character in s:
        if character in hash:
            stack.append(character)
        else:
            if len(stack) == 0 or character != hash[stack.pop()]:
                return False
    return len(stack) == 0

print(isValid("([)]"))