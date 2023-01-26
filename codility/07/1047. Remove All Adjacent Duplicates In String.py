def removeDuplicates(s: str) -> str:
    stack = []
    stack.append(s[0])

    if len(s) < 2:
        return stack

    for char in s[1:]:
        # do not forget this condition for case when there are no chars
        if len(stack) == 0:
            stack.append(char)
        elif char == stack[-1]:
            stack.pop()
        else:
            stack.append(char)

    return "".join(stack)

print(removeDuplicates("abbaca"))