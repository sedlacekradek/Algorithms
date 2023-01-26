# scores 37 %

def count_ways(n, hash_map):
    res = 0
    if n in hash_map:
        return hash_map[n]
    if n == 0:
        return 1
    if n < 0:
        return 0
    res += count_ways(n-1, hash_map)
    res += count_ways(n-2, hash_map)
    return res

def solution(a,b):
    res = []
    hash_map = {}

    for n in a:
        if n in hash_map:
            continue
        else:
            ways = count_ways(n, hash_map)
            hash_map[n] = ways

    for a, b in zip(a, b):
        # slower and clear
        res.append(hash_map[a] % (2 ** b))
        # faster but a bit wtf
        # res.append(hash_map[a] & (2 ** b - 1))

    return res

print(solution([4, 4, 5, 5, 1], [3, 2, 4, 3, 1])) # [5, 1, 8, 0, 1]
