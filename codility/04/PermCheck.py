def solution(A):
    count = {}

    for n in range(1, len(A) + 1):
        count[n] = 0

    for number in A:
        if number not in count:
            return False
        count[number] = count.get(number) + 1
        if count[number] > 1:
            return False

    if min(count) < 1:
        return False

    return True

print(solution([4, 1, 3, 2]))
print(solution([4, 1, 2]))
print(solution([2,3,4,5]))
print(solution([2,3,3,4,5]))