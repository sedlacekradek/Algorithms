"""
Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string "".

Example 1:
Input: strs = ["flower","flow","flight"]
Output: "fl"
"""


def longestCommonPrefix(strs):
    prefix = strs[0]

    for word in strs:
        while word.startswith(prefix) is False:
            prefix = prefix[:-1]
    return prefix




print(longestCommonPrefix(["aaa", "aa", "aaa"]))