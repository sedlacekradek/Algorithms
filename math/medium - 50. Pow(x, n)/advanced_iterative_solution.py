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
    #O (log n) solution
    # 2^8 = 4^4
    # 2^9 = 2*4^4

    res = 1
    abs_n = abs(n)

    # edge case
    if n == 0:
        return 1

    while abs_n > 0:
        if abs_n % 2 == 1:
            res *= x
            abs_n -= 1
        else:
            x *= x
            abs_n = abs_n // 2

    if n > 0:
        return res

    if n < 0:
        return 1 / res


print(myPow(2,10))
print(myPow(2.1,3))
print(myPow(0,5))
print(myPow(5,0))
# print(myPow(0.00001,2147483647))