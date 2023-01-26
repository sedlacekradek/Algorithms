"""
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

Implement the MinStack class:
MinStack() initializes the stack object.
void push(int val) pushes the element val onto the stack.
void pop() removes the element on the top of the stack.
int top() gets the top element of the stack.
int getMin() retrieves the minimum element in the stack.
You must implement a solution with O(1) time complexity for each function.

Example 1:
Input
["MinStack","push","push","push","getMin","pop","top","getMin"]
[[],[-2],[0],[-3],[],[],[],[]]
Output
[null,null,null,null,-3,null,0,-2]

Explanation
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin(); // return -3
minStack.pop();
minStack.top();    // return 0
minStack.getMin(); // return -2
"""

class MinStack(object):

    def __init__(self):
        # keeps all values
        self.stack = []
        # records the lowest value at each time a new value has been added
        self.min_val_stack = []

    def push(self, val):
        # when a new value is added, check if it becomes the lowest number in the stack
        # if true, append it to the min_val_stack, the [-1] value of min_val_stack will always be the
        # lowest value in the stack
        # if false, append min_val_stack with the currently lowest number
        if self.min_val_stack == [] or val < self.min_val_stack[-1]:
            self.min_val_stack.append(val)
        else:
            self.min_val_stack.append(self.min_val_stack[-1])
        self.stack.append(val)

    def pop(self):
        # not forget to remove also the last value from min_val
        self.min_val_stack.pop()
        return self.stack.pop()

    def top(self):
        return self.stack[-1]

    def getMin(self):
        # returns the current lowest value
        return self.min_val_stack[-1]


obj = MinStack()
obj.push(5)
obj.push(-3)
print(obj.pop())
print(obj.getMin())
param_3 = obj.top()
param_4 = obj.getMin()