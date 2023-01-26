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

    # edge case guard
    if len(s1) > len(s2):
        return False

    # create hashmaps with 26 letters as keys and 0 as values
    s1_hash_map = {}
    s2_hash_map = {}
    import string
    for letter in string.ascii_lowercase:
        s1_hash_map[letter] = 0
        s2_hash_map[letter] = 0

    # update s1_hash with frequency of letters in s1
    # update s2_hash with frequency of letters in the first len(s1) characters of the string
    match = 26
    for i in range(0, len(s1)):
        s1_hash_map[s1[i]] = s1_hash_map.get(s1[i]) + 1
        s2_hash_map[s2[i]] = s2_hash_map.get(s2[i]) + 1

    # compare the 2 hashes and for each mismatch decrease the number of matches
    # this is the only time we need to compare the whole dictionaries, from now on, we can only compare the changes
    for key in s1_hash_map:
        if s1_hash_map[key] != s2_hash_map[key]:
            match -= 1

    # iterate through s2 and if 26 matches found, return True
    left = 0
    right = len(s1)
    while right < len(s2):

        if match == 26:
            return True

        # decrease the frequency number in s2_hash for the letter marked by left pointer
        # check if it now matches, if it does, increase the match by +1
        # check if it  was matching before (= if the difference is just 1) and if it was, decrease the match count by -1
        s2_hash_map[s2[left]] = s2_hash_map.get(s2[left]) - 1
        if s2_hash_map[s2[left]] == s1_hash_map[s2[left]]:
            match += 1
        elif s2_hash_map[s2[left]] + 1 == s1_hash_map[s2[left]]:
            match -= 1

        # increase the frequency number in s2_hash for the letter marked by right pointer
        # check if it now matches, if it does, increase the match by +1
        # check if it  was matching before (= if the difference is just 1) and if it was, decrease the match count by -1
        s2_hash_map[s2[right]] = s2_hash_map.get(s2[right]) + 1
        if s2_hash_map[s2[right]] == s1_hash_map[s2[right]]:
            match += 1
        elif s2_hash_map[s2[right]] - 1 == s1_hash_map[s2[right]]:
            match -= 1

        # move both left and right pointers to the right by one space
        left += 1
        right += 1

    # last loop would not check for correct result
    # therefore we need to check one last time if condition met
    return match == 26



print(checkInclusion(s1="ab", s2="eidbaooo"))
print(checkInclusion(s1="ab", s2="eidboaoo"))
print(checkInclusion(s1="adc", s2="dcda"))