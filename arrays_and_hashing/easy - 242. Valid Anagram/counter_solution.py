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

from collections import Counter

def isAnagram(s, t):
    # time complexity O(s+t)
    # basically same as hash_solution
    return Counter(s) == Counter(t)

print(isAnagram(s="zanagram", t="nagaram"))