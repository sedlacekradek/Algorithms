def solution(nums, k):
    freq = {}
    res = []

    for n in nums:
        freq[n] = freq.get(n , 0) + 1

    from operator import itemgetter

    items = sorted(freq.items(), key=itemgetter(1), reverse=True)
    counter = 0
    for key, val in items:
        if counter == k:
            return res
        res.append(key)
        counter += 1

    return res

print(solution(nums = [3,3,1,2,2,3], k = 2))
print(solution(nums = [3,0,1,0], k = 1))