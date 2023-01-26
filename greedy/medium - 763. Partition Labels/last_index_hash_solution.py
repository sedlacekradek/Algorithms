"""
You are given a string s. We want to partition the string into as many parts as possible
so that each letter appears in at most one part.
Note that the partition is done so that after concatenating all the parts in order,
the resultant string should be s.
Return a list of integers representing the size of these parts.

Example 1:
Input: s = "ababcbacadefegdehijhklij"
Output: [9,7,8]
Explanation:
The partition is "ababcbaca", "defegde", "hijhklij".
This is a partition so that each letter appears in at most one part.
A partition like "ababcbacadefegde", "hijhklij" is incorrect, because it splits s into less parts.

Example 2:
Input: s = "eccbbbbdec"
Output: [10]
"""

def partitionLabels(s):
    # Input: s = "ababcbacadefegdehijhklij"
    # Output: [9, 7, 8]

    hash_map = {}

    for i, l in enumerate(s):
        hash_map[l] = i

    res = []
    last_index = 0
    counter = 0

    for i, v in enumerate(s):
        counter += 1
        last_index = max(hash_map[v], last_index)

        if i == last_index:
            res.append(counter)
            counter = 0

    return res

print(partitionLabels(s = "ababcbacadefegdehijhklij"))





