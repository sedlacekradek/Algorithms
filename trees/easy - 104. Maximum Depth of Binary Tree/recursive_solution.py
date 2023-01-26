"""
Given the root of a binary tree, return its maximum depth.
A binary tree's maximum depth is the number of nodes along the longest path
from the root node down to the farthest leaf node.

Example 1:
Input: root = [3,9,20,null,null,15,7]
Output: 3

Example 2:
Input: root = [1,null,2]
Output: 2
"""


def maxDepth(root):
    # O (n)

    # base case
    if root is None:
        return 0
    # do nto forget to add 1 at each step
    return 1 + max(maxDepth(root.left), maxDepth(root.right))
