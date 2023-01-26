"""
Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.
In other words, return true if one of s1's permutations is the substring of s2.

Example 1:
Input: s1 = "ab", s2 = "eidbaooo"
Output: true
Explanation: s2 contains one permutation of s1 ("ba").

Example 2:
Input: s1 = "ab", s2 = "eidboaoo"
Output: false
"""


def checkInclusion(s1, s2):
    # Input: s1 = "ab", s2 = "eidbaooo"
    # Output: true
    s1_hash_map = {}
    s2_hash_map = {}

    # populate s1 hash
    for character in s1:
        s1_hash_map[character] = s1_hash_map.get(character, 0) + 1

    i = 0
    # slide the window of size of len(s1) through s2
    while i + len(s1) <= len(s2):

        # for each character in the window
        for character in s2[i:i+len(s1)]:
            # if character not in s1, break out of loop
            if character not in s1:
                s2_hash_map = {}
                break
            # if character is in s1, increase the number of frequency in hash_map
            s2_hash_map[character] = s2_hash_map.get(character, 0) + 1
            # if character more times in s2 than in s1, break out of loop
            if s2_hash_map[character] > s1_hash_map[character]:
                s2_hash_map = {}
                break
        # now we know that both hash_maps must contain only the same values
        # and that no s2 value is too high
        # return true if sum if all values of both dictionaries are the same
        if sum(s1_hash_map.values()) == sum(s2_hash_map.values()):
            return True
        i += 1

    return False

print(checkInclusion(s1="ab", s2="eidbaooo"))
print(checkInclusion(s1="ab", s2="eidboaoo"))
print(checkInclusion(s1="adc", s2="dcda"))