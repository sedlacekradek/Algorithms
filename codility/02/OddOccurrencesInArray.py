def solution(a):
    result = 0
    for number in a:
        result ^= number

    return result

print(solution([9, 3, 9, 3, 9, 7, 9]))