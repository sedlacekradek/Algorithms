def solution(X, Y, D):
    # Implement your solution here
    if X == Y:
        return 0

    distance = Y - X
    jumps = (distance // D)
    if jumps * D < distance:
        jumps += 1

    return jumps

print(solution(9, 29, 10)) # 2