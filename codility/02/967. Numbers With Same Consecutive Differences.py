"""
Given two integers n and k, return an array of all the integers of length n where the difference
between every two consecutive digits is k. You may return the answer in any order.
Note that the integers should not have leading zeros. Integers as 02 and 043 are not allowed.

Example 1:
Input: n = 3, k = 7
Output: [181,292,707,818,929]
Explanation: Note that 070 is not a valid number, because it has leading zeroes.

Example 2:
Input: n = 2, k = 1
Output: [10,12,21,23,32,34,43,45,54,56,65,67,76,78,87,89,98]
"""


def numsSameConsecDiff(N: int, k: int):

    # list all possible numbers - number for which we can apply +/- k and still by between 0 and 9
    possible = [i for i in range(1, 10) if (i + k < 10 or i - k >= 0)]

    # each iteration add one digit, we already have 1 digit, so we do not need to include N
    for position in range(1, N):
        res = []

        for i in range(len(possible)):
            if (1 <= possible[i] % 10 + k < 10):
                number = possible[i] * 10 + (possible[i] % 10 + k)
                res.append(number)

            if (0 <= possible[i] % 10 - k < 10):
                number = possible[i] * 10 + (possible[i] % 10 - k)
                # to avoid duplicate values, if this value is the same as the last value added, skip
                # first we check if res is not empty to avoid error when checking res[-1]
                if len(res) == 0 or number != res[-1]:
                    res.append(number)

        possible = res

    return res

print(numsSameConsecDiff(N = 3, k = 7))
print(numsSameConsecDiff(N = 2, k = 4))
print(numsSameConsecDiff(N = 2, k = 0))

# [929, 707, 292, 818, 181]
# [37, 40, 73, 15, 48, 51, 84, 26, 59, 62, 95]
# [33, 66, 99, 11, 44, 77, 22, 55, 88]

