# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode], lower=float("-inf"), upper=float("inf")) -> bool:
        if not root:
            return True
        # for left nodes always checks if they are not higher than the maximum val so far
        # for right nodes checks if they are not lower than minimum val so far
        if root.val >= upper or root.val <= lower:
            return False

        # update lower and upper values for left and right branches of the tree
        return self.isValidBST(root.left, lower, root.val) and self.isValidBST(root.right, root.val, upper)