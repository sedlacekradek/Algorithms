"""
Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string "".

Example 1:
Input: strs = ["flower","flow","flight"]
Output: "fl"
"""


def longestCommonPrefix(strs):
    # take first word and set it as a prefix
    prefix = strs[0]
    for word in strs:
        # shorten the prefix until common part is found for each word
        while not word.startswith(prefix):
            prefix = prefix[:-1]

    return prefix



print(longestCommonPrefix(["aaa","aa","aaa"]))


