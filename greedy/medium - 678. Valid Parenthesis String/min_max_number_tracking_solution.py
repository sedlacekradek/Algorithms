"""
Given a string s containing only three types of characters: '(', ')' and '*', return true if s is valid.

The following rules define a valid string:
Any left parenthesis '(' must have a corresponding right parenthesis ')'.
Any right parenthesis ')' must have a corresponding left parenthesis '('.
Left parenthesis '(' must go before the corresponding right parenthesis ')'.
'*' could be treated as a single right parenthesis ')' or a single left parenthesis '(' or an empty string "".


Example 1:
Input: s = "()"
Output: true

Example 2:
Input: s = "(*)"
Output: true

Example 3:
Input: s = "(*))"
Output: true
"""


def checkValidString(s):
    # keeping track of max and min number of open left parentheses
    max_left = 0
    min_left = 0

    for c in s:
        # if a new left bracket, always increase the number of both max and min by 1
        if c == "(":
            max_left += 1
            min_left += 1
        # if right bracket, the number of open left brackets must be always decreased by 1
        if c == ")":
            max_left -= 1
            min_left -= 1
        # star can be both left and right bracket, therefore we keep track of both of these options
        if c == "*":
            max_left += 1
            min_left -= 1
       # min number can go under 0. if it does, just change it back to 0
        if min_left < 0:
            min_left = 0
        # max number can never be < 0, if it does, we can return False
        if max_left < 0:
            return False
    # check if it is possible that all left brackets have been closed
    return min_left == 0


print(checkValidString(s = "(*))"))
print(checkValidString(s = "(*)))"))
print(checkValidString(s = "((*))"))
print(checkValidString(s = "(*)("))
print(checkValidString(s = "(((((*(()((((*((**(((()()*)()()()*((((**)())*)*)))))))(())(()))())((*()()(((()((()*(())*(()**)()(())"))

