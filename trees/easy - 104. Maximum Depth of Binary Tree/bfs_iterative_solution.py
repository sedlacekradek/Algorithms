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

    # edge case
    if root is None:
        return 0


    level = 0
    # import and use deque to be able to pop left
    from collections import deque
    que = deque([root])

    # iterate through tree levels
    while que:
        for _ in range(len(que)):
            # remove leftmost node
            node = que.popleft()
            # add its left child to the que
            if node.left:
                que.append(node.left)
            # add its right child to the que
            if node.right:
                que.append(node.right)
        # level 1 if there are still nodes in the que
        level += 1

    return level