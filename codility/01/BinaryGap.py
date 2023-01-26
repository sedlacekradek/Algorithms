def solution(n):
    number = bin(n)
    number = number[2:]
    result = 0
    counter = 0

    for digit in number:
        if digit == "0":
            counter += 1
        else:
            result = max(result, counter)
            counter = 0

    return result

print(solution(153))
print(solution(1041))
print(solution(32))
print(solution(6))
print(solution(10))
print(solution(0))