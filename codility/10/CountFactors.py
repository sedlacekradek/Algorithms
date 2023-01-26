def solution(n):
    i = 1
    result = 0

    while (i * i < n):
        if (n % i == 0):
            result += 2
        i += 1

    if (i * i == n):
        result += 1

    return result

print(solution(24))
print(solution(18))
print(solution(16))