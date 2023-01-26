def isValid(s):
    """
    Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
    An input string is valid if:
    Open brackets must be closed by the same type of brackets.
    Open brackets must be closed in the correct order.
    Every close bracket has a corresponding open bracket of the same type.
    """

#solution below denied due to "([)]" expected False

    opening1 = []
    closing1 = []
    opening2 = []
    closing2 = []
    opening3 = []
    closing3 = []

    for char in s:

        if char == "(":
            opening1.append(char)
        if char == ")":
            closing1.append(char)
            if len(opening1) < len(closing1):
                return False

        if char == "[":
            opening2.append(char)
        if char == "]":
            closing2.append(char)
            if len(opening2) < len(closing2):
                return False

        if char == "{":
            opening3.append(char)
        if char == "}":
            closing3.append(char)
            if len(opening3) < len(closing3):
                return False

    if len(opening1) != len(closing1) or len(opening2) != len(closing2) or len(opening3) != len(closing3):
        return False

    return True

print(isValid("[]"))