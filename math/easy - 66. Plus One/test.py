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
    list = []
    result = []
    for digit in digits:
        list.append(str(digit))
    string = "".join(list)
    number = (int(string)+1)
    string = str(number)
    for character in string:
        result.append(int(character))
    return result


print(plusOne([9]))
print(plusOne([4, 3, 2, 1]))