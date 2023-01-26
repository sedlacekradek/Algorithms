"""
You are given a large integer represented as an integer array digits, where each digits[i] is the
ith digit of the integer. The digits are ordered from most significant to least significant in left-to-right order.
The large integer does not contain any leading 0's.
Increment the large integer by one and return the resulting array of digits.

Example 1:

Input: digits = [4,3,2,1]
Output: [4,3,2,2]
Explanation: The array represents the integer 4321.
Incrementing by one gives 4321 + 1 = 4322.
Thus, the result should be [4,3,2,2].

Example 2:

Input: digits = [9]
Output: [1,0]
Explanation: The array represents the integer 9.
Incrementing by one gives 9 + 1 = 10.
Thus, the result should be [1,0].
"""


def plusOne(digits):

    result_list = []

    if len(digits) == 1:
        result = digits[0]+1
        for digit in str(result):
            result_list.append(int(digit))
        return result_list

    result = 0
    for digit in digits:
        result = result * 10
        result += digit
    result += 1
    for digit in str(result):
        result_list.append(int(digit))
    return result_list

print(plusOne([9]))
print(plusOne([4,3,2,1]))