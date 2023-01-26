def lengthOfLongestSubstring(s):
    res = 0
    counter = 0

    from collections import deque
    seen = deque()

    for char in s:
        while char in seen:
            seen.popleft()
            counter -= 1
        seen.append(char)
        counter += 1
        res = max(res, counter)

    return res



print(lengthOfLongestSubstring("dvdf"))