"""
You are given a string s and an integer k. You can choose any character of the string and
change it to any other uppercase English character. You can perform this operation at most k times.
Return the length of the longest substring containing the same letter you can get after performing the above operations.

Example 1:
Input: s = "ABAB", k = 2
Output: 4
Explanation: Replace the two 'A's with two 'B's or vice versa.

Example 2:
Input: s = "AABABBA", k = 1
Output: 4
Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
The substring "BBBB" has the longest repeating letters, which is 4.
"""



def characterReplacement(s, k):
    # create a hashmap of all letters in a substring
    # if the substring is not higher than most frequent letter + k
        # increase the size of a substring
    # else
        # decrease the size of substring (left pointer to the right)
        # remove the leftmost letter from the frequency hash_map
    # when right pointer is at the end of string -> return length of the largest substring found

    hash_map = {}
    left_index = 0
    right_index = 0
    result = 0

    while right_index < len(s):
        hash_map[s[right_index]] = hash_map.get(s[right_index], 0) + 1
        if (right_index - left_index + 1) > max(hash_map.values()) + k:
            hash_map[s[left_index]] = hash_map.get(s[left_index]) - 1
            left_index += 1
        # important - update result before increasing the substring size!!!
        result = max(result, right_index - left_index + 1)
        right_index += 1
    return result




print(characterReplacement("AABABBA", k=1))
print(characterReplacement("ABAB", k=2))
print(characterReplacement("ABBB", k=2))


