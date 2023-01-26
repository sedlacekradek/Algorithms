"""
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing
all non-alphanumeric characters, it reads the same forward and backward.
Alphanumeric characters include letters and numbers.
Given a string s, return true if it is a palindrome, or false otherwise.

Example 1:
Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.

Example 2:
Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.

Example 3:
Input: s = " "
Output: true
Explanation: s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.
"""


def isPalindrome(s):

    # convert to lower case and remove if not alphanumeric
    s = ''.join(char for char in s if char.isalnum()).lower()

    # edge cases
    if len(s) < 2:
        return True

    # initiate left and right pointer
    i1 = 0
    i2 = len(s) - 1

    # check if left and right pointers point at the same value
    while i1 < i2:
        # return False if not
        if s[i1] != s[i2]:
            return False
        i1 += 1
        i2 -= 1
    # return True if loop finished without returning False
    return True

print(isPalindrome("race a car"))
print(isPalindrome("A man, a plan, a canal: Panama"))
print(isPalindrome(" "))
print(isPalindrome("aa"))

