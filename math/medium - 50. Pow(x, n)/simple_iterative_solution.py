"""
Implement pow(x, n), which calculates x raised to the power n (i.e., xn).

Example 1:
Input: x = 2.00000, n = 10
Output: 1024.00000

Example 2:
Input: x = 2.10000, n = 3
Output: 9.26100

Example 3:
Input: x = 2.00000, n = -2
Output: 0.25000
Explanation: 2-2 = 1/22 = 1/4 = 0.25
"""

def myPow(x, n):
    # O (n) - does not pass leetcode test cases, O (log n) solution is needed

    orig_val = x
    if n > 0:
        for _ in range(0, n-1):
            x *= orig_val
    elif n < 0:
        for _ in range(0, abs(n) - 1):
            x *= orig_val
        x = 1 / x
    else:
        return 1

    return x

print(myPow(2,-2))
print(myPow(2.1,3))
print(myPow(0,5))
print(myPow(5,0))
# print(myPow(0.00001,2147483647))