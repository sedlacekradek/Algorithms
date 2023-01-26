"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
An input string is valid if:
Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.

Example 1:
Input: s = "()"
Output: true

Example 2:
Input: s = "()[]{}"
Output: true

Example 3:
Input: s = "(]"
Output: false
"""

def isValid(s):
    pairs = {
        '[': ']',
        '{': '}',
        '(': ')'
    }
    stack = []

    for char in s:
        # if char one of keys in dict (= opening bracket), add in stack list
        if char in pairs:
            stack.append(char)
        # if a closing bracket
        # if stack is empty (i.e. closing bracket is not closing anything) return False
        # pairs[stack.pop()] returns closing bracket of the one in stack and removes the last addition to the list
        # if the closing bracket is not the correct one, return False
        elif len(stack) == 0 or pairs[stack.pop()] != char:
            return False
    # if stack empty -> all brackets have been closed -> return True
    # else returns False
    return len(stack) == 0
