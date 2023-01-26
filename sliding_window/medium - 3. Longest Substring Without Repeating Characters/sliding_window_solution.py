"""
Given a string s, find the length of the longest
substring without repeating characters.

Example 1:
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Example 2:
Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Example 3:
Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
"""

def lengthOfLongestSubstring(s):
    # create 2 pointers - i1 in "s" and i2 in "substring"
    # when same letter found -> i2 is moved to the right
    # substring length is calculated as substring[i2:]
    substring = []
    i1 = 0
    i2 = 0
    result = 0

    while i1 < len(s):
        # update result
        if len(substring[i2:]) > result:
            result = len(substring[i2:])

        # if same character is found in substring[i2:]
        if s[i1] in substring[i2:]:
            while substring[i2] != s[i1]:
                i2 += 1
            i2 += 1

        # append substring and move i1 to the right
        substring.append(s[i1])
        i1 += 1

    # before result is returned we need to update result one last time ouf of the loop
    if len(substring[i2:]) > result:
        result = len(substring[i2:])

    return result


print(lengthOfLongestSubstring("abcabcbb"))
print(lengthOfLongestSubstring("bbbbb"))
print(lengthOfLongestSubstring("pwwkew"))
print(lengthOfLongestSubstring(" "))
print(lengthOfLongestSubstring("dvdf")) # 3
print(lengthOfLongestSubstring("aabaab!bb")) # 3

