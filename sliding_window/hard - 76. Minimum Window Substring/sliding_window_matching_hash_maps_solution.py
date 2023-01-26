"""
Given two strings s and t of lengths m and n respectively, return the minimum window
substring of s such that every character in t (including duplicates) is included in the window.
If there is no such substring, return the empty string "".

The testcases will be generated such that the answer is unique.

Example 1:
Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.

Example 2:
Input: s = "a", t = "a"
Output: "a"
Explanation: The entire string s is the minimum window.

Example 3:
Input: s = "a", t = "aa"
Output: ""
Explanation: Both 'a's from t must be included in the window.
Since the largest window of s only has one 'a', return empty string.
"""

def minWindow(s, t):
    # time complexity - O(n)

    # edge cases
    if t == "":
        return ""


    # hashmap to count matches
    hash_matches = {}

    # hashmap of frequency of letters in string t
    hash_t = {}
    for letter in t:
        hash_t[letter] = hash_t.get(letter, 0) + 1

    # length initialized with length infinity
    length = float("infinity")
    result = 0
    matching = 0
    # match_needed is same as number of entries in hash_t hashmap
    match_needed = len(hash_t)
    # left pointer
    lpointer = 0

    # i - right pointer
    for i in range(0, len(s)):

        # if right pointer find a letter that is in t
        if s[i] in t:
            # update hashmap
            hash_matches[s[i]] = hash_matches.get(s[i], 0) + 1
            # if frequency of this letter is the same in both dictionaries, +1 to the match counter
            if hash_matches[s[i]] == hash_t[s[i]]:
                matching += 1

        # if we found all letter we were looking for, shorten the string (move the left pointer) until this is
        # no longer true -> check the length of the resulting substring -> if length is shortest yet, update result
        while matching == match_needed:
            # counting length between 2 pointers -> (right_pointer - left_pointer + 1)
            if (i - lpointer + 1) < length:
                length = (i - lpointer + 1)
                result = s[lpointer:i+1]
            # update hash_matches if needed
            if s[lpointer] in hash_t:
                hash_matches[s[lpointer]] = hash_matches.get(s[lpointer]) - 1
                # if the frequency of a given letter is lower than we need, update the counter "matching"
                # the counter may stay the same even if the frequency lowered if the previous value was
                # higher than what we needed
                # e.g. counter for letter "a" was 3, but we only need 2
                if hash_matches[s[lpointer]] < hash_t[s[lpointer]]:
                    matching -= 1
            # left pointer one space to the right
            lpointer += 1

    # if result == 0, return an empty string as per description
    if result == 0:
        result = ""

    return result

print(minWindow(s = "ADOBECODEBANC", t = "ABC"))
print(minWindow(s = "a", t = "a"))
print(minWindow(s = "a", t = "aa"))
print(minWindow(s = "aa", t = "aa"))



