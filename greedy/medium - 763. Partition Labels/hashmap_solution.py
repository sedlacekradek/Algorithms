def partitionLabels(s: str):
    res = []
    hash_map = {}

    for i in range(len(s)):
        hash_map[s[i]] = i

    i = 0
    last_char = 0
    while i < len(s):
        last_char = max(last_char, hash_map[s[i]])
        if i == last_char:
            if len(res) > 0:
                res.append(i + 1 - sum(res))
            else:
                res.append(i + 1)
        i += 1

    return res

print(partitionLabels("eccbbbbdec"))
print(partitionLabels("e"))