"""
Given two strings s and t, return true if t is an anagram of s, and false otherwise.
An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase,
typically using all the original letters exactly once.

Example 1:
Input: s = "anagram", t = "nagaram"
Output: true

Example 2:
Input: s = "rat", t = "car"
Output: false
"""


def isAnagram(s, t):
    # time complexity O(s+t)

    s_dic = {}
    t_dic = {}

    if len(s) != len(t):
        return False

    for c in s:
        s_dic[c] = s_dic.get(c, 0) + 1
    for c in t:
        t_dic[c] = t_dic.get(c, 0) + 1
    for key in s_dic:
        if key not in t_dic or t_dic[key] != s_dic[key]:
            return False
    return True

print(isAnagram(s="zanagram", t="nagaram"))