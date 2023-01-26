def solution(S):
    left = 0
    right = 0

    for char in S:
        if char == "(":
            left += 1
        else:
            right += 1

        if right > left:
            return 0

    if left == right:
        return 1
    else:
        return 0