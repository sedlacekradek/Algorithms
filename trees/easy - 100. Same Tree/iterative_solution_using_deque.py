"""
Given the roots of two binary trees p and q, write a function to check if they are the same or not.
Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

Example 1:
Input: p = [1,2,3], q = [1,2,3]
Output: true

Example 2:
Input: p = [1,2], q = [1,null,2]
Output: false

Example 3:
Input: p = [1,2,1], q = [1,1,2]
Output: false
"""


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        from collections import deque
        t1 = deque([p])
        t2 = deque([q])

        # edge cases
        if p is None and q is None:
            return True
        elif p is None or q is None:
            return False
        elif p.val != q.val:
            return False

        while t1 and t2:

            node1 = t1.popleft()
            node2 = t2.popleft()
            # if different values, False
            if node1.val != node2.val:
                return False
            # continue down the tree and add further values
            if node1.left and node2.left:
                t1.append(node1.left)
                t2.append(node2.left)
            if node1.right and node2.right:
                t1.append(node1.right)
                t2.append(node2.right)
            # if trees are not symmetrical, return False
            if not node1.left and node2.left or node1.left and not node2.left or not node1.right and node2.right or node1.right and not node2.right:
                return False

        return True