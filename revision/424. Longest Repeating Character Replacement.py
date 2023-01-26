def characterReplacement(s,k):
    hash_map = {}
    l = 0
    r = 0
    res = 0

    while r < len(s):
        hash_map[s[r]] = hash_map.get(s[r], 0) + 1
        if max(hash_map.values()) + k < (r - l + 1):
            hash_map[s[l]] = hash_map.get(s[l], 0) - 1
            l += 1
        res = max(res, r - l + 1)
        r += 1
    return res
