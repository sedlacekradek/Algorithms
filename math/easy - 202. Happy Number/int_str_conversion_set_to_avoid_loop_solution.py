"""
Write an algorithm to determine if a number n is happy.
A happy number is a number defined by the following process:
Starting with any positive integer, replace the number by the sum of the squares of its digits.
Repeat the process until the number equals 1 (where it will stay), or it loops
endlessly in a cycle which does not include 1.
Those numbers for which this process ends in 1 are happy.
Return true if n is a happy number, and false if not.

Example 1:
Input: n = 19
Output: true
Explanation:
1^2 + 9^2 = 82
8^2 + 2^2 = 68
6^2 + 8^2 = 100
1^2 + 0^2 + 0^2 = 1

Example 2:
Input: n = 2
Output: false
"""

def isHappy(n):
    res = 0
    # create set of visited numbers, more efficient than a list
    visited = set()

    # loop until we revisit a number (which would mean we are in a loop) or until we get our result
    while res != 1 and res not in visited:
        visited.add(res)  # add, not append
        res = 0  # do not forget to reset the res variable
        # int -> str -> int conversion
        for digit in str(n):
            res += int(digit) ** 2
        n = res
    return res == 1

print(isHappy(19))
print(isHappy(2))