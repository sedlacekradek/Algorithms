def solution(A):
    max_list = []
    max_val = 0

    for i, val in enumerate(A):
        if i == 0:
            max_list.append(val)
            max_val = val
        else:
            submax = max(val, max_list[i - 1] + val)
            max_list.append(submax)
            max_val = max(max_val, submax)

    return max_val

print(solution([-1,-1,-1]))