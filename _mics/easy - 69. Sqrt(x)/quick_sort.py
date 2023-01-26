"""
Given a non-negative integer x, return the square root of x rounded down to the nearest integer.
The returned integer should be non-negative as well.
You must not use any built-in exponent function or operator.
For example, do not use pow(x, 0.5) in c++ or x ** 0.5 in python.

Example 1:
Input: x = 4
Output: 2
Explanation: The square root of 4 is 2, so we return 2.

Example 2:
Input: x = 8
Output: 2
Explanation: The square root of 8 is 2.82842..., and since we round it down to the nearest integer, 2 is returned.

NOTES:
- basically looking for the first number that, if squared, is not bigger than X
- the largest possible number can be found by dividing X by 2
- then it is a problem of finding the number in a sorted array -> quick sort an option
"""


def mySqrt(x):
    # result cannot be bigger than x // 2
    max_number = x // 2
    # left pointer
    min = 1
    # right pointer
    max = max_number

    # edge cases
    if x == 1:
        return 1
    if x == 0:
        return 0

    # example of X and resulting array
    # 12
    # 1 2 3 4 5 6

    # quick sort
    while min <= max:
        # when max or min changed -> recalc middle
        middle = (max + min) // 2
        # if we can get exact result
        if middle * middle == x:
            return middle
        # if middle*middle > x -> we know that max possible result is middle - 1
        if (middle * middle) > x:
            max = middle-1
        # if middle*middle < x -> we know that max possible result is middle + 1
        if (middle * middle) < x:
            min = middle+1
            # return result only if lower, because we need to round down as per problem description
            result = middle
    return result

print(mySqrt(8))