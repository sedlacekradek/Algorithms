def solution(N, A):
    res = [0 for _ in range(N + 1)]
    my_max = 0
    recent_max = False

    for number in A:
        if number > N and recent_max is False:
            res = [my_max] * (N + 1)
            recent_max = True
        elif number <= N:
            res[number] += 1
            my_max = max(my_max, res[number])
            recent_max = False

    return res[1:]

print(solution(5, [3, 4, 4, 6, 1]))
print(solution(5, [6, 6, 6, 6, 6, 6]))