"""
Given a binary tree, determine if it is height-balanced

Example 1:
Input: root = [3,9,20,null,null,15,7]
Output: true

Example 2:
Input: root = [1,2,2,3,3,null,null,4,4]
Output: false

Example 3:
Input: root = []
Output: true
"""

class Solution(object):

    def __init__(self):
        # global result variable
        self.res = True

    def isBalanced(self, root):
        def maxDepth(root):
            # if end of tree
            if not root:
                return 0
            # count depth of left and right
            left = maxDepth(root.left)
            right = maxDepth(root.right)
            # if the difference > 1, change global to False
            if abs(left - right) > 1:
                self.res = False
            # return max of left and right and increase by 1
            return 1 + max(left, right)

        # call helper function and return global result
        maxDepth(root)
        return self.res
