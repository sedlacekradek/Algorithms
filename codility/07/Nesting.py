def solution(S):
    left_count = 0
    right_count = 0

    for char in S:
        if char == "(":
            left_count += 1
        else:
            right_count += 1

        if right_count > left_count:
            return 0

    if left_count != right_count:
        return 0

    return 1