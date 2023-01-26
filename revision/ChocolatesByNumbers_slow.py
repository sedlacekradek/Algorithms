def solution(N, M):
    visited = set()
    position = 0
    res = 0

    while True:
        if position not in visited:
            visited.add(position)
            res += 1
            position = (position + M) % N
        else:
            return res