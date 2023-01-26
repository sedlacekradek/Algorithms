def solution(a):
    # scores 66 %

    a_sorted = a[:]
    a_sorted.sort()
    hash_map = {}
    count = {}
    res = []

    for number in a:
        count[number] = count.get(number, 0) + 1

    for i in range(0, len(a)):
        if a_sorted[i] in hash_map:
            continue
        for j in range(0, len(a)):
            if a_sorted[j] > a_sorted[i] // 2:
                hash_map[a_sorted[i]] = hash_map.get(a_sorted[i], 0) + (len(a) - j) - count[a_sorted[i]]
                break
            if a_sorted[i] % a_sorted[j] != 0:
                hash_map[a_sorted[i]] = hash_map.get(a_sorted[i], 0) + 1

    for number in a:
        if number in hash_map:
            res.append(hash_map[number])
        else:
            res.append(0)

    return res

print(solution([3, 1, 2, 3, 6])) #[2, 4, 3, 2, 0]
print(solution([1,1,1,1]))
print(solution([1]))
print(solution([2,4,2,4,2,4]))
print(solution([9,99,999,9999]))