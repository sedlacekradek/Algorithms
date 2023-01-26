"""
Given the roots of two binary trees root and subRoot, return true if there is a subtree
of root with the same structure and node values of subRoot and false otherwise.
A subtree of a binary tree tree is a tree that consists of a node in tree and all of
this node's descendants. The tree tree could also be considered as a subtree of itself.

Example 1:
Input: root = [3,4,5,1,2], subRoot = [4,1,2]
Output: true

Example 2:
Input: root = [3,4,5,1,2,null,null,null,null,0], subRoot = [4,1,2]
Output: false
"""


def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

    # the order of the following 2 conditions is important
    # if subRoot is empty, automatically True
    if not subRoot:
        return True
    # if root empty and subRoot not empty, return False
    if not root:
        return False

    def same_tree(t1, t2):
        # compare 2 trees and return if they are the same
        if not t1 and not t2:
            return True
        if not t1 or not t2:
            return False
        if t1.val != t2.val:
            return False
        # recursively calls itself
        return same_tree(t1.left, t2.left) and same_tree(t1.right, t2.right)

    # if subTree found
    if same_tree(root, subRoot):
        return True

    # recursively calls itself
    return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)