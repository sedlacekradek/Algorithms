"""
Evaluate the value of an arithmetic expression in Reverse Polish Notation.
Valid operators are +, -, *, and /. Each operand may be an integer or another expression.
Note that division between two integers should truncate toward zero.
It is guaranteed that the given RPN expression is always valid.
That means the expression would always evaluate to a result, and there will not be any division by zero operation.

Example 1:
Input: tokens = ["2","1","+","3","*"]
Output: 9
Explanation: ((2 + 1) * 3) = 9

Example 2:
Input: tokens = ["4","13","5","/","+"]
Output: 6
Explanation: (4 + (13 / 5)) = 6

Example 3:
Input: tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
Output: 22
Explanation: ((10 * (6 / ((9 + 3) * -11))) + 17) + 5
= ((10 * (6 / (12 * -11))) + 17) + 5
= ((10 * (6 / -132)) + 17) + 5
= ((10 * 0) + 17) + 5
= (0 + 17) + 5
= 17 + 5
= 22
"""
def evalRPN(tokens):
    # time complexity O(n)
    # keep adding characters to result[] until an operator is found
    # when operator, pop the last 2 elements, carry out operation and append result
    # be careful with "/" and "-", the order of numbers is important here
    # the numbers must be reversed
    result = []

    for item in tokens:
        if item == "+":
            result.append(result.pop() + result.pop())
        elif item == "-":
            n2 = result.pop()
            n1 = result.pop()
            result.append(n1 - n2)
        elif item == "*":
            result.append(result.pop() * result.pop())
        elif item == "/":
            n2 = result.pop()
            n1 = result.pop()
            # division returns float, needs to be converted to int, which will also automatically truncate toward zero
            result.append(int(n1 / n2))
        else:
            # not to forget save items as int
            result.append(int(item))
    return result[0]


print(evalRPN(tokens=["4", "13", "5", "/", "+"]))
print(evalRPN(tokens=["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))
print(evalRPN(tokens=["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))